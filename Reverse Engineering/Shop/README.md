# Shop

Best Stuff - Cheap Stuff, Buy Buy Buy... Store Instance: source. The shop is open for business at (link)

# Hints

1. Always check edge cases when programming

# What I Did

I run the program and trying to figure out what is happening. This program is about buying and selling
fruits, and i saw that there is a fruitful flag the price is 100 golds and i only have 40 golds,
So i'm assuming that i have to do something to get that fruitful flag.

In the hint it says that we need to check edge cases,
i googled what edge cases is, edge cases is basically when user gives weird inputs that makes our code works
not like as we want it to do.

Some of edge cases is like, a very big or small number that pass the limit of integer value, very long words,
wrong data type inputs, etc.

I tried every edge cases i know in this program, until i found that the program gives me more money
if i input negative value in "How many items i want to buy stage"

So i just put negative value to get golds and buy the fruitful flag, then it shows me the flag,
but the flag is in integer form
```
Flag is:  [112 105 99 111 67 84 70 123 98 52 100 95 98 114 111 103 114 97 109 109 101 114 95 51 100 97 51 52 97 56 102 125]
```
I create python script to change it back to char
and the flag is 
```
picoCTF{b4d_brogrammer_3da34a8f}
```