-- 문제: 전화번호에 '033'이 포함된 공장 조회
-- DB: Oracle
-- 핵심: INSTR 함수, 명령어 사용순서, 명령어 적용 순서

SELECT factory_id, factory_name, address FROM FOOD_FACTORY where instr(address, '강원도') > 0 ORDER BY FACTORY_ID ASC