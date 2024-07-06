from langchain_community.agent_toolkits import GmailToolkit
from langchain_community.tools.gmail.create_draft import GmailCreateDraft
from langchain.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun

class CreateDraftTool():
  @tool("Create Draft")
  def create_draft(data):
    """
    	Useful to create an email draft.
      The input to this tool should be a pipe (|) separated text
      of length 3 (three), representing who to send the email to,
      the subject of the email and the actual message.
    """
    email, subject, message = data.split('|')
    gmail = GmailToolkit()
    draft = GmailCreateDraft(api_resource=gmail.api_resource)
    resutl = draft({
				'to': [email],
				'subject': subject,
				'message': message
		})
    return f"\nDraft created: {resutl}\n"
  
  @tool("search tool")
  def search_tool():
    return DuckDuckGoSearchRun()