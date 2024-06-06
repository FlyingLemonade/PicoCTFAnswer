enc_flag = "picoCTF{w1{1wq8/7376j.:}"
tempFlag = ""
for i in range (8):
  if (i < 8):
    tempFlag += enc_flag[i]

for i in range (8, 24):
  if(i & 1 == 0):
    tempFlag += chr(ord(enc_flag[i])-5)
  else :
    tempFlag += chr(ord(enc_flag[i])+2)

tempFlag = tempFlag[:-1] + "}"
print(tempFlag)

  

