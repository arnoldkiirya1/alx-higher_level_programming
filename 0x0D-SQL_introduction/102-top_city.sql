-- This script calculates the average temperature by city for July and August and displays the top 3 cities with the highest temperatures

SELECT city, AVG(temperature) AS avg_temp
FROM temperatures
WHERE MONTH(date) IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
