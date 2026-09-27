import math


def checkPrimeNumber(nums : list[int]) -> int :
    primeCount = 0

    for i in nums :
        if nums > 1 :
            for j in range(2, int(i**0,5)+1) :
                if i % j == 0:
                    break
        else:
            primeCount += 1

    return primeCount

def checkPrimeWilson(nums : list[int]) -> int :
    primeCount = 0

    for n in nums:
        if (math.factorial(n-1)+1) % n != 0 :
            pass
        else:
            primeCount += 1

    return primeCount


def checkPrimeFerma() :
    pass



def main() :
    rawInp = input("Введіть числа для перевірки через кому(наприклад: 1, 2,3): ")
    numsList = []

    for i in rawInp.split(", "):
        try:
            numsList.append(int(i))
        except ValueError:
            continue

    print(f"Очищений список цілих чисел: {numsList}")
    

if __name__ == "__main__" :
    main()