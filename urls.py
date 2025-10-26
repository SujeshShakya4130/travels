"""
URL configuration for adventures project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
# from users.routers.users_routers import urlpatterns as users_router
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.conf import settings
from django.conf.urls.static import static
from blog.routers.blog_routers import blog_router
from faqs.routers.faqs_routers import faqs_router
from users.routers.users_routers import users_router
from queries.routers.queries_routers import queries_router
from trip_reviews.routers.trip_reviews_routers import trip_reviews_router
from company.homepage.routers.homepage_routers import homepage_router
from company.team.routers.team_routers import team_router
from company.popup.routers.popup_routers import popup_router
from company.privacypolicy.routers.privacypolicy_routers import privacypolicy_router
from company.termsandconditions.routers.termsandconditions_routers import termsandconditions_router
from company.visaandinformation.routers.visaandinformation_routers import visaandinformation_router
from company.legaldocuments.routers.legaldocuments_routers import legaldocuments_router
from adventure.package.routers.package_routers import package_router
from adventure.activities.routers.activities_routers import activities_router
from adventure.collection.routers.collection_routers import collection_router
from adventure.destination.routers.destination_routers import destination_router
from booking.routers.booking_routers import booking_router

schema_view = get_schema_view(
    openapi.Info(
        title="ADVENTURES API",
        default_version='v1',
        description="Trekking - Backend",
        contact=openapi.Contact(email='sujeshshakya4130@gmail.com'),
        terms_of_service="https://policies.google.com/terms?hl=en",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include(blog_router.urls)),
    path('faq/', include(faqs_router.urls)),
    path('user/', include(users_router.urls)),
    path('queries/', include(queries_router.urls)),
    path('reviews/', include(trip_reviews_router.urls)),
    path('homepage/', include(homepage_router.urls)),
    path('team/', include(team_router.urls)),
    path('popup/', include(popup_router.urls)),
    path('privacypolicy/', include(privacypolicy_router.urls)),
    path('termsandconditions/', include(termsandconditions_router.urls)),
    path('visaandinformation/', include(visaandinformation_router.urls)),
    path('legaldocuments/', include(legaldocuments_router.urls)),
    path('package/', include(package_router.urls)),
    path('activities/', include(activities_router.urls)),
    path('collection/', include(collection_router.urls)),
    path('destination/', include(destination_router.urls)),
    path('booking/', include(booking_router.urls)),

    # Swagger UI:
    path('', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
                                       cache_timeout=0), name='schema-redoc'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
