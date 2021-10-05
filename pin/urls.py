from django.urls import path
from . import views 

urlpatterns = [
    # path('get/all/',views.results,name='add_pin'),
    path('lookup/',views.PincodeList.as_view(),name='pin-detail'),
    path('get/all/',views.GetPincodes.as_view(),name='get-pincodes')
]