SELECT student_name, grade
FROM students s
JOIN grades g ON s.id = g.student_id
AND s.group_id = (
SELECT id
FROM groups
WHERE group_number = 101
)
AND g.subject_id = (
SELECT id
FROM subjects
WHERE subject_name = "World History Since"
);