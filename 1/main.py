import math
import random

MAXF = 30000 # максимальне дозволене ціле число для перевірки щоб запобігти переповненнямм
CONSTK = 20 # кільксіть раундів для теаореми міллера-рабіна (більше краще)

def checkPrimeTrivDiv(nums : list[int]) -> int : # метод пробного ділення
    primeCounter = 0

    for n in nums :
        if n >= MAXF :
            print(f"[Trial division]Число {n} проіноровано - запобігання переповнення памяті")
            continue
        if n > 1 :
            for i in range(2, int(math.isqrt(n))+1) :
                if n % i == 0:
                    break
            else:
                primeCounter += 1

    return primeCounter

def checkPrimeWilson(nums : list[int]) -> int : # теорема вілсона : ((n-1)! +1) % n == 0
    primeCounter = 0

    for n in nums :
        if n >= MAXF :
            print(f"[Wilson]Число {n} проіноровано - запобігання переповнення памяті")
            continue
        if n > 1:
            if (math.factorial(n-1)+1) % n == 0 :
                primeCounter += 1

    return primeCounter

# def checkPrimeFermat(nums : list[int]) -> int : # теорема ферма : a^(p-1) == 1 (mod p)
#     primeCounter = 0

#     for n in nums :
#         if n >= MAXF :
#             print(f"[Fermat]Число {n} проіноровано - запобігання переповнення памяті")
#         else:
#             if n <= 1 :
#                 continue
#             if n in (2,3):
#                 primeCounter += 1
#                 continue
#             if n % 2 == 0:
#                 continue

#             for _ in range(CONSTK) :
#                 a = random.randint(2, n - 2)
#                 if pow(a, n-1, n) != 1 :
#                     break
#             else:
#                 primeCounter += 1

#     return primeCounter

def checkPrimeMillRab(nums : list[int]) -> int : # n-1 = 2^s * d
    primeCounter = 0

    for n in nums :
        if n >= MAXF :
            print(f"[Miller-Rabin]Число {n} проіноровано - запобігання переповнення памяті")
            continue
        else:
            if n <= 1:
                continue
        if n in (2, 3):
            primeCounter += 1
            continue
        if n % 2 == 0:
            continue

        d = n - 1
        s = 0
        while d % 2 == 0:
            d //= 2
            s += 1

        for _ in range(CONSTK):
            a = random.randint(2, n - 2)
            x = pow(a, d, n)

            if x == 1 or x == n - 1:
                continue

            for _ in range(s - 1):
                x = pow(x, 2, n)
                if x == n - 1:
                    break

            else:
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
    f"Методом пробного ділення: {checkPrimeTrivDiv(numsList)}\n"
    f"За теоремою Вілсона: {checkPrimeWilson(numsList)}\n"
    f"За теоремою Міллера-Рабіна: {checkPrimeMillRab(numsList)}")
    
    

if __name__ == "__main__" :
    main()