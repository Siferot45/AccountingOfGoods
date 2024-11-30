class Shop:
    def __init__(self):
        """
        Инициализация менеджера продуктов, который использует файл для хранения данных о продуктах.

        Атрибуты:
            __file_name (str): Имя файла, в котором хранятся данные о продуктах (по умолчанию 'products.txt').
        """
        self.__file_name = 'products.txt'
        
    def get_products(self):
        """
        Читает список продуктов из файла.

        Возвращает:
            str: Содержимое файла с данными о продуктах, разделённое символами новой строки.
        """
        with open(self.__file_name) as file:
            return file.read()

    def add(self, *products):
        """
        Добавляет новые продукты в файл, если их нет в списке.

        Аргументы:
            *products (Product): Продукты для добавления. Каждый продукт должен быть экземпляром класса `Product`.

        Выводит:
            str: Сообщение, если продукт уже есть в магазине.
        """
        list_product = self.get_products().split('\n')

        # Создаем множество с именами уже существующих продуктов
        existing_names = {line.split(', ')[0] for line in list_product}

        # Открываем файл для записи новых продуктов
        with open(self.__file_name, 'w') as file:
            for product in products:
                
                # Проверка, если продукт уже существует
                if product.name in existing_names:
                    print(f'Продукт {product} уже есть в магазине')
                else:
                    # Записываем новый продукт в файл
                    file.write(str(product) + '\n')