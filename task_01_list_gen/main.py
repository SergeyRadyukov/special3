def get_input_parameters():
    number= int(input('Введите целое число: '))
    """
    Получаем N

    :return: N, например: 14
    :rtype: int
    """
    # TODO: в этой функции пишем весь необходимый код для
    #  получения входных параметров.
    #  Логику расчётов тут не программируем
    pass

def display_result(odd_numbers):
    print('', odd_numbers)
    #return odd_numbers
    """
    Выводим список нечётных чисел

    :param odd_numbers: список нечётных чисел, например: [1, 3, 5, 7, 9, 11, 13]
    :type odd_numbers: List[int]
    """
    # TODO: в этой функции пишем весь необходимый код
    #  для вывода результата в нужном формате.
    #  Логику расчётов тут не программируем
    pass

def get_odd_numbers(number):
    odd_number = []
    for i in range(1, number + 1):
        if i % 2 == 1:
            odd_number.append(i)
    """
    Получаем отсортированный по возрастанию список
    нечётных чисел от 1 до number.

    :param number: до какого числа нужно рассчитать, например: 14
    :type number: int

    :return: список нечётных чисел, например: [1, 3, 5, 7, 9, 11, 13]
    :rtype: List[int]
    """
    # TODO: в этой функции получаем отсортированный
    #  по возрастанию список нечётных чисел от 1 до number.
    #  print'ов и input'ов тут не должно быть.
    #  Функция на вход принимает ранее полученные данные
    #  (из функции get_input_parameters).
    #  Функция на выход отдаёт результат необходимый для отображения работы программы,
    #  который будет передан в функцию display_result.
    pass


if __name__ == '__main__':
    # Это условие необходимо, чтобы в рамках автотестов не произошёл
    # вызов функций get_input_parameters и display_result
    number = get_input_parameters()  # получаем параметры
    odd_numbers = get_odd_numbers(number)  # получаем нечётные числа
    display_result(odd_numbers)  # выводим результат