from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    single_photo = models.FileField(upload_to='images/')
    yil = models.SmallIntegerField()
    oy = models.CharField(max_length=10)
    def __str__(self):
        return self.title

class Photos(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    photo = models.FileField(upload_to='images/')
    def __str__(self):
        return self.article.title
