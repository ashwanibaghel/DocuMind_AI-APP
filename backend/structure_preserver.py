import re

def add_sections_and_paragraphs(text):
    lines = text.splitlines()
    output = []
    current_section = None
    paragraph_lines = []
    paragraph_count = 0

    def flush_paragraph():
        nonlocal paragraph_lines, paragraph_count
        if paragraph_lines:
            paragraph_count += 1
            clean_para = " ".join(paragraph_lines).strip()
            output.append(f"[Paragraph {paragraph_count}]: {clean_para}\n")
            paragraph_lines.clear()

    for i, line in enumerate(lines):
        stripped = line.strip()

        # Section header detection: numbered headings or obvious all-caps headers
        if re.match(r'^(\d+(\.\d+)*[\.|\)]?\s+.+|[A-Z][A-Z\s]+)$', stripped) and len(stripped.split()) <= 10:
            flush_paragraph()
            current_section = stripped
            output.append(f"\n===== Section: {current_section} =====\n")
            paragraph_count = 0
            continue

        # Proper paragraph detection: blank line between two non-empty lines
        if stripped == "":
            flush_paragraph()
            continue

        paragraph_lines.append(stripped)

    flush_paragraph()  # last one
    return "\n".join(output)
