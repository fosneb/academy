# Сохраняем в переменной алфавит
alphabet = "abcdefghijklmnopqrstuvwxyz"


# Определяем функцию, шифрующую слова
def caesar(word):
    # Создаём переменную в которую будем записывать новое слово
    new_word = ""
    # Проходим циклом по текущему слову
    for i in word:
        # Получаем индекс буквы в алфавите
        index = alphabet.find(i)
        # Если это, например, буква "z", то меняем индекс на 0
        # Получаем на выходе букву "a"
        if alphabet[index] == alphabet[-1]:
            letter = alphabet[0]
        # Иначе, прибавляем к индексу еденицу и берём букву из алфавита
        else:
            letter = alphabet[index + 1]
        # Собираем новое слово по буквам
        new_word += letter
    # Возвращаем новое слово
    # !!ВНИМАНИЕ!!
    # Если не указать return, функция вернёт None как результат своего исполнения
    return new_word


# Выводим новое слово
print(caesar("hello"))