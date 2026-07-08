###let's create my dream cafe's menu:
from fastapi import FastAPI
menu= FastAPI()
@menu.get("/menu/{type_of_drink}/}")

def get_order(type_of_drink):
    return f("Place Your order{type_of_drink} ")