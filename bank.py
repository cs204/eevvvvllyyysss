def value(greeting):
    if greeting.lower().startswith("здравствуйте"):
        return 0
    elif greeting.lower().startswith("з"):
        return 20
    else:
        return 100

def main():
    greeting = input("Введите приветствие: ")
    print(f"${value(greeting)}")

if __name__ == "__main__":
    main()
