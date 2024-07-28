from .models import HashingAlgorithm
from table import Table
from table.utils import A
from table.columns import Column, CheckboxColumn, LinkColumn, Link


class HashingAlgorithmTable(Table):
    x = CheckboxColumn(field='', header='')
    id = Column(field='id', header='S/N', attrs={'class': "user-name"})
    name = Column(field='name', header='Name', attrs={'class': 'custom user-name'},
                  header_attrs={'search': True}, searchable=False)
    hash_type = Column(field='hash_type',  header='Hash Type',
                             searchable=False, attrs={'class': "user-name"})
    action = LinkColumn(header='Action',
                        links=[Link(text='Edit', viewname='hashing_algorithms:edit', args=(A('id'),)),
                               Link(text='View', viewname='hashing_algorithms:show', args=(A('id'),))],
                        delimiter=" | ")

    class Meta:
        model = HashingAlgorithm
        attrs = {'class': 'table-bordered'}
        sort = [
            (0, 'asc'),
            (1, 'asc'),
            (2, 'asc')
        ]
        search = True
        pagination = True
        info = True
        zero_records = "No Records"
        # ext_button = True
        # ext_button_template = "My btn"
        # ext_button_template_name = "The btn"
