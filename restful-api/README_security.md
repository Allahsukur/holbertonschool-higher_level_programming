# Secure Flask API with Authentication and Authorization

This project implements a secure Flask API with comprehensive authentication and authorization mechanisms, including Basic HTTP Authentication, JWT (JSON Web Token) authentication, and role-based access control.

## Features

- **Basic HTTP Authentication**: Simple username/password authentication
- **JWT Authentication**: Token-based authentication for stateless sessions
- **Role-based Access Control**: Different access levels for users and admins
- **Password Hashing**: Secure password storage using Werkzeug security
- **Comprehensive Error Handling**: Proper HTTP status codes for all authentication errors

## Installation

1. Install the required dependencies:
```bash
pip install -r requirements.txt
```

2. Run the Flask application:
```bash
python task_05_basic_security.py
```

The API will be available at `http://localhost:5000`

## API Endpoints

### Public Endpoints

- `GET /` - Welcome message
- `POST /login` - JWT login endpoint

### Protected Endpoints

#### Basic Authentication
- `GET /basic-protected` - Requires Basic HTTP Authentication

#### JWT Authentication
- `GET /jwt-protected` - Requires valid JWT token
- `GET /users` - List all users (requires JWT)
- `GET /profile` - Get current user profile (requires JWT)

#### Role-based Access
- `GET /admin-only` - Admin-only access (requires JWT with admin role)

## Usage Examples

### 1. Basic Authentication

```bash
# Without credentials (will fail)
curl http://localhost:5000/basic-protected

# With valid credentials
curl -u user1:password http://localhost:5000/basic-protected
```

### 2. JWT Authentication

```bash
# Login to get JWT token
curl -X POST http://localhost:5000/login \
  -H "Content-Type: application/json" \
  -d '{"username": "user1", "password": "password"}'

# Use JWT token to access protected endpoint
curl -H "Authorization: Bearer <your_jwt_token>" \
  http://localhost:5000/jwt-protected
```

### 3. Role-based Access

```bash
# Login as admin
curl -X POST http://localhost:5000/login \
  -H "Content-Type: application/json" \
  -d '{"username": "admin1", "password": "password"}'

# Access admin-only endpoint
curl -H "Authorization: Bearer <admin_jwt_token>" \
  http://localhost:5000/admin-only
```

## User Credentials

The API comes with pre-configured users:

- **Regular User**: `user1` / `password` (role: user)
- **Admin User**: `admin1` / `password` (role: admin)

## Security Features

### Password Security
- Passwords are hashed using Werkzeug's `generate_password_hash()`
- Password verification uses `check_password_hash()`
- No plain-text passwords are stored

### JWT Security
- Tokens include user role information
- Proper error handling for expired, invalid, and missing tokens
- All authentication errors return 401 status code

### Role-based Access Control
- Users have assigned roles (user/admin)
- Admin-only endpoints check for admin role
- Non-admin users get 403 Forbidden for admin endpoints

## Error Handling

The API implements comprehensive error handling:

- **401 Unauthorized**: Missing or invalid authentication
- **403 Forbidden**: Insufficient permissions (role-based)
- **400 Bad Request**: Invalid request data

### JWT Error Types
- Missing or invalid token
- Expired token
- Revoked token
- Fresh token required

## Testing

Run the comprehensive test suite:

```bash
python test_secure_api.py
```

This will test:
- Basic authentication with valid/invalid credentials
- JWT authentication flow
- Role-based access control
- Error handling for various scenarios

## Security Best Practices

1. **Change the JWT Secret Key**: In production, replace `'your-secret-key-change-in-production'` with a strong, unique secret key.

2. **Use HTTPS**: Always use HTTPS in production to encrypt data in transit.

3. **Token Expiration**: Consider implementing token expiration for enhanced security.

4. **Rate Limiting**: Implement rate limiting to prevent brute force attacks.

5. **Input Validation**: Add comprehensive input validation for all endpoints.

6. **Database Storage**: Replace in-memory storage with a secure database in production.

## File Structure

```
restful-api/
├── task_05_basic_security.py    # Main secure Flask API
├── test_secure_api.py           # Comprehensive test suite
├── requirements.txt             # Python dependencies
└── README_security.md          # This documentation
```

## Dependencies

- Flask >= 2.0.0
- Flask-HTTPAuth >= 4.0.0
- Flask-JWT-Extended >= 4.0.0
- Werkzeug (included with Flask)

## Learning Objectives

After completing this exercise, you should understand:

1. **API Security Importance**: Why authentication and authorization are crucial
2. **Basic Authentication**: How HTTP Basic Auth works and its limitations
3. **JWT Authentication**: Token-based authentication for stateless APIs
4. **Role-based Access Control**: Implementing different permission levels
5. **Password Security**: Proper password hashing and verification
6. **Error Handling**: Consistent error responses for security scenarios

## Next Steps

Consider implementing these additional security features:

- Token refresh mechanism
- Password reset functionality
- Account lockout after failed attempts
- Audit logging
- CORS configuration
- API rate limiting 