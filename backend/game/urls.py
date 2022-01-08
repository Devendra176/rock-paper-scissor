from django.urls import path,include
from .views import (GetFrontPage)

urlpatterns = [
    path('frontend/', GetFrontPage.as_view()),
    path('game/',include('game.api.urls'))
]