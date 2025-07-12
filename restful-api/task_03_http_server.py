def do_GET(self):
    """
    Handle GET requests for different endpoints
    """
    if self.path == '/':
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        response = "Hello, this is a simple API!"
        self.wfile.write(response.encode('utf-8'))

    elif self.path == '/data':
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        data = {
            "name": "John",
            "age": 30,
            "city": "New York"
        }
        response = json.dumps(data)
        self.wfile.write(response.encode('utf-8'))

    elif self.path == '/status':
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        response = "OK"
        self.wfile.write(response.encode('utf-8'))

    elif self.path == '/info':
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        info = {
            "version": "1.0",
            "description": "A simple API built with http.server"
        }
        response = json.dumps(info)
        self.wfile.write(response.encode('utf-8'))

    else:
        self.send_response(404)
        self.send_header('Content-type', 'text/plain')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

        response = "Endpoint not found"
        self.wfile.write(response.encode('utf-8'))