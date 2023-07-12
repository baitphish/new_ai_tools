import requests
import json
import gspread

def get_new_ai_tools():
  """Returns a list of all the new AI tools and their abilities."""
  url = "https://api.github.com/search/repositories?q=created:>2023-01-01&language:python&stars:>100"
  response = requests.get(url)
  data = json.loads(response.content)
  tools = []
  for repo in data["items"]:
    if "AI" in repo["description"]:
      tools.append({
        "name": repo["name"],
        "description": repo["description"],
        "url": repo["html_url"],
      })
  return tools

def upload_tools_to_google_sheet(tools):
  """Uploads the list of new AI tools to a Google Sheet document."""
  sheet = gspread.create("New AI Tools")
  sheet.append_row(["Name", "Description", "URL"])
  for tool in tools:
    sheet.append_row(tool.values())

def github_launch():
  """Runs the script on GitHub."""
  tools = get_new_ai_tools()
  upload_tools_to_google_sheet(tools)

if __name__ == "__main__":
  github_launch()
