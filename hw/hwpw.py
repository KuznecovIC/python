from peewee import *
from datetime import datetime

# Подключение к базе данных SQLite
DB = SqliteDatabase('barbershop.db')

# Базовый класс модели
class BaseModel(Model):
    class Meta:
        database = DB

# Модель Master
class Master(BaseModel):
    first_name = CharField(max_length=50, null=False)
    last_name = CharField(max_length=50, null=False)
    middle_name = CharField(max_length=50, null=True)
    phone = CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.middle_name or ''}".strip()

# Модель Service
class Service(BaseModel):
    title = CharField(max_length=100, unique=True)
    description = TextField(null=True)
    price = DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f"{self.title} ({self.price} руб.)"

# Модель Appointment
class Appointment(BaseModel):
    client_name = CharField(max_length=100, null=False)
    client_phone = CharField(max_length=20, null=False)
    date = DateTimeField(default=datetime.now)
    master = ForeignKeyField(Master, backref='appointments')
    status = CharField(max_length=20, default='pending')
    comment = TextField(default='')

    def __str__(self):
        return f"Запись #{self.id} на {self.date.strftime('%d.%m.%Y %H:%M')}"

# Модель связи Master-Service (многие ко многим)
class MasterService(BaseModel):
    master = ForeignKeyField(Master)
    service = ForeignKeyField(Service)

    class Meta:
        primary_key = CompositeKey('master', 'service')

# Модель связи Appointment-Service (многие ко многим)
class AppointmentService(BaseModel):
    appointment = ForeignKeyField(Appointment)
    service = ForeignKeyField(Service)

    class Meta:
        primary_key = CompositeKey('appointment', 'service')

def create_tables():
    """Создание таблиц в базе данных"""
    with DB:
        DB.create_tables([
            Master,
            Service,
            Appointment,
            MasterService,
            AppointmentService
        ])

def populate_test_data():
    """Наполнение базы тестовыми данными"""
    # Очистка таблиц
    AppointmentService.delete().execute()
    MasterService.delete().execute()
    Appointment.delete().execute()
    Service.delete().execute()
    Master.delete().execute()

    # Создание мастеров
    masters = [
        Master.create(
            first_name="Иван",
            last_name="Петров",
            middle_name="Александрович",
            phone="+79991112233"
        ),
        Master.create(
            first_name="Дмитрий",
            last_name="Смирнов",
            middle_name="Владимирович",
            phone="+79998887766"
        ),
        Master.create(
            first_name="Алексей",
            last_name="Иванов",
            phone="+79995554433"
        )
    ]

    # Создание услуг
    services = [
        Service.create(
            title="Мужская стрижка",
            description="Классическая мужская стрижка",
            price=800.00
        ),
        Service.create(
            title="Бритьё головы",
            description="Горячее полотенце и бритьё опасной бритвой",
            price=600.00
        ),
        Service.create(
            title="Детская стрижка",
            description="Стрижка для детей до 12 лет",
            price=500.00
        ),
        Service.create(
            title="Стрижка бороды",
            description="Коррекция формы бороды",
            price=400.00
        )
    ]

    # Связи мастеров и услуг
    MasterService.insert_many([
        {'master': masters[0].id, 'service': services[0].id},
        {'master': masters[0].id, 'service': services[1].id},
        {'master': masters[1].id, 'service': services[0].id},
        {'master': masters[1].id, 'service': services[2].id},
        {'master': masters[2].id, 'service': services[3].id},
        {'master': masters[2].id, 'service': services[0].id}
    ]).execute()

    # Создание записей
    appointments = [
        Appointment.create(
            client_name="Алексей Иванов",
            client_phone="+79001234567",
            date=datetime(2023, 10, 15, 10, 0),
            master=masters[0],
            status="confirmed",
            comment="Хочу короткую стрижку"
        ),
        Appointment.create(
            client_name="Сергей Сидоров",
            client_phone="+79009876543",
            date=datetime(2023, 10, 15, 11, 30),
            master=masters[1],
            status="pending",
            comment="Укладка для мероприятия"
        ),
        Appointment.create(
            client_name="Ольга Петрова",
            client_phone="+79001112233",
            date=datetime(2023, 10, 16, 14, 0),
            master=masters[2],
            status="completed",
            comment="Коррекция бороды"
        )
    ]

    # Связи записей и услуг
    AppointmentService.insert_many([
        {'appointment': appointments[0].id, 'service': services[0].id},
        {'appointment': appointments[0].id, 'service': services[3].id},
        {'appointment': appointments[1].id, 'service': services[2].id},
        {'appointment': appointments[1].id, 'service': services[1].id},
        {'appointment': appointments[2].id, 'service': services[3].id},
        {'appointment': appointments[2].id, 'service': services[0].id}
    ]).execute()

def print_data():
    """Вывод данных из базы"""
    print("\nМастера:")
    for master in Master.select():
        print(f"- {master}")
        services = (Service.select()
                   .join(MasterService)
                   .where(MasterService.master == master))
        print("  Услуги:", ", ".join(str(s) for s in services))

    print("\nУслуги:")
    for service in Service.select():
        print(f"- {service}")

    print("\nЗаписи:")
    for appointment in Appointment.select():
        print(f"- {appointment}")
        print(f"  Клиент: {appointment.client_name}, тел.: {appointment.client_phone}")
        print(f"  Статус: {appointment.status}, мастер: {appointment.master}")
        services = (Service.select()
                   .join(AppointmentService)
                   .where(AppointmentService.appointment == appointment))
        print("  Услуги:", ", ".join(str(s) for s in services))
        if appointment.comment:
            print(f"  Комментарий: {appointment.comment}")

def main():
    """Основная функция"""
    create_tables()
    populate_test_data()
    print_data()

if __name__ == '__main__':
    main()