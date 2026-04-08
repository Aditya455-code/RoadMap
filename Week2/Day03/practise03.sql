#Running total of sales month by month
SELECT month,sales,
   SUM(sales) OVER (ORDER BY month) AS running_total
FROM monthly_sales;


#The salary difference between an employee and the average of their department
SELECT 
 name,
 department,
 salary,
 AVG(salary) OVER(ORDER BY department) AS dept_avg,
 salary-AVG(salary) OVER (PARTITION BY department)AS diff
FROM employees



 
