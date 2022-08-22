from django.views.generic import TemplateView
import requests
from bs4 import BeautifulSoup

class Home(TemplateView):
  template_name = "home.html"

  page = requests.get("https://github.com/trending")

  soup = BeautifulSoup(page.text, "html.parser")

  repos = soup.find(class_="application-main")

  box = repos.find_all(class_="Box-row")

  print(len(box))
  for eachrepo in box:
    repo = eachrepo.find_all('a')
    name = repo[1].get('href').split('/')
    repostar = repo[2].get_text()
    print("Profile_Name_of _repo", name[1])
    print("Repo_Name", name[2])
    print("Repo_Star", repostar)
    print("----------------------------------------------------------------------------------------------------------")
