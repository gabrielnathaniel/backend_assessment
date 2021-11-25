from contacts.models import Contact, ContactLabel, Label
from contacts.serializers import ContactSerializer
from contacts.serializers import UserSerializer
from contacts.permissions import IsOwnerOrReadOnly

from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework import permissions
from rest_framework import renderers
from rest_framework import viewsets
from rest_framework import permissions

from rest_framework.decorators import api_view
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.reverse import reverse

class ContactViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        contact = self.get_object()
        return Response(contact.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    # This viewset automatically provides `list` and `retrieve` actions.
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'contacts': reverse('contact-list', request=request, format=format)
    })