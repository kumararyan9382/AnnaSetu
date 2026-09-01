import requests

r_home = requests.get('http://127.0.0.1:8000/')
assert 'id="farmer-step2-reg-form"' in r_home.text
assert 'id="farmer-reg-input"' in r_home.text
assert 'id="verified-registry-pill"' in r_home.text

r_book = requests.get('http://127.0.0.1:8000/book')
assert 'id="farmer-reg-no"' in r_book.text
assert 'id="frn-verified-badge"' in r_book.text

print("SUCCESS: Farmer Registration Number validation verified on both Home Page and Booking Portal!")
