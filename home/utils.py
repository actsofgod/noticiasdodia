from urllib.request import urlopen
from bs4 import BeautifulSoup


def get_globo_posts():
    all_posts = []
    res = urlopen("https://www.globo.com/")
    bs = BeautifulSoup(res, "html.parser")

    try:
        posts = bs.find_all("div", {"class": "hui-premium"})
        for post in posts:
            try:
                title = post.find("p", {"class": "hui-premium__title"})
                title = title.get_text().strip()
                link = post.find("a", {"class": "hui-premium__link"})
                link = link.get("href")
                notice = {"title": title, "link": link}
                all_posts.append(notice)
            except:
                pass

        return all_posts
    except:
        return None


def get_meiahr_posts():
    all_posts = []
    res = urlopen("https://meiahora.ig.com.br/")
    bs = BeautifulSoup(res, "html.parser")

    try:
        posts = bs.find_all("div", {"class": "box-hardnews-destaque"})
        for post in posts:
            try:
                title = post.find("p")
                title = title.get_text().strip()
                link = post.find("a")
                link = link.get("href")
                notice = {"title": title, "link": link}
                all_posts.append(notice)
            except:
                pass

        return all_posts
    except:
        return None
