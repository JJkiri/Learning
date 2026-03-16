SELECT a.Author_id, a.Author_name, b.Category, sum(s.Sales * b.price) as TOTAL_SALES--sum(집계)을 제외한 모든 함수가 gruop by 대상
from author a
join book b on a.author_id = b.author_id
join book_sales s on b.book_id = s.book_id
where to_char(s.sales_date, 'yyyy-mm') = '2022-01'
group by a.Author_id, a.Author_name, b.Category
order by a.Author_id, b.Category desc