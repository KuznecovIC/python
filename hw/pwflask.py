from flask import Flask, request, jsonify
from peewee import *
from datetime import datetime
import json

app = Flask(__name__)

# Настройка базы данных
db = SqliteDatabase('barbershop.db')

# Модель Мастера
class Master(Model):
    first_name = CharField(max_length=50)
    last_name = CharField(max_length=50)
    middle_name = CharField(max_length=50, null=True)
    phone = CharField(max_length=20)

    class Meta:
        database = db

# Модель Записи
class Appointment(Model):
    client_name = CharField(max_length=100)
    client_phone = CharField(max_length=20)
    date = DateTimeField()
    master = ForeignKeyField(Master, backref='appointments')
    status = CharField(max_length=20, default='ожидание')

    class Meta:
        database = db

# Функции преобразования
def master_to_dict(master):
    return {
        'id': master.id,
        'first_name': master.first_name,
        'last_name': master.last_name,
        'middle_name': master.middle_name,
        'phone': master.phone
    }

def appointment_to_dict(appointment):
    return {
        'id': appointment.id,
        'client_name': appointment.client_name,
        'client_phone': appointment.client_phone,
        'date': appointment.date.strftime('%Y-%m-%d %H:%M:%S'),
        'master': master_to_dict(appointment.master),
        'status': appointment.status
    }

# Валидация данных
def validate_master_data(data):
    required = ['first_name', 'last_name', 'phone']
    if not all(field in data for field in required):
        return False, 'Отсутствуют обязательные поля'
    return True, None

def validate_appointment_data(data):
    required = ['client_name', 'client_phone', 'master_id', 'date']
    if not all(field in data for field in required):
        return False, 'Отсутствуют обязательные поля'
    
    try:
        datetime.strptime(data['date'], '%Y-%m-%d %H:%M:%S')
    except ValueError:
        return False, 'Неверный формат даты'
    
    return True, None

# Маршруты API
@app.route('/')
def home():
    return jsonify({
        "API": "Barbershop", 
        "version": "1.0",
        "endpoints": {
            "masters": "/masters",
            "appointments": "/appointments"
        }
    })

@app.route('/masters', methods=['GET'])
def get_masters():
    masters = Master.select()
    return json_response({'masters': [master_to_dict(m) for m in masters]})

@app.route('/masters/<int:master_id>', methods=['GET'])
def get_master(master_id):
    master = Master.get_or_none(Master.id == master_id)
    if not master:
        return json_response({'error': 'Мастер не найден'}, 404)
    return json_response(master_to_dict(master))

@app.route('/masters', methods=['POST'])
def create_master():
    data = request.get_json()
    is_valid, error = validate_master_data(data)
    if not is_valid:
        return json_response({'error': error}, 400)
    
    master = Master.create(
        first_name=data['first_name'],
        last_name=data['last_name'],
        middle_name=data.get('middle_name'),
        phone=data['phone']
    )
    return json_response(master_to_dict(master), 201)

@app.route('/masters/<int:master_id>', methods=['PUT'])
def update_master(master_id):
    master = Master.get_or_none(Master.id == master_id)
    if not master:
        return json_response({'error': 'Мастер не найден'}, 404)
    
    data = request.get_json()
    master.first_name = data.get('first_name', master.first_name)
    master.last_name = data.get('last_name', master.last_name)
    master.middle_name = data.get('middle_name', master.middle_name)
    master.phone = data.get('phone', master.phone)
    master.save()
    
    return json_response(master_to_dict(master))

@app.route('/masters/<int:master_id>', methods=['DELETE'])
def delete_master(master_id):
    master = Master.get_or_none(Master.id == master_id)
    if not master:
        return json_response({'error': 'Мастер не найден'}, 404)
    
    master.delete_instance()
    return '', 204

