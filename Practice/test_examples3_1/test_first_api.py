import requests
import pytest


class TestFirstApi:
    """Параметризация"""
    names = [
        ("YaVas"),
        ("Borov"),
        ("")
    ]

    @pytest.mark.parametrize("name", names)
    def test_hello_call(self, name):
        url = "https://playground.learnqa.ru/api/hello"
        data = {"name": name}

        response_hello_call = requests.get(url, params=data)

        assert response_hello_call.status_code == 200, "Wrong response code"

        response_hello_call_dict = response_hello_call.json()
        assert "answer" in response_hello_call_dict, "There is no field 'answer' in the response_hello_call"

        if len(name) == 0:
            expected_response_hello_call_text = "Hello, someone"
        else:
            expected_response_hello_call_text = f"Hello, {name}"
        actual_response_hello_call_text = response_hello_call_dict["answer"]
        assert actual_response_hello_call_text == expected_response_hello_call_text, "Actual text in the response is not correct"
