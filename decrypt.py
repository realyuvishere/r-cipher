# store sentence
s = str(input("Enter sentence: "))
# remove spaces
s_ = s.replace(' ', '')
# store key
key = int(input('Enter split key: '))

# split the string into a list
_l_ = list(s_)

# reverse the whole word
_l_.reverse()
s_ = ''.join(_l_)

# initialize list for splitting into key-length groups
_l = list()

for i in range(len(s_)//key):
    _s = s_[i*key:(i+1)*key]
    _l.append(_s)

# store difference in lengths for left out characters in the end
s_i = len(s_)
_li = len(_l)*key

# append left out characters from the end
if (s_i - _li != 0):
    last_ = s_[_li:s_i]
    _l.append(last_)

# initialize list for storing the reversed key-length groups
l_ = list()

for _i in _l:
    _il = list(_i)
    _il.reverse()
    
    l_.append(''.join(_il))

# join the list containing reversed key-length groups into a single word and split it into a list
_l_ = list(''.join(l_))

# initialize list for restoring spaces as per the intial sentence stored in the beginning
l = list()
space = 0

for i_ in range(len(s)):
    
    if (s[i_] == ' '):
        l.append(' ')
        space += 1
    else:    
        l.append(_l_[i_ - space])

# print the encrypted sentence by joining the list containing spaces as per the initial sentence
print(''.join(l))
