SELECT earnings, COUNT(*)
FROM 
(SELECT salary*months AS earnings
FROM Employee) AS E
GROUP BY earnings
ORDER BY earnings DESC
LIMIT 1;