SELECT subject_name, teacher_name
FROM subjects s
JOIN teachers t ON s.teacher_id = t.id
AND teacher_name = "Jessica Jones"
;