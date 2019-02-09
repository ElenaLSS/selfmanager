from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from .models import SpecificTask, WeekDayTime
import datetime

# Create your views here.
base_date = datetime.date(2019, 1, 7)


def index(request):
    today = datetime.date.today()
    current_base_date = get_year_base_date(today.year)
    week = int((today - current_base_date).days / 7 + 1)
    week_base = get_year_week(today.year, week)
    week_base_plus_7 = week_base + datetime.timedelta(6)
    context = {'week': week, 'week_one': week_base.strftime('%Y-%m-%d')}
    user = request.user
    task_set = user.specifictask_set.all().filter(start_time__lte=week_base).filter(end_time__lte=week_base_plus_7)
    week_data = []
    for task in task_set:
        for week_day_time in task.weekdaytime_set:
            week_data[week_day_time.day].append(task)
            pass
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


