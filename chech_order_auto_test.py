# Валерия Панкратова, 21-я когорта — Финальный проект. Инженер по тестированию плюс
from stand_requests import check_order_information


def test_check_order_by_track():
    assert check_order_information().status_code == 200

