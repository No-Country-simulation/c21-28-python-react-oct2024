import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/x")
def read_root():
   return "Hola desde FastApi!"

if __name__ == '__main__':
   uvicorn.run(app, host="127.0.0.1", port=80)
#uvicorn — host localhost — port 5555 hola1:app