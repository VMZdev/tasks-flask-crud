from flask import Flask, request, jsonify
from models.task import Task

#__name__ = "__main__"
app = Flask(__name__)

# CRUD
# Create, Read, Update and Delete
# Tabela: Tarefa

tasks = []
task_id_control = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control # Inserção do taask_id_control que esta fora da definição de rota
    data = request.get_json() # Receber os dados em json
    new_task = Task(id=task_id_control, title=data['title'], description=data.get("description", "")) # Caso não coloque uma descrição,
    # o campo ficará vazio, ou seja, é assim que vc coloca elementos root
    task_id_control += 1 # numero do id = n+1
    tasks.append(new_task) # Adicionar a nova task à lista de tasks
    print(tasks)
    return jsonify({"message": 'Nova tarefa criada com sucesso'}) # Por padrão, temos que voltar ou XML ou JSON, mas tem que ser com um dicionario

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
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
    
    return jsonify({"message": "Não foi possivel encontrar a atividade"}), 404 #jsonify precisa utiluizar o dicionario

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
    print(task)
    if task == None:
        return jsonify({"message": "Não foi possivel encontrar a atividade"}), 404

    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    print(task)
    return jsonify({"message": "Tarefa atualizada com sucesso"})

@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = None #
    for t in tasks: # 
        if t.id == id: # Nada mais nada menos que um PROCV
            task = t #

    if task == None:
        return jsonify({"message": "Não foi possivel encontrar a atividade"}), 404
    
    tasks.remove(task)
    return jsonify({"message": "Tarefa deletada com sucesso"})

if __name__ == "__main__":
    app.run(debug=True)