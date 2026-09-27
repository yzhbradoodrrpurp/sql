from pathlib import Path
from shutil import copy2

from PIL import Image, ImageDraw, ImageFont
from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor
from docx.text.paragraph import Paragraph


ROOT = Path("/Users/yzhbradoodrrpurp/Desktop/sql")
SOURCE = ROOT / "homework/ex2/Basic SQL exercise 2.docx"
OUTPUT = ROOT / "homework/ex2/2023141220023_易治行_Basic_SQL_Exercise_2.docx"
NAME_IMAGE = ROOT / "tmp/ex2_work/student_name.png"


def set_run_font(run, name: str, size: float, bold=False, italic=False):
    run.font.name = name
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = RGBColor(0, 0, 0)
    rfonts = run._element.get_or_add_rPr().get_or_add_rFonts()
    rfonts.set(qn("w:ascii"), name)
    rfonts.set(qn("w:hAnsi"), name)
    rfonts.set(qn("w:eastAsia"), name)


def insert_before(ref_paragraph, text=""):
    new_p = OxmlElement("w:p")
    ref_paragraph._p.addprevious(new_p)
    return Paragraph(new_p, ref_paragraph._parent)


def insert_after(ref_paragraph, text=""):
    new_p = OxmlElement("w:p")
    ref_paragraph._p.addnext(new_p)
    return Paragraph(new_p, ref_paragraph._parent)


def format_title(p, text):
    p.style = "Title"
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after = Pt(6)
    r = p.add_run(text)
    set_run_font(r, "Times New Roman", 20, bold=True)


def format_meta(p, text):
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p.paragraph_format.space_after = Pt(12)
    r = p.add_run()
    r.add_picture(str(NAME_IMAGE), width=Inches(2.25))


