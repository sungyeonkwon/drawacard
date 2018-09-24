from django.db import models
from django.utils import timezone

# Create your models here.

class Card(models.Model):

    LANG_CHOICES = [
        ('ko', 'Korean'),
        ('ja', 'Japanese'),
        ('zhs', 'Chinese'),
    ]

    # card = models.ForeignKey(Card, on_delete=models.CASCADE)
    language = models.CharField(
        max_length=10,
        choices=LANG_CHOICES,
        default='ko',
    )

    keyword = models.CharField(max_length=200,null=True,blank=True,)

    drawn_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.language

    def drawn(self):
        self.drawn_date = timezone.now()
        self.save()
