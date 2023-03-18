#  Ввод имеющейся суммы и количества откликов
purchase = list(map(int, input().split()))
# Списки вы которые будут определены отклики
b_offers = []
a_offers = []
# Конечное количество книг
quantity = 0
# Сортировка книг по сложности
for i in range(purchase[-1]):
    temporary_offer = list(map(str, input().split()))
    if temporary_offer[-1] == "B":
        b_offers.append(int(temporary_offer[0]))
    elif temporary_offer[-1] == "A":
        a_offers.append(int(temporary_offer[0]))
# Сортировка книг по стоймости
b_offers.sort()
a_offers.sort()
# Подсчёт количества книг
for i in b_offers:
    if i <= purchase[0]:
        purchase[0] -= i
        quantity += 1
for i0 in a_offers:
    if i0 <= purchase[0]:
        purchase[0] -= i0
        quantity += 1
# Вывод количества книг
print(quantity)
