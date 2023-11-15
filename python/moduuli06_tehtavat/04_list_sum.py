def sum_numbers(numbers):
    summa = 0
    for num in numbers:
        summa += num
    return summa


lukuja = [0, 1, 5, 8, 9, 10, 22, 44, 55, 88, 77, 77, 77, 77, 77, 77, 99, 99]
print(f"Listassa olevien lukujen summa on: {sum_numbers(lukuja)}")
