# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes 
# a string as input and returns the i and j indices that 
# correspond to the beginning and end indices of the longest 
# palindrome in the string. 
#
# Grading Notes:
# 
# You will only be marked correct if your function runs 
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!

import time


def is_palindrom(text):
    text = text.lower()
    for i in range(len(text)/2):
        if text[i] != text[-(1+i)]:
            return False
    else:
        return True


def bruce_subpalindrome(text):
    begin, end = 0, 0
    longest_index = begin, end
    delta = 0
    length = len(text)
    for i in range(length):
        for j in range(begin, length+1):  # string[i:j] not include char--j
            if is_palindrom(text[i:j]):
                if  j - i > end - begin: 
                    begin, end = i, j

    return begin, end


def look_forward(begin, end, text):
    for end in range(end, len(text)+1):
        if not is_palindrom(text[begin:end]):
            return end-1
    else:
        return end


def look_symmtery(axis, text):
    temp_begin, temp_end = axis - 1, axis + 2
    length = len(text)
    while temp_begin - 1 >= 0 and temp_end + 1<= length:
        if is_palindrom(text[temp_begin -1 : temp_end + 1]):
            temp_begin -= 1
            temp_end += 1
        else:
            break

    return temp_begin, temp_end 
            
    
def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    # Your code here
    if text == '': return 0, 0

    candidates = [grow(start, end, text)
                  for start in range(len(text))
                  for end in (start, start+1)]

    return max(candidates, key=lambda slice: slice[1] - slice[0])


def grow(begin, end, text):
    ## the text[begin-1] is amazing!
    while (begin > 0 and end < len(text)
        and text[begin-1].upper() == text[end].upper()):
            begin -= 1; end += 1
    return begin, end


def test_is_palindrom():
    L = is_palindrom
    assert(L('racecar') == True)
    assert(L('Racecar') == True)
    assert(L('Race car') == False)
    assert(L('RaceDcar') == False)
    print('test done!')


def test_look_symmtry():
    L = look_symmtery
    print( L(3, 'racecar') )
    assert( L(3, 'racecar') == (0, 7))
    print (L(3, 'RacecarX') )
    assert L(3, 'RacecarX') == (0, 7)
    print (L(14, 'something rac e car going'))
    assert L(14, 'something rac e car going') == (8,21)

def test_look_forward():
    L = look_forward
    print( L(0, 2, 'xxxxxA') )
    assert L(0, 2, 'xxxxxA') == 5
    assert L(1, 2, 'xxxxxA') == 5
    assert L(0, 2, 'aacdefg') == 2
    assert L(0, 2, 'abcdefg') == 1
    print('test done!')


def test():

    start = time.time()
    
    #L = bruce_subpalindrome
    L = longest_subpalindrome_slice
    print( L('racecar') )
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    print( L('Race carr') )
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8,21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    print('used time {0}'.format(time.time() - start))
    return 'tests pass'

print test()
#print test_is_palindrom()
#print(test_look_symmtry())
