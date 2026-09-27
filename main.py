import math
import random

CONSTK = 20
MAX_WILSON = 1000
MAX_TRIVDIV = 10**12


def isPrimeTrivDiv(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True


def isPrimeWilson(n: int) -> bool:
    if n <= 1:
        return False
    return (math.factorial(n - 1) + 1) % n == 0


def isPrimeMillRab(n: int, k: int = CONSTK) -> bool:
    if n <= 1:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0:
        return False

    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue

        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True


def main():
    raw_inp = input("Введіть числа через кому: ").strip()
    nums = []
    for item in raw_inp.split(","):
        try:
            nums.append(int(item.strip()))
        except ValueError:
            continue

    if not nums:
        print("Список чисел порожній.")
        return

    print(f"\nОчищений список чисел: {nums}\n")

    mrCount = sum(1 for n in nums if isPrimeMillRab(n))
    print(f"Метод Міллера — Рабіна: {mrCount}")

    trivValid = [n for n in nums if n < MAX_TRIVDIV]
    trivCount = sum(1 for n in trivValid if isPrimeTrivDiv(n))
    trivSkipped = len(nums) - len(trivValid)
    skipMsg = f" (пропущено {trivSkipped} чисел > {MAX_TRIVDIV})" if trivSkipped else ""
    print(f"Пробне ділення: {trivCount}{skipMsg}")

    wilsonValid = [n for n in nums if n <= MAX_WILSON]
    wilsonCount = sum(1 for n in wilsonValid if isPrimeWilson(n))
    wilsonSkipped = len(nums) - len(wilsonValid)
    skipMsg = f" (пропущено {wilsonSkipped} чисел > {MAX_WILSON})" if wilsonSkipped else ""
    print(f"Теорема Вілсона: {wilsonCount}{skipMsg}")


if __name__ == "__main__":
    main()