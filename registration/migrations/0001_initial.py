# Generated by Django 2.1.1 on 2018-09-23 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_number', models.CharField(max_length=7)),
                ('last_name', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('year_level', models.CharField(choices=[('1ST YEAR', '1ST YEAR'), ('2ND YEAR', '2ND YEAR'), ('3RD YEAR', '3RD YEAR'), ('4TH YEAR', '4TH YEAR'), ('5TH YEAR', '5TH YEAR'), ('GRADE 11', 'GRADE 11'), ('GRADE 12', 'GRADE 12')], default='1ST YEAR', max_length=30)),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
