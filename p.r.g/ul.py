import requests #الدرس ااول التعامل مع المكتبة


url =   "api.quotable.io/random"

response = requests.get(url)
#______________salah_______________#
print(response.status_code)
print(response.text)
print(response.json())
