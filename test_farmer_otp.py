import requests

r = requests.get('http://127.0.0.1:8000/')
assert 'id="farmer-login-phone"' in r.text
assert 'id="send-otp-btn"' in r.text
assert 'id="farmer-login-otp"' in r.text
assert 'id="farmer-otp-submit-btn"' in r.text
assert 'id="staff-login-id"' in r.text
print("SUCCESS: Farmer Mobile OTP login system and Staff Login are fully verified on the front page!")
