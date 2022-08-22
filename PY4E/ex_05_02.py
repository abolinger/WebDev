largest = None
smallest = None
while True:
    num = input('Enter a number: ')
    if num == 'done':
        break
    try:
        n = int(num)
    except:
        print('Invalid input')
        continue
    if largest is None or n > largest:
        largest = n
    elif smallest is None or n < smallest:
        smallest = n
print('Maximum is', largest)
print('Minimum is', smallest)
