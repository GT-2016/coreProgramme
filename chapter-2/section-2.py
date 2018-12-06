# coding:utf-8
"""
Chapter 2
"""
def fun_2_6():
    import decimal
    print decimal.Decimal('1.1')

def fun_2_13():
    foo='abc'
    for i ,ch in enumerate(foo):
        print ch, '%d' %i

def fun_2_14():
    squared = [x ** 2 for x in range(4)]
    print squared
    sqdEvens = [x ** 2 for x in range(8) if not x % 2]
    print sqdEvens

def exercise_2_15():
    a = input("number one")
    b = input("number two")
    c = input("number three")
    lists = [a,b,c]
    # print sorted(lists,reverse = True)
    print sorted(lists)[::-1]

if __name__ == "__main__":
    exercise_2_15()