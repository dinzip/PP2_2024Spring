import re

def test(pattern, text, testnum, result):
    res = re.sub(pattern, ':', text)
    print(res)
    if res == result:
        print(f'Test {testnum} passed!')
    else:
        print(f'Test {testnum} didn\'t pass')

pattern = r'[\s,.]'
test(pattern, 'my name, gl.,4', 1, 'my:name::gl::4')
