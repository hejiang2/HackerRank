/*
CASE input_expression   
     WHEN when_expression THEN result_expression [ ...n ]   
     [ ELSE else_result_expression ]   
END  
*/

SELECT CASE
    WHEN (A + B > C AND  B + C > A AND A + C > B) THEN 
    CASE
        WHEN (A = B OR A = C OR B = C) THEN 
        CASE
            WHEN (A = B AND B = C) THEN "Equilateral"
            ELSE "Isosceles"
        END
        ELSE "Scalene"
    END
    ELSE "Not A Triangle"
END
FROM TRIANGLES;    