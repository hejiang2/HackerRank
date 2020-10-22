/*
Manhattan distance: The distance between two points measured along axes at right angles. In a plane with p1 at (x1, y1) and p2 at (x2, y2), it is |x1 - x2| + |y1 - y2|.
*/

SELECT CAST(ABS(a-c) + ABS(b-d) AS DECIMAL(18,4)) 
FROM
(SELECT MIN(LAT_N) AS a, MIN(LONG_W) AS b, MAX(LAT_N) AS c, MAX(LONG_W) AS d
FROM STATION) AS DISTANCE;