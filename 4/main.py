import json


class DictMixin:
    def to_dict(self) -> dict:
        return { k: v for k, v in self.__dict__.items() if not k.startswith('_')}

    def to_json(self) -> str:
        return json.dumps(self.to_dict(), ensure_ascii=False)


class CompareMixin:
    def key(self):
        raise NotImplementedError("Метод key() має бути ралізованим у підкласі")

    def __lt__(self, other):
        if not isinstance(other, CompareMixin):
            return NotImplemented
        return self.key() < other.key()

    def __eq__(self, other):
        if not isinstance(other, CompareMixin):
            return NotImplemented
        return self.key() == other.key()


class Product(DictMixin, CompareMixin):
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def key(self):
        return self.price

    def __repr__(self):
        return f"Product(name={self.name!r}, price={self.price})"


if __name__ == "__main__":
    print("MRO класу Product:")
    for cls in Product.mro():
        print(f" - {cls.__name__}")


    p1 = Product("Ноутбук", 35000.0)
    p2 = Product("Миша", 800.0)
    p3 = Product("Клавіатура", 1500.0)

    print("\nСловник (to_dict):",
          p1.to_dict())
    print("Json (to_json):",
          p1.to_json())

    products = [p1, p2, p3]
    print("\nДо Сортування:", products)
    print("Після сортування за ціною:", sorted(products))
    print("p2 < p1:", p2 < p1)
    print("p1 == p2:", p1 == p2)