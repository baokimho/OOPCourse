from task4 import count_negative_numbers

def count_even_numbers(numbers):
    return sum(1 for num in numbers if num % 2 == 0)

def main():
    numbers = []
    print("Enter integers (0 to stop):")
    while True:
        try:
            num = int(input())
            if num == 0:
                break
            numbers.append(num)
        except ValueError:
            print("Please enter a valid integer.")
    
    negative_count = count_negative_numbers(numbers)
    even_count = count_even_numbers(numbers)
    
    print(f"Number of negative integers: {negative_count}")
    print(f"Number of even integers: {even_count}")

if __name__ == "__main__":
    main()
