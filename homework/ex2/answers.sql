/*
 * Basic SQL Exercise 2
 * Student: 2023141220023 Yi Zhixing
 * PostgreSQL syntax
 */

/* ======================== Part 1 ======================== */

/* 1(a). Increase Comp. Sci. instructor salaries by 10%. */
UPDATE instructor
SET salary = salary * 1.10
WHERE dept_name = 'Comp. Sci.';


/* 1(b). Delete courses that have never been offered. */
DELETE FROM course AS c
WHERE NOT EXISTS (
    SELECT 1
    FROM section AS s
    WHERE s.course_id = c.course_id
);


/*
 * 1(c). Insert students with more than 100 credits as instructors.
 * In the supplied university schema, salary has CHECK (salary > 29000),
 * so the requested salary of 10000 causes this statement to be rejected.
 */
INSERT INTO instructor (ID, name, dept_name, salary)
SELECT ID, name, dept_name, 10000
FROM student
WHERE tot_cred > 100;


/*
 * 1(d). Create CS-001 with zero credits.
 * In the supplied university schema, credits has CHECK (credits > 0),
 * so the requested value 0 causes this statement to be rejected.
 */
INSERT INTO course (course_id, title, dept_name, credits)
VALUES ('CS-001', 'Weekly Seminar', 'Comp. Sci.', 0);


/* 1(e). Create section 1 of CS-001 in Fall 2009. */
INSERT INTO section (course_id, sec_id, semester, year)
VALUES ('CS-001', '1', 'Fall', 2009);


/* 1(f). Enroll every Comp. Sci. student in that section. */
INSERT INTO takes (ID, course_id, sec_id, semester, year, grade)
SELECT ID, 'CS-001', '1', 'Fall', 2009, NULL
FROM student
WHERE dept_name = 'Comp. Sci.';


/* 1(g). Remove Chavez's enrollment from that section. */
DELETE FROM takes AS t
WHERE t.course_id = 'CS-001'
  AND t.sec_id = '1'
  AND t.semester = 'Fall'
  AND t.year = 2009
  AND t.ID IN (
      SELECT s.ID
      FROM student AS s
      WHERE s.name = 'Chavez'
  );


/*
 * 1(h). Delete CS-101.
 * With the supplied schema, section.course_id uses ON DELETE CASCADE, so the
 * course offerings would not block this delete; their teaches and takes rows
 * would also be deleted through cascading foreign keys. However, CS-101 is
 * referenced as prereq.prereq_id, and that foreign key has no ON DELETE
 * action. Therefore this statement is rejected while those prerequisite rows
 * exist. In a schema without cascading section deletion, existing offerings
 * would likewise cause a foreign-key violation and would need deletion first.
 */
DELETE FROM course
WHERE course_id = 'CS-101';


/* 1(i). Delete enrollments for courses whose title contains "database". */
DELETE FROM takes AS t
WHERE EXISTS (
    SELECT 1
    FROM course AS c
    WHERE c.course_id = t.course_id
      AND LOWER(c.title) LIKE '%database%'
);


/* ======================== Part 2 ======================== */

/* 2(a). Employees and residence cities for First Bank Corporation. */
SELECT e.employee_name, e.city
FROM employee AS e
JOIN works AS w
  ON w.employee_name = e.employee_name
WHERE w.company_name = 'First Bank Corporation';


/* 2(b). Their names, streets, and cities when salary is over 10000. */
SELECT e.employee_name, e.street, e.city
FROM employee AS e
JOIN works AS w
  ON w.employee_name = e.employee_name
WHERE w.company_name = 'First Bank Corporation'
  AND w.salary > 10000;


/* 2(c). Employees who do not work for First Bank Corporation. */
SELECT e.employee_name
FROM employee AS e
WHERE NOT EXISTS (
    SELECT 1
    FROM works AS w
    WHERE w.employee_name = e.employee_name
      AND w.company_name = 'First Bank Corporation'
);


/* 2(d). Employees earning more than every Small Bank employee. */
SELECT DISTINCT w.employee_name
FROM works AS w
WHERE w.salary > ALL (
    SELECT sb.salary
    FROM works AS sb
    WHERE sb.company_name = 'Small Bank Corporation'
);


/* 2(e). Companies in every city occupied by Small Bank Corporation. */
SELECT DISTINCT c.company_name
FROM company AS c
WHERE NOT EXISTS (
    SELECT 1
    FROM company AS sb
    WHERE sb.company_name = 'Small Bank Corporation'
      AND NOT EXISTS (
          SELECT 1
          FROM company AS c2
          WHERE c2.company_name = c.company_name
            AND c2.city = sb.city
      )
);


/* 2(f). Company or tied companies with the most employees. */
SELECT w.company_name
FROM works AS w
GROUP BY w.company_name
HAVING COUNT(DISTINCT w.employee_name) >= ALL (
    SELECT COUNT(DISTINCT w2.employee_name)
    FROM works AS w2
    GROUP BY w2.company_name
);


/* 2(g). Companies with a higher average salary than First Bank. */
SELECT w.company_name
FROM works AS w
GROUP BY w.company_name
HAVING AVG(w.salary) > (
    SELECT AVG(f.salary)
    FROM works AS f
    WHERE f.company_name = 'First Bank Corporation'
);
