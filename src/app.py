from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import socket

hostName = socket.gethostname()
hostPort = 8080
message = "Hello Python"

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        flag=False
        if self.path=="/healthz":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html>ok</html>", "utf-8"))
        else:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes("<html><head><title>Hello Python</title></head>", "utf-8"))
            self.wfile.write(bytes("<body><p><h1>Hello, This is your hello-python web-service</h1></p>", "utf-8"))
            self.wfile.write(bytes("<p><b>URL-Path: </b>%s</p>" % self.path, "utf-8"))
            self.wfile.write(bytes("<p><b>Hostname: </b>%s</p>" % hostName, "utf-8"))
            self.wfile.write(bytes("<p><b>Message: </b>%s</p>" % message, "utf-8"))
            self.wfile.write(bytes("<hr/><br/>", "utf-8"))
            self.wfile.write(bytes("<table><tr><th>Header</th><th>Value</th></tr>", "utf-8"))
            for key,val in self.headers.items():
              if not flag:
                self.wfile.write(bytes("<tr>","utf-8"))
                flag=True
              self.wfile.write(bytes("<td>%s</td>"   % key,"utf-8"))
              self.wfile.write(bytes("<td>%s</td>\n" % val,"utf-8"))
              if flag:
                self.wfile.write(bytes("</tr>\n","utf-8"))
                flag=False
            self.wfile.write(bytes("</table>", "utf-8"))
            print("GET request, Path:",str(self.path),",Headers:\n", str(self.headers))
            self.wfile.write(bytes("</body></html>", "utf-8"))

myServer = HTTPServer(('', hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))