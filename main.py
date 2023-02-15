'''setup project
pip freeze > requirements.txt
'''
import uvicorn
from fastapi.openapi.docs import get_swagger_ui_html

from ecommerce.customer import router as customer_router
from ecommerce.inventory import router as inventory_router
from ecommerce.user import router as user_router

from fastapi import FastAPI

app = FastAPI(title="EcommerceApp",
              version="0.0.1")

app.include_router(user_router.router)
app.include_router(inventory_router.router)
app.include_router(customer_router.router)

if __name__ == "__main__":
    uvicorn.run(app)
