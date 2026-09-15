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
    "Teamworks", "Athlete", "NIL",
    "NFL", "NBA", "MLB", "NHL", "MLS", "PGA", "NASCAR", "UFC",
    "ESPN", "Fox Sports", "NBC Sports", "CBS Sports", "Turner Sports",
    "Bleacher Report", "The Athletic", "Sports Illustrated",
    "Nike", "Adidas", "Under Armour", "New Balance", "Puma",
    "Gatorade", "Powerade", "Wilson", "Callaway",
    "Red Bull", "Fanatics", "Ticketmaster", "Live Nation",
    "Sportradar", "Stats Perform",
    "WME Sports", "CAA Sports", "Wasserman", "Endeavor",
    "IMG", "Octagon",
    "University of Florida", "Florida Gators",
    "Opendorse" 
]
SENIOR_KEYWORDS = [
    "senior", "director", "manager", "lead", "principal", 
    "head", "chief", "vp ", "sr ", "sr."
]
def is_entry_level(job):
    title = job.get("job_title", "").lower()
    if not title:
        return False
    return not any(keyword in title for keyword in SENIOR_KEYWORDS)
def is_target_employer(job):
    employer = job.get("employer_name", "")
    if not employer:
        return False
    return any(target.lower() in employer.lower() for target in TARGET_EMPLOYERS)

def get_jobs():
    url = "https://jsearch.p.rapidapi.com/search-v2"
    headers = {
        "x-rapidapi-key": os.environ.get("RAPIDAPI_KEY"),
        "x-rapidapi-host": "jsearch.p.rapidapi.com",
    }
    
    all_jobs = []
    
    for employer in TARGET_EMPLOYERS:
        

        search_term = f"{employer} -senior -manager -director -vp"
        
        querystring = {
            "query": search_term,
            "num_pages": "2",
            "country": "us",
            "date_posted": "month",
            "employment_types": "INTERN,FULLTIME"
        }
        
        try:
            response = requests.get(url, headers=headers, params=querystring)
            response.raise_for_status() 
            
            jobs = response.json().get("data", {}).get("jobs", [])
            print(f"Scraped {len(jobs)} jobs searching for '{employer}'...")
            

            filtered = [
                job for job in jobs 
                if is_target_employer(job) and is_entry_level(job)
            ]
            
            if filtered:
                print(f"  Kept {len(filtered)} target jobs.")
                
            all_jobs.extend(filtered)
            
        except Exception as e:
            print(f"API Error on employer '{employer}': {e}")
            
    return all_jobs