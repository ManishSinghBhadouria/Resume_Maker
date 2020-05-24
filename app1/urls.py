from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views




urlpatterns = [
    path('resume',views.resume,name='resume'),
    path('demo',views.demo,name='demo'),
    path('',views.home,name='home'),
    path('signin',views.signin,name='signin'),
    path('signup',views.signup,name='signup'),
    path('signout',views.signout,name='signout'),   
    path('view_resume',views.view_resume,name='view_resume'),
    path('addski',views.addski,name='addski'), 
    path('addlan',views.addlan,name='addlan'), 
    path('addedu',views.addedu,name='addedu'), 
    path('addpro',views.addpro,name='addpro'), 
    

    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
