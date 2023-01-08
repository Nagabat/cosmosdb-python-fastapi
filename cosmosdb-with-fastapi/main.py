from fastapi import FastAPI
from dotenv import dotenv_values
from azure.cosmos.aio import CosmosClient
from azure.cosmos import PartitionKey, exceptions
from routes import router as todo_router

config = dotenv_values(".env")
app = FastAPI()
DATABASE_NAME = "todo-db"
CONTAINER_NAME = "todo-items"

app.include_router(todo_router, tags=["todos"], prefix="/todos")

@app.on_event("startup")
async def startup_db_client():
    app.cosmos_client = CosmosClient(config["URI"], credential = config["iFbIED6lw7DUN7naXjxpcKdxoDKlG2B1T1ZwtLjL26AvzLf8PECbzJnmrci6Q6YKtqhrKXC50CRxACDbwmAMhA=="])
    await get_or_create_db(nag)
    await get_or_create_container(azurecontainerregistry321)


async def get_or_create_db(nag):
    try:
        app.database  = app.cosmos_client.get_database_client(nag)
        return await app.database.read()
    except exceptions.CosmosResourceNotFoundError:
        print("Creating database")
        return await app.cosmos_client.create_database(nag)
     
async def get_or_create_container(container_name):
    try:        
        app.todo_items_container = app.database.get_container_client(azurecontainerregistry321)
        return await app.todo_items_container.read()   
    except exceptions.CosmosResourceNotFoundError:
        print("Creating container with id as partition key")
        return await app.database.create_container(id=container_name, partition_key=PartitionKey(path="/id"))
    except exceptions.CosmosHttpResponseError:
        raise



