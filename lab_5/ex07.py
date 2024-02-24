import re

def test(pattern, text, testnum, result):
    res = re.sub(pattern, lambda a: a.group('ch').upper(), text)
    print(res)
    if res == result:
        print(f'Test {testnum} passed!')
    else:
        print(f'Test {testnum} didn\'t pass')

pattern = r'_(?P<ch>.)'
test(pattern, 'l_str_fdew f_Re_ds_dop', 1, 'lStrFdew fReDsDop')