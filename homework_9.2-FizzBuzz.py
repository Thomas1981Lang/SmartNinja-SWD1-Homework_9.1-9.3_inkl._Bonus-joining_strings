

print('')
print('')
print('Welcome to FizzBuzz!')
print('')

while True:

    print('Please select a number between 1 and 100 or "e" for Exit')
    counter_input = input('Your choice: ');

    if counter_input.lower() == 'e':
        print('')
        print('')
        # Debug
        print('Debug Exit')
        # Debug
        print('Goodbye, see you next time')
        break

    elif counter_input.isdigit() and int(counter_input) >= 1 and int(counter_input) <= 100:
        print('')
        print('')
        # Debug
        print('Debug counter.isdigit() and counter >= 1 and counter <= 100')
        # Debug

        for x in range(1, int(counter_input) + 1):
            diff_three = x % 3
            diff_five = x % 5
            if diff_three == 0 and diff_five == 0:
                print('fizzbuzz')
            elif diff_five == 0:
                print('buzz')
            elif diff_three == 0:
                print('fizz')
            else:
                print(x)
        print('')
        print('')

    else:
        print('')
        print('')
        # Debug
        print('Debug else')
        # Debug
        print('An error occurred while entering, please try again!')