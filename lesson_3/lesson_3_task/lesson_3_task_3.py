
# Импортируем необходимые классы
from Address import Address
from Mailing import Mailing

# Создаем экземпляры адресов
sender = Address("123456", "Москва", "Ленина", "10", "5")
recipient = Address("654321", "Санкт-Петербург", "Невский", "25", "7")

# Создаем почтовое отправление
mail = Mailing(
    to_address=recipient,
    from_address=sender,
    cost=100,
    track="123456789012"
)

# Выводим информацию об отправлении
print(f"Отправление {mail.track} из {mail.from_address.index}, "
      f"{mail.from_address.city}, {mail.from_address.street}, "
      f"{mail.from_address.house} - {mail.from_address.apartment} "
      f"в {mail.to_address.index}, {mail.to_address.city}, "
      f"{mail.to_address.street}, {mail.to_address.house} - "
      f"{mail.to_address.apartment}. Стоимость {mail.cost} рублей.")