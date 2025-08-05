from langchain.agents import initialize_agent, AgentType
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import Tool
from tools.weather_forecast_tool import get_weather_forecast
from tools.best_travel_days_tool import get_best_travel_days
from tools.suggest_destinations_tool import suggest_destinations_based_on_weather
from tools.trip_planner_tool import plan_trip
from tools.estimate_trip_cost_tool import estimate_trip_cost

GEMINI_API_KEY = "AIzaSyD_yut0jbXWrtSmSm6r0xiq3sBpyaIdIlQ"

llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=GEMINI_API_KEY)

tools = [
    Tool(name="GetWeatherForecast", func=get_weather_forecast, description="Get weather for a location and date range"),
    Tool(name="FindGoodDays", func=get_best_travel_days, description="Find good days for travel based on weather"),
    Tool(name="SuggestDestinations", func=suggest_destinations_based_on_weather, description="Suggest travel destinations based on preferences"),
    Tool(name="PlanTrip", func=plan_trip, description="Create a basic travel plan based on destination and duration"),
    Tool(name="EstimateBudget", func=estimate_trip_cost, description="Estimate travel cost based on location and days")
]

agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

def run_agent(user_input: str) -> str:
    return agent.run(user_input)
