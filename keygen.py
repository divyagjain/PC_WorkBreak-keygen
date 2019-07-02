'''
Keygen for https://www.trisunsoft.com/pc-work-break/ Version 8.0
Author: v-i-k-r-a-m (v-i-k-r-a-m@krypdon.dev)

'''
import functools
import random
from os import system, name


letters = ['Z','B','L','J','S','G','D','Y','K','W']

def typecheck(*args1,isclassmethod=False):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args2, **keywords):
            args = args2[1:] if isclassmethod else args2
            for (arg2,arg1) in zip(args,args1):
                if not isinstance(arg2, arg1):
                    raise TypeError(
                        'expected type: %s, actual type: %s' % ( 
                            arg1, type(arg2)))
            return func(*args2, **keywords)
        return wrapper
    return decorator


def clear():
    if name == 'nt': 
        _ = system('cls')
    else: 
        _ = system('clear')


@typecheck(int,int)
def rand_num(start:int, end:int):
    return random.sample(range(start, end), 1)[0]


@typecheck(int)
def pc_num_to_letters(num:int):
    nl = str(num)
    return "".join([letters[int(x)] for x in ((6 - len(nl)) * "0" + nl)])


@typecheck(int)
def num_to_letters(num:int):
    key = ""
    if num<10:
        key = letters[0]
        key += letters[num]
    else:
        key = "".join([letters[int(i)] for i in str(num)])
    return key


@typecheck(int)
def keygen(pc_num:int):
    ''' Single License=1PC,  Personal License=3PCs, Home License = 10 PCs, 
    Team License = More than 10 PCs and Enterprise License = More than 100 PCs.'''
    if  1> pc_num or pc_num> 999999:
        raise ValueError('Number of computers must be between 1 and 999999. \nBut got %d '% pc_num)
    
    edition = "SG"
    key = []
    pcs_num = ""
    signature = 'TPNM'
    if 1 < pc_num < 4:
        edition = "PS"
    elif 3 < pc_num <11:
        edition = "HM"
    elif 10 < pc_num <101:
        edition = "TM"
        pcs_num = "-" + pc_num_to_letters(pc_num)
    elif 100 < pc_num <1000000 :
        edition = "EP"
        pcs_num = "-" + pc_num_to_letters(pc_num)

    key.append(signature)
    key.append("-")
    key.append(num_to_letters(rand_num(1,13)))
    key.append(num_to_letters(rand_num(0,60)))
    key.append("-")    
    key.append(num_to_letters(rand_num(1,32)))
    key.append(edition)
    key.append("-")
    key.append(num_to_letters(rand_num(0,24)))
    key.append(num_to_letters(rand_num(0,59)))
    key.append(pcs_num)
    return "".join(key)

def main():
    clear()
    print("Keygen PC WorkBreak Version 8.0")
    print("software url https://www.trisunsoft.com/pc-work-break/")
    print("by v-i-k-r-a-m (v-i-k-r-a-m@krypdon.dev)")
    print(50*"_"+'\n')
    print("License for:")
    print("1 PC:", keygen(1))
    print("3 PC:", keygen(3))
    print("10 PC:", keygen(10))
    rn = rand_num(11,101)
    print("%d PC:" % rn, keygen(rn))
    rn = rand_num(100,999)
    print("%d PC:" % rn, keygen(rn))
    rn = rand_num(1000,9999)
    print("%d PC:" % rn, keygen(rn))

if __name__ == '__main__':
    main()
