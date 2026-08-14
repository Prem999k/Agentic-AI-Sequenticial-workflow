# 🧠 Agentic AI Workflows using LangGraph

A practical **Agentic AI workflow project** built using **LangGraph and LangChain** that demonstrates how LLM-powered applications can be designed using different workflow patterns such as **Sequential, Parallel, Conditional, Iterative, and Human-in-the-Loop workflows**.

The project focuses on understanding how AI agents can be orchestrated using **state, nodes, edges, conditional routing, loops, tool calls, and human intervention**.

---

## 📌 Project Overview

Agentic AI systems often require multiple steps instead of a single LLM call.

This project demonstrates how **LangGraph** can be used to connect multiple processing steps into controlled workflows.

Each workflow represents a different way of coordinating AI tasks:

- **Sequential Workflow** — executes tasks one after another
- **Parallel Workflow** — executes independent tasks simultaneously
- **Conditional Workflow** — dynamically routes tasks based on conditions
- **Iterative Workflow** — repeatedly improves results using feedback
- **Human-in-the-Loop Workflow** — introduces human approval into the AI process

The project also includes sample academic and fee-related PDF documents that can be used as inputs for document-based AI workflows.

---

## ✨ Features

- 🤖 Agentic AI workflow orchestration
- 🔗 Sequential workflow execution
- ⚡ Parallel workflow execution
- 🔀 Conditional workflow routing
- 🔄 Iterative workflow with feedback
- 👤 Human-in-the-Loop workflow
- 🧠 Stateful LangGraph workflows
- 🛠️ LLM and tool integration
- 📄 PDF-based workflow inputs
- 🌐 Streamlit application
- 🔐 Environment variable support
- 🧩 Modular workflow architecture

---

## 🏗️ System Architecture

```text
                         User Input
                             │
                             ▼
                    ┌─────────────────┐
                    │    LangGraph    │
                    │      State      │
                    └────────┬────────┘
                             │
          ┌──────────────────┼──────────────────┐
          │                  │                  │
          ▼                  ▼                  ▼
    Sequential           Parallel          Conditional
     Workflow             Workflow           Workflow
          │                  │                  │
          └──────────────────┼──────────────────┘
                             │
                             ▼
                      Iterative Workflow
                             │
                             ▼
                   Human-in-the-Loop
                             │
                             ▼
                        Final Output

🔄 Workflow Patterns
1. 🔗 Sequential Workflow

File: sequentialWF.py

The Sequential Workflow executes tasks in a fixed order where the output of one step becomes the input for the next step.

Input
  ↓
Node 1
  ↓
Node 2
  ↓
Node 3
  ↓
Output
Use Cases
Multi-step AI processing
Document processing
Content generation
Research pipelines
Data transformation
LLM chains
2. ⚡ Parallel Workflow

File: parallelWF.py

The Parallel Workflow executes independent tasks separately and combines their results.

                    ┌──► Task 1 ──┐
                    │             │
Input ──────────────┼──► Task 2 ──┼──► Combine ──► Output
                    │             │
                    └──► Task 3 ──┘

Parallel execution is useful when multiple tasks do not depend on each other.

Use Cases
Parallel research
Multiple LLM evaluations
Multi-perspective analysis
Independent AI tasks
Faster processing
3. 🔀 Conditional Workflow

File: conditionalWF.py

The Conditional Workflow dynamically determines the next step based on a condition or the current state.

                         Input
                           ↓
                       Decision
                      /   |   \
                     /    |    \
                    ▼     ▼     ▼
                 Node A Node B Node C
                    \     |     /
                     \    |    /
                      ▼   ▼   ▼
                        Output
Use Cases
Query routing
Intent classification
Decision making
Dynamic AI workflows
Agent selection
Task-specific processing
4. 🔄 Iterative Workflow

File: iterativeWF.py

The Iterative Workflow generates an output, evaluates it, and improves it using feedback until the required condition is satisfied or the maximum number of attempts is reached.

Input
  ↓
Generate
  ↓
Review
  ↓
Approved?
 ┌───────┴───────┐
 │               │
Yes              No
 │               │
 ▼               ▼
END           Improve
                  │
                  └──────► Review
Example
Topic
  ↓
Writer
  ↓
Draft
  ↓
Reviewer
  ↓
Approved?
  ├── Yes → END
  └── No  → Writer → Improved Draft
Use Cases
AI content generation
Self-correction
Draft refinement
Quality control
Feedback-based generation
AI response evaluation
5. 👤 Human-in-the-Loop Workflow

File: HumanInTheLoop.py

The Human-in-the-Loop workflow introduces human approval or intervention into an automated AI workflow.

AI Task
  ↓
AI Result
  ↓
Human Review
  ↓
Approved?
 ┌───────┴───────┐
 │               │
Yes              No
 │               │
 ▼               ▼
Continue        Revise
Use Cases
AI content approval
Document validation
Sensitive decisions
Enterprise AI systems
Human supervision
Quality assurance
📄 Sample Documents

The project includes sample PDF documents that can be used as inputs for document-based AI workflows.

academics_handbook.pdf

Academic handbook containing information that can be used for document processing and AI-based question answering.

fee_structure.pdf

Fee structure document that can be used for fee-related queries and document-based workflow experiments.

These documents can later be integrated into a Retrieval-Augmented Generation (RAG) pipeline.

🧠 LangGraph Architecture

The project demonstrates the major building blocks of LangGraph.

State

State stores information shared between different workflow nodes.

State
 ├── Input
 ├── Messages
 ├── Results
 ├── Feedback
 └── Status
Nodes

Nodes represent individual tasks such as:

LLM calls
Tool calls
Python functions
Data processing
Decision logic
Edges

Edges define how nodes are connected.

Node A
  ↓
Node B
Conditional Edges

Conditional edges dynamically determine which node executes next.

Node A
  ↓
Condition
 ├── True  → Node B
 └── False → Node C
START and END

Every workflow has a starting point and termination point.

START
  ↓
Workflow
  ↓
END
🛠️ Technology Stack
Programming
Python
AI / LLM
LangChain
LangGraph
Google Gemini
Groq
Tools
Tavily Search
Application
Streamlit
Configuration
Python-dotenv
Version Control
Git
GitHub
📁 Project Structure
Agentic-AI-Sequenticial-workflow/
│
├── app.py
│
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
