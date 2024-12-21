def is_even(z):
    if z % 2 == 0:
        print(z, 'is even')
        return True
    else:
        print(z, 'is odd')
        return False

first = 0
second = 1
even_sum = 0

while first < 4 * 10**6:
    if is_even(first):
        even_sum += first

    new = first + second
    first = second
    second = new

print(even_sum, ': is the sum of even numbers from 0 to', 4 * 10**6)
