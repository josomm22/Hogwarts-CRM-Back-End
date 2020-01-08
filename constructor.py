from database import database


def construct():
    tag_full = ''
    for entry in database['students']:
        tag_intro = '<h3>'
        tag_outro = '<h3>'
        tag_single = tag_intro + str(entry['first_name']) + ' '+ str(entry['last_name'])
        tag_full = tag_full + tag_single
    return tag_full

def students_table():
    outer_tag_intro = '<table>'
    outer_tag_outro = '</table>'
    headers = '<tr> <th>Firstname</th><th>Lastname</th>'
