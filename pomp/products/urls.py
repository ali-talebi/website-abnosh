from django.urls import path 
from .views import Total_product   , details_of_product , Text_original_page_views , newsletter 

app_name = "app1"
urlpatterns = [
    path("" , Total_product  , name = "Total_product" ) , 
    
    path("" , newsletter , name = "newsletter"  ) , 
    path("detail/<slug:slug>/<int:id>" , details_of_product , name="details_of_product" ) , 
    

    
]
