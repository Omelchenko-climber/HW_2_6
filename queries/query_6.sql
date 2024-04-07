SELECT student_name
FROM students s
JOIN groups g ON s.group_id = g.id
AND g.group_number = 102
;