import datetime
b=datetime.datetime.now()
print(b)

import datetime
b=datetime.datetime.now()
c=b-datetime.timedelta(weeks=3)
print(c)

a={1, 2,3,4}
a.add(5)
print(a)
a.pop()
print(a)

a={'a':2}
oldkey='a'
newkey='A'
a[newkey]=a.pop(oldkey)
print(a)