from django.shortcuts import render
<<<<<<< HEAD
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
=======
from django.http import Http404
from django.http import HttpResponse
from .models import SpecificTask, WeekDayTime
import datetime

# Create your views here.
base_date = datetime.date(2019, 1, 7)

# 0 表示6点
# 0 表示周一

def index(request):
    # 获得当前的日期
    today = datetime.date.today()
    # 获得当前的年份的第一周的星期一的日期
    current_base_date = get_year_base_date(today.year)
    # 获得当前是第几周
    week = int((today - current_base_date).days / 7 + 1)
    # 当前所在周的星期一
    week_base = get_year_week(today.year, week)
    # 当前所在周的星期日
    week_base_plus_7 = week_base + datetime.timedelta(6)
    context = {'week': week}
    user = request.user
    # 查询在当前周的任务
    task_set = user.specifictask_set.all().filter(end_time__gte=week_base_plus_7)\
        .filter(start_time__lte=week_base_plus_7)

    # ->对数据进行处理，产生用于渲染模板的数据
    week_data_list_3 = [[] for i in range(3)]
    week_data_list_7 = [[] for i in range(4)]

    for i in range(3):
        for j in range(18):
            taskdata = {'length': 40, 'time': j}
            week_data_list_3[i].append(taskdata)
    for i in range(4):
        for j in range(18):
            taskdata = {'length': 40, 'time': j}
            week_data_list_7[i].append(taskdata)

    for task in task_set:
        # print(task.headline)
        for week_day_time in task.weekdaytime_set.all():
            if datetime.timedelta(days=week_day_time.day) + week_base < task.start_time:
                continue
            taskdata = {'headline': task.headline, 'start': task.start_time, 'time': week_day_time.time,
                        'length': week_day_time.time_length*40}
            if week_day_time.day >= 3:
                # print("hhh")
                for i in range(week_day_time.time, week_day_time.time + week_day_time.time_length):
                    for item in week_data_list_7[week_day_time.day - 3]:
                        if item['time'] == i:
                            week_data_list_7[week_day_time.day - 3].remove(item)
                            break
                week_data_list_7[week_day_time.day - 3].append(taskdata)
                print(week_data_list_7[week_day_time.day - 3])
            else:
                for i in range(week_day_time.time, week_day_time.time + week_day_time.time_length):
                    for item in week_data_list_3[week_day_time.day]:
                        if item['time'] == i:
                            week_data_list_3[week_day_time.day].remove(item)
                            break
                week_data_list_3[week_day_time.day].append(taskdata)
    for i in range(3):
        week_data_list_3[i].sort(key=lambda x: x['time'])
    for i in range(4):
        week_data_list_7[i].sort(key=lambda x: x['time'])
    # 对数据进行处理，产生用于渲染模板的数据<-
    context['week_data_list_3'] = week_data_list_3
    context['week_data_list_7'] = week_data_list_7

    return render(request, 'timemanager/index.html', context)


def add_task(request):
    if request.method == 'POST':
        pass
        raise Http404("en")
    else:
        raise Http404("不合法的查询！")


def get_day(year, month, day):  # 返回星期几
    date_current = datetime.date(year, month, day)
    delta = date_current - base_date
    return delta.days % 7 + 1


def get_year_base_date(year):  # 求某年的 第一周 第一天 日期
    day = get_day(year, 1, 1)  # year 年 1 月 1 日是星期几
    return datetime.date(year, 1, (1+7-day) % 7 + 1)


def get_year_week(year, week):
    year_base = get_year_base_date(year)
    return year_base + datetime.timedelta(days=(week-1) * 7)


>>>>>>> upstream/master
