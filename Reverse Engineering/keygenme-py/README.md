# keygenme-py

(file link)

# Hints

no hints.

# What I Did

First thing first, i tried to run the code and skimming the script
while i am trying to figure out what is happening,

In the code there is this part that looks suspicious for me
```
key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"
key_part_dynamic1_trial = "xxxxxxxx"
key_part_static2_trial = "}"
key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial
```
I assume that we need to find that 8 letters that lost.
First thing that comes in my mind is that we need to bruteforce the word,
but i still figuring out to find another more elegant way to solve it.

Seeing the flow of the program, i saw that the program check users input to validate the key
in the enter_license function. Inside of that function it calls another function it is 
check_key function, check_key function takes user input(user_key) and username of the user (bUsername_trial).

In the check_key function it calls global key_full_template_trial
which is the flag, but with 8 censored letters.
```
global key_full_template_trial = "picoCTF{1n_7h3_|<3y_of_xxxxxxxx}"
```

What the check_key function do :
1. Check if user input lenght = the length of the flag
2. Check if user input from character 0 to the length of key_part_static1_trial and compared it with key_part_static1_trial to check if both of it share the same letters or not.
3. Check the rest of the user input and compare it with hashlib.sha256(username_trial).hexdigest()[number]

So, basically the censored flag is in that hashlib.sha256(username_trial).hexdigest()[number] we just need to see
what words it calls.

In the script.py i change the code so it prints the flag.

and the flag is

```
picoCTF{1n_7h3_|<3y_of_ac73dc29}
```