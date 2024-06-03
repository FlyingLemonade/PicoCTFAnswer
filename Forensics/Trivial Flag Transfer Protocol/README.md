# Trivial Flag Transfer Protocol

Figure out how they moved the flag.

# Hints

1. What are some other ways to hide data?

# What I Did

I download and open the file in wireshark, after that when i 
check if there is any downloadable file. Turns out there are some
files that can be downloaded.

<image src="Pic_1.jpg">

So i download all the files there.

I look at the instruction.txt file then i try to
decrypt it using caesar cipher.

GSGCQBRFAGRAPELCGBHEGENSSVPFBJRZHFGQVFTHVFRBHESYNTGENAFSRE.SVTHERBHGNJNLGBUVQRGURSYNTNAQVJVYYPURPXONPXSBEGURCYNA

Turns out it is a ROT13 and the real message is

TFTPDOESNTENCRYPTOURTRAFFICSOWEMUSTDISGUISEOURFLAGTRANSFER.FIGUREOUTAWAYTOHIDETHEFLAGANDIWILLCHECKBACKFORTHEPLAN

"TFTP DOESNT ENCRYPT OUR TRAFFIC SO WE MUST DUSGUISE OUR FLAG
TRANSFER. FIGURE OUT AWAY TO HIDE THE FLAG AND I WILL CHECK 
BACK FOR THE PLAN"

And in plan file there is also a message

VHFRQGURCEBTENZNAQUVQVGJVGU-QHRQVYVTRAPR.PURPXBHGGURCUBGBF

When i put it in rot13 Decryptor it gives me

IUSEDTHEPROGRAMANDHIDITWITH-DUEDILIGENCE.CHECKOUTTHEPHOTOS

"I USED THE PROGRAM AND HID IT WITH-DUE DILIGENCE. CHECK OUT THE PHOTOS"

Based on the plan file i need to check each of the picture.

I put it in exif tool and hexedit but i get nothing,
so i decided to find more clue, and i see .deb file, i googled
about it and turns out i can extract it using this online extractor

https://www.ezyzip.com/extract-deb-file-online.html

and then when i explore the folders, i find that there is a steghide in the bin
folder, so i assume that i can do something to the images with steghide.
After using steghide tools without password it gives me nothing,
i need to know the password to decode the file.
I use this tools to decode it

https://futureboy.us/stegano/decinput.html

I Check the pcap file again i find nothing. Then when i look at the
second hint (plan file) i figured out that this 
"I USED THE PROGRAM AND HID IT WITH-DUE DILIGENCE" might be telling us what is
the password. After trying a bunch of words as it passwords i get the flag when i use
DUEDILIGENCE (with uppercase letter) as it password.

and the flag is

``` 

picoCTF{h1dd3n_1n_pLa1n_51GHT_18375919} 

```


