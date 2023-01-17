def get_input_parameters():
    original_list = []
    n = int(input('Количество элементов: '))
    shift = int(input('Сдвиг: '))
    for i in range(n):
        print('Введите', i + 1, 'элемент списка: ', end=' ')
        numbers = int(input())
        original_list.append(numbers)
    print('Изначальный список:', original_list)

    return shift, original_list
    """
    Получаем сдвиг и начальны список

    :return: например: [3, [1, 4, -3, 0, 10]]
    :rtype: List[int, List[int]]
    """
    # TODO: в этой функции пишем весь необходимый код для
    #  получения входных параметров.
    #  Логику расчётов тут не программируем
    pass


def display_result(shifted_list):
    print('Сдвиг:', shift)
    print('Сдвинутый список: ', shifted_list)
    return
    """
    Выводим получившиеся список

    :param shifted_list: сдвинутый список, например: [5, 1, 2, 3, 4]
    :type shifted_list: List[int]
    """
    # TODO: в этой функции пишем весь необходимый код
    #  для вывода результата в нужном формате.
    #  Логику расчётов тут не программируем
    pass


def shift_list(shift, original_list):
    shifted_list = []
    for _ in range(shift):
        original_list.insert(0, original_list.pop())
    shifted_list.extend(original_list)

    return shifted_list
    """
    Сдвигаем список на определённое количество элементов в право

    :param shift: сдвиг: 3
    :type shift: int
    :param original_list: Исходный список: [1, 4, -3, 0, 10]
    :type original_list: List[int]

    :return: сдвинутый список, например: [5, 1, 2, 3, 4]
    :rtype: List[int]
    """
    # TODO: в этой функции пишем логику сдвига списка вправо на shift элементов.
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
    shift = input_data[0]
    original_list = input_data[1]
    shifted_list = shift_list(shift, original_list)  # сдвигаем список.
    display_result(shifted_list)  # выводим результат
