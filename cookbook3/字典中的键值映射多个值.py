# Author:GaoYuCai
from collections import defaultdict
d=defaultdict(list)
d["a"].append(1)
d["a"].append(2)
d["a"].append(4)
b=defaultdict(set)
b["a"].add(1)
b["a"].add(2)
b["a"].add(4)
c={}
c.setdefault("a",[]).append(1)
c.setdefault("a",[]).append(2)
c.setdefault("a",[]).append(4)
print(c)

