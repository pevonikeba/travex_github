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
from allauth.account.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin


from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.views.static import serve
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenVerifyView, TokenRefreshView, TokenObtainPairView

from place.views import PlaceViewSet, GroupViewSet, ClimateViewSet, TypeOfTerrainViewSet, CategoryViewSet, \
    UserPlaceRelationView, TypeTransportViewSet, TypeCuisineViewSet, GoogleLogin, CustomUserListCreateView, \
    CustomUserDetailView, BookmarkViewSet, ActivateUserEmail, CustomUserView

router = SimpleRouter()

router.register(r'api/place_relation', UserPlaceRelationView)
router.register(r'api/categories', CategoryViewSet)

router.register(r'api/type_transport', TypeTransportViewSet)
router.register(r'api/type_cuisine', TypeCuisineViewSet)

router.register(r'api/places', PlaceViewSet)
router.register(r'api/groups', GroupViewSet)
router.register(r'api/bookmarks', BookmarkViewSet)

router.register(r'api/climates', ClimateViewSet)
router.register(r'api/terrains', TypeOfTerrainViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/drf-auth/', include('rest_framework.urls')),
    path('', include('social_django.urls', namespace='social')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

    path('users/', CustomUserView.as_view({'post': 'create'})),

    # path("djoser_auth/", include("djoser.urls")),
    # path("djoser_auth/", include("djoser.urls.jwt")),

    re_path(r'^auth/', include('djoser.urls.authtoken')),


    # path('', TemplateView.as_view(template_name="index.html")),
    path('accounts/', include('allauth.urls')),
    path('logout', LogoutView.as_view()),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('auth/google/', GoogleLogin.as_view(), name='google_login'),

    # gets all user profiles and create a new profile
    path("all-profiles/", CustomUserListCreateView.as_view(), name="all-profiles"),
    # retrieves profile details of the currently logged in user
    path("profile/<int:pk>", CustomUserDetailView.as_view(), name="profile"),

    # path('activate/<uid>/<token>', ActivateUser.as_view({'get': 'activation'}), name='activation'),
    # path(r'activate/<uid>/<token>', UserActivationView.as_view()),
    # path('activate/<str:uid>/<str:token>/', UserActivationView.as_view()),

    # path(r'^auth/users/activate/<str:uid>/<str:token>/', UserActivationView.as_view()),
    path('auth/user/activate/<str:uid>/<str:token>/', ActivateUserEmail.as_view(), name='activate email'),

    path('api/bookmarks/<pk>', BookmarkViewSet.as_view({'get': 'list', 'delete': 'destroy'})),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += router.urls
