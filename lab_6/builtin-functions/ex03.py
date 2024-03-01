def determine(test_num, test):
    rev_test = ''.join(list(reversed(test)))
    print('Test #{} is {} palindrom'.format(test_num, 'a' if rev_test == test else 'not a'))


a = input()

determine(1, a)