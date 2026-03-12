# AtlasMind AI Travel Planner 🌍

AtlasMind is an intelligent travel planning application that generates personalized travel itineraries using AI. The app combines large language models with real-time web search to produce structured day-by-day travel plans that can be exported directly into a calendar.

Built using Streamlit, LangChain, and Google Gemini, AtlasMind acts as an AI-powered travel assistant capable of researching destinations and organizing trip schedules automatically.

# About

Author / Developer : 
mail :

## Features

🌍 AI-Powered Travel Planning using Gemini LLM

🔎 Real-time Web Search using SerpAPI

📅 Day-by-Day Itinerary Generation

📥 Downloadable Calendar Export (.ics)

⚡ Fast Cached AI Agent for Better Performance

🖥 Interactive Web Interface built with Streamlit

## Technology Stack

Python

Streamlit

LangChain

Google Gemini

SerpAPI

icalendar

## Project Structure
AtlasMind-AI-Travel-Planner<br>
│<br>
├── AI_travel.py<br>
├── requirements.txt<br>
├── README.md<br>
├── .gitignore<br>
│── .streamlit<br>
    └── secrets.toml
## Installation

Clone the repository

git clone https://github.com/yourusername/AtlasMind-AI-Travel-Planner.git
cd AtlasMind-AI-Travel-Planner

Install dependencies

pip install -r requirements.txt

Set up API keys (see API Keys section)

## Run the application

streamlit run AI_travel.py

The application will open in your browser at:

http://localhost:8501
API Keys Setup

## AtlasMind requires two API keys:

Google Gemini API key

SerpAPI key

Create the following file:

.streamlit/secrets.toml

Add your keys:

GEMINI_API_KEY = "your_gemini_api_key"
SERP_API_KEY = "your_serpapi_key"

⚠️ Important: Never upload secrets.toml to GitHub. It is already excluded in .gitignore.

## Usage

Enter a travel destination

Select the number of days for the trip

Click Generate Itinerary

View your AI-generated travel plan

Download the itinerary as a calendar (.ics) file

## Example Output
Day 1: Arrival and city exploration
Day 2: Historical landmarks and museums
Day 3: Local food tour and cultural experiences
Day 4: Nature or adventure activities
Day 5: Shopping and departure
Future Improvements

🌐 Google Maps route integration

💰 Travel budget estimation

🧠 User preference memory

🏨 Hotel and flight recommendations

☁ Cloud deployment for public access

## License

This project is licensed under the MIT License.


If you want, I can also help you add a professional GitHub header section with badges (Python, Streamlit, AI, License, Stars) so the repository looks much more impressive to recruiters and developers.








