from langgraph.graph import StateGraph, START , END
from typing import TypedDict, Annotated
from langchain_core.messages import BaseMessage, HumanMessage
from langchain.schema import HumanMessage
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from langgraph.checkpoint.memory import MemorySaver



load_dotenv()
from langgraph.graph.message import add_messages
class ChatState(TypedDict):
    messages:Annotated[list[BaseMessage], add_messages]


# llm=ChatOpenAI()
llm = ChatOpenAI(
    # model="gpt-3.5-turbo",
    model="mistralai/mistral-7b-instruct:free",
    openai_api_base="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY")
)

def chat_node(state: ChatState):

    #take user query from state
    messages=state['messages']

    #send to llm
    response=llm.invoke(messages)

    #response store state
    return {'messages': [response]}
    

checkpointer=MemorySaver()

graph=StateGraph(ChatState)

graph.add_node('chat_node', chat_node)

graph.add_edge(START, 'chat_node')
graph.add_edge('chat_node', END)

chatbot=graph.compile(checkpointer=checkpointer)

initial_state={
    'messages': [HumanMessage(content='What is the capital of india')]
}
# chatbot.invoke(initial_state)
# chatbot.invoke(initial_state, config={"configurable": {"thread_id": "1"}})
# response=chatbot.invoke(initial_state)['messages'][-1].content
# print(response)


thread_id='1'
while True:
    
    user_message = input('type here: ')
    print('User:', user_message)

    if user_message.strip().lower() in ['exit', 'quit', 'bye']:
        break
    
    config={'configurable': {'thread_id': thread_id,"checkpoint_ns": "default"}}
    response = chatbot.invoke({'messages': [HumanMessage(content=user_message)]}, config=config)
    print('AI:',  response['messages'][-1].content)
  