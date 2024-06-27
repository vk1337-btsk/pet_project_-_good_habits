from django.contrib import admin

from apps.habit.models import Habit, GoodHabit


@admin.register(Habit)
class HabitAdmin(admin.ModelAdmin):
    """Админ панель отображение модели Привычки"""
    list_display = ('user', 'place', 'time', 'action', 'duration', 'is_published')
    search_fields = ('user',)


@admin.register(GoodHabit)
class GoodHabitAdmin(admin.ModelAdmin):
    """Админ панель отображение модели Полезной привычки"""
    list_display = ('pleasant_habit', 'reward', 'frequency')
    search_fields = ('pleasant_habit',)
