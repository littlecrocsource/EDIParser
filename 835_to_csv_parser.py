import sys
import os.path
import pandas as pd

# Use pip installer to include lxml and edi_835_parser
from edi_835_parser import parse

# command line args
directory = sys.argv[1]
filename = sys.argv[2]

path = directory + filename

if os.path.exists(directory):
    if not os.path.isfile(path+".txt"):
         print(f"[ERROR] Can't open {filename}.txt")
    else:
        print(f"[SUCCESS] Found x12 835 EDI file: [{filename}.txt]")
        transaction_sets = parse(path+".txt")
        data = transaction_sets.to_dataframe()

        # Run this uncommented first and then delete the first "Unnamed: 0 " 
        # column from the csv
        data.to_csv(path+".csv")

        df = pd.read_csv(path+".csv")
        print(df)

        # Comment this if running for first time
        # df.to_xml(directory+filename+".xml")
else:
    print(f"[ERROR] Check {directory}")



   


