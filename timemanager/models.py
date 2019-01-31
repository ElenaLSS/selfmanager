
from django.contrib.auth.models import User
from django.db import models

# Create your models here.




class SpecificTask(models.Model):
    FAIL = 'fail'
    FINISH = 'finish'
    WAIT = 'wait'
    STATUS_CHOICES = (
        (FAIL, '失败'),
        (FINISH, '完成'),
        (WAIT, '待完成')
    )
    create_time = models.DateTimeField('date published')  # 创建时间
    start_time = models.DateTimeField('date published')   # 开始时间
    end_time = models.DateTimeField('date published')     # 结束时间
    headline = models.CharField(max_length=200)           # 标题
    description = models.CharField(max_length=200)        # 描述
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=WAIT,)

class WeekDayTime(models.Model):
    specific_task = models.ForeignKey(SpecificTask, on_delete=models.CASCADE)
    day = models.IntegerField()
    time = models.IntegerField()
    time_length = models.IntegerField(default=1)
