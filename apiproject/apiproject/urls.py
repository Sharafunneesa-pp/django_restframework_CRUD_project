"""
URL configuration for apiproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from api import views
from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from myapp import views as myapp_views
from rest_framework.authtoken.views import ObtainAuthToken
from webapp import views as web_views


router=DefaultRouter()
router.register("categories",views.CategoriesView,basename="categories")
# for u in router.urls:
#     print(u)
router.register("users",views.UsersView,basename="users")
router.register("api/v2/users",myapp_views.RegistrationView,basename="accounts")
router.register("api/v2/categories",myapp_views.CategoriesView,basename="categories")
router.register("api/v2/vehicles",myapp_views.VehicleView,basename="vehicles")
router.register("api/v2/wishlist",myapp_views.WishListView,basename="wishlist")


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/vehicles/",views.VehicleView.as_view()),
    path("api/vehicles/<int:pk>/",views.VehicleDetailsView.as_view()),
    path("api/v2/token/",ObtainAuthToken.as_view()),
    path("register",web_views.RegistrationView.as_view(),name="register"),
    path("login",web_views.SigninView.as_view(),name="signin"),
    path("home",web_views.IndexView.as_view(),name="home"),


]+router.urls
