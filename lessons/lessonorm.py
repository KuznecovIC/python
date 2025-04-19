import peewee as pw
db = pw.SqliteDatabase('lessons\students_new.db')

class Profession(pw.Model):
    title = pw.CharField(unique=True)
    description = pw.TextField(null=True)

    class Meta:
        database = db
        table_name = 'professions'

class Group(pw.Model):
    group_name = pw.CharField(unique=True)
    start_date = pw.DateTimeField(constraints=[pw.SQL('DEFAULT CURRENT_TIMESTAMP')])
    end_date = pw.DateTimeField(null=True)
    profession = pw.ForeignKeyField(Profession, backref='groups', null=True)

    class Meta:
        database = db
        table_name = 'groups'

class Student(pw.Model):
    first_name = pw.CharField()
    middle_name = pw.CharField(null=True)
    last_name = pw.CharField()
    age = pw.IntegerField(null=True)
    group = pw.ForeignKeyField(Group, backref='students', null=True)

    class Meta:
        database = db
        table_name = 'students'

all students = Student.select()

