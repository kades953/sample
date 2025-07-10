from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()

@app.post("/log")
async def log_ip(request: Request):
    client_ip = request.client.host
    form = await request.form()
    username = form.get("username")
    print(f"[LOG] IP: {client_ip}, Username: {username}")
    return {"status": "logged"}
