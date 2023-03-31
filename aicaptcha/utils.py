from urllib.parse import urlencode

#class ocr:
#	def __init__(self, dict):
#		self.dict = dict
#	def __str__(self):
#		return urlencode(self.dict)
#	@property
#	def text(self):
#		return self.dict["text"]

#class audio:
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

class recaptchav3:
	def __init__(self, dict):
		self.dict = dict
	def __str__(self):
		return urlencode(self.dict)
	@property
	def token(self):
		return self.dict["token"]

class hcaptcha:
	def __init__(self, dict):
		self.dict = dict
	def __str__(self):
		return urlencode(self.dict)
	@property
	def token(self):
		return self.dict["generated_pass_UUID"]
	@property
	def key(self):
		return self.dict["key"]