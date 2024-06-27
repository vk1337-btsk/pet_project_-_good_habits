from django.db import models

from config import settings

NULLABLE = {'blank': True, 'null': True}

FREQUENCY = [
    ('EVERY_DAY', 'раз в день'),
    ('EVERY OTHER DAY', 'через день'),
    ('EVERY WEEK', 'раз в неделю'),
]


class Habit(models.Model):
    """Модель привычки"""

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Создатель привычки',
                             **NULLABLE)
    place = models.CharField(max_length=200, verbose_name='Место')
    time = models.DateTimeField(verbose_name='Время выполнения')
    action = models.CharField(max_length=200, verbose_name='Действие')
    duration = models.PositiveIntegerField(default=120, verbose_name='Время на выполнение (сек)')
    is_published = models.BooleanField(default=True, verbose_name='Признак публичности привычки')
    is_pleasant_habit = models.BooleanField(default=True, verbose_name='Признак приятности привычки')

    def __str__(self):
        return f'Я буду {self.action} в {self.time} в {self.place}'

    class Meta:
        verbose_name = 'Добавить привычку'
        verbose_name_plural = 'Настройка привычки'


class GoodHabit(models.Model):
    """Модель полезной привычки"""

    pleasant_habit = models.ForeignKey(Habit, on_delete=models.CASCADE, verbose_name='Приятная привычка', **NULLABLE)
    reward = models.TextField(verbose_name='Вознаграждение за выполнение', **NULLABLE)
    frequency = models.CharField(max_length=100, default=FREQUENCY[0][0], choices=FREQUENCY,
                                 verbose_name='Периодичность')

    def __str__(self):
        return f'{self.pleasant_habit}'

    class Meta:
        verbose_name = 'Полезная привычка'
        verbose_name_plural = 'Полезные привычки'
        ordering = ('pleasant_habit',)
