import re

data = []
with open('day4_input.txt') as file:
    data = file.read().splitlines()

# Patterns
byr_pattern = re.compile("byr:([\d]{4})(\s|$)")
iyr_pattern = re.compile("iyr:([\d]{4})(\s|$)")
eyr_pattern = re.compile("eyr:([\d]{4})(\s|$)")
hgt_pattern = re.compile("hgt:([\d]+)(in|cm)(\s|$)")
hcl_pattern = re.compile("hcl:(#[0-9a-f]{6})(\s|$)")
ecl_pattern = re.compile("ecl:(amb|blu|brn|gry|grn|hzl|oth)(\s|$)")
pid_pattern = re.compile("pid:([\d]{9})(\s|$)")
cid_pattern = re.compile("cid:([^\s]+)(\s|$)")

def check_passport(passport):
    # Birth Year Check
    if "byr" not in passport:
        return False
    if passport["byr"] < 1920 or passport["byr"] > 2002:
        return False

    if "iyr" not in passport:
        return False
    if passport["iyr"] < 2010 or passport["iyr"] > 2020:
        return False

    if "eyr" not in passport:
        return False
    if passport["eyr"] < 2020 or passport["eyr"] > 2030:
        return False

    if "hgt" not in passport:
        return False
    if passport["hgt"][1] == "in":
        if passport["hgt"][0] < 59 or passport["hgt"][0] > 76:
            return False
    elif passport["hgt"][1] == "cm":
        if passport["hgt"][0] < 150 or passport["hgt"][0] > 193:
            return False

    if "hcl" not in passport:
        return False

    if "ecl" not in passport:
        return False

    if "pid" not in passport:
        return False

    return True

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
            passport["byr"] = int(byr.group(1))

        iyr = iyr_pattern.search(line)
        if iyr:
            passport["iyr"] = int(iyr.group(1))

        eyr = eyr_pattern.search(line)
        if eyr:
            passport["eyr"] = int(eyr.group(1))

        hgt = hgt_pattern.search(line)
        if hgt:
            passport["hgt"] = [int(hgt.group(1)), hgt.group(2)]

        hcl = hcl_pattern.search(line)
        if hcl:
            passport["hcl"] = hcl.group(1)

        ecl = ecl_pattern.search(line)
        if ecl:
            passport["ecl"] = ecl.group(1)

        pid = pid_pattern.search(line)
        if pid:
            passport["pid"] = pid.group(1)

if(check_passport(passport)):
    num_valid += 1
            
print(num_valid)
