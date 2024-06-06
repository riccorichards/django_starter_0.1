from django.contrib import admin
# Import the admin module to register and manage models in the Django admin interface.

from django.urls import path, include
# Import path and include to define URL patterns and include other URL configurations.

from api.views import CreateUserView
# Import the CreateUserView from the api.views module to handle user registration.

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# Import views from the simplejwt package to handle token generation and refreshing for JWT authentication.

urlpatterns = [
    path('admin/', admin.site.urls),
    # Define a URL pattern for the Django admin interface.

    path("api/user/register/", CreateUserView.as_view(), name="register"),
    # Define a URL pattern for user registration, linking to the CreateUserView.

    path("api/token/", TokenObtainPairView.as_view(), name="get_token"),
    # Define a URL pattern for obtaining JWT tokens, linking to the TokenObtainPairView.

    path("api/token/refresh/", TokenRefreshView.as_view(), name="refresh"),
    # Define a URL pattern for refreshing JWT tokens, linking to the TokenRefreshView.

    path("api-auth/", include("rest_framework.urls")),
    # Include the default authentication URLs provided by the Django REST framework for login and logout.
]
