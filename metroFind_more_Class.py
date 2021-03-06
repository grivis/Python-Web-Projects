import re

metroTMP = {'Новоясеневская6' : [('Ясенево6',), 1000, '', False],
             'Ясенево6' : [('Новоясеневская6', 'Теплый стан6'), 1000, '', False],
             'Теплый стан6' : [('Ясенево6', 'Коньково6'), 1000, '', False],
             'Коньково6': [('Теплый стан6', 'Беляево6'), 1000, '', False],
             'Беляево6': [('Коньково6', 'Калужская6'), 1000, '', False],
             'Калужская6': [('Беляево6', 'Новые черемушки6'), 1000, '', False],
             'Новые черемушки6': [('Калужская6', 'Профсоюзная6'), 1000, '', False],
             'Профсоюзная6': [('Новые черемушки6', 'Академическая6'), 1000, '', False],
             'Академическая6': [('Профсоюзная6', 'Ленинский проспект6'), 1000, '', False],
             'Ленинский проспект6': [('Академическая6', 'Шаболовская6'), 1000, '', False],
             'Шаболовская6': [('Ленинский проспект6', 'Октябрьская6'), 1000, '', False],
             'Октябрьская6': [('Октябрьская5', 'Третьяковская6', 'Шаболовская6'), 1000, '', False],
             'Третьяковская6': [('Октябрьская6', 'Китай-город6', 'Новокузнецкая2', 'Третьяковская8'), 1000, '', False],
             'Китай-город6': [('Третьяковская6', 'Тургеневская6', 'Китай-город7'), 1000, '', False],
             'Тургеневская6': [('Китай-город6', 'Сухаревская6', 'Чистые пруды1', 'Сретенский бульвар10'), 1000, '', False],
             'Сухаревская6': [('Тургеневская6', 'Проспект мира6'), 1000, '', False],
             'Проспект мира6': [('Проспект мира5', 'Сухаревская6', 'Рижская6'), 1000, '', False],
             'Рижская6': [('Проспект мира6', 'Алексеевская6'), 1000, '', False],
             'Алексеевская6': [('Рижская6', 'ВДНХ6'), 1000, '', False],
             'ВДНХ6': [('Алексеевская6', 'Ботанический сад6'), 1000, '', False],
             'Ботанический сад6': [('ВДНХ6', 'Свиблово6'), 1000, '', False],
             'Свиблово6': [('Ботанический сад6', 'Бабушкинская6'), 1000, '', False],
             'Бабушкинская6': [('Свиблово6', 'Медведково6'), 1000, '', False],
             'Медведково6': [('Бабушкинская6',), 1000, '', False],
             'Бульвар Дмитрия Донского9' : [('Аннино9',), 1000, '', False],
             'Аннино9' : [('Бульвар Дмитрия Донского9', 'Улица академика Янгеля9'), 1000, '', False],
             'Улица академика Янгеля9' : [('Аннино9', 'Пражская9'), 1000, '', False],
             'Пражская9': [('Улица академика Янгеля9', 'Южная9'), 1000, '', False],
             'Южная9': [('Пражская9', 'Чертановская9'), 1000, '', False],
             'Чертановская9': [('Южная9', 'Севастопольская9'), 1000, '', False],
             'Севастопольская9': [('Чертановская9', 'Нахимовский проспект9', 'Каховская11'), 1000, '', False],
             'Нахимовский проспект9': [('Севастопольская9', 'Нагорная9'), 1000, '', False],
             'Нагорная9': [('Нахимовский проспект9', 'Нагатинская9'), 1000, '', False],
             'Нагатинская9': [('Нагорная9', 'Тульская9'), 1000, '', False],
             'Тульская9': [('Нагатинская9', 'Серпуховская9'), 1000, '', False],
             'Серпуховская9': [('Тульская9', 'Полянка9', 'Добрынинская5'), 1000, '', False],
             'Полянка9': [('Серпуховская9', 'Боровицкая9'), 1000, '', False],
             'Боровицкая9': [('Полянка9', 'Чеховская9', 'Библиотека имени Ленина1', 'Арбатская3', 'Александровский сад4'), 1000, '', False],
             'Чеховская9': [('Боровицкая9', 'Цветной бульвар9', 'Тверская2', 'Пушкинская7'), 1000, '', False],
             'Цветной бульвар9': [('Чеховская9', 'Менделеевская9', 'Трубная10'), 1000, '', False],
             'Менделеевская9': [('Савеловская9', 'Цветной бульвар9'), 1000, '', False],
             'Савеловская9': [('Менделеевская9', 'Дмитровская9'), 1000, '', False],
             'Дмитровская9': [('Савеловская9', 'Тимирязевская9'), 1000, '', False],
             'Тимирязевская9': [('Дмитровская9', 'Петровско-Разумовская9'), 1000, '', False],
             'Петровско-Разумовская9': [('Тимирязевская9', 'Владыкино9'), 1000, '', False],
             'Владыкино9': [('Петровско-Разумовская9', 'Отрадное9'), 1000, '', False],
             'Отрадное9': [('Владыкино9', 'Бибирево9'), 1000, '', False],
             'Бибирево9': [('Отрадное9', 'Алтуфьево9'), 1000, '', False],
             'Алтуфьево9': [('Бибирево9',), 1000, '', False],
             'Октябрьская5': [('Парк культуры5', 'Добрынинская5', 'Октябрьская6'), 1000, '', False],
             'Парк культуры5' : [('Октябрьская5', 'Киевская5', 'Парк культуры1'), 1000, '', False],
             'Киевская5': [('Парк культуры5', 'Краснопресненская5', 'Киевская3', 'Киевская4'), 1000, '', False],
             'Краснопресненская5': [('Белорусская5', 'Киевская5'), 1000, '', False],
             'Белорусская5': [('Краснопресненская5', 'Новослободская5', 'Белорусская2'), 1000, '', False],
             'Новослободская5': [('Белорусская5', 'Проспект мира5', 'Менделеевская9'), 1000, '', False],
             'Проспект мира5': [('Новослободская5', 'Комсомольская5', 'Проспект мира6'), 1000, '', False],
             'Комсомольская5': [('Проспект мира5', 'Курская5', 'Комсомольская1'), 1000, '', False],
             'Курская5': [('Комсомольская5', 'Таганская5', 'Курская3', 'Чкаловская10'), 1000, '', False],
             'Таганская5': [('Курская5', 'Павелецкая5', 'Таганская7'), 1000, '', False],
             'Добрынинская5': [('Октябрьская5', 'Павелецкая5','Серпуховская9'), 1000, '', False],
             'Павелецкая5': [('Таганская5', 'Добрынинская5', 'Павелецкая2'), 1000, '', False],
             'Саларьево1': [('Румянцево1',), 1000, '', False],
             'Румянцево1': [('Саларьево1', 'Тропарево1'), 1000, '', False],
             'Тропарево1': [('Румянцево1', 'Юго-Западная1'), 1000, '', False],
             'Юго-Западная1': [('Тропарево1', 'Проспект Вернадского1'), 1000, '', False],
             'Проспект Вернадского1': [('Юго-Западная1', 'Университет1'), 1000, '', False],
             'Университет1': [('Проспект Вернадского1', 'Воробьевы горы1'), 1000, '', False],
             'Воробьевы горы1': [('Университет1', 'Спортивная1'), 1000, '', False],
             'Спортивная1': [('Воробьевы горы1', 'Фрунзенская1'), 1000, '', False],
             'Фрунзенская1': [('Спортивная1', 'Парк культуры1'), 1000, '', False],
             'Парк культуры1': [('Фрунзенская1', 'Кропоткинская1', 'Парк культуры5'), 1000, '', False],
             'Кропоткинская1': [('Библиотека имени Ленина1', 'Парк культуры1'), 1000, '', False],
             'Библиотека имени Ленина1': [('Кропоткинская1', 'Охотный ряд1', 'Боровицкая9', 'Арбатская3', 'Александровский сад4'), 1000, '', False],
             'Охотный ряд1': [('Библиотека имени Ленина1', 'Лубянка1', 'Театральная2', 'Площадь революции3'), 1000, '', False],
             'Лубянка1': [('Охотный ряд1', 'Чистые пруды1', 'Кузнецкий мост7'), 1000, '', False],
             'Чистые пруды1': [('Лубянка1', 'Красные ворота1'), 1000, '', False],
             'Красные ворота1': [('Чистые пруды1', 'Комсомольская1'), 1000, '', False],
             'Комсомольская1': [('Красные ворота1', 'Комсомольская5', 'Красносельская1'), 1000, '', False],
             'Красносельская1': [('Комсомольская1', 'Сокольники1'), 1000, '', False],
             'Сокольники1': [('Красносельская1', 'Преображенская площадь1'), 1000, '', False],
             'Преображенская площадь1': [('Сокольники1', 'Черкизовская1'), 1000, '', False],
             'Черкизовская1': [('Преображенская площадь1', 'Бульвар Рокоссовского1'), 1000, '', False],
             'Бульвар Рокоссовского1': [('Черкизовская1',), 1000, '', False],
             'Алма-Атинская2': [('Красногвардейская2',), 1000, '', False],
             'Красногвардейская2': [('Алма-Атинская2','Домодедовская2'), 1000, '', False],
             'Домодедовская2': [('Красногвардейская2', 'Орехово2'), 1000, '', False],
             'Орехово2': [('Домодедовская2', 'Царицыно2'), 1000, '', False],
             'Царицыно2': [('Орехово2', 'Кантемировская2'), 1000, '', False],
             'Кантемировская2': [('Царицыно2', 'Каширская2'), 1000, '', False],
             'Каширская2': [('Кантемировская2', 'Коломенская2', 'Каширская11'), 1000, '', False],
             'Коломенская2': [('Каширская2', 'Автозаводская2'), 1000, '', False],
             'Автозаводская2': [('Коломенская2', 'Павелецкая2'), 1000, '', False],
             'Павелецкая2': [('Автозаводская2', 'Новокузнецкая2', 'Павелецкая5'), 1000, '', False],
             'Новокузнецкая2': [('Павелецкая2', 'Театральная2', 'Третьяковская6', 'Третьяковская8'), 1000, '', False],
             'Театральная2': [('Новокузнецкая2', 'Тверская2', 'Охотный ряд1', 'Площадь революции3'), 1000, '', False],
             'Тверская2': [('Театральная2', 'Маяковская2', 'Чеховская9', 'Пушкинская7'), 1000, '', False],
             'Маяковская2': [('Тверская2', 'Белорусская2'), 1000, '', False],
             'Белорусская2': [('Маяковская2', 'Динамо2', 'Белорусская5'), 1000, '', False],
             'Динамо2': [('Белорусская2', 'Аэропорт2'), 1000, '', False],
             'Аэропорт2': [('Динамо2', 'Сокол2'), 1000, '', False],
             'Сокол2': [('Аэропорт2', 'Войковская2'), 1000, '', False],
             'Войковская2': [('Сокол2', 'Водный стадион2'), 1000, '', False],
             'Водный стадион2': [('Войковская2', 'Речной вокзал2'), 1000, '', False],
             'Речной вокзал2': [('Водный стадион2',), 1000, '', False],
             'Зябликово10': [('Шипиловская10',), 1000, '', False],
             'Шипиловская10': [('Зябликово10','Борисово10'), 1000, '', False],
             'Борисово10': [('Шипиловская10', 'Марьино10'), 1000, '', False],
             'Марьино10': [('Борисово10', 'Братиславская10'), 1000, '', False],
             'Братиславская10': [('Марьино10', 'Люблино10'), 1000, '', False],
             'Люблино10': [('Братиславская10', 'Волжская10'), 1000, '', False],
             'Волжская10': [('Люблино10', 'Печатники10'), 1000, '', False],
             'Печатники10': [('Волжская10', 'Кожуховская10'), 1000, '', False],
             'Кожуховская10': [('Печатники10', 'Дубровка10'), 1000, '', False],
             'Дубровка10': [('Кожуховская10', 'Крестьянская застава10'), 1000, '', False],
             'Крестьянская застава10': [('Дубровка10', 'Римская10', 'Пролетарская7'), 1000, '', False],
             'Римская10': [('Крестьянская застава10', 'Чкаловская10', 'Площадь Ильича8'), 1000, '', False],
             'Чкаловская10': [('Римская10', 'Курская5', 'Сретенский бульвар10', 'Курская3'), 1000, '', False],
             'Сретенский бульвар10': [('Чкаловская10', 'Трубная10', 'Чистые пруды1', 'Тургеневская6'), 1000, '', False],
             'Трубная10': [('Сретенский бульвар10', 'Достоевская10', 'Цветной бульвар9'), 1000, '', False],
             'Достоевская10': [('Трубная10', 'Марьина роща10'), 1000, '', False],
             'Марьина роща10': [('Достоевская10', 'Бутырская10'), 1000, '', False],
             'Бутырская10': [('Марьина роща10', 'Фонвизинская10'), 1000, '', False],
             'Фонвизинская10': [('Бутырская10',), 1000, '', False],
             'Котельники7': [('Жулебино7',), 1000, '', False],
             'Жулебино7': [('Котельники7', 'Лермонтовский проспект7'), 1000, '', False],
             'Лермонтовский проспект7': [('Жулебино7', 'Выхино7'), 1000, '', False],
             'Выхино7': [('Лермонтовский проспект7', 'Рязанский проспект7'), 1000, '', False],
             'Рязанский проспект7': [('Выхино7', 'Кузьминки7'), 1000, '', False],
             'Кузьминки7': [('Рязанский проспект7', 'Текстильщики7'), 1000, '', False],
             'Текстильщики7': [('Кузьминки7', 'Волгоградский проспект7'), 1000, '', False],
             'Волгоградский проспект7': [('Текстильщики7', 'Пролетарская7'), 1000, '', False],
             'Пролетарская7': [('Волгоградский проспект7', 'Таганская7', 'Крестьянская застава10'), 1000, '', False],
             'Таганская7': [('Пролетарская7', 'Китай-город7', 'Таганская5'), 1000, '', False],
             'Китай-город7': [('Таганская7', 'Китай-город6', 'Кузнецкий мост7'), 1000, '', False],
             'Кузнецкий мост7': [('Китай-город7', 'Пушкинская7', 'Лубянка1'), 1000, '', False],
             'Пушкинская7': [('Кузнецкий мост7', 'Баррикадная7', 'Тверская2', 'Чеховская9'), 1000, '', False],
             'Баррикадная7': [('Пушкинская7', 'Улица 1905 года7', 'Краснопресненская5'), 1000, '', False],
             'Улица 1905 года7': [('Баррикадная7', 'Беговая7'), 1000, '', False],
             'Беговая7': [('Улица 1905 года7', 'Полежаевская7'), 1000, '', False],
             'Полежаевская7': [('Беговая7', 'Октябрьское Поле7'), 1000, '', False],
             'Октябрьское Поле7': [('Полежаевская7', 'Щукинская7'), 1000, '', False],
             'Щукинская7': [('Октябрьское Поле7', 'Спартак7'), 1000, '', False],
             'Спартак7': [('Щукинская7', 'Тушинская7'), 1000, '', False],
             'Тушинская7': [('Спартак7', 'Сходненская7'), 1000, '', False],
             'Сходненская7': [('Тушинская7', 'Планерная7'), 1000, '', False],
             'Планерная7': [('Сходненская7', ), 1000, '', False],
             'Новокосино8': [('Новогиреево8',), 1000, '', False],
             'Новогиреево8': [('Новокосино8', 'Перово8'), 1000, '', False],
             'Перово8': [('Новогиреево8', 'Шоссе энтузиастов8'), 1000, '', False],
             'Шоссе энтузиастов8': [('Перово8', 'Авиамоторная8'), 1000, '', False],
             'Авиамоторная8': [('Шоссе энтузиастов8', 'Площадь Ильича8'), 1000, '', False],
             'Площадь Ильича8': [('Авиамоторная8', 'Марксистская8', 'Римская10'), 1000, '', False],
             'Марксистская8': [('Площадь Ильича8', 'Третьяковская8', 'Таганская7', 'Таганская5'), 1000, '', False],
             'Третьяковская8': [('Марксистская8', 'Новокузнецкая2', 'Третьяковская6'), 1000, '', False],
             'Щелковская3': [('Первомайская3', ), 1000, '', False],
             'Первомайская3': [('Щелковская3', 'Измайловская3'), 1000, '', False],
             'Измайловская3': [('Первомайская3', 'Партизанская3'), 1000, '', False],
             'Партизанская3': [('Измайловская3', 'Семеновская3'), 1000, '', False],
             'Семеновская3': [('Партизанская3', 'Электрозаводская3'), 1000, '', False],
             'Электрозаводская3': [('Семеновская3', 'Бауманская3'), 1000, '', False],
             'Бауманская3': [('Электрозаводская3', 'Курская3'), 1000, '', False],
             'Курская3': [('Бауманская3', 'Площадь революции3', 'Чкаловская10'), 1000, '', False],
             'Площадь революции3': [('Курская3', 'Арбатская3', 'Театральная2', 'Охотный ряд1'), 1000, '', False],
             'Арбатская3': [('Площадь революции3', 'Смоленская3', 'Библиотека имени Ленина1', 'Боровицкая9', 'Александровский сад4'), 1000, '', False],
             'Смоленская3': [('Арбатская3', 'Киевская3'), 1000, '', False],
             'Киевская3': [('Смоленская3', 'Парк победы3', 'Киевская5', 'Киевская4'), 1000, '', False],
             'Парк победы3': [('Киевская3', 'Славянский бульвар3'), 1000, '', False],
             'Славянский бульвар3': [('Парк победы3', 'Кунцевская3'), 1000, '', False],
             'Кунцевская3': [('Славянский бульвар3', 'Молодежная3', 'Кунцевская4'), 1000, '', False],
             'Молодежная3': [('Кунцевская3', 'Крылатское3'), 1000, '', False],
             'Крылатское3': [('Молодежная3', 'Строгино3'), 1000, '', False],
             'Строгино3': [('Крылатское3', 'Мякинино3'), 1000, '', False],
             'Мякинино3': [('Строгино3', 'Волоколамская3'), 1000, '', False],
             'Волоколамская3': [('Мякинино3', 'Митино3'), 1000, '', False],
             'Митино3': [('Волоколамская3', 'Пятницкое шоссе3'), 1000, '', False],
             'Пятницкое шоссе3': [('Митино3',), 1000, '', False],
             'Александровский сад4': [('Арбатская4', 'Охотный ряд1', 'Боровицкая9', 'Арбатская3'), 1000, '', False],
             'Арбатская4': [('Александровский сад4', 'Смоленская4'), 1000, '', False],
             'Смоленская4': [('Арбатская4', 'Киевская4'), 1000, '', False],
             'Киевская4': [('Смоленская4', 'Студенческая4', 'Киевская5', 'Киевская3'), 1000, '', False],
             'Студенческая4': [('Киевская4', 'Кутузовская4'), 1000, '', False],
             'Кутузовская4': [('Студенческая4', 'Фили4'), 1000, '', False],
             'Фили4': [('Кутузовская4', 'Багратионовская4'), 1000, '', False],
             'Багратионовская4': [('Фили4', 'Филевский парк4'), 1000, '', False],
             'Филевский парк4': [('Багратионовская4', 'Пионерская4'), 1000, '', False],
             'Пионерская4': [('Филевский парк4', 'Кунцевская4'), 1000, '', False],
             'Кунцевская4': [('Пионерская4', 'Кунцевская4', 'Кунцевская3'), 1000, '', False],
             'Каховская11': [('Варшавская11', 'Севастопольская9'), 1000, '', False],
             'Варшавская11': [('Каховская11', 'Каширская11'), 1000, '', False],
             'Каширская11': [('Варшавская11', 'Каширская2'), 1000, '', False]}


