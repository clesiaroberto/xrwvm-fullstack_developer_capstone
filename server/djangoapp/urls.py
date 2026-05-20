# Uncomment the imports before you add the code
# from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from djangoapp import views

app_name = 'djangoapp'
urlpatterns = [
    path(route='get_cars', view=views.get_cars, name ='getcars'),
    path(route='get_dealers', view=views.get_dealerships, name='get_dealers'),
    path(route='add_review', view=views.add_review, name='add_review'),
    path('get_dealer_details/<int:dealer_id>/', views.get_dealer_details, name='get_dealer_details'),
    path('get_dealer_reviews/<int:dealer_id>/', views.get_dealer_reviews, name='get_dealer_reviews'),
    path('get_dealers/<str:state>/', views.get_dealerships, name='get_dealers_by_state'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
