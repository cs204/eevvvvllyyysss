def main():
    greeting = input("Приветствие: ")

    if greeting.lower().startswith("здравствуйте"):
        print("$0")
    elif greeting.lower().startswith("з"):
        print("$20")
    else:
        print("$100")

if __name__ == "__main__":
    main()
