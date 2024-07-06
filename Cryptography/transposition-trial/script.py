cipher = "heTfl g as iicpCTo{7F4NRP051N5_16_35P3X51N3_V091B0AE}2"

arr = []
for i in range (len(cipher)):
  if i % 3 == 2 and i >= 2:
    arr.append(cipher[i-2]+cipher[i-1]+cipher[i])

print(arr)

for word in arr:

  print(word[2]+word[0]+word[1], end="")

