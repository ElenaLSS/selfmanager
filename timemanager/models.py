
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
    headline = models.CharField(max_length=200)  # 标题
    create_time = models.DateField()  # 创建时间
    start_time = models.DateField()   # 开始时间
    end_time = models.DateField()     # 结束时间

    description = models.CharField(max_length=200)        # 描述
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=WAIT,)

    def __str__(self):
        return self.headline


class WeekDayTime(models.Model):
    specific_task = models.ForeignKey(SpecificTask, on_delete=models.CASCADE)
    day = models.IntegerField()
    time = models.IntegerField()
    time_length = models.IntegerField(default=1)

    def __str__(self):
        return self.specific_task.headline

