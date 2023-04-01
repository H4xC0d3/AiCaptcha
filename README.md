# AiCaptcha
Python library for solving various types of captcha including Hcaptcha and ReCaptchaV3(enterprise/normal).

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
hcaptcha_result = solver.Hcaptcha(site_key="hcaptcha_site_key_here", page_url="hcaptcha_page_url_here")
print(hcaptcha_result.dict)

# Solve a ReCaptchaV3 (enterprise/normal)
recaptcha_result = solver.ReCaptchaV3(type="recaptchav3_type(enterprise/normal)", site_key="recaptchav3_site_key_here", page_url="recaptchav3_page_url_here", action="recaptchav3_action_here")
print(recaptcha_result.dict)
```

### Channel
Telegram : [AiCaptcha](https://t.me/aicaptcha)

### Support
Telegram : [Mr.Abood](https://t.me/O0O0I)\
If you need a free trial contact support.
