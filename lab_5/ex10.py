import re

def test(pattern, func, text, testnum, result):
    res = re.sub(pattern, func, text)
    print(res)
    if res == result:
        print(f'Test {testnum} passed!')
    else:
        print(f'Test {testnum} didn\'t pass')

pattern = r'.[A-Z]'
change_to = lambda a: f'{a.group().lower()[0]}_{a.group().lower()[1]}'
test(pattern, change_to, 'YouTube, iPhone and eBay', 1, 'You_tube, i_phone and e_bay')