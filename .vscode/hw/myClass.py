class BMI:

    def __init__(self, name, age, height, weight):
        self.__height = height
        self.__weight = weight
        self.__name = name
        self.__age = age

    def getBMI(self):
        self.__BMI = self.__weight / ((self.__height / 100) ** 2)
        return self.__BMI

    def getStatus(self):
        self.BMINumber = self.getBMI()
        if self.BMINumber >= 25:
            return 'Overweight'
        elif 18 < self.BMINumber < 25:
            return 'Normal'
        else:
            return 'Underweight'

    def getInfo(self):
        self.__myStatus = self.getStatus()
        print(self.__name, '的年紀是', self.__age, ',BMI值為: ',
              self.__BMI, ',狀態為:', self.__myStatus)
