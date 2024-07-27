from .models import CourseTopic
from table import Table
from table.utils import A
from table.columns import Column, CheckboxColumn, LinkColumn, Link


class CourseTopicTable(Table):
    x = CheckboxColumn(field='', header='')
    id = Column(field='id', header='S/N', attrs={'class': "user-name"})
    name = Column(field='name', header='Name', attrs={
                  'class': 'custom user-name'}, header_attrs={'search': True}, searchable=False)
    slug = Column(field='slug',  header='Slug',
                  searchable=False, attrs={'class': "user-name"})
    course = Column(field='course',  header='Course',
                    searchable=False, attrs={'class': "user-name"})
    action = LinkColumn(header='Action',
                        links=[Link(text='Edit', viewname='course_topics:edit', args=(A('id'),)),
                               Link(text='View', viewname='course_topics:show', args=(A('id'),))],
                        delimiter=" | ")

    class Meta:
        model = CourseTopic
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
