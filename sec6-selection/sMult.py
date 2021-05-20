'''
Develop function: def special_multiplication(string):


Input: abcxf

Output: abbcccxxxxfffff


'''

def special_multiplication(word):
    new_str=''
    for inx,w in enumerate(word):
        new_str=new_str+((inx+1)*w)
    return new_str

res=special_multiplication("abcxf")
print(res)