metroTMP1 = {'Проспект Ветеранов1': [('Ленинский проспект1',), 1000, '', False],
            'Ленинский проспект1': [('Проспект Ветеранов1', 'Автово1'), 1000, '', False],
            'Автово1': [('Ленинский проспект1', 'Кировский завод1'), 1000, '', False],
            'Кировский завод1': [('Автово1', 'Нарвская1'), 1000, '', False],
            'Нарвская1': [('Кировский завод1', 'Балтийская1'), 1000, '', False],
            'Балтийская1': [('Нарвская1', 'Технологический институт1'), 1000, '', False],
            'Технологический институт1': [('Балтийская1', 'Пушкинская1', 'Технологический институт2'), 1000, '', False],
            'Пушкинская1': [('Технологический институт1', 'Владимирская1', 'Звенигородская5'), 1000, '', False],
            'Владимирская1': [('Пушкинская1', 'Площадь Восстания1', 'Достоевская4'), 1000, '', False],
            'Площадь Восстания1': [('Владимирская1', 'Чернышевская1', 'Маяковская3'), 1000, '', False],
             'Чернышевская1': [('Площадь Восстания1', 'Площадь Ленина1'), 1000, '', False],
             'Площадь Ленина1': [('Чернышевская1', 'Выборгская1'), 1000, '', False],
             'Выборгская1': [('Площадь Ленина1', 'Лесная1'), 1000, '', False],
             'Лесная1': [('Выборгская1', 'Площадь Мужества1'), 1000, '', False],
             'Площадь Мужества1': [('Лесная1', 'Политехническая1'), 1000, '', False],
             'Политехническая1': [('Площадь Мужества1', 'Академическая1'), 1000, '', False],
             'Академическая1': [('Политехническая1', 'Гражданский проспект1'), 1000, '', False],
             'Гражданский проспект1': [('Академическая1', 'Девяткино1'), 1000, '', False],
             'Девяткино1': [('Гражданский проспект1',), 1000, '', False],
             'Купчино2': [('Звездная2',), 1000, '', False],
             'Звездная2': [('Купчино2', 'Московская2'), 1000, '', False],
             'Московская2': [('Звездная2', 'Парк Победы2'), 1000, '', False],
             'Парк Победы2': [('Московская2', 'Электросила2'), 1000, '', False],
             'Электросила2': [('Парк Победы2', 'Московские ворота2'), 1000, '', False],
             'Московские ворота2': [('Электросила2', 'Фрунзенская2'), 1000, '', False],
             'Фрунзенская2': [('Московские ворота2', 'Технологический институт2'), 1000, '', False],
             'Технологический институт2': [('Фрунзенская2', 'Сенная площадь2', 'Технологический институт1'), 1000, '', False],
             'Сенная площадь2': [('Технологический институт2', 'Невский проспект2', 'Спасская4'), 1000, '', False],
             'Невский проспект2': [('Сенная площадь2', 'Горьковская2', 'Гостиный двор3'), 1000, '', False],
             'Горьковская2': [('Невский проспект2', 'Петроградская2'), 1000, '', False],
             'Петроградская2': [('Горьковская2', 'Черная речка2'), 1000, '', False],
             'Черная речка2': [('Петроградская2', 'Пионерская2'), 1000, '', False],
             'Пионерская2': [('Черная речка2', 'Удельная2'), 1000, '', False],
             'Удельная2': [('Пионерская2', 'Озерки2'), 1000, '', False],
             'Озерки2': [('Удельная2', 'Проспект Просвещения2'), 1000, '', False],
             'Проспект Просвещения2': [('Озерки2', 'Парнас2'), 1000, '', False],
             'Парнас2': [('Проспект Просвещения2',), 1000, '', False],
             'Международная5': [('Бухарестская5',), 1000, '', False],
             'Бухарестская5': [('Международная5', 'Волковская5'), 1000, '', False],
             'Волковская5': [('Бухарестская5', 'Обводный канал5'), 1000, '', False],
             'Обводный канал5': [('Волковская5', 'Звенигородская5'), 1000, '', False],
             'Звенигородская5': [('Обводный канал5', 'Садовая5', 'Пушкинская1'), 1000, '', False],
             'Садовая5': [('Звенигородская5', 'Адмиралтейская5', 'Сенная площадь2', 'Спасская4'), 1000, '', False],
             'Адмиралтейская5': [('Садовая5', 'Спортивная5'), 1000, '', False],
             'Спортивная5': [('Адмиралтейская5', 'Чкаловская5'), 1000, '', False],
             'Чкаловская5': [('Спортивная5', 'Крестовский остров5'), 1000, '', False],
             'Крестовский остров5': [('Чкаловская5', 'Старая Деревня5'), 1000, '', False],
             'Старая Деревня5': [('Крестовский остров5', 'Комендантский проспект5'), 1000, '', False],
             'Комендантский проспект5': [('Старая Деревня5',), 1000, '', False],
             'Рыбацкое3': [('Обухово3',), 1000, '', False],
             'Обухово3': [('Рыбацкое3', 'Пролетарская3'), 1000, '', False],
             'Пролетарская3': [('Обухово3', 'Ломоносовская3'), 1000, '', False],
             'Ломоносовская3': [('Пролетарская3', 'Елизаровская3'), 1000, '', False],
             'Елизаровская3': [('Ломоносовская3', 'Площадь Александра Невского3'), 1000, '', False],
             'Площадь Александра Невского3': [('Елизаровская3', 'Маяковская3', 'Площадь Александра Невского4'), 1000, '', False],
             'Маяковская3': [('Гостиный двор3', 'Площадь Александра Невского3', 'Площадь Восстания1'), 1000, '', False],
             'Гостиный двор3': [('Площадь Александра Невского3', 'Василеостровская3', 'Невский проспект2'), 1000, '', False],
             'Василеостровская3': [('Гостиный двор3', 'Приморская3'), 1000, '', False],
             'Приморская3': [('Василеостровская3', ), 1000, '', False],
             'Улица Дыбенко4': [('Проспект Большевиков4',), 1000, '', False],
             'Проспект Большевиков4': [('Улица Дыбенко4', 'Ладожская4'), 1000, '', False],
             'Ладожская4': [('Проспект Большевиков4', 'Новочеркасская4'), 1000, '', False],
             'Новочеркасская4': [('Ладожская4', 'Площадь Александра Невского4'), 1000, '', False],
             'Площадь Александра Невского4': [('Новочеркасская4', 'Лиговский проспект4', 'Площадь Александра Невского3'), 1000, '', False],
             'Лиговский проспект4': [('Площадь Александра Невского4', 'Достоевская4'), 1000, '', False],
             'Достоевская4': [('Лиговский проспект4', 'Спасская4', 'Владимирская1'), 1000, '', False],
             'Спасская4': [('Сенная площадь2', 'Садовая5'), 1000, '', False]}


