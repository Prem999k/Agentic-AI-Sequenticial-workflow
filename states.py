#so now we are creating a graph 
# and the 1st thing you create is a state

import os

#1st way  typed DICT most common

from typing import TypedDict
class State(TypedDict):
    topic : str
    summary : str
    score : int

#2nd way  using pydantic 
#it is good at data validation and type checking at runtime

from pydantic import BaseModel,field_validator

class State(BaseModel):
    topic : str
    summary : str
    score : int

    @field_validator
    def score_positive(cls,v):
        if v < 0:
            raise ValueError("Score must be positive")
        
#3rd way python dataclass
#strandard py data class but it is used rarely 

from dataclasses import dataclass,field

@dataclass
class State:
    topic : str=""
    summary : str =""
    messages : list =field(default_factory=list)

#4th way using langgraph state class

from langgraph import MessagesState

class State(MessagesState):
    # messages filed is already included with add messages reducer
    #just add your extra fields
    user_name : str=""
    language : str=""
