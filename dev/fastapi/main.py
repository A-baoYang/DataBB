from fastapi import FastAPI, status, HTTPException, Query, Request, Response
from fastapi.middleware.cors import CORSMiddleware


tags_metadata = [
    {"name": "chat", "description": "取得 AI 回覆"},
]
app = FastAPI(
    title="My API",
    service_name="my_api",
    description="Get chat reply from AI model.",
    version="0.0.1b",
    contact={"name": "ABC", "email": "xxxxxabc@gmail.com",},
    license_info={
        "name": "GNU GPL 3.0",
        "url": "https://www.gnu.org/licenses/gpl-3.0.html",
    },
    openapi_tags=tags_metadata,
    debug=True,
)
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"message": "My API is ready"}


@app.get("/connect_test")
def read_requests(request: Request):
    return {"message": "Hello World", "root_path": request.scope.get("root_path")}

