from django.db import models
from .validator import validate_file_extension
import datetime

# Create your models here.
def reviews_directory_path(instance, filename):
    return 'files/user_{0}/{1}'.format(instance.user.id, filename)

class Reviews(models.Model):
    item_set =  models.FileField( upload_to=reviews_directory_path, validators=[validate_file_extension])
    user_set =  models.FileField( upload_to=reviews_directory_path, validators=[validate_file_extension])
    testing_set = models.FileField( upload_to=reviews_directory_path, validators=[validate_file_extension])
    note = models.CharField(max_length=200, blank=True, null=True)
