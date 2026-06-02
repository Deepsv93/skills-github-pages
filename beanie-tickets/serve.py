#!/usr/bin/env python3
"""Simple local server for the Beanie Ticket Generator."""
import http.server, socketserver, os, webbrowser, threading

PORT = 8787
DIR  = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *a, **kw):
        super().__init__(*a, directory=DIR, **kw)
    def log_message(self, *_):
        pass   # quiet

def open_browser():
    import time; time.sleep(0.5)
    webbrowser.open(f'http://localhost:{PORT}')

threading.Thread(target=open_browser, daemon=True).start()
print(f"Beanie Ticket Generator running at http://localhost:{PORT}")
print("Press Ctrl+C to stop.")
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
