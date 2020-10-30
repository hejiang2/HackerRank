# X^2 + X^2 = Distance^2
# X would be defined as the difference between the two x coordinates of P1 and P2. 
# Y would be defined as the difference between the two y coordinates of P1 and P2.
SELECT CAST(SQRT(POWER((a - b), 2) + POWER((c - d), 2)) AS DECIMAL(8,4))
FROM 
(SELECT MIN(LAT_N) a, MAX(LAT_N) b, MIN(LONG_W) c, MAX(LONG_W) d
FROM STATION) AS ED;