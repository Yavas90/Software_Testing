from json.decoder import JSONDecodeError
import requests


def print_response(self):
    print(f"Код ответа: {self.status_code}\nТекст ответа: {self.text}")


print("Hello from Yaroslav")
payload1 = {"name": "YaVas"}

url = "https://playground.learnqa.ru/"

response_get_text = requests.get(f"{url}api/get_text", verify=False)
print_response(response_get_text)

try:
    parsed_response_get_text = response_get_text.json()
    print(parsed_response_get_text)
except JSONDecodeError:
    print("Response is not a JSON format")

response_hello = requests.get(f"{url}api/hello", params=payload1, verify=False)
parsed_response_hello = response_hello.json()
print_response(response_hello)

"""Для GET params"""
response_get_check_type = requests.get(f"{url}api/check_type", params={"param1": "value1"}, verify=False)
print_response(response_get_check_type)

"""Для POST data"""
response_post_check_type = requests.post(f"{url}api/check_type", data={"param1": "value1"}, verify=False)
print_response(response_post_check_type)

response_get_301_f = requests.get(f"{url}api/get_301", allow_redirects=False, verify=False)
print_response(response_get_301_f)

response_get_301_t = requests.get(f"{url}api/get_301", allow_redirects=True, verify=False)
print_response(response_get_301_t)

first_response = response_get_301_t.history[0]
second_response = response_get_301_t
print(f"Первый url: {first_response.url}\nВторой url: {second_response.url}")

headers = {"some_header": "123"}
response_show_all_headers = requests.get(f"{url}api/show_all_headers", headers=headers, verify=False)
print(f"{print_response(response_show_all_headers)}\nHeaders: {response_show_all_headers.headers}")

payload2 = {"login": "secret_login", "password": "secret_pass"}
response_get_auth_cookie = requests.post(f"{url}api/get_auth_cookie", data=payload2, verify=False)
print_response(response_get_auth_cookie)
print(dict(response_get_auth_cookie.cookies))
print(response_get_auth_cookie.headers)

response_check_auth_cookie = requests.post(f"{url}api/get_auth_cookie", data=payload2, verify=False)
cookie_value = response_check_auth_cookie.cookies.get("auth_cookie")
cookies = {}
if cookie_value is not None:
    cookies.update({"auth_cookie": cookie_value})

response_check_auth_cookie2 = requests.post(f"{url}api/check_auth_cookie", cookies=cookies, verify=False)
print_response(response_check_auth_cookie2)
