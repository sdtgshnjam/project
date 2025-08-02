import requests
import json
import time
name = input("entr u are name:\n")
ps = input("enter u are password:\n")
if ps == 1234:
      print(f"hi\n:{name}{ps}")
else:
    print("go to hell")
    
"""
المشروع الاول ____________________SALAH______________________
"""
def get_quote():
    url = "https://api.quotable.io/random"
    response = requests.get(url)
    if response.status_code == 200:
     data  = response.json()
     return {
            "quote": data["content"],
            "author": data["author"]
        }
    else:
       return None
def sa(count=10):
   all_guotes = []
   for i in range(count):
       print(f"جار تحميل الأقتباس{i+1}...")

       quote = get_quote()
       if quote:
          all_guotes.append(quote)
          time.sleep(1)
   return all_guotes

    
def save_to_json_quotes(data, filename="quotes.json"):
   with open(filename, "w", encoding="utf-8") as f:
      json.dump(data, f, ensure_ascii=False, indent=4)
      print(f"تم حفظ الاقتباس{len(data)} ....{filename}")

quotes = sa(10)
save_to_json_quotes(quotes)
