from django.db import models

from apps.common.models import Quiz
from apps.course_topics.models import CourseTopic
from apps.courses.models import Course


# Create your models here.
class CourseTopicQuiz(Quiz):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    course_topic = models.ForeignKey(CourseTopic, on_delete=models.CASCADE)

    class Meta:
        db_table = 'course_topic_quizzes'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("CourseTopicQuiz_detail", kwargs={"pk": self.pk})
