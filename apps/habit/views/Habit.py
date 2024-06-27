from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, \
    ListModelMixin

from apps.habit.models import Habit
from apps.habit.paginations import HabitPagination
from apps.habit.serliazers import HabitSerializer


class HabitViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, ListModelMixin,
                   GenericViewSet):
    """Представление модели привычки, которое включает в себя механизм CRUD"""

    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitPagination

    def get_queryset(self):
        """Пользователь может видеть только свои приятные привычки с признаком приятной привычки"""

        user = self.request.user
        if user.is_staff:
            return Habit.objects.all()
        else:
            return Habit.objects.filter(user=user, is_pleasant_habit=True, is_published=True)

    def perform_create(self, serializer):
        """При создании приятной привычки присваивается автор"""

        serializer.save(user=self.request.user)
