-- column: flaver
-- 조건: july total_order + first_half total order ranked in top 3 
-- same flavor has different shipment_id, need to grouping
-- from *조건 subquery) & row(num? id? just row?) >= 3?

--select flavor
--from
select flavor
from(
select j.flavor, j.total+h.total as total2
from
    (select flavor, sum(total_order) as total
    from july
    group by flavor) j
join
    (select flavor, sum(total_order) as total
    from first_half
    group by flavor) h
on j.flavor = h.flavor
order by total2 desc)
where rownum <= 3