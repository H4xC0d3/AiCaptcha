from urllib.parse import urlencode

#class ocr:
#	def __init__(self, dict):
#		self.dict = dict
#	def __str__(self):
#		return urlencode(self.dict)
#	@property
#	def text(self):
#		return self.dict["text"]

#class objectrecognition:
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