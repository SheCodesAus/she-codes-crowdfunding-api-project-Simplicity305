from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()
# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    goal = models.IntegerField()
    image = models.URLField()
    is_open = models.BooleanField()
    date_created = models.DateTimeField()#(auto_now_add=True) - 
            # NOTE check if auto now should be used. Updated Thinkific slide shows empty brackets
    # owner = models.CharField(max_length=200) - code replaced by below in users setup??
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner_projects')
    
    
class Pledge(models.Model):
    amount = models.IntegerField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
          'Project',
          on_delete=models.CASCADE,
          related_name='pledges'
    )
#  Is there a preference to display code a certain way? eg one line vs multiple lines?

    # supporter = models.CharField(max_length=200) - removed as users setup only shows the below code for supporter
 
    supporter = models.ForeignKey(
    User,
    on_delete=models.CASCADE,
    related_name='supporter_pledges')