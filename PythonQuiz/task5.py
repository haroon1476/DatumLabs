
def flattenList(inputData):

    flatList = [] # creating an empty list to store flat data
    # count = 0

    for item in inputData:

        # checking if a nested list appears in my parent list
        if isinstance(item, list):
            # multilevel flatten
            flatList.extend(flattenList(item)) 
        else:
            # if element within the list is a simple interger, then simple appending to the flattening list
            flatList.append(item)

        # print("\nTest")
        # count = count + 1
        # print(f"iteration {count} , current item = {item} , flattened list = {flatList}")
            

    return flatList


inputData = [1,[2,[3,4],5],6,[[7]]]
flatData = flattenList(inputData)
print(flatData) 