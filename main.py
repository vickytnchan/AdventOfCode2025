### Counts the number of times the dial lands on zero
def count_zeros(filename, starting_dial_number):
    print(f"Starting dial number is {starting_dial_number}.")

    with open(filename, "r") as f:
        lines = f.readlines()

    new_dial_number = int(starting_dial_number)
    zeros_total = 0
    for line in lines:
        number_to_increment_by = int(line.strip()[1:])
        if "R" in line:
            line.strip()
            operation = "add"
            new_dial_number += number_to_increment_by
        elif "L" in line:
            operation = "subtract"
            new_dial_number -= number_to_increment_by
        else:
            print("Error: line does not contain L or R")
        while new_dial_number > 99:
            new_dial_number -= 100
        while new_dial_number < 0:
            new_dial_number += 100
        if new_dial_number == 0:
            print("Dial is on zero! Adding 1 to the zeros_total.")
            zeros_total += 1
        else:
            print(f"New dial number: {new_dial_number}")

    print(f"Total number of times the dial stopped at zero: {zeros_total}. "
          f"Therefore password is '{zeros_total}'.")

if __name__ == '__main__':
    count_zeros("input.txt", 50)

