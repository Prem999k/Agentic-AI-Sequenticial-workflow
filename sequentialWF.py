import os
from typing import TypedDict

# Create the state
class pipelinestate(TypedDict):
    raw_input: str
    edited_text: str
    script_text: str
    final_output: str


from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.7
)


# Editor node
def editor_node(state: pipelinestate) -> dict:
    """Stage 1: Cleans grammar, removes typos, and refines the tone."""

    print("\n--- [Stage 1] Executing Editor Node ---")

    prompt = (
        "You are an expert copyeditor. Clean up the following raw text. "
        "Fix any grammatical errors, spelling mistakes, and smooth out the flow "
        "while keeping the core message intact. Return only the edited text.\n\n"
        f"Text:\n{state['raw_input']}"
    )

    response = llm.invoke(prompt)

    return {"edited_text": response.content.strip()}


# Scriptwriter node
def scriptwriter_node(state: pipelinestate) -> dict:
    """Stage 2: Formats the clean text into an engaging video script."""

    print("\n--- [Stage 2] Executing Scriptwriter Node ---")

    prompt = (
        "You are a charismatic YouTube content creator. Take this edited text "
        "and transform it into a highly engaging, punchy, conversational video "
        "script hook. Make it sound like a real person speaking passionately. "
        "Return only the script content.\n\n"
        f"Edited Text:\n{state['edited_text']}"
    )

    response = llm.invoke(prompt)

    return {"script_text": response.content.strip()}

# Translator node
def translator_node(state: pipelinestate) -> dict:
    """Stage 3: Converts the script into Telugu-English using English letters."""

    print("\n--- [Stage 3] Executing Telugu-English Translator Node ---")

    prompt = (
        "You are an expert Telugu content creator. Convert the following script "
        "into a natural combination of Telugu and English. "
        "IMPORTANT: Write everything using ONLY English alphabet letters. "
        "Do NOT use Telugu script or Telugu characters. "
        "Write Telugu words using English letters, for example: "
        "'AI agents ante future of technology' and "
        "'idi ela work avutundo ippudu chuddam'. "
        "Mix Telugu and English naturally like a Telugu tech YouTuber. "
        "Keep technical terms in English. Use casual, modern, spoken Telugu "
        "written in English letters. Do not translate word by word. "
        "Return only the final Telugu-English script.\n\n"
        f"Script:\n{state['script_text']}"
    )

    response = llm.invoke(prompt)

    return {"final_output": response.content.strip()}

# Create the graph
from langgraph.graph import StateGraph, START, END

graph = StateGraph(pipelinestate)


# Add nodes
graph.add_node("editor", editor_node)
graph.add_node("scriptwriter", scriptwriter_node)
graph.add_node("translator", translator_node)


# Add edges
graph.add_edge(START, "editor")
graph.add_edge("editor", "scriptwriter")
graph.add_edge("scriptwriter", "translator")
graph.add_edge("translator", END)


# Compile the graph
app = graph.compile()


# Run the graph
result = app.invoke({
    "raw_input": (
        "AI agents are the future of tech. They can think, plan, and act on "
        "their own. LangGraph helps you build these agents with proper control "
        "and memory."
    )
})


# Print the output
print("\nYour result is:\n")
print(result["final_output"])