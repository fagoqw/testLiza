from django.db import models


class Comic(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True)
    status = models.CharField(max_length=20, choices=[('draft', 'Черновик'), ('published', 'Опубликовано')])


class Panel(models.Model):
    comic = models.ForeignKey('Comic', on_delete=models.CASCADE)
    order = models.IntegerField()
    image = models.ImageField(upload_to='comics/images')
    text_elements = models.JSONField(default=[])


