from django.db import models

# Create your models here.

class Text(models.Model):
    position = models.IntegerField
    text = models.CharField(max_length=200)
    Parent = models.ForeignKey('self', on_delete=models.CASCADE, related_name='+', null=True, default=None, blank=True)

    # function takes primary key of Text object, and should return number
    # i.e PK (3)
    # return value 1.1.1
    # core-idea: there is need for the function that counts the number of this child of the parent,
    # and then combine it with the number of parents
    def get_nesting_number():
        
        return