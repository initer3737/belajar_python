# ? and or xor
# and
c=True
print('nilai c$=',c)
c&=False
print('nilai c$=False, nilai c menjadi ',c)
c=True
print('nilai c=',c)
c &=True
print('nilai c$=True, nilai c menjadi ',c)

# xor
c=True
print('nilai c$=',c)
c^=False
print('nilai c^=False, nilai c menjadi ',c)
c=True
print('nilai c=',c)
c ^=True
print('nilai c^=True, nilai c menjadi ',c)

# shift
# todo geser ke kanan 2 kali
d=0b0100
print("nilai d ",format(d,'04b'))
d >>=2
print("nilai d menjadi ",format(d,'04b'))