from flask import Flask, request, jsonify
from models.task import Task
app = Flask(__name__)

tasks = []  # armazena objetos
task_id_control = 1


# CREATE
@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()  # o metodo .gte_json() recupera o que o cliente enviou
    new_task = Task(id=task_id_control, title=data['title'], description=data.get("description", ""))
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message": "Nova tarefa criada com sucesso!"})


# READ
@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = [task.to_dict() for task in tasks]

    output = {
                "tasks": task_list,
                "total_tasks": len(task_list)
            }
    return jsonify(output)


@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
    return jsonify({"message": "Nao foi possivel encontrar a atividade"}), 404


# UPDATE
@app.route('/tasks/<int:id>', methods=["PUT"])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break
    print(task)

    if task == None:
        return jsonify({"message": "Nao foi possivel encontrar a atividade"}), 404

    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    print(task)

    return jsonify({"message": "Tarefa atualizada com sucesso"})


# DELETE
@app.route('/tasks/<int:id>', methods=["DELETE"])
def delete_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break

    if task is None:
        return jsonify({"message": "Nao foi possivel encontrar a atividade"})

    tasks.remove(task)
    return jsonify({"message": "Tarefa deletada com sucesso!"})


if __name__ == "__main__":
    app.run(debug=True)
