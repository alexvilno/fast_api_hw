import uvicorn
from fastapi import FastAPI, APIRouter
from api.endpoints import points_router

app = FastAPI(
    version="1.0",
    title="Peoples/regions API"
)

main_router = APIRouter()

main_router.include_router(router=points_router, prefix="/api", tags=["api"])


@app.get("/")
async def root():
    return {"message:": "Hello"}

app.include_router(main_router)

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        reload=True,
        port=1234
    )
