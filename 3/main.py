
def pairs_with_sum( *numbers : int, target : int) -> list[tuple[int, int]]:
    """
    Пошук унікальних пар цілих чисел заданої суми

    Параметри
        *numbers - довільна кількість цілтх чисел
        target - цільовае значення суми

    Повертає відсортованйи список унікальних пар  
    """
    seen : set[int] = set()
    pairs : set[tuple[int, int]] = set()

    for num in numbers:
        diff = target - num
        if diff in seen:
            pairs.add((diff, num) if diff <= num else (num, diff))
            seen.remove(diff)
        else:
            seen.add(num)

    return sorted(pairs)

def main():
    print("\n Демонстраційні виклики з прикладів:")
    print(pairs_with_sum(1, 2, 3, 4 ,5, target=5)) #[(1, 4), (2, 3)]
    print(pairs_with_sum(1, 3, 3, target=4)) # [(1, 3)]  (друга 3 не використовується, бо 1 вже використана)
    print(pairs_with_sum(2, 2, 2, 2, target=4)) # [(2, 2)]  (пари унікальні)
    print(pairs_with_sum(1, 2, 3, target=10) , end="\n\n") # []

    try:
        raw_nums = input("Введіть ціли числа через кому або пробіл: ").replace(",", " ").split(' ')
        if not raw_nums:
            print("ERR! Список чисел не має бути порожнім")
            return

        nums = [int(item) for item in raw_nums]

        raw_target = input("Введіть цільову суму (target):").strip()
        if not raw_target:
            print("ERR! Цільова сума не має бути порожньою")
            return

        target = int(raw_target)

        result = pairs_with_sum(*nums, target=target)

        print(f"Вхідні числа: {nums}")
        print(f"Цільова сума: {target}")

        if result:
            print(f"Знайдені пари: {result}\nКількість пар: {len(result)}")
        else:
            print(f"Пар із заданою сумою ({target}) не знайдено")

        
    except ValueError :
        print("ERR! Вводьте лише цілі числа")
    except KeyboardInterrupt :
        print("Err! Виконання програми перервано")

if __name__ == "__main__":
    main()