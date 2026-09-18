/* ======================== Part I ======================== */

/* I-1. Titles of 3-credit courses in the Comp. Sci. department. */
SELECT title
FROM course
WHERE dept_name = 'Comp. Sci.'
  AND credits = 3;


/* I-2. IDs of students taught by Einstein, without duplicates. */
SELECT DISTINCT t.ID
FROM takes AS t
JOIN teaches AS te
  ON te.course_id = t.course_id
 AND te.sec_id = t.sec_id
 AND te.semester = t.semester
 AND te.year = t.year
JOIN instructor AS i
  ON i.ID = te.ID
WHERE i.name = 'Einstein';


/* I-3. Highest instructor salary. */
SELECT MAX(salary) AS highest_salary
FROM instructor;


/* I-4. All instructors earning the highest salary. */
SELECT ID, name, dept_name, salary
FROM instructor
WHERE salary = (
    SELECT MAX(salary)
    FROM instructor
);


/* I-5. Enrollment of every section offered in Fall 2017. */
SELECT s.course_id,
       s.sec_id,
       COUNT(t.ID) AS enrollment
FROM section AS s
LEFT JOIN takes AS t
  ON t.course_id = s.course_id
 AND t.sec_id = s.sec_id
 AND t.semester = s.semester
 AND t.year = s.year
WHERE s.semester = 'Fall'
  AND s.year = 2017
GROUP BY s.course_id, s.sec_id;


/* I-6. Maximum enrollment among all Fall 2017 sections. */
WITH section_enrollment AS (
    SELECT s.course_id,
           s.sec_id,
           COUNT(t.ID) AS enrollment
    FROM section AS s
    LEFT JOIN takes AS t
      ON t.course_id = s.course_id
     AND t.sec_id = s.sec_id
     AND t.semester = s.semester
     AND t.year = s.year
    WHERE s.semester = 'Fall'
      AND s.year = 2017
    GROUP BY s.course_id, s.sec_id
)
SELECT MAX(enrollment) AS maximum_enrollment
FROM section_enrollment;


/* I-7. Sections having the maximum enrollment in Fall 2017. */
WITH section_enrollment AS (
    SELECT s.course_id,
           s.sec_id,
           COUNT(t.ID) AS enrollment
    FROM section AS s
    LEFT JOIN takes AS t
      ON t.course_id = s.course_id
     AND t.sec_id = s.sec_id
     AND t.semester = s.semester
     AND t.year = s.year
    WHERE s.semester = 'Fall'
      AND s.year = 2017
    GROUP BY s.course_id, s.sec_id
)
SELECT course_id, sec_id, enrollment
FROM section_enrollment
WHERE enrollment = (
    SELECT MAX(enrollment)
    FROM section_enrollment
);


/* ======================== Part II ======================== */

/* II-1. SSN, name, and salary of every department manager. */
SELECT e.ssn, e.name, e.salary
FROM employee AS e
JOIN department AS d
  ON d.mgr_ssn = e.ssn;


/* II-2. Employees who work more than 100 hours on any project. */
SELECT DISTINCT e.name, e.ssn
FROM employee AS e
JOIN hourlog AS h
  ON h.ssn = e.ssn
WHERE h.hours > 100;


/* II-3. Employees who work on at least two projects. */
SELECT e.name, e.ssn
FROM employee AS e
JOIN hourlog AS h
  ON h.ssn = e.ssn
GROUP BY e.ssn, e.name
HAVING COUNT(DISTINCT h.pno) >= 2;


/* II-4. Employees who have never worked on a project. */
SELECT e.name, e.ssn
FROM employee AS e
WHERE NOT EXISTS (
    SELECT 1
    FROM hourlog AS h
    WHERE h.ssn = e.ssn
);


/* II-5. Employees who work on every project Singh works on. */
SELECT e.name, e.ssn
FROM employee AS e
WHERE NOT EXISTS (
    SELECT 1
    FROM hourlog AS sh
    JOIN employee AS singh
      ON singh.ssn = sh.ssn
    WHERE singh.name = 'Singh'
      AND NOT EXISTS (
          SELECT 1
          FROM hourlog AS eh
          WHERE eh.ssn = e.ssn
            AND eh.pno = sh.pno
      )
);


/* II-6. Employees who work on every project their department manages. */
SELECT e.name, e.ssn
FROM employee AS e
WHERE NOT EXISTS (
    SELECT 1
    FROM project AS p
    WHERE p.dno = e.dno
      AND NOT EXISTS (
          SELECT 1
          FROM hourlog AS h
          WHERE h.ssn = e.ssn
            AND h.pno = p.pno
      )
);
