from datetime import date

from logger.models import (
    Pantheon,
    Role,
    God,
)

pantheon_syntax = ('name', 'date_release')
pantheons = (
    ('Greek', date.today()),
    ('Roman', date.today()),
    ('Chinese', date.today()),
    ('Norse', date.today()),
    ('Hindu', date.today()),
    ('Egyptian', date.today()),
    ('Mayan', date.today()),
    ('Japanese', date.today()),
)

role_syntax = ('name', 'damage', 'attack')
roles = (
    ('Hunter', 'P', 'R'),
    ('Assassin', 'P', 'M'),
    ('Warrior', 'P', 'M'),
    ('Mage', 'M', 'R'),
    ('Guardian', 'M', 'M'),
)

god_syntax = ('name', 'role', 'pantheon', 'date_release')
gods = (
    ("Agni",            'Mage',     'Hindu',    date(2012, 5, 31)),
    ("Anubis",          'Mage',     'Egyptian', date(2012, 5, 31)),
    ("Arachne",         'Assassin', 'Greek',    date(2012, 5, 31)),
    ("Artemis",         'Hunter',   'Greek',    date(2012, 5, 31)),
    ("Bastet",          'Assassin', 'Hindu',    date(2012, 5, 31)),
    ("Hades",           'Mage',     'Greek',    date(2012, 5, 31)),
    ("He Bo",           'Mage',     'Chinese',  date(2012, 5, 31)),
    ("Hel",             'Mage',     'Norse',    date(2012, 5, 31)),
    ("Hun Batz",        'Assassin', 'Mayan',    date(2012, 5, 31)),
    ("Kali",            'Assassin', 'Hindu',    date(2012, 5, 31)),
    ("Kukulkan",        'Mage',     'Mayan',    date(2012, 5, 31)),
    ("Odin",            'Warrior',  'Norse',    date(2012, 5, 31)),
    ("Ra",              'Mage',     'Egyptian', date(2012, 5, 31)),
    ("Sobek",           'Guardian', 'Egyptian', date(2012, 5, 31)),
    ("Vamana",          'Warrior',  'Hindu',    date(2012, 5, 31)),
    ("Ymir",            'Guardian', 'Norse',    date(2012, 5, 31)),
    ("Zeus",            'Mage',     'Greek',    date(2012, 5, 31)),
    ("Guan Yu",         'Warrior',  'Chinese',  date(2012, 6, 29)),
    ("Bakasura",        'Assassin', 'Hindu',    date(2012, 7, 20)),
    ("Anhur",           'Hunter',   'Egyptian', date(2012, 8, 3)),
    ("Cupid",           'Hunter',   'Roman',    date(2012, 8, 17)),
    ("Thor",            'Assassin', 'Norse',    date(2012, 9, 7)),
    ("Ares",            'Guardian', 'Greek',    date(2012, 10, 4)),
    ("Freya",           'Mage',     'Norse',    date(2012, 10, 18)),
    ("Loki",            'Assassin', 'Norse',    date(2012, 11, 2)),
    ("Bacchus",         'Guardian', 'Roman',    date(2012, 11, 19)),
    ("Xbalanque",       'Hunter',   'Mayan',    date(2012, 12, 21)),
    ("Hercules",        'Warrior',  'Roman',    date(2013, 1, 13)),
    ("Vulcan",          'Mage',     'Roman',    date(2013, 1, 31)),
    ("Neith",           'Hunter',   'Egyptian', date(2013, 2, 13)),
    ("Poseidon",        'Mage',     'Greek',    date(2013, 2, 28)),
    ("Aphrodite",       'Mage',     'Greek',    date(2013, 3, 13)),
    ("Apollo",          'Hunter',   'Greek',    date(2013, 3, 28)),
    ("Ne Zha",          'Assassin', 'Chinese',  date(2013, 4, 17)),
    ("Fenrir",          'Assassin', 'Norse',    date(2013, 5, 1)),
    ("Isis",            'Mage',     'Egyptian', date(2013, 5, 15)),
    ("Athena",          'Guardian', 'Greek',    date(2013, 6, 5)),
    ("Chronos",         'Mage',     'Greek',    date(2013, 7, 10)),
    ("Chang'e",         'Mage',     'Chinese',  date(2013, 7, 24)),
    ("Tyr",             'Warrior',  'Norse',    date(2013, 8, 7)),
    ("Zhong Kui",       'Mage',     'Chinese',  date(2013, 8, 28)),
    ("Thanatos",        'Assassin', 'Greek',    date(2013, 9, 18)),
    ("Mercury",         'Assassin', 'Roman',    date(2013, 10, 2)),
    ("Sun Wukong",      'Warrior',  'Chinese',  date(2013, 10, 23)),
    ("Ah Muzen Cab",    'Hunter',   'Mayan',    date(2013, 11, 7)),
    ("Nu Wa",           'Mage',     'Chinese',  date(2013, 12, 5)),
    ("Chaac",           'Warrior',  'Mayan',    date(2013, 12, 18)),
    ("Geb",             'Guardian', 'Egyptian', date(2014, 1, 16)),
    ("Nemesis",         'Assassin', 'Greek',    date(2014, 2, 6)),
    ("Scylla",          'Mage',     'Greek',    date(2014, 3, 5)),
    ("Ullr",            'Hunter',   'Norse',    date(2014, 3, 19)),
    ("Kumbhakarna",     'Guardian', 'Hindu',    date(2014, 4, 16)),
    ("Osiris",          'Warrior',  'Egyptian', date(2014, 5, 6)),
    ("Janus",           'Mage',     'Roman',    date(2014, 5, 28)),
    ("Rama",            'Hunter',   'Hindu',    date(2014, 6, 24)),
    ("Serqet",          'Assassin', 'Egyptian', date(2014, 7, 15)),
    ("Cabrakan",        'Guardian', 'Mayan',    date(2014, 8, 19)),
    ("Sylvanus",        'Guardian', 'Roman',    date(2014, 10, 1)),
    ("Nox",             'Mage',     'Roman',    date(2014, 10, 29)),
    ("Ao Kuang",        'Mage',     'Chinese',  date(2014, 11, 19)),
    ("Awilix",          'Assassin', 'Mayan',    date(2014, 12, 17)),
    ("Hou Yi",          'Hunter',   'Chinese',  date(2015, 1, 14)),
    ("Bellona",         'Warrior',  'Roman',    date(2015, 2, 25)),
    ("Medusa",          'Hunter',   'Greek',    date(2015, 4, 1)),
    ("Ah Puch",         'Mage',     'Mayan',    date(2015, 4, 28)),
    ("Ratatoskr",       'Assassin', 'Norse',    date(2015, 6, 2)),
    ("Ravana",          'Warrior',  'Hindu',    date(2015, 6, 30)),
    ("Khepri",          'Guardian', 'Egyptian', date(2015, 8, 4)),
    ("Xing Tian",       'Guardian', 'Chinese',  date(2015, 9, 1)),
    ("Sol",             'Mage',     'Norse',    date(2015, 10, 6)),
    ("Chiron",          'Hunter',   'Greek',    date(2015, 11, 17)),
    ("Amaterasu",       'Warrior',  'Japanese', date(2016, 1, 12)),
    ("Raijin",          'Mage',     'Japanese', date(2016, 2, 16)),
    ("Skadi",           'Hunter',   'Norse',    date(2016, 3, 15)),
    ("Jing Wei",        'Hunter',   'Chinese',  date(2016, 4, 12)),
    ("Susano",          'Assassin', 'Japanese', date(2016, 5, 10)),
    ("Fafnir",          'Guardian', 'Norse',    date(2016, 6, 7)),
    ("Erlang Shen",     'Warrior',  'Chinese',  date(2016, 7, 6)),
    ("Terra",           'Guardian', 'Roman',    date(2016, 8, 2)),
    ("Izanami",         'Hunter',   'Japanese', date(2016, 8, 30)),
    ("Camazotz",        'Assassin', 'Mayan',    date(2016, 10, 11)),

)


def populate():
    for pantheon in pantheons:
        Pantheon(**dict(zip(pantheon_syntax, pantheon))).save()

    for role in roles:
        Role(**dict(zip(role_syntax, role))).save()

    for god in gods:
        d = dict(zip(god_syntax, god))
        d['pantheon'] = Pantheon.objects.all().filter(name__iexact=d['pantheon'])[0]
        d['role'] = Role.objects.all().filter(name__iexact=d['role'])[0]
        God(**d).save()
