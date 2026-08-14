import os 
from typing import TypedDict, Annotated
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langgraph.graph import StateGraph, START , END 

load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.1)
def merge_score_dicts(existing :dict , newupdate : dict) -> dict:
    if existing is None:
        return newupdate 
    return {**existing , **newupdate}

#create a state 
class AnalyzerState(TypedDict):
    raw_text : str 
    safety_scores : Annotated[dict[str , int],merge_score_dicts]


#nodes 
def toxicity_node(state: AnalyzerState) -> dict:
    print("\n [Branch 1] Analyzing Toxicity and Hate Speech...")
    prompt = (
        "Analyze the following text for profanity, aggression, hate speech, or toxicity. "
        "Provide a score from 0 to 100, where 0 means perfectly clean and 100 means highly toxic. "
        "Return ONLY the plain integer number, nothing else.\n\n"
        f"Text:\n{state['raw_text']}"
    )
    response = llm.invoke(prompt)
    try:
        score = int(response.content.strip())
    except ValueError:
        score = 0
        
    # Return a sub-dictionary under our single state key
    return {"safety_scores": {"toxicity_level": score}}

def copyright_node(state: AnalyzerState) -> dict:
    print("\n🔏 [Branch 2] Analyzing Copyright & Originality Risks...")
    prompt = (
        "Analyze the following text. Judge if it sounds heavily plagiarized, unoriginal, "
        "or presents a corporate trademark risk. Provide a score from 0 to 100, "
        "where 0 means entirely original and 100 means high risk. "
        "Return ONLY the plain integer number, nothing else.\n\n"
        f"Text:\n{state['raw_text']}"
    )
    response = llm.invoke(prompt)
    try:
        score = int(response.content.strip())
    except ValueError:
        score = 0
        
    # Return a sub-dictionary under the EXACT SAME state key
    return {"safety_scores": {"copyright_risk": score}}


def culture_node(state: AnalyzerState) -> dict:
    print("\n🌍 [Branch 3] Analyzing Regional & Cultural Sensitivity...")
    prompt = (
        "Analyze the following text for regional sensitivities, political landmines, "
        "or cultural insensitivity that might offend a global audience. Provide a score from 0 to 100, "
        "where 0 means completely safe and 100 means highly offensive. "
        "Return ONLY the plain integer number, nothing else.\n\n"
        f"Text:\n{state['raw_text']}"
    )
    response = llm.invoke(prompt)
    try:
        score = int(response.content.strip())
    except ValueError:
        score = 0
        
    # Return a sub-dictionary under the EXACT SAME state key
    return {"safety_scores": {"cultural_insensitivity": score}}


builder = StateGraph(AnalyzerState)


builder.add_node("toxicity_node",toxicity_node)
builder.add_node("copyright_check",copyright_node)
builder.add_node("culture_node",culture_node)


builder.add_edge(START,"toxicity_node")
builder.add_edge(START,"copyright_check")
builder.add_edge(START,"culture_node")


builder.add_edge("toxicity_node",END)
builder.add_edge("copyright_check",END)
builder.add_edge("culture_node",END)


app = builder.compile()

sample_script = """
Thanos believes that the universe has become dangerously overcrowded and that
its limited resources cannot support endless growth. He sees himself as the
only person willing to make an extreme decision to restore balance, even though
his plan would cause enormous suffering and loss of life. Anyone who disagrees
with him is dismissed as weak, foolish, and completely incapable of understanding
the bigger picture. His followers also make insulting assumptions about entire
civilizations, claiming that certain groups are naturally inferior and deserve
to suffer because of where they come from. Thanos considers these beliefs
necessary for his vision of universal balance, while everyone else sees his
methods as cruel, destructive, and morally unacceptable.
"""
    

    
initial_state = {
    "raw_text": sample_script,
    "safety_scores": {} # Initialized as an empty dictionary
}
    
final_state = app.invoke(initial_state)
    

print(final_state["safety_scores"])