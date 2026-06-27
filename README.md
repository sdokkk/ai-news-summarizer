# AI News Summarizer

An AI-powered news summarizer built with Python and the OpenAI API.

The application downloads a web page, extracts the main article content, generates a concise summary using GPT, and saves the result as a Markdown file.

---

## Features

* Fetch web pages from a URL
* Extract readable article text
* Generate AI summaries using OpenAI GPT
* Save summaries as Markdown files
* Modular project structure for easy extension

---

## Project Structure

```text
project1-summarizer/
│
├── llm/
│   └── openai_client.py      # OpenAI API wrapper
│
├── tools/
│   ├── fetcher.py            # Download webpage
│   ├── parser.py             # Extract article text
│   ├── validator.py          # Validate URLs
│   └── markdown.py           # Save Markdown output
│
├── output/                   # Generated summaries
├── summarizer.py             # Application entry point
├── requirements.txt
├── .env
└── README.md
```

---

## Requirements

* Python 3.11+
* OpenAI API Key

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
OPENAI_API_KEY=your_api_key_here
```

---

## Usage

Run the application:

```bash
python summarizer.py
```

Input a webpage URL when prompted.

Example:

```text
https://openai.com/news/
```

The application will:

1. Validate the URL
2. Download the webpage
3. Extract the article text
4. Generate an AI summary
5. Save the result as a Markdown file

---

## Example Output

```text
正在下载网页...
正在提取正文...
正在调用 GPT...

========== AI Summary ==========

...

Markdown saved to:

output/20260628_050558.md
```

---

## Tech Stack

* Python
* OpenAI API
* Requests
* BeautifulSoup4
* python-dotenv

---

## Roadmap

### Version 1.0

* [x] URL validation
* [x] Webpage download
* [x] HTML parsing
* [x] GPT summary generation
* [x] Markdown export

### Future Plans

* Support X (Twitter)
* Support Reddit
* Support YouTube transcripts
* Generate article titles automatically
* Extract author and publish date
* Scheduled news monitoring
* Multi-Agent workflow

---

## License

MIT License
