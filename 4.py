def calc_stat(listened):  # От англ. calculate statistics, посчитать статистику
    N = len(listened)
    return f'Вы прослушали {N} песен.'

# Пример вызова функции
print(calc_stat([189, 148, 210, 144, 174, 158, 163, 189, 227, 198]))