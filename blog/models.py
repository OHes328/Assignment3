from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    # title이 제목이 되었으면 할 때
    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]