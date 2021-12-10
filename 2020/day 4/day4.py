import re

data = []
with open('day4_input.txt') as file:
    data = file.read().splitlines()

# Patterns
byr_pattern = re.compile("byr:([^\s]+)")
iyr_pattern = re.compile("iyr:([^\s]+)")
eyr_pattern = re.compile("eyr:([^\s]+)")
hgt_pattern = re.compile("hgt:([^\s]+)")
hcl_pattern = re.compile("hcl:([^\s]+)")
ecl_pattern = re.compile("ecl:([^\s]+)")
pid_pattern = re.compile("pid:([^\s]+)")
cid_pattern = re.compile("cid:([^\s]+)")

def check_passport(passport):
    if("byr" in passport
           and "iyr" in passport
           and "eyr" in passport
           and "hgt" in passport
           and "hcl" in passport
           and "ecl" in passport
           and "pid" in passport):
            return True
    return False

num_valid = 0
passport = {}
for line in data:
    if(line == ''):
        # Check passport
        if(check_passport(passport)):
            num_valid += 1

        passport = {}
    else:
        byr = byr_pattern.search(line)
        if byr:
            passport["byr"] = byr.group(1)

        iyr = iyr_pattern.search(line)
        if iyr:
            passport["iyr"] = iyr.group(1)

        eyr = eyr_pattern.search(line)
        if eyr:
            passport["eyr"] = eyr.group(1)

        hgt = hgt_pattern.search(line)
        if hgt:
            passport["hgt"] = hgt.group(1)

        hcl = hcl_pattern.search(line)
        if hcl:
            passport["hcl"] = hcl.group(1)

        ecl = ecl_pattern.search(line)
        if ecl:
            passport["ecl"] = ecl.group(1)

        pid = pid_pattern.search(line)
        if pid:
            passport["pid"] = pid.group(1)

        cid = cid_pattern.search(line)
        if cid:
            passport["cid"] = cid.group(1)

if(check_passport(passport)):
    num_valid += 1
            
print(num_valid)
