from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [

    path('', views.homepage, name='homepage'),
    path('categories_/', views.categories_, name='categories_'),
    path('category_/<int:category_id>', views.category_, name='category_'),
    path('ebooks_/', views.ebooks_, name='ebooks_'),
    path('ebook_/<int:ebook_id>', views.ebook_, name='ebook_'),
    path('ebook_/<int:ebook_id>/comment_', views.comment, name='comment_'),
    path('login_', views.login_, name='login_'),
    path('logout', views.logout, name='logout'),
    path('signup_', views.signup_, name='signup_')
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
