# AI-Scripting

AI-Scripting is a small Streamlit application that:

- Loads a web page using Selenium + Google Chrome.
- Extracts and cleans the `<body>` content with BeautifulSoup.
- Sends the cleaned text to an Ollama model (`llama3.2` by default) to extract specific information based on your prompt.

---

## 1. Prerequisites

### 1.1 Python

- **Python 3.10+** (3.11+ recommended)
- `pip` available in your shell.

Check your versions:

```bash
python --version
pip --version
```

On some systems you may need to use:

```bash
python3 --version
pip3 --version
```

### 1.2 Google Chrome and ChromeDriver

This project uses Selenium with **Google Chrome**, so you need:

1. Google Chrome installed.
2. A compatible **ChromeDriver** for your Chrome version and operating system.

Go to the official Chrome for Testing page:

`https://googlechromelabs.github.io/chrome-for-testing/#stable`

Download the **stable** driver that matches:

- Your OS (Windows / macOS / Linux).
- Your architecture (x64, arm64, etc.).
- Your Chrome version (stable recommended).

After downloading:

1. Extract the archive.
2. Copy the ChromeDriver executable into the **root of this project** (the same folder where `main.py` lives).

By default, the code expects:

```python
chrome_driver_path = "./chromedriver"
```

If the driver file has a different name or location (for example `chromedriver.exe` or a subfolder), update the `chrome_driver_path` in `scrape.py` to match.

---

## 2. Installation by Operating System

### 2.1 Windows

1. **Clone or download the repository**

```bash
git clone <YOUR_REPO_URL>
cd scripting
```

2. **Create and activate a virtual environment**

```bash
python -m venv venv
venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Place ChromeDriver**

- Copy `chromedriver.exe` into the project root.
- If the file is not named exactly `chromedriver.exe` or is not in the root, adjust this line in `scrape.py`:

```python
chrome_driver_path = "./chromedriver.exe"
```

Use the correct path and filename for your setup.

---

### 2.2 macOS

1. **Clone or download the repository**

```bash
git clone <YOUR_REPO_URL>
cd scripting
```

2. **Create and activate a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Place ChromeDriver**

- Copy the `chromedriver` binary into the project root.
- Ensure it has execute permission:

```bash
chmod +x chromedriver
```

- Check that `scrape.py` has the correct path (default is fine if the file is in the root):

```python
chrome_driver_path = "./chromedriver"
```

---

### 2.3 Linux

1. **Clone or download the repository**

```bash
git clone <YOUR_REPO_URL>
cd scripting
```

2. **Create and activate a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Place ChromeDriver**

- Copy the `chromedriver` binary into the project root.
- Make sure it is executable:

```bash
chmod +x chromedriver
```

- Confirm or update this line in `scrape.py`:

```python
chrome_driver_path = "./chromedriver"
```

---

## 3. Ollama configuration

This project uses **Ollama** via `OllamaLLM` with the model `llama3.2`.

1. Install Ollama from the official website.
2. Download the model:

```bash
ollama pull llama3.2
```

3. Make sure the Ollama server is running before starting the app.

---

## 4. Running the application

From the project root, with the virtual environment activated:

```bash
streamlit run main.py
```

Streamlit will open your browser automatically or print a local URL like `http://localhost:8501` where you can access the app.

---

## 5. How to use the app

Inside the Streamlit UI:

1. **Enter a website URL**
   - Type the URL of the site you want to scrape.
   - You can also adapt the example text in `main.py` (there is a sample URL for testing).

2. **Click “Scrape Site”**
   - The app launches Chrome via Selenium.
   - It loads the page and extracts the `<body>` HTML.
   - The cleaned text is stored in the session and can be inspected in the **“View DOM Content”** expander.

3. **Describe what you want to parse**
   - In the text area “What do you want to parse?”, write a natural language description of the information you want (for example: “List all product names and prices found on the page”).

4. **Click “Parse Content”**
   - The DOM content is split into chunks and sent to the Ollama model.
   - The model returns only the information that matches your description.
   - The result is displayed under **“AI Result:”**.

---

## 6. Customization

### 6.1 Change the Ollama model

Open `parse.py` and update:

```python
model = OllamaLLM(model="llama3.2")
```

Replace `"llama3.2"` with the name of any other model you have installed in Ollama.

### 6.2 Adjust DOM chunk size

In `scrape.py`, the function `split_dom_content` controls how the DOM is split:

```python
def split_dom_content(dom_content, max_length=6000):
    ...
```

Increase or decrease `max_length` depending on your model limits and performance needs.

---

## 7. Common issues and troubleshooting

- **ChromeDriver version mismatch**  
  If Selenium complains about driver or browser version, download the correct ChromeDriver that matches your installed Chrome from the Chrome for Testing page.

- **Permissions on macOS/Linux**  
  If `chromedriver` cannot be executed, run:

  ```bash
  chmod +x chromedriver
  ```

- **Ollama not responding**  
  Check that:
  - The Ollama service is running.
  - The model (`llama3.2` or your custom one) is installed.
  - There are no connection errors in the terminal where you launched `streamlit run main.py`.

---

## 8. Project structure

- `main.py` – Streamlit UI.
- `scrape.py` – Selenium + BeautifulSoup scraping and DOM processing.
- `parse.py` – Integration with Ollama for parsing the text.
- `requirements.txt` – Python dependencies.
- `chromedriver` / `chromedriver.exe` – ChromeDriver binary placed in the project root.
