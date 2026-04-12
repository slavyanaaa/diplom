from sender_stand_request import post_new_order, get_order

# Импортируем модуль data, в котором определены данные, необходимые для HTTP-запросов.
import data 

def test_order():
    response = post_new_order(data.user_body)
    track_number = response.json()["track"]
    assert track_number is not None
    response = get_order (track_number)
    assert response.status_code == 200