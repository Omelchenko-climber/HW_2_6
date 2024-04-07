SELECT student_name, grade, date_of
FROM students std
JOIN groups grp ON std.group_id = grp.id
AND grp.id = (
SELECT id
FROM groups
WHERE group_number = 103
)
JOIN grades grd ON std.id = grd.student_id
JOIN subjects sub ON grd.subject_id = sub.id
AND sub.id = (
SELECT id
FROM subjects
WHERE subject_name = "World History Since"
)
ORDER BY date_of DESC
;