from .models import CourseQuiz
from table import Table
from table.utils import A
from table.columns import Column, CheckboxColumn, LinkColumn, Link


class CourseQuizTable(Table):
    x = CheckboxColumn(field='', header='')
    id = Column(field='id', header='S/N', attrs={'class': "user-name"})
    name = Column(field='name', header='Name', attrs={
                  'class': 'custom user-name'}, header_attrs={'search': True}, searchable=False)
    action = LinkColumn(header='Action',
                        links=[Link(text='Edit', viewname='course_quizzes:edit', args=(A('id'),)),
                               Link(text='View', viewname='course_quizzes:show', args=(A('id'),))],
                        delimiter=" | ")

    class Meta:
        model = CourseQuiz
        attrs = {'class': 'table-bordered'}
        sort = [
            (0, 'asc'),
            (1, 'asc'),
            (2, 'asc')
        ]
        search = True
        pagination = True
        info = True
        info = True
        # ext_button = True
        # ext_button_template = "My btn"
        # ext_button_template_name = "The btn"
