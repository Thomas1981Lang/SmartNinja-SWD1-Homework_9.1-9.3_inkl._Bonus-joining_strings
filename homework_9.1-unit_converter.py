def kim(value):
    return value * 0.62137


def mik(value):
    return value / 0.62137


print('')
print('')
print('Welcome to Unity Converter | kilometer - miles')

while True:
    print('Do you want to convert kilometers to miles or miles to kilometers?')

    print('Options:')
    print('(1) kilometers into miles')
    print('(2) miles into kilometers')
    print('(e) Exit')
    print('')

    mode_choice = input('Choose: ')
    mode_choice = mode_choice.lower()

    if mode_choice == '1':
        print('')
        print('')
        # Debug
        print('Debug k_i_m')
        # Debug
        print('We are now converting kilometers to miles')
        print('')
        km = float(input('Kilometer: '))
        miles_converted = kim(km)
        print('{0} kilometers are {1} miles'.format(str(km), str(round(miles_converted, 3))))
        print('')
        print('')
    elif mode_choice == '2':
        print('')
        print('')
        # Debug
        print('Debug m_i_k')
        # Debeug
        print('We are now converting miles to kilometers')
        print('')
        miles = float(input('Miles: '))
        km_converted = mik(miles)
        print('{0} miles are {1} kilometers'.format(str(miles), str(round(km_converted, 3))))
        print('')
        print('')
    elif mode_choice == 'e':
        print('')
        print('')
        # Debug
        print('Debug Exit')
        # Debug
        print('Goodbye, see you next time')
        break
    else:
        print('')
        print('')
        # Debug
        print('Debug Else')
        # Debug
        print('An error occurred while entering, please try again!')
        print('')
