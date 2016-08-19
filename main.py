import webapp2
from caesar import encrypt

header = """
<!DOCTYPE html>
<html>
<head>
    <title>Caesar</title>
    <style type="text/css">
        form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
        textarea {
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
    </style>
</head>
<body>
"""

footer = """
</body>
</html>
"""

main_html = """
<form action="/rot13" method="post">
    <label>Rotate by:</label>
    <input type="text" name="rot" value="{0}">
    <textarea name="text">{1}</textarea>
    <br>
    <input type="submit">
</form>
"""


class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        return self.response.write(*a, **kw)


class Main(Handler):
    def get(self):
        self.write(header + main_html.format('0','') + footer)


class Rot13(Handler):
    def post(self):
        rot = int(self.request.get('rot'))
        text = self.request.get('text')
        rotText = encrypt(text, rot)
        self.write(header + main_html.format(rot, rotText) + footer)


app = webapp2.WSGIApplication([
    ('/', Main),
    ('/rot13', Rot13),
], debug=True)
