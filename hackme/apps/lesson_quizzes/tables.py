from .models import LessonQuiz
from table import Table
from table.utils import A
from table.columns import Column, CheckboxColumn, LinkColumn, Link


class LessonQuizTable(Table):
    x = CheckboxColumn(field='', header='')
    id = Column(field='id', header='S/N', attrs={'class': "user-name"})
    name = Column(field='name', header='Name', attrs={
                  'class': 'custom user-name'}, header_attrs={'search': True}, searchable=False)
    course = Column(field='course',  header='Course',
                    searchable=False, attrs={'class': "user-name"})
    course_topic = Column(field='course_topic',  header='Course Topic',
                          searchable=False, attrs={'class': "user-name"})
    action = LinkColumn(header='Action',
                        links=[Link(text='Edit', viewname='lesson_quizzes:edit', args=(A('id'),)),
                               Link(text='View', viewname='lesson_quizzes:show', args=(A('id'),))],
                        delimiter=" | ")

    class Meta:
        model = LessonQuiz
        attrs = {'class': 'table-bordered'}
        sort = [
            (0, 'asc'),
            (1, 'asc'),
            (2, 'asc')
        ]
        search = True
        pagination = True
        info = True
        # ext_button = True
        # ext_button_template = "My btn"
        # ext_button_template_name = "The btn"
