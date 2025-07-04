def q1(x1, x2, y1, y2):
    dst = lambda x1, y1, x2, y2: ((x1 - x2)**2 + (y1 - y2)**2)**0.5
    return dst(x1, x2, y1, y2)

def q2():
    A = [1, 2, 3, 4, 5, 6, 7, 8]
    L=[]
    L = list(map(lambda x:x ** 3,A))
    print("Generate the power of 3 of each element in A", L)

    R = list(filter(lambda x: 20 <= x <= 40, map(lambda x:x ** 2,A)))
    print("Return the resultant square in the range of [20, 40]: ", R)

    E = list(filter(lambda x: x % 2 == 0, A))
    print("Even number in A is: ", E)

def q3():
    inventory = [
    {"name": "Laptop", "price": 1200, "stock": 10, "catergories": ["electronics", "computers"]},
    {"name": "Smartphone", "price": 800, "stock": 0, "catergories": ["electronics", "mobiles"]},
    {"name": "Headphone", "price": 150, "stock": 25, "catergories": ["electronics", "audio"]},
    {"name": "Desk Chair", "price": 100, "stock": 5, "catergories": ["furniture", "office"]},
    {"name": "Notebook", "price": 5, "stock": 100, "catergories": ["stationery", "office"]},
    ]
    out_of_stock = list(filter(lambda x: x["stock"] == 0, inventory))
    if(any(out_of_stock)):
        print("Products that are out of stock: ", out_of_stock)
    else:
        print("There are not any products out of stock")

    category = input("Input a category: ")
    price = int(input("Input a price: "))

    check_products = list(filter(lambda i: category in i["catergories"] and i["stock"] > 0 and i["price"] > price, inventory))

    if check_products:
        print("Products in category", category, "with price >", price, "and in stock:", check_products)
    else:
        print("There are no products in this category that meet the conditions.")

def main():
    num = int(input("Select the question: "))

    if(num == 1):
        x1 = int(input("Input x1: "))
        x2 = int(input("Input x2: "))
        y1 = int(input("Input y1: "))
        y2 = int(input("Input y2: "))
        print("The distance (dst) of two pixels is ", q1(x1, x2, y1, y2))
    
    if(num == 2):
        q2()

    if(num == 3):
        q3()

main()