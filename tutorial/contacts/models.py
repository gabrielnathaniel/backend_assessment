from enum import auto
from django.db import models
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

class Contact(models.Model):
    id = models.IntegerField(auto, primary_key=True)
    name = models.CharField(max_length=100, blank=True, default='')
    email = models.CharField(max_length=100, blank=True, default='email@email.com')
    phone = models.CharField(max_length=100, blank=True, default='021123456789')
    notes = models.CharField(max_length=100, blank=True, default='empty')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['id']

class ContactLabel(models.Model):
    contact_id = models.ForeignKey('Contact', on_delete=models.CASCADE)
    label_id = models.ForeignKey('Label', on_delete=models.CASCADE)

    class Meta:
        ordering = ['contact_id']

class Label(models.Model):
    id = models.IntegerField(auto, primary_key=True)
    name = models.CharField(max_length=100, blank=True, default='teman-kantor')
    slug = models.CharField(max_length=100, blank=True, default='abcde')

    class Meta:
        ordering = ['id']

owner = models.ForeignKey('auth.User', related_name='contacts', on_delete=models.CASCADE)
highlighted = models.TextField()

def save(self, *args, **kwargs):
    # Use the `pygments` library to create a highlighted HTML
    # representation of the code snippet.
    lexer = get_lexer_by_name(self.language)
    linenos = 'table' if self.linenos else False
    options = {'title': self.title} if self.title else {}
    formatter = HtmlFormatter(style=self.style, linenos=linenos,
                              full=True, **options)
    self.highlighted = highlight(self.code, lexer, formatter)
    super(Contact, self).save(*args, **kwargs)