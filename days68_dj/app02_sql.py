import os

if __name__ == '__main__':
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "days68_dj.settings")
    import django

    django.setup()

    from app02 import models

    from django.db.models import Avg

    #我们使用原生SQL语句，按照部分分组求平均工资：
    # SELECT d.name,avg(salary) as avg FROM	app02_employee e JOIN app02_dept d ON e.dept_id = d.id GROUP BY	dept_id
    #ORM查询：
    res = models.Dept.objects.annotate(avg=Avg('employee__salary')).values('name', 'avg')


    # res = models.Employee.objects.annotate(avg=Avg('salary')).values('avg')


    print(res)
