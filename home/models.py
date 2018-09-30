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

    keyword = models.CharField(max_length=200,null=True,blank=True)
    drawn_date = models.DateTimeField(blank=True, null=True)

    card_name = models.CharField(max_length=200,null=True,blank=True)
    card_text = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.language
        # if self.language:
        #     return "Language: " + self.language + " / Keyword: "+ self.keyword
        # return "Language: " + self.language

    def drawn(self):
        self.drawn_date = timezone.now()
        self.save()
