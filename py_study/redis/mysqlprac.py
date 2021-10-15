from mysqltools import MysqlConnect

# sql = ""
# r = MysqlConnect().connect(sql)
# print(r)

# 1.找出以 a、b、s开始的员工信息
# sql = """select * from emp where ename regexp '^[abs]';"""
# sql = """select * from emp where left(ename, 1) in ('a','b','s');"""

# 2.返回员工的详细信息并按姓名排序
# sql = """select * from emp order by ename;"""

# 3.返回员工的信息并按工作降序工资升序排列
# sql = """select * from emp order by job desc,sal;"""

# 4.返回拥有员工的部门名、部门号
# sql = """select dname,dept.deptno from emp inner join dept on emp.deptno=dept.deptno group by dept.deptno; """

# 5.工资高于smith的员工信息
# sql = """select * from emp where sal > (select sal from emp where ename='smith');"""

# 6.返回员工和所属经理的姓名
# sql = """select emp.ename, e.ename as manager_name from emp inner join emp as e on e.empno=emp.mgr; """

# 7.返回雇员的雇佣日期早于其经理雇佣日期的员工及其经理姓名
# sql = """select emp.ename,e.ename as manager_name from emp inner join emp as e on e.empno=emp.mgr
# where emp.hiredate<e.hiredate;"""

# 8.返回员工姓名及其所在的部门名称
# sql = """select ename,dname from emp inner join dept on emp.deptno=dept.deptno;"""

# 9.返回从事clerk工作的员工姓名和所在部门名称
# sql = """select ename,dname from emp inner join dept on emp.deptno=dept.deptno where job='clerk';"""
# 10.返回部门号及其本部门的最低工资
# sql = """select emp.deptno,min(sal) from emp inner join dept on emp.deptno=dept.deptno group by dept.deptno;"""
# 11.返回销售部（sales）所有员工的姓名
# sql = """select ename from emp inner join dept on emp.deptno=dept.deptno where dname='sales';"""
# 12.返回与scott从事相同工作的员工
# sql = """select * from emp where job = (select job from emp where ename='scott') and ename!='scott';"""
# 13.返回员工的详细信息（包括部门名称及部门地址）
sql = """select emp.*,dname,loc from emp inner join dept on emp.deptno=dept.deptno;"""
# 14.返回员工工作及其从事此工作的最低工资
# sql = """select job, min(sal) from emp group by job; """
# 15.返回工资处于第四级别的员工的姓名
# sql = """select ename from emp,salgrade where sal between lowsal and hisal and grade=4;"""
# 16.返回工资为二等级的职员姓名、部门所在地、和二等级的最低工资和最高工资
# sql = """select ename,loc,lowsal,hisal from emp,dept,salgrade where emp.deptno=dept.deptno
# and sal between lowsal and hisal and grade=2;"""
# 17.工资等级高于smith的员工信息
# sql = """select emp.*,grade from emp ,salgrade where sal between lowsal and hisal and grade>(
# select grade from emp ,salgrade where sal between lowsal and hisal and ename='smith')"""
try:
    for i in MysqlConnect().connect(sql):
        print(i)
except Exception as e:
    print(e)
