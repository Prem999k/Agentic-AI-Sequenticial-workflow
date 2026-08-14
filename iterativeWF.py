import os
from typing import TypedDict,Annotated
from dotenv import load_dotenv
from langgraph.graph import StateGraph,START,END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch

load_dotenv()

# tools
search_tool=TavilySearch(max_results=3)
tools=[search_tool]

# llms
writer_llm=ChatGroq(model="openai/gpt-oss-120b",temperature=0.7)

writer_llm_with_tools = writer_llm.bind_tools(tools)

reviewer_llm=ChatGroq(model="openai/gpt-oss-20b",temperature=0.2)



# state
class State(TypedDict):
    topic:str
    messages:Annotated[list,add_messages]
    draft:str
    review_feedback:str
    is_approved:bool
    attempt:int

# writer node
WRITER_SYSTEM_PROMPT=(
    "You are an expert LinkedIn content writer. "
    "Write engaging, professional LinkedIn posts about the given topic. "
    "If the topic requires current information, statistics, or trends, "
    "use the web search tool before writing. "
    "If previous feedback is provided, fix every issue mentioned. "
    "Rules: strong hook in the first line, one clear takeaway, "
    "short paragraphs, around 150-200 words, end with a question or CTA, "
    "professional but human tone, and no hashtags."
)

def writer_node(state:State)->dict:
    attempt=state.get("attempt",0)+1
    topic=state["topic"]
    previous_feedback=state.get("review_feedback","")
    if attempt==1:
        user_message=(
            f"Write a LinkedIn post about: {topic}. "
            f"If current information is necessary, search the web first."
        )
    else:
        user_message=(
            f"Your previous LinkedIn post about '{topic}' was rejected.\n\n"
            f"Reviewer's feedback:\n{previous_feedback}\n\n"
            f"Write a new improved draft that fixes every issue. "
            f"Do not repeat the same mistakes. Return only the final post."
        )
    messages=[
        ("system",WRITER_SYSTEM_PROMPT),
        ("human",user_message)
    ]
    response=writer_llm_with_tools.invoke(messages)
    return{
        "messages":[("human",user_message),response],
        "attempt":attempt
    }

# tool node
tool_node=ToolNode(tools)


def extract_draft_node(state:State) -> dict:
    """After the writer finishes tool calls, pulls the final text out as the draft."""
    last_message = state['messages'][-1]
    draft = last_message.content 
     # print(f"\n\n generated post \n {draft} \n ")
    return {"draft" : draft}
 
# reviewer node
REVIEWER_SYSTEM_PROMPT=(
    "You are a strict LinkedIn content reviewer. "
    "Evaluate the post using these criteria: "
    "1. Strong hook in first line. "
    "2. One clear valuable takeaway. "
    "3. Easy to skim with short paragraphs. "
    "4. Approximately 150-200 words. "
    "5. Ends with an engaging question or CTA. "
    "6. Professional but human tone. "
    "7. No hashtags. "
    "8. Relevant to the topic. "
    "9. No unnecessary repetition. "
    "Respond exactly as:\n"
    "VERDICT: APPROVED or REJECTED\n"
    "FEEDBACK: <one short paragraph explaining why>"
)



def reviewer_node(state:State) -> dict:
    """Reviews the draft and decides: approve or reject with feedback."""
    draft = state['draft']

    prompt = (
        f"review this LinkedIn post draft : \n"
        f"{draft}\n"
        f"give your reviews"
    )
    response = reviewer_llm.invoke(
        [("system",REVIEWER_SYSTEM_PROMPT),("human",prompt)]
    )
    review_text = response.content.strip()
    
    is_approved = "APPROVED" in review_text.upper().split("FEEDBACK")[0]

    if "FEEDBACK:" in review_text:
        feedback = review_text.split("FEEDBACK:", 1)[1].strip()
    else:
        feedback = review_text

    verdict = "APPROVED" if is_approved else "REJECTED"
    print(f"[Verdict: {verdict}]")
    print(f"[Feedback: {feedback}]")

    return {
        "review_feedback": feedback,
        "is_approved": is_approved,
    }


# writer tool router
def should_use_tool(state:State):
    last_message=state["messages"][-1]
    if getattr(last_message,"tool_calls",None):
        return"tools"
    return"extract_draft"

# reviewer loop router
def should_stop_looping(state:State):
    if state["is_approved"]:
        print("\nPost approved.")
        return END
    if state["attempt"]>=3:
        print("\nMaximum attempts reached.")
        return END
    print("\nPost rejected. Sending feedback to writer...")
    return"writer"

# graph
graph=StateGraph(State)

# nodes
graph.add_node("writer",writer_node)
graph.add_node("tools",tool_node)
graph.add_node("extract_draft",extract_draft_node)
graph.add_node("reviewer",reviewer_node)

# edges
graph.add_edge(START,"writer")
graph.add_conditional_edges("writer",should_use_tool)
graph.add_edge("tools","writer")
graph.add_edge("extract_draft","reviewer")
graph.add_conditional_edges("reviewer",should_stop_looping)

app=graph.compile()

# application
print("="*55)
print("Welcome to the LinkedIn Post Generator")
print("="*55)
print("This tool will draft, research, review, and improve your post.")
print("="*55)

topic=input("\nWhat topic do you want a LinkedIn post about?\n> ").strip()

if not topic:
    print("\nNo topic given. Exiting.")
else:
    print("\nStarting generation...\n")
    initial_state={
        "topic":topic,
        "messages":[],
        "draft":"",
        "review_feedback":"",
        "is_approved":False,
        "attempt":0
    }
    try:
        final_state=app.invoke(initial_state)
        print("\n"+"="*55)
        print("FINAL LINKEDIN POST")
        print("="*55)
        print(final_state.get("draft","No draft generated."))
        print("="*55)
        print(f"Total attempts: {final_state.get('attempt',0)}")
        print(f"Approved: {final_state.get('is_approved',False)}")
        print("="*55)
    except Exception as e:
        print(f"\nError: {e}")