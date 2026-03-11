import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, Tool, AgentType
from langchain_community.utilities import SerpAPIWrapper
from icalendar import Calendar, Event
from datetime import datetime, timedelta
import re


# -------------------- ICS Calendar Helper --------------------

def generate_ics_content(plan_text: str, start_date: datetime = None) -> bytes:

    cal = Calendar()
    cal.add('prodid', '-AtlasMind-AI-Travel-Planner-')
    cal.add('version', '2.0')

    if start_date is None:
        start_date = datetime.today()

    plan_text = plan_text.replace("Final Answer:", "").strip()

    day_pattern = re.compile(r'Day (\d+)[:\s]+(.*?)(?=Day \d+|$)', re.DOTALL)
    days = day_pattern.findall(plan_text)

    if not days:

        event = Event()
        event.add('summary', "Travel Itinerary")
        event.add('description', plan_text)
        event.add('dtstart', start_date.date())
        event.add('dtend', start_date.date())
        event.add("dtstamp", datetime.now())

        cal.add_component(event)

    else:

        for day_num, day_content in days:

            day_num = int(day_num)
            current_date = start_date + timedelta(days=day_num - 1)

            event = Event()
            event.add('summary', f"Day {day_num} Itinerary")
            event.add('description', day_content.strip())
            event.add('dtstart', current_date.date())
            event.add('dtend', current_date.date())
            event.add("dtstamp", datetime.now())

            cal.add_component(event)

    return cal.to_ical()


# -------------------- Load AI Agent --------------------

@st.cache_resource
def load_agent():

    gemini_llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",
        google_api_key=st.secrets["GEMINI_API_KEY"]
    )

    search = SerpAPIWrapper(
        serpapi_api_key=st.secrets["SERP_API_KEY"]
    )

    search_tool = Tool(
        name="google_search",
        func=search.run,
        description="Search the internet for travel attractions, activities and accommodations"
    )

    agent = initialize_agent(
        tools=[search_tool],
        llm=gemini_llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=False,
        handle_parsing_errors=True
    )

    return agent


agent = load_agent()


# -------------------- Streamlit UI --------------------

st.set_page_config(page_title="Navora AI", page_icon="🌍")

st.title("🌍 AtlasMind-AI-Travel-Planner")
st.caption("Intelligent Travel Planning Agent")

if "itinerary" not in st.session_state:
    st.session_state.itinerary = None


destination = st.text_input("Where do you want to travel?")

num_days = st.number_input(
    "Trip duration (days)",
    min_value=1,
    max_value=30,
    value=5
)


col1, col2 = st.columns(2)


# -------------------- Generate Itinerary --------------------

with col1:

    if st.button("Generate Itinerary"):

        if not destination:
            st.warning("Please enter a destination.")

        else:

            with st.spinner("🔍 Researching and planning your trip..."):

                prompt = f"""
                You are a professional travel planner.

                Create a clear day-by-day itinerary.

                Destination: {destination}
                Duration: {num_days} days

                Requirements:
                - Each day must start with "Day 1:", "Day 2:", etc
                - Include attractions, food places, and activities
                - Ensure realistic travel flow
                """

                response = agent.invoke({"input": prompt})
                response_text = response["output"]

                st.session_state.itinerary = response_text

                display_text = response_text.replace("Final Answer:", "").strip()

                st.subheader("📍 Your Travel Plan")
                st.write(display_text)


# -------------------- Download Calendar --------------------

with col2:

    if st.session_state.itinerary:

        ics_content = generate_ics_content(st.session_state.itinerary)

        st.download_button(
            label="📅 Download Calendar (.ics)",
            data=ics_content,
            file_name="travel_itinerary.ics",
            mime="text/calendar"
        )
