SELECT m.member_name, r.review_text, to_char(r.review_date,'yyyy-mm-dd') as review_date
from rest_review r
join member_profile m
on m.member_id  = r.member_id

where r.member_id = 
    (select member_id
    from (select member_id, count(*) as cnt
        from rest_review
        group by member_id
        order by cnt desc)
    where rownum = 1)
order by to_char(r.review_date,'yyyy-mm-dd') asc, r.review_text asc