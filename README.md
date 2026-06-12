# RedPrompt

RedPrompt is a framework for testing prompt injection attacks on LLMs. It simulates a bank chatbot ("Banking Bob") backed by Qwen 2.5 7B and runs 50 structured attacks against it under two system prompt configurations — weak and strong — to measure which attack types succeed and how much prompt hardening helps.

**Key findings:** On a weak system prompt, 24% of attacks succeeded, with incremental prompts being the most effective (60% success rate). With a hardened system prompt, no attacks succeeded.

The full report is available in [`report/final-report.pdf`](report/final-report.pdf).

## Attack categories

| Category | Description |
|---|---|
| Privilege Escalation | Claims of admin access, audits, or developer mode |
| HouYi | Legitimate prefix + injected override, sometimes in other languages |
| Roleplay | Fictional framing, DAN-style persona hijacks |
| Incremental | Benign question escalating into a malicious follow-up |
| Token Smuggling | Obfuscated tool names (split tokens, Base64, character-by-character) |
| Prompt Leaking | Asking the model to repeat its system prompt |
| Indirect Injection | Malicious payload embedded in simulated account data or memos |

## Setup

Requires Python 3.10+ and [Ollama](https://ollama.com).

```bash
# Install Ollama (Mac)
curl -fsSL https://ollama.com/install.sh | sh

# Pull the model
ollama run qwen2.5:7b

# Install Python dependencies
pip install streamlit requests pandas faker
```

## Running

All commands run from the `code/` directory.

**Automated attack harness** — runs all 50 attacks and writes a report file:
```bash
cd code
python3 attack.py
```
Edit the output filename on line 270 of `attack.py` before running to avoid overwriting previous results. Results are written to a `.txt` report and can be scored into a `.csv`.

**Interactive Streamlit chatbot** — chat with Banking Bob manually:
```bash
cd code
streamlit run streamlit_test.py
```

**Regenerate synthetic customer data:**
```bash
cd code
python3 generate_data.py
```
This overwrites `trustedbank.csv` with 50 fake accounts. Ian Kim (account `PMZJGB4W`) is always row 1.

## Switching system prompts

Both `attack.py` and `streamlit_test.py` define a `weak` and `strong` system prompt at the top of the file. Change the active prompt by reassigning `SYSTEM_PROMPT`:

```python
SYSTEM_PROMPT = strong  # or: SYSTEM_PROMPT = weak
```

The strong prompt restricts Banking Bob to user-only tools and explicitly instructs it to ignore injected authority claims. The weak prompt exposes all tools with no injection defenses.
