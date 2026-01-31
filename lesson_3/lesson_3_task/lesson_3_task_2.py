
# Импортируем класс Smartphone из другого файла
from smartphone import Smartphone


catalog = [
    Smartphone("Apple", "iPhone 15", "79123456789"),
    Smartphone("Samsung", "Galaxy S23", "79012345678"),
    Smartphone("Xiaomi", "Mi 13", "79212345678"),
    Smartphone("Huawei", "P60", "79312345678"),
    Smartphone("Oppo", "A17", "79412345678")
]

for Smartphone in catalog:

    print(f"{Smartphone.brand} - {Smartphone.model}. {Smartphone.phone_number}")

