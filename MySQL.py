select AVG(prod_price) as avg_price
FROM products
where vend_id = 'id1'

select COUNT(*) as num_cust
FROM Customers;

select count(cust_email) as num_cust
from customers;


select cust_id,count(*) as orders
from orders
group by cust_id
having count(*) >= 2
having  count(*) >=60



select order_num,count(*) as items
from orderitems
group by orderitem
having count(*) >= 3
order by items,orders_NUm
