import os

def word_stats(path : str) -> float | None:
    if not path.endswith(".txt"):
        print(f"ERR! Підтримуються тільки файли з розширенням .txt")
        return None

    try:
        with open(path, "r", encoding="utf-8") as f:
            line = f.read()
    except FileNotFoundError:
        print(f"ERR! Файл {path} відсутній в поточній дерикторії")
        return None

    raw_words = line.split()
    words = []
    for word in raw_words:
        cleaned = "".join(ch for ch in word if ch.isalpha())
        if cleaned:
            words.append(cleaned)

    if not words:
        return None

    words_count = len(words)
    words_longest = max(words, key=len)
    words_shortest = min(words, key=len)
    words_average = sum(len(w) for w in words) / words_count
    
    reports_lines = [
        f"{'Слів:':.<18}{words_count:.>14}\n",
        f"{'Найдовше:':.<18}{words_longest:.>14}\n",
        f"{'Найкоротше:':.<18}{words_shortest:.>14}\n",
        f"{'Середня довжина:':.<18}{words_average:.>14.2f}\n"
    ]

    base_name = os.path.splitext(path)[0]
    out_path = f"{base_name}_report.txt"

    with open(out_path, "w", encoding="utf-8") as f:
        f.writelines(reports_lines)

    return round(words_average, 2)

def main():
    try:
        path = input("Введіть шлях до вхідного файлу: ").strip()

        if not path:
            print("ERR! Шлях до файлу не може бути порожнім")
            return

        result = word_stats(path)
        if result is None:
            print("ERR! Не вдалося обчислити статистику слів")
            return

        base_name = os.path.splitext(path)[0]
        print(f"Звіт успішно збережено у: {base_name}_report.txt\nСередня довжина слова: {result}")

    except (PermissionError, UnicodeDecodeError, ValueError, KeyboardInterrupt, OSError) as err:
        print(f"ERR! Помилка під час виконання програми {err}")

if __name__ == "__main__" :
    main()