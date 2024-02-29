from django.contrib import admin
from django.urls import path
from mainApp.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('bolim/', bolim),
    path('kitob/', kitob,name='kitob'),
    path('yangi/', yangi_kitoblar),
    path('', LoginView.as_view(),name='login'),
    path('logaut/', LogoutView.as_view()),
    path('kitob/<int:id>/',kitob_ochir),
]
