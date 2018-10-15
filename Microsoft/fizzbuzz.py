def fizzbuzz(number):
    count = 1
    for i in range(number+1):
        print(i)
    while count <= number: 
        if count % 3 == 0:
            print("Fizz")
        elif count %5 == 0:
            print("Buzz")
        else:
            print("fizzbuzz")
            print(count)
        count += 1
fizzbuzz(100)