def sortDict(myDict):
  
    # fist converting dictionary to list to apply some sortig algo
    items = [(k,v) for k,v in myDict.items()]
    print(items)

    # Applying selection sort by value
    for i in range(len(items)):
        for j in range(i+1, len(items)):
            if (items[i][1] > items[j][1]):

                # print(f" First item =  {items[i][1]}")
                # print(f" Second item = {items[j][1]}")

                #Swapping
                temp = items[i]
                items[i] = items[j]
                items[j] = temp

    #converting items to dictionary
    sortedDict = {}
    for k,v in items:
        sortedDict[k] = v

    return sortedDict


scores = {"Alice":50 , "Bob":75 , "Charlie":12}
sortedScores = sortDict(scores)
print(sortedScores)