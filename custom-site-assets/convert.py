import re
from typing import Dict, List, Tuple

from utils import (
    DocLink,
    DocPath,
    Settings,
    parse_graph,
    pp,
    raw_dir,
    site_dir,
    write_settings,
)


def extract_note_description(lines: List[str]) -> str:
    """Extract a concise, clean summary (140-160 chars) from the markdown note content for SEO and OpenGraph."""
    cleaned_chunks: List[str] = []
    in_code_block = False
    in_frontmatter = False

    for line in lines:
        stripped = line.strip()

        # Handle YAML frontmatter delimiters
        if stripped == "---":
            in_frontmatter = not in_frontmatter
            continue
        if in_frontmatter:
            continue

        # Handle code blocks
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue

        # Skip empty lines, metadata markers, headings, list markers, quotes, and images
        if not stripped or stripped.startswith(
            ("#", "!", ">", "Created:", "Updated:", "|", "$$")
        ):
            continue

        # Remove wikilinks [[Target|Alias]] -> Alias, [[Target]] -> Target
        text = re.sub(r"\[\[(?:[^|\]]*\|)?([^\]]+)\]\]", r"\1", stripped)
        # Remove standard markdown links [text](url) -> text
        text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
        # Remove LaTeX inline math $...$
        text = re.sub(r"\$[^$]+\$", "", text)
        # Remove markdown bold/italics/code/strikethrough
        text = re.sub(r"[*_`~]", "", text)
        # Remove html tags
        text = re.sub(r"<[^>]+>", "", text)
        # Remove backslashes and replace double quotes with single quotes
        text = text.replace("\\", "").replace('"', "'")
        # Normalize whitespace
        text = " ".join(text.split())

        if text:
            cleaned_chunks.append(text)
            if sum(len(c) for c in cleaned_chunks) >= 150:
                break

    full_summary = " ".join(cleaned_chunks)
    # Sanitize backslashes, double quotes, and newlines
    full_summary = (
        full_summary.replace("\\", "").replace('"', "'").replace("\n", " ").strip()
    )

    if not full_summary:
        return "Notes and research on machine learning, AI security, and cybersecurity."

    if len(full_summary) > 155:
        # Trim cleanly at word boundary
        truncated = full_summary[:155].rsplit(" ", 1)[0]
        return f"{truncated}..."
    return full_summary


# Files and directories to exclude from published documentation navigation and pages
IGNORED_MD_FILES = {"claude.md", "agents.md"}
IGNORED_INTERNAL_PARTS = {
    ".skills",
    ".agents",
    ".notes",
    ".github",
    ".obsidian",
    "templates",
    "design-mockup",
}
IGNORED_SECTION_DIRS = {
    "attachments",
    "templates",
    "pdfs",
    ".skills",
    ".agents",
    ".notes",
    ".github",
    ".obsidian",
    "design-mockup",
}


if __name__ == "__main__":
    Settings.parse_env()
    Settings.sub_file(site_dir / "config.toml")
    Settings.sub_file(site_dir / "content/_index.md")
    Settings.sub_file(site_dir / "templates/macros/footer.html")
    Settings.sub_file(site_dir / "static/js/graph.js")

    nodes: Dict[str, str] = {}
    edges: List[Tuple[str, str]] = []
    section_count = 0

    all_paths = list(sorted(raw_dir.glob("**/*")))

    for path in [raw_dir, *all_paths]:
        doc_path = DocPath(path)
        path_parts_lower = [p.lower() for p in doc_path.old_rel_path.parts]

        if doc_path.is_file:
            if doc_path.is_md:
                # Skip internal markdown files and skill/agent files
                if doc_path.old_rel_path.name.lower() in IGNORED_MD_FILES or any(
                    part in IGNORED_INTERNAL_PARTS for part in path_parts_lower
                ):
                    print(f"Skipping internal page: {doc_path.old_rel_path}")
                    continue

                # Page
                nodes[doc_path.abs_url] = doc_path.page_title
                content = doc_path.content
                parsed_lines: List[str] = []
                for line in content:
                    parsed_line, linked = DocLink.parse(line, doc_path)

                    # Fix LaTEX new lines
                    parsed_line = re.sub(r"\\\\\s*$", r"\\\\\\\\", parsed_line)

                    parsed_lines.append(parsed_line)

                    edges.extend([doc_path.edge(rel_path) for rel_path in linked])

                # Calculate reading time (approx 200 WPM)
                words = " ".join(content).split()
                reading_time = max(1, (len(words) + 199) // 200)

                # Extract description for SEO & OpenGraph
                description = extract_note_description(content)

                content_frontmatter = [
                    "---",
                    f'title: "{doc_path.page_title}"',
                    f'description: "{description}"',
                    f"date: {doc_path.modified}",
                    f"updated: {doc_path.modified}",
                    "template: docs/page.html",
                    "extra:",
                    f"    reading_time: {reading_time}",
                    f'    meta_description: "{description}"',
                    "---",
                    # To add last line-break
                    "",
                ]
                doc_path.write(["\n".join(content_frontmatter), *parsed_lines])
                print(f"Found page: {doc_path.new_rel_path}")
            else:
                # Resource (images, attachments, etc.) - copy for markdown embeds
                doc_path.copy()
                print(f"Found resource: {doc_path.new_rel_path}")
        else:
            """Section"""
            # Skip creating navigation sections for attachments, templates, and internal folders
            if any(part in IGNORED_SECTION_DIRS for part in path_parts_lower):
                print(f"Skipping navigation section: {doc_path.old_rel_path}")
                continue

            # Frontmatter
            # TODO: sort_by depends on settings
            content = [
                "---",
                f'title: "{doc_path.section_title}"',
                "template: docs/section.html",
                f"sort_by: {Settings.options['SORT_BY']}",
                f"weight: {section_count}",
                "extra:",
                f"    sidebar: {doc_path.section_sidebar}",
                "---",
                # To add last line-break
                "",
            ]
            section_count += 1
            doc_path.write_to("_index.md", "\n".join(content))
            print(f"Found section: {doc_path.new_rel_path}")

    pp(nodes)
    pp(edges)
    parse_graph(nodes, edges)
    write_settings()
