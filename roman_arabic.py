import re
command=input('How can I help you? ')
s_command=command.split()
fst_num_tsf={'0':'','1':'I','2':'II','3':'III','4':'IV','5':'V','6':'VI','7':'VII','8':'VIII','9':'IX'}
snd_num_tsf={'0':'','1':'X','2':'XX','3':'XXX','4':'XL','5':'L','6':'LX','7':'LXX','8':'LXXX','9':'XC'}
thd_num_tsf={'0':'','1':'C','2':'CC','3':'CCC','4':'CD','5':'D','6':'DC','7':'DCC','8':'DCCC','9':'CM'}
fth_num_tsf={'0':'','1':'M','2':'MM','3':'MMM'}
Roman_symbol_to_value={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
def Roman_symbol_to_value_func(symbol):
    return Roman_symbol_to_value[symbol]
def simplify_Rnumber(rnumber):#create a new string that make characters without minus
    return rnumber.replace('IV','V').replace('IX','X').replace('XL','L').replace('XC','C').replace('CD','D',).replace('CM','M')
def isRoman(rnumber):
    if not re.search(r'^[IVXLCDM]+$',rnumber):
        return False
    Roman_symbols='IVXLCDM'
    length=len(rnumber)
    for i in range(7):
        if i%2==0:
            for j in range(length-3):
                if rnumber[j]==rnumber[j+1]==rnumber[j+2]==rnumber[j+3]==Roman_symbols[i]:
                    return False
        else:
            for j in range(length-1):
                if rnumber[j]==rnumber[j+1]==Roman_symbols[i]:
                    return False
    if 'IL' in rnumber or 'IC' in rnumber or 'ID' in rnumber or 'IM' in rnumber or \
        'XD' in rnumber or 'XM' in rnumber:
        return False
    for i in range(len(rnumber)-2):
        if Roman_symbol_to_value[rnumber[i]]<Roman_symbol_to_value[rnumber[i+1]]<Roman_symbol_to_value[rnumber[i+2]]:
            return False

    simple_rnumber=simplify_Rnumber(rnumber)
    if sorted(list(simple_rnumber),key=Roman_symbol_to_value_func,reverse=True)!=list(simple_rnumber):
        return False
    if 'IVI' in rnumber or 'IXI' in rnumber or 'XLX' in rnumber or 'XCX' in rnumber or 'CDC' in rnumber or 'CMC' in rnumber:
        return False
    if 'IVV' in rnumber or 'IXV' in rnumber or 'IXX' in rnumber or 'XLL' in rnumber or 'XCC' in rnumber or 'XCL' in rnumber or 'CDD' in rnumber or 'CMM' in rnumber or 'CMD' in rnumber:
        return False
    if 'VIV' in rnumber or 'XLX' in rnumber or 'CDC' in rnumber:
        return False
    return True
#  MDCLXVI fake example:MDCCCCLLXVII
def simplyfy_gRn(gRn,gRs):
    reverse_gRs=gRs[::-1]
    length=len(gRs)
    simple_gRn=gRn
    for i in range(0,length-2,2):
        replaced1=reverse_gRs[i]+reverse_gRs[i+1]
        replaced2=reverse_gRs[i]+reverse_gRs[i+2]
        replacedby1=reverse_gRs[i+1]
        replacedby2=reverse_gRs[i+2]
        simple_gRn=simple_gRn.replace(replaced1,replacedby1).replace(replaced2,replacedby2)
    if length%2==0:
        simple_gRn=simple_gRn.replace(reverse_gRs[length-2:],reverse_gRs[length-1])
    return simple_gRn
def gRs_symbol_to_value(gRs):
    map={}
    reverse_gRs=gRs[::-1]
    length=len(gRs)
    for i in range(length):
        if i%2==0:
            map[reverse_gRs[i]]=10**(i//2)
        else:
            map[reverse_gRs[i]]=5*10**(i//2)
    return map

def is_gRn(gRn,gRs):

    length=len(gRs)
    reverse_gRs=gRs[::-1]
    for i in gRn:
        if i not in gRs:
            return False

    for i in range(length):
        if i%2==0:
            for j in range(len(gRn)-3):
                if gRn[j]==gRn[j+1]==gRn[j+2]==gRn[j+3]==reverse_gRs[i]:
                    return False
        else:
            for j in range(len(gRn)-1):
                if gRn[j]==gRn[j+1]==reverse_gRs[i]:
                    return False

    for i in range(0,length-3,2):
        for j in range(i+3,length):
            long_gap_pair=reverse_gRs[i]+reverse_gRs[j]
            if long_gap_pair in gRn:
                return False
    gRs_symbol_to_value_map=gRs_symbol_to_value(gRs)
    for i in range(len(gRn)-2):
        if gRs_symbol_to_value_map[gRn[i]]<gRs_symbol_to_value_map[gRn[i+1]]<gRs_symbol_to_value_map[gRn[i+2]]:
            return False

    simple_gRn=simplyfy_gRn(gRn,gRs)
    def gRs_symbol_to_value_func(symbol):

        return gRs_symbol_to_value_map[symbol]
    if sorted(list(simple_gRn),key=gRs_symbol_to_value_func,reverse=True)!=list(simple_gRn):
        return False

    for i in range(0,length-2,2):
        depulate_pair_one=reverse_gRs[i]+reverse_gRs[i+1]+reverse_gRs[i]
        depulate_pair_two=reverse_gRs[i]+reverse_gRs[i+2]+reverse_gRs[i]
        depulate_pair_three=reverse_gRs[i]+reverse_gRs[i+2]+reverse_gRs[i+2]
        depulate_pair_four=reverse_gRs[i]+reverse_gRs[i+2]+reverse_gRs[i+1]
        depulate_pair_five=reverse_gRs[i]+reverse_gRs[i+1]+reverse_gRs[i+1]
        depulate_pair_six=reverse_gRs[i+1]+reverse_gRs[i]+reverse_gRs[i+1]
        if depulate_pair_one in gRn or depulate_pair_two in gRn or depulate_pair_three in gRn or depulate_pair_four in gRn or depulate_pair_five in gRn or depulate_pair_six in gRn:
            return False
    if length%2==0:
        depulate_pair_seven=reverse_gRs[length-2]+reverse_gRs[length-1]+reverse_gRs[length-2]
        depulate_pair_eight=reverse_gRs[length-2]+reverse_gRs[length-1]+reverse_gRs[length-1]
        depulate_pair_nine=reverse_gRs[length-1]+reverse_gRs[length-2]+reverse_gRs[length-1]
        if depulate_pair_seven in gRn or depulate_pair_eight in gRn or depulate_pair_nine in gRn:
            return False

    return True

def swap(symbols, i, j):
    if i == j:
        return
    temp = symbols[j]
    symbols[j] = symbols[i]
    symbols[i] = temp


def reverse(symbols,i,j):
    if symbols is None or i<0 or j<0 or i>=j or len(symbols)<j+1:
        return
    while i<j:
        swap(symbols,i,j)
        i+=1
        j-=1
def get_next_permutation(symbols,size):
    i=size-2
    while i>=0 and symbols[i]>=symbols[i+1]:
        i-=1
    if i<0:
        return False
    j=size-1
    while symbols[j]<=symbols[i]:
        j-=1
    swap(symbols,i,j)
    reverse(symbols,i+1,size-1)
    return True


def bad_gRs(reverse_gRs):
    for i in range(len(reverse_gRs)):
        if i%2==0 and reverse_gRs[i]=='_':
            return True
    return False
def badcase1(gRn,gRs):
    for i in gRn:
        if i not in gRs:
            return True
    return False
def badcase2(gRn,gRs):
    reverse_gRs=gRs[::-1]
    length=len(gRs)
    for i in range(length):
        if i%2==0:
            for j in range(len(gRn)-3):
                if gRn[j]==gRn[j+1]==gRn[j+2]==gRn[j+3]==reverse_gRs[i]:
                    return True
        else:
            for j in range(len(gRn)-1):
                if gRn[j]==gRn[j+1]==reverse_gRs[i]:
                    return True
    return False
def badcase3(gRn,gRs):
    reverse_gRs=gRs[::-1]
    length=len(gRs)
    for i in range(0,length-3,2):
        for j in range(i+3,length):
            long_gap_pair=reverse_gRs[i]+reverse_gRs[j]
            if long_gap_pair in gRn:
                return True
    return False
def badcase4(gRn,gRs):
    reverse_gRs=gRs[::-1]
    length=len(gRs)
    gRs_symbol_to_value_map=gRs_symbol_to_value(gRs)
    for i in range(len(gRn)-2):
        if gRs_symbol_to_value_map[gRn[i]]<gRs_symbol_to_value_map[gRn[i+1]]<gRs_symbol_to_value_map[gRn[i+2]]:
            return True
    return False
def badcase5(gRn,gRs):
    reverse_gRs=gRs[::-1]
    length=len(gRs)
    simple_gRn=simplyfy_gRn(gRn,gRs)
    gRs_symbol_to_value_map=gRs_symbol_to_value(gRs)
    def gRs_symbol_to_value_func(symbol):
        return gRs_symbol_to_value_map[symbol]
    if sorted(list(simple_gRn),key=gRs_symbol_to_value_func,reverse=True)!=list(simple_gRn):
        return True
    return False
def badcase6(gRn,gRs):
    reverse_gRs=gRs[::-1]
    length=len(gRs)
    for i in range(0,length-2,2):
        depulate_pair_one=reverse_gRs[i]+reverse_gRs[i+1]+reverse_gRs[i]
        depulate_pair_two=reverse_gRs[i]+reverse_gRs[i+2]+reverse_gRs[i]
        depulate_pair_three=reverse_gRs[i]+reverse_gRs[i+2]+reverse_gRs[i+2]
        depulate_pair_four=reverse_gRs[i]+reverse_gRs[i+2]+reverse_gRs[i+1]
        depulate_pair_five=reverse_gRs[i]+reverse_gRs[i+1]+reverse_gRs[i+1]
        depulate_pair_six=reverse_gRs[i+1]+reverse_gRs[i]+reverse_gRs[i+1]
        if depulate_pair_one in gRn or depulate_pair_two in gRn or depulate_pair_three in gRn or depulate_pair_four in gRn or depulate_pair_five in gRn or depulate_pair_six in gRn:
            return True
    if length%2==0:
            depulate_pair_seven=reverse_gRs[length-2]+reverse_gRs[length-1]+reverse_gRs[length-2]
            depulate_pair_eight=reverse_gRs[length-2]+reverse_gRs[length-1]+reverse_gRs[length-1]
            depulate_pair_nine=reverse_gRs[length-1]+reverse_gRs[length-2]+reverse_gRs[length-1]
            if depulate_pair_seven in gRn or depulate_pair_eight in gRn or depulate_pair_nine in gRn:
                return True
    return False
def bad_gap_gRs(symbols_in_gRn,gRs_str):
    symbols_in_gRs=list(gRs_str.replace('_',''))
    for i in symbols_in_gRn:
        gap=symbols_in_gRn.index(i)-symbols_in_gRs.index(i)
        if gap>1 or gap<-1:
            return True
    return False

def generate_gRs(gRn):
    symbols_in_gRn=[]
    for i in gRn:
        if i in symbols_in_gRn:
            continue
        else:
            symbols_in_gRn.append(i)
    num_of_s_in_gRn=len(symbols_in_gRn)
    gRs_list=[]
    new_symbols=symbols_in_gRn.copy()
    for i in range(num_of_s_in_gRn-1):
        new_symbols.append('_')
    new_symbols.sort()
    size = len(new_symbols)
    gRss_set=set()
    while get_next_permutation(new_symbols, size):
        gRs=''.join(new_symbols).strip('_')
        reverse_gRs=gRs[::-1]
        length=len(gRs)
        if bad_gRs(reverse_gRs):
            continue
        if bad_gap_gRs(symbols_in_gRn,gRs):
            continue
        if badcase1(gRn,gRs):
            continue
        if badcase2(gRn,gRs):
            continue
        if badcase3(gRn,gRs):
            continue
        if badcase4(gRn,gRs):
            continue
        if badcase5(gRn,gRs):
            continue
        if badcase5(gRn,gRs):
            continue
        if badcase6(gRn,gRs):
            continue
        gRss_set.add(gRs)
    return gRss_set
def q1(l):
    if re.search(r'^[1-9][0-9]*$',l):
        if int(l)>3999:
            print("Hey, ask me something that's not impossible to do!")#need exit?
        elif len(l)==1:
            print(f'Sure! It is {fst_num_tsf[l]}')
        elif len(l)==2:
            print(f'Sure! It is {snd_num_tsf[l[0]]+fst_num_tsf[l[1]]}')
        elif len(l)==3:
            print(f'Sure! It is {thd_num_tsf[l[0]]+snd_num_tsf[l[1]]+fst_num_tsf[l[2]]}')
        else:
            print(f'Sure! It is {fth_num_tsf[l[0]]+thd_num_tsf[l[1]]+snd_num_tsf[l[2]]+fst_num_tsf[l[3]]}')
    elif isRoman(l):
        sum=0
        for i in range(len(l)-1):
            if Roman_symbol_to_value[l[i]]>=Roman_symbol_to_value[l[i+1]]:
                sum+=Roman_symbol_to_value[l[i]]
            else:
                sum-=Roman_symbol_to_value[l[i]]
        sum+=Roman_symbol_to_value[l[len(l)-1]]
        print(f'Sure! It is {sum}')
    else:
        print("Hey, ask me something that's not impossible to do!")#need exit?
def figure_to_roman(l,generalisedRomansymbols):
    temp=[]
    for i in range(len(l)):
        if int(l[i])<4:
            temp.append(generalisedRomansymbols[-(2*(len(l)-i)-1)]*int(l[i]))
        elif int(l[i])==4:
            generalisedfour=generalisedRomansymbols[-(2*(len(l)-i)-1)]+generalisedRomansymbols[-(2*(len(l)-i))]
            temp.append(generalisedfour)
        elif int(l[i])==9:
            generalisednine=generalisedRomansymbols[-(2*(len(l)-i)-1)]+generalisedRomansymbols[-(2*(len(l)-i)+1)]
            temp.append(generalisednine)
        else:
            generalisedbig=generalisedRomansymbols[-(2*(len(l)-i))]+generalisedRomansymbols[-(2*(len(l)-i)-1)]*(int(l[i])-5)
            temp.append(generalisedbig)
    newRoman=''.join(temp)
    print(f'Sure! It is {newRoman}')

def q2(l,generalisedRomansymbols):
    length=len(generalisedRomansymbols)
    if not re.search(r'^[a-zA-Z]+$',generalisedRomansymbols):
        print("Hey, ask me something that's not impossible to do!")
    elif len(set(generalisedRomansymbols))!=len(generalisedRomansymbols):
        print("Hey, ask me something that's not impossible to do!")
    elif re.search(r'^[1-9][0-9]*$',l):
        if int(l[0])<4:
            if len(generalisedRomansymbols)<2*len(l)-1:
                print("Hey, ask me something that's not impossible to do!")
            else:
                figure_to_roman(l,generalisedRomansymbols)
        elif int(l[0])==9:
            if len(generalisedRomansymbols)<2*len(l)+1:
                print("Hey, ask me something that's not impossible to do!")
            else:
                figure_to_roman(l,generalisedRomansymbols)
        else:
            if len(generalisedRomansymbols)<2*len(l):
                print("Hey, ask me something that's not impossible to do!")
            else:
                figure_to_roman(l,generalisedRomansymbols)
    elif is_gRn(l,generalisedRomansymbols):
        gRs_symbol_to_value_map=gRs_symbol_to_value(generalisedRomansymbols)
        sum=0
        for i in range(len(l)-1):
            if gRs_symbol_to_value_map[l[i]]>=gRs_symbol_to_value_map[l[i+1]]:
                sum+=gRs_symbol_to_value_map[l[i]]
            else:
                sum-=gRs_symbol_to_value_map[l[i]]
        sum+=gRs_symbol_to_value_map[l[len(l)-1]]
        print(f'Sure! It is {sum}')
    else:
        print("Hey, ask me something that's not impossible to do!")#need exit?
def q3(l):
    if not re.search(r'^[a-zA-Z]+$',l):
        print("Hey, ask me something that's not impossible to do!")
    else:
        gRslist=generate_gRs(l)
        reasonable_gRn_sum=[]
        for dic in gRslist:
            if True:
                simple_gRn=simplyfy_gRn(l,dic)
                gRs_symbol_to_value_map=gRs_symbol_to_value(dic)
                sum=0
                for i in range(len(l)-1):
                    if gRs_symbol_to_value_map[l[i]]>=gRs_symbol_to_value_map[l[i+1]]:
                        sum+=gRs_symbol_to_value_map[l[i]]
                    else:
                        sum-=gRs_symbol_to_value_map[l[i]]
                sum+=gRs_symbol_to_value_map[l[len(l)-1]]
                reasonable_gRn_sum.append([sum,dic])
        if reasonable_gRn_sum==[]:
            print("Hey, ask me something that's not impossible to do!")
        else:
            reasonable_gRn_sum.sort()
            print(f'Sure! It is {reasonable_gRn_sum[0][0]} using {reasonable_gRn_sum[0][1]}')
if s_command[0]=='Please' and s_command[1]=='convert':
    if len(s_command)==3:
        q1(s_command[2])
    elif len(s_command)==5 and s_command[3]=='using':
        q2(s_command[2],s_command[4])
    elif len(s_command)==4 and s_command[3]=='minimally':
        q3(s_command[2])
    else:
        print("I don't get what you want, sorry mate!")
else:
    print("I don't get what you want, sorry mate!")

