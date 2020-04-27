from django.db import models

class User(models.Model):
    user_name = models.CharField(max_length=100)
    user_age = models.IntegerField()
    user_country_code = models.CharField(max_length=2)

    def __str__(self):
        return self.user_name

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note_title = models.CharField(max_length=50)
    note_text = models.CharField(max_length=200)
    note_date = models.DateTimeField("published")    

    def __str__(self):
        return self.note_title