import re

def test(pattern, text, testnum, result):
    res = re.split(pattern, text)
    print(res)
    if res == result:
        print(f'Test {testnum} passed!')
    else:
        print(f'Test {testnum} didn\'t pass')

pattern = '[A-Z]'
test(pattern, 'iDamAdarynFFsoFmy:R8thWex', 1, ['i', 'am', 'daryn', '', 'so', 'my:', '8th', 'ex'])