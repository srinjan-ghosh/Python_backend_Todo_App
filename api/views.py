# imports
from flask import Blueprint, jsonify, request
from flask_cors import CORS
from .models import Todo
from . import db
from sqlalchemy import desc

api = Blueprint('api', __name__)
CORS(api)

# ROUTES

# -- ADD NEW TODO
@api.route('/add', methods=['POST'])
def add_todo():
    # get the json data
    data = request.get_json()

    #create a new Todo object with the data passed 
    new_todo = Todo(todo=data['todo'])

    #add it to the database
    db.session.add(new_todo)
    db.session.commit()

    return jsonify({"id": new_todo.id}), 201

# -- GET ALL TODOS
@api.route('/todos', methods=['GET'])
def get_todos():

    todo_list = Todo.query.order_by(desc(Todo.id)).all()

    todos = []

    for todo in todo_list:
        todos.append({
            "id": todo.id,
            "todo": todo.todo,
            "done": todo.done
        })
    return jsonify({"todos": todos})

# -- GET TODO ITEM BY ID
@api.route('/todo/<int:id>', methods=['GET'])
def get_todo(id):
    # get the todo by the id of the todo
    todo_list = Todo.query.filter_by(id=id).first()

    # check whether the todo exists for the particular id
    if todo_list is None:
        return jsonify({"todo": "no todo found"}), 404

    todo = []

    todo.append({
        "id": todo_list.id,
        "todo": todo_list.todo,
        "done": todo_list.done
    })

    return jsonify({"todo": todo})

# -- UPDATE TODO
#   -- Update Todo Title
@api.route('/update_todo_title/<int:id>', methods=['PUT'])
def update_todo_title(id):
    # get the todo by the id of the todo
    todo = Todo.query.filter_by(id=id).first()

    # check whether the todo exists for the particular id
    if todo is None:
        return jsonify({"todo": "no todo found"}), 404

    # get the new todo title as json
    new_todo_title = request.get_json()['todo']

    # update the todo title
    todo.todo = new_todo_title

    # add to the database
    db.session.commit()

    return 'Updated', 201

#   -- Mark Todo as Done
@api.route('/update_checked/<int:id>', methods=['PUT'])
def update_todo_done(id):
    # get the todo by the id of the todo
    todo = Todo.query.filter_by(id=id).first()

    # check whether the todo exists for the particular id
    if todo is None:
        return jsonify({"todo": "no todo found"}), 404
    
    # change the 'done' property value. if true then false. if false then true
    todo.done = not todo.done

    #update the todo item
    db.session.commit()

    return 'Updated', 201

# -- DELETE TODO
@api.route('/delete/<int:id>', methods=['DELETE'])
def delete_todo(id):
    # get the todo by the id of the todo
    todo = Todo.query.filter_by(id=id).first()

    # check whether the todo exists for the particular id
    if todo is None:
        return jsonify({"todo": "no todo found"}), 404

    # delete the specified todo from the database
    db.session.delete(todo)
    db.session.commit()

    return 'Deleted', 201
