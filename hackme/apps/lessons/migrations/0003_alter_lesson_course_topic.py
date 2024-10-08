# Generated by Django 5.0.7 on 2024-08-04 21:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_topics', '0003_alter_coursetopic_course'),
        ('lessons', '0002_lesson_course_topic_alter_lesson_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lesson',
            name='course_topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='course_topics.coursetopic'),
        ),
    ]
