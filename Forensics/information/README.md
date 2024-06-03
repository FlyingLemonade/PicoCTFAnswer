# information

Files can always be changed in a secret way. Can you find the flag? cat.jpg

# Hints

1. Look at the details of the file
2. Make sure to submit the flag as picoCTF{XXXXX}

# What I Did

I download the file and see it in exif tool,
and the license part of the image is showing some suspicious line of
text 

cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9

so i tried to decode it using base64 and i get the flag


the flag is 

``` 

picoCTF{the_m3tadata_1s_modified} 

```





