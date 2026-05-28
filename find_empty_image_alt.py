"""
Find markdown files containing images with empty alt text and no title.

Matches:  ![](url)
Does NOT match: ![](url "title")  or  ![alt](url)
"""
import re
import glob

CONTENT_DIR = "content"

# Match ![]( ... ) where the parentheses contain no double-quotes (i.e. no title)
PATTERN = re.compile(r'!\[\]\([^"]*\)')


def main():
    files = sorted(glob.glob(f"{CONTENT_DIR}/*.md"))
    found = 0

    for filepath in files:
        with open(filepath, encoding="utf-8") as f:
            text = f.read()

        matches = PATTERN.findall(text)
        if matches:
            print(f"{filepath} ({len(matches)} image(s))")
            found += 1

    print(f"\nDone. {found} file(s) with empty alt and no title.")


if __name__ == "__main__":
    main()
