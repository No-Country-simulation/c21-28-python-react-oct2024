 #!/usr/bin/python3

from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
import time
import json
import threading

hostName = “0.0.0.0”
serverPort = 80
 
class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
if __name__ == “__main__”:
 webServer = ThreadedHTTPServer((hostName, serverPort), Handler)
 print(“Server started http://%s:%s" % (hostName, serverPort))
try:
 webServer.serve_forever()
 except KeyboardInterrupt:
 pass
webServer.server_close()
 print(“Server stopped.”)