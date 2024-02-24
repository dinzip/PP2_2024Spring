import re

def test(pattern, text, testnum, result):
    res = re.sub(pattern, r'\1 \2', text)
    print(res)
    if res == result:
        print(f'Test {testnum} passed!')
    else:
        print(f'Test {testnum} didn\'t pass')

pattern = r'(?P<low>\w)(?P<upp>[A-Z])'
test(pattern, "MySuperTest", 1, "My Super Test")
test(pattern, " MySuperTest IAmRobot", 2, " My Super Test I Am Robot")