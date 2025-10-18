from django.shortcuts import render
from app.models import *
# Create your views here.
from django.http import HttpResponse
from django.db.models import Q

def insert_dept(request):
    dno=int(input('enter Dept_no'))
    TDO=Dept.objects.get_or_create(dept_no=dno)
    na=input('Enter the Deptname')
    lo=input('Enter the Loctaion')
    TDO=Dept.objects.get_or_create(dname=na,loc=lo)
    if TDO[1]:
        return HttpResponse('Dept is created')
    else:
        return HttpResponse('Dept is already present')

def insert_emp(request):
    dno=int(input('enter Dept_no'))
    LDO=Dept.objects.filter(dept_no=dno)
    if LDO:
        DO=LDO[0]

        eno=int(input('Enter Employee_no'))
        ena=input('enter Employee_name')
        job=input('enter Job')
        hire=input('Enter Hiredate')
        sal=float(input('enter salary'))
        com=input('enter commission')
        if com:
            com=float(com)
        else:
            com=None

        mgr_empno=input('enter manager emp_no')
        if mgr_empno:
            mgr_empno=Emp.objects.get_or_create(empno=int(mgr_empno))
        else:
            mgr_empno=None


        TEO=Emp.objects.get_or_create(empno=eno,ename=ena,job= job,mgr=mgr_empno,hiredate=hire,sal=sal,comm=com)
        if TEO[1]:
            return HttpResponse('Employee created successfully.')
        else:
            return HttpResponse('Employee already exists.')
    
    else:
        return HttpResponse('doesnt exist')

def display_emp(request):
    QLEO=Emp.objects.all()
    QLEO=Emp.objects.filter(job='Manager',dept_no=20)
    QLEO=Emp.objects.filter(Q(job='Manager')|Q(dept_no=30))
    QLEO=Emp.objects.filter(ename__startswith='s',sal__gte=1000)
    QLEO=Emp.objects.filter(hiredate__year__gte=2025)
    QLEO=Emp.objects.filter(hiredate__year__lt=2025)

    d={'QLEO':QLEO}
    return render(request,'display_emp.html',d)

def display_dept(request):
    QLDO=Dept.objects.all()
    d={'QLDO':QLDO}
    return render(request,'display_dept.html',d)

#Select_related
def EmpTODeptjoin(request):
    QLEDO=Emp.objects.all().select_related('dept_no')
    QLEDO=Emp.objects.filter(sal__gt=1000).select_related('dept_no')
    QLEDO=Emp.objects.filter(job='Clerk').select_related('dept_no')
    QLEDO=Emp.objects.select_related('dept_no').filter(dept_no__loc='Dallas')
    QLEDO=Emp.objects.select_related('dept_no').filter(empno__gte=102)
    QLEDO=Emp.objects.select_related('dept_no').filter(empno__gt=103)
    QLEDO=Emp.objects.select_related('dept_no').filter(ename='Smith')
    QLEDO=Emp.objects.select_related('dept_no').filter(ename__startswith='S')
    QLEDO=Emp.objects.select_related('dept_no').filter(dept_no__dname__endswith='s')
    QLEDO=Emp.objects.select_related('dept_no').filter(dept_no__loc__regex='r')
    QLEDO=Emp.objects.select_related('dept_no').filter(dept_no__dept_no__lt=30)
    QLEDO=Emp.objects.select_related('dept_no').filter(dept_no__dept_no__gte=30,ename__startswith='s')
    QLEDO=Emp.objects.select_related('dept_no').filter(Q(sal__lt=800)|Q(ename__contains='o'))
    QLEDO=Emp.objects.select_related('dept_no').filter(job='Manager',dept_no__gte=20)
    QLEDO=Emp.objects.select_related('dept_no').filter(ename='King',dept_no__dept_no=10)
    QLEDO=Emp.objects.select_related('dept_no').filter(Q(comm__isnull=True)|Q(ename__startswith='S'))

    d={'QLEDO':QLEDO}
    return render(request,'EmpTODeptjoin.html',d)


