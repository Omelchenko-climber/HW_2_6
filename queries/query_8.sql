SELECT teacher_name, subject_name, ROUND(AVG(grade), 1) AS avg_grade
FROM teachers t
JOIN subjects s ON t.id = s.teacher_id
AND teacher_name = "Lucas Fletcher"
JOIN grades g ON s.id = g.subject_id
GROUP BY teacher_name, subject_name
ORDER BY avg_grade DESC
;