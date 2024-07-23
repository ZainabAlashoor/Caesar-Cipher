''' 
    Caesar Cipher is one of the oldest encryption techniques, 
    it was used by Julius Caesar to send messages to his allies.
'''
'''
    How does it work? By replacing letters to a certain number of position. 
    Both you and the other party should agree on a fixed number(int) of positions to solve the message.
'''
'''
    @note: 
    upper case letters in ASCII:
    'A' = 65 to 'Z' = 90
    lower case letters in ASCII:
    'a' = 97 to 'z' = 122
'''

def encrypt(string, position):
    """return a string encrypted"""
    newString = ''
    
    for c in range(len(string)):
        ch = string[c]

        # check if it's lower or upper case letter:
        if ch.isupper():
            newString += chr((ord(ch) + position-65) % 26 + 65) 
        else: 
            newString += chr((ord(ch) + position-97) % 26 + 97)
            
    return newString

def decrypt(string, position):
    """return an encrypted string to its original form"""
    newString = ''
    
    for c in range(len(string)):
        ch = string[c]

        # check if it's lower or upper case letter:
        if ch.isupper():
            newString += chr((ord(ch) - position-65) % 26 + 65)
        else: 
            newString += chr((ord(ch) - position-97) % 26 + 97)
            
    return newString


print ('Welcome 😽!!')
choice = input('do you want to encrypt a text or decrypt it (en/de)? ')
choice.lower()
original_string = input('Enter the text you want to convert: ')
position = int(input('Enter the number of positions: '))
if choice=='en':
    your_cipher = encrypt(original_string, position)
    print ('your text enctypted: ' + your_cipher)
elif choice=='de':
    your_cipher = decrypt(original_string, position)
    print ('your text dectypted: ' + your_cipher)
else:
    print('invalid input')
