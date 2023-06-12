from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name + " | " + self.password + " | " + self.major + " | " + self.status


class data(models.Model):
    studentId = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    iq = models.CharField(max_length=100)
    interestOutsideInformatic = models.CharField(max_length=100)
    interestOutsideInformatic_2 = models.CharField(max_length=100)
    interestOutsideInformatic_3 = models.CharField(max_length=100)
    interestOutsideInformatic_4 = models.CharField(max_length=100)
    interestInsideInformatic = models.CharField(max_length=100)
    interestInsideInformatic_2 = models.CharField(max_length=100)
    interestInsideInformatic_3 = models.CharField(max_length=100)
    interestInsideInformatic_4 = models.CharField(max_length=100)
    hobby = models.CharField(max_length=100)
    hobby_2 = models.CharField(max_length=100)
    hobby_3 = models.CharField(max_length=100)
    hobby_4 = models.CharField(max_length=100)
    hobby_5 = models.CharField(max_length=100)
    hobby_6 = models.CharField(max_length=100)
    hobby_7 = models.CharField(max_length=100)
    hobby_8 = models.CharField(max_length=100)
    hobby_9 = models.CharField(max_length=100)
    juniorNetworkAdministrator = models.CharField(max_length=100)
    juniorWebProgramer = models.CharField(max_length=100)
    juniorProgramer = models.CharField(max_length=100)
    
class result(models.Model):
    studentId = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    major = models.CharField(max_length=100)
    profile = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    subject_2 = models.CharField(max_length=100)
    subject_3 = models.CharField(max_length=100)
    subject_4 = models.CharField(max_length=100)
    subject_5 = models.CharField(max_length=100)
    