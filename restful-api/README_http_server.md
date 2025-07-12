# Simple HTTP Server

A basic HTTP server implementation using Python's `http.server` module.

## Features

- ✅ Basic HTTP server setup using `http.server.BaseHTTPRequestHandler`
- ✅ Multiple endpoints with different response types
- ✅ JSON data serving with proper content-type headers
- ✅ Error handling for undefined endpoints (404)
- ✅ Clean logging and server management

## Endpoints

| Endpoint | Method | Response | Content-Type |
|----------|--------|----------|--------------|
| `/` | GET | "Hello, this is a simple API!" | text/plain |
| `/data` | GET | `{"name": "John", "age": 30, "city": "New York"}` | application/json |
| `/status` | GET | "OK" | text/plain |
| `/info` | GET | `{"version": "1.0", "description": "A simple API built with http.server"}` | application/json |
| Any other | GET | "Endpoint not found" (404) | text/plain |

## Usage

### 1. Start the Server

```bash
python3 simple_http_server.py
```

The server will start on `http://localhost:8000`

### 2. Test with Browser

Open your browser and visit:
- `http://localhost:8000` - Welcome message
- `http://localhost:8000/data` - JSON data
- `http://localhost:8000/status` - Status check
- `http://localhost:8000/info` - API information

### 3. Test with curl

```bash
# Test root endpoint
curl http://localhost:8000/

# Test data endpoint
curl http://localhost:8000/data

# Test status endpoint
curl http://localhost:8000/status

# Test info endpoint
curl http://localhost:8000/info

# Test undefined endpoint (should return 404)
curl http://localhost:8000/nonexistent
```

### 4. Test with Python Script

```bash
# Install requests if not already installed
pip install requests

# Run the test script
python3 test_server.py
```

## Expected Output

### Server Output:
```
Server started at http://localhost:8000
Available endpoints:
  - / (root) - Returns welcome message
  - /data - Returns JSON data
  - /status - Returns API status
  - /info - Returns API information
  - Any other path returns 404

Press Ctrl+C to stop the server
```

### Browser/curl Output:
- `/` → "Hello, this is a simple API!"
- `/data` → `{"name": "John", "age": 30, "city": "New York"}`
- `/status` → "OK"
- `/info` → `{"version": "1.0", "description": "A simple API built with http.server"}`
- `/nonexistent` → "Endpoint not found" (404 status)

## Key Implementation Details

1. **HTTP Handler**: Extends `http.server.BaseHTTPRequestHandler`
2. **Routing**: Uses `self.path` to route requests to different endpoints
3. **Headers**: Properly sets content-type headers for different response types
4. **JSON**: Uses `json.dumps()` to convert Python dictionaries to JSON strings
5. **Error Handling**: Returns 404 for undefined endpoints
6. **Logging**: Custom log message format for cleaner output

## Files

- `simple_http_server.py` - Main server implementation
- `test_server.py` - Test script to verify all endpoints
- `README_http_server.md` - This documentation 