
def pairs_with_sum( *numbers : int, target : int) -> list[tuple[int, int]]:
    """
    Пошук унікальних пар цілих чисел заданої суми

    Параметри
        *numbers - довільна кількість цілтх чисел
        target - цільовае значення суми

    Повертає відсортованйи список унікальних пар  
    """
    seen = set() 
    raw_pairs : list[tuple[int, int]] = []

    for num in numbers:
        diff = target - num
        if diff in seen:
            raw_pairs.append([min(diff, num), max(diff, num)])
        seen.add(num)

    unique_pairs = list({tuple(sorted(pair)) for pair in raw_pairs})

    return sorted(unique_pairs)
 
def main():
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