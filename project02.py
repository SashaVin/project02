r = str.lower(input())
u = r.split(' ')
t = ''.join(u)
k = len(t) - 1
a = 0
q = 1
while k - a >= a:
    if t[k - a] == t[a]:
        a = a + 1
    else:
        q = 0
        break
if q == 1:
    print('Ого, это палиндром!')
if q == 0:
    print('К сожалению, это не палиндром(')
