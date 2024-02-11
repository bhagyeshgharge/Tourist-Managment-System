from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.index),
    path('user_login',views.UserLogin),
    path('register',views.register),    
    path('user_log',views.User_logout),
    path('admin_login',views.admin_login),
    path('admin_register',views.admin_register),
    path('admin-index',views.Admin_index),
    path('add_package',views.add_package),
    path('package_details/<pid>',views.package),
    path('book_package/<tid>',views.book_package),
    path('my_booking',views.my_booking),
    path('contact',views.contact)
    


]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
