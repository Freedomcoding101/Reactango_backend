from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    username = models.CharField(max_length=255, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, default="/placeholder.png")
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return self.name

class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="projects")  # Tied to a user
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(blank=True, null=True)
    technologies = models.CharField(max_length=255, blank=True)  # List of tech used (comma-separated or JSON)
    project_url = models.URLField(blank=True, null=True)  # Link to live project
    repo_url = models.URLField(blank=True, null=True)  # Link to GitHub repo
    created_at = models.DateTimeField(auto_now_add=True)
    _id = models.AutoField(primary_key=True, editable=False)

    def __str__(self):
        return f"{self.title} ({self.user.username})"
