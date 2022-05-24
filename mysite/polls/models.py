from django.db import models
# Create your models here.
class Detail(models.Model):
    def __str__(self):
        return self.user_name+", "+self.email_id
    
    user_name=models.CharField(max_length=20)
    email_id=models.EmailField(max_length=254)

