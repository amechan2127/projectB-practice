
#lst2=list(map(str,input().split()))

import itertools
lst1=list(map(str,input().split()))
for i in itertools.product(lst1, repeat=3):
    print("["+i+"]")