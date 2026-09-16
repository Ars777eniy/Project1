#Спортлото: 5 из 36
from utils import colors
import random

# Билет
expected = [2, 17, 8, 10, 1]

attempts = 0 # кол-во попыток
ALL = 5 # сколько номеров нужно угадать
MAX = 36 # сколько номеров всего
PRICE = 2 # стоимость билета в рублях
a = 0

print("\033[36;4m"+"Проведение розыгрыша:"+"\033[0m")

while True:
    attempts += 1
    a += PRICE
    ticket = random.sample(range(1, MAX + 1), ALL)

    print("\r" + colors.F_GREEN + str(ticket) + colors.RESET, end="")

    ticket_sorted = sorted(ticket)
    expected_sorted = sorted(expected)

    if ticket_sorted == expected_sorted:
        print(f"\r🚀{colors.F_RED}Угадали! Количество попыток:{attempts}, потрачено денег: {a} рублей, стоимость одного билета: {PRICE}{colors.RESET}")
        attempts = 0
        a = 0
        print(f"{colors.F_BLUE_U}Номера в билете: {expected_sorted}")
        print(f"{colors.F_BLUE_U}Выпавшие номера: {ticket_sorted}")
        break