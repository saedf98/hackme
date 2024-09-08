from .models import User
from table import Table
from table.utils import A
from table.columns import Column, CheckboxColumn, LinkColumn, Link


class UserTable(Table):
    x = CheckboxColumn(field='', header='')
    id = Column(field='id', header='S/N', attrs={'class': "user-name"})
    username = Column(field='username', header='Username', attrs={
        'class': 'custom user-name'}, header_attrs={'search': True}, searchable=False)
    email = Column(field='email', header='Email', attrs={
        'class': 'custom user-name'}, header_attrs={'search': True}, searchable=False)
    first_name = Column(field='first_name',  header='Firstname',
                        searchable=False, attrs={'class': "user-name"})
    last_name = Column(field='last_name',  header='Lastname',
                       searchable=False, attrs={'class': "user-name"})
    action = LinkColumn(header='Action',
                        links=[
                            # Link(text='Edit', viewname='levels:edit', args=(A('id'),)),
                               Link(text='View', viewname='users:show', args=(A('id'),))],
                        delimiter=" | ")

    class Meta:
        model = User
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
