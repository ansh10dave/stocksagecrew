# Stocksagecrew Crew

Welcome to the Stocksagecrew Crew project 

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
### Customizing
- Modify `src/stocksagecrew/config/agents.yaml` to define your agents
- Modify `src/stocksagecrew/config/tasks.yaml` to define your tasks
- Modify `src/stocksagecrew/crew.py` to add your own logic, tools and specific args
- Modify `src/stocksagecrew/main.py` to add custom inputs for your agents and tasks

- I am currently running this with ollama - llama 3.2 vision model 11b
Modify crew.py: 
llm = LLM(model="ollama/llama3.2-vision11b", base_url="http://localhost:11434")

## Project Overview 
StockSageCrew is a GenAI-powered intelligent stock news scanner and explainer built using CrewAI. It automates the process of:

    🔎 Scanning the latest financial news from multiple online sources

    🧠 Analyzing and understanding the context of market-moving stories

    🗣️ Explaining the significance of top stock-related news in plain English

It uses a multi-agent approach to simulate a team of financial analysts powered by LLMs (Ollama/LLaMA3), configured through agents.yaml and tasks.yaml.

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```
## 🖥️ Streamlit UI Integration

This project now includes a **Streamlit UI** for running the CrewAI-based stock news scanner and displaying the results interactively.

### 🔧 How to Run the Streamlit App
Go to the root folder, 
```bash
$ streamlit run ui.py

```
Adding a Funtion calling for searching stocks
Now you can search for company and it shows the best matches for company names. Next I will add stock prices 

## Understanding Your Crew

The StockSageCrew Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.
