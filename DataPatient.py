class DataPatient(object):

    def __init__(self):
        """Constructor"""
        self.name = ""
        self.patronymic = ""
        self.surname = ""
        self.DateofBirth = ""
        self.polis = ""
        self.doctor = ""
        self.dateofreceipt = ""
        self.gender = ""
    def SetPatient(self, name:str, patronymic:str, surname:str, DateofBirth:str, polis:str, doctor:str, dateofreceipt:str, gender:str):
        """Constructor"""
        self.name = name
        self.patronymic = patronymic
        self.surname = surname
        self.DateofBirth = DateofBirth
        self.polis = polis
        self.doctor = doctor
        self.dateofreceipt = dateofreceipt
        self.gender = gender


    # def SetPatient (name:str, patronymic:str, surname:str, DateofBirth:str, polis:int, doctor:str, dateofreceipt:str, gender:str):
    #     """
    #     Сохраняет данные о пациенте
    #     :param name: имя пациента
    #     :param patronymic : отчество пациента
    #     :param surname : фамилия пациента
    #     :param DateofBirth : дата рождения
    #     :param polis : полис пациента
    #     :param doctor :  принимающий доктор
    #     :param dateofreceipt :  дата приема
    #     :param gender : пол пациента
    #     """

