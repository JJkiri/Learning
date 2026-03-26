
SELECT extract(year from o.sales_date) as year, extract(month from o.sales_date) as month, u.gender as gender, count(distinct u.user_id)as users
from user_info u
join online_sale o on u.user_id = o.user_id

where u.gender is not null

group by extract(year from o.sales_date), extract(month from o.sales_date), u.gender
order by extract(year from o.sales_date), extract(month from o.sales_date), u.gender