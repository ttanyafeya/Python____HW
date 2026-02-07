#Конструктор должен принимать на вход следующие параметры:
# марка телефона;
# модель телефона;
# абонентский номер («+79…»).



class Smartphone:
    def __init__(self, brand, model, phone_number):
        self.brand = brand  # марка телефона
        self.model = model  # модель телефона
        self.phone_number = phone_number  # абонентский номер
