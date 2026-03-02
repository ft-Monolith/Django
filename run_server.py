#!/usr/bin/env python3
from http.server import HTTPServer, SimpleHTTPRequestHandler
import os

os.chdir('Django-0-Initiation')
server_address = ('', 8000)
httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
print("Server running at http://localhost:8000")
print("Press Ctrl+C to stop")
try:
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped")
