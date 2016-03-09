#Dictionaries that go from integers to words

unitdict = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}
tendict = {'1':'ten', '2':'twenty', '3':'thirty', '4':'forty', '5':'fifty', '6':'sixty', '7':'seventy', '8':'eighty', '9':'ninety'}
hundreddict = {'1':'one hundred', '2':'two hundred', '3':'three hundred', '4':'four hundred', '5':'five hundred', '6':'six hundred', '7':'seven hundred', '8':'eight hundred', '9':'nine hundred'}

# Now, take a number, split it up and call correct dictionary

def convertToLetter(n):
    numarray = []
    numstring = str(n)
    for char in numstring:
        numarray.append(char)
    if(len(numarray) == 1):
        print unitdict[numarray[-1]]
    elif (len(numarray) == 2):
        print tendict[numarray[-2]]
        print unitdict[numarray[-1]]
    elif (len(numarray) == 3):
        print hundreddict[numarray[-3]]
        print 'and'
        print tendict[numarray[-2]]
        print unitdict[numarray[-1]]
    else:
        return 'one thousand'
    
#print unitdict['1']
convertToLetter(22)
