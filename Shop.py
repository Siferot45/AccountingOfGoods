class Shop:

    def __init__(self):
        self.__file_name = 'products.txt'
        
    def get_products(self):
        with open(self.__file_name) as file:
            for string in file:
                return string

    def add(self,*products):
        list_product = self.get_products()

        if list_product is not [x for x in products]:
            with open(self.__file_name, 'w') as file:
                file.write(file)