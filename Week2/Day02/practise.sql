#SALARY HIGHER THAN THE AVERAGE OF THE DEPARTMENT
SELECT department,AVG(salary) as dept_avg
FROM employees 
GROUP BY department
HAVING AVG(salary)>(SELECT AVG(salary) FROM employee);



#TOP 3 PRODUCTS SOLD IN EACH REGION
WITH ranked_sales AS (
   SELECT
    product,
    region,
    quantity,
    ROW_NUMBER() OVER (PARTITION BY region ORDER BY quantity DESC) AS rank
     FROM sales
)
SELECT product,region,quantity
FROM ranked_sales
WHERE rank<=3;



