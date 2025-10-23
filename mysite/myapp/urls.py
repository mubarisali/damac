from django.urls import path
from .views import home, island, riverside, safagate, district

urlpatterns = [
    path('', home, name='home'),
    
    path('island/', island, name='island'),
    path('riverside/', riverside, name='riverside'),
    path('safagate/', safagate, name='safagate'),
    path('district/', district, name='district'),
    
]
