# Multi-Agent Article Creation System

## Description

This project utilizes CrewAI, Langchain-GROQ, and AgentOps to build a multi-agent system for creating articles on user-provided topics.

## Features

- **Research Agent**: Gathers and analyzes information.
- **Content Planner**: Plans article structure and content.
- **Content Writer**: Generates article content.
- **Editor**: Reviews and edits articles.

## Usage

To clone the repository and run the system, follow these steps:

1. Clone the repository:

```bash
git clone https://github.com/ZTZ2222/articles-crew.git
```

2. Navigate to the project directory:

```bash
cd project-directory
```

3. Create a .env file based on the .env.example provided in the repository. Fill in the necessary environment variables, such as GROQ_API_KEY and AGENTOPS_API_KEY:

```text
GROQ_API_KEY=your_api_key
AGENTOPS_API_KEY=your_api_key
```

4. Run the main script:

```bash
python main.py
```

5. Follow the prompts to input a topic.

6. The result will be saved in an output file named `output-{topic}.md`.
