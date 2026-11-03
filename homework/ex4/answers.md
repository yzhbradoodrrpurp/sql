# SQL and Relational Algebra Exercise 4 — Answers

姓名：易治行  
学号：2023141220023

## I. University schema — relational algebra

Assume the standard university schema:

- `student(ID, name, dept_name, tot_cred)`
- `takes(ID, course_id, sec_id, semester, year, grade)`
- `course(course_id, title, dept_name, credits)`
- `instructor(ID, name, dept_name, salary)`

### 1. Students who have taken at least one Comp. Sci. course

```text
π_{student.name}(
  student ⋈_{student.ID = takes.ID}
  (takes ⋈_{takes.course_id = course.course_id}
   σ_{course.dept_name = 'Comp. Sci.'}(course))
)
```

### 2. Students who have not taken any course offering before Spring 2009

```text
π_{ID, name}(student)
−
π_{student.ID, student.name}(
  student ⋈_{student.ID = takes.ID} σ_{year < 2009}(takes)
)
```

Here “before Spring 2009” is interpreted under the standard university data, whose semesters are Spring, Summer, and Fall; therefore it means `year < 2009`.

### 3. Maximum instructor salary in each department

```text
γ_{dept_name; max(salary) → max_salary}(instructor)
```

### 4. Lowest of the per-department maximum salaries

```text
D ← γ_{dept_name; max(salary) → max_salary}(instructor)
γ_{min(max_salary) → lowest_max_salary}(D)
```

## II. Library schema — relational algebra

Given:

- `member(member_no, name, dob)`
- `books(isbn, title, authors, publisher)`
- `borrowed(member_no, isbn, date)`

Let:

```text
MH ← σ_{publisher = 'McGraw-Hill'}(books)
```

### 1. Members who have borrowed any McGraw-Hill book

```text
π_{name}(
  member ⋈_{member.member_no = borrowed.member_no}
  (borrowed ⋈_{borrowed.isbn = MH.isbn} MH)
)
```

### 2. Members who have borrowed all McGraw-Hill books

```text
P ← π_{member_no, isbn}(
       borrowed ⋈_{borrowed.isbn = MH.isbn} MH
     )
Q ← π_{isbn}(MH)
π_{name}(member ⋈ (P ÷ Q))
```

### 3. Members who have borrowed more than five different McGraw-Hill books

```text
T ← γ_{member_no; count(distinct isbn) → book_count}(
       borrowed ⋈_{borrowed.isbn = MH.isbn} MH
     )
π_{member_no, name}(
  member ⋈ σ_{book_count > 5}(T)
)
```

## III. 软件公司管理系统

关系模式：

- `R(Rno, Rname, Rage, Rsex, Rlevel)`
- `X(Xno, Xname, Xloc, Rno)`
- `C(Rno, Xno, pay)`

### A. 关系代数

#### 1. 查找超过 40 岁的人员的编号和姓名

```text
π_{Rno, Rname}(σ_{Rage > 40}(R))
```

#### 2. 求在单个项目中获得报酬超过 2000 的男性人员的编号和姓名

```text
π_{R.Rno, R.Rname}(
  σ_{R.Rsex = '男' ∧ C.pay > 2000}
  (R ⋈_{R.Rno = C.Rno} C)
)
```

#### 3. 查询参与了 8 号人员参与的所有项目的人员的编号、名字、级别

```text
P ← π_{Rno, Xno}(C)
Q ← π_{Xno}(σ_{Rno = 8}(C))
π_{Rno, Rname, Rlevel}(R ⋈ (P ÷ Q))
```

### B. SQL

#### 4. 查询名称中含有“手机”两个字的项目的项目号和所在地点

```sql
SELECT Xno, Xloc
FROM X
WHERE Xname LIKE '%手机%';
```

#### 5. 查询所在地点为“成都”的项目的主管的姓名、年龄、性别

```sql
SELECT DISTINCT R.Rname, R.Rage, R.Rsex
FROM X
JOIN R ON R.Rno = X.Rno
WHERE X.Xloc = '成都';
```

#### 6. 查询参与了 8 号人员参与的所有项目的人员的编号、名字、级别

```sql
SELECT R.Rno, R.Rname, R.Rlevel
FROM R
WHERE NOT EXISTS (
    SELECT 1
    FROM C AS C8
    WHERE C8.Rno = 8
      AND NOT EXISTS (
          SELECT 1
          FROM C AS CP
          WHERE CP.Rno = R.Rno
            AND CP.Xno = C8.Xno
      )
);
```

#### 7. 查询同时参与了 9 号和 12 号项目的员工的编号和姓名

```sql
SELECT R.Rno, R.Rname
FROM R
JOIN C ON C.Rno = R.Rno
WHERE C.Xno IN (9, 12)
GROUP BY R.Rno, R.Rname
HAVING COUNT(DISTINCT C.Xno) = 2;
```

#### 8. 参与 11 号项目的人员每人报酬增加 100 元

```sql
UPDATE C
SET pay = pay + 100
WHERE Xno = 11;
```
