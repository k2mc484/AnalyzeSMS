# 1b. Kyle Hall Luke Torrez
#The results of this lab were very interesting because of the diffferent type of words used
#     in a spam email compared to a regular email. Spam emails contained more flashy words to catch a
#     reader's eye. Specifically, words about winning something or an urgency to respond. I learned from
#     this homework assignment that spam emails are specifically crafted to catch a reader's attention.

def analyzeSMS(filename):
    spamDict = {}
    hamDict = {}
    lineAsList= []
    hamToggle= False
    numberHam = 0
    numberSpam = 0
    
    inFile = open(filename, encoding = "utf-8")

    for	line in inFile:
        singleLine = line.split()
        lineAsList.append(singleLine)
    
    for line in lineAsList:
        if(line[0] == "ham"):
            hamToggle = True
            numberHam = numberHam +1
            
        else:
            hamToggle = False
            numberSpam = numberSpam + 1

                
        for word in range(1,len(line)):
            line[word] = line[word].lower()
            line[word] = line[word].strip()
            line[word] = line[word].strip(" 1234567890!@#$%^&*()_-+=|\}}{{:;<,>.?/£")

            if(hamToggle == True):
                if(line[word] in hamDict):
                    hamDict[line[word]] = hamDict[line[word]] + 1
                else:
                    hamDict[line[word]] = 1
            
            else:
                if(line[word] in spamDict):
                    spamDict[line[word]] = spamDict[line[word]] + 1
                else:
                    spamDict[line[word]] = 1
    print("Top 20 wost frequent Spam words ('WORD','FREQUENCY')")
    tupleSpam = spamDict.items()
    tupleSpam = sorted(tupleSpam, key = lambda item: item[1],reverse = True)
 
    for x in range(0,20):
        if(len(tupleSpam[x][0])>=1):
            print(tupleSpam[x])
    print()
    print("Top 20 wost frequent Ham words ('WORD','FREQUENCY')")
    tupleHam = hamDict.items()
    tupleHam = sorted(tupleHam, key = lambda item: item[1],reverse = True)
    for x in range(0,20):
         if(len(tupleHam[x][0])>=1):
            print(tupleHam[x])

    print()
    print("Number of Ham messages: "+ str(numberHam))
    print("Total Number of Ham words: " +str(len(tupleHam)))
    print("Number of Spam messages: "+ str(numberSpam))
    print("Total Number of Spam words: " +str(len(tupleSpam)))


# n in a non-negative integer
def genSeq(n):
    return [(i*i) if i%2 == 0 else (-i*i*i) for i in range(n)]

def listWithout(forbiddenItems, inputList):
    return[word for word in inputList if word not in forbiddenItems]