@app.route('/appointments', methods=['GET'])
def get_appointments():
    sort_by = request.args.get('sort_by', 'date')
    direction = request.args.get('direction', 'asc')
    
    query = Appointment.select()
    
    if hasattr(Appointment, sort_by):
        field = getattr(Appointment, sort_by)
        query = query.order_by(field.desc() if direction == 'desc' else field)
    
    return json_response({'appointments': [appointment_to_dict(a) for a in query]})

@app.route('/appointments/<int:appointment_id>', methods=['GET'])
def get_appointment(appointment_id):
    appointment = Appointment.get_or_none(Appointment.id == appointment_id)
    if not appointment:
        return json_response({'error': 'Запись не найдена'}, 404)
    return json_response(appointment_to_dict(appointment))

@app.route('/appointments/master/<int:master_id>', methods=['GET'])
def get_master_appointments(master_id):
    master = Master.get_or_none(Master.id == master_id)
    if not master:
        return json_response({'error': 'Мастер не найден'}, 404)
    
    appointments = Appointment.select().where(Appointment.master == master)
    return json_response({'appointments': [appointment_to_dict(a) for a in appointments]})

@app.route('/appointments', methods=['POST'])
def create_appointment():
    data = request.get_json()
    is_valid, error = validate_appointment_data(data)
    if not is_valid:
        return json_response({'error': error}, 400)
    
    master = Master.get_or_none(Master.id == data['master_id'])
    if not master:
        return json_response({'error': 'Мастер не найден'}, 404)
    
    appointment = Appointment.create(
        client_name=data['client_name'],
        client_phone=data['client_phone'],
        date=data['date'],
        master=master,
        status=data.get('status', 'ожидание')
    )
    return json_response(appointment_to_dict(appointment), 201)

@app.route('/appointments/<int:appointment_id>', methods=['PUT'])
def update_appointment(appointment_id):
    appointment = Appointment.get_or_none(Appointment.id == appointment_id)
    if not appointment:
        return json_response({'error': 'Запись не найдена'}, 404)
    
    data = request.get_json()
    
    if 'master_id' in data:
        master = Master.get_or_none(Master.id == data['master_id'])
        if not master:
            return json_response({'error': 'Мастер не найден'}, 404)
        appointment.master = master
    
    appointment.client_name = data.get('client_name', appointment.client_name)
    appointment.client_phone = data.get('client_phone', appointment.client_phone)
    appointment.status = data.get('status', appointment.status)
    
    if 'date' in data:
        try:
            appointment.date = datetime.strptime(data['date'], '%Y-%m-%d %H:%M:%S')
        except ValueError:
            return json_response({'error': 'Неверный формат даты'}, 400)
    
    appointment.save()
    return json_response(appointment_to_dict(appointment))

@app.route('/appointments/<int:appointment_id>', methods=['DELETE'])
def delete_appointment(appointment_id):
    appointment = Appointment.get_or_none(Appointment.id == appointment_id)
    if not appointment:
        return json_response({'error': 'Запись не найдена'}, 404)
    
    appointment.delete_instance()
    return '', 204

# Вспомогательная функция для JSON-ответов
def json_response(data, status=200):
    return json.dumps(data, ensure_ascii=False), status, {'Content-Type': 'application/json; charset=utf-8'}

# Инициализация базы данных и тестовых данных
def initialize_db():
    db.connect()
    db.create_tables([Master, Appointment], safe=True)
    
    # Создаем тестовые данные если таблицы пустые
    if not Master.select().exists():
        master1 = Master.create(
            first_name="Иван",
            last_name="Барберов",
            phone="+7-999-111-11-11"
        )
        Master.create(
            first_name="Петр",
            last_name="Стриженов",
            phone="+7-999-222-22-22"
        )
        
        Appointment.create(
            client_name="Алексей Клиентов",
            client_phone="+7-888-111-11-11",
            date="2025-05-10 12:00:00",
            master=master1,
            status="подтверждено"
        )

# Запуск приложения
if __name__ == '__main__':
    initialize_db()
    app.run(debug=True)