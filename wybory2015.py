import pandas as pd
from collections import OrderedDict


col = u'Zawód'
profession_mapping = OrderedDict([
    ## przed-grupy:
    (u'automatyk', [
        u'automat',
    ]),
    (u'biolog', [
        u'biolog',
        u'biotechnolog',
        u'ekolog',
    ]),
    (u'elektryk/elektronik',[
        u'elektryk',
        u'elektronik',
        u'elektr',
    ]),
    (u'pracownik bhp', [
        u'bhp',
        u'BHP',
        u'higieny pracy',
        u'inspektor pracy',
        u'inspektor bezpieczeństwa',
    ]),
    (u'budowlaniec', [
        u'budowlaniec',

        u'spawacz',
        u'murarz',
        u'tynk',

        u'inż. budownictwa',
        u'inżynier budownictwa',        # ??
        u'technik budownictwa',
        u'technik budowlany',

        u'budowl',

    ]),
    (u'chemik', [
        u'chemik',
        u'technik chemik',
        u'chemi',
    ]),
    (u'Etyk/Filozof', [
        u'etyk',
        u'etyczka',
        u'teolog',
        u'teolożka',
        u'filozof',
        u'filozofka',
    ]),
    (u'Fryzjer/Kosmetyka', [
        u'fryzjer',
        u'kosmetyczka',
    ]),
    (u'Górnik', [
        u'górnik',
        u'górnictw',
        u'górnic',
    ]),
    (u'Historyk', [
        u'historyk',
        u'historyk sztuki',
        u'archeolog',
        u'history',

    ]),
    (u'mechanik', [
        u'mechanik',
        u'mechatronik',
        u'technik-mechanik',
        u'technik mechanik',

    ]),
    (u'nauczyciel', [
        u'nauczyciel',
        u'polonista',
        u'polonistka',
        u'matematyk',
        u'wychowawca',

    ]),
    (u'Kierowca', [
        u'kierowca',
        u'taksówkarz',
        u'instruktor nauki jazdy',
    ]),
    (u'kulturoznawca', [
        u'kultur',
    ]),
    (u'Logistyk', [
        u'logistyk',
        u'specjalista do spraw logistyki',
        u'specjalista ds. logistyki',
        u'mgr inż. transportu',

        u'spedytor',
        u'magazynier',
        u'magazy',
        u'logisty',
    ]),
    (u'Polityk', [
        u'polityk',
        u'polityczka',
        u'politolog',
        u'politolożka',
    ]),
    (u'rzemieślnik', [
        u'stolarz',
        u'krawiec',
        u'krawcowa',

    ]),
    (u'Sportowiec', [
        u'sportowiec',
        u'trener',
        u'sport',
        u'zawodnik',
        u'pływ',
    ]),
    (u'Student', [
        u'student',
        u'studentka',
        u'doktorant',
        u'doktorantka',
    ]),
    (u'Sociolog', [
        u'socjolog',
        u'socjolożka',
    ]),
    (u'pracownik socjalny', [
        u'pracownik socjalny',
        u'pracownica socjalna',
        u'opiekun w domu pomocy społecznej',
        u'socjal'
    ]),
    (u'pracownik turystyki', [
        u'turysty'
        u'hotel'

    ]),
    (u'pracownik gastronomii', [
        u'pracownik gastronomii',
        u'barman',
        u'kelner',
        u'kelnerka',
        u'kuchar',
        u'barista',
        u'baristka',
        u'żywienia',
        u'żywnoś',
    ]),
    (u'pracownik turystyki', [
        u'hotelarz',
        u'turyst',
    ]),
    (u'pracownik ochrony środowiska', [
        u'ochrony środowiska',
        u'środowisk',
    ]),
    (u'Językoznawca/Tłumacz', [
        u'tłumacz',
        u'tłumaczka',
        u'lektor języka',
        u'filolog',
        u'germanista',
        u'germanistka',
        u'anglista',
        u'anglistka',
        u'językoznaw',
        u'lingwist',
    ]),

    ## grupy właściwe
    (u'Bezrobotny', [
        u'bezrobotny',
        u'bezrobotna',
        u'bez zawodu',
        u'brak zawodu',
        u'nie pracuj',
    ]),
    (u'Nauczyciel/Wykładowca', [
        u'nauczyciel',
        u'wykładowca',
        u'pedagog',
        u'pedagożka',
        # u'filolog',
        u'matematyk',
        u'politolog',
        u'pracownik naukowy',
        u'dyrektor szkoły',     ## menedżer?
        u'kierownik placówki oświatowej',
        u'pracownik naukowo-dydaktyczny',
        u'pracownik umysłowy',
        u'doktor nauk',

        u'katecheta',
        u'katechetka',

        u'oświat',
    ]),
    (u'Emeryt/Rencista', [
        u'emeryt',
        u'rencista',
        u'emerytka',
        u'rencistka',
        u'emerytowany',
        u'emerytowana',
    ]),
    (u'Prawnik', [
        u'prawnik',
        u'adwokat',
        u'radca prawny',
        u'radca',
        u'notariusz',
        u'sędzia',
        u'sądu',
        u'sądo',
        u'adwoka',
        u'prawa',
    ]),
    (u'Handlowiec', [
        u'handlowiec',
        u'sprzedawca',
        u'przedstawiciel handlowy',
        u'telemarketer',
        u'specjalista do spraw sprzedaży',
        u'specjalista ds. sprzedaży',
        u'specjalista do spraw marketingu',
        u'specjalista ds. marketingu',
        u'specjalista do spraw marketingu i handlu',
        u'specjalista ds. reklamy',
        u'specjalista marketingu',
        u'specjalista ds. sprzedaży internetowej',

        u'kierownik sprzedaży',
        u'przedstawiciel medyczny',

        u'doradca klienta',
        u'marketingowiec',
        u'agent ubezpieczeniowy',       #?
        u'doradca ubezpieczeniowy',
        u'specjalista do spraw ubezpieczeń',
        u'broker',

        u'doradca do spraw rynku nieruchomości',
        u'do spraw reklamy',
        u'ds reklamy',
        u'do spraw handlu',
        u'ds. handlu',

        u'kasjer',
        u'kasjerka',

        u'kierownik do spraw sprzedaży',
        u'zaopatrzeniowiec',
        u'marketing',
        u'rachunko',
        u'public relations',
        u'ubezpiecze',
        u'sprzedaż',
        u'reklam',

    ]),
    (u'Lekarz/Farmaceuta', [
        u'lekarz',
        u'lekarz medycyny',
        u'dentysta',

        u'weterynarz',
        u'weterynar',
        u'lekarz weterynarii',
        u'lekarz medycyny',
        u'logopeda',
        u'psycholog',
        u'kardio',
        u'psycholo',
        u'orto',
        u'stomatolo',


        u'farmaceuta',
        u'technik farmacji',
        u'technik dentystyczny',

        u'ratownik medyczny',

        u'fizjoterapeuta',      ## ?
        u'fizjoterapeutka',
        u'terapeuta',
        u'terapeutka',

        u'optyk',
        u'chirurg',

        u'pielęgniarka',
        u'pielęgniarz',
        u'magister pielęgniarstwa',
        u'położna',
        u'opiekun medyczny',
        u'opiekun osoby',
        u'sanitariusz',

        u'masażysta',
        u'masażystka',

        u'technik elektroradiologii',
        u'rehabil',
        u'zdrow',
        u'leczn',
        u'medyc',
        u'farmac',

    ]),
    (u'Ekonomista', [
        u'ekonomista',
        u'ekonomistka',
        u'księgowy',
        u'księgowa',
        u'technik ekonomista',
        u'doradca podatkowy',
        u'doradca finansowy',
        u'finansista',
        u'główny księgowy',
        u'bankowiec',
        u'analityk finansowy',
        u'analityk bankowy',
        u'analityk biznesowy',
        u'magister ekonomii',
        u'specjalista bankowości',
        u'audytor',
        u'auditor',
        u'mgr ekonomii',
        u'rewident',
        u'makler',

        u'ekono',
        u'finans',
        u'bank',
        u'kredyt',
        u'giełd',
        u'księgowoś',
        u'inwesty',
        u'fundusz',

    ]),
    (u'Inżynier', [
        u'inżynier',
        u'informatyk',
        u'programista',
        u'programista aplikacji',
        u'programistka',
        u'architekt',
        u'administrator systemów komputerowych',
        u'tester oprogramowania',
        u'komputer',
        u'internet',
    ]),
    (u'Urzędnik', [
        u'urzędnik',
        u'urzędnik samorządowy',
        u'wyższy urzędnik samorządowy',
        u'parlamentarzysta',        # ???
        u'przedstawiciel władzy samorządowej',
        u'administratywistka',
        u'administratywista',
        u'pracownik administracyjny',
        u'pracownik administracji samorządowej',
        u'technik administracji',
        u'urzędnik państwowy',
        u'pracownik administracji',
        u'samorządowiec',
        u'pracownik samorządowy',
        u'pracownik administrac',
        u'pracownik nik',
        u'poseł',
        u'parlamentarzysta',
        u'parlamentarzystka',
        u'specjalista administracji publicznej',
        u'specjalista ds. administracji',
        u'mgr administracji',
        u'magister administracji',
        u'do spraw administracji',      # clash with IT?
        u'radny',
        u'radna',
        u'senator',
        u'samorząd',
        u'urzędni',

        u'działacz',
        u'związkow',
        u'władzy publicznej'

    ]),
    (u'kierownik', [
        u'kierownik',
        u'kierowniczka',
    ]),
    (u'Menedżer', [
        u'menedżer',
        u'menadżer',
        u'manager',
        u'menager',
        u'prezes',
        u'dyrektor generalny',
        u'dyrektor',
        u'kierownik',
    ]),
    (u'Rolnik', [
        u'rolnik',
        u'technik rolnik'
        u'leśnik',
        u'le\u015bnik',
        u'techik leśnik',
        u'zootechnik',
        u'ogrodnik',
        u'pszczelarz',
        u'doradca rolniczy',
        u'sadowni',
        u'roln',
        u'ogro'

    ]),
    (u'Mundurowy', [
        u'mundurowy',
        u'oficer',
        u'strażak',
        u'policjant',
        u'wojskowy',
        u'żołnierz',
        u'żołnierz zawodowy',
        u'kryminolog',
        u'detektyw',
        u'strażnik miejski',
    ]),
    (u'Przedsiębiorca', [
        u'przedsiębiorca',
        u'właściciel',
    ]),
    (u'Artysta/Wolny Zawód', [
        u'artysta',
        u'artystka',
        u'muzyk',
        u'organista',
        u'aktor',
        u'reżyser',
        u'reżyser filmowy',
        u'fotograf',
        u'dziennikarz',
        u'dziennikarka',
        u'grafik',
        u'grafik komputerowy',
        u'plastyk',
        u'publicysta',
        u'projektant wnętrz',
        u'wydawca',
        u'producent filmowy',
        u'pisarz',
        u'wokalista',
        u'wokalistka',
        u'śpiewak',
        u'śpiewaczka',
        u'piosenkar',
        u'poeta',
        u'literat',
        u'rzeźbiarz',
        u'plastyczka',
        u'plastyk',
        u'witrażysta',
        u'witrażystka',
        u'kompozytor',
        u'krytyk',
        u'bloger',
    ]),
])


def load_xls(file_path):
    with open(file_path) as fd:
        data = pd.read_excel(fd)
    return data


def map_profession(text, mapping):
    for group, tokens in mapping.items():
        for token in tokens:
            if token in text:
                return token
    return text


def consolidate(df, mapping, column=col):
    for group, tokens in mapping.items():
        for token in tokens:
            df.loc[df[col].str.contains(token), col] = group
    return df


def consolidate_column(data, mapping, column=col):
    data = data.apply(lambda row: map_profession(row[column]))
