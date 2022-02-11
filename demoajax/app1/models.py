from django.db import models


class UserDetail(models.Model):
    full_name = models.CharField(max_length=100)
    email_id = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email_id
