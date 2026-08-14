Agentic AI Workflows with LangGraph

A practical Agentic AI workflow project built with LangGraph that
demonstrates how LLM-based applications can be designed as structured
workflows instead of simple single-model chains.

The project covers multiple workflow patterns including Sequential,
Parallel, Conditional, Iterative, and Human-in-the-Loop (HITL)
workflows. It also includes a Streamlit application and sample
academic/fee documents that can be used as workflow inputs.

🚀 Project Overview

This project is focused on understanding the fundamentals of Agentic
AI and LangGraph orchestration.

Instead of asking one LLM to perform an entire task, the workflow
divides the task into smaller steps and controls how information moves
between them.

Core workflow patterns:

Sequential Workflow --- tasks execute one after another.

Parallel Workflow --- independent tasks execute concurrently.

Conditional Workflow --- the next step is selected based on a
condition.

Iterative Workflow --- a task is repeatedly improved using
feedback.

Human-in-the-Loop Workflow --- human approval or intervention is
added before continuing.

🧠 Workflow Architecture

                         ┌─────────────────────┐
                         │       INPUT         │
                         └──────────┬──────────┘
                                    │
                ┌───────────────────┼───────────────────┐
                │                   │                   │
                ▼                   ▼                   ▼
        ┌──────────────┐    ┌──────────────┐    ┌──────────────┐
        │  Sequential  │    │   Parallel   │    │ Conditional  │
        │   Workflow   │    │   Workflow   │    │   Workflow   │
        └──────┬───────┘    └──────┬───────┘    └──────┬───────┘
               │                   │                   │
               └───────────────────┼───────────────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │    Iterative      │
                         │     Workflow      │
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │ Human-in-the-Loop │
                         │      Workflow     │
                         └─────────┬─────────┘
                                   │
                                   ▼
                         ┌───────────────────┐
                         │   Final Output    │
                         └───────────────────┘

📁 Project Structure

Agentic-AI-Sequenticial-workflow/
│
├── app.py
├── sequentialWF.py
├── parallelWF.py
├── conditionalWF.py
├── iterativeWF.py
├── HumanInTheLoop.py
│
├── academics_handbook.pdf
├── fee_structure.pdf
│
├── requirements.txt
├── .gitignore
└── README.md

🔄 Workflow Patterns

1. Sequential Workflow

File: sequentialWF.py

A sequential workflow executes nodes in a fixed order.

Input
  ↓
Node A
  ↓
Node B
  ↓
Node C
  ↓
Output

Each step receives the result of the previous step.

Use cases:

Document processing

Multi-step content generation

Data transformation

Research → summarize → format

Structured LLM pipelines

2. Parallel Workflow

File: parallelWF.py

Parallel workflows allow independent tasks to execute separately before
combining their results.

              ┌──► Task A ──┐
Input ────────┼──► Task B ──┼──► Combine ──► Output
              └──► Task C ──┘

This is useful when tasks do not depend on each other.

Use cases:

Multiple independent LLM evaluations

Parallel research

Multi-perspective analysis

Faster workflow execution

3. Conditional Workflow

File: conditionalWF.py

A conditional workflow dynamically selects the next node based on the
current state.

                 ┌──► Path A
Input → Decision ┤
                 └──► Path B

For example:

Question
   ↓
Classify
   ↓
┌───────────────┐
│ Academic?     │── Yes ──► Academic workflow
│               │
│ Fee related?  │── Yes ──► Fee workflow
└───────────────┘

Use cases:

Routing questions

Agent selection

Query classification

Error handling

Dynamic decision-making

4. Iterative Workflow

File: iterativeWF.py

An iterative workflow repeatedly executes a task until a condition is
satisfied or a maximum number of attempts is reached.

Input
  ↓
Generate
  ↓
Evaluate
  ↓
Good enough?
 ┌──────┴──────┐
Yes           No
 ↓             ↓
END        Improve
              │
              └──────► Evaluate

This pattern is useful for self-correction and quality improvement.

Use cases:

Content refinement

Code improvement

AI response evaluation

Draft → review → revise

Quality-controlled generation

5. Human-in-the-Loop Workflow

File: HumanInTheLoop.py

Human-in-the-loop workflows introduce a human decision point into an
automated workflow.

AI Task
  ↓
AI Result
  ↓
Human Review
  ↓
┌──────────────┐
│ Approve?     │
└──────┬───────┘
       │
   ┌───┴───┐
  Yes      No
   ↓        ↓
 Continue  Revise

This is useful when an AI system should not make a final decision
without human oversight.

Use cases:

Approval workflows

Sensitive decisions

Document validation

AI-generated content review

Enterprise automation

📄 Sample Documents

The repository contains two sample PDF documents:

academics_handbook.pdf

Academic-related information that can be used as input for workflow
experiments.

fee_structure.pdf

Fee-related information that can be used for testing document-based
workflows and routing.

These documents make the project more practical by providing real input
data for experimenting with AI workflows.

🛠️ Tech Stack

Python

LangGraph

LangChain

Google Gemini

Groq

Tavily Search

Streamlit

python-dotenv

⚙️ Installation

1. Clone the repository

git clone https://github.com/Prem999k/Agentic-AI-Sequenticial-workflow.git
cd Agentic-AI-Sequenticial-workflow

2. Create a virtual environment

Using uv:

uv venv

Activate it on Windows:

.venv\Scripts\activate

3. Install dependencies

uv pip install -r requirements.txt

Or:

uv sync

if the project is configured with a pyproject.toml.

🔐 Environment Variables

Create a .env file in the project root:

GOOGLE_API_KEY=your_google_api_key
GROQ_API_KEY=your_groq_api_key
TAVILY_API_KEY=your_tavily_api_key

Never commit .env or API keys to GitHub.

▶️ Running the Workflows

Sequential

python sequentialWF.py

Parallel

python parallelWF.py

Conditional

python conditionalWF.py

Iterative

python iterativeWF.py

Human-in-the-Loop

python HumanInTheLoop.py

Streamlit Application

streamlit run app.py

🎯 What This Project Demonstrates

This project demonstrates the transition from traditional LLM calls to
stateful agentic workflows.

Key concepts covered:

Graph-based AI orchestration

Nodes and edges

State management

Conditional routing

Parallel execution

Iterative loops

Human approval

LLM integration

Tool calling

Workflow control

Multi-step reasoning

AI application development

💡 Why LangGraph?

LangGraph makes complex AI workflows easier to model as a graph.

Instead of writing large amounts of nested control logic, the
application can represent:

State + Nodes + Edges + Conditions

This makes workflows easier to understand, debug, extend, and maintain.

🔮 Future Improvements

Possible extensions include:

Add RAG with vector databases

Add persistent conversation memory

Add more tools and external APIs

Add structured output using Pydantic

Add LangSmith tracing and evaluation

Add authentication to the Streamlit application

Add more document types

Add multi-agent collaboration

Add production deployment

Add automated testing for each workflow

👨‍💻 Author

Prem Kumar
