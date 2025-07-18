
text = "aabbcddce"

charCount = {} # creating an empty dict to store count

for char in text:
    if char in charCount:
        # if already in dict, summing their occurence
        charCount[char] += 1
    else:
        # if elemnt is encountered for the first time, setting occcurence to 1
        charCount[char] = 1

for char in text:
    if charCount[char] == 1:
        print(f"{char}")
        break
