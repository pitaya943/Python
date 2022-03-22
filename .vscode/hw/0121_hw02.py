# coding:utf-8
import sys

DSScore = [['A', 87], ['B', 68], ['C', 54], ['D', 78], ['E', 88],
           ['F', 51], ['G', 97], ['H', 47], ['I', 68], ['J', 49]]

PGScore = [['A', 57], ['B', 78], ['C', 56], ['D', 90], ['E', 68],
           ['F', 57], ['G', 98], ['H', 87], ['I', 59], ['J', 61]]

DSfailed = []
PGfailed = []

for item in DSScore:
    if item[1] < 60:
        DSfailed.append(item[0])

for item in PGScore:
    if item[1] < 60:
        PGfailed.append(item[0])

setOfDSfailed = set(DSfailed)
setOfPGfailed = set(PGfailed)

# 只有DS
DSnotPG = setOfDSfailed - setOfPGfailed
# 只有PG
PGnotDS = setOfPGfailed - setOfDSfailed
# 兩者
DSandPG = setOfDSfailed & setOfPGfailed
# 只有一科
onlyFailed = setOfDSfailed ^ setOfPGfailed
# 任一科
ifFailed = DSandPG | onlyFailed

print("\nData Structure Score:\n", DSScore,
      "\n\nProgramming Score:\n", PGScore)

print("------------------------------------")
print("If failed:\n", ifFailed)
print("DS failed:\n", setOfDSfailed)
print("PG failed:\n", setOfPGfailed)
print("Only DS failed:\n", DSnotPG)
print("Only PG failed:\n", PGnotDS)
print("Both failed:\n", DSandPG)
print("Only one of them failed:\n", onlyFailed)
print("------------------------------------")
