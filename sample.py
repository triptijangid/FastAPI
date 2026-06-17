from fastapi import FastAPI
app = FastAPI()

@app.get("/hello")
def say_hello():
    return "Hi, World"

@app.get("/orders/{order_id}")
def order_details(order_id: str):
    return {"Order_id " : order_id}
