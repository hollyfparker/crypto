from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet = alphabet_lower + alphabet_upper
    key = 0
    encrypted = ""
    
    for i in range(len(text)):
        keychar = key % len(rot)
        
        if text[i] in alphabet_lower:
            new_char = rotate_character(text[i], alphabet_position(rot[keychar]))
          
            encrypted += new_char.lower()
            key += 1

        elif text[i] in alphabet_upper:
            new_char = rotate_character(text[i], alphabet_position(rot[keychar]))
          
            encrypted += new_char.upper()
            key += 1  

        else:
          encrypted += text[i]
        
    return encrypted


def main():
    text = input('Type your message:')
    rot = input('Type your key:')
    
    print(encrypt(text, rot))

if __name__ == "__main__":
    main()