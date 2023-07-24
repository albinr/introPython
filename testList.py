#INitalizae

names = ["Jonas", "Viggo", "Albin", "Hugo", "Katarina"]
print(names)

# stor loopen



#hitta minsta loopen

minsta = 0

print("namnet när vi startar hitta minsta",names[minsta])
length = len(names)
for nameIndex in range(length):
    print("kollar plats, namn: ",nameIndex, names[nameIndex])
    if names[nameIndex] < names[minsta]:
        minsta = nameIndex

print("minsta:",minsta)

#lägg minsta först

minstaNamn = names[minsta]
print("minstaNamn är: ",minstaNamn)
names.pop(minsta)
names.insert(0,minstaNamn)
#end

print(len(names))
# names.pop(2)
print(names)
