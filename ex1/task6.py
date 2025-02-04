from task5 import count_negative_numbers, count_even_numbers

def sum_positive_divisible_by_three(numbers):
    return sum(num for num in numbers if num > 0 and num % 3 == 0)


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
    
    # Using the functions from previous tasks
    negative_count = count_negative_numbers(numbers)
    even_count = count_even_numbers(numbers)
    sum_divisible_by_three = sum_positive_divisible_by_three(numbers)
    
    print(f"Number of negative integers: {negative_count}")
    print(f"Number of even integers: {even_count}")
    print(f"Sum of positive integers divisible by three: {sum_divisible_by_three}")

if __name__ == "__main__":
    main()
