from pydub import AudioSegment
from fastapi import UploadFile
import numpy as np
import json

def test(file: UploadFile):
	return {"filename": file.filename}

def trimming():
	audio_data = AudioSegment.from_mp3("./audio_tmp/tmp.mp3")
	jsondata = {
		"duration_seconds": audio_data.duration_seconds,
		"frame_rate": audio_data.frame_rate,
		"channels": audio_data.channels
	}
	print(jsondata)
	# jsondata = [
	# 	{
	# 		"labels": "noise",
	# 		"start" : 0.0,
	# 		"stop" : 10.0
	# 	},
	# 	{
	# 		"labels": "noise",
	# 		"start" : 10.0,
	# 		"stop" : 20.0
	# 	}
	# ]
	return json.dumps(jsondata)