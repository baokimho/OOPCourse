def factorials(n: int) -> dict:
    def factorial(x):
        result = 1
        for i in range(1, x + 1):
            result *= i
        return result
    
    return {i: factorial(i) for i in range(1, n + 1)}

# Example usage
k = factorials(5)
print(k[1])  
print(k[3])  
print(k[5])  
