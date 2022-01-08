from django.urls import path
from .views import (AddUser, PredictValueView, FinalResultView )

urlpatterns = [
    path('addusers/', AddUser.as_view(), name='api_add_users'),
    path('predict/value/', PredictValueView.as_view(), name='api_predict_value'),
    path('predict/final/score/', FinalResultView.as_view(), name='api_predict_final_score'),
]