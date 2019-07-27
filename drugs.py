#Drug use in New Jersey in 2014
import drugsdata
import matplotlib.pyplot as plt
import numpy as np

list_of_report = drugsdata.get_reports()

marijuanaUse = []
tobaccoUse = []
alcoholUse = []
illicitUse = []

newJersey = []

#Reference
for i in list_of_report:
    if i["Year"] != 2014:
        continue
    elif i["State"] != "New Jersey":
        continue
    else:
        newJersey.append(i)

#People who used marijuana in New Jersey in 2014 in the past year
for i in list_of_report:
    if i["Year"] != 2014:
        continue
    elif i["State"] != "New Jersey":
        continue
    else:
        marijuanaUse.append(i["Rates"]["Marijuana"]["Used Past Month"])

#Tobacco use
for i in list_of_report:
    if i["Year"] != 2014:
        continue
    elif i["State"] != "New Jersey":
        continue
    else:
        tobaccoUse.append(i["Rates"]["Tobacco"]["Use Past Month"])

#Alcohol Use
for i in list_of_report:
    if i["Year"] != 2014:
        continue
    elif i["State"] != "New Jersey":
        continue
    else:
        alcoholUse.append(i["Rates"]["Alcohol"]["Use Past Month"])

#Illicit drug use
for i in list_of_report:
    if i["Year"] != 2014:
        continue
    elif i["State"] != "New Jersey":
        continue
    else:
        illicitUse.append(i["Rates"]["Illicit Drugs"]["All Except Marijuana Used Past Month"])

print("| New Jersey |")
print("Marijuana use: ", marijuanaUse)
print("Tobacco use: ", tobaccoUse)
print("Alcohol use: ", alcoholUse)
print("Illicit use: ", illicitUse)

#Create bar graph of data
#data to plot
numofGroups = 4
percent12to17 = (6.4, 7.11, 14.23, 2.56)
percent18to25 = (16.4, 31.02, 59.94, 6.2)
percent26plus = (4.75, 21.74, 61.52, 2.22)

#Create plot
fig, ax = plt.subplots()
index = np.arange(numofGroups)
bar_width = 0.20
opacity = 1.0

firstageGroup= plt.bar(index, percent12to17, bar_width, alpha=opacity, color='lightcoral', label='Ages 12-17')
secondageGroup = plt.bar(index + bar_width, percent18to25, bar_width, alpha=opacity, color='indianred', label='Ages 18-25')
thirdageGroup = plt.bar(index + bar_width + bar_width, percent26plus, bar_width, alpha=opacity, color='brown', label='Ages 26+')

plt.xlabel('Drugs')
plt.ylabel('Percentage of users')
plt.title('Drug Usage in New Jersey (2014)')
plt.xticks(index + bar_width, ('Marijuana', 'Tobacco', 'Alcohol', 'Illicit Drugs'))
plt.legend()
plt.gca().yaxis.grid(True)

plt.tight_layout()
plt.show()
