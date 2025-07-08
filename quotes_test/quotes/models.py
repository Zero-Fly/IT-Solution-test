from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Quote(models.Model):
    text = models.TextField(verbose_name="Quote text")
    source = models.CharField(max_length=200, verbose_name="Source")
    weight = models.PositiveIntegerField(verbose_name="Quote weight", default=1)
    views = models.PositiveIntegerField(default=0, verbose_name="Views")
    likes = models.PositiveIntegerField(default=0, verbose_name="Likes")
    dislikes = models.PositiveIntegerField(default=0, verbose_name="Dislikes")

    def clean(self):
        # max quantity check
        if Quote.objects.filter(source=self.source).count() >= 3:
            if not self.pk or Quote.objects.get(pk=self.pk).source != self.source:
                raise ValidationError(
                    f"Reached maximum quantity"
                )
        # empty text    
        if not self.text.strip():
            raise ValidationError("Empty quote text")
        #empty source
        if not self.source.strip():
            raise ValidationError("Empty quote source")
        

class Meta:
    verbose_name = "Quote"
    verbose_name_plural = "Quotes"
    constraints = [
        models.UniqueConstraint(
            fields=['text', 'source'],
            name='unique_quote_source'
        )
    ]