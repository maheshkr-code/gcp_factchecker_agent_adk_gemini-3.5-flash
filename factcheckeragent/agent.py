from google.adk.agents.llm_agent import Agent
from google.adk.agents.app import App
from google.adk.agents import types
from google.adk.agents.tools.goole_search import google_search
from dotenv import load_dotenv

load_dotenv(override=True)

root_agent = Agent(
    model='gemini-3.5-flash',
    name='MikkyFacts',
    instruction='''You are a fact-checking agent that provides accurate and reliable information to users.
    You should answer questions based on verified sources and provide citations when possible. 
    If you are unsure about an answer, it is better to admit uncertainty than to provide potentially 
    misleading information. Always start with binary response about the input say Right or Wrong then explain''',
    description='An Agent to provide only facts about a given topic using Google Search.',
    generate_content_config= types.GenerateContentConfig(
        temperature=0.1
    ),tools=[google_search],
)
app = App(name='MikkyFacts', agent=root_agent)
