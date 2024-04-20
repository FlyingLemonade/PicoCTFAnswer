# Easy1

# Description
The one time pad can be cryptographically secure, but not when you know the key. Can you solve this? We've given you the encrypted flag, key, and a table to help UFJKXQZQUNB with the key of SOLVECRYPTO. Can you use this table to solve it?.

# Hints
1. Submit your answer in our flag format. For example, if your answer was 'hello', you would submit 'picoCTF{HELLO}' as the flag.
2. Please use all caps for the message.

# What I Did
 This question ask me to download a txt file that contain the table
 to decrypt the cipher text.

 I just need to identify the cipher text and its 
 corresponding key combination from the provided text table.
 Since this is a decryption, i need to use the table reversed way.
 
 If the encryption works by 
  E + D --> H
 Then to decrypt it, i need to do
 (By finding H in E row, then see what E + ? --> H)
  
  E + H --> D

 or just use this https://www.dcode.fr/vigenere-cipher

  U + S --> Y 
  F + O --> J 
  J + L --> C
  K + V --> L
  X + E --> H
  Q + C --> M
  Z + R --> S
  Q + Y --> I
  U + P --> V
  N + T --> G
  B + O --> N

  sadly the answer is not YJCLHMSIVGN, so i turn
  the formula

  S + U --> C 
  O + F --> R 
  L + J --> Y
  V + K --> P
  E + X --> T
  C + Q --> O
  R + Z --> I
  Y + Q --> S
  P + U --> F
  T + N --> U
  O + B --> N

 this second result looks like the flag
 
 ``` picoCTF{CRYPTOISFUN} ```
