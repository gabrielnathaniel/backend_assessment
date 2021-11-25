from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from contacts import views

from contacts.views import ContactViewSet, UserViewSet, api_root
from rest_framework import renderers

from rest_framework.routers import DefaultRouter

contact_list = ContactViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
contact_detail = ContactViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
contact_highlight = ContactViewSet.as_view({
    'get': 'highlight'
}, renderer_classes=[renderers.StaticHTMLRenderer])
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'contacts', views.ContactViewSet)
router.register(r'users', views.UserViewSet)

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls)),
]