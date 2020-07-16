

# LeetCode MySQL 刷题记录

## [游戏玩法分析 II](https://leetcode-cn.com/problems/game-play-analysis-ii/)

```
Table: Activity

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| player_id    | int     |
| device_id    | int     |
| event_date   | date    |
| games_played | int     |
+--------------+---------+
(player_id, event_date) 是这个表的两个主键
这个表显示的是某些游戏玩家的游戏活动情况
每一行是在某天使用某个设备登出之前登录并玩多个游戏（可能为0）的玩家的记录
请编写一个 SQL 查询，描述每一个玩家首次登陆的设备名称

查询结果格式在以下示例中：

Activity table:
+-----------+-----------+------------+--------------+
| player_id | device_id | event_date | games_played |
+-----------+-----------+------------+--------------+
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-05-02 | 6            |
| 2         | 3         | 2017-06-25 | 1            |
| 3         | 1         | 2016-03-02 | 0            |
| 3         | 4         | 2018-07-03 | 5            |
+-----------+-----------+------------+--------------+

Result table:
+-----------+-----------+
| player_id | device_id |
+-----------+-----------+
| 1         | 2         |
| 2         | 3         |
| 3         | 1         |
+-----------+-----------+
```

```

select player_id,device_id 
from  
Activity a 
where (a.player_id,a.event_date) in 
(
    select
     player_id,min(event_date)
     from Activity
      group by player_id
    )
```

## 从不订购的客户

```
某网站包含两个表，Customers 表和 Orders 表。编写一个 SQL 查询，找出所有从不订购任何东西的客户。

Customers 表：

+----+-------+
| Id | Name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+
Orders 表：

+----+------------+
| Id | CustomerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+
例如给定上述表格，你的查询应返回：

+-----------+
| Customers |
+-----------+
| Henry     |
| Max       |
+-----------+

```

```
/*select customers.name  as 'Customers'
from 
customers
where customers.id not in
 (
    select customerid 
    from
    orders

);
*/


select a.Name as Customers
from Customers as a
left join orders as b 
on a.id = b.customerid
where b.customerid is null

```

## [有趣的电影](https://leetcode-cn.com/problems/not-boring-movies/)

```
作为该电影院的信息部主管，您需要编写一个 SQL查询，找出所有影片描述为非 boring (不无聊) 的并且 id 为奇数 的影片，结果请按等级 rating 排列。

 

例如，下表 cinema:

+---------+-----------+--------------+-----------+
|   id    | movie     |  description |  rating   |
+---------+-----------+--------------+-----------+
|   1     | War       |   great 3D   |   8.9     |
|   2     | Science   |   fiction    |   8.5     |
|   3     | irish     |   boring     |   6.2     |
|   4     | Ice song  |   Fantacy    |   8.6     |
|   5     | House card|   Interesting|   9.1     |
+---------+-----------+--------------+-----------+
对于上面的例子，则正确的输出是为：

+---------+-----------+--------------+-----------+
|   id    | movie     |  description |  rating   |
+---------+-----------+--------------+-----------+
|   5     | House card|   Interesting|   9.1     |
|   1     | War       |   great 3D   |   8.9     |

```

```
select id ,movie ,description,rating
from 
cinema
where description != 'boring'
and mod(id,2)=1
order by rating DESC
```

## 至少有五名直接下属的经理

```
Employee 表包含所有员工和他们的经理。每个员工都有一个 Id，并且还有一列是经理的 Id。

+------+----------+-----------+----------+
|Id    |Name 	  |Department |ManagerId |
+------+----------+-----------+----------+
|101   |John 	  |A 	      |null      |
|102   |Dan 	  |A 	      |101       |
|103   |James 	  |A 	      |101       |
|104   |Amy 	  |A 	      |101       |
|105   |Anne 	  |A 	      |101       |
|106   |Ron 	  |B 	      |101       |
+------+----------+-----------+----------+
给定 Employee 表，请编写一个SQL查询来查找至少有5名直接下属的经理。对于上表，您的SQL查询应该返回：

+-------+
| Name  |
+-------+
| John  |
+-------+
```

```
/*
select 
    Name
from
    Employee
where Id
     in 
(
    select ManagerId
    from Employee
    group by ManagerId
    having  Count(ManagerId) >= 5
)
*/

select  
    name 
    from 
     Employee as t1 join
     (
         select ManagerId
         from 
         Employee
         group by ManagerId
         having Count(ManagerId) >= 5
     ) as t2

     on t1.Id = t2.ManagerId
```

'GROUP BY 子句必须出现在WHERE 子句之后，ORDER BY 子句之前。'

