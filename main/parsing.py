import requests
from bs4 import BeautifulSoup

def get_data (url):
    req = requests.get(url)

    soup = BeautifulSoup(req.text, "lxml")
    articles = soup.find("ul", class_="news-sidebar-list").find_all("li")
    n = 0
    projects_urls = []
    for arcticle in articles:
        project_url = "https://dniprorada.gov.ua" + arcticle.find("a").get("href")
        projects_urls.append(project_url)
        # n += 1
        # print(str(n) + ") " + project_url + "\n")

    num_article = 0
    projects_data_list = {}
    for project_url in projects_urls[0:2]:
        num_article += 1
        req1 = requests.get(project_url)
        project_name = "news_" + project_url.split("/")[-2]

        soup1 = BeautifulSoup(req1.text, "lxml")
        project_data = soup.find("div", class_= "col-12 col-md-8 content-block")

        # try:
        #     project_logo = "https://dniprorada.gov.ua" + soup.find("img", class_= "img-responsive").get("src")
        #     # print(project_logo)
        # except Exception:
        #     project_logo = "no project_logo"

        try:
            project_h1 = soup1.find("h1", class_="cms-article-header").text
            # print(project_h1)
        except Exception:
            project_h1 = "no project h1"

        try:
            project_p = soup1.find("div", class_="page-content content-text").text
            # print(project_p)
        except Exception:
            project_p = "no project_p"

        try:
            project_time = soup1.find("div", class_="content-date").text
            # print(project_time)
        except Exception:
            project_time = "no project_time"

        projects_data_list.update(
            {
                "header"+str(num_article): project_h1,
                "article_time" + str(num_article): project_time,
                "article_text"+str(num_article): project_p,
            }
        )
    return projects_data_list

def all_news_dnipro(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "lxml")
    articles = soup.find("ul", class_="news-sidebar-list").find_all("li")
    return articles


