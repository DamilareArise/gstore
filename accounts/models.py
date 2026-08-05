from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


class Role(models.Model):
    ROLE_CHOICES = [
            ('ADMIN', 'Admin'),
            ('CUSTOMER', 'Customer'),
            ('VENDOR', 'Vendor'),
        ]
    name = models.CharField(max_length=50, unique=True, choices=ROLE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
# class UserRole(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_roles')
#     role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='user_roles')
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
    
#     class Meta:
#         unique_together = ('user', 'role')
    
#     def __str__(self):
#         return f"{self.user.username} - {self.role.name}"



class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]
    
    # ROLE_CHOICES = [
    #     ('Admin', 'Admin'),
    #     ('Customer', 'Customer'),
    #     ('Vendor', 'Vendor'),
    # ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    # role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='Customer')
    role = models.ManyToManyField(Role, related_name='user_profiles', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.username
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            profile = UserProfile.objects.create(user=instance)
            customer_role = Role.objects.get(name='CUSTOMER')
            profile.role.add(customer_role)