from django.db import models

from apps.common.models import Quiz
from apps.course_topics.models import CourseTopic
from apps.courses.models import Course


# Create your models here.
class CourseTopicQuiz(Quiz):
    course = models.ForeignKey(
        Course,
        related_name='course_topic_quizzes',
        on_delete=models.CASCADE)
    course_topic = models.ForeignKey(
        CourseTopic,
        related_name='course_topic_quizzes',
        on_delete=models.CASCADE)

    class Meta:
        db_table = 'course_topic_quizzes'

    def get_default_name(self):
        return f"{self.course_topic.name} Quiz"

    def __str__(self):
        return self.name
