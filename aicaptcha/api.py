from .utils import *
import requests
from io import BufferedReader
from base64 import b64encode
requests.urllib3.disable_warnings()

class AiCaptcha:
	def __init__(self, api_key) -> None:
		self.__api_key = api_key
		self.__host = "http://captcha.x-api.tech/"
	
	def Limits(self) -> limits_class:
		response = requests.get(self.__host+"/limit/"+self.__api_key).json()
		if response["status"]:
			response.pop("status")
			return limits_class(response)
		else:
			raise Exception(response["error"]) 
	
	def Hcaptcha(self, site_key: str, page_url: str, user_agent: str, version: str=None, widget_id: str=None, proxy: dict=None) -> hcaptcha_class:
		return hcaptcha_class(self.__request({"task": {"site_key": site_key, "page_url": page_url, "user_agent": user_agent, "version": version, "widget_id": widget_id, "proxy": proxy}, "type": "Hcaptcha"}))
	
	def ReCaptchaV3(self, site_key: str, page_url: str, action: str, type: str="normal", user_agent: str=None, cb: str=None, cookies=None, v: str=None, co: str=None, domain: str=None, proxy: dict=None) -> recaptchav3_class:
		return recaptchav3_class(self.__request({"task": {"type": type, "site_key": site_key, "page_url": page_url, "action": action, "user_agent": user_agent, "cb": cb, "cookies": cookies, "v": v, "co": co, "domain": domain, "proxy": proxy}, "type": "ReCaptchaV3"}))
	
	def Audio(self, audio: str, numbers_sensitivity: bool=False) -> audio_class:
		return audio_class(self.__request({"task": {"audio_base64": self.__get_file(audio), "numbers_sensitivity": numbers_sensitivity}, "type": "Audio"}))
	
	def ObjectRecognition(self, image: str, max_results: int=5) -> objectrecognition_class:
		return objectrecognition_class(self.__request({"task": {"image_base64": self.__get_file(image), "max_results": max_results}, "type": "ObjectRecognition"}))
	
#	def TikTok(self, install_id: str, device_id: str, version: str) -> tiktok:
#		return tiktok(self.__request({"task": {"install_id": install_id, "device_id": device_id}, "type": "TikTok", "version": version}))
#	
#	def Puzzle(self, background: str, piece: str) -> puzzle:
#		return puzzle(self.__request({"task": {"background_image": self.__get_file(background),"piece_image": self.__get_file(piece)}, "type": "Puzzle"}))
#	
#	def OCR(self, image: str) -> ocr:
#		return ocr(self.__request({"task": {"image": self.__get_file(image)}, "type": "OCR"}))
	
	def __request(self, payload):
		payload.update({"api_key": self.__api_key})
		response = requests.post(
			self.__host+"solve/captcha",
			json=payload,
			verify=False
		).json()
		if response["status"]:
			response.pop("status")
			return response
		else:
			raise Exception(response["error"])
	
	def __get_file(self, content):
		if isinstance(content, str) and content.startswith("http") and "://" in content:
			return b64encode(requests.get(content).content).decode()
		elif isinstance(content, bytes):
			return b64encode(content).decode()
		elif isinstance(content, BufferedReader):
			return b64encode(content.read()).decode()
		elif isinstance(content, str):
			return b64encode(open(content, "rb").read()).decode()
		else:
			raise ValueError("The file value is incorrect or not supported.")