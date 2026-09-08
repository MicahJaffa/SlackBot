import os
import requests
from dotenv import load_dotenv

load_dotenv()

QUERIES = [
    "sports marketing entry level",
    "sports media entry level",
    "sports communications entry level",
    "athletic department marketing",
    "sports content creator",
    "sports social media manager",
    "sports public relations",
    "NIL marketing",
    "sports broadcasting entry level",
    "sports journalism entry level",
    "sports sponsorship entry level",
    "sports digital media"
]

TARGET_EMPLOYERS = [
    # Pro Sports Leagues
    "NFL", "NBA", "MLB", "NHL", "MLS", "PGA", "NASCAR", "UFC",
    # Sports Media
    "ESPN", "Fox Sports", "NBC Sports", "CBS Sports", "Turner Sports",
    "Bleacher Report", "The Athletic", "Sports Illustrated",
    # Sportswear & Equipment
    "Nike", "Adidas", "Under Armour", "New Balance", "Puma",
    "Gatorade", "Powerade", "Wilson", "Callaway",
    # Sports Business
    "Red Bull", "Fanatics", "Ticketmaster", "Live Nation",
    "Sportradar", "Stats Perform",
    # Sports Agencies
    "WME Sports", "CAA Sports", "Wasserman", "Endeavor",
    "IMG", "Octagon",
    # Universities
    "University of Florida", "Florida Gators",
    # NIL Specific
    "Athlete", "NIL", "Opendorse", "Teamworks"
]
def is_target_employer(job):
    employer = job.get("employer_name", "").lower()
    return any(target.lower() in employer for target in TARGET_EMPLOYERS)

def get_jobs():
    url = "https://jsearch.p.rapidapi.com/search-v2"
    headers = {
        "x-rapidapi-key": os.environ["RAPIDAPI_KEY"],
        "x-rapidapi-host": "jsearch.p.rapidapi.com",
        "Content-Type": "application/json"
    }
    all_jobs = []
    for query in QUERIES:
        querystring = {
            "query": query,
            "num_pages": "1",
            "country": "us",
            "date_posted": "week",
            "employment_types": "INTERN,FULLTIME"
        }
        response = requests.get(url, headers=headers, params=querystring)
        jobs = response.json().get("data", {}).get("jobs", [])
        filtered = [job for job in jobs if is_target_employer(job)]
        all_jobs.extend(filtered)
    return all_jobs