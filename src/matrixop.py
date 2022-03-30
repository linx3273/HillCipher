import numpy as np
from egcd import egcd
import string
import src.msgs as msgs

# contains all lowercase alphabets including . ? to make the modulus prime
__entries = string.ascii_lowercase+".?_"

# stores a dictionary each character in __entries to a number from 0-29, will be used for converting letters to indices
__char_to_index = dict(zip(__entries,range(len(__entries))))

# stores a dictionary that will map the numbers 0-29 to each character in __entries. will be used to convert indices to letters
__index_to_char = dict(zip(range(len(__entries)),__entries))


def __crypt(inp,keymatrix,keylen):
    inpCopy = inp
    # padding the message
    while len(inpCopy)%keylen != 0:
        inpCopy = inpCopy+'.'

    # creating column matrices of message to encrypt
    iMatrix = []
    temp = []
    for i in inpCopy:
        temp.append(__char_to_index[i])
        if len(temp)==keylen:
            iMatrix.append(temp)
            temp = []
    
    # storing the column matrices after the encryption multiplication into oMatrix
    oMatrix = []
    for i in iMatrix:
        temp = np.array(i)
        temp = np.transpose(temp)
        oMatrix.append(np.dot(keymatrix,temp)%len(__entries))
    
    #converting to string
    oMatrix = list(oMatrix)
    out = ""   
    for i in oMatrix:
        for j in i:
            out += __index_to_char[j]

    #removing the padding
    
    return out
    
    

def __getMatrixModularInverse(key,modulus=len(__entries)):
     #finding matrix modulus inverse for the key
    det = int(np.round(np.linalg.det(key))) #finding determinant of the matrix
    invDet = egcd(det,modulus)[1] % modulus #finding inverse of determinant and apply modulus
    return (invDet * np.round(det*np.linalg.inv(key)).astype(int) % modulus) # multiply invDet to det* inverse(matrix) with applied modulus

def cryptHandler(inp,keymatrix,flag):
    if flag==1: # encrypt
        msgs.msg(f"The Ciphertext is:\n{__crypt(inp,keymatrix,len(keymatrix))}")
    else:   # decrypt
        msgs.msg(f"the Plaintext is:\n{__crypt(inp,__getMatrixModularInverse(keymatrix),len(keymatrix))}")
        