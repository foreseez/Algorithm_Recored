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

