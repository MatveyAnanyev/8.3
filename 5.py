def calc_stat(listened):  # От англ. calculate statistics, посчитать статистику
    N = len(listened)
    total_seconds = sum(listened)
    total_minutes = total_seconds // 60
    return f'Вы прослушали {N} песен общей продолжительностью {total_minutes} минут.'

# Пример вызова функции
print(calc_stat([189, 148, 210, 144, 174, 158, 163, 189, 227, 198]))