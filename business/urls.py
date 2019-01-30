from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('business/', views.BusinessListView.as_view()),
    path('business/<int:pk>/', views.BusinessDetailsView.as_view()),
    path('service/', views.ServiceListView.as_view()),
    path('service/<int:pk>/', views.ServiceDetailsView.as_view()),

]
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)