```
表: Candidate

+-----+---------+
| id  | Name    |
+-----+---------+
| 1   | A       |
| 2   | B       |
| 3   | C       |
| 4   | D       |
| 5   | E       |
+-----+---------+  
表: Vote

+-----+--------------+
| id  | CandidateId  |
+-----+--------------+
| 1   |     2        |
| 2   |     4        |
| 3   |     3        |
| 4   |     2        |
| 5   |     5        |
+-----+--------------+
id 是自动递增的主键，
CandidateId 是 Candidate 表中的 id.
请编写 sql 语句来找到当选者的名字，上面的例子将返回当选者 B.

+------+
| Name |
+------+
| B    |
+------+


select Name 
from 
(
    select CandidateId as id
    from Vote
    group by CandidateId
    order by count(id) desc
    limit 1
) as winner join Candidate
on Candidate.id = winner.id
```

## 员工奖金

```
选出所有 bonus < 1000 的员工的 name 及其 bonus。

Employee 表单

+-------+--------+-----------+--------+
| empId |  name  | supervisor| salary |
+-------+--------+-----------+--------+
|   1   | John   |  3        | 1000   |
|   2   | Dan    |  3        | 2000   |
|   3   | Brad   |  null     | 4000   |
|   4   | Thomas |  3        | 4000   |
+-------+--------+-----------+--------+
empId 是这张表单的主关键字
Bonus 表单

+-------+-------+
| empId | bonus |
+-------+-------+
| 2     | 500   |
| 4     | 2000  |
+-------+-------+
empId 是这张表单的主关键字
输出示例：

+-------+-------+
| name  | bonus |
+-------+-------+
| John  | null  |
| Dan   | 500   |
| Brad  | null  |
+-------+-------+
```

```
select e.name,b.bonus
from 
Employee e left join Bonus b
on e.empId = b.empId
where bonus is null or bonus < 2000
```

## 查询回答率最高的问题

```
从 survey_log 表中获得回答率最高的问题，survey_log 表包含这些列：id, action, question_id, answer_id, q_num, timestamp。

id 表示用户 id；action 有以下几种值："show"，"answer"，"skip"；当 action 值为 "answer" 时 answer_id 非空，而 action 值为 "show" 或者 "skip" 时 answer_id 为空；q_num 表示当前会话中问题的编号。

请编写 SQL 查询来找到具有最高回答率的问题。

 

示例：

输入：
+------+-----------+--------------+------------+-----------+------------+
| id   | action    | question_id  | answer_id  | q_num     | timestamp  |
+------+-----------+--------------+------------+-----------+------------+
| 5    | show      | 285          | null       | 1         | 123        |
| 5    | answer    | 285          | 124124     | 1         | 124        |
| 5    | show      | 369          | null       | 2         | 125        |
| 5    | skip      | 369          | null       | 2         | 126        |
+------+-----------+--------------+------------+-----------+------------+
输出：
+-------------+
| survey_log  |
+-------------+
|    285      |
+-------------+
解释：
问题 285 的回答率为 1/1，而问题 369 回答率为 0/1，因此输出 285 。
```

```
select Answer_cnt.question_id as survey_log 
from 
(select question_id,count(*) as answer_cnt
from survey_log 
where action = "answer"
group by question_id ) as Answer_cnt
 
 join 

(select question_id,count(*) as  action_cnt 
from survey_log
where action = "show"
group by question_id 
) as Show_cnt 

on Answer_cnt.question_id = Show_cnt.question_id
order by  Answer_cnt.answer_cnt / Show_cnt.action_cnt  desc
limit 1

#  注意 大小写注意 show_cnt 和Show_cnt 
```

![image-20200710144556254](/Users/zengyujian/Library/Application Support/typora-user-images/image-20200710144556254.png)

 



## [统计各专业学生人数](https://leetcode-cn.com/problems/count-student-number-in-departments/)

