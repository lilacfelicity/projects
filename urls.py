from django.contrib import admin
from django.urls import path
from django.conf import settings # new
from django.urls import path, include # new
from django.conf.urls.static import static # new
from . import views

urlpatterns = [
    # post views
    path('',views.main),
    path('single/'      ,views.show_post_list,{'slug':'single'}),
    path('album/'       ,views.show_post_list,{'slug':'album'}),
    path('videoclip/'   ,views.show_post_list,{'slug':'videoclip'}),
    path('group/'       ,views.show_post_list,{'slug':'group'}),
    path('article/'     ,views.show_post_list,{'slug':'article'}),
       
    path('single/<slug:slug>/'      ,views.show_post),
    path('album/<slug:slug>/'       ,views.show_post),
    path('videoclip/<slug:slug>/'  ,views.show_post),
    path('group/<slug:slug>/'      ,views.show_post),
    path('articles/<slug:slug>/'   ,views.show_post),
]

#urlpatterns = [
#    path('admin/', admin.site.urls),

#    path('', include('KPOP.urls')), # new]
#if settings.DEBUG: # new
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#    from .views import HomePageView

#urlpatterns = [
#    path('', HomePageView.as_view(), name='home'),
#]
