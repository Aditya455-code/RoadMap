#INNER JOIN
SELECT c.id ,c.name
FROM customer c
INNER JOIN orders o
ON c.id=o.customer_id;


#LEFT JOIN
SELECT c.id ,c.name
FROM customer c
LEFT JOIN orders o
ON c.id=o.customer_id;


#RIGHT JOIN
SELECT c.id ,c.name
FROM customer c
LEFT JOIN orders o
ON c.id=o.customer_id;


#FULL OUTER JOIN
SELECT c.id ,c.name
FROM customer c
FULL OUTER JOIN orders o
ON c.id=o.customer_id;


#CROSS JOIN
SELECT c.id ,c.name
FROM customer c
CROSS JOIN orders o;
 


#CUSTOMERS WHO DID'NT ORDER ANYTHING
SELECT c.id ,c.name
FROM customer c
LEFT JOIN orders o
ON c.id=o.customer_id
WHERE o.customer_id IS NULL;

#ALL DATA FROM BOTH TABLES INCLUDING DUPLICATES
SELECT names FROM customer
UNION ALL
SELECT name FROM old_cuatomer;