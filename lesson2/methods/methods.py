class PrintMethod:
    def print_response(self):
        print("Код ответа:", self.status_code)
        print("Текст ответа:", self.text, "\n")