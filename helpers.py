def alphabet_position(letter):
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet = alphabet_lower + alphabet_upper
    for char in letter:
        pos = alphabet.index(char)

        return pos 

def rotate_character(char, rot): 
    alphabet_lower = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet = alphabet_lower + alphabet_upper
    encrypted = ''
    for char in char:
        if char not in alphabet:
            encrypted = encrypted + char
        else:
            rotated_index = alphabet.index(char) + rot
            if rotated_index < 26:
                encrypted = encrypted + alphabet[rotated_index]
            else:
                encrypted = encrypted + alphabet[rotated_index % 26]
    return encrypted
    