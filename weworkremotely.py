import requests
from bs4 import BeautifulSoup


keyword = input("검색어를 입력하세요:").strip().lower()

# keyword = "Full-stack"   # (이 값은 이제 URL에 직접 반영함)
base = "https://weworkremotely.com/remote-full-stack-programming-jobs"  # ← 주소만 교체
# base = "https://weworkremotely.com/remote-python-jobs"                # 예: 파이썬일 때

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0 Safari/537.36"}

response = requests.get(base, headers=headers)   # ← params 제거
soup = BeautifulSoup(response.text, "html.parser")

sections = soup.find_all("section", class_="jobs")
for section in sections:
    jobs = section.find_all("li", class_="feature")
    for job in jobs:
        title = job.find("h4", class_="new-listing__header__title").get_text()
        a_tag = job.select_one('a[href^="/remote-jobs/"]')
        notice_url = "https://weworkremotely.com" + a_tag["href"]
        company = job.find("p", class_="new-listing__company-name").get_text()
        location = job.find("p", class_="new-listing__company-headquarters").get_text()

        print("\n🎉Skill: Full-stack")
        print("⭐Title:", title)
        print("⭐Company:", company)
        print("⭐Location:", location)
        print("⭐Notice URL:", notice_url)
