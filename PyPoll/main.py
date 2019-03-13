import csv

with open("election_data.csv",'r') as elecdata:
    dummy = csv.reader(elecdata,delimiter = ',')
    datalist = [r for r in dummy]
    datalist = datalist[1:]
    numvotes = len(datalist)
    bigcanlist = []
    winner = ""
    for r in datalist:
        bigcanlist.append(r[2])
    canlist = set(bigcanlist)
    canvotelist = {}
    for element in canlist:
        canvotelist[element] = [0,0]
    for element in canlist:
        canvotecount = 0
        canvotepercent = 0.0
        for r in datalist:
            if r[2] == element:
                canvotecount = canvotecount +1
        canvotepercent = canvotecount/numvotes
        canvotelist[element]=[canvotecount,canvotepercent]
    winvote = 0
    for element in canvotelist:
        if canvotelist[element][0] > winvote:
            winner = element
            winvote = canvotelist[element][0]
    print("Election Results")
    print("-------------------------")
    print("Total Votes: "+str(numvotes))
    print("-------------------------")
    for element in canvotelist:
        print(element+": {0:.0%}".format(canvotelist[element][1])+" ({:,.0f})".format(canvotelist[element][0]))
    print("-------------------------")
    print("Winner: "+winner)
    outputfile = open("Output.txt","w")
    outputfile.write("Election Results\n")
    outputfile.write("-------------------------\n")
    outputfile.write("Total Votes: "+str(numvotes)+"\n")
    outputfile.write("-------------------------\n")
    for element in canvotelist:
        outputfile.write(element+": {0:.0%}".format(canvotelist[element][1])+" ({:,.0f})\n".format(canvotelist[element][0]))
    outputfile.write("-------------------------\n")
    outputfile.write("Winner: "+winner+"\n")
    outputfile.close()
 