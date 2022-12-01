import sys
import itertools

special_chars = ['#','*','@','$','!','€','&','.']
year_list = range(1950, 2030)
nums_list = range(0,9)

changes1 = {
    'a':'4',
    'e':'3',
    'i':'1',
    'o':'0'
}

changes2 = {
    'a':'@',
    'e':'3',
    'i':'1',
    'o':'0'
}

def nameyear(name):
    passwords = []
    for year in year_list:
        passwords.append(name+str(year))
    return passwords

def namespecial(name):
    passwords = []
    for special in special_chars:
        passwords.append(name+special)
    return passwords

def namespecialyear(name):
    passwords = []
    for special in special_chars:
        for year in year_list:
            passwords.append(name+special+str(year))
    return passwords

def nameyearspecial(name):
    passwords = []
    for special in special_chars:
        for year in year_list:
            passwords.append(name+str(year)+special)
    return passwords

def namenum(name):
    passwords = []
    for num in nums_list:
        passwords.append(name+str(num))
    return passwords

def namenumspecial(name):
    passwords = []
    for special in special_chars:
        for num in nums_list:
            passwords.append(name+str(num)+special)
    return passwords

def namespecialnum(name):
    passwords = []
    for special in special_chars:
        for num in nums_list:
            passwords.append(name+special+str(num))
    return passwords

def namenum2(name):
    passwords = []
    nums = []
    for combination in itertools.product(range(10), repeat=2):
        nums.append(''.join(map(str, combination)))
    for num in nums:
        passwords.append(name+num)
    return passwords

def namenum2special(name):
    passwords = []
    nums = []
    for combination in itertools.product(range(10), repeat=2):
        nums.append(''.join(map(str, combination)))
    for num in nums:
        for special in special_chars:
            passwords.append(name+num+special)
    return passwords

def namespecialnum2(name):
    passwords = []
    nums = []
    for combination in itertools.product(range(10), repeat=2):
        nums.append(''.join(map(str, combination)))
    for num in nums:
        for special in special_chars:
            passwords.append(name + special + num)
    return passwords

def namenum3(name):
    passwords = []
    nums = []
    for combination in itertools.product(range(10), repeat=3):
        nums.append(''.join(map(str, combination)))
    for num in nums:
        passwords.append(name+num)
    return passwords

def namenum3special(name):
    passwords = []
    nums = []
    for combination in itertools.product(range(10), repeat=3):
        nums.append(''.join(map(str, combination)))
    for num in nums:
        for special in special_chars:
            passwords.append(name+num+special)
    return passwords

def namespecialnum3(name):
    passwords = []
    nums = []
    for combination in itertools.product(range(10), repeat=3):
        nums.append(''.join(map(str, combination)))
    for num in nums:
        for special in special_chars:
            passwords.append(name+special+num)
    return passwords

def name_hack(name):
    passwords = []

    for i in range(1,4):
        for each in itertools.permutations(changes1, i):
            nnn = name
            for key in each:
                if key in name:
                    val = changes1[key]
                    nnn = nnn.replace(key,val)
                else:
                    break

            if nnn not in passwords and name!=nnn:
                passwords.append(nnn)

    for i in range(1,4):
        for each in itertools.permutations(changes2, i):
            nnn = name
            for key in each:
                if key in name:
                    val = changes2[key]
                    nnn = nnn.replace(key,val)
                else:
                    break
            if nnn not in passwords and name!=nnn:
                passwords.append(nnn)
    return passwords

def name_hackyear(name):
    passwords = []
    passw = name_hack(name)
    for p in passw:
        for year in year_list:
            passwords.append(p+str(year))
    return passwords

def name_hackyearspecial(name):
    passwords = []
    passw = name_hack(name)
    for p in passw:
        for year in year_list:
            for special in special_chars:
                passwords.append(p+str(year)+special)
    return passwords

def name_hackspecialyear(name):
    passwords = []
    passw = name_hack(name)
    for p in passw:
        for year in year_list:
            for special in special_chars:
                passwords.append(p+special+str(year))
    return passwords


def generate(name, opt=None):
    all = []
    if opt:
        if '1' in opt: all += nameyear(name)
        if '2' in opt: all += namespecial(name)
        if '3' in opt: all += namespecialyear(name)
        if '4' in opt: all += nameyearspecial(name)
        if '5' in opt: all += namenum(name)
        if '6' in opt: all += namenumspecial(name)
        if '7' in opt: all += namespecialnum(name)
        if '8' in opt: all += namenum2(name)
        if '9' in opt: all += namenum2special(name)
        if '10' in opt: all += namespecialnum2(name)
        if '11' in opt: all += namenum3(name)
        if '12' in opt: all += namenum3special(name)
        if '13' in opt: all += namespecialnum3(name)
        if '14' in opt: all += name_hack(name)
        if '15' in opt: all += name_hackyear(name)
        if '16' in opt: all += name_hackyearspecial(name)
        if '17' in opt: all += name_hackspecialyear(name)
    else:
        all += nameyear(name)
        all += namespecial(name)
        all += namespecialyear(name)
        all += nameyearspecial(name)
        all += namenum(name)
        all += namenumspecial(name)
        all += namespecialnum(name)
        all += namenum2(name)
        all += namenum2special(name)
        all += namespecialnum2(name)
        all += namenum3(name)
        all += namenum3special(name)
        all += namespecialnum3(name)
        all += name_hack(name)
        all += name_hackyear(name)
        all += name_hackyearspecial(name)
        all += name_hackspecialyear(name)

    return all


def main(params):

    print("GenPass - Word based password generator")
    print("By Jokin Totem Security")

    if "-h" in params:
        print("\nUsage: python3 genpass.py word")

        print("\nOptions:")
        print(" Capitalize the word: python3 genpass.py -t word")
        print(" Combination options: python3 genpass.py -c 1,2,3 word")
        print("     1: name + year -> totem1999 ")
        print("     2: name + specialchar -> totem#")
        print("     3: name + scpecialchar + year -> totem@1992")
        print("     4: name + year + scpecialchar -> totem2001$")
        print("     5: name + num -> totem0")
        print("     6: name + num + scpecialchar -> totem3!")
        print("     7: name + scpecialchar + num -> totem@0")
        print("     8: name + num2 -> totem05")
        print("     9: name + num2 + scpecialchar -> totem31!")
        print("     10: name + scpecialchar + num2 -> totem@19")
        print("     11: name + num3 -> totem100")
        print("     12: name + num3 + scpecialchar -> totem011!")
        print("     13: name + scpecialchar + num3 -> totem@168")
        print("     14: name in hack language -> t0t3m")
        print("     15: name in hack language + year -> t0tem2001")
        print("     16: name in hack language + year + scpecialchar -> tot3m1999#")
        print("     17: name in hack language + scpecialchar + year -> tot3m@1999")

    name = str(params[-1]).lower()

    if len(params) <= 1 or name == '-h' or name == '-t':
        print("\nIntroduce a word -> python3 genpass.py totem")
    else:
        all = []
        if "-c" in params:
            ind = params.index('-c')
            opt = params[ind+1]
            opt = opt.split(",")
            all = generate(name,opt)
            if "-t" in params: all += generate(name.capitalize(),opt)
        else:
            all = generate(name)
            if "-t" in params:
                all += generate(name.capitalize())

        with open('genpass.txt', 'w') as f:
            for a in all:
                f.write("%s\n" % a)

        print("\nWordlist generated successfuly")

if __name__ == '__main__':
    main(sys.argv)

