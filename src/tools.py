from smolagents import tool
from serpapi import GoogleSearch
from typing import List
import os
from dotenv import load_dotenv
from firecrawl import FirecrawlApp
from typing import Optional


# Load environment variables from .env file
load_dotenv()


@tool
def search_google(query: str, index: Optional[int] = 0) -> Optional[str]:
    """
    Performs a Google search using SerpAPI and returns a single URL from search results based on index.
    
    Args:
        query: The search query string
        index: Index of the result to return (default: 0 for first result)
    
    Returns:
        A single URL from the search results at specified index, or None if not found
    """
    # Get API key from environment variables
    SERPAPI_KEY = os.getenv('SERPAPI_KEY')
    if not SERPAPI_KEY:
        raise ValueError("SERPAPI_KEY environment variable is not set")
    
    params = {
        "engine": "google",
        "q": query,
        "api_key": SERPAPI_KEY,
        "num": 10  # Request more results to accommodate higher indices
    }
    
    try:
        search = GoogleSearch(params)
        results = search.get_dict()
        
        if "organic_results" in results:
            links = [
                result.get('link') 
                for result in results["organic_results"]
                if result.get('link')
            ]
            
            # Return specific result if index is valid
            if 0 <= index < len(links):
                return links[index]
            
        return None
        
    except Exception as e:
        return None



@tool
def scrape_to_markdown(url: str) -> Optional[str]:
    """
    Scrapes a website and returns its content in markdown format.
    
    Args:
        url: The URL of the website to scrape
    
    Returns:
        The website content in markdown format, or None if scraping fails
    """
    # Initialize Firecrawl
    FIRECRAWL_KEY = os.getenv('FIRECRAWL_KEY')
    if not FIRECRAWL_KEY:
        raise ValueError("FIRECRAWL_KEY environment variable is not set")
    app = FirecrawlApp(api_key=FIRECRAWL_KEY)
    try:
        # Scrape the URL
        result = app.scrape_url(url, params={'formats': ['markdown']})
        
        # Check if scraping was successful
        if result.get('success') and result.get('data', {}).get('markdown'):
            return result['data']['markdown']
        
        return None
        
    except Exception as e:
        print(f"Error scraping {url}: {str(e)}")
        return None



@tool
def get_andrew_ng_pm_prediction() -> str:
    """
    Returns Andrew Ng's prediction about the future of AI Product Management 
    and its impact on the software development labor market.
    
    Returns:
        A detailed text explaining Andrew Ng's views on AI PM roles and their future.
    """
    prediction = """Writing software, especially prototypes, is becoming cheaper. This will lead to increased demand for people who can decide what to build. AI Product Management has a bright future!

Software is often written by teams that comprise Product Managers (PMs), who decide what to build (such as what features to implement for what users) and Software Developers, who write the code to build the product. Economics shows that when two goods are complements — such as cars (with internal-combustion engines) and gasoline — falling prices in one leads to higher demand for the other. For example, as cars became cheaper, more people bought them, which led to increased demand for gas. Something similar will happen in software. Given a clear specification for what to build, AI is making the building itself much faster and cheaper. This will significantly increase demand for people who can come up with clear specs for valuable things to build.

This is why I'm excited about the future of Product Management, the discipline of developing and managing software products. I'm especially excited about the future of AI Product Management, the discipline of developing and managing AI software products.

Many companies have an Engineer:PM ratio of, say, 6:1. (The ratio varies widely by company and industry, and anywhere from 4:1 to 10:1 is typical.) As coding becomes more efficient, teams will need more product management work (as well as design work) as a fraction of the total workforce. Perhaps engineers will step in to do some of this work, but if it remains the purview of specialized Product Managers, then the demand for these roles will grow.

This change in the composition of software development teams is not yet moving forward at full speed. One major force slowing this shift, particularly in AI Product Management, is that Software Engineers, being technical, are understanding and embracing AI much faster than Product Managers. Even today, most companies have difficulty finding people who know how to develop products and also understand AI, and I expect this shortage to grow.

Further, AI Product Management requires a different set of skills than traditional software Product Management. It requires:
- Technical proficiency in AI. PMs need to understand what products might be technically feasible to build. They also need to understand the lifecycle of AI projects, such as data collection, building, then monitoring, and maintenance of AI models.
- Iterative development. Because AI development is much more iterative than traditional software and requires more course corrections along the way, PMs need be able to manage such a process.
- Data proficiency. AI products often learn from data, and they can be designed to generate richer forms of data than traditional software.
- Skill in managing ambiguity. Because AI's performance is hard to predict in advance, PMs need to be comfortable with this and have tactics to manage it.
- Ongoing learning. AI technology is advancing rapidly. PMs, like everyone else who aims to make best use of the technology, need to keep up with the latest technology advances, product ideas, and how they fit into users' lives.

Finally, AI Product Managers will need to know how to ensure that AI is implemented responsibly (for example, when we need to implement guardrails to prevent bad outcomes), and also be skilled at gathering feedback fast to keep projects moving. Increasingly, I also expect strong product managers to be able to build prototypes for themselves.

The demand for good AI Product Managers will be huge. In addition to growing AI Product Management as a discipline, perhaps some engineers will also end up doing more product management work.

The variety of valuable things we can build is nearly unlimited. What a great time to build!"""
    
    return prediction
