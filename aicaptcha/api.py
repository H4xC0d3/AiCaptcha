from .utils import *
import requests
from io import BufferedReader
from base64 import b64encode
requests.urllib3.disable_warnings()

class AiCaptcha:
	def __init__(self, api_key) -> None:
		self.__api_key = api_key
		self.__host = "http://captcha.x-api.tech/"
	
	def Hcaptcha(self, sitekey: str, host: str) -> hcaptcha:
		return hcaptcha(self.__request({"task": {"sitekey": sitekey, "host": host}, "type": "Hcaptcha"}))
	
	def ReCaptchaV3(self, site_key: str, page_url: str, action: str, user_agent: str=None, cb: str=None, cookies=None, v: str=None, co: str=None, domain: str=None) -> recaptchav3:
		return recaptchav3(self.__request({"task": {"site_key": site_key, "page_url": page_url, "action": action, "user_agent": user_agent, "cb": cb, "cookies": cookies, "v": v, "co": co, "domain": domain}, "type": "ReCaptchaV3"}))
	
	def ReCaptchaV3Enterprise(self, site_key: str, page_url: str, action: str, user_agent: str=None, cb: str=None, cookies=None, v: str=None, co: str=None, domain: str=None) -> recaptchav3:
		return recaptchav3(self.__request({"task": {"site_key": site_key, "page_url": page_url, "action": action, "user_agent": user_agent, "cb": cb, "cookies": cookies, "v": v, "co": co, "domain": domain}, "type": "ReCaptchaV3Enterprise"}))
	
	def TikTok(self, install_id: str, device_id: str, version: str) -> tiktok:
		return tiktok(self.__request({"task": {"install_id": install_id, "device_id": device_id}, "type": "TikTok", "version": version}))
	
	def Puzzle(self, background: str, piece: str) -> puzzle:
		return puzzle(self.__request({"task": {"background_image": self.__get_file(background),"piece_image": self.__get_file(piece)}, "type": "Puzzle"}))
	
	def OCR(self, image: str) -> ocr:
		return ocr(self.__request({"task": {"image": self.__get_file(image)}, "type": "OCR"}))
	
	def ObjectRecognition(self, image: str) -> objectrecognition:
		return objectrecognition(self.__request({"task": {"image": self.__get_file(image)}, "type": "ObjectRecognition"}))
	
	def Audio(self, audio: str, numbers_sensitivity: bool=True) -> audio:
		return audio(self.__request({"task": {"audio": self.__get_file(audio), "numbers_sensitivity": numbers_sensitivity}, "type": "Audio"}))
	
	def __request(self, payload):
		payload.update({"token": self.__api_key})
		response = requests.post(
			self.__host+"solve/captcha",
			json=payload,
			verify=False
		).json()
		if response["status"]:
			response.pop("status")
			return response
		else:
			raise ValueError(response["error"])
	
	def __get_file(self, content):
		if isinstance(content, str):
			return b64encode(open(content, "rb").read()).decode()
		elif isinstance(content, bytes):
			return b64encode(content).decode()
		elif isinstance(content, BufferedReader):
			return b64encode(content.read()).decode()
		else:
			raise ValueError("The file value is incorrect or not supported.")
