students = LOAD '/user/student/student/highmarks_input/*'
    USING PigStorage(',')
    AS (student_id:chararray, math:int, english:int, science:int);

valid_students = FILTER students BY
    student_id IS NOT NULL
    AND math IS NOT NULL
    AND english IS NOT NULL
    AND science IS NOT NULL
    AND student_id != 'student_id';

with_average = FOREACH valid_students GENERATE
    student_id,
    (math + english + science) / 3.0 AS average_marks;

classified = FOREACH with_average GENERATE
    student_id,
    average_marks,
    (average_marks >= 85.0 ? 'Top Students' :
     (average_marks < 35.0 ? 'Weak Students' : 'Other Students'))
     AS category;

category_groups = GROUP classified BY category;

category_summary = FOREACH category_groups GENERATE
    group AS category,
    COUNT(classified) AS student_count,
    AVG(classified.average_marks) AS category_average;

STORE category_summary
    INTO '/user/student/student/pig_category_output'
    USING PigStorage(',');
