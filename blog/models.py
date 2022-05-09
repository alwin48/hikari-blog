from django.db import models
from django.urls import reverse

# from django.contrib.auth.models import AbstractUser

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to='upload/')

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# class User(AbstractUser):
#     pass

class BlogPost(models.Model):
    """Model representing a Blog Post"""
    title = models.CharField(max_length=256)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=4096*8, help_text='Enter text for blog')
    date_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='upload/')
    likes = models.PositiveBigIntegerField(default=0)

    def __str__(self) -> str:
        return self.title

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this blog_post."""
        # return reverse('book-detail', args=[str(self.id)])
        return reverse("post-detail", kwargs={"pk": self.pk})
    
