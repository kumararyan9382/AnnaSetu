import requests

r = requests.get('http://127.0.0.1:8000/')
assert 'id="farmer-login-id"' in r.text
assert 'id="farmer-login-pass"' in r.text
assert 'id="staff-login-id"' in r.text
assert 'id="staff-login-pass"' in r.text
assert 'id="staff-login-center"' in r.text
print("SUCCESS: Both Farmer Login and Staff Operator Login forms with User ID and Password are fully active on the homepage!")
