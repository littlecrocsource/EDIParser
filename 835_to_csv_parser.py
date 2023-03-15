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

        data.to_csv(path+".csv")

        df = pd.read_csv(path+".csv")
        df.drop(columns=df.columns[0], axis=1,inplace=True)
        print(df)
        df.to_xml(directory+filename+".xml")
else:
    print(f"[ERROR] Check {directory}")



   


