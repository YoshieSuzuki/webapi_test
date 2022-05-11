import os
import shutil
from distutils.command.upload import upload
from pathlib import Path

import uvicorn
from fastapi import FastAPI, File, UploadFile

from trimming import test, trimming

app = FastAPI()

@app.get('/index/{name}')
def hello_world(name: str):
	return f"Hello {name}!"

@app.post('/api/getcsv')
def get_csv(file: UploadFile = File(...)):
	return test(file)

@app.post('/api/trimming/')
def get_csv(file: UploadFile):
	destination: Path = Path()
	destination = destination / "audio_tmp" / "tmp.mp3"
	try:
		with destination.open("wb") as buffer:
			shutil.copyfileobj(file.file, buffer)
	finally:
		file.file.close()

	return trimming()

if __name__ == "__main__":
	uvicorn.run(app, port=8080, host='0.0.0.0')
