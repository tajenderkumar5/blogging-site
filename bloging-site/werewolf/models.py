from django.conf import settings 
from django.db import models



User = settings.AUTH_USER_MODEL
# Create your models here.
class werewolf(models.Model):
  user = models.ForeignKey(User , default=1 , null=True , on_delete = models.SET_NULL)
  title = models.CharField(max_length=120)
  slug = models.SlugField(unique=True)
  content = models.TextField(null=True,blank=True)

  def get_absolute_url(self):
          return f"/blog/{self.slug}"

  def get_edit_url(self):
          return f"{self. get_absolute_url}/edit"
  
  def get_delete_url(self):
          return f"{self. get_absolute_url}/delete"