def string_to_integer(str):
    try:
        assert(str != None)
        assert(len(str) != 0)
            
        result = 0
        multiplier = 1
        index = 0
        sign = {'+': 1, '-': -1}
        
        if str[0] in sign:
            multiplier = sign[str[0]]
            index = 1
            
        while index < len(str):
            c = str[index]
            assert(ord(c) >= ord('0') and ord(c) <= ord('9'))
            result *= 10
            result += ord(c) - ord('0')
            index += 1
        
        result *= multiplier
        assert(result <= 2147483647 and result >= -2147483648)
        return result
    except AssertionError:
        print('Invalid input.')

def main():
    print('input: 64, expected: %s, actual: %s' % (64, string_to_integer('64')))
    print('input: -64, expected: %s, actual: %s' % (-64, string_to_integer('-64')))
    string_to_integer('')
    print('input: 8964, expected: %s, actual: %s' % (8964, string_to_integer('8964')))
    print('input: -567, expected: %s, actual: %s' % (-567, string_to_integer('-567')))
    print('input: 0001, expected: %s, actual: %s' % (1, string_to_integer('0001')))
    string_to_integer('   10  ')
    string_to_integer(None)

main()