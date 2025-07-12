#!/usr/bin/python3
"""
Simple HTTP Server using Python's http.server module
"""
import json
import http.server
import socketserver


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """
    Custom HTTP request handler for the simple API
    """
    
    def do_GET(self):
        """
        Handle GET requests for different endpoints
        """
        # Set default headers
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        # Route requests based on path
        if self.path == '/':
            # Root endpoint
            response = "Hello, this is a simple API!"
            self.wfile.write(response.encode('utf-8'))
            
        elif self.path == '/data':
            # JSON data endpoint
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            response = json.dumps(data)
            self.wfile.write(response.encode('utf-8'))
            
        elif self.path == '/status':
            # Status endpoint
            response = "OK"
            self.wfile.write(response.encode('utf-8'))
            
        elif self.path == '/info':
            # Info endpoint
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            response = json.dumps(info)
            self.wfile.write(response.encode('utf-8'))
            
        else:
            # 404 Not Found for undefined endpoints
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            
            response = "Endpoint not found"
            self.wfile.write(response.encode('utf-8'))
    
    def log_message(self, format, *args):
        """
        Override log_message to provide cleaner logging
        """
        print(f"[{self.address_string()}] {format % args}")


def run_server(port=8000):
    """
    Start the HTTP server on the specified port
    """
    with socketserver.TCPServer(("", port), SimpleAPIHandler) as httpd:
        print(f"Server started at http://localhost:{port}")
        print("Available endpoints:")
        print("  - / (root) - Returns welcome message")
        print("  - /data - Returns JSON data")
        print("  - /status - Returns API status")
        print("  - /info - Returns API information")
        print("  - Any other path returns 404")
        print("\nPress Ctrl+C to stop the server")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nServer stopped.")


if __name__ == "__main__":
    run_server() 