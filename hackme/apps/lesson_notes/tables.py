from .models import LessonNote
from table import Table
from table.utils import A
from table.columns import Column, CheckboxColumn, LinkColumn, Link


class LessonNoteTable(Table):
    x = CheckboxColumn(field='', header='')
    id = Column(field='id', header='S/N',
                attrs={'class': "user-name"})
    lesson = Column(field='name', header='Name', attrs={
        'class': 'custom user-name  text-wrap'}, header_attrs={'search': True}, searchable=False)
    action = LinkColumn(header='Action',
                        links=[Link(text='Edit', viewname='lesson_notes:edit', args=(A('id'),)),
                               Link(text='View', viewname='lesson_notes:show', args=(A('id'),))],
                        delimiter=" | ")

    class Meta:
        model = LessonNote
        attrs = {'class': 'table-bordered'}
        sort = [
            (0, 'asc'),
        ]
        search = True
        pagination = True
        info = True
        # ext_button = True
        # ext_button_template = "My btn"
        # ext_button_template_name = "The btn"
