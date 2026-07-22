def sell_coke():
    change = 0
    coke_price = 50
    print(f"Amount Due: {coke_price}")
    amount = int(input("Insert Coin: "))
    if amount != 25 or amount != 10 or amount != 5:
        print("Amount Due: ", 50)
        amount = int(input("Insert Coin: "))
        change += amount
    while amount < coke_price:
        coke_price = coke_price - amount
        print(f"Amount Due: {coke_price}")
        amount = int(input("Insert Coin: "))
        change += amount
    print(f"Change Owed: {change - 50}")


sell_coke()
