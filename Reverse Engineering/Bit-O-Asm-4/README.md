# Bit-O-Asm-4

Can you figure out what is in the eax register? Put your answer in the picoCTF flag format: picoCTF{n} where n is the contents of the eax register in the decimal number base. If the answer was 0x11 your flag would be picoCTF{17}.
Download the assembly dump here.

# Hints

1. Don't tell anyone I told you this, but you can solve this problem without understanding the compare/jump relationship.
2. Of course, if you're really good, you'll only need one attempt to solve this problem.

# What I Did

I need to guess what the eax value is, below is the important lines that used to guess
or related to eax.

Notes :
cmp : compare both value by substracting one of the value with the other one (the value is not stored)
jle : jump if less than (paired with cmp)
jmp : jump to address input

```
<+15>:    mov    DWORD PTR [rbp-0x4],0x9fe1a        #rbp-4 = 0x9fe1a(654874)
<+22>:    cmp    DWORD PTR [rbp-0x4],0x2710         #0x9fe1a(654874) - 0x2710(10000) ==> compareValue = 644874
<+29>:    jle    0x55555555514e <main+37>           #True go to +37, 644874 less than 93824992235854
<+31>:    sub    DWORD PTR [rbp-0x4],0x65           #JUMPED
<+35>:    jmp    0x555555555152 <main+41>           #JUMPED
<+37>:    add    DWORD PTR [rbp-0x4],0x65           #rbp-4 = 0x9fe1a(654874) - 0x65(101) ==> 654773
<+41>:    mov    eax,DWORD PTR [rbp-0x4]            #eax = rbp-4 ==> 654773
```

Based on the calculation the value of eax is 654773.
So the flag is

```

picoCTF{654773}

```
