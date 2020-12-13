import pandas as pd
import re


def get_dict(passport):
    # currently looks like 'iyr:2010 ecl:gry hgt:181cm ... '
    data = passport.split()
    return {field.split(':')[0]: field.split(':')[1] for field in data}


def is_valid(row):
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    # if any elements (other than cid) are not present:
    if row[fields].isnull().values.any():
        return 0

    byr, iyr, eyr, hgt, hcl, ecl, pid = row[fields]

    valid = (is_byr_valid(byr) *
             is_iyr_valid(iyr) *
             is_eyr_valid(eyr) *
             is_hgt_valid(hgt) *
             is_hcl_valid(hcl) *
             is_ecl_valid(ecl) *
             is_pid_valid(pid))

    return valid


def is_byr_valid(byr):
    match = byr_re.fullmatch(byr)
    if not match:
        return False
    byr = int(byr)
    if byr < 1920 or byr > 2002:
        return False

    return True


def is_iyr_valid(iyr):
    match = iyr_re.fullmatch(iyr)
    if not match:
        return False
    iyr = int(iyr)
    if iyr < 2010 or iyr > 2020:
        return False

    return True


def is_eyr_valid(eyr):
    match = eyr_re.fullmatch(eyr)
    if not match:
        return False
    eyr = int(eyr)
    if eyr < 2020 or eyr > 2030:
        return False

    return True


def is_hgt_valid(hgt):
    match = hgt_re.fullmatch(hgt)
    if not match:
        return False

    type = hgt[-2:]
    hgt = int(hgt[:-2])

    assert (type == 'cm') or (type == 'in')

    if type == 'cm':
        if hgt < 150 or hgt > 193:
            return False
    elif hgt < 59 or hgt > 76:
        return False
    return True


def is_hcl_valid(hcl):
    match = hcl_re.fullmatch(hcl)
    if not match:
        return False
    return True


def is_ecl_valid(ecl):
    match = ecl_re.fullmatch(ecl)
    if not match:
        return False
    return True


def is_pid_valid(pid):
    match = pid_re.fullmatch(pid)
    if not match:
        return False
    return True


# regex
byr_re = re.compile('[1,2][9,0][0-9][0-9]')
iyr_re = re.compile('20[1,2][0-9]')
eyr_re = re.compile('20[2,3][0-9]')
hgt_re = re.compile('(1[5-9][0-9]cm|[5-7][0-9]in)')
hcl_re = re.compile('#[a-z,0-9]{6}')
ecl_re = re.compile('(amb|blu|brn|gry|grn|hzl|oth)')
pid_re = re.compile('[0-9]{9}')


f = open('input.txt', 'r')

passports = f.read().split('\n\n')
# make lists of dictionaries:
passports = [get_dict(passport) for passport in passports]

df = pd.DataFrame(passports)

df['valid'] = df.apply(is_valid, axis=1)
print(df['valid'].sum())

f.close()
