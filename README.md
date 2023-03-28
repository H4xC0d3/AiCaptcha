# AiCaptcha
Python library for solving various types of captcha including Hcaptcha, ReCaptchaV3, TikTok, Puzzle, OCR, Object Recognition and Audio.

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
captcha_solver = AiCaptcha(api_key)

# Solve an Hcaptcha
hcaptcha_result = captcha_solver.Hcaptcha(sitekey="your_site_key_here", host="your_host_here")
print(hcaptcha_result.dict)

# Solve a ReCaptchaV3
recaptcha_result = captcha_solver.ReCaptchaV3(site_key="your_site_key_here", page_url="your_page_url_here", action="your_action_here")
print(recaptcha_result.dict)

# Solve a TikTok captcha
tiktok_result = captcha_solver.TikTok(install_id="your_install_id_here", device_id="your_device_id_here", version="your_version_here")
print(tiktok_result.dict)

# Solve a Puzzle captcha
puzzle_result = captcha_solver.Puzzle(background="path_to_background_image", piece="path_to_piece_image")
print(puzzle_result.dict)

# Solve an OCR captcha
ocr_result = captcha_solver.OCR(image="path_to_image")
print(ocr_result.dict)

# Solve an Object Recognition captcha
objectrecognition_result = captcha_solver.ObjectRecognition(image="path_to_image")
print(objectrecognition_result.dict)

# Solve an Audio captcha
audio_result = captcha_solver.Audio(audio="path_to_audio_file", numbers_sensitivity=True)
print(audio_result.dict)
```

### Contact
Telegram : [Mr.Abood](https://t.me/O0O0I)
