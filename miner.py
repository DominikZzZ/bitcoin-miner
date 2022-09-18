
from time import sleep, localtime
from random import choice, randint


chars ="abcdefghijklmnopqrstuwxyz"
chars_up = chars.upper()
digits = "1234567890"
all_chars = chars + chars_up + digits

btc_amount = 0


if __name__ == "__main__":
    while True:
        year = localtime().tm_year
        month = localtime().tm_mon
        day = localtime().tm_mday
        hour = localtime().tm_hour
        minute = localtime().tm_min
        second = localtime().tm_sec
        date = f"{day}/{month}/{year}, {hour}:{minute}.{second}"

        string = "".join(choice(all_chars) for i in range(64))

        if randint(0, 250) == 100: btc_amount += 0.0001

        sleep(0.125)

        print(f"[{date}] [{string}] [{round(btc_amount, 4)} btc]")
