from flask import Flask, render_template
import pymysql.cursors
import logging
from flask_socketio import SocketIO, emit # type: ignore
from models.room import Room


app = Flask(__name__)
logging.basicConfig(filename='error.log',level=logging.DEBUG)
conn = pymysql.connect(host='localhost',
                       user='root',
                       password='root')

socketio = SocketIO(app)


@app.route("/", methods=['GET', 'POST'])
def hello():
    logging.debug("Hello was called")
    return render_template('index.html')

@app.route("/pp", methods=['GET'])
def test_write():
    logging.debug("test_write was called")
    logging.debug("connect was called")
    create_and_use_db("test1")
    logging.debug("creating table")
    create_table()
    return 'hello world'

def create_and_use_db(db_name):
    create_sql = 'create database {}'.format(db_name)
    try:
        conn.cursor().execute(create_sql)
    except pymysql.err.ProgrammingError:
        logging.debug("db already exists")

    use_sql = 'use {}'.format(db_name)
    conn.cursor().execute(use_sql)

def create_table():
    create_table_sql = 'CREATE TABLE example ( id smallint unsigned not null auto_increment, name varchar(20) not null, constraint pk_example primary key (id) );'
    try:
        conn.cursor().execute(create_table_sql)
    except pymysql.err.InternalError:
        logging.debug("table already exists")

    logging.debug("table created")

@socketio.on('my message')
def test_message(message):
    emit('my response', {'data': 'got it!'})

@socketio.on('test')
def this_is_a_test(message):
    print("test message:", message)


@socketio.on('message_sent')
def log_changes(message):
    logging.debug("message sent:", message)

    if 'room' in message:
        # a room is contained in this update
        room_json = message['room']
        room = Room.from_json(room_json)
        logging.debug(room)



if __name__ == '__main__':
    print("LISTENING")
    socketio.run(app)