```
一所大学有 2 个数据表，分别是 student 和 department ，这两个表保存着每个专业的学生数据和院系数据。

写一个查询语句，查询 department 表中每个专业的学生人数 （即使没有学生的专业也需列出）。

将你的查询结果按照学生人数降序排列。 如果有两个或两个以上专业有相同的学生数目，将这些部门按照部门名字的字典序从小到大排列。

student 表格如下：

| Column Name  | Type      |
|--------------|-----------|
| student_id   | Integer   |
| student_name | String    |
| gender       | Character |
| dept_id      | Integer   |
其中， student_id 是学生的学号， student_name 是学生的姓名， gender 是学生的性别， dept_id 是学生所属专业的专业编号。

department 表格如下：

| Column Name | Type    |
|-------------|---------|
| dept_id     | Integer |
| dept_name   | String  |
dept_id 是专业编号， dept_name 是专业名字。

这里是一个示例输入：
student 表格：

| student_id | student_name | gender | dept_id |
|------------|--------------|--------|---------|
| 1          | Jack         | M      | 1       |
| 2          | Jane         | F      | 1       |
| 3          | Mark         | M      | 2       |
department 表格：

| dept_id | dept_name   |
|---------|-------------|
| 1       | Engineering |
| 2       | Science     |
| 3       | Law         |
示例输出为：

| dept_name   | student_number |
|-------------|----------------|
| Engineering | 2              |
| Science     | 1              |
| Law         | 0              |

```

```
SELECT  dept_name,count(student_id)as student_number  #这里改成count(gender)  也可以 
FROM
	department
	left OUTER join 
	student
	on department.dept_id = student.dept_id
GROUP BY department.dept_name

ORDER BY student_number DESC,department.dept_name 
```

- 注意上面的Count 后面要跟一个分组聚合的操作group by  至于Count里面 统计那一列都可以 。group by 会自动按照分组的字段分组求和。

## 谁有最多的好友



```
在 Facebook 或者 Twitter 这样的社交应用中，人们经常会发好友申请也会收到其他人的好友申请。

 

表 request_accepted 存储了所有好友申请通过的数据记录，其中， requester_id 和 accepter_id 都是用户的编号。

 

| requester_id | accepter_id | accept_date|
|--------------|-------------|------------|
| 1            | 2           | 2016_06-03 |
| 1            | 3           | 2016-06-08 |
| 2            | 3           | 2016-06-08 |
| 3            | 4           | 2016-06-09 |
写一个查询语句，求出谁拥有最多的好友和他拥有的好友数目。对于上面的样例数据，结果为：

| id | num |
|----|-----|
| 3  | 3   |
注意：

保证拥有最多好友数目的只有 1 个人。
好友申请只会被接受一次，所以不会有 requester_id 和 accepter_id 值都相同的重复记录。
 

解释：

编号为 '3' 的人是编号为 '1'，'2' 和 '4' 的好友，所以他总共有 3 个好友，比其他人都多。

```



```
SELECT rid as id ,count(1) as num
FROM
(
SELECT 
     R.request_id as rid ,R.accepted_id as aid 
FROM  
	  request_accepted as R 
Union ALL

SELECT 
     A.accepted_id as rid ,A.request_id as aid 
 FROM
		request_accepted as A 
		)  as TX
		
		group by rid 
		order by num DESC
		
		LIMIT 1
```

```
描述

给定 3 个表： salesperson， company， orders。
输出所有表 salesperson 中，没有向公司 'RED' 销售任何东西的销售员。

示例：
输入

表： salesperson

+----------+------+--------+-----------------+-----------+
| sales_id | name | salary | commission_rate | hire_date |
+----------+------+--------+-----------------+-----------+
|   1      | John | 100000 |     6           | 4/1/2006  |
|   2      | Amy  | 120000 |     5           | 5/1/2010  |
|   3      | Mark | 65000  |     12          | 12/25/2008|
|   4      | Pam  | 25000  |     25          | 1/1/2005  |
|   5      | Alex | 50000  |     10          | 2/3/2007  |
+----------+------+--------+-----------------+-----------+
表 salesperson 存储了所有销售员的信息。每个销售员都有一个销售员编号 sales_id 和他的名字 name 。

表： company

+---------+--------+------------+
| com_id  |  name  |    city    |
+---------+--------+------------+
|   1     |  RED   |   Boston   |
|   2     | ORANGE |   New York |
|   3     | YELLOW |   Boston   |
|   4     | GREEN  |   Austin   |
+---------+--------+------------+
表 company 存储了所有公司的信息。每个公司都有一个公司编号 com_id 和它的名字 name 。

表： orders

+----------+------------+---------+----------+--------+
| order_id | order_date | com_id  | sales_id | amount |
+----------+------------+---------+----------+--------+
| 1        |   1/1/2014 |    3    |    4     | 100000 |
| 2        |   2/1/2014 |    4    |    5     | 5000   |
| 3        |   3/1/2014 |    1    |    1     | 50000  |
| 4        |   4/1/2014 |    1    |    4     | 25000  |
+----------+----------+---------+----------+--------+
表 orders 存储了所有的销售数据，包括销售员编号 sales_id 和公司编号 com_id 。

输出

+------+
| name | 
+------+
| Amy  | 
| Mark | 
| Alex |
+------+
解释

根据表 orders 中的订单 '3' 和 '4' ，容易看出只有 'John' 和 'Pam' 两个销售员曾经向公司 'RED' 销售过。

所以我们需要输出表 salesperson 中所有其他人的名字。
```

