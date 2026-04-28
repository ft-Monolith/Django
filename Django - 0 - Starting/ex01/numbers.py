def display_numbers():
    with open("numbers.txt") as f:
        nbrs = f.read()
    
    numbers = nbrs.split(",")
    
    for number in numbers:
        print(number.strip())


if __name__ == '__main__':
    display_numbers()
