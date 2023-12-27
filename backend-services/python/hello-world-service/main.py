from fastapi import FastAPI
from application.services.hello_world_service import HelloWorldService

app = FastAPI()
hello_world_service = HelloWorldService()  

@app.get('/api/v1/hws', status_code=200)
async def hello():
    return {"message": hello_world_service.get_hello_world_message()}