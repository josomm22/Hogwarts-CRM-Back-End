from database import database
import names
from random import randint as randint


def construct():
    tag_full = ''
    for entry in database['students']:
        tag_intro = '<h3>'
        tag_outro = '<h3>'
        tag_single = tag_intro + \
            str(entry['first_name']) + ' ' + str(entry['last_name'])
        tag_full = tag_full + tag_single
    return tag_full


def students_table():
    outer_tag_intro = '<table>'
    outer_tag_outro = '</table>'
    headers = '<tr> <th>Firstname</th><th>Lastname</th>'

def createArr(amount, numberOfKeys, minLevel, maxLevel):
        array = []
        for element in range(amount):
            element = []
            element.append(randint(1,numberOfKeys))
            element.append(randint(minLevel,maxLevel))
            array.append(element)
        return array

def createRandomStudent(id):
    newStudent = {}
    newStudent['id'] = id
    newStudent['first_name'] = names.get_first_name()
    newStudent['last_name'] = names.get_last_name()
    random_day = str(randint(1, 30))
    if (len(random_day) is 1):
        random_day = '0'+random_day
        random_day = str(randint(1, 30))
    random_month = str(randint(1, 12))
    if (len(random_month) is 1):
        random_month = '0'+random_month
    newStudent['date_created'] = random_day+'/'+random_month+'/'+'2019 16:20:69'
    newStudent['last_updated'] = newStudent['date_created']
    newStudent['existing_skills'] = createArr(5,17,1,5)
    newStudent['desired_skills'] = createArr(5,17,1,5)
    newStudent['course_interests'] = createArr(2,4,0,0)
    return newStudent
    

def createStudentArray(numberOfStudents):
    studentArray = []
    i = 0
    while(i < numberOfStudents):
        i +=1
        print(i)
        student = createRandomStudent(i+1006)
        studentArray.append(student)
    print(studentArray)

createStudentArray(10)
