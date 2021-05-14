from config import *
from random import choice
from os import system


def decorator_cycle(func):
    def wrapper():
        while True:
            func()
            if input("Начать новую игру (1-Да): ") != "1":
                break
            system("cls")
    return wrapper


@decorator_cycle
def play():
    system("cls")

    def find(s, w):
        list_index, i = list(), 0
        for _ in range(0, w.count(s)):
            i = w.find(s, i)
            list_index.append(i)
            i += 1
        return list_index

    with open("data.txt", "r", encoding="utf8") as file:
        unknown_word = choice([row[:-1] for row in file])
    word, num_errors = ["_" for _ in unknown_word], 0

    while True:
        print(STATES[num_errors])
        print("Неизвестное слово:", "".join(word))

        if num_errors == 10:
            print("Вы проиграли\nИскомое слово:", unknown_word)
            return

        if "_" not in word:
            print("Вы выиграли\nИскомое слово:", unknown_word)
            return

        symbol = input("Введите букву: ")

        if len(symbol) == 1 and symbol in unknown_word and symbol not in word:
            indexes = find(symbol, unknown_word)
            for index in indexes:
                word[index] = symbol
        else:
            num_errors += 1

        system("cls")


if __name__ == "__main__":
    play()
