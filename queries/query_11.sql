SELECT student_name, teacher_name, ROUND(AVG(grade), 1) as avg_grade
FROM students std
JOIN grades gr ON std.id = gr.student_id
JOIN subjects sub ON gr.subject_id = sub.id
JOIN teachers tch ON sub.teacher_id = tch.id
WHERE student_name = "Angela Jordan" AND teacher_name = "Jessica Jones"
GROUP BY student_name, teacher_name
;