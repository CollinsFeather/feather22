def calculate_change(amount):
    coins = {'Half Dollar': 50, 'Quarter': 25, 'Dime': 10, 'Nickel': 5, 'Penny': 1}
    change = {}

    if amount < 1 or amount > 99:
        print("Please enter a number between 1 and 99.")
        return

    for coin_name, coin_value in coins.items():
        while amount >= coin_value:
            if coin_name in change:
                change[coin_name] += 1
            else:
                change[coin_name] = 1
            amount -= coin_value

    output = ""
    for coin_name, count in change.items():
        if count == 1:
            if coin_name == "Penny":
                output += f"one {coin_name}, "
            else:
                output += f"one {coin_name} "
        else:
            if coin_name == "Penny":
                output += f"{count} {coin_name}s, "
            else:
                output += f"{count} {coin_name}s "

    output = output.rstrip(", ")
    print("You have " + output + ".")

# Example usage
amount = int(input("Enter the amount (between 1 and 99): "))
calculate_change(amount)
