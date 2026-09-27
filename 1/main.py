import math
import random

CONSTK = 5 # кільксіть раундів для теаореми ферма (більше краще)

def checkPrimeNumber(nums : list[int]) -> int : # метод пробного ділення
    primeCounter = 0

    for i in nums :
        if i > 1 :
            for j in range(2, int(i**0.5)+1) :
                if i % j == 0:
                    break
            else:
                primeCounter += 1

    return primeCounter

def checkPrimeWilson(nums : list[int]) -> int : # теорема вілсона : ((n-1)! +1) % n == 0
    primeCounter = 0

    for n in nums :
        if n > 1:
            if (math.factorial(n-1)+1) % n != 0 :
                break
        else:
            primeCounter += 1

    return primeCounter

def checkPrimeFerma(nums : list[int]) -> int : # теорема ферма : a^(p-1) == 1 (mod p)
    primeCounter = 0

    for n in nums :
        if n <= 1 :
            continue
        if n in (2,3):
            primeCounter += 1
            continue
        if n % 2 == 0:
            continue

        for _ in range(CONSTK) :
            a = random.randint(2, n - 2)
            if pow(a, n-1, n) != 1 :
                break
        else:
            primeCounter += 1

    return primeCounter

def main() :
    rawInp = input("Введіть числа для перевірки через кому(наприклад: 1, 2,3): ").strip()
    numsList = []

    for i in rawInp.split(","):
        try:
            numsList.append(int(i))
        except ValueError:
            continue

    print(f"Очищений список цілих чисел: {numsList}")
    print("КІлькість простих чисел різними способами:\n"
    f"Методом пробного ділення: {checkPrimeNumber(numsList)}\n"
    f"За теоремою Вілсона: {checkPrimeWilson(numsList)}\n"
    f"За теоремою Ферма: {checkPrimeFerma(numsList)}")
    

if __name__ == "__main__" :
    main()