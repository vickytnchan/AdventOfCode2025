'''

I was so close to the solution, but switched to an LLM suggested fix and got stuck for hours because I don't intuitively understand how floor behaves.

Lessons learnt:
Don't use LLM suggestions of replacement functions that you don't find intuitive / can't understand (like floor)
Rather prefer to keep the code that you've built up from your understanding of the coding problem
You may be closer to the solution than you think.
Create and use test data + breakpoints/ build unit tests for testing edge cases
'''

### Counts the number of times the dial lands on or passes zero
def count_zeros(filename, starting_dial_number):
    print(f"Starting dial number is {starting_dial_number}.")

    with open(filename, "r") as f:
        lines = f.readlines()

    new_dial_number = int(starting_dial_number)
    landed_zeros_total = 0
    pass_over_zeros_total = 0
    for index, line in enumerate(lines):
        number_to_increment_by = int(line.strip()[1:])

        dial_number_before_instruction = new_dial_number
        if "L" in line:
            number_to_increment_by *= -1
        elif "R" not in line:
            instruction_number = index + 1
            raise Exception(f"Error: the instruction '{line}' from line {instruction_number} of {filename} does not contain L or R.")

        new_dial_number += number_to_increment_by

        print(f"Operation: {number_to_increment_by} as instruction was {line.strip("\n")}. ")

        landed_on_zero = False
        times_passed_over_zero_this_turn = 0

        if new_dial_number == 0:
            print("Dial landed on zero! Adding 1 to the landed_zeros_total.")
            new_dial_number = 0
            landed_on_zero = True
            landed_zeros_total += 1

        if new_dial_number < 0 and dial_number_before_instruction != 0:
            times_passed_over_zero_this_turn += 1
            print("Went from positive to negative")

        if abs(new_dial_number) > 99:
            times_passed_over_zero_this_turn += abs(int(new_dial_number/100))
            if new_dial_number % 100 == 0:
                print("Dial landed on zero! Adding 1 to the landed_zeros_total.")
                landed_on_zero = True
                landed_zeros_total += 1
                times_passed_over_zero_this_turn -= 1
            new_dial_number %= 100

        if new_dial_number < 0:
            new_dial_number += 100

        if times_passed_over_zero_this_turn > 0:
            pass_over_zeros_total += times_passed_over_zero_this_turn
            print(f"The instruction '{line.strip()}' applied to {dial_number_before_instruction} means that the dial passes over zero {times_passed_over_zero_this_turn} times. "
                  f"\nNew pass_over_zeros_total is {pass_over_zeros_total}.")

        total_zeros = pass_over_zeros_total + landed_zeros_total
        if landed_on_zero or times_passed_over_zero_this_turn > 0:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print(f"New total_zeros is {total_zeros}")

        print(f"New dial number: {new_dial_number}.\n")


    print(f"Total number of times the dial stopped at zero: {landed_zeros_total}. "
          f"Number of additional times the dial passed over zero: {pass_over_zeros_total}. "
          f"Therefore password is '{total_zeros}'.")

if __name__ == '__main__':
    count_zeros("input.txt", 50)
