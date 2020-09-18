'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    
    # lenth or word is less than 2, return a 0
    if len(word) < 2:
        return 0
    #if lenth of wor is equal to 2 do the next thing
    if len(word) == 2:
        # if the word two characters are equal to th return 1, return 0 otherwise
        if word == 'th':
            return 1
        else:
            return 0    
    # all other cases, use recursion. The recursion will look at the first 2 charactor then evaulate the next place of the array doing the same thing
    return count_th(word[0:2]) + count_th(word[1:])
    

cool = 'thththth'
print(count_th(cool))

cool_r = 'hthththt'
print(count_th(cool_r))

cool_r2 = 'hhththht'
print(count_th(cool_r2))


y = 'y'
print(count_th(y))