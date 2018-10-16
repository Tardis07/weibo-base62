def div(num):
    d1 = num % 62
    d2 = num // 62 % 62
    d3 = num // 62 // 62 % 62
    d4 = num // 62 // 62 // 62
    return [d4,d3,d2,d1]

base = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

l = str(input())

if l[2] == '1':
    n = [int(l[:2]),int(l[2:10]),int(l[10:])]
else :
    n = [int(l[:2]),int(l[2:9]),int(l[9:])]

div_n = [n[0]]
div_n += div(n[1])
div_n += div(n[2])

out = ''.join([base[i] for i in div_n])

print(out)
