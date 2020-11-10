from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
# from django.conf.urls import patterns, include
from django.conf.urls.static import static
from .api import categori_list,LoginAdminAPI,category_detail,RegisterAPI,LoginAPI,UserAPI,Movie_list,Movie_detail,Profile_list,Profile_detail
from .recommned import recomend
urlpatterns = [
    path('cat/',categori_list),
    path('cat/<int:pk>',category_detail),
    path('movie/<int:pk>',Movie_list),
    path('movie_ID/<int:pk>',Movie_detail),
    path('auth/register/', RegisterAPI.as_view()),
    path('auth/login/',LoginAPI.as_view()),
    path('auth/loginAdmin/',LoginAdminAPI.as_view()),
    path('recommend/<int:UID>',recomend),
    path('auth/user/', UserAPI.as_view()),
    path('auth/profile/<int:pk>',Profile_list),
    path('auth/profile_ID/<int:pk>',Profile_detail)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL)