SELECT DISTINCT(subject_name)
FROM subjects sub
JOIN grades gr ON sub.id = gr.subject_id
AND gr.student_id = (
SELECT id
FROM students
WHERE student_name = "Angela Jordan"
)
;