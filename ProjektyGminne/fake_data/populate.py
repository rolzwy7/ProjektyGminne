from projekty_gminne import models
from random import randint
from datetime import timedelta
from django.utils import timezone


opis = """Konkurs dotyczny bardzo ważnych rzeczy dotyczących mieszkańców {wstaw_nazwe_dzielnicy_tutej} i te rzeczy bardzo wszyskich interesują i są bardzo ważne"""
print("[*] Fake data populate imported")

KONKURS_GLOBAL_IT = 1
KONKURSY_NUM = 47

ORGANIZATIONS_A = [
    "Ministerstwo",
    "Organizacja",
    "Zrzeszenie"
]

ORGANIZATIONS_B = [
    "Nauki i Turystyki",
    "Robienia Hałasu",
    "Sportów wodnych i niewodnych",
    "Żeglarstwa",
    "Kultury",
    "Oświaty",
    "Palenia Trampek",
]


def get_rand_dzielnica():
    rand = randint(1, models.Dzielnica.objects.count()) - 1
    return models.Dzielnica.objects.all()[rand]


def add_projekty():
    pass


def add_konkurs(active):
    if active:
        from_ = randint(-30, -10)
        to = randint(10, 30)
    else:
        from_ = randint(-60, -30)
        to = randint(-40, -20)
    global KONKURS_GLOBAL_IT
    dzielnica_name = get_rand_dzielnica().name
    konkurs = models.Konkurs(
        dogrywka=False,
        dzielnica_id=get_rand_dzielnica(),
        description=opis,
        date_start=timezone.now() + timedelta(days=from_),
        date_finish=timezone.now() + timedelta(days=to),
        name="Konkurs #%s - %s" % (KONKURS_GLOBAL_IT, dzielnica_name)
    )
    print("\t- added:", konkurs)
    konkurs.save()
    KONKURS_GLOBAL_IT = KONKURS_GLOBAL_IT + 1


def add_projekty():
    count = 0
    all_konkurs = models.Konkurs.objects.all()
    all_konkurs_count = models.Konkurs.objects.count()
    for i in range(0, all_konkurs_count):
        for j in range(0, 4):
            dofinan = randint(1, 10) * 10 ** randint(5, 6)
            print("\t-Projekt #%s%s" % (i, j))
            proj_obj = models.Projekt(
                konkurs_id=all_konkurs[i],
                name="Projekt #%s%s" % (i, j),
                instytucja_wdrazajaca="%s %s" % (
                    ORGANIZATIONS_A[randint(0, len(ORGANIZATIONS_A) - 1)],
                    ORGANIZATIONS_B[randint(0, len(ORGANIZATIONS_B) - 1)]
                ),
                wnioskodawca="Gmina Warszawa",
                okres_realizacji_od=timezone.now() + timedelta(days=randint(360, 720)),
                okres_realizacji_do=timezone.now() + timedelta(days=randint(90, 180)),
                wartosc_projektu=dofinan,
                kwota_dofinansowania=int(dofinan * (randint(10, 50)/100)),
                description="Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea"
            )
            proj_obj.save()
            count = count + 1


def populate():
    # Delete all
    print("- deleting data from tables")
    to_delete = [
        models.Gmina, models.Dzielnica, models.Konkurs,
        models.Projekt, models.Glos, models.ApiMockData
    ]
    for _ in to_delete:
        print("\t- done:", _)
        _.objects.all().delete()

    print("- Adding gmina Warszawa")
    # Gmina
    if models.Gmina.objects.filter(name="Warszawa").count() != 1:
        gmina = models.Gmina(name="Warszawa")
        gmina.save()

    print("- Adding dzielnice:")
    # Dzielnice
    DZIELNICE = [
        'Bemowo', 'Białołęka', 'Bielany', 'Mokotów',
        'Ochota', 'Praga-Południe', 'Praga-Północ', 'Rembertów',
        'Śródmieście', 'Targówek', 'Ursus', 'Ursynów',
        'Wawer', 'Wesoła', 'Wilanów', 'Włochy', 'Wola', 'Żoliborz'
    ]
    for d in DZIELNICE:
        gmina_warszawa = models.Gmina.objects.all()[0]
        dzielnica = models.Dzielnica(gmina_id=gmina_warszawa, name=d)
        dzielnica.save()
        print("\t- added:", d)
    # Konkursy
    print("- Adding konkursy:")
    for i in range(0, KONKURSY_NUM):
        if i % 3:
            add_konkurs(False)
        else:
            add_konkurs(True)
    print("- Adding projekty:")
    add_projekty()

populate()
