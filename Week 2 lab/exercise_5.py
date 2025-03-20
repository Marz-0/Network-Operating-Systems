
#Exercise 5 - Functions

def add_numbers(a, b):
    return a + b


print(add_numbers(2, 5))



def find_max(numbers):
    return max(numbers)

print(find_max([10, 34, 11, 7]))  



def count_vowels(text):
    vowels = 'AEIOUaeiou'
    return sum(1 for char in text if char in vowels)

print(count_vowels("Hello there, how are you today?"))  




