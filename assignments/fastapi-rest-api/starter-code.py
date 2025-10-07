from fastapi import FastAPI, HTTPException

app = FastAPI()

# Dados em memória
users = []

@app.get("/")
def read_root():
    return {"message": "Bem-vindo à API FastAPI!"}

@app.post("/users")
def create_user(user: dict):
    user["id"] = len(users) + 1
    users.append(user)
    return user

@app.get("/users")
def list_users():
    return users

@app.get("/users/{user_id}")
def get_user(user_id: int):
    for user in users:
        if user["id"] == user_id:
            return user
    raise HTTPException(status_code=404, detail="Usuário não encontrado")

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for i, user in enumerate(users):
        if user["id"] == user_id:
            del users[i]
            return {"message": "Usuário removido"}
    raise HTTPException(status_code=404, detail="Usuário não encontrado")
