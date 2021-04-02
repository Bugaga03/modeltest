# Модуль с описание функций работы с базой данных
# Импортируем модуль, описывающий данные пациента
from DataPatient import DataPatient
# Создаем класс с заглушкой (пустой пациент без данных)
# class Violation:
#     name = ""
#     patronymic = ""
#     surname = ""
#     DateofBirth = ""
#     polis = ""
#     doctor = ""
#     dateofreceipt = ""
#     gender = ""

class Data(object):

    def Save(data:list):
        print("Save")
        f = open("database.csv", 'w', encoding='utf-8')
        for record in data:
            f.write(record.name)
            f.write(",")
            f.write(record.patronymic)
            f.write(",")
            f.write(record.surname)
            f.write(",")
            f.write(record.DateofBirth)
            f.write(",")
            f.write(record.polis)
            f.write(",")
            f.write(record.doctor)
            f.write(",")
            f.write(record.dateofreceipt)
            f.write(",")
            f.write(record.gender)
            f.write('\n')
        f.close()
    def Load(self):
        print("Load")
        data = []
        f = open("database.csv", 'r', encoding='utf-8')
        for line in f:
            record0 = line.split(',')
            record = DataPatient()
            record.name = record0[0]
            record.patronymic = record0[1]
            record.surname = record0[2]
            record.DateofBirth = record0[3]
            record.polis = record0[4]
            record.doctor = record0[5]
            record.dateofreceipt = record0[6]
            record.gender = record0[7].strip()
            data.append(record)
        f.close()
        return data
    def GetPatient(data:list, ID:int):
        print("GetPatient")
    # def SetPatient(data:list, ID:int, d:DataPatient):
    #     print("SetPatient")
    def FindName(data:list, name_f:str):
        # for line in data:
        #     if name_f = name
        print("FindName")


    def FindPolis(data:list, polis:int):
        print("FindPolis")
    def Add(data:list, d:DataPatient):
        print("add")
        data.append(d)
        return data