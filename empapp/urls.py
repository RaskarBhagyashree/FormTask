from django.urls import path
from empapp import views
urlpatterns = [
   path('user-form',views.dashboard),
   path('empforms',views.empdata),
]