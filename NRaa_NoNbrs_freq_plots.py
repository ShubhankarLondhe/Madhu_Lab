import matplotlib.pyplot as plt

# NRaa DB
ls = [
1.430759000000000000e+07,
1.073707500000000000e+07,
7.415360000000000000e+05,
3.278190000000000000e+05,
8.002760000000000000e+05,
1.780785000000000000e+06,
1.695018000000000000e+06,
8.554813000000000000e+06,
1.175848000000000000e+06,
1.955240000000000000e+05,
6.535630000000000000e+05,
3.343950000000000000e+06,
2.708160000000000000e+05,
5.947730000000000000e+05,
1.972290000000000000e+05,
5.148200000000000000e+05
]

ls_sum = sum(ls)
ls_per = [i*100/ls_sum for i in ls]

# No Neighbours DB
lt = [
1.430867700000000000e+07,
1.073728700000000000e+07,
7.415390000000000000e+05,
3.278440000000000000e+05,
8.002260000000000000e+05,
1.780670000000000000e+06,
1.695288000000000000e+06,
8.555028000000000000e+06,
1.175905000000000000e+06,
1.955520000000000000e+05,
6.536320000000000000e+05,
3.343991000000000000e+06,
2.708460000000000000e+05,
5.947480000000000000e+05,
1.972090000000000000e+05,
5.148090000000000000e+05
]

lt_sum = sum(lt)
lt_per = [i*100/lt_sum for i in lt]

import matplotlib.pyplot as plt

cg = list(range(1,17))
ls_1 = [i/1e6 for i in ls]
plt.bar(cg,ls_1)
plt.xlabel("Chemical Group Number")
plt.ylabel("Frequency ($10^6$)")
plt.title("Frequency of central chemical groups in NRaa database")
plt.xticks(cg)
plt.show()

plt.bar(cg,ls_per)
plt.xlabel("Chemical Group Number")
plt.ylabel("Frequency (percentage)")
plt.title("Percentage of central chemical groups in NRaa database")
plt.xticks(cg)
plt.show()


lt_1 = [i/1e6 for i in lt]
plt.bar(cg,lt_1)
plt.xlabel("Chemical Group Number")
plt.ylabel("Frequency ($10^6$)")
plt.title("Frequency of central chemical groups in no neighbours database")
plt.xticks(cg)
plt.show()

plt.bar(cg,lt_per)
plt.xlabel("Chemical Group Number")
plt.ylabel("Frequency (percentage)")
plt.title("Percentage of central chemical groups in no neighbours database")
plt.xticks(cg)
plt.show()