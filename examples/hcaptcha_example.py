from aicaptcha import AiCaptcha

api_key = "a433a493-bc2c-41a7-baab-fb898442d2ed"
solver = AiCaptcha(api_key)

hcaptcha_result = solver.Hcaptcha(site_key="a5f74b19-9e45-40e0-b45d-47ff91b7a6c2", page_url="https://accounts.hcaptcha.com/demo", user_agent="Mozilla/5.0 (Linux; Android 10; BLA-L29) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36")

# To add a proxy:
#, proxy={"type": "HTTP", "address": "http://ip:port"}
#, proxy={"type": "HTTP", "address": "http://user:pass@ip:port"}

print(hcaptcha_result.token)
print(hcaptcha_result.key)
