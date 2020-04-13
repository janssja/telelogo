# from classroom.views import classroom
from django.contrib import admin
# from django.contrib.auth import views as auth_views
from django.urls import include, path

from telelogo.users.views import user_detail_view, user_redirect_view, user_update_view

app_name = "users"

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('classroom.urls')),
    # path('accounts/signup/', classroom.SignUpView.as_view(), name='signup'),
    # path('accounts/login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<str:username>/", view=user_detail_view, name="detail"),
]
