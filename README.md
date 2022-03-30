# HillCipher
- Written on Python 3.8.10
- install dependencies using `pip install -r requirements.txt`

## Running the program
### Help
- use `python main.py --help` or `python main.py -h`

### Encryption
- to encrypt the message `python main.py [encrypt/e] [KEY] [MSG]`

### Decryption
- to decrypt the message `python main.py [decrypt/d] [KEY] [MSG]`


### Rules for the KEY
- the range of accepted characters for the key is `A-Z` 
- the length of the key must be a perfect square

### Rules for the MSG
- the range of accepted characters for the msg is `a-z?._`

## NOTE
- if the determinant of the keymatrix is 0
- if the determinant of the keymatrix is equal to the length of `a-z?._` i.e. 29




 


