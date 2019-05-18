from projekty_gminne import models
import random
from random import randint
from datetime import timedelta
from django.utils import timezone
from django.db.models import Q
import string


opis = """Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."""
print("[*] Fake data populate imported")

KONKURS_GLOBAL_IT = 1

KONKURSY_NUM = 37
PROJ_PER_KONKURS = [3, 5]
PESEL_NUM = 100

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


def add_votes():
    def randomString(stringLength=10):
        """Generate a random string of fixed length """
        letters = string.digits
        return ''.join(random.choice(letters) for i in range(stringLength))
    aktywne_projekty = models.Projekt.objects.all()

    aktywne_projekty_len = aktywne_projekty.count()
    c = 1
    for ap in aktywne_projekty:
        rand_votes_num = randint(0, 40)
        print(
        "[%s/%s | %.2f%%]" % (c, aktywne_projekty_len, 100 * c/aktywne_projekty_len),
        "[*] Adding ", rand_votes_num, "votes to", ap, "project")
        c = c + 1
        for i in range(0, rand_votes_num):
            print("\r\t progress: %.2f%%" % (100 * (i+1)/rand_votes_num), end="")
            obj = models.Glos(name=randomString(stringLength=11), projekt_id=ap)
            obj.save()
        print("")


def add_mock_pesel_api():
    obj = models.ApiMockData(
        dzielnica_id=get_rand_dzielnica(),
        pesel=str(randint(10000000000, 99999999999)))
    obj.save()


def add_konkurs(active):
    if active:
        from_ = randint(-30, -10)
        to = randint(10, 30)
    else:
        from_ = randint(-60, -40)
        to = randint(-30, -20)
    global KONKURS_GLOBAL_IT
    dzielnica_name = get_rand_dzielnica()
    konkurs = models.Konkurs(
        dogrywka=False,
        dzielnica_id=dzielnica_name,
        description=opis,
        date_start=timezone.now() + timedelta(days=from_),
        date_finish=timezone.now() + timedelta(days=to),
        name="Konkurs #%s - %s" % (KONKURS_GLOBAL_IT, dzielnica_name.name)
    )
    print("\t- added:", konkurs)
    konkurs.save()
    KONKURS_GLOBAL_IT = KONKURS_GLOBAL_IT + 1


def add_projekty():
    count = 0
    all_konkurs = models.Konkurs.objects.all()
    all_konkurs_count = models.Konkurs.objects.count()
    for i in range(0, all_konkurs_count):
        for j in range(0, randint(PROJ_PER_KONKURS[0], PROJ_PER_KONKURS[1])):
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
    for i in range(0, PESEL_NUM + 1):
        print("\rAdding PESEL %s/%s\t" % (i, PESEL_NUM), end="")
        add_mock_pesel_api()
    print("")
    add_votes()


print("Konkursy   :", KONKURSY_NUM)
print("Projekty   : od", PROJ_PER_KONKURS[0], "do", PROJ_PER_KONKURS[1])
print("PESEL num. :", PESEL_NUM)
input("\n\n<enter>")
print("\n\n")

populate()
