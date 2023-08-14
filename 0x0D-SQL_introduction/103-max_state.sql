-- This script calculates the maximum temperature for each state and displays the results ordered by state name

SELECT state, MAX(temperature) AS max_temp
FROM temperatures
GROUP BY state
ORDER BY state;
