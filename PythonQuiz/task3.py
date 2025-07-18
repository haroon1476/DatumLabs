text = "mississipi"

charCount = {} # creating an empty dic to store count

for char in text:
    if char in charCount:
        # if already in dict, summing their occurence
        charCount[char] += 1
    else:
        # if character comes for the first time, setting occurence to 1
        charCount[char] = 1

print(charCount)