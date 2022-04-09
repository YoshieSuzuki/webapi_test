import csv
import json
import os

from fastapi import UploadFile
from inaSpeechSegmenter import Segmenter, seg2csv
from pydub import AudioSegment


def trimming():
	row_list = []
	audio_data = AudioSegment.from_mp3('./audio_tmp/tmp.mp3')

	seg = Segmenter(vad_engine='smn', detect_gender=False)
	segmentation = seg('./audio_tmp/tmp.mp3')
	seg2csv(segmentation, './audio_tmp/Result.csv')

	with open('./audio_tmp/Result.csv', 'r') as f:
		for row in csv.DictReader(f, delimiter="\t",):
			row_list.append(row)

	os.remove('./audio_tmp/tmp.mp3')
	os.remove('./audio_tmp/Result.csv')

	return json.dumps(row_list)
