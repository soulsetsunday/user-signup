import webapp2
import cgi
import re

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$")

def valid_username(username):
    return USER_RE.match(username)
    
def valid_password(password):
    return PASS_RE.match(password)

def valid_email(email):
    return EMAIL_RE.match(email)

class MainHandler(webapp2.RequestHandler):
    def build_page(self, user_name_entered="", email_entered="", errors=['','','','','']):
        userlable="<label>Username</label>"
        #userarea = "<input type='text' name='username' value ="+user_name_entered+">"
        userarea="<textarea name = 'username' rows='1' cols='20'>"+user_name_entered+"</textarea>"
        
        error_element_noname = ""
        if errors[0]:
            error_element_noname ="<div style='display:inline;color:red' class='error'>{0}</div>".format(*errors)
        error_element_invalid = ""
        if errors[1]:
            error_element_invalid ="<div style='display:inline;color:red' class='error'>{1}</div>".format(*errors)
        usersection = userlable+userarea+error_element_noname+error_element_invalid+"<br>"
        
        #for passwords, use input instead of textarea
        #input is a void tag
        passlable="<label>Password</label>"
        passarea = "<input name='password' type='password'>"
        
        error_element_invalid_pass = ""
        if errors[2]:
            error_element_invalid_pass ="<div style='display:inline;color:red' class='error'>{2}</div>".format(*errors)    
        passsection = passlable+passarea+error_element_invalid_pass+"<br>"


        verifylable="<label>Verify Password</label>"
        verifyarea = "<input name='verify' type='password'>"+"</input>"
        
        error_element_verify = ""
        if errors[3]:
            error_element_verify ="<div style='display:inline;color:red' class='error'>{3}</div>".format(*errors)
        verifysection = verifylable+verifyarea+error_element_verify+"<br>"


        emaillable="<label>Email (optional)</label>"
        #emailarea = "<input name='email' value="+email_entered+">"
        emailarea = "<textarea name = 'email'  rows='1' cols='20'>"+email_entered+"</textarea>"
        
        error_element_email = ""
        if errors[4]:
            error_element_email ="<div style='display:inline;color:red' class='error'>{4}</div>".format(*errors)
        emailsection = emaillable+emailarea+error_element_email+"<br>"
        
            
        header = "<h1>Signup</h1>"
        submit = "<input type='submit'/>"
        form = "<form method='post'>"+usersection+passsection+verifysection+emailsection+"<br>"+submit+"</form>"
        return header+form
    
    def get(self):
        content = self.build_page()
        self.response.write(content)

    def check_errors(self, username, email):
        enter_name_error=""
        valid_name_error=""
        valid_pass_error=""
        pass_mismatch_error=""
        valid_email_error=""
        if self.request.get("username") == "":
            enter_name_error="Please enter a name."
        elif not (valid_username(username)):
            valid_name_error="Invalid name."
        if not (valid_password(self.request.get("password"))):
            valid_pass_error="Invalid password"
        if not self.request.get("password") == self.request.get("verify"):
            pass_mismatch_error="The passwords don't match."
        if email != "":
            if not (valid_email(email)):
                valid_email_error="Please enter a valid email or leave blank"
        
        if enter_name_error == valid_name_error == valid_pass_error == pass_mismatch_error == valid_email_error:
            self.redirect("/welcome?username="+username)
        return (enter_name_error, valid_name_error, valid_pass_error, pass_mismatch_error, valid_email_error)

        
    def post(self):
        username=self.request.get("username")
        escaped_username = cgi.escape(username)
        email=self.request.get("email")
        escaped_email = cgi.escape(email)
        errors = self.check_errors(escaped_username, escaped_email)
        content=self.build_page(escaped_username, escaped_email, errors)

        self.response.write(content)
        
class WelcomeHandler(webapp2.RequestHandler):
    def get(self):
        username = self.request.get("username")
        self.response.write("Welcome, "+username+"!")

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/welcome', WelcomeHandler)
], debug=True)
