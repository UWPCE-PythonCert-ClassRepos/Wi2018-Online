#!/usr/bin/env python3
# Dict Lab
# 2/12/18

initial_dict = {"name": "Chris", "city": "Seattle", "cake": "chocolate"}
print(initial_dict)
del initial_dict["cake"]
print(initial_dict)
initial_dict["fruit"] = "Mango"
print(initial_dict.keys())
print(initial_dict.values())
print("cake" in initial_dict)
print("Mango" in initial_dict.values())
initial_dict2 = initial_dict.copy()
for x in initial_dict2.keys():
    initial_dict2[x] = x.lower().count("t")
print(initial_dict2)

s2 = set(range(0, 20, 2))
s3 = set(range(0, 20, 3))
s4 = set(range(0, 20, 4))
print(s3.issubset(s2))
print(s4.issubset(s2))
s5 = set("python")
s5.add("i")
print(s5)
s6 = frozenset("marathon")
print(s5.union(s6))
print(s5.intersection(s6))