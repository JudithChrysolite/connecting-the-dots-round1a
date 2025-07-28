# 🧠 Connecting the Dots - Round 1A | Adobe India Hackathon 2025

Reimagining PDF reading by extracting structured outlines from documents using intelligent, offline, Dockerized processing.

---

## 🚀 Challenge Statement

You're handed a PDF — instead of simply reading it, the goal is to make sense of it like a machine.  
This project extracts a **structured outline** (Title, H1, H2, H3 headings along with page numbers) from input PDF files and outputs the result as a clean hierarchical JSON file.

---

## 📌 Features

- Accepts one or more PDF files (≤ 50 pages each)
- Extracts:
  - Document Title
  - Headings with levels: **H1**, **H2**, **H3**
  - Page numbers for each heading
- Outputs structured `JSON` files per PDF
- Runs entirely **offline** inside a Docker container
- Compatible with **linux/amd64** platforms
- Designed to process multiple PDFs in `/app/input` and output corresponding JSONs in `/app/output`

---

## 📂 Project Structure

<pre><code> 
 . ├── app/
│ └── main.py # Main extraction logic
├── sample_dataset/
│ ├── input/
│ │ ├── adobe.pdf
│ │ └── sample.pdf
│ ├── output/
│ │ ├── adobe.json
│ │ └── sample.json
│ └── schema/
│ └── output_schema.json
├── schema/
│ └── output_schema.json
├── Dockerfile # Container configuration
├── requirements.txt # Python dependencies
</code></pre>
---

## 🧪 Sample Output Format

```json
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "What is AI?", "page": 2 },
    { "level": "H3", "text": "History of AI", "page": 3 }
  ]
}
````

---

## 🧰 Dependencies

* Python 3.8+
* Libraries: `PyMuPDF`, `pdfminer`, `re`, etc.
  (See `requirements.txt` for full list)

---

## 🛠️ How to Build the Docker Image

```bash
docker build --platform linux/amd64 -t connecting-the-dots:round1a .
```

---

## ▶️ How to Run the Container

> ⛔ Runs completely offline — no internet access inside the container

```bash
docker run --rm \
  -v $(pwd)/sample_dataset/input:/app/input \
  -v $(pwd)/sample_dataset/output:/app/output \
  --network none \
  connecting-the-dots:round1a
```

---

## ✅ Expected Behavior

* Input: PDFs placed inside `/app/input`
* Output: Corresponding `.json` files will be saved in `/app/output`
* Each output file is named like `filename.pdf → filename.json`

---

## ⚙️ Implementation Details

* The system uses **font size, weight, and positional cues** to differentiate heading levels
* Built-in logic for **multi-page traversal and outline structuring**
* No hardcoded rules — generalizes across most academic & formal PDFs
* Respects strict constraints:

  * ⚡ ≤ 10 sec per 50-page PDF
  * 📦 Model size ≤ 200MB
  * 🧠 CPU-only (no GPU)
  * 🌐 Offline execution only

---
🧩 Tech Stack

Python
PyMuPDF (fitz)
Docker
Offline Execution
