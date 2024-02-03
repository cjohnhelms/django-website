from django.db import models

class Experience(models.Model):
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.company
    
class Education(models.Model):
    university = models.CharField(max_length=100)
    college = models.CharField(max_length=100)
    degree_type = models.CharField(max_length=50)
    degree_field = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.university
    
class Certification(models.Model):
    institution = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    date_achieved = models.DateField()

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name