Select case sval when 1 then 'nan' else 'nv' end as sval from where sval !=' '

```
/*select s.name 
from 
salesperson s 
where s.sales_id not in 
(   select o.sales_id 
from
orders o  
left join 
company c  
on o.com_id = c.com_id 
where c.name = 'RED'

)
*/

SELECT
    S.name
FROM
    salesperson S
    LEFT JOIN
    orders O ON S.sales_id = O.sales_id
    LEFT JOIN
    company C ON O.com_id = C.com_id
GROUP BY
    S.name
HAVING
    SUM(IF(C.name = 'RED', 1, 0))  = 0
ORDER BY
    S.sales_id


```

```
 平均工资：部门与公司比较
给如下两个表，写一个查询语句，求出在每一个工资发放日，每个部门的平均工资与公司的平均工资的比较结果 （高 / 低 / 相同）。

 

表： salary

| id | employee_id | amount | pay_date   |
|----|-------------|--------|------------|
| 1  | 1           | 9000   | 2017-03-31 |
| 2  | 2           | 6000   | 2017-03-31 |
| 3  | 3           | 10000  | 2017-03-31 |
| 4  | 1           | 7000   | 2017-02-28 |
| 5  | 2           | 6000   | 2017-02-28 |
| 6  | 3           | 8000   | 2017-02-28 |
 

employee_id 字段是表 employee 中 employee_id 字段的外键。

 

| employee_id | department_id |
|-------------|---------------|
| 1           | 1             |
| 2           | 2             |
| 3           | 2             |
 

对于如上样例数据，结果为：

 

| pay_month | department_id | comparison  |
|-----------|---------------|-------------|
| 2017-03   | 1             | higher      |
| 2017-03   | 2             | lower       |
| 2017-02   | 1             | same        |
| 2017-02   | 2             | same        |
 

解释

 

在三月，公司的平均工资是 (9000+6000+10000)/3 = 8333.33...

 

由于部门 '1' 里只有一个 employee_id 为 '1' 的员工，所以部门 '1' 的平均工资就是此人的工资 9000 。因为 9000 > 8333.33 ，所以比较结果是 'higher'。

 

第二个部门的平均工资为 employee_id 为 '2' 和 '3' 两个人的平均工资，为 (6000+10000)/2=8000 。因为 8000 < 8333.33 ，所以比较结果是 'lower' 。

 

在二月用同样的公式求平均工资并比较，比较结果为 'same' ，因为部门 '1' 和部门 '2' 的平均工资与公司的平均工资相同，都是 7000 。


```

```
计算公司每个月的平均工资
MySQL 有一个内置函数 avg() 获得一列数字的平均值。同时我们需要将 pay_date 列按一定格式输出以便后面使用。
sql

select avg(amount) as company_avg,  date_format(pay_date, '%Y-%m') as pay_month
from salary
group by date_format(pay_date, '%Y-%m')
;
company_avg	pay_month
7000.0000	2017-02
8333.3333	2017-03
计算每个部门每个月的平均工资
为了实现这个目标，我们将 salary 表和 employee 表用条件 salary.employee_id = employee.id 连接起来。
sql

select department_id, avg(amount) as department_avg, date_format(pay_date, '%Y-%m') as pay_month
from salary
join employee on salary.employee_id = employee.employee_id
group by department_id, pay_month
;
department_id	department_avg	pay_month
1	7000.0000	2017-02
1	9000.0000	2017-03
2	7000.0000	2017-02
2	8000.0000	2017-03
将 2 中的表和之前的公司数据作比较并求出结果
如果没用过 MySQL 的流控制语句 case...when... 那这一步会是最难的。
就像其他语言一样，MySQL 也有流控制语句，点击 这里 了解更多。

最后，将上面两个查询结合起来并用 on department_salary.pay_month = company_salary.pay_month 将它们连接。

sql

select department_salary.pay_month, department_id,
case
  when department_avg>company_avg then 'higher'
  when department_avg<company_avg then 'lower'
  else 'same'
end as comparison
from
(
  select department_id, avg(amount) as department_avg, date_format(pay_date, '%Y-%m') as pay_month
  from salary join employee on salary.employee_id = employee.employee_id
  group by department_id, pay_month
) as department_salary
join
(
  select avg(amount) as company_avg,  date_format(pay_date, '%Y-%m') as pay_month from salary group by date_format(pay_date, '%Y-%m')
) as company_salary
on department_salary.pay_month = company_salary.pay_month
;
```

