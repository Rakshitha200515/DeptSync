from django.urls import path
from .views import DeptView, resourceRequests,login_view,makeObjections

urlpatterns = [
    path('onGoingPrj/', DeptView, name='file-upload'),
    path('resReq/' , resourceRequests),
    path('login/' , login_view),
    path('objt/',makeObjections)
]
