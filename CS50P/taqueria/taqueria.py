def main():
    total = 0
    while True:
        try:
            food = input("Item: ").lower().title()
            if food in foods:
                price = foods[food]
                total += price
                print(f"Total: ${total:.2f}")
            else:
                continue
        except EOFError:
            break

    return total

foods = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

if __name__ == "__main__":
    main()
