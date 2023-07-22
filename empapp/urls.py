from django.urls import path
from empapp import views
urlpatterns = [
   path('',views.dashboard),
   path('empforms',views.empdata),
]