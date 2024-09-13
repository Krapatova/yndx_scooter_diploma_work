# Валерия Панкратова, 21-я когорта — Финальный проект. Инженер по тестированию плюс
import stand_requests


def positive_assert(track_number):
    response = stand_requests.check_order_information(track_number)
    assert response.status_code == 200


def test_check_order_by_recent_track():
    positive_assert(stand_requests.track_number_from_new_order)