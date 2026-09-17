from lib import calculate_discount

def main():
    price = 1000.0
    discount = 15.0
    result = calculate_discount(price, discount)
    print(f"Початкова ціна: {price} грн")
    print(f"Ціна зі знижкою {discount}%: {result} грн")

if __name__ == "__main__":
    main()