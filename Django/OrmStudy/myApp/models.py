from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=32, verbose_name="姓名")
    age = models.SmallIntegerField(verbose_name="年龄")

    sex_choices = ((0, '男'), (1, '女'), (2, '保密'))
    sex = models.SmallIntegerField(choices=sex_choices, verbose_name="性别有男，女，保密")

    birthday = models.DateField(verbose_name="生日")

    classmate = models.CharField(db_column="class", max_length=5, db_index=True, verbose_name="班级")
    description = models.TextField(default="", verbose_name="个性签名")

    class Meta:
        db_table = 'db_student'

    def __str__(self):
        return self.name + " " + str(self.age)


