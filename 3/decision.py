# Вводим координаты точек и формируем список
cordinates = list(map(int, input().split()))
# Первый и второй отрезки
first = set(range(cordinates[0], cordinates[1] + 1))
second = set(range(cordinates[2], cordinates[3] + 1))
# Проверяем не содержит ли первый отрезок точки из второго
# Выводим кто победил
if first.isdisjoint(second):
    print("Второй выйграл")
else:
    print("Первый выйграл")
