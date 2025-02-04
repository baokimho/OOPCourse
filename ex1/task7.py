def arithmetic_progression(max_value):
    a = 3  # First term
    d = 3  # Common difference
    terms = []
    
    while a <= max_value:
        terms.append(a)
        a += d
    
    return terms

def count_terms(terms):
    return len(terms)

def sum_of_terms(terms):
    return sum(terms)

def sum_of_squared_terms(terms):
    return sum(x**2 for x in terms)

def main():
    max_value = int(input("Enter the maximum value of the AP: "))
    terms = arithmetic_progression(max_value)
    
    num_terms = count_terms(terms)
    sum_terms = sum_of_terms(terms) 
    sum_squared_terms = sum_of_squared_terms(terms)
    
    print(f"Number of terms: {num_terms}")
    print(f"Sum of terms: {sum_terms}")
    print(f"Sum of squared terms: {sum_squared_terms}")

if __name__ == "__main__":
    main()