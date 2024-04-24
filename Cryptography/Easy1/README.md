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

  U + S --> Y <br>
  F + O --> J <br>
  J + L --> C <br>
  K + V --> L <br>
  X + E --> H <br>
  Q + C --> M <br>
  Z + R --> S <br>
  Q + Y --> I <br>
  U + P --> V <br>
  N + T --> G <br>
  B + O --> N <br>

  sadly the answer is not YJCLHMSIVGN, so i turn
  the formula

  S + U --> C <br>
  O + F --> R <br>
  L + J --> Y <br>
  V + K --> P <br>
  E + X --> T <br>
  C + Q --> O <br>
  R + Z --> I <br>
  Y + Q --> S <br>
  P + U --> F <br>
  T + N --> U <br>
  O + B --> N <br>

 this second result looks like the flag
 
 ``` picoCTF{CRYPTOISFUN} ```
