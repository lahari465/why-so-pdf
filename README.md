# why-so-pdf 📄

> Started with 50 questions. Ended up questioning the PDF.

## 🕵️ The PDF Incident

It started with interview preparation.

I was preparing around 50 questions and answers for one of my projects. While exploring an AI tool, I accidentally clicked a button that processed the content and generated a PDF.

And I got curious.

What actually happens behind that button? How does text magically turn into a properly formatted PDF? What Python libraries make that possible?

One question led to another, and eventually I stumbled upon **ReportLab**.

Naturally, I started experimenting.

I wrote some Python code, added predefined content, played around with formatting, and generated my own PDF.

Was it necessary? Probably not.

Was I fascinated by the fact that Python could generate an actual PDF? Absolutely.

And that's how `why-so-pdf` happened.

## ⚙️ What Does It Do?

A simple Python script that generates a formatted PDF containing 50 predefined interview questions and answers.

The content is currently written directly inside the Python script, while ReportLab handles the PDF generation and formatting.

Nothing fancy. Just a small experiment with a surprisingly interesting library.

## 🛠️ Built With

- Python
- ReportLab

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone <repository-url>
cd why-so-pdf
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Alternatively:

```bash
pip install reportlab
```

### 3. Run the script

```bash
python pdf_incident.py
```

The generated PDF will be saved to the output location configured in the script.

## 📚 What I Learned

- Working with Python libraries and imports
- Generating PDF documents programmatically
- Using ReportLab's Platypus framework
- Formatting paragraphs and text styles
- Managing spacing and page layouts
- Understanding how Python can automate document creation

## 🎯 Why This Project?

Not every project needs to solve a massive problem.

Sometimes, clicking the wrong button, asking one extra question, and following your curiosity is enough to start building something.

This is one of those projects.

---

*Built with Python, ReportLab, and a little too much curiosity.*
