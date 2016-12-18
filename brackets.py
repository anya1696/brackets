inversion = '-'

priority = ['-', '&', 'v', '>', '=']


def rule_rpe_brackets(s_string_first):  # Добавляет скобки к аргументам
    open_bracket = '('
    close_bracket = ')'
    reserved_symbols = priority
    reserved_symbols.append(open_bracket)
    reserved_symbols.append(close_bracket)
    i = 0
    while i < len(s_string_first) - 1:
        print(i)
        if s_string_first[i] not in reserved_symbols:
            if s_string_first[i - 1] != open_bracket or s_string_first[i + 1] != close_bracket:
                s_string_first = s_string_first.replace(s_string_first[i], open_bracket + s_string_first[i] + close_bracket)
        i += 1
    if s_string_first[len(s_string_first) - 1] not in reserved_symbols:
        s_string_first = s_string_first.replace(s_string_first[len(s_string_first) - 1],open_bracket + s_string_first[len(s_string_first) - 1] + close_bracket)
    return s_string_first


def rule_inversion(s_sting):  # добавляет скобки к отрицанию
    open_bracket = '('
    close_bracket = ')'
    s_in_bracket = ''
    counter_open_brackets = 0
    counter_close_brackets = 0
    i = len(s_sting) - 1
    y = 0
    k = 0
    while i >= 0:
        if s_sting[i] == '-':
            s_in_bracket += s_sting[i]
            y = i
            while ((counter_open_brackets == 0 or counter_close_brackets == 0) or counter_open_brackets != counter_close_brackets) and y < len(
                    s_sting)-1:
                y += 1
                if s_sting[y] == open_bracket:
                    counter_open_brackets += 1
                if s_sting[y] == close_bracket:
                    counter_close_brackets += 1
                s_in_bracket += s_sting[y]
            counter_open_brackets = 0
            counter_close_brackets = 0
            if y + 1 > len(s_sting) - 1:
                y = -1
            if i - 1 < 0:
                i += 1
            if s_sting[i - 1] != open_bracket and s_sting[y + 1] != close_bracket:
                s_sting = s_sting.replace(s_in_bracket, open_bracket + s_in_bracket + close_bracket)
        s_in_bracket = ''
        k += 1
        i = len(s_sting) - 1 - k  # убрать к
    return s_sting


def rule_conjunction(s_string):
    open_bracket = '('
    close_bracket = ')'
    s_in_bracket = ''
    counter_open_brackets = 0
    counter_close_brackets = 0
    equals_counters = 0
    i = 0
    y = 0
    while i < len(s_string) - 1:
        print(i)
        if s_string[i] == '&':
            print('DAAAAAAAAAAAAAAAAAAAa')
            y = i
            while ((counter_open_brackets == 0 or counter_close_brackets == 0) or counter_open_brackets != counter_close_brackets) and y < len(s_string):
                y -= 1
                if s_string[y] == open_bracket:
                    counter_open_brackets += 1
                if s_string[y] == close_bracket:
                    counter_close_brackets += 1
                s_in_bracket += s_string[y]
                print(s_in_bracket, '| ', '|', open_bracket + s_in_bracket + close_bracket)
            counter_close_brackets = 0
            counter_open_brackets = 0
            print(y)
            while equals_counters != 2:
                if s_string[y] == open_bracket:
                    counter_open_brackets += 1
                if s_string[y] == close_bracket:
                    counter_close_brackets += 1
                s_in_bracket += s_in_bracket[y]
                if counter_open_brackets == counter_close_brackets:
                    equals_counters = +1
                y+=1
            s_string = s_string.replace(s_in_bracket, open_bracket + s_in_bracket + close_bracket)
            print(s_string)
        i+=1
    return s_string


s = input()
stest = [
    'a&bvc',
    'a>b=b>a',
    '-----c'
]
stest.append(s)
for c in s:
    if c == ' ':
        s = s.replace(c, '')
s = rule_rpe_brackets(s)
print(s, ' pre br')
s = rule_inversion(s)
print(s, 'rule_inversion')
#s = rule_conjunction(s)
print(s)
