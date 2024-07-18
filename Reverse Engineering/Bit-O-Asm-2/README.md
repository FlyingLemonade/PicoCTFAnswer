# Bit-O-Asm-2

Can you figure out what is in the eax register? Put your answer in the picoCTF flag format: picoCTF{n} where n is the contents of the eax register in the decimal number base. If the answer was 0x11 your flag would be picoCTF{17}.
Download the assembly dump here.

# Hints

1. PTR's or 'pointers', reference a location in memory where values can be stored.

# What I Did

I look at the file and look at the line with eax in it.

```
<+15>:    mov    DWORD PTR [rbp-0x4],0x9fe1a
<+22>:    mov    eax,DWORD PTR [rbp-0x4]
```

based on those lines the eax contains a pointer that refer to the data that stored in
rbp-0x4. The rbp-0x4 contains 0x9fe1a, so the flag is
the decimal value of 0x9fe1a which is 654874

So the flag is

```

picoCTF{654874}

```
