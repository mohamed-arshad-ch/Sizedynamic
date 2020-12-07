from django.urls import path
from .views import *
urlpatterns = [
    
    path('',Index.as_view(),name="index"),
    path('savepic/',Picture.as_view(),name="savepic"),
    path('login',Login.as_view(),name="login"),
    path('signup',Signup.as_view(),name="signup"),
    path('checkout',Checkout.as_view(),name="checkout")
    
]
