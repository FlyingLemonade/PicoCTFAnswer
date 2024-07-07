# CanYouSee

How about some hide and seek?
Download this file here.

# Hints

1. How can you view the information about the picture?
2. If something isn't in the expected form, maybe it deserves attention?

# What I Did

After extracting the zip there is an image file there, i put it in exif tool,
to find some clues.

In the exif tool i see that this Attribution URL looks like base64 encoded
```Attribution URL : cGljb0NURntNRTc0RDQ3QV9ISUREM05fYTZkZjhkYjh9Cg==```

So i tried to put it in the base64 decoder and i get the flag.
The flag is
``` 

picoCTF{ME74D47A_HIDD3N_a6df8db8}

```