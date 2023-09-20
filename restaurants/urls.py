from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import RestaurantListView, RestaurantDetailView,\
    RestaurantCreateView, RestaurantUpdateView, RestaurantDeleteView,\
    MyPostView,home,bg
urlpatterns = [

    path("bg/",bg,name="bg"),
    path('', RestaurantListView.as_view(), name='home'),

    path('<slug:slug>/', RestaurantDetailView.as_view(), name='detail'),

 

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
