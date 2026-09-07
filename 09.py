pin = "1234"
attempts = 0

while attempts < 3:
    user_pin = input("Enter PIN: ")

    if user_pin == pin:
        print("Access Granted!")
        break
    else:
        attempts += 1
        print("Wrong PIN")

if attempts == 3:
    print("ATM Locked!")