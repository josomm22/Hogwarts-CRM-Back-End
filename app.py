from flask import Flask, jsonify, render_template
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
def get_student_table():
    students = []
    for student in database['students']:
        student_row = dict(id = student['id'], firstName = student['first_name'], lastName = student['last_name'], dateCreated = student['date_created'], dateUpdated = student['last_updated'] )
        students.append(student_row)
    return jsonify({'students': students})


if __name__ == "__main__":
    threading.Thread(target=app.run).start()
    time.sleep(0.5)