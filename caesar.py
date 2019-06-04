from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet = alphabet_lower + alphabet_upper
    encrypted = ''
    
    for char in text:
        if char not in alphabet:
            encrypted = encrypted + char
        elif char in alphabet_upper:
            rotated_index = alphabet_upper.index(char) + rot
            if rotated_index < 26:
                encrypted = encrypted + alphabet_upper[rotated_index]
            else:
                encrypted = encrypted + alphabet_upper[rotated_index % 26]
        elif char in alphabet_lower:
            rotated_index = alphabet_lower.index(char) + rot
            if rotated_index < 26:
                encrypted = encrypted + alphabet_lower[rotated_index]
            else:
                encrypted = encrypted + alphabet_lower[rotated_index % 26]

    return encrypted 

def main():
    text = input('Type your message:')
    rot = int(input('Number of rotations:'))


    print(encrypt(text, rot))
if __name__ == "__main__":
    main()

    