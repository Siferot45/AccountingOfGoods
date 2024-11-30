class Product:
    """
    Класс, представляющий продукт с именем, весом и категорией.

    Атрибуты:
        name (str): Название продукта.
        weight (float): Вес продукта в килограммах.
        category (str): Категория, к которой относится продукт.

    Методы:
        __str__(): Возвращает строковое представление объекта `Product`.
    """
    
    def __init__(self, name, weight, category):
        """
        Инициализация нового продукта.

        Аргументы:
            name (str): Название продукта.
            weight (float): Вес продукта в килограммах.
            category (str): Категория продукта (например, "Еда", "Одежда").
        """
        self.name = name
        self.weight = weight
        self.category = category
        
    def __str__(self):
        """
        Возвращает строковое представление объекта `Product`.

        Возвращает:
            str: Строковое представление продукта в формате "name, weight, category".
        """
        return(f'{self.name}, {self.weight}, {self.category}')
