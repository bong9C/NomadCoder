import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self, skills):
        self.skills = skills
        self.base = "https://berlinstartupjobs.com"
        self.headers = {
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
        }

    def job(self, page):
        html = (requests.get(page, headers=self.headers))
        soup = BeautifulSoup(response.content, "html.parser")

        container = soup.find("div", class_="bsj-template__b")

        for jobs in container.find_all("div", class_="bjs-jlid"):


skills = ["engineering","python", "typescript", "javascript","AI"]
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"}
base = "https://berlinstartupjobs.com"
response = (requests.get(base, headers=headers))
soup = BeautifulSoup(response.content, "html.parser")



        container = soup.find("div", class_="bsj-template__b")
        jobs = container.find_all("li",class_="bjs-jlid")

        for job in jobs:
            a_title = job.find("h4", class_="bjs-jlid__h")
            title = a_title.find("a").text
            notice_url = a_title.find("a")["href"]
            company = job.find("a",class_="bjs-jlid__b").text
            work = job.find("div", class_="bjs-jlid__description").text
            print(f"\n🎉Skill: {base_url}\n ⭐Title: {title}\n ⭐Company: {company}\n ⭐Work: {work}\n ⭐Notice URL: {notice_url}")
        print(len(jobs))
        print("    ")

