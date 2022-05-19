"""travex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework_simplejwt.views import TokenVerifyView, TokenRefreshView, TokenObtainPairView

from allauth.account.views import LogoutView

from travex.views import ActivateUserEmail, ResetPasswordView, eula

from place.views import GoogleLogin, CustomUserListCreateView, \
    CustomUserDetailView, CustomUserView, AppleLogin, check_version


urlpatterns = [
    path('admin/', admin.site.urls),
    path('check_version/', check_version),
    path('api/places/', include("place.urls", namespace="place")),
    path('api/achievements/', include("achievement.urls", namespace="achievement")),
    path('api/drf-auth/', include('rest_framework.urls')),
    path('eula/', eula),
    path('', include('social_django.urls', namespace='social')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    path('users/', CustomUserView.as_view({'post': 'create'})),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('auth/google/', GoogleLogin.as_view(), name='google_login'),
    path('auth/apple/', AppleLogin.as_view(), name="apple_login"),
    # gets all user profiles and create a new profile
    path("all-profiles/", CustomUserListCreateView.as_view(), name="all-profiles"),
    path("profile/<int:pk>", CustomUserDetailView.as_view(), name="profile"),
    path('auth/user/activate/<str:uid>/<str:token>/', ActivateUserEmail.as_view(), name='activate email'),
    path(settings.DJOSER.PASSWORD_RESET_CONFIRM_URL, ResetPasswordView.as_view()),

    # retrieves profile details of the currently logged in user
    # path('api/bookmarks/<pk>', BookmarkViewSet.as_view({'get': 'list', 'delete': 'destroy'})),
    # path('i18n/', include('django.conf.urls.i18n')),
    # path('activate/<uid>/<token>', ActivateUser.as_view({'get': 'activation'}), name='activation'),
    # path(r'activate/<uid>/<token>', UserActivationView.as_view()),
    # path('activate/<str:uid>/<str:token>/', UserActivationView.as_view()),
    # path(r'^auth/users/activate/<str:uid>/<str:token>/', UserActivationView.as_view()),
    # path("djoser_auth/", include("djoser.urls")),
    # path("djoser_auth/", include("djoser.urls.jwt")),
]

# urlpatterns += i18n_patterns(
#
# )

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
