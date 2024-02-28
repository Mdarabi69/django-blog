from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=300, db_index=True)
    body = models.TextField()
    author = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now_add=True)
    pic = models.ImageField(upload_to='image/%y/%m/%d/')

    def __str__(self) -> str:
        return self.title