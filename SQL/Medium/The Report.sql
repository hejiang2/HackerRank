** join on value between value_min and value_max
SELECT CASE WHEN G.Grade < 8 THEN NULL ELSE S.Name END AS Name, G.Grade, S.Marks
FROM Students S
JOIN Grades G
ON S.Marks BETWEEN G.Min_Mark and G.Max_Mark
** ON S.Marks >= G.Min_Mark AND S.Marks <= G.Max_Mark
ORDER BY G.Grade DESC, Name, S.Marks;