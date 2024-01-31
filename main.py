from fastapi import FastAPI 
from users import router_users

app = FastAPI() 
 
app.include_router(router_users, prefix="/api", tags=["api"])

@app.get("/") 
def read_root(): 
   return {"Hello": "World"} 
