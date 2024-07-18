# Bit-O-Asm-3

Can you figure out what is in the eax register? Put your answer in the picoCTF flag format: picoCTF{n} where n is the contents of the eax register in the decimal number base. If the answer was 0x11 your flag would be picoCTF{17}.
Download the assembly dump here.

# Hints

1. Not everything in this disassembly listing is optimal.

# What I Did

This is the important assembly code we need, that related to eax. I give it below
and I did the calculation too

```
<+15>:    mov    DWORD PTR [rbp-0xc],0x9fe1a
<+22>:    mov    DWORD PTR [rbp-0x8],0x4
<+29>:    mov    eax,DWORD PTR [rbp-0xc]        #eax = 0x9fe1a(654874)
<+32>:    imul   eax,DWORD PTR [rbp-0x8]        #eax = 0x9fe1a(654874) * 0x4(4) ==> 2619496
<+36>:    add    eax,0x1f5                      #eax = 2619496 + 0x1f5(501) ==> 2619997
<+41>:    mov    DWORD PTR [rbp-0x4],eax        #rbp-0x4 = eax ==> rbp-0x4 = 2619997
<+44>:    mov    eax,DWORD PTR [rbp-0x4]        #eax = rbp-0x4 ==> eax = 2619997
```

Based on that calculation the eax final value is 2619997
so the flag is

```

picoCTF{2619997}

```
