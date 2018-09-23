from django.db import models


class Student(models.Model):
    student_number = models.CharField(max_length=7)
    last_name = models.UpperCharField()
    first_name = models.UpperCharField()
    year_level = (
        ('1ST YEAR', '1ST YEAR'),
        ('2ND YEAR', '2ND YEAR'),
        ('3RD YEAR', '3RD YEAR'),
        ('4TH YEAR', '4TH YEAR'),
        ('5TH YEAR', '5TH YEAR'),
    )
    date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.last_name + " " + self.first_name
