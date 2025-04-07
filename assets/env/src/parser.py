import pandas as pd
import re
import bibtexparser

# === FILE PATHS ===
INPUT_BIB = "assets/data/Primeros_Libros/Primeros_Libros.bib"
REFERENCE_CSV = "assets/data/escape_characters.csv"
MAPPING_CSV = "assets/data/Full_CSV_BibTeX_Field_Comparison.csv"
ESCAPE_CSV = "assets/data/escape_characters.csv"
OUTPUT_CSV = "assets/data/output.csv"

# === LOAD CSV FILES ===
reference_df = pd.read_csv(REFERENCE_CSV)
field_mapping_df = pd.read_csv(MAPPING_CSV)
escape_chars_df = pd.read_csv(ESCAPE_CSV)

# === BUILD FIELD MAPPING (literal fields only) ===
field_mapping_df['Equivalent BibTeX Field'] = field_mapping_df['Equivalent BibTeX Field'].astype(str).str.strip()
literal_mappings = field_mapping_df[
    field_mapping_df['Equivalent BibTeX Field'].apply(lambda x: x.islower() and x.isidentifier())
]
bibtex_to_csv_map = dict(zip(
    literal_mappings['Equivalent BibTeX Field'],
    literal_mappings['CSV Column']
))

# === SPECIAL FIELDS WITH HARD-CODED LOGIC ===
instruction_based_fields = {
    "Key": lambda entry: entry.get("ID", ""),
    "Item Type": lambda entry: entry.get("ENTRYTYPE", "")
}

# === ESCAPE CHARACTER MAP (merged with additions) ===
escape_chars_df.dropna(inplace=True)
escape_mapping = dict(zip(escape_chars_df["Escaped as"].str.strip(), escape_chars_df["Character"].str.strip()))

basic_escapes = {
    esc: char for esc, char in escape_mapping.items()
    if " or " not in esc and esc.startswith("\\")
}

extended_escapes = {}
for esc, char in basic_escapes.items():
    extended_escapes[esc] = char
    extended_escapes[f"{{{esc}}}"] = char

manual_additions = {
    r"{\textbar}": "|", r"\textbar": "|",
    r"{\textless}": "<", r"\textless": "<",
    r"{\textgreater}": ">", r"\textgreater": ">",
    r"{\_}": "_", r"\_": "_",
    r"{\%}": "%", r"\%": "%",
    r"{\&}": "&", r"\&": "&",
    r"{\$}": "$", r"\$": "$"
}

final_escape_map = {**extended_escapes, **manual_additions}

# === CLEANING FUNCTIONS ===
def clean_braces(text):
    if not isinstance(text, str):
        return text
    while text.startswith('{') and text.endswith('}'):
        inner = text[1:-1]
        if inner.count('{') == inner.count('}'):
            text = inner
        else:
            break
    return re.sub(r'\{([^{}]+)\}', r'\1', text)

def unescape_latex(text):
    if not isinstance(text, str):
        return text
    for escaped, literal in sorted(final_escape_map.items(), key=lambda x: -len(x[0])):
        text = text.replace(escaped, literal)
    text = text.replace('{}', '')
    return clean_braces(text)

# === LOAD BIBTEX FILE ===
with open(INPUT_BIB, "r", encoding="utf-8") as bibfile:
    bib_database = bibtexparser.load(bibfile)

# === MAP BIBTEX ENTRIES TO ZOTERO CSV ROWS ===
csv_columns = reference_df.columns.tolist()

def map_bibtex_to_csv(entry):
    row = {col: "" for col in csv_columns}
    for field, func in instruction_based_fields.items():
        if field in row:
            row[field] = func(entry)
    for bib_field, csv_field in bibtex_to_csv_map.items():
        if csv_field in row and bib_field in entry:
            row[csv_field] = unescape_latex(entry[bib_field])
    return row

csv_rows = [map_bibtex_to_csv(entry) for entry in bib_database.entries]
csv_df = pd.DataFrame(csv_rows)

# === EXPORT TO CSV ===
csv_df.to_csv(OUTPUT_CSV, index=False, encoding="utf-8")
print(f"✅ Done. Exported to {OUTPUT_CSV}")
