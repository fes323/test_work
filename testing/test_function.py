import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "testing.settings")
django.setup()

from django.test import TestCase
from management.models import Room, Chair, Table, ChairTypeEnum, get_rooms_with_missing_seats


class RoomTestCase(TestCase):
    def setUp(self):
        # создаем три комнаты
        self.room1 = Room.objects.create(name='Room 1')
        self.room2 = Room.objects.create(name='Room 2')
        self.room3 = Room.objects.create(name='Room 3')

        # создаем три стула каждого типа и распределяем их по комнатам
        self.bench_chair1 = Chair.objects.create(stock_keeping_unit='1', type=ChairTypeEnum.BENCH, placed_at=self.room1)
        self.bench_chair2 = Chair.objects.create(stock_keeping_unit='2', type=ChairTypeEnum.BENCH, placed_at=self.room2)
        self.bench_chair3 = Chair.objects.create(stock_keeping_unit='3', type=ChairTypeEnum.BENCH, placed_at=self.room3)

        self.dining_chair1 = Chair.objects.create(stock_keeping_unit='4', type=ChairTypeEnum.DINING, placed_at=self.room1)
        self.dining_chair2 = Chair.objects.create(stock_keeping_unit='5', type=ChairTypeEnum.DINING, placed_at=self.room2)
        self.dining_chair3 = Chair.objects.create(stock_keeping_unit='6', type=ChairTypeEnum.DINING, placed_at=self.room3)

        self.armchair1 = Chair.objects.create(stock_keeping_unit='7', type=ChairTypeEnum.ARMCHAIR, placed_at=self.room1)
        self.armchair2 = Chair.objects.create(stock_keeping_unit='8', type=ChairTypeEnum.ARMCHAIR, placed_at=self.room2)
        self.armchair3 = Chair.objects.create(stock_keeping_unit='9', type=ChairTypeEnum.ARMCHAIR, placed_at=self.room3)

        # создаем два стола с количеством посадочных мест в каждой комнате
        self.table1 = Table.objects.create(stock_keeping_unit='10', seats=2, placed_at=self.room1)
        self.table2 = Table.objects.create(stock_keeping_unit='11', seats=4, placed_at=self.room2)
        self.table3 = Table.objects.create(stock_keeping_unit='12', seats=6, placed_at=self.room3)

    def test_get_rooms_with_missing_seats(self):
        # проверяем, что функция возвращает только комнату 3, так как в ней количество посадочных мест меньше,
        # чем количество стульев типов BENCH, DINING и ARMCHAIR, переданных в качестве аргументов
        self.assertQuerysetEqual(get_rooms_with_missing_seats(ChairTypeEnum.BENCH, ChairTypeEnum.DINING, ChairTypeEnum.ARMCHAIR), [self.room3], transform=lambda x: x)

