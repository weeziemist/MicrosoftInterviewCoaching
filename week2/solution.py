def string_to_integer(str):
        if len(str) == 0:
            return 0
            
        result = 0
        multiplier = 1
        index = 0
        sign = {'+': 1, '-': -1}
        
        if str[0] in sign:
            multiplier = sign[str[0]]
            index = 1
            
        while index < len(str):
            c = str[index]
            if ord(c) >= ord('0') and ord(c) <= ord('9'):
                result *= 10
                result += ord(c) - ord('0')
            else:
                return 0
            index += 1
        
        result *= multiplier
        if result > 2147483647 or result < -2147483648:
            return 0
        return result

def main():
    expected = {'64': 64, '-64': -64, '': 0, '785fjhf': 0, '3000000000': 0, '8964': 8964, '-567': -567, '0001': 1, '   10  ': 0}
    passed = 0
    failed = 0
    for key in expected:
        if string_to_integer(key) == expected[key]:
            print('passed')
            passed += 1
        else:
            print('failed, case: %s, actual: %s, expected: %s' % (key, string_to_integer(key), expected[key]))
            failed += 1
    print('passed %s, failed %s.' % (passed, failed))

main()