def reverse_stringA(string):
'''String Reverse Using Extended Slice'''
    return(string[::-1])

def reverse_stringB(s):
'''String Reverse Using str.join() and reversed()'''
    return(''.join(reversed(s)))

def reverse_stringC(s):
'''String Reverse Using list.reverse() and str.join()'''
    a = list(s)
    a.reverse()
    return ''.join(a)

def reverse_stringD(s):
'''String Reverse Using For Loop'''
    rev_string = ""
    for char in s:
        rev_string = char + rev_string
    return rev_string
    
def reverse_stringE(s):
'''String Reverse Using EWhile Loop'''
    rev_string = ""
    a = len(s) - 1 
    while a >= 0:
        rev_string = rev_string + s[a] 
        a = a - 1
    return rev_string
    
def reverse_stringF(s):
'''String Reverse Using  Recursion'''
    if len(s) == 0:
        return s
    else:
        return reverse_stringF(s[1:]) + s[0]
