from django.db import models

# Create your models here.

class Registration(models.Model):
    user_first_name = models.CharField('First name',max_length=50)
    user_last_name = models.CharField('Last name',max_length=50)
    user_email = models.EmailField('Email')
    user_password = models.CharField('Password',max_length=50)
    user_date = models.DateTimeField(auto_now_add=True)
    user_mobile = models.PositiveIntegerField('Mobile Number')
    
    def __str__(self):
        return self.user_first_name+" "+self.user_last_name

class Quotes(models.Model):
    user_name = models.ForeignKey(Registration,on_delete=models.CASCADE,related_name='reg')
    Quote_image = models.ImageField('Quotes Image',upload_to="images")
    Quote_caption = models.CharField('Caption',max_length=300)
    Quote_date = models.DateTimeField(auto_now_add=True)