def empmgr(request):
    QLEMO=Emp.objects.all().select_related('mgr')
    # QLEMO=Emp.objects.all().select_related('mgr').filter(ename__startswith='S')
    # QLEMO=Emp.objects.all().select_related('mgr').filter(ename__startswith='S',mgr__isnull=False)
    # QLEMO=Emp.objects.all().select_related('mgr').filter(mgr__isnull=True,comm__isnull=False)
    # QLEMO=Emp.objects.all().select_related('mgr').filter(job='Analyst',ename='Ford')
    # QLEMO=Emp.objects.all().select_related('mgr').filter(dept_no=10,mgr__isnull=True)
    # QLEMO=Emp.objects.all().select_related('mgr').filter(Q(ename__startswith='S') | Q(mgr__isnull=True))
    # QLEMO=Emp.objects.all().select_related('mgr').filter(ename__endswith='t',mgr__isnull=False)
    # QLEMO=Emp.objects.all().select_related('mgr').filter(ename__contains='r',comm__isnull=False)
    # QLEMO=Emp.objects.all().select_related('mgr').filter(ename__startswith='S',dept_no__lte=30)
    # QLEMO=Emp.objects.all().select_related('mgr').filter(empno=101)
    # QLEMO=Emp.objects.all().select_related('mgr').filter(sal__gt=200,ename__startswith='S')
    # QLEMO=Emp.objects.all().select_related('mgr').filter(sal__lte=800,ename__startswith='S')
    # QLEMO=Emp.objects.all().select_related('mgr').filter(job='Clerk',dept_no=30)
    # QLEMO=Emp.objects.all().select_related('mgr').filter(Q(job='Salesman')|Q(ename='Allen'))

    
    d={'QLEMO':QLEMO}
    return render(request,'empmgr.html',d)


def empdeptmgr(request):
    QLEDMO=Emp.objects.all().select_related('dept_no','mgr')
    # QLEDMO=Emp.objects.all().select_related('dept_no','mgr').filter(dept_no=10)
    # QLEDMO=Emp.objects.all().select_related('dept_no','mgr').filter(dept_no__dname__contains='R')
    # QLEDMO=Emp.objects.all().select_related('dept_no','mgr').filter(mgr__isnull=True,dept_no__dname='Accounting')
    # QLEDMO=Emp.objects.all().select_related('dept_no','mgr').filter(Q(dept_no__dname__startswith='S') | Q(dept_no__loc='New York'))
    # QLEDMO=Emp.objects.all().select_related('dept_no','mgr').filter(comm__isnull=True).exclude(job='Manager')
    # QLEDMO=Emp.objects.all().select_related('dept_no','mgr').filter(dept_no__loc='Dallas').exclude(job='Analyst')
    # QLEDMO=Emp.objects.all().select_related('dept_no','mgr').filter(sal__lte=2000,dept_no=20)
    # QLEDMO=Emp.objects.all().select_related('dept_no','mgr').filter(Q(ename__startswith='A') | Q(ename__endswith='N'))
    # QLEDMO=Emp.objects.all().select_related('dept_no','mgr').filter(sal__range=(1000,2500))
    # QLEDMO=Emp.objects.all().select_related('dept_no','mgr').filter(Q(comm__gt=500) | Q(sal__lt=1500))
    # QLEDMO=Emp.objects.all().select_related('dept_no','mgr').filter(sal__range=(1500,3500), job__startswith='S')
    # QLEDMO=Emp.objects.all().select_related('dept_no','mgr').filter(comm__isnull=True).exclude(dept_no__loc='New York')
    # QLEDMO=Emp.objects.all().select_related('dept_no','mgr').filter(dept_no__dname__startswith='A', comm__gt=0)
    # QLEDMO=Emp.objects.all().select_related('dept_no','mgr').filter(mgr__isnull=True)
    # QLEDMO=Emp.objects.all().select_related('dept_no','mgr').exclude(job__in=['Manager','President']).filter(sal__lt=2000)
    # QLEDMO=Emp.objects.all().select_related('dept_no','mgr').filter(dept_no__dname='Sales',comm__gt=200)

    d={'QLEDMO':QLEDMO}
    return render(request,'empdeptmgr.html',d)





#Pre_fetch related

