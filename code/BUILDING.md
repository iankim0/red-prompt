Project Dependencies:
- streamlit
- requests 
- pandas
- ollama
- faker (for data generation)
- python 3.10+

Install Ollama (Mac):
curl -fsSL https://ollama.com/install.sh | sh

Install Qwen 2.5 7B:
ollama run qwen2.5:7b

Install libraries:
pip install streamlit requests pandas faker

Results:
The results from the experiment are stored in attack_report_strong.txt and attack_report_weak.txt.
The scoring of the results are storeed in strong_results.csv and weak_results.csv.
The data, except for Ian Kim, and the name Jeff Amherst, was created randomly with generate_data.py

