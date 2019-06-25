from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    url('^$',views.login_page,name = 'form'),
    url('^$',views.welcome,name='welcome'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^new/profile$', views.new_profile, name='new-profile'),    
    url(r'^comment/(\d+)$',views.comment,name='comment'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)