import ast
from functools import wraps


def unique(genfunc):
    @wraps(genfunc)
    def wrapзer(*args, **kwargs):
        gen = genfunc(*args, **kwargs)
        seen = set()

        try:
            first = next(gen)
            has_first = True
        except StopIteration:
            has_first = False

        def inner():
            if has_first:
                seen.add(first)
                yield first
            for item in gen:
                if item not in seen:
                    seen.add(item)
                    yield item

        return inner()

    return wrapзer

@unique
def flatten(data: list):
    if not isinstance(data, list):
        raise TypeError(f"очікувався список, отримано {type(data).__name__}")

    for item in data:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item

def main():
    while True:
        raw_data = input("Вкладений список: ")
        try:
            parsed = ast.literal_eval(raw_data)
            if not isinstance(parsed, list):
                raise ValueError
            result = list(flatten(parsed))
            print(f"Результат: {result}")
            break
        except (SyntaxError, ValueError, TypeError,RecursionError):
            print("Помилка: некоректний запис списку")

if __name__ == "__main__":
    main()