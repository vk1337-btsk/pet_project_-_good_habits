from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.habit.apps import HabitConfig
from apps.habit.views.GoodHabit import GoodHabitCreateAPIView, GoodHabitListAPIView, GoodHabitRetrieveAPIView, \
    GoodHabitUpdateAPIView, GoodHabitDestroyAPIView
from apps.habit.views.Habit import HabitViewSet

app_name = HabitConfig.name

router = DefaultRouter()
router.register(r'habits', HabitViewSet, basename='habits')

urlpatterns = [

    # GoodHabit
    path('good_habits/create/', GoodHabitCreateAPIView.as_view(), name='good_habit_create'),
    path('good_habits/', GoodHabitListAPIView.as_view(), name='good_habit_list'),
    path('good_habits/<int:pk>/', GoodHabitRetrieveAPIView.as_view(), name='good_habit_retrieve'),
    path('good_habits/update/<int:pk>/', GoodHabitUpdateAPIView.as_view(), name='good_habit_update'),
    path('good_habits/delete/<int:pk>/', GoodHabitDestroyAPIView.as_view(), name='good_habit_delete'),

]

urlpatterns += router.urls
