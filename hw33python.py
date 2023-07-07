

#дз
class Kruzka:
    def __init__(self, color, text, type):
        self.color = color                                        # Цвет кружки
        self.text = text                                          # Текст на кружке
        self.type = type                                          # Тип кружки (с текстом, с картинкой и т.д.)

k1 = Kruzka('white', 'Boss', 'с текстом')
k2 = Kruzka('black', 'spidermen2', 'с картинкой')
k3 = Kruzka('Серая','Ха ха домой','с гравировкой')
k4 = Kruzka('Голубая','анилоксовый вал это не дукторный','с термопечатью')



class Market:
    katalog = []                                                  # Список кружек в каталоге
    sklad = []                                                    # Список кружек на складе

    def add_catalog(self, kruzka):
        self.katalog.append(kruzka)                               # Добавление кружки в каталог

    def smotri_catalog(self):
        for kruzka in self.katalog:
            print(kruzka.__dict__)                                # Вывод атрибутов кружки из каталога

    def zakaz_catalog(self, index, kolichestvo):
        if index >= 0 and index < len(self.katalog):              # Проверка индекса каталога
            kruzka = self.katalog[index]                          # Получение кружки по индексу из каталога
            self.sklad.append(kruzka)                             # Добавление кружки на склад
            self.sklad.append(kolichestvo)                        # Добавление количества кружек на складе
            print(f"Заказана партия кружек {kruzka.color} {kruzka.text} {kruzka.type}. Количество: {kolichestvo}")
        else:
            print("Некорректный индекс каталога")

    def smotri_skladd(self):
        for i in range(0, len(self.sklad), 2):                    # Обход элементов на складе с шагом 2
            kruzka = self.sklad[i]                                # Получение кружки из списка на складе
            kolichestvo = self.sklad[i+1]                         # Получение количества кружек на складе
            print(f"На складе есть {kolichestvo} кружек {kruzka.color} {kruzka.type}")

    def sell_magaz(self, kruzka):
        for i in range(0, len(self.sklad), 2):
            if self.sklad[i] == kruzka and self.sklad[i + 1] > 0: # Проверка соответствия кружки и наличия на складе
                self.sklad[i + 1] -= 1                            #Отнимаем количество кружек
                print(f"Продана кружка {kruzka.color} {kruzka.type}")
                return True
        print("Такой кружки нет на складе или она закончилась")
        return False



market = Market()
market.add_catalog(k1)                                             # Добавление кружки k1 в каталог
market.add_catalog(k2)
market.add_catalog(k3)
market.add_catalog(k4)

market.smotri_catalog()                                            # Просмотр каталога

market.zakaz_catalog(0, 5)                                         # Заказ партии кружек по индексу 0 с количеством 5
market.zakaz_catalog(1, 3)
market.zakaz_catalog(2, 12)
market.zakaz_catalog(3, 43)

market.smotri_skladd()                                             # Просмотр склада

market.sell_magaz(k1)                                              # Продажа кружки
market.sell_magaz(k2)
market.sell_magaz(k3)
market.sell_magaz(k4)
market.sell_magaz(k4)

market.smotri_skladd()                                             # Просмотр склада после продажи
