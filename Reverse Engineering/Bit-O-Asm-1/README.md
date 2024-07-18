# Bit-O-Asm-1

Can you figure out what is in the eax register? Put your answer in the picoCTF flag format: picoCTF{n} where n is the contents of the eax register in the decimal number base. If the answer was 0x11 your flag would be picoCTF{17}.
Download the assembly dump here.

# Hints

1. As with most assembly, there is a lot of noise in the instruction dump. Find the one line that pertains to this question and don't second guess yourself!

# What I Did

This challange is quite straightforward i just need to open the file and look for eax.
Since i already know a bit about assembly i can guess that the data inside eax is 0x30.

`<+15>:    mov    eax,0x30`

I changed 0x30 to decimal value its 48,
so the flag is

```

picoCTF{48}

```
