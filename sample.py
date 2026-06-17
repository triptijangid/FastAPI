from fastapi import FastAPI
from enum import Enum

app = FastAPI()

fake_orders_db = {
    "ORD-201": {"status": "shipped",     "city": "Delhi",     "amount": 3200, "delivery_days": 2},
    "ORD-202": {"status": "in_progress", "city": "Mumbai",    "amount": 1500, "delivery_days": 5},
    "ORD-203": {"status": "delivered",   "city": "Bangalore", "amount": 900,  "delivery_days": 1},
    "ORD-204": {"status": "shipped",     "city": "Chennai",   "amount": 4100, "delivery_days": 3},
    "ORD-205": {"status": "in_progress", "city": "Hyderabad", "amount": 620,  "delivery_days": 6},
}

# TODO: Define OrderStatus Enum with members: shipped, in_progress, delivered
class OrderStatus(str, Enum):
    shipped = "shipped"
    in_progress = "in_progress"
    delivered = "delivered"

# TODO: Implement GET /orders/{order_id}
# Return the full order dict or a "not found" message

@app.get("/orders/{order_id}")
def get_order(order_id: str):
    order = fake_orders_db.get(order_id)

    if not order:
        return f"No order found for order ID {order_id}"
    
    return order

# TODO: Implement GET /orders/{order_id}/{key}
# Return the value for the key, or descriptive error messages for missing order/key

@app.get("/orders/{order_id}/{key}")
def get_order_field(order_id : str, key: str):
    order = fake_orders_db.get(order_id)

    if not order:
        return f"No order found for order ID {order_id}"
    
    try:
        value = order[key]
        return value
    except KeyError:
        return f"No valid field called {key} found for the order."

# TODO: Implement GET /orders with required `status` query parameter (OrderStatus type)
# Return a list of matching order dicts
@app.get("/orders")
def get_orders(status: OrderStatus):
    return [
        order 
        for order in fake_orders_db.values()
        if order["status"] == status.value
    ]
