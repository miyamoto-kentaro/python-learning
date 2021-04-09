# use at funning short process in dictionary
k = ['mon','tue', 'wed']
v = ['coffee','milk','water']


d = {}
for x, y in zip(k, v):
    d[x] = y

print(d)

d = {x: y for x,y in zip(k,v)}
print(d)