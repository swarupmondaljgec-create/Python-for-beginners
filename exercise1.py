def count_numbers(mode, numbers):
    if mode == 'even':
        return sum(1 for n in numbers if n % 2 == 0)
    elif mode == 'odd':
        return sum(1 for n in numbers if n % 2 != 0)
    else:   
        return -1
even_count = count_numbers('even', [1, 2, 3, 4, 5])  # Output: 2
print(even_count)
odd_count = count_numbers('odd', [1, 2, 3, 4, 5])   # Output: 3
print(odd_count)
prime_count = count_numbers('prime', [1, 2, 3, 4, 5]) # Output: -1
print(prime_count)