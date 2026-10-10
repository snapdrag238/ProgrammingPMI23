import json


class DictMixin:
    """
    Домішка для серіалізації публічних атрибутів об'єкта у словник та JSON
    """
    def to_dict(self) -> dict:
        """
        Повертає словник усіх публічних атрибутів екземпляра (без тих, що починаються з '_')
        """
        return { k: v for k, v in self.__dict__.items() if not k.startswith('_')}

    def to_json(self) -> str:
        """
        Повертає JSON-рядок із публічними атрибутами об'єкта
        """
        return json.dumps(self.to_dict(), ensure_ascii=False)


class CompareMixin:
    """
    Домішка для порівняння об'єктів за ключем, що повертає метод key()
    """
    def key(self):
        """
        Абстрактний метод, який повинен повертати ключ для порівняння об'єктів
        """
        raise NotImplementedError("Метод key() має бути реалізованим у підкласі")

    def __lt__(self, other):
        """
        Порівняння 'менше' (<) за значенням key()
        """
        if not isinstance(other, CompareMixin):
            return NotImplemented
        return self.key() < other.key()

    def __eq__(self, other):
        """
        Порівняння на рівність (==) за значенням key()
        """
        if not isinstance(other, CompareMixin):
            return NotImplemented
        return self.key() == other.key()


class Product(DictMixin, CompareMixin):
    """
    Клас товару, що підтримує серіалізацію та порівняння за ціною
    """
    def __init__(self, name: str, price: float):
        """
        Ініціалізує назву та ціну товару
        """
        self.name = name
        self.price = price

    def key(self):
        """
        Повертає ціну як ключ для порівняння товарів
        """
        return self.price

    def __repr__(self):
        """
        Повертає тектсове представлення об'єкта Product
        """
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