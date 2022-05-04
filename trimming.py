from pydub import AudioSegment
from fastapi import UploadFile
import numpy as np
import json

def test(file: UploadFile):
	return {"filename": file.filename}

def trimming(file):
	jsondata = [
		{
			"labels": "noise",
			"start" : 0.0,
			"stop" : 10.0
		},
		{
			"labels": "noise",
			"start" : 10.0,
			"stop" : 20.0
		}
	]
	return json.dumps(jsondata)