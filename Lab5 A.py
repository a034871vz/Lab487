
''' Main '''

totalSpam = 0
spamCounter = 0
spamAverage = 0
fname = "mbox.txt"
try:
    file = open(fname)  # Open file
except:
    print("File cannot be opened: ")
    exit()
if file != None:
    try:
        for line in file:  # Read file content
            if line.startswith("X-DSPAM-Confidence:"):
                try:
                    totalSpam += float(line[20:-1])
                    spamCounter += 1
                except:
                    continue
    except:
        print("Error on reading file content!")
    spamAverage = totalSpam / spamCounter
    print("Average spam confidence: " + str(spamAverage))
    print(spamCounter)
    try:
        file.close()  # Close file
    except:
        print("File could not be closed!")
        exit()