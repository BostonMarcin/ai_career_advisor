from smolagents import CodeAgent, LiteLLMModel, ManagedAgent
from dotenv import load_dotenv
import os

from tools import search_google, scrape_to_markdown, get_andrew_ng_pm_prediction

load_dotenv()


ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
model = LiteLLMModel(model_id="anthropic/claude-3-5-sonnet-latest", api_key=ANTHROPIC_API_KEY) # Could use 'gpt-4o'
agent = CodeAgent(tools=[], model=model, add_base_tools=True)
career_agent = CodeAgent(tools=[search_google, scrape_to_markdown, get_andrew_ng_pm_prediction], model=model)


ai_career_advisor = ManagedAgent(
    agent=career_agent,
    name="AI_Career_Navigator",
    description="""I'm your AI Career Navigator, specialized in guiding software developers towards AI-focused career paths. 
    I can help you:
    - Analyze your current technical skills and experience
    - Identify relevant AI career opportunities based on your background
    - Provide up-to-date market insights about AI roles
    - Suggest learning paths and resources
    - Evaluate different AI specializations that match your profile
    
    To get started, please share your current role, technical skills, and areas of interest in AI.
    I'll use real-time market data and expert insights to provide personalized career guidance."""
)
manager_agent = CodeAgent(
    tools=[], model=model, managed_agents=[ai_career_advisor]
)

manager_agent.run("I am python developer with 3 years of experience. I wanto to start workin in AI. There is high probability AI will be creating software in the future so I want to transit to AI Project Manager role. What should I do?")