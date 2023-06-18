from aicaptcha import AiCaptcha
import requests

api_key = "a433a493-bc2c-41a7-baab-fb898442d2ed"
solver = AiCaptcha(api_key)

recaptchav3_result = solver.ReCaptchaV3(type="normal", site_key="6LdyC2cUAAAAACGuDKpXeDorzUDWXmdqeg-xy696", page_url="https://recaptcha-demo.appspot.com/recaptcha-v3-request-scores.php", action="examples/v3scores")
recaptchav3_token = recaptchav3_result.token

print("captcha token:", recaptchav3_token)

result = requests.get("https://recaptcha-demo.appspot.com/recaptcha-v3-verify.php?action=examples/v3scores&token={}".format(recaptchav3_token)).json()

if result["success"]:
    print("Done solve captcha!")
else:
    print("Captcha could not be solved!")
