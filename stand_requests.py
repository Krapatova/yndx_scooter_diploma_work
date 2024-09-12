import requests
import configurations
import data

#Создаем заказ
def create_order():
    return requests.post(configurations.SERVICE_URL + configurations.CREATE_ORDER_PATH,
                         json = data.user_body)

#Сохраняем созданный трек номер
response = create_order().json()
track_number = response['track']

#Вставляем сохраненный трек-номер в параметры запроса
def new_params(new_track):
    current_param = {"t": new_track}
    return current_param

#Запрос на получение заказа по трек-номеру
def check_order_information():
    return requests.get(configurations.SERVICE_URL + configurations.GET_ORDER_BY_TRACK,
                        params = new_params(track_number))

