import pyinsane2
from flask import Flask, Response, request
from flask_cors import CORS
import json
import base64
import img2pdf
import time
import numpy as np
from PIL import Image
import io
import sys




def scan(res=128, multiple=False):
	try:
		pyinsane2.init()
	except:
		return None
	try:
		devices = pyinsane2.get_devices()
		assert(len(devices) > 0)
		device = devices[0]
		pyinsane2.set_scanner_opt(device, 'resolution', [res])
		pyinsane2.set_scanner_opt(device, 'mode', ['Color'])
		pyinsane2.maximize_scan_area(device)

		scan_session = device.scan(multiple=multiple)
		try:
			while True:
				scan_session.scan.read()
		except EOFError:
			pass
		image = scan_session.images[-1]
		pyinsane2.exit()
		
	except:
		print("Can not access scanner !")
		pyinsane2.exit()
		image = None

	return image

app = Flask(__name__)
CORS(app)

@app.route("/scan", methods=["POST"])
def index() :
	#something todo
	res = int(request.form.to_dict()["res_enter"])
	is_multiple = request.form.to_dict()["is_multiple"] == "true"
	data = scan(res, is_multiple)
	if data is None:
		json_data = {
			"type" : "Error",
			"content" : "No image data",
			"name" : ""
		}
	else:
		
		img_byte_arr = io.BytesIO()
		data.save(img_byte_arr, format='PNG')
		img_byte_arr = img_byte_arr.getvalue()

		json_data = {
			"type" : "DATA",
			"content" : base64.b64encode(img2pdf.convert(img_byte_arr)).decode('ascii'),
			"name" : "img" + str(time.time) + ".jpg",
			"width" : np.array(data).shape[1],
			"height" : np.array(data).shape[0]
		}
	print("shape : ", np.array(data).shape)
	return Response(json.dumps(json_data), mimetype="application/json")


if __name__ == "__main__" :
	with open("logg.txt", "w") as flog :
		sys.stdout = flog
		app.run(host = "127.0.0.1", port = 8000, debug=False)