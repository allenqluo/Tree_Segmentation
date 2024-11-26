from glob import glob
import pandas as pd

filenames = glob('NEON_struct-plant/**/*vst_apparentindividual*.csv', recursive=True)

dfs = []

for filename in filenames:
    month = pd.read_csv(filename)
    dfs.append(month)

    # print(filename)

all_data = pd.concat(dfs, ignore_index=True)
all_data.drop_duplicates(inplace=True)

# print(len(all_data.index))

all_data.to_csv("NEON_struct-plant/TEAK_appindv_allyears_2022.csv")