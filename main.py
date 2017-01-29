
import webapp2
import cgi

def build_page(textarea_content):
    userlable="<label>Username</label>"
    userarea = "<textarea name='username'>"+textarea_content+"</textarea>"
    usersection = userlable+userarea+"<br>"
    
    passlable="<label>Password</label>"
    passarea = "<textarea name='password'>"+textarea_content+"</textarea>"
    passsection = passlable+passarea+"<br>"


    verifylable="<label>Verify Password</label>"
    verifyarea = "<textarea name='verify'>"+textarea_content+"</textarea>"
    verifysection = verifylable+verifyarea+"<br>"

    emaillable="<label>Email (optional)</label>"
    emailarea = "<textarea name='email'>"+textarea_content+"</textarea>"
    emailsection = emaillable+emailarea+"<br>"
    
        
    header = "<h1>Signup</h1>"
    submit = "<input type='submit'/>"
    form = "<form method='post'>"+usersection+passsection+verifysection+emailsection+"<br>"+submit+"</form>"
    return header+form

class MainHandler(webapp2.RequestHandler):
    def get(self):
        content = build_page("")
        self.response.write(content)
        
    def post(self):

        self.response.write(content)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
