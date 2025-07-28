import os
import fitz  # PyMuPDF
import json

def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)
    fonts = {}
    headings = []

    for page_num, page in enumerate(doc, start=1):
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:
            if "lines" not in b:
                continue
            for line in b["lines"]:
                line_text = ""
                for span in line["spans"]:
                    size = round(span["size"], 1)
                    font = span["font"]
                    text = span["text"].strip()
                    if not text:
                        continue

                    line_text += text + " "

                    fonts.setdefault((font, size), 0)
                    fonts[(font, size)] += 1

                if line_text:
                    headings.append((line_text.strip(), size, font, page_num))

    # Identify most common font sizes to infer heading levels
    font_stats = {}
    for text, size, font, _ in headings:
        font_stats[size] = font_stats.get(size, 0) + 1

    top_sizes = sorted(font_stats.keys(), reverse=True)[:3]
    levels = ["H1", "H2", "H3"]
    size_to_level = {size: levels[i] for i, size in enumerate(top_sizes)}

    # Extract title from first matching largest font text
    title = ""
    for text, size, font, page_num in headings:
        if size == top_sizes[0]:
            title = text
            break

    outline = []
    for text, size, font, page_num in headings:
        level = size_to_level.get(size)
        if level:
            outline.append({"level": level, "text": text, "page": page_num})

    return {"title": title, "outline": outline}


def main():
    input_dir = "/app/input"
    output_dir = "/app/output"

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for filename in os.listdir(input_dir):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(input_dir, filename)
            try:
                result = extract_outline(pdf_path)
                output_file = os.path.join(output_dir, filename.replace(".pdf", ".json"))
                with open(output_file, "w", encoding="utf-8") as f:
                    json.dump(result, f, indent=2, ensure_ascii=False)
                print(f"✅ Processed: {filename}")
            except Exception as e:
                print(f"❌ Error processing {filename}: {e}")

if __name__ == "__main__":
    main()
