# We need to import request to access the details of the POST request
# and render_template, to render our templates (form and response)
# we'll use url_for to get some URLs for the app on the templates
from flask import Flask, render_template, request, url_for
# nlp = __import__(input('nlp'))
from nlp import *
# Initialize the Flask application
app = Flask(__name__)

# Define a route for the default URL, which loads the form
@app.route('/')
def form():
    return render_template('index.html')

# Define a route for the action of the form, for example '/hello/'
# We are also defining which type of requests this route is
# accepting: POST requests in this case
@app.route('/similarity/', methods=['POST'])
def similarity():
    print("Hi it hit me at post /similarity")
    name=request.form['string1']
    email=request.form['string2']
    return render_template('form_action.html', name=name, email=email)

# Run the app :)
if __name__ == '__main__':
  app.run(
        host="0.0.0.0",
        port=int("8080")
  )



# # This class will handles any incoming request from
# # the browser
# class RequestHandler(BaseHTTPRequestHandler):
#
#     # Handler for the GET requests
#     def do_GET(self):
#         if self.path == "/":
#             self.path = "/index.html"
#
#         try:
#             # Check the file extension required and
#             # set the right mime type
#
#             sendReply = False
#             if self.path.endswith(".html"):
#                 mimetype = 'text/html'
#                 sendReply = True
#             if self.path.endswith(".jpg"):
#                 mimetype = 'image/jpg'
#                 sendReply = True
#             if self.path.endswith(".gif"):
#                 mimetype = 'image/gif'
#                 sendReply = True
#             if self.path.endswith(".js"):
#                 mimetype = 'application/javascript'
#                 sendReply = True
#             if self.path.endswith(".css"):
#                 mimetype = 'text/css'
#                 sendReply = True
#
#             if sendReply == True:
#                 # Open the static file requested and send it
#                 f = open(curdir + sep + self.path)
#                 self.send_response(200)
#                 self.send_header('Content-type', mimetype)
#                 self.end_headers()
#                 self.wfile.write(f.read())
#                 f.close()
#             return
#
#         except IOError:
#             self.send_error(404, 'File Not Found: %s' % self.path)
#
#     #USE THIS OJASH
#     # Handler for the POST requests
#     def do_POST(self):
#         form = cgi.FieldStorage(fp=self.rfile, headers=self.headers, environ= {
#                 'REQUEST_METHOD' : 'POST',
#                 'CONTENT_TYPE': self.headers['Content-Type']
#             })
#
#         if self.path == "/similarity":
#
#             threshold = form['threshold'].value
#             q1 = form['string1'].value
#             q2 = form['string2'].value
#             q2 = q2.split('%')
#             print(q2)
#             result = basic_paraphrase_recognizer(q1, q2, threshold)
#             self.send_response(200)
#             self.end_headers()
#             print('result is')
#             print(result)
#             self.wfile.write(str(result).encode())
#             return
#
#
# try:
#     # Create a web server and define the handler to manage the
#     # incoming request
#     server = HTTPServer(('', PORT_NUMBER), RequestHandler)
#     ##print 'Started httpserver on port ', PORT_NUMBER
#
#     # Wait forever for incoming htto requests
#     server.serve_forever()
#
# except KeyboardInterrupt:
#     print('^C received, shutting down the web server')
#     server.socket.close()