branchesMos = {'Сокольническая' : '1', 'Замоскворецкая' : '2', 'Арбатско-Покровская' : '3', 'Филёвская' : '4', 'Кольцевая' : '5', 'Калужско-Рижская' : '6',
            'Таганско-Краснопресненская' : '7', 'Калининско-Солнцевской' : '8', 'Серпуховско-Тимирязевская' : '9', 'Люблинско-Дмитровская' : '10',
            'Каховская' : '11'}

branchesSpb = {'Кировско-Выборгская' : '1', 'Московско-Петроградская' : '2', 'Невско-Василеостровская' : '3', 'Правобережная' : '4', 'Фрунзенско-Приморская' : '5'}

def findNumOfBranch(st, metroLst):
    branchNum = ''
    for i in metroLst:
        if i[:-1] == st:
            branchNum = i[-1:]
        elif i[:-2] == st:
            branchNum = i[-2:]

    return branchNum

def findWay(yourStation, bankStation, city):
    global metroTMP, metroBranch, branchesSpb, metroTMP1
    metroBranch = {}
    metroMap = {}

    if  city == 0:
        metroBranch = branchesMos
        metroMap = metroTMP
    else:
        metroBranch = branchesSpb
        metroMap = metroTMP1

    count = len(metroMap)


    for i in metroMap.keys():
        metroMap[i][1] = 1000
        metroMap[i][2] = ''
        metroMap[i][3] = False
    metroLst = list(metroMap)

    if yourStation[-1] != ')':
        yourStation += findNumOfBranch(yourStation, metroLst)
    else:
        r1 = re.findall('[(](.*)[)]', yourStation)
        branch = metroBranch[r1[0]]
        r2 = re.findall('(.+)[ ]', yourStation)
        yourStation = r2[0] + branch

    if bankStation[-1] != ')':
        bankStation += findNumOfBranch(bankStation, metroLst)
    else:
        r1 = re.findall('[(](.*)[)]', bankStation)
        branch = metroBranch[r1[0]]
        r2 = re.findall('(.+)[ ]', bankStation)
        bankStation = r2[0] + branch

    bankStation += findNumOfBranch(bankStation, metroLst)

    #print(yourStation, bankStation)

    st = metroMap.get(yourStation)

    if not st:
        return None, None
    else:
        st[1] = 0
        for i in st[0]:
            temp = metroMap.get(i)
            temp[1] = 1
            temp[2] = yourStation
        st[2] = yourStation
        st[3] = True
        count -= 1

        while count > 0:
            for i in metroMap.keys():
                st = metroMap[i]
                if st[1] != 1000 and st[3] != True:
                    weight = st[1]
                    for j in st[0]:
                        if metroMap[j][1] >= (weight + 1):
                            metroMap[j][1] = (weight + 1)
                            metroMap[j][2] = i
                    metroMap[i][3] = True
                    if count <= 0:
                        break
                    count -= 1

        # wayList = []
        # wayList.append(bankStation)
        # curSt = metroMap[bankStation][2]
        # while curSt != yourStation:
        #     wayList.append(curSt)
        #     curSt = metroMap[curSt][2]


    return metroMap[bankStation][1]





