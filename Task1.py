import math

def is_palindrome(x):
    is_palindrome = x == x[::-1]

    char_freq = {}
    for char in x:
        if char in char_freq:
            char_freq[char] += 1
        else:
            char_freq[char] = 1
            
    return (is_palindrome, char_freq)


def is_prime(n):
    if n <= 1:
        return {}, {}  
    
    divisibility_check = {}
    divisors_used = []
    
    for i in range(2, int(math.sqrt(n)) + 1):
        divisible = n % i == 0
        divisibility_check[i] = divisible
        if divisible:
            divisors_used.append(i)
    
    return divisibility_check, {'divisors_used': divisors_used}

def main():
    results = []
    failed_attempts = []
    
    for attempt in range(3):
        try:
            user_string = input("Enter a string: ")
            palindrome_result, char_frequencies = is_palindrome(user_string)
            
            user_number = int(input("Enter a number: "))
            divisibility_check, divisors_used = is_prime(user_number)
            
            result_dict = {
                "user_input": {
                    "string": user_string,
                    "number": user_number
                },
                "palindrome_result": palindrome_result,
                "char_frequencies": char_frequencies,
                "divisibility_check": divisibility_check,
            }
            
            results.append(result_dict)
            break
            
        except ValueError as e:
            print(f"Invalid input: {e}")
            failed_attempts.append((input("Please re-enter your input: "), str(e)))
            
            if attempt == 2:
                print("Maximum attempts reached. Exiting.")
                break
            
    print("\nResults:")
    for result in results:
        print(result)

    if (failed_attempts):    
        print("\nFailed Attempts:")
        for failed in failed_attempts:
            print(failed)


main()
