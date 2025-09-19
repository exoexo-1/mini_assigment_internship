
````markdown
# Mini Assignment — Call Transcript Analyzer

A small web app built for the Groq internship challenge. It accepts a customer service call transcript, uses Groq’s LLM API to produce a summary and sentiment, shows the result in a browser, and saves it in a CSV file.


## 🧰 Tech Stack

- Python 3.x  
- FastAPI — to serve the UI + backend API  
- `groq` Python client — to call Groq’s inference / LLM APIs  
- `python-dotenv` — to load API key from `.env`  
- HTML + JavaScript — for a simple frontend form  
- CSV file storage — `call_analysis.csv` stores all analyzed transcripts

---

## 🔧 Setup & Installation

1. **Clone the repo**

   ```bash
   git clone https://github.com/exoexo-1/mini_assigment_internship.git
   cd mini_assigment_internship
````

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**

   Create a `.env` file in the root directory, with contents like:

   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

   > ⚠️ Make sure `.env` is in `.gitignore` so that you don’t accidentally commit your secret.

4. **Run the app**

   ```bash
   uvicorn server:app --reload
   ```

5. **Use the app**

   * Open a browser at `http://127.0.0.1:8000/`
   * Paste or type in your transcript in the form
   * Click *Analyze* → you'll see Summary & Sentiment results
   * Check `call_analysis.csv` to see stored results

---

## 🔍 How It Works

1. The user enters a transcript via a form in the browser.
2. The backend (FastAPI) sends this transcript to the Groq model via the `groq` Python client, asking explicitly for JSON output with keys `summary` and `sentiment`.
3. The result is parsed and returned to the frontend.
4. The transcript, summary, sentiment, and timestamp are appended to `call_analysis.csv`.

---

## ⚙️ Model / Variants

* Current model used is: `llama-3.1-8b-instant` (or whatever you set)
* You may try other Groq models for comparison (e.g. larger/smaller, more context, or tool-use variants) depending on performance & cost.

---

## 🔐 Security & Best Practices

* **Do not commit secrets** (API keys, `.env`) into your repo history.
* If you accidentally commit a secret, remove it from history and regenerate your key.
* Make sure `.gitignore` includes `.env`.

---

## 🗒️ Demo / Submission Guide

When recording your video demo, you might cover:

* What the app does
* How your code is structured
* Demo: run the server, submit transcript, see live results
* Show the CSV file update
* Brief note: if Groq API key isn’t available, fallback can be added (if implemented)

---

## 📂 Files in Repository

| Filename                | Purpose                                                          |
| ----------------------- | ---------------------------------------------------------------- |
| `server.py`             | The main FastAPI app                                             |
| `templates/index.html`  | The front-end form + UI                                          |
| `requirements.txt`      | Python dependencies                                              |
| `sample_transcript.txt` | An example transcript you can test with                          |
| `call_analysis.csv`     | The output CSV storing analyses                                  |
| `.gitignore`            | To avoid committing sensitive or unnecessary files (e.g. `.env`) |

---

## 🛠 Troubleshooting

| Issue                                  | Potential Fix                                                                                                      |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| “GROQ\_API\_KEY not set” error         | Check `.env` file exists, content is correct, `load_dotenv()` is called, you restarted the server after setting it |
| JSON parsing error from API            | Ensure prompt requests strict JSON; check you’re using a model that returns JSON in its message content            |
| Push to GitHub fails (secret scanning) | Remove committed secrets, remove them from history, regenerate API key                                             |

---

## 👤 Author

* **Your Name** — (you can put your name here)
* GitHub: [exoexo-1](https://github.com/exoexo-1)

---

## 📄 License

This project is for learning / demo / internship submission purposes. Feel free to reuse or modify.

```

---

If you want, I can also generate a more minimal README (just 1-page) or add badges (Python version, build status) if you're using CI. Do you want that?
::contentReference[oaicite:0]{index=0}
```
