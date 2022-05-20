from django.db import models


# from django.contrib.auth.models import User

class Teacher(models.Model):
    language_choices = (
        ("AJ", "Anglicky jazyk"),
        ("NJ", "Nemecky jazyk"),
        ("IT", "Italsky jazyk"),
        ("RJ", "Rusky jazyk"),
        ("FJ", "Francouzsky jazyk"),
        ("SJ", "Spanelsky jazyk"),
    )
    location_choices = (
        ("01", "Praha"),
        ("02", "Stredocesky kraj"),
        ("03", "Jihocesky kraj"),
        ("04", "Plzensky kraj"),
        ("05", "Karlovarsky kraj"),
        ("06", "Ustecky kraj"),
        ("07", "Liberecky kraj"),
        ("08", "Kralovehradecky kraj"),
        ("09", "Pardubicky kraj"),
        ("10", "Vysocina"),
        ("11", "Jihomorovsky kraj"),
        ("12", "Zlinsky kraj"),
        ("13", "Olomoucky kraj"),
        ("14", "Moravskoslezsky kraj"),
    )
    name = models.CharField(max_length=50)
    language = models.CharField(max_length=50, choices=language_choices)
    location = models.CharField(max_length=50, choices=location_choices, null=True, blank=True)
    price = models.IntegerField()
    level = models.CharField(max_length=50, null=True, blank=True)
    about_me = models.CharField(max_length=250)
    # location = models.CharField(max_length=10)
    # image = models.ImageField(upload_to="")
    # gender = models.CharField(max_length=10)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Location(models.Model):
    region = models.CharField(max_length=100)
    city = models.CharField(max_length=60)
