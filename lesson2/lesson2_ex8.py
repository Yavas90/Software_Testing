import requests
import time
import json
from methods.methods import PrintMethod

url = "https://playground.learnqa.ru/ajax/api/longtime_job"

"""Отправляем запрос и получаем token"""
response_without_get_params = requests.get(url, verify=False)
obj = json.loads(response_without_get_params.text)
token = obj["token"]
seconds = obj["seconds"]
PrintMethod.print_response(response_without_get_params)
time.sleep(seconds)

"""Отправляем запрос с полученным  token"""
payload = {"token": token}
response_with_get_token = requests.get(url, params=payload, verify=False)
PrintMethod.print_response(response_with_get_token)
