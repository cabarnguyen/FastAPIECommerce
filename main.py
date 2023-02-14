'''setup project
pip freeze > requirements.txt
'''
from ecommerce.user import router as user_router

from fastapi import FastAPI

app = FastAPI(title="EcommerceApp",
              version="0.0.1")

app.include_router(user_router.router)

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}
#
# @app.get("/hello/{name}")
# async def say_hello(name: int):
#     return {"message": f"Hello {name}"}

# @app.get("/customer")
# async def read_customers():
#     return  db.retrieve_customers()