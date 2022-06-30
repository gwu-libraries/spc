from internetarchive import get_item
target = 'files/file_name.txt'
md = {'metadata-field-name': 'value'}
item = get_item('item_identifier')
item.modify_metadata(md, target=target)
f = item.get_file('file_name.txt')
f.__dict__['metadata-field-name']
U'value'
