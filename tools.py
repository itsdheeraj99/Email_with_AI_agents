from langchain_community.agent_toolkits import GmailToolkit
from langchain_community.tools.gmail.create_draft import GmailCreateDraft
from langchain.tools import tool
from langchain_community.tools import DuckDuckGoSearchRun

class CreateDraftTool():
  @tool("Create Draft")
  def create_draft(data):
    """
    	Useful to create an email draft.
      
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