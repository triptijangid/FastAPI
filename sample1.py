from fastapi import FastAPI, Depends, HTTPException
from enum import Enum

app = FastAPI()

ORDERS = {
    "ORD-101": {
        "status": "shipped",
        "city": "Delhi",
        "amount": 2500,
        "delivery_days": 2
    },
    "ORD-102": {
        "status": "cancelled",
        "city": "Bangalore",
        "amount": 4000,
        "delivery_days": 0
    },
    "ORD-103": {
        "status": "delivered",
        "city": "Mumbai",
        "amount": 1500,
        "delivery_days": 0
    }
}

@app.get("/hello")
def say_hello():
    return "Hello Everyone"

@app.get("/hi")
def say_hello():
    return "hi Everyone"

@app.get("/orders/{order_id:}")
def get_order_details(order_id: str):
    order = ORDERS.get(order_id)
    if not order:
        return f"No order found for the order id: {order_id}."
    return order

@app.get("/orders/{order_id}/{key}")
def get_order_field(order_id: str, key: str):
    order = ORDERS.get(order_id)
    if not order:
        return f"No order found for the order_id: {order_id}"
    
    try:
        value = order[key]
        return value
    except KeyError:
        return f"No valid field called {key} is found."
    
class FuelType(str, Enum):
    petrol = "petrol"
    diesel = "diesel"
    ev = "ev"
    cng = "cng"

@app.get("/fuel/{type}")
def get_fuel_type(type: FuelType):
    return {"fuel_type": type}

def verify_token(token: str):
    if len(token) < 5:
        raise HTTPException(status_code=401, detail="Invalid credentials.")
    
    print("Token Valid.")

@app.get("/myorders/{token}")
def get_all_orders(token: str = Depends(verify_token)):
    return "All order details"

def pagination(page_number: int = 9, limit: int = 20):
    return {"page_number": page_number, "limit": limit}

@app.get("/lists")
def list_products(page: dict = Depends(pagination)):
    return {"page_number": page["page_number"], "limit": page["limit"]}