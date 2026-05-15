# E-Commerce API - PR-DR Demo

Real-world REST API for testing GitHub to PR-DR deployment pipeline.

## API Endpoints

### GET /
- Returns API information and available endpoints

### GET /health
- Health check endpoint with timestamp

### GET /users
- Get all users

### GET /users/<id>
- Get specific user by ID

### GET /orders
- Get all orders

### POST /orders
- Create new order
- Body: `{"user_id": 1, "product": "Laptop", "amount": 999.99}`

### GET /info
- Deployment and version information

## Test Commands
```bash
curl http://localhost:8080/
curl http://localhost:8080/health
curl http://localhost:8080/users
curl http://localhost:8080/users/1
curl http://localhost:8080/orders
curl -X POST http://localhost:8080/orders -H "Content-Type: application/json" -d '{"user_id":1,"product":"Laptop","amount":999.99}'
```
