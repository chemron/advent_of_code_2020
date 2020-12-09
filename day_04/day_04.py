import pandas as pd
import numpy as np


def get_dict(passport):
    # currently looks like 'iyr:2010 ecl:gry hgt:181cm ... '
    data = passport.split()
    return {field.split(':')[0] : field.split(':')[1] for field in data}


def is_valid(row):
    return np.prod(pd.notna(row[['iyr', 'ecl', 'hgt', 'pid',
                                 'byr', 'hcl', 'eyr']]))


f = open('input.txt', 'r')

passports = f.read().split('\n\n')
# make lists of dictionaries:
passports = [get_dict(passport) for passport in passports]

df = pd.DataFrame(passports)
df['valid'] = df.apply(is_valid, axis=1)


print(df['valid'].sum())

f.close()
