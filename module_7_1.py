from Product import Product
from Shop import Shop

s1 = Shop()

p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2) 

s1.add(p1, p2, p3)

#print(s1.get_products())