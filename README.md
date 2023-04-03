# AiCaptcha
Python library for solving various types of captcha including Hcaptcha, ReCaptchaV3(enterprise/normal), ObjectRecognition and Audio.

## Installation
To install the library, simply run the following command:
``` 
pip install aicaptcha
```
## Usage
To use the library, import the AiCaptcha class from the aicaptcha module, create an instance of the class with your API key, and call the appropriate method to solve the captcha.

Here's an example:
``` python
from aicaptcha import AiCaptcha

api_key = "your_api_key_here"
solver = AiCaptcha(api_key)

# Solve an Hcaptcha
hcaptcha_result = solver.Hcaptcha(site_key="hcaptcha_site_key_here", page_url="hcaptcha_page_url_here", user_agent="your_user_agent_here")
print(hcaptcha_result.token)
print(hcaptcha_result.key)

# Solve a ReCaptchaV3 (enterprise/normal)
recaptchav3_result = solver.ReCaptchaV3(type="recaptchav3_type(enterprise/normal)", site_key="recaptchav3_site_key_here", page_url="recaptchav3_page_url_here", action="recaptchav3_action_here")
print(recaptchav3_result.token)

# Solve a audio captcha
audio_captcha_result = solver.Audio(audio="audio_filename_or_content_or_url", numbers_sensitivity=False)
print(audio_captcha_result.text)
print(audio_captcha_result.confidence)

# Solve the captcha specifying the name of the objects
object_recognition_captcha_result = solver.ObjectRecognition(image="image_filename_or_content_or_url", max_results=5)
print(object_recognition_captcha_result.results)
```

### Channel
Telegram : [AiCaptcha](https://t.me/aicaptcha)

### Support
Telegram : [support](https://t.me/O0O0I)\
for free trial contact support.
