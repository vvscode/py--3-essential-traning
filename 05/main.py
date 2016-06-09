#!/usr/local/bin/python3
def main():
    num = 5
    num2 = 42.3
    print(num, type(num))
    print(num2, type(num2))
    print(num / 2, type(num / 2))
    print(float(5), type(float(5)))

    s = r'This is \n string'
    print(s)
    s2 = 'This is \nstring'
    print(s2)
    # new style
    print('This is {} forty two'.format(42))
    # old style:
    x = 23
    print("this is a twenty three %s number" % x)
    print('''
    Test
    ''')
    # or
    m_string = '''
        here
        multiple
        rows
    '''
    print(m_string)

    v_tuple = (1, 2, 3)
    for t in v_tuple:
        print(t)
    print(type(v_tuple), v_tuple)
    v_list = [1, 2, 3]
    for l in v_list:
        print(l)
    print(type(v_list), v_list)
    v_list.insert(1, 7)
    v_list.insert(8, 9)
    print(type(v_list), v_list)
    v_str = 'string'
    print(type(v_str), v_str[1: 4])
    for c in v_str:
        print(c, end=' ')

    v_three = "three"
    v_dict = {"one": 1, "two": 2, v_three: 3}
    print(type(v_dict), v_dict)
    for k in v_dict:
        print(k, v_dict[k])
    for k in sorted(v_dict.keys()):
        print(k, v_dict[k])
    v_dict_2 = dict(
        one=1, two=2, three=3, four=4, five="five"
    )
    for k in v_dict_2:
        print(k, v_dict_2[k])
    v_dict_2['six'] = 6
    for k in v_dict_2:
        print(k, v_dict_2[k])

    x1 = (1, 2)
    x2 = (1, 2)
    print(x1, id(x1), x2, id(x2))
    s1 = "123"
    s2 = "123"
    print(s1, id(s1), s2, id(s2))
    print(s1 == s2)
    print(s1 is s2)
    print((1, 2) == (1, 2))
    print((1, 2) is (1, 2))
    print(id((1, 2)), id((1, 2)))

if __name__ == '__main__':  # some comments in source code
    main()
