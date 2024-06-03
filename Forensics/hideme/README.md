# hideme

Every file gets a flag.
The SOC analyst saw one image been sent back and forth between two people. They decided to investigate and found out that there was more than what meets the eye here.

# Hints

no hints.

# What I Did

I try to look the hex of the file using hexedit,
and then i see that there is something suspicious
<image src="Pic_1.jpg">

So based on that string i assume that i need to find that secret document and
get the flag. I try to change the flag.png to zip and extract it
and luckily it works and i get the secret directory. Inside that secret directory
i find the flag.

The flag is

``` 

picoCTF{Hiddinng_An_imag3_within_@n_ima9e_dc2ab58f} 

```