"""Python server: standalone reference and practice project."""

from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = b"local teaching server"
        self.send_response(200)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
print("Bound only to loopback on port", server.server_port)
server.server_close()
