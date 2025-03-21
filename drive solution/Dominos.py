
s = input("s: ")
prev = ''

while s != prev:
    prev = s
    s = s.replace('R.L', 'xxx')
    s = s.replace('R.', 'RR')
    s = s.replace('.L', 'LL')

print(s.replace('xxx', 'R.L'))
