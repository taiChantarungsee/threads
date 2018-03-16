import pandas as pd

#Read in files.
laua_data = pd.read_csv("2016_fixed_laua.csv")
log = open("log.txt", "w")
from pprint import pprint
pprint(laua_data.to_dict(), log)