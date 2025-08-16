import requests
from bs4 import BeautifulSoup


skills = ["engineering","python", "typescript", "javascript","AI"]
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"}
base = "https://berlinstartupjobs.com"

for skill in skills:
    if skill == "engineering":
        for x in range(2):
            if x == 0:
                base_url = f"{base}/engineering/"
            elif x == 1:
                base_url = f"https://berlinstartupjobs.com/engineering/page/{x+1}"
            else:
                base_url = f"{base}/skill-areas/{skill}/"

            response = (requests.get(base_url, headers=headers))
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