## [每位学生的最高成绩](https://leetcode-cn.com/problems/highest-grade-for-each-student/)

```
表：Enrollments

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| student_id    | int     |
| course_id     | int     |
| grade         | int     |
+---------------+---------+
(student_id, course_id) 是该表的主键。

 

编写一个 SQL 查询，查询每位学生获得的最高成绩和它所对应的科目，若科目成绩并列，取 course_id 最小的一门。查询结果需按 student_id 增序进行排序。

查询结果格式如下所示：

Enrollments 表：
+------------+-------------------+
| student_id | course_id | grade |
+------------+-----------+-------+
| 2          | 2         | 95    |
| 2          | 3         | 95    |
| 1          | 1         | 90    |
| 1          | 2         | 99    |
| 3          | 1         | 80    |
| 3          | 2         | 75    |
| 3          | 3         | 82    |
+------------+-----------+-------+

Result 表：
+------------+-------------------+
| student_id | course_id | grade |
+------------+-----------+-------+
| 1          | 2         | 99    |
| 2          | 2         | 95    |
| 3          | 3         | 82    |
+------------+-----------+-------+

```

```
select student_id ,min(course_id),grade
from Enrollments
where (student_id,grade) IN (
select student_id,max(grade) as grade
from Enrollments 
group by student_id
order by student_id
)
group by student_id
order by student_id
```

## [部门工资前三高的所有员工](https://leetcode-cn.com/problems/department-top-three-salaries/)

```
Employee 表包含所有员工信息，每个员工有其对应的工号 Id，姓名 Name，工资 Salary 和部门编号 DepartmentId 。

+----+-------+--------+--------------+
| Id | Name  | Salary | DepartmentId |
+----+-------+--------+--------------+
| 1  | Joe   | 85000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
| 5  | Janet | 69000  | 1            |
| 6  | Randy | 85000  | 1            |
| 7  | Will  | 70000  | 1            |
+----+-------+--------+--------------+
Department 表包含公司所有部门的信息。

+----+----------+
| Id | Name     |
+----+----------+
| 1  | IT       |
| 2  | Sales    |
+----+----------+
编写一个 SQL 查询，找出每个部门获得前三高工资的所有员工。例如，根据上述给定的表，查询结果应返回：

+------------+----------+--------+
| Department | Employee | Salary |
+------------+----------+--------+
| IT         | Max      | 90000  |
| IT         | Randy    | 85000  |
| IT         | Joe      | 85000  |
| IT         | Will     | 70000  |
| Sales      | Henry    | 80000  |
| Sales      | Sam      | 60000  |
+------------+----------+--------+
解释：

IT 部门中，Max 获得了最高的工资，Randy 和 Joe 都拿到了第二高的工资，Will 的工资排第三。销售部门（Sales）只有两名员工，Henry 的工资最高，Sam 的工资排第二。
```

```
select 
    e1.Name as Employee ,e1.Salary,Department.Name as Department
from    
    Employee as e1,Department
    where e1.DepartmentId = Department.Id 

    and  3> ( 
        select  count(DISTINCT e2.Salary)
        from Employee as e2
        where e1.Salary < e2.Salary 
        AND e1.DepartmentId = e2.DepartmentId
    )

    order   by Department.NAME,Salary desc;

```

## 求团队的人数

```
编写一个 SQL 查询，以求得每个员工所在团队的总人数。

查询结果中的顺序无特定要求。

查询结果格式示例如下：

Employee Table:
+-------------+------------+
| employee_id | team_id    |
+-------------+------------+
|     1       |     8      |
|     2       |     8      |
|     3       |     8      |
|     4       |     7      |
|     5       |     9      |
|     6       |     9      |
+-------------+------------+
Result table:
+-------------+------------+
| employee_id | team_size  |
+-------------+------------+
|     1       |     3      |
|     2       |     3      |
|     3       |     3      |
|     4       |     1      |
|     5       |     2      |
|     6       |     2      |
+-------------+------------+
ID 为 1、2、3 的员工是 team_id 为 8 的团队的成员，
ID 为 4 的员工是 team_id 为 7 的团队的成员，
ID 为 5、6 的员工是 team_id 为 9 的团队的成员。

```

```
select Employee.employee_id,size.team_size
from 
Employee 
left join (
    select team_id,count(*) as team_size
    from Employee
    group by team_id
) as size 
on Employee.team_id = size.team_id 
```

