inversion = '-'

priority = ['-', '&', 'v', '>', '=']


def rule_rpe_brackets(s_string_first):  # Добавляет скобки к аргументам
    open_bracket = '('
    close_bracket = ')'
    reserved_symbols = priority
    reserved_symbols.append(open_bracket)
    reserved_symbols.append(close_bracket)
    i = 0
    y = 0
    while i < len(s_string_first) - 1:
        if s_string_first[i] not in reserved_symbols:
            if s_string_first[i - 1] != open_bracket or s_string_first[i + 1] != close_bracket:
                s_string_first = s_string_first.replace(s_string_first[i],
                                                        open_bracket + s_string_first[i] + close_bracket)
        i += 1
    if s_string_first[len(s_string_first) - 1] not in reserved_symbols:
        s_string_first = s_string_first.replace(s_string_first[len(s_string_first) - 1],
                                                open_bracket + s_string_first[len(s_string_first) - 1] + close_bracket)
    return s_string_first


def rule_inversion(s_sting):  # добавляет скобки к отрицанию
    open_bracket = '('
    close_bracket = ')'
    s_in_bracket = ''
    counter_open_brackets = 0
    counter_close_brackets = 0
    i = len(s_sting) - 1
    while i >= 0:
        if s_sting[i] == '-':
            s_in_bracket += s_sting[i]
            y = i
            while ((
                           counter_open_brackets == 0 or counter_close_brackets == 0) or counter_open_brackets != counter_close_brackets) and y < len(
                    s_sting) - 1:
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
            if s_sting[i - 1] != open_bracket or s_sting[y + 1] != close_bracket:
                s_sting = s_sting.replace(s_in_bracket, open_bracket + s_in_bracket + close_bracket)
                i = len(s_sting)
        s_in_bracket = ''
        i -= 1  # убрать к
    return s_sting


def rule_conjunction(s_string_con, operation):  # два аргумента , левоассоциативность
    open_bracket = '('
    close_bracket = ')'
    s_in_bracket = ''
    counter_open_brackets = 0
    counter_close_brackets = 0
    equals_counters = 0
    i = 0
    k = 0
    y = 0
    while i < len(s_string_con) - 1:
        if s_string_con[i] == operation:
            y = i
            while ((
                           counter_open_brackets == 0 or counter_close_brackets == 0) or counter_open_brackets != counter_close_brackets) and y < len(
                    s_string_con) - 1:
                y -= 1
                if s_string_con[y] == open_bracket:
                    counter_open_brackets += 1
                if s_string_con[y] == close_bracket:
                    counter_close_brackets += 1
            counter_close_brackets = 0
            counter_open_brackets = 0
            k = y
            while equals_counters < 2 and y < len(s_string_con) - 1:
                if s_string_con[y] == open_bracket:
                    counter_open_brackets += 1
                if s_string_con[y] == close_bracket:
                    counter_close_brackets += 1
                s_in_bracket += s_string_con[y]
                if counter_open_brackets == counter_close_brackets and counter_close_brackets + counter_open_brackets > 0:
                    equals_counters += 1
                    counter_close_brackets = 0
                    counter_open_brackets = 0
                y += 1
            if y == len(s_string_con) - 1 or k == 0:
                s_string_con = s_string_con.replace(s_in_bracket, open_bracket + s_in_bracket + close_bracket)
            elif s_string_con[k - 1] != open_bracket and s_string_con[y + 1] != close_bracket and len(s_in_bracket) > 0:
                s_string_con = s_string_con.replace(s_in_bracket, open_bracket + s_in_bracket + close_bracket)
            s_in_bracket = ''
            i+=1
        i += 1
        equals_counters = 0
        counter_close_brackets = 0
        counter_open_brackets = 0
    return s_string_con

def rule_implication(s_string_imp):
    open_bracket = '('
    close_bracket = ')'
    s_in_bracket = ''
    counter_open_brackets = 0
    counter_close_brackets = 0
    equals_counters = 0
    i = len(s_string_imp) - 1
    k = 0
    y = 0
    while i > 0:
        if s_string_imp[i] == '>':
            y = i
            while (counter_open_brackets == 0 or counter_close_brackets == 0) or counter_open_brackets != counter_close_brackets:
                y -= 1
                if s_string_imp[y] == open_bracket:
                    counter_open_brackets += 1
                if s_string_imp[y] == close_bracket:
                    counter_close_brackets += 1
            counter_close_brackets = 0
            counter_open_brackets = 0
            k = y
            while equals_counters < 2 and y < len(s_string_imp) - 1:
                if s_string_imp[y] == open_bracket:
                    counter_open_brackets += 1
                if s_string_imp[y] == close_bracket:
                    counter_close_brackets += 1
                s_in_bracket += s_string_imp[y]
                if counter_open_brackets == counter_close_brackets and counter_close_brackets + counter_open_brackets > 0:
                    equals_counters += 1
                    counter_close_brackets = 0
                    counter_open_brackets = 0
                y += 1
            if y == len(s_string_imp) - 1 or k == 0:
                s_string_imp = s_string_imp.replace(s_in_bracket, open_bracket + s_in_bracket + close_bracket)
                i = len(s_string_imp)
            elif s_string_imp[k - 1] != open_bracket and s_string_imp[y + 1] != close_bracket and len(s_in_bracket) > 0:
                s_string_imp = s_string_imp.replace(s_in_bracket, open_bracket + s_in_bracket + close_bracket)
                i = len(s_string_imp)
            s_in_bracket = ''
            i -= 1
        i -= 1
        equals_counters = 0
        counter_close_brackets = 0
        counter_open_brackets = 0
    return s_string_imp

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
s = rule_conjunction(s, '&')
print(s, 'rule_&')
s = rule_conjunction(s, 'v')
print(s, 'rule_v')
s = rule_conjunction(s, '=')
print(s, 'rule_=')
s = rule_implication(s)
print(s , 'rule_>')
print(s)
