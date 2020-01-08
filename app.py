from flask import Flask, jsonify, abort, request, render_template
import threading
import time
from database import database
from constructor import construct as construct

app = Flask(__name__)

@app.route("/")
def main():
    me = {'username': 'jonathan'}
    return render_template('index.html', title ='poop', user=me)


@app.route("/students", methods=['GET'])
def get_students_table():
    students = []
    for student in database['students']:
        student_row = dict(id = student['id'], firstName = student['first_name'], lastName = student['last_name'], dateCreated = student['date_created'], dateUpdated = student['last_updated'] )
        students.append(student_row)
    return jsonify({'students': students})

@app.route("/students", methods=['POST'])
def create_new_student():
    students_db = database['students']
    if not request.json or not 'first_name' in request.json:
        abort(400)
    print(students_db)
    new_student = {
        'id': students_db[-1]['id']+1,
        'first_name': request.json['first_name'],
        'last_name': request.json['last_name'],
        'date_created': '08/01/2020',
        'last_updated': '08/01/2020',
        'existing_skillz': [[1,4],[3,2],[9,5],[14,4],[16,2]],
        'desired_skillz': [[1,5],[2,5],[6,4],[14,5],[3,2]],
        'course_interests': [3,4]
    }
    students_db.append(new_student)
    return jsonify({'new_student': new_student}), 201

@app.route("/students/<int:student_id>", methods=['GET'])
def get_student(student_id):
    students_db = database['students']
    student_details = [student for student in students_db if student['id'] == student_id]
    if len(student_details) == 0:
        abort(404)
    return jsonify({'student_details': student_details[0]})



if __name__ == "__main__":
    threading.Thread(target=app.run).start()
    time.sleep(0.5)