from smartphone import Smartphone

catalog = [
    Smartphone('Xiaomi', 'Watch S4', '+79008007060'),
    Smartphone('Samsung', 'Galaxy A17', '+79231234567'),
    Smartphone('Poco', 'F7 Ростест', '+79039908070'),
    Smartphone('HUAWEI', 'Pura 80', '+79131233241'),
    Smartphone('Google', 'Pixel 10 ', '+79526483792'),
]

for smartphone in catalog:
    print(f'{smartphone.brandTel} - {smartphone.modelTel}. {smartphone.subscriberNumber}.')
