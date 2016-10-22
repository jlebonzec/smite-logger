import datetime

from django.db import models

# Create your models here.


class Role(models.Model):
    _physical = 'P'
    _magical = 'M'
    _damage_type = (
        (_physical, 'Physical'),
        (_magical, 'Magical')
    )
    name = models.CharField(max_length=30, unique=True)
    damage = models.CharField(
        max_length=1,
        choices=_damage_type,
        default=_physical,
    )
    # TODO: how to set name as primary index?


class Pantheon(models.Model):
    name = models.CharField(max_length=30, unique=True)
    date_release = models.DateField(default=datetime.date.today())


class God(models.Model):
    # TODO: set several fields as index
    name = models.CharField(max_length=60, unique=True)
    date_release = models.DateField(datetime.date.today())
    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE
    )
    pantheon = models.ForeignKey(
        Pantheon,
        on_delete=models.CASCADE
    )


class Match(models.Model):
    _win = 'W'
    _loss = 'L'
    _results = (
        (_win, 'Win'),
        (_loss, 'Loss')
    )
    self = models.ForeignKey(God, related_name='self')
    opponent = models.ForeignKey(God, related_name='opponent')
    result = models.CharField(
        max_length=1,
        choices=_results,
        default=_win
    )
    date = models.DateTimeField(
        default=datetime.datetime.now()
    )
    kills = models.IntegerField()
    deaths = models.IntegerField()
    notes = models.TextField()
