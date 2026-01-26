--lv2_string_date
-- upper,lower
SELECT animal_id, name
from ANIMAL_INS
--where name like '%el%' or '%El%' or '%eL%' or '%EL%'
-- 'el' in name & capital letter & small letter
-- 1) name column >> upper or lower 적용 후 비교
-- 2) REGEXP 사용
where  lower(name) like '%el%' and animal_type = 'Dog'

order by name