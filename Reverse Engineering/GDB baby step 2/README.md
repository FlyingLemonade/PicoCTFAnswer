# GDB baby step 2

Can you figure out what is in the eax register at the end of the main function? Put your answer in the picoCTF flag format: picoCTF{n} where n is the contents of the eax register in the decimal number base. If the answer was 0x11 your flag would be picoCTF{17}.
Debug this.

# Hints

1. You could calculate eax yourself, or you could set a breakpoint for after the calculcation and inspect eax to let the program do the heavy-lifting for you.

# What I Did

I downloaded the file in picoCTF terminal and debug it using gdb. Based on the hint, i create 2 breakpoints one in the main and the other one is at the end of the main (main+60)

<img src="Pic_1.jpg">

Then to look the value of the eax i used
`info registers eax` command

<img src="Pic_2.jpg">

so the flag is

```

picoCTF{307019}

```
