from django.urls import path
app_name = "products"
from . views import FoodCreateView,FoodListView,FoodUpdateView, FoodDeleteView,CleaningCreateView, CleaningListView,CleaningUpdateView,CleaningDeleteView,RequestFoodCreateView, RequestCleaningCreateView

urlpatterns = [
    path("createfood/",FoodCreateView.as_view(), name = "food_form"),
    path("listfood/", FoodListView.as_view(), name = "food_list"),
    path("updatefood/<uuid:uuid>/", FoodUpdateView.as_view(), name = "food_update"),
    path("deletefood/<uuid:uuid>/",FoodDeleteView.as_view(), name = "food_delete"),
    #urls cleaning
    path("createcleaning/",CleaningCreateView.as_view(), name = "cleaning_form"),
    path("listcleaning/",CleaningListView.as_view(), name = "cleaning_list"),
    path("updatecleaning/<uuid:uuid>/",CleaningUpdateView.as_view(), name = "cleaning_update"),
    path("deletecleaning/<uuid:uuid>/",CleaningDeleteView.as_view(), name = "cleaning_delete"),
    #urls request_food
    path("requestfood/",RequestFoodCreateView.as_view(),name="request_food"),
    #urls request_cleaning
    path("requestcleaning/",RequestCleaningCreateView.as_view(), name = "request_cleaning"),

]