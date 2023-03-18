# Вводим количество денег
asset = list(map(int, input().split()))[0]
# Вводим отклики и формируем список
orders = list(map(int, input().split()))
# Формуруем список для удобства
orders.sort()
# Определяем счётчик
quantity = 0
# Проходим откликам циклом
for i in orders:
    # Если отклик стоит меньше имеющихся средств, покупаем
    if i <= asset:
        asset -= i
        quantity += 1
# Вводим количество задач
print(quantity)
