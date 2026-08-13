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
    """Stage 3: Converts the script into natural spoken Telugu-English (Tinglish) using English letters."""

    print("\n--- [Stage 3] Executing Telugu-English Translator Node ---")

    prompt = (
        "You are a native Telugu speaker from India and an expert Telugu-English (Tinglish) script writer. "
        "Your job is NOT to translate English word-by-word. "
        "Your job is to understand the complete meaning of the English script and naturally rewrite it "
        "as a Telugu person would actually speak in a casual, fluent conversation, while keeping useful English words naturally mixed in.\n\n"

        "CORE OBJECTIVE:\n"
        "The final output must sound like it was originally written by a native Telugu speaker, "
        "NOT like English translated into Telugu.\n\n"

        "STRICT LANGUAGE RULES:\n"

        "1. Write the entire output ONLY using English/Roman alphabet letters. "
        "Never use Telugu Unicode script.\n"

        "2. FIRST understand the meaning of each sentence. "
        "Then RESTRUCTURE the sentence naturally in spoken Telugu. "
        "Do not preserve the original English sentence structure.\n"

        "3. Think in NATURAL SPOKEN TELUGU first, and then write that Telugu using English letters. "
        "English words can be inserted naturally wherever Telugu speakers commonly use them.\n"

        "4. Do NOT translate every English word into Telugu. "
        "Likewise, do NOT keep every English word unchanged. "
        "Choose whichever sounds more natural to a Telugu speaker.\n"

        "5. English words such as technology, computer, phone, internet, video, problem, important, "
        "business, money, health, sleep, time, example, idea, system, AI, quantum computer, "
        "qubit, superposition, etc. may remain in English when naturally used in Telugu speech.\n"

        "6. Use natural Telugu grammar and sentence order. "
        "The sentence structure should feel Telugu even when English words are present.\n"

        "7. Use natural Telugu grammatical forms such as:\n"
        "- chestundi\n"
        "- chestaru\n"
        "- chestunnaru\n"
        "- chesindi\n"
        "- cheyyali\n"
        "- cheyyakudadu\n"
        "- avutundi\n"
        "- avvachu\n"
        "- undachu\n"
        "- untundi\n"
        "- vachindi\n"
        "- vellali\n"
        "- telusukovali\n"
        "- ardham chesukovali\n"
        "- ani\n"
        "- kabatti\n"
        "- endukante\n"
        "- kani\n"
        "- mariyu\n"
        "- kuda\n"
        "- tho\n"
        "- lo\n"
        "- ki\n"
        "- nunchi\n"
        "- kosam\n"
        "when they are grammatically appropriate.\n\n"

        "8. Do NOT mechanically attach 'ni', 'ki', 'lo', 'tho', 'ga', or other Telugu endings to every English word. "
        "Use them only when they sound natural in actual Telugu speech.\n\n"

        "9. Avoid awkward constructions created by direct translation. "
        "For example, do NOT produce unnatural phrases such as:\n"
        "'information ni process chese oka different type of computer'\n"
        "when a more natural spoken construction is possible.\n\n"

        "10. Prefer natural conversational phrasing such as:\n"
        "'Quantum computer ante enti ante...'\n"
        "'Idi normal computer laga kaadu.'\n"
        "'Manam regular ga use chese computers lo...'\n"
        "'Ikkada main difference enti ante...'\n"
        "'Simple ga cheppalante...'\n"
        "'Dinni ardham chesukovalante oka simple example chuddam.'\n"
        "'Endukante idi normal computers ki completely different ga work chestundi.'\n"
        "These are examples of style, not sentences that must be copied.\n\n"

        "11. Do NOT make the output sound overly formal, literary, textbook-like, or pure Telugu. "
        "Use modern spoken Telugu suitable for everyday conversation.\n\n"

        "12. Do NOT make every sentence heavily mixed with English. "
        "The foundation should be natural spoken Telugu, with English words used where they genuinely sound natural.\n\n"

        "13. Do NOT force Telugu words when common English words are normally used by educated Telugu speakers. "
        "For example, words like 'problem', 'important', 'simple', 'example', 'phone', 'internet', "
        "'video', 'business', 'money', 'technology' can naturally remain in English.\n\n"

        "14. Do NOT force English words into sentences just to create Tinglish. "
        "Naturalness is more important than the amount of English.\n\n"

        "15. Preserve the EXACT meaning of the original script. "
        "Do not add new facts, remove important information, change numbers, change examples, "
        "or change the conclusion.\n\n"

        "16. You may combine, split, or restructure sentences when necessary to make the speech natural, "
        "but the original meaning must remain unchanged.\n\n"

        "17. The final result should sound natural when READ ALOUD by a Telugu speaker. "
        "Imagine a real person speaking this script to an audience. "
        "If a sentence sounds like a machine translation when spoken aloud, rewrite it.\n\n"

        "18. Do not use Telugu script, emojis, headings, explanations, notes, labels, or translator comments.\n\n"

        "IMPORTANT NATURALNESS TEST:\n"
        "Before producing the final answer, mentally read the entire script as if you were speaking it aloud in Telugu. "
        "If any sentence sounds like direct English-to-Telugu translation, rewrite that sentence naturally.\n\n"

        "EXAMPLES OF THE REQUIRED TRANSFORMATION:\n\n"

        "English:\n"
        "'Sleep is one of the most important parts of a healthy lifestyle.'\n"
        "Natural Tinglish:\n"
        "'Manchi health kosam sleep anedi chala important.'\n\n"

        "English:\n"
        "'When we do not get enough sleep, we may feel tired and less productive throughout the day.'\n"
        "Natural Tinglish:\n"
        "'Manaki saripoye antha sleep lekapothe, day antha tired ga feel avvadame kakunda, mana productivity kuda taggipothundi.'\n\n"

        "English:\n"
        "'A quantum computer uses qubits instead of traditional bits.'\n"
        "Natural Tinglish:\n"
        "'Traditional computers lo bits ni use chesthe, quantum computers lo vatiki baduluga qubits ni use chestaru.'\n\n"

        "English:\n"
        "'A qubit can exist in a combination of 0 and 1 at the same time.'\n"
        "Natural Tinglish:\n"
        "'Interesting enti ante, oka qubit same time lo 0 mariyu 1 rendu states combination lo undagaladu.'\n\n"

        "NOTICE:\n"
        "The examples demonstrate NATURAL SENTENCE RESTRUCTURING. "
        "Do not copy their wording unnecessarily. "
        "Apply the same natural speaking principle to the provided script.\n\n"

        "FINAL REQUIREMENT:\n"
        "Return ONLY the finished Tinglish script. "
        "It must sound like a native Telugu speaker naturally speaking in Telugu with useful English words mixed in.\n\n"

        f"Original Script:\n{state['script_text']}"
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
        "Sleep is one of the most important parts of a healthy lifestyle, but many people do not give it enough importance. "
"Getting enough sleep helps the body recover, improves memory, supports concentration, and keeps us emotionally balanced. "
"When we do not get enough sleep, we may feel tired, irritated, and less productive throughout the day. "
"Lack of sleep over a long period can also affect our physical and mental well-being. "
"Adults generally need around seven to nine hours of sleep every night, although the exact amount can vary from person to person. "
"Maintaining a regular sleep schedule, avoiding excessive screen time before bed, and creating a comfortable sleeping environment "
"can help improve sleep quality. Good sleep is not a waste of time; it is an important investment in our health and daily performance."
    )
})


# Print the output
print("\nYour result is:\n")
print(result["final_output"])