import os
from agents import Agents 
from tasks import Tasks
from gmail_service import get_mails
from crewai import Crew


#Agents
email_categorizing_agent = Agents.email_categorizer_agent()
email_researcher_agent = Agents.email_researcher_agent()
email_writing_agent = Agents.email_drafting_agent()

#Tasks
emails = get_mails()

email_categorizing_task = Tasks.categorize_emails_task(email_categorizing_agent, emails)
email_researching_task = Tasks.research_email_task(email_researcher_agent, emails)
email_drafting_task = Tasks.draft_email_task(email_writing_agent, emails)

email_researching_task.context = [email_categorizing_task]
email_drafting_task.context = [email_categorizing_task, email_researching_task] 

#Build and Launch Crew
crew = Crew(
    agents = [email_categorizing_agent, email_researcher_agent, email_writing_agent],
    tasks = [email_categorizing_task, email_researching_task, email_drafting_task]
)

result = crew.kickoff()
print(result)