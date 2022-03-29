import egcd
import numpy as np
import string
import src.msgs as msgs

__keymap = dict(zip(string.ascii_uppercase,range(len(string.ascii_uppercase))))

def __isPerfectSquare(num):
    # returns squareroot if perfect square else returns 0
    temp = int(np.sqrt(num))

    if temp*temp == num:
        return temp
    return 0


def __checkKey(key,keylen):
    # check if length of key is perfect square
    # check if key has accepted characters
    sqroot = __isPerfectSquare(keylen)
    if sqroot!=0:
        for i in key:
            if key not in string.ascii_uppercase:
                return -1    # if a character is out of the key range
        return sqroot # if everything is valid
    return 0    # if the length of the key is not a perfect square


def buildKeyMatrix(key):
    keylen = len(key)
    sqroot = __checkKey(key,keylen)
    if sqroot==0:
        msgs.errmsg("Length of key is not a perfect square")
    elif sqroot==-1:
        msgs.errmsg("Key is not within the range of accepted characters. Use only uppercase alphabets")
    else:
        # creating a sqroot*sqroot matrix where sqroot is the squareroot of the length of the key
        keymatrix = []
        temp = []
        for i in key:
            temp.append(__keymap[i])
            if len(temp)==sqroot:
                keymatrix.append(temp)
                temp = []
        return np.array(keymatrix)