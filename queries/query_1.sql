SELECT student_name, ROUND(AVG(grade), 1) AS average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
GROUP BY student_name
ORDER BY average_grade DESC
LIMIT 5;