# Safe Opener

Can you open this safe? I forgot the key to my safe but this program is supposed to help me with retrieving the lost key. Can you help me unlock my safe? Put the password you recover into the picoCTF flag format like: picoCTF{password}

# Hints

no hints.

# What I Did

I downloaded the file and when i opened the file,
i saw this immediately 
```
String encodedkey = "cGwzYXMzX2wzdF9tM18xbnQwX3RoM19zYWYz";
```
It looks like base64, and when i decode it i get the password,
we are looking for it's pl3as3_l3t_m3_1nt0_th3_saf3
so the flag is

```
picoCTF{pl3as3_l3t_m3_1nt0_th3_saf3}
```