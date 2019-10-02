str_one = 'Happy'
str_two = 'Day'

print(str_one + str_two + ' is the same as {}{}'.format(str_one, str_two))

print('')
print('')

print(str_one + ' ' + str_two + ' is the same as {} {}'.format(str_one, str_two))

print('')
print('')

print('%s %s ' % (str_one, str_two) + 'is the same as {1} {0}'.format(str_two, str_one) + ' and ' + str_one + ' ' + str_two)

print('')
print('')

print('{0} {1} is the same as {3} {2}'.format(str_one, str_two, str_two, str_one))

print('')
print('')