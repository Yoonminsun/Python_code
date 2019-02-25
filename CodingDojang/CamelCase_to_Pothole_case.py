import re
data = 'numGoat30'
p = re.compile('([A-Z])')
m = p.sub('_\g<1>',data).lower()
p = re.compile('([0-9])')
n = p.sub('_\g<1>',m)
print(n)


