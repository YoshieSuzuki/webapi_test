from fastapi import FastAPI
from fastapi import UploadFile, File
import uvicorn
from trimming import test, trimming

app = FastAPI()

@app.get('/index/{name}')
def hello_world(name: str):
	return f"Hello {name}!"

@app.post('/api/getcsv')
def get_csv(file: UploadFile = File(...)):
	return test(file)

@app.post('/api/trimming')
def get_csv(file: UploadFile = File(...)):
	return trimming(file)

if __name__ == "__main__":
	uvicorn.run(app, port=8080, host='0.0.0.0')