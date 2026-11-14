
# why-so-pdf 🤨

> **50 interview questions. One accidental click. An unnecessary engineering adventure.**

### 💀 The Incident

All I wanted was to prepare 50 interview questions and answers for one of my projects.

Then I accidentally clicked an AI tool's PDF generation button.

A PDF appeared. Beautiful. Formatted. Ready to go.

Normal people would've downloaded it and moved on.

Unfortunately, I had a question.

**"Okay, but HOW did it do that?"**

And just like that, interview preparation took a backseat. I went down a rabbit hole of Python libraries, PDF generation, formatting, and eventually discovered **ReportLab**.

Naturally, I had to try it myself.

A few imports, questionable formatting decisions, and several experiments later...

**Ladies and gentlemen, we have a PDF generator.**

Was this necessary? No.

Could I have spent that time preparing for the actual interview? Absolutely.

Do I regret it? Not particularly.

### ⚙️ What does it do?

It takes predefined content sitting inside a Python script and turns it into a formatted PDF.

Current capabilities include:

- Generates a PDF containing 50 interview questions and answers.
- Uses ReportLab for document creation and formatting.
- Handles paragraphs, styles, spacing, and page layouts.

No fancy AI. No complicated pipelines. Just Python doing its thing.

### 🧪 The technology behind the incident

| Technology | Role |
|---|---|
| Python | The mastermind |
| ReportLab | The actual PDF magician |

### 🚀 Reproducing the incident

**1. Clone the repository**

```bash
git clone <repository-url>
cd why-so-pdf
```

**2. Install dependencies**

```bash
pip install -r requirements.txt
```

**3. Execute the script**

```bash
python pdf_incident.py
```

And there it is. Your PDF. No accidental button clicks required.

### 🧠 Unexpected takeaways

- Explored Python libraries and imports.
- Got familiar with ReportLab and its Platypus framework.
- Experimented with paragraphs, styles, and document layouts.
- Learned how programmatic PDF generation actually works.
- Discovered that curiosity has absolutely no sense of priority.

### 📍 Project status

<badge color="success">Operational</badge>

- [x] Accidentally discover PDF generation.
- [x] Get unnecessarily curious.
- [x] Build a working PDF generator.
- [ ] Explain to myself why I did all this.

---

**In conclusion:**

I came for 50 interview questions.

I left with a Python project.

The interview preparation was not the only thing that got processed.

*Built with Python, ReportLab, and a complete inability to leave things unexplored.*
