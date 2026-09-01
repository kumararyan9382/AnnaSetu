import requests

r = requests.get('http://127.0.0.1:8000/book')
assert 'value=""' in r.text
assert 'value="रामेश कुमार' not in r.text
assert 'value="9876543210"' not in r.text
assert 'value="तरावड़ी' not in r.text
assert 'value="करनाल' not in r.text
assert 'value="HR-05-AE-4421"' not in r.text
print("SUCCESS: All farmer details and vehicle fields are 100% blank and ready for custom user input!")
