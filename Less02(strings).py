# Задача:
# Выполните следующие действия в PyCharm:
# В переменную example запишите любую строку.
# Выведите на экран(в консоль) первый символ этой строки.
# Выведите на экран(в консоль) последний символ этой строки (используя отрицательный индекс).
# Выведите на экран(в консоль) вторую половину этой строки (С нечётным количеством символов: 'Urban' -> 'ban').
# Выведите на экран(в консоль) это слово наоборот.
# Выведите на экран(в консоль) каждый второй символ этой строки. (Пример: 'Топинамбур'->'оиабр')
# Вводные данные:
# example = 'Топинамбур'
# Вывод на экран(в консоль):
# Т
# р
# амбур
# рубманипоТ
# оиабр
# Примечания:
# Для вывода значений на экран используйте функцию print()
# Для доступа к символу строки по индексу используйте квадратные скобки и индекс символа
# ('Urban'[3] -  четвёртый символ строки 'Urban' - 'a')
# Индексация начинается с нуля.

example = "Ираклий"


print("Строка: " + example)
print("Первый символ в строке: " + example[0])
print("Послдедний символ в строке: " + example[-1])

halfStr = int(len(example)/2)
print("Вторая половина строки: " + example[halfStr:])

print("Строка в обратном порядке: " + example[::-1])
print("Каждый второй символ строки: " + example[1::2])
