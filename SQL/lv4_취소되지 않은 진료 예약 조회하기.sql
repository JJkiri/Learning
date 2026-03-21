-- 
-- condition 1) 2022-04-13, 2) APNT_CNCL_YN = 'N' 3) MCDP_CD = 'CS'

SELECT a.apnt_no,p.pt_name,p.pt_no,a.mcdp_cd,d.dr_name, a.apnt_ymd
from
appointment a
join patient p on  a.pt_no = p.pt_no
join doctor d on d.dr_id = a.mddr_id

where to_char(a.apnt_ymd,'yyyy-mm-dd') = '2022-04-13'
and a.APNT_CNCL_YN = 'N'
and a.MCDP_CD = 'CS'

order by a.apnt_ymd asc