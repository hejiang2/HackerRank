/*
The returned type of the AVG() depends on the evaluated type of the expression passed to the function.
For example, if you want your result to be float, you need to ensure your column or expression type is float.
*/
SELECT CONVERT(INTEGER, 
  CEILING( 
      AVG(CONVERT(FLOAT, SALARY)) - AVG(CONVERT(FLOAT, REPLACE(SALARY, '0', '')))
    )
)
FROM EMPLOYEES;