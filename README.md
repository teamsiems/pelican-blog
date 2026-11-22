# pelican-blog

- [Get Pelican](https://getpelican.com/)
- [Markdown Cheatsheet](https://www.markdownguide.org/cheat-sheet/)
- [teamsiems blog](https://teamsiems.github.io/pelican-blog/docs/index.html)

## Content maintenance

**`convert_to_markdown.py`** — cleans `.md` files in `content/`:

- Converts leftover WordPress HTML blocks to Markdown (via `markdownify`)
- Removes WordPress block comments (`<!-- wp:... -->`)
- Fixes over-escaped bold markers (`\*\*text\*\*` → `**text**`) in all files
- Removes lone `\` lines left by `<br>` tags between block elements

```
python convert_to_markdown.py
```

Output reports how many files were HTML-converted, how many only needed the bold fix, and how many were already clean.
