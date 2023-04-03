from urllib.parse import urlencode
import json

#class ocr:
#	def __init__(self, dict):
#		self.dict = dict
#	def __str__(self):
#		return urlencode(self.dict)
#	@property
#	def text(self):
#		return self.dict["text"]

#class puzzle:
#	def __init__(self, dict):
#		self.dict = dict
#	def __str__(self):
#		return urlencode(self.dict)
#	@property
#	def text(self):
#		return self.dict["text"]

#class tiktok:
#	def __init__(self, dict):
#		self.dict = dict
#	def __str__(self):
#		return urlencode(self.dict)
#	@property
#	def text(self):
#		return self.dict["text"]

class objectrecognition_class:
	def __init__(self, dict):
		self.dict = dict
	def __str__(self):
		return json.dumps(self.dict["results"])
	@property
	def results(self):
		return self.dict["results"]

class audio_class:
	def __init__(self, dict):
		self.dict = dict
	def __str__(self):
		return urlencode(self.dict)
	@property
	def text(self):
		return self.dict["text"]
	@property
	def confidence(self):
		return self.dict["confidence"]

class recaptchav3_class:
	def __init__(self, dict):
		self.dict = dict
	def __str__(self):
		return urlencode(self.dict)
	@property
	def token(self):
		return self.dict["recaptcha_token"]

class hcaptcha_class:
	def __init__(self, dict):
		self.dict = dict
	def __str__(self):
		return urlencode(self.dict)
	@property
	def token(self):
		return self.dict["recaptcha_token"]
	@property
	def key(self):
		return self.dict["key"]

class limits_class:
	def __init__(self, dict):
		self.dict = dict["limits"]
	def __str__(self):
		return urlencode(self.dict)
	@property
	def hcaptcha(self):
		return self.dict["hcaptcha_limit"] if "hcaptcha_limit" in self.dict else 0
	@property
	def recaptchav3(self):
		return self.dict["recaptcha_v3_limit"] if "recaptcha_v3_limit" in self.dict else 0
	@property
	def recaptchav2(self):
		return self.dict["recaptcha_v2_limit"] if "recaptcha_v2_limit" in self.dict else 0
	@property
	def ocr(self):
		return self.dict["ocr_limit"] if "ocr_limit" in self.dict else 0
	@property
	def audio(self):
		return self.dict["audio_limit"] if "audio_limit" in self.dict else 0
	@property
	def object_recognition(self):
		return self.dict["object_recognition_limit"] if "object_recognition_limit" in self.dict else 0
	@property
	def puzzle(self):
		return self.dict["puzzle_limit"] if "puzzle_limit" in self.dict else 0
	@property
	def tiktok(self):
		return self.dict["tiktok_limit"] if "tiktok_limit" in self.dict else 0
	@property
	def funcaptcha(self):
		return self.dict["funcaptcha_limit"] if "funcaptcha_limit" in self.dict else 0