"""
Convert all .md files in content/ from WordPress HTML blocks to clean Markdown.
Preserves Pelican frontmatter (Key: Value lines at top of file).
"""
import os
import re
from pathlib import Path
from markdownify import markdownify as md


CONTENT_DIR = Path(__file__).parent / "content"

# Pelican frontmatter keys
FRONTMATTER_KEYS = re.compile(
    r'^(Title|Date|Author|Category|Tags|Slug|Status|Summary|Modified|'
    r'Save_as|Template|Lang|Translation|Series|Series_index|'
    r'Keywords|Image)\s*:',
    re.IGNORECASE
)


def split_frontmatter(text):
    """Split Pelican frontmatter from body. Returns (frontmatter_lines, body)."""
    lines = text.splitlines(keepends=True)
    i = 0
    # Collect contiguous frontmatter lines (allow one blank line between them)
    in_front = True
    front_lines = []
    while i < len(lines) and in_front:
        line = lines[i]
        stripped = line.strip()
        if FRONTMATTER_KEYS.match(stripped):
            front_lines.append(line)
            i += 1
        elif stripped == "" and i < len(lines) - 1 and FRONTMATTER_KEYS.match(lines[i + 1].strip()):
            # blank line between frontmatter entries
            front_lines.append(line)
            i += 1
        else:
            in_front = False
    # The separator blank line between frontmatter and body
    while i < len(lines) and lines[i].strip() == "":
        front_lines.append(lines[i])
        i += 1
    body = "".join(lines[i:])
    return "".join(front_lines), body


def remove_wp_comments(text):
    """Remove WordPress block comments like <!-- wp:paragraph --> and <!-- /wp:paragraph -->."""
    # Remove wp block comment lines (including ones with JSON attributes)
    text = re.sub(r'[ \t]*<!-- /?wp:[^\n]*-->\n?', '', text)
    return text


def fix_bold_escaping(text):
    """Fix **text** sequences that markdownify over-escapes in HTML text nodes."""
    return re.sub(r'\\\*\\\*([^\n]+?)\\\*\\\*', r'**\1**', text)


def fix_br_artifacts(text):
    """Remove lone backslash lines left by <br> tags between block elements."""
    text = re.sub(r'^\\\s*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text


def convert_body(body):
    """Convert HTML in body to Markdown."""
    # Remove WordPress block comments first
    body = remove_wp_comments(body)

    # Convert HTML to Markdown using markdownify
    # heading_style=ATX uses ## style headings
    converted = md(
        body,
        heading_style="ATX",
        bullets="-",
        newline_style="backslash",
        strip=["script", "style"],
    )

    # Collapse 3+ consecutive blank lines into 2
    converted = re.sub(r'\n{3,}', '\n\n', converted)

    # Strip trailing whitespace on each line
    converted = "\n".join(line.rstrip() for line in converted.splitlines())

    # Ensure single trailing newline
    converted = converted.strip() + "\n"

    return converted


def process_file(filepath):
    text = filepath.read_text(encoding="utf-8")
    frontmatter, body = split_frontmatter(text)

    new_body = body
    html_converted = False

    # Convert HTML to Markdown if HTML tags or WP block comments are present
    if re.search(r'<[a-zA-Z]', body) or '<!-- wp:' in body:
        new_body = convert_body(body)
        html_converted = True

    # Fix over-escaped bold markers — applies to both freshly converted and
    # already-clean files (markdownify escapes ** in HTML text nodes)
    new_body = fix_bold_escaping(new_body)
    # Remove lone backslash lines left by <br> between block elements
    new_body = fix_br_artifacts(new_body)

    new_text = frontmatter + new_body
    if new_text != text:
        filepath.write_text(new_text, encoding="utf-8")
        return "converted" if html_converted else "fixed"
    return False


def main():
    files = sorted(CONTENT_DIR.glob("*.md"))
    converted = 0
    fixed = 0
    skipped = 0
    for f in files:
        try:
            result = process_file(f)
            if result == "converted":
                print(f"  converted: {f.name}")
                converted += 1
            elif result == "fixed":
                print(f"  fixed: {f.name}")
                fixed += 1
            else:
                skipped += 1
        except Exception as e:
            print(f"  ERROR {f.name}: {e}")

    print(
        f"\nDone. {converted} files converted, {fixed} files fixed, {skipped} already clean.")


if __name__ == "__main__":
    main()
