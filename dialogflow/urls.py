from django.conf.urls import url
from . import views

urlpatterns = [
    #/main/

    url(r'^keyboard/',views.keyboard),
    url(r'^message',views.message),	
]

