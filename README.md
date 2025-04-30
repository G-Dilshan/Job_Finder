# 🧠 AI Job Finder Assistant

An AI-powered job-finding assistant that fetches the latest jobs from LinkedIn and Naukri using intelligent tools integrated with LLMs (Gemini), Langchain, and FastMCP.

## 🚀 Features

- 🔍 Fetch jobs from LinkedIn and Naukri using Apify actors.
- 🤖 Integrate Google Gemini LLM via Langchain for intelligent processing.
- 🧰 Multi-Agent reasoning using FastMCP for job filtering and analysis.
- 🌐 Secure environment with `.env` configuration for API keys.
- 🧪 Modular structure for scalability and easy testing.

---

## 📦 Tech Stack

- **Programming Language**: Python 3.10+
- **Libraries**:
  - [Langchain](https://github.com/langchain-ai/langchain) for LLM interaction.
  - [Google Generative AI (Gemini)](https://ai.google.dev/) for AI-based processing.
  - [Apify](https://apify.com/) for job data extraction from LinkedIn.
  - [FastMCP](https://github.com/mcp-ai/fastmcp) for Multi-Agent Coordination.
  - **dotenv** for secure environment management.

---


## Deployment

### 1. Clone the repository:

```bash
git clone https://github.com/G-Dilshan/Job_Finder.git
cd job-finder-ai
```
### 2. Install dependencies:

```bash
pip install -r requirements.txt
```
### 3. Configure API Keys with .env File:

```bash
GOOGLE_API_KEY=your_google_api_key
APIFY_API_TOKEN=your_apify_api_token
LINKEDIN_APIFY_ACTOR=your_apify_actor_id
```

### 4. Run the Application:

```bash
streamlit run app.py
```



## Usage
### Once the application is running, you can interact with the system and get the latest job listings. The app will:

- Fetch job listings based on the parameters defined (such as job roles or keywords).
- Use Google Gemini for intelligent processing and filtering of job data.
- Use Apify for fetching jobs from LinkedIn.

---
