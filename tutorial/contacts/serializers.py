from rest_framework import fields, serializers
from contacts.models import Contact, ContactLabel, Label
from django.contrib.auth.models import User

class ContactSerializer(serializers.HyperlinkedModelSerializer):
    labels = serializers.HyperlinkedRelatedField(
        many = True,
        read_only = True,
        view_name='label_detail'
    )
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='contact-highlight', format='html')

    class Meta:
        model = Contact
        fields = ['url', 'id', 'highlight', 'owner',
                  'name', 'email', 'phone', 'notes', 'labels']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    contacts = serializers.HyperlinkedRelatedField(many=True, view_name='contact-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'contacts']