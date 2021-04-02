# This is a sample Python script.
from DataPatient import DataPatient
from Data import Data
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

    # d = DataPatient("цукцук","цукцук","цукцук","цукцук",12554455,"цукцук","цукцук","цукцук")
database = Data
dataList = database.Load(database)
for record in dataList:
    print(record.name)

d = DataPatient()
d.SetPatient("Максим", "Николаевич", "Кожин", "06.08.1983", "124578", "Смирнова МК", "07.12.2021", "мужской")

dataList = database.Add(dataList, d)
database.Save(dataList)

dataList = database.Load(database)
for record in dataList:
    print(record.name)

# dataList = database.Load(database)
# for record in dataList:
#     print(record.name)

# Поиск
x = input(str())
dataList = database.Load(database)
for record in dataList:

        print(record.name)

# print(dataList)

# Поиск
# x = input(str())
# poisk = Data.FindName(database,x)
# print(x)
