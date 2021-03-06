from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.contrib.auth.views import (
    login,
    logout_then_login,
    password_reset,
    password_reset_complete,
    password_reset_confirm,
)

from wagtail.wagtailadmin import urls as wagtailadmin_urls
from wagtail.wagtaildocs import urls as wagtaildocs_urls
from wagtail.wagtailcore import urls as wagtail_urls

from rest_framework.routers import DefaultRouter

from core import urls as core_urls
from events.views import (
    events,
    users,
    locations,
    speakers,
    dues,
)
from blog.views import BlogIndexView
from api.viewsets import (
    EventViewSet,
    EventLocationViewSet,
    AttendanceViewSet,
    SpeakerViewSet,
    SponsorViewSet,
    UserProfileViewSet
)


router = DefaultRouter()
router.register(r'events', EventViewSet)
router.register(r'locations', EventLocationViewSet)
router.register(r'attendees', AttendanceViewSet)
router.register(r'sponsors', SponsorViewSet)
router.register(r'speakers', SpeakerViewSet)
router.register(r'users', UserProfileViewSet)

# General
urlpatterns = [
    url(r'^', include(core_urls)),
    url(r'^django-admin/', admin.site.urls, name='django-admin'),
]

# Wagtail
urlpatterns += [
    url(r'^admin/', include(wagtailadmin_urls)),
    url(r'^documents/', include(wagtaildocs_urls)),
    url(r'^pages/', include(wagtail_urls)),
]

# Members
urlpatterns += [
    url(r'^accounts/', include('allauth.urls')),
    url(r'^member/profile/(?P<user_id>[\w.-_@]+)/$', users.detail_view, name='profile'),
    url(r'^member/edit/(?P<user_id>[\w.-_@]+)/$', users.update_view, name='profile-edit'),
    url(r'^member/list/$', users.list_view, name='member-list'),
    url(r'^account/settings/', TemplateView.as_view(
        template_name='users/settings.html'),
        name='user-settings'),
]

# Events
urlpatterns += [
    url(r'^events/$', events.dashboard_view, name='event-dashboard'),
    url(r'^events/cubs/$', TemplateView.as_view(
        template_name='events/cubs.html'),
        name='cubs-tickets'
    ),
    url(r'^events/list/$', events.list_view, name='event-list'),
    url(r'^events/create/$', events.create_view, name='event-create'),
    url(
        r'^events/(?P<slug>[-\w]+)/$',
         events.detail_view,
         name='event-detail'
    ),
    url(
        r'^events/(?P<slug>[-\w]+)/edit/$',
         events.edit_view,
         name='event-edit'
    ),
    url(r'^locations/create/$', locations.create_view, name='location-create'),
    url(r'^speaker/(?P<slug>[-\w]+)/$', speakers.detail_view, name='speaker-detail'),
    url(r'^dues/$', dues.pay_dues, name='dues'),
    url(r'^(?P<slug>[-\w]+)/rsvp/$', events.rsvp_view, name='rsvp'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
    url(r'^pages/$', BlogIndexView.as_view(), name='blog'),
]

# API
urlpatterns += [
    url(r'^api/', include(router.urls, namespace='api')),
]
