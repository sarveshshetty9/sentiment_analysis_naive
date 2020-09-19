import csv
import os
import pandas as pd

import re
import converter as conv
import cleaner as clr
import usersentencedivert as usd
import twitterhandler as twk
def convertcsvtotsv():
    
    with open('sample.csv','r') as fileread, open('test.tsv', 'w') as tsvwrite:
        csvin = csv.reader(fileread)
        tsvout = csv.writer(tsvwrite, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
        for row in csvin:
            tsvout.writerow(row)
        fileread.close()
        tsvwrite.close()
def refurbish():
    with open('sample.csv','r') as fileread, open('test.csv', 'w') as tsvwrite:
        csvin = csv.reader(fileread)
        tsvout = csv.writer(tsvwrite, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
        for row in csvin:
            tsvout.writerow(row)
        fileread.close()
        tsvwrite.close()     