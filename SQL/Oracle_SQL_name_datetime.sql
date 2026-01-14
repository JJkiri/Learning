-- 문제: 등록일이 가장 최근인 동물의 이름을 조회
-- 주제: subquerry
-- 포인트: where절에서 집계함수의 조건 적용 기초


select name from animal_ins where datetime = (select min(datetime) from animal_ins)