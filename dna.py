import csv
import sys

def main():
    
    # input check
    if len(sys.argv) ! = 3 :
        print("Usage: dna.py data.csv sequence.txt")
        return 1
        
    # variables
    dnaseq = {} #dictionary for STR and it's count
    csvfilename = sys.argv[1]
    txtfilename = sys.argv[2]

    # Extract STRs from 1st row of csv file and initialize dictionary
    # open CSV file
    with open(csvfilename) as csvfile:
        #make an object 
        firstrow = csv.reader(csvfile)
        for row in firstrow:
            dnaSTRs = row
            #takes out "name"
            dnaSTRs.pop(0)
            break
    # put each DNA STRS in the dictionary
    for STR in dnaSTRs:
        dnaseq[STR] = 1
    
    # Read sequnce.txt file and store into 1d array
    with open(txtfilename, newline='') as txtfile:
        # object for txtfile
        txtreader = csv.reader(txtfile)
        for row in txtreader:
            # dnalist is an array
            dnalist = row
    # convert array to string
    dnastring = dnalist[0]

    # NOTE: 1st row of CSV file is extracted and put into dictionary, txtfile is put into array-->string
    
    # Compute longest run of consecutve repeats of STR in DNA sequence string
    for STR in dnaseq:
        STRlen = len(STR)
        maxcount = 0
        for i in range(len(dnastring)):
            # reset temp
            tempcount = 0
            # compare if STR matches with the sequence 
            if dnastring[i: i+ STRlen] == STR:
                # if one match is found: 
                # compare next string length with the STR
                while dnastring[i: i+STRlen] == dnastring[i+STRlen : i+STRlen+STRlen]:
                    tempcount += 1
                    i += STRlen
                if tempcount > maxcount:
                    maxcount = tempcount
        dnaseq[STR] += maxcount

    # Match STR count with csvdata
    # DictReader
    with open(csvfilename, newline='') as csvfile:
        # object made
        csvdata = csv.DictReader(csvfile)
        for person in csvdata:
            found = 0
            for STR in dnaseq:
                if dnaseq[STR] == int(person[STR]):
                    found += 1
            # If every STR matches, print name
            if found == len(dnaseq):
                print(person['name'])
                exit()
        print("No match")


main()
