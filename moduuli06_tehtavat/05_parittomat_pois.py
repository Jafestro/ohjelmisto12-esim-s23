# Funktio puhdistaa parittomat luvut pois listalta
def only_even(numbers):
    evens = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
    return evens


# data
lukuja = [0, 1, 5, 8, 9, 10, 22, 44, 55, 88, 77, 77, 77, 77, 77, 77, 99, 99]

print(f"Alkuperäinen lista\n {lukuja}")
print(f"Muokattu/karsittu lista\n {only_even(lukuja)}")
