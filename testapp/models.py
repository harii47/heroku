from django.db import models


#  This is a User Details Model

class Blood_Donner_Model(models.Model):
    Name = models.CharField(max_length=30)
    Email = models.EmailField(max_length=50)
    Mobile = models.IntegerField()
    Address = models.CharField(max_length=50)
    Blood_Group = models.CharField(max_length=10)
    Last_Donation_Date = models.DateField(default=False)
    Date_O_Birth = models.DateTimeField()


class Feedback_Table(models.Model):
    Name = models.CharField(max_length=30)
    Rating = models.IntegerField()
    Feedback = models.CharField(max_length=200)


class Suggestion_Table(models.Model):
    name = models.CharField(max_length=30)
    suggestion_name = models.CharField(max_length=200)


class Problem_Table(models.Model):
    problem_name = models.CharField(max_length=100)
    Moblie = models.ForeignKey(Blood_Donner_Model,on_delete=models.CASCADE)


class Updates_Table(models.Model):
    Next_Camp_Address = models.CharField(max_length=50)
    Camp_Date = models.DateField()
    Timing_from = models.TimeField()
