SELECT group_number, ROUND(AVG(grade), 1) AS avg_grade
FROM students s
JOIN grades g ON s.id = g.student_id
AND subject_id = (
SELECT id
FROM subjects
WHERE subject_name = 'World History Since'
)
JOIN groups grp ON s.group_id = grp.id
GROUP BY s.group_id
ORDER BY avg_grade DESC
;