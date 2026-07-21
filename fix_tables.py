import re

INPUT_FILE = "teamoverzicht.html"     # change to your actual filename
OUTPUT_FILE = "teamoverzicht.html"

COLGROUP = """<colgroup>
    <col style="width:22%">
    <col style="width:22%">
    <col style="width:14%">
    <col style="width:18%">
    <col style="width:12%">
    <col style="width:12%">
  </colgroup>
  """

with open(INPUT_FILE, "r", encoding="utf-8") as f:
    html = f.read()

# Insert the colgroup right after every opening <table> tag
fixed_html = re.sub(r"(<table>)", r"\1\n  " + COLGROUP.strip(), html)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(fixed_html)

print(f"Done. Wrote {OUTPUT_FILE}")