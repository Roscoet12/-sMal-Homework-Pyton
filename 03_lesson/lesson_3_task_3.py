from address import Address
from mailing import Mailing

to_address = Address('123456', 'Санкт-Петербург', 'Богатырский проспект', '4', '13')
from_address = Address('098765', 'Москва', 'Ленина', '6', '654')
mail = Mailing(to_address, from_address, '150', 'RTY123456')

print(mail)
