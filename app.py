from flask import Flask, jsonify, abort, request, render_template
import threading
import time
import os
from database import database, skillz, courses_list
from secondary import makeTimeStamp as makeTimeStamp
from flask_cors import CORS, cross_origin


app = Flask(__name__)
CORS(app)


@app.route("/")
def main():
    # me = {'username': 'jonathan'}
    return 'welcome to the Hogwarts Api'


@app.route("/students", methods=['GET'])
def get_students_table():
    students = []
    for student in database['students']:
        student_row = dict(id=student['id'], firstName=student['first_name'], lastName=student['last_name'],
                           dateCreated=student['date_created'], dateUpdated=student['last_updated'])
        students.append(student_row)
    response = {'students': students}
    return jsonify(response)


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
        'date_created': makeTimeStamp(),
        'last_updated': makeTimeStamp(),
        'existing_skillz': request.json['existing_skillz'],
        'desired_skillz': request.json['desired_skillz'],
        'course_interests': request.json['course_interests'],
    }
    students_db.append(new_student)
    return jsonify({'new_student': new_student}), 201


@app.route("/students/<int:student_id>", methods=['GET'])
def get_student(student_id):
    students_db = database['students']
    student_details = [
        student for student in students_db if student['id'] == student_id]
    if len(student_details) == 0:
        abort(404)
    return jsonify({'student_details': student_details[0]})


@app.route("/students/<int:student_id>", methods=['PUT'])
def update_student_details(student_id):
    students_db = database['students']
    student_details = [
        student for student in students_db if student['id'] == student_id]
    if len(student_details) == 0:
        abort(404)
    if not request.json:
        abort(400)
    # if 'first_name' in request.json and type(request.json['first_name']) != unicode:
    #     abort(400)
    # if 'last_name' in request.json and type(request.json['last_name']) is not unicode:
    #     abort(400)
    content = request.get_json()
    content = content['object']
    student_details[0]['first_name'] = content['first_name']
    student_details[0]['last_name'] = content['last_name']
    student_details[0]['existing_skillz'] = content['existing_skillz']
    student_details[0]['desired_skillz'] = content['desired_skillz']
    student_details[0]['course_interests'] = content['course_interests']
    student_details[0]['last_updated'] = makeTimeStamp()
    return jsonify({'student_details': student_details[0]})

@app.route("/students/skillssummary", methods=['GET'])
def get_students_skills():
    skills_array = []
    for student in database['students']:
        skills_array.append(student['existing_skillz'])
    return jsonify( skills_array)

@app.route("/students/creationsummary", methods=['GET'])
def get_created_on_date():
    created_on_array = []
    for student in database['students']:
        created_on_array.append(student['date_created'])
    return jsonify(created_on_array)


@app.route("/curriculum/skills", methods=['GET'])
def get_skillz():
    return jsonify(skillz)


@app.route("/curriculum/courses", methods=['GET'])
def get_courses():
    return jsonify(courses_list)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
