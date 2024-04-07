SELECT student_name, ROUND(AVG(grade), 1) AS avg_grade
FROM students s
JOIN grades g ON s.id = g.student_id
AND subject_id = (
SELECT id
FROM subjects
WHERE subject_name = 'World History Since'
)
GROUP BY student_name
ORDER BY avg_grade DESC
LIMIT 1;