class Calculator:
    def __init__(self):
        self.numbers = []

    def get_inputs(self):
        self.numbers = []
        print("Enter numbers one by one. Type 'done' when finished:")
        while True:
            user_input = input("Enter a number: ")
            if user_input.lower() == 'done':
                break
            try:
                number = float(user_input)
                self.numbers.append(number)
            except ValueError:
                print("Invalid input! Please enter a valid number.")

    def calculate_sum(self):
        return sum(self.numbers)

    def calculate_difference(self):
        if not self.numbers:
            return 0
        result = self.numbers[0]
        for num in self.numbers[1:]:
            result -= num
        return result

    def calculate_product(self):
        if not self.numbers:
            return 0
        product = 1
        for num in self.numbers:
            product *= num
        return product

    def calculate_average(self):
        if not self.numbers:
            return 0
        return sum(self.numbers) / len(self.numbers)

def main():
    calc = Calculator()
    
    while True:
        print("My calculator")
        print("1. Sum")
        print("2. Difference")
        print("3. Product")
        print("4. Average")
        print("5. Exit")

        choice = input("Choose an operation (1-5): ")

        if choice == '5':
            print("Exiting calculator. Goodbye!")
            break

        calc.get_inputs()

        if choice == '1':
            print("Sum:", calc.calculate_sum())
        elif choice == '2':
            print("Difference:", calc.calculate_difference())
        elif choice == '3':
            print("Product:", calc.calculate_product())
        elif choice == '4':
            print("Average:", calc.calculate_average())
        else:
            print("Invalid choice. Please select 1-5.")

# Run the program
main()
