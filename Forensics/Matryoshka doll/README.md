# Matryoshka doll

Matryoshka dolls are a set of wooden dolls of decreasing size placed one inside another. What's the final one? Image: this

# Hints

1. Wait, you can hide files inside files? But how do you find them?
2. Make sure to submit the flag as picoCTF{XXXXX}

# What I Did

When i put the image in exiftool i see that this file might can be extracted.
<img src="Pic_1.JPG">

So i try to change it to zip and extract it, it gives me another file that can be extracted
so i keep repeating the step until i get the flag
and the flag is

``` picoCTF{4f11048e83ffc7d342a15bd2309b47de} ```
