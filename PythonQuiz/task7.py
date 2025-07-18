
def printPyramid(n):
    for i in range(1,n):

        # First priting spaces
        for space in range(n-i):
            print("  ", end ="")
    
        # Then printing stars
        for k in range(2*i-1):
            print("* ", end ="")
    
        print()


printPyramid(5)