def build_name_image():
    text = "2023141220023  易治行"
    font = ImageFont.truetype("/System/Library/Fonts/Hiragino Sans GB.ttc", 46)
    probe = Image.new("RGBA", (10, 10), (255, 255, 255, 0))
    draw = ImageDraw.Draw(probe)
    box = draw.textbbox((0, 0), text, font=font)
    image = Image.new("RGBA", (box[2] - box[0] + 24, box[3] - box[1] + 18), (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)
    draw.text((12, 7 - box[1]), text, font=font, fill=(0, 0, 0, 255))
    image.save(NAME_IMAGE)


def format_heading(p, text, level=1):
    p.style = f"Heading {level}"
    p.paragraph_format.space_before = Pt(10)
    p.paragraph_format.space_after = Pt(5)
    p.paragraph_format.keep_with_next = True
    r = p.add_run(text)
    set_run_font(r, "Times New Roman", 15 if level == 1 else 12, bold=True)


def format_code(p, sql):
    p.paragraph_format.left_indent = Inches(0.28)
    p.paragraph_format.right_indent = Inches(0.08)
    p.paragraph_format.space_before = Pt(2)
    p.paragraph_format.space_after = Pt(7)
    p.paragraph_format.line_spacing = Pt(12)
    p.paragraph_format.keep_together = True
    r = p.add_run(sql)
    set_run_font(r, "Courier New", 9.2)


def format_note(p, text):
    p.paragraph_format.left_indent = Inches(0.28)
    p.paragraph_format.space_after = Pt(7)
    p.paragraph_format.keep_together = True
    lead, sep, rest = text.partition(":")
    if sep:
        r = p.add_run(lead + ":")
        set_run_font(r, "Times New Roman", 10.5, bold=True)
        r = p.add_run(rest)
        set_run_font(r, "Times New Roman", 10.5)
    else:
        r = p.add_run(text)
        set_run_font(r, "Times New Roman", 10.5)


ANSWERS = {
    "1a": {
        "sql": "UPDATE instructor\nSET salary = salary * 1.10\nWHERE dept_name = 'Comp. Sci.';"
    },
    "1b": {
        "sql": "DELETE FROM course AS c\nWHERE NOT EXISTS (\n    SELECT 1\n    FROM section AS s\n    WHERE s.course_id = c.course_id\n);"
    },
    "1c": {
        "sql": "INSERT INTO instructor (ID, name, dept_name, salary)\nSELECT ID, name, dept_name, 10000\nFROM student\nWHERE tot_cred > 100;",
        "note": "Constraint note: In the supplied university schema, salary must be greater than 29000. Therefore, the requested salary of 10000 causes this statement to be rejected unless that check constraint is changed."
    },
    "1d": {
        "sql": "INSERT INTO course (course_id, title, dept_name, credits)\nVALUES ('CS-001', 'Weekly Seminar', 'Comp. Sci.', 0);",
        "note": "Constraint note: In the supplied university schema, credits must be greater than 0. Therefore, the requested value 0 causes this statement to be rejected unless that check constraint is changed."
    },
    "1e": {
        "sql": "INSERT INTO section (course_id, sec_id, semester, year)\nVALUES ('CS-001', '1', 'Fall', 2009);"
    },
    "1f": {
        "sql": "INSERT INTO takes (ID, course_id, sec_id, semester, year, grade)\nSELECT ID, 'CS-001', '1', 'Fall', 2009, NULL\nFROM student\nWHERE dept_name = 'Comp. Sci.';"
    },
    "1g": {
        "sql": "DELETE FROM takes AS t\nWHERE t.course_id = 'CS-001'\n  AND t.sec_id = '1'\n  AND t.semester = 'Fall'\n  AND t.year = 2009\n  AND t.ID IN (\n      SELECT s.ID\n      FROM student AS s\n      WHERE s.name = 'Chavez'\n  );"
    },
    "1h": {
        "sql": "DELETE FROM course\nWHERE course_id = 'CS-101';",
        "note": "Result: section.course_id uses ON DELETE CASCADE, so course offerings and their dependent teaches and takes rows would be removed automatically. However, CS-101 is also referenced as prereq.prereq_id, whose foreign key has no ON DELETE action. In the supplied data, the statement is therefore rejected until those prerequisite references are deleted or updated. Without cascading section deletion, existing sections would also block the delete."
    },
    "1i": {
        "sql": "DELETE FROM takes AS t\nWHERE EXISTS (\n    SELECT 1\n    FROM course AS c\n    WHERE c.course_id = t.course_id\n      AND LOWER(c.title) LIKE '%database%'\n);"
    },
    "2a": {
        "sql": "SELECT e.employee_name, e.city\nFROM employee AS e\nJOIN works AS w\n  ON w.employee_name = e.employee_name\nWHERE w.company_name = 'First Bank Corporation';"
    },
    "2b": {
        "sql": "SELECT e.employee_name, e.street, e.city\nFROM employee AS e\nJOIN works AS w\n  ON w.employee_name = e.employee_name\nWHERE w.company_name = 'First Bank Corporation'\n  AND w.salary > 10000;"
    },
    "2c": {
        "sql": "SELECT e.employee_name\nFROM employee AS e\nWHERE NOT EXISTS (\n    SELECT 1\n    FROM works AS w\n    WHERE w.employee_name = e.employee_name\n      AND w.company_name = 'First Bank Corporation'\n);"
    },
    "2d": {
        "sql": "SELECT DISTINCT w.employee_name\nFROM works AS w\nWHERE w.salary > ALL (\n    SELECT sb.salary\n    FROM works AS sb\n    WHERE sb.company_name = 'Small Bank Corporation'\n);"
    },
    "2e": {
        "sql": "SELECT DISTINCT c.company_name\nFROM company AS c\nWHERE NOT EXISTS (\n    SELECT 1\n    FROM company AS sb\n    WHERE sb.company_name = 'Small Bank Corporation'\n      AND NOT EXISTS (\n          SELECT 1\n          FROM company AS c2\n          WHERE c2.company_name = c.company_name\n            AND c2.city = sb.city\n      )\n);"
    },
    "2f": {
        "sql": "SELECT w.company_name\nFROM works AS w\nGROUP BY w.company_name\nHAVING COUNT(DISTINCT w.employee_name) >= ALL (\n    SELECT COUNT(DISTINCT w2.employee_name)\n    FROM works AS w2\n    GROUP BY w2.company_name\n);"
    },
    "2g": {
        "sql": "SELECT w.company_name\nFROM works AS w\nGROUP BY w.company_name\nHAVING AVG(w.salary) > (\n    SELECT AVG(f.salary)\n    FROM works AS f\n    WHERE f.company_name = 'First Bank Corporation'\n);"
    },
}


def ensure_styles(doc):
    existing = {s.name for s in doc.styles}
    for name in ("Title", "Heading 1", "Heading 2"):
        if name not in existing:
            style = doc.styles.add_style(name, WD_STYLE_TYPE.PARAGRAPH)
            style.base_style = doc.styles["Normal"]


def key_for_question(text):
    stripped = text.strip()
    if len(stripped) >= 2 and stripped[0] in "abcdefghi" and stripped[1] == ".":
        return stripped[0]
    return None


def main():
    build_name_image()
    copy2(SOURCE, OUTPUT)
    doc = Document(OUTPUT)
    ensure_styles(doc)

    first = doc.paragraphs[0]
    title = insert_before(first)
    format_title(title, "Basic SQL Exercise 2")
    meta = insert_before(first)
    format_meta(meta, "2023141220023  易治行")

    note = doc.paragraphs[2]
    note.text = (
        "This exercise does not provide schema-creation or data-insertion files. "
        "You may write the SQL statements directly, or create a schema and sample data first."
    )
    note.paragraph_format.space_after = Pt(10)
    for run in note.runs:
        set_run_font(run, "Times New Roman", 10, italic=True)

    part = None
    original_paragraphs = list(doc.paragraphs)
    for p in original_paragraphs:
        text = p.text.strip()
        if text.startswith("1. Write the following"):
            part = "1"
            h = insert_before(p)
            format_heading(h, "Part 1 University Schema Data Modifications")
            p.paragraph_format.keep_with_next = True
            for run in p.runs:
                set_run_font(run, "Times New Roman", 11, bold=True)
            continue
        if text.startswith("2. Consider the following"):
            part = "2"
            h = insert_before(p)
            format_heading(h, "Part 2 Employee Database Queries")
            h.paragraph_format.page_break_before = True
            p.paragraph_format.keep_with_next = True
            for run in p.runs:
                set_run_font(run, "Times New Roman", 11, bold=True)
            continue

        letter = key_for_question(text)
        if part and letter:
            key = part + letter
            if key not in ANSWERS:
                continue
            p.paragraph_format.keep_with_next = True
            p.paragraph_format.space_before = Pt(4)
            p.paragraph_format.space_after = Pt(2)
            for run in p.runs:
                set_run_font(run, "Times New Roman", 10.5, bold=True)
            code_p = insert_after(p)
            format_code(code_p, ANSWERS[key]["sql"])
            if "note" in ANSWERS[key]:
                note_p = insert_after(code_p)
                format_note(note_p, ANSWERS[key]["note"])

    # Format the employee-schema lines as compact monospaced definitions.
    for p in doc.paragraphs:
        t = p.text.strip()
        if t.startswith(("employee(", "works(", "company(", "manages(")):
            p.paragraph_format.left_indent = Inches(0.28)
            p.paragraph_format.space_after = Pt(1)
            for run in p.runs:
                set_run_font(run, "Courier New", 9.5)
        elif t == "Give an expression in SQL for each of the following queries.":
            p.paragraph_format.space_before = Pt(6)
            p.paragraph_format.space_after = Pt(5)
            p.paragraph_format.keep_with_next = True
            for run in p.runs:
                set_run_font(run, "Times New Roman", 10.5, italic=True)

    # Preserve the source page geometry and add page numbering in the footer.
    for section in doc.sections:
        section.header_distance = Inches(0.35)
        section.footer_distance = Inches(0.45)
        footer = section.footer
        fp = footer.paragraphs[0]
        fp.alignment = WD_ALIGN_PARAGRAPH.CENTER
        r = fp.add_run("2023141220023  Yi Zhixing  |  Basic SQL Exercise 2  |  ")
        set_run_font(r, "Times New Roman", 8.5)
        fld = OxmlElement("w:fldSimple")
        fld.set(qn("w:instr"), "PAGE")
        fp._p.append(fld)

    doc.core_properties.title = "2023141220023 易治行 Basic SQL Exercise 2"
    doc.core_properties.author = "易治行"
    doc.core_properties.subject = "Completed SQL homework"
    doc.save(OUTPUT)
    print(OUTPUT)


if __name__ == "__main__":
    main()
