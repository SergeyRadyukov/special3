def get_input_parameters():
    number = int(input('Кол-во контейнеров: '))
    list_container_weights = []
    for i in range(number):
        while True:
            weight = int(input('Введите вес ' + str(i + 1) + ' контейнера: '))
            if weight <= 200:
                break
        list_container_weights.append(weight)
    list_container_weights.sort(reverse=True)
    new_container_weight = int(input('Введите вес нового контейнера: '))
    return list_container_weights, new_container_weight
    """
    Получаем список весов контейнеров и вес нового контейнера
    Незабываем проверит данные: все числа целые и не превышают 200.

    :return: список весов контейнеров и вес нового контейнера,
             например: [[165, 163, 160, 160, 157, 157, 155, 154], 162]
    :rtype: List[List[int], int]
    """
    # TODO: в этой функции пишем весь необходимый код для
    #  получения входных параметров.
    #  Логику расчётов тут не программируем
    pass


def display_result(serial_number_new_container):
    print('Номер, куда встанет новый контейнер:', serial_number_new_container)
    return
    """
    Выводим порядковый номер нового контейнера.

    :param serial_number_new_container: порядковый номер нового контейнера, например: 3
    :type serial_number_new_container: int
    """
    # TODO: в этой функции пишем весь необходимый код
    #  для вывода результата в нужном формате.
    #  Логику расчётов тут не программируем
    pass


def search_serial_number_new_container(list_container_weights, new_container_weight):
    serial_number_new_container = []
    for c in range(len(list_container_weights)):
        serial_number_new_container = c + 1
        if list_container_weights[c] < new_container_weight:
            break
    return serial_number_new_container
    """
    Ищем куда вставим новый контейнер.

    :param list_container_weights: список весов контейнеров, например: [165, 163, 160, 160, 157, 157, 155, 154]
    :type list_container_weights: List[int]
    :param new_container_weight: вес нового контейнера, например: 166
    :type new_container_weight: int

    :return: порядковый номер нового контейнера, например: 3
    :rtype: int
    """
    # TODO: в этой функции пишем логику поиска куда вставим новый контейнер.
    #  print'ов и input'ов тут не должно быть.
    #  Функция на вход принимает ранее полученные данные
    #  (из функции get_input_parameters).
    #  Функция на выход отдаёт результат необходимый для отображения работы программы,
    #  который будет передан в функцию display_result.
    pass


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    input_data = get_input_parameters()  # получаем параметры
    list_container_weights = input_data[0]
    new_container_weight = input_data[1]
    # Ищем куда вставим новый контейнер.
    serial_number_new_container = search_serial_number_new_container(list_container_weights, new_container_weight)
    display_result(serial_number_new_container)  # выводим результат