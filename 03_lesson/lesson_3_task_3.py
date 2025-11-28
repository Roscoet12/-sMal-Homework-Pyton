from address import Address
from mailing import Mailing

toAdd = Address('123456', 'Санкт-Петербург', 'Богатырский проспект', '4', '13')
fromAdd = Address('098765', 'Москва', 'улица Ленина', '6', '654')

mail = Mailing(toAdd, fromAdd, '150', 'RTY123456')

mail.addToAddress(toAdd)
mail.addFromAddress(fromAdd)

print(mail)

