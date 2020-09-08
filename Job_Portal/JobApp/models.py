from django.db import models


class JobSeeker(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'))
    name = models.CharField(max_length=50, blank=False)
    email = models.EmailField()
    date_of_birth = models.DateTimeField(null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=False)
    address = models.CharField(max_length=100, null=True)
    contact = models.IntegerField(null=True)

    def __str__(self):
        return self.name


class Company(models.Model):
    TYPE_CHOICES = (
        ('Airlines', 'Airlines'),
        ('Automotive Sales, Support & Service', 'Automotive Sales, Support & Service'),
        ('Banks', 'Banks'),
        ('Call Center', 'Call Center'),
        ('Consumer Products', 'Consumer Products'),
        ('Designing / Printing', 'Designing / Printing'),
        ('E-business', 'E-business'),
        ('Education', 'Education'),
        ('Event Management', 'Event Management'),
        ('Finance', 'Finance'),
        ('Governmental Company', 'Governmental Company'),
        ('Health', 'Health'),
        ('Hotels', 'Hotels'),
        ('Insurance', 'Insurance'),
        ('Information Technology', 'Information Technology'),
        ('Import/Export', 'Import/Export'),
        ('ISP', 'ISP'),
        ('Media', 'Media'),
        ('NGO', 'NGO'),
        ('Real Estate', 'Real Estate'),
        ('Travel Agency', 'Travel Agency')
    )
    name = models.CharField(max_length=50, null=False)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES, null=False)
    address = models.CharField(max_length=50, null=False)
    contact = models.IntegerField(null=True)
    email = models.EmailField(null=True)
    description = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=50, null=False)
    company_name = models.ForeignKey(Company, on_delete=models.CASCADE, null=False)
    post_date = models.DateTimeField(auto_now_add=True)
    last_date = models.DateTimeField(null=False)

    def __str__(self):
        return self.title
