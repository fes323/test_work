from django.db import models
from django.db.models import Sum, Q, Count


class Room(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name


class ChairTypeEnum(models.TextChoices):
    BENCH = 'B', 'Bench chair'
    DINING = 'D', 'Dining chair'
    ARMCHAIR = 'A', 'Armchair'


class Chair(models.Model):
    stock_keeping_unit = models.CharField(max_length=200)
    type = models.CharField(max_length=1, choices=ChairTypeEnum.choices, null=False, blank=False)
    placed_at = models.ForeignKey(Room, models.SET_NULL, null=True, related_name='chairs')


class Table(models.Model):
    stock_keeping_unit = models.CharField(max_length=200)
    seats = models.PositiveSmallIntegerField(null=False, blank=False)
    placed_at = models.ForeignKey(Room, models.SET_NULL, null=True, related_name='tables')


def get_rooms_with_missing_seats(*chair_types: ChairTypeEnum) -> models.QuerySet:
    num_chairs = Count('chairs', filter=reduce(lambda q1, q2: q1 | q2, [Q(chairs__type=ct) for ct in chair_types]))
    num_seats = Sum('tables__seats')
    rooms = Room.objects.annotate(num_chairs=num_chairs).annotate(num_seats=num_seats).filter(num_chairs__gt=num_seats)
    return rooms