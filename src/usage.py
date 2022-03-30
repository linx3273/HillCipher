def inf():
    return '''Usage
    hillcipher <Option>

Option:
    encrypt     e       To encrypt the message based on given key
    decrypt     d       To decrypt the message based on given key
    --help      -h      Displays this message

'''

def encInf():
    return '''Usage:
    hillcipher [encrypt/e] [key] [message]

[key]           Accepted characters - A-Z
[message]       Accepted characters - a-z ?.
Note: 
    Whitespace included in messages 
    Length of key must be a perfect square

'''



def decInf():
    return '''Usage:
    hillcipher [decrypt/d] [key] [message]
    
[key]           Accepted characters - A-Z
[message]       Accepted characters - a-z ?.

Note: 
    Whitespace included in messages
    Length of key must be a perfect square        
    
'''