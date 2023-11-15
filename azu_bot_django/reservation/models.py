from django.db import models

from azu_bot_django.settings import MAX_CHAR_LENGHT
from cafe.models import Cafe
from menu.models import Set


class Reservation(models.Model):
    cafe = models.ForeignKey(
        Cafe,
        on_delete=models.CASCADE,
        related_name='reservations',
        verbose_name='В кафе'
    )
    date = models.DateField(
        'Дата бронирования'
    )
    name = models.CharField(
        'Имя клиента',
        max_length=MAX_CHAR_LENGHT
    )
    number = models.CharField(
        'Номер телефона клиента',
        max_length=MAX_CHAR_LENGHT
    )
    status = models.CharField(
        max_length=20,
        choices=[
            ('booked', 'Забронировано'),
            ('cancelled', 'Отменено')
        ],
        default=None
    )
    sets_and_quantities = models.ManyToManyField(
        'OrderSets',
        related_name='sets_and_qtys_booking'
    )

    class Meta:
        verbose_name = 'Бронь'
        verbose_name_plural = 'Брони'
        ordering = ('date',)

    def __str__(self):
        return f'В кафе {self.cafe}, для {self.name} на {self.date}'


class OrderSets(models.Model):
    reservation = models.ForeignKey(
        Reservation,
        on_delete=models.CASCADE,
        related_name='order_sets',
        default=None
    )
    sets = models.ForeignKey(
        Set,
        on_delete=models.CASCADE,
        related_name='order_sets'
    )
    quantity = models.IntegerField(
        'Количество сета'
    )

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ {self.sets} в количестве {self.quantity}'


class SimpleTableReservation(models.Model):
    simple_table = models.ForeignKey(
        'tables.SimpleTable',
        on_delete=models.CASCADE,
        related_name='reservations_simple_table',
        verbose_name='Забронированный простой стол'
    )
    reservation = models.ForeignKey(
        Reservation,
        on_delete=models.CASCADE,
        related_name='simple_tables',
        verbose_name='Бронь'
    )
    quantity = models.IntegerField(
        'Количество мест'
    )


class BarTableReservation(models.Model):
    bar_table = models.ForeignKey(
        'tables.BarTable',
        on_delete=models.CASCADE,
        related_name='reservations_bar_table',
        verbose_name='Забронированный барный стол'
    )
    reservation = models.ForeignKey(
        Reservation,
        on_delete=models.CASCADE,
        related_name='bar_tables',
        verbose_name='Бронь'
    )
    quantity = models.IntegerField(
        'Количество мест'
    )
