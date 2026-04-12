# Импорт настроек из модуля configuration, который содержит параметры конфигурации, такие как URL сервиса
import configuration

# Импорт библиотеки requests для выполнения HTTP-запросов
import requests

# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data 

def post_new_order(body):
        return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=body)
response = post_new_order(data.user_body)
assert response.status_code == 201
print(response.status_code)
track_number = response.json()["track"]
def get_order(track_number):
        return requests.get(f"{configuration.URL_SERVICE}/v1/orders/track?t={track_number}")
response = get_order (track_number)
print(response.status_code) 