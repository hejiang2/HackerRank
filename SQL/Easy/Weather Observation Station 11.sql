SELECT DISTINCT CITY
FROM STATION
WHERE CITY NOT LIKE '[aeiou]%[aeiou]';
-- not start with vowels AND end with vowels, only start/end is fine