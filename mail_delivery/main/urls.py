from django.conf.urls import url
from main import views


urlpatterns = [
    url(r'send/', views.call_email_distribution, name='send email'),
]