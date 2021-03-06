from django.conf.urls import url
#from home import views
from django.views.generic import TemplateView
from django.conf import settings
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

from home import views

urlpatterns = [
    url(r'^$', views.index, name='index'), 
    url(
        r'^favicon.ico$',
        RedirectView.as_view(
            url=staticfiles_storage.url('home/images/favicon_dev.ico'),
            permanent=False),
        name="favicon"
    )
]