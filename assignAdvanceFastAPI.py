from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# TODO: Add CORSMiddleware via app.add_middleware(...)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:3000"],
    allow_methods = ["GET", "POST"],
    allow_credentials = True,
    allow_headers = ["*"]
)

# TODO: Add middleware using @app.middleware("http")
# async def log_requests(request: Request, call_next):
#     ...
@app.middleware("http")
async def log_requests(request: Request, call_next):
    print("Base URL:", request.base_url)
    print("Query Params:", request.query_params)

    response = await call_next(request)
    return response

# TODO: Write verify_token dependency
def verify_token(token: str):
    if len(token) < 5:
        raise HTTPException(status_code=401, detail="invalid credentials")
    return token

# TODO: Write pagination dependency
def pagination(skip: int = 0, limit: int = 10):
    
    return {
        "skip": skip,
        "limit": limit
    }

# TODO: Wire verify_token into the /orders/{token} route
@app.get("/orders/{token}")
def get_all_orders(token: str = Depends(verify_token)):
    return {
        "status": "ok", "orders": "all order details"
    }

# TODO: Wire pagination into the /products route
@app.get("/products")
def list_products(page: dict = Depends(pagination)):
    return {
        "page_number": page["skip"], "limit": page["limit"]
    }
