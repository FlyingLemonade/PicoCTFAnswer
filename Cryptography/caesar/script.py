def caesar_cipher(text, shift):
    result = ''
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            result += chr(shifted)
        else:
            result += char
    return result

plaintext = "gvswwmrkxlivyfmgsrhnrisegl"

for i in range (26):
  encrypted_text = caesar_cipher(plaintext, i)
  print(encrypted_text)


