from django.db import models
from django.utils import timezone

# Create your models here.


class Role(models.Model):
    _physical = 'physical'
    _magical = 'magical'
    _damage_type = (
        (_physical, 'Physical'),
        (_magical, 'Magical')
    )
    _ranged = 'ranged'
    _melee = 'melee'
    _attack_type = (
        (_ranged, 'Ranged'),
        (_melee, 'Melee')
    )
    name = models.CharField(max_length=30, unique=True, db_index=True)
    damage = models.CharField(
        max_length=1,
        choices=_damage_type,
        default=_physical,
    )
    attack = models.CharField(
        max_length=1,
        choices=_attack_type,
        default=_melee
    )

    def __str__(self):
        return self.name


class Pantheon(models.Model):
    name = models.CharField(max_length=30, unique=True, db_index=True)
    date_release = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name


class God(models.Model):
    # TODO: set several fields as index
    name = models.CharField(max_length=60, unique=True, db_index=True)
    date_release = models.DateField(timezone.now)
    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE
    )
    pantheon = models.ForeignKey(
        Pantheon,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class Match(models.Model):
    _win = 'W'
    _loss = 'L'
    _results = (
        (_win, 'Win'),
        (_loss, 'Loss')
    )
    self = models.ForeignKey(God, related_name='self', db_index=True)
    opponent = models.ForeignKey(God, related_name='opponent', db_index=True)
    result = models.CharField(
        max_length=1,
        choices=_results,
        default=_win,
        db_index=True
    )
    date = models.DateTimeField(
        default=timezone.now
    )
    kills = models.IntegerField()
    deaths = models.IntegerField()
    notes = models.TextField()
