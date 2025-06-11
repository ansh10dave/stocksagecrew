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

## 🖥️ Streamlit UI Integration

This project now includes a Streamlit UI for interacting with the CrewAI-based stock assistant and displaying results interactively.
Features

    Company Name Extraction from user input using Ollama LLM
    Stock Symbol Search using Alpha Vantage API
    Real-time Stock Quote Retrieval via Alpha Vantage's Global Quote API
    Interactive Real-time Stock Charts embedded using TradingView’s free widget (no API key required)
    Clean display of company matches and stock details

### 🔧 How to Run the Streamlit App
Go to the root folder, 
```bash
$ streamlit run ui.py

```
Usage

    Enter a company's name or query about its stock in the input box.

    Click Check and get news to get company matches and the latest stock data. It also returns latest and relevant news about the company.

    View interactive charts for the stock that support time range selection (1m, 6m, 1y, 5y, etc.) powered by TradingView.

    It shows news and sentiment from the alpha vantage (alpha intelligence api)
	

## Functionality Highlights

Ollama LLM Usage

    Extracts company names from natural language prompts.
    Connects to your locally running Ollama server (http://localhost:11434/api/generate).

Alpha Vantage API Integration

    Searches for stock symbols matching the extracted company name.
    Fetches real-time stock quote data (price, open, high, low, volume, etc.).

Interactive Stock Chart

    Uses TradingView’s free iframe widget for embedding professional-grade interactive charts.
    No need for additional API keys or backend integration for chart rendering.

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```


## Understanding Your Crew

The StockSageCrew Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.
