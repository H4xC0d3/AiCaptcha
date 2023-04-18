# AiCaptcha
Python library utilizes AiCaptcha's API to solve captcha challenges with the power of AI. With our advanced technology, you can effortlessly handle various types of captcha challenges without any hassle. 

## Installation
To install the library, simply run the following command:
``` 
pip install aicaptcha==1.0.4
```

## Services
- [x] `hCaptcha`
- [x] `ReCaptchaV3`
- [x] `Audio Captcha`
- [x] `Object Recognition Captcha`

## Usage
To use the library, import the AiCaptcha class from the aicaptcha module, create an instance of the class with your API key, and call the appropriate method to solve the captcha.

## Examples
### hCaptcha
HCaptcha is a type of captcha that asks users to select certain images that match a given description. To solve an HCaptcha using the AiCaptcha library, you can use the `Hcaptcha` method and pass in the `site_key` and `page_url` parameters, as well as your user agent string. Here's an example:
``` python
from aicaptcha import AiCaptcha

api_key = "your_api_key_here"
solver = AiCaptcha(api_key)

hcaptcha_result = solver.Hcaptcha(site_key="hcaptcha_site_key_here", page_url="hcaptcha_page_url_here", user_agent="your_user_agent_here")
print(hcaptcha_result.token)
print(hcaptcha_result.key)
```

### ReCaptcha V3
ReCaptchaV3 is a type of captcha that uses a risk analysis engine to determine whether a user is a bot or a human. To solve a ReCaptchaV3 using the AiCaptcha library, you can use the `ReCaptchaV3` method and pass in the `type`, `site_key`, `page_url`, and `action` parameters. Here's an example: 
``` python
from aicaptcha import AiCaptcha

api_key = "your_api_key_here"
solver = AiCaptcha(api_key)

recaptchav3_result = solver.ReCaptchaV3(type="recaptchav3_type(enterprise/normal)", site_key="recaptchav3_site_key_here", page_url="recaptchav3_page_url_here", action="recaptchav3_action_here")
print(recaptchav3_result.token)
```

### Audio Captcha
Audio Captcha is a type of captcha that plays an audio clip containing a sequence of numbers or letters, which the user is required to transcribe. To solve an Audio Captcha using the AiCaptcha library, you can use the `Audio` method and pass in the `audio` parameter, which can be either the filename or content or URL of the audio file. If you set the `numbers_sensitivity` parameter to `True`, the recognition will be performed on both numbers and letters, but with a higher sensitivity to numbers, which can increase the accuracy of the recognition for number sequences. Here's an example:
``` python
from aicaptcha import AiCaptcha

api_key = "your_api_key_here"
solver = AiCaptcha(api_key)

audio_captcha_result = solver.Audio(audio="audio_filename_or_content_or_url", numbers_sensitivity=False)
print(audio_captcha_result.text)
print(audio_captcha_result.confidence)
```

### Object Recognition Captcha
Object Recognition Captcha is a type of captcha that shows an image containing multiple objects, and the user is required to select all objects of a certain type. To solve an Object Recognition Captcha using the AiCaptcha library, you can use the `ObjectRecognition` method and pass in the `image` parameter, which can be either the filename or content or URL of the image. You can also set the `max_results` parameter to specify the maximum number of objects to return. Here's an example:
``` python
from aicaptcha import AiCaptcha

api_key = "your_api_key_here"
solver = AiCaptcha(api_key)

object_recognition_captcha_result = solver.ObjectRecognition(image="image_filename_or_content_or_url", max_results=5)
print(object_recognition_captcha_result.results)
```

## Free API Key
``` txt
a433a493-bc2c-41a7-baab-fb898442d2ed
```

## 
Channel: [AiCaptcha](https://t.me/aicaptcha)\
Support: [support](https://t.me/AiCaptchaSupport)
