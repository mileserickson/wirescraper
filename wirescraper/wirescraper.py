import pandas as pd
from selenium.webdriver import Firefox, Chrome


def get_article_title(article):
    sel = "h3.title"
    title = article.find_element_by_css_selector(sel)
    return title.text


def get_article_url(article):
    sel = "a.headline-link"
    a = article.find_element_by_css_selector(sel)
    return a.get_attribute('href')


def get_article_date(article):
    sel = "span.js-date"
    date = article.find_element_by_css_selector(sel)
    return pd.Timestamp(date.text).isoformat()[:10]


def get_article_author(article):
    sel = "p.author"
    author = article.find_element_by_css_selector(sel)
    return author.text[3:]


def get_article_summary(article):
    sel = "div.summary"
    summary = article.find_element_by_css_selector(sel)
    return summary.text


def get_article_data(article):
    return {
        'title': get_article_title(article),
        'date': get_article_date(article),
        'author': get_article_author(article),
        'summary': get_article_summary(article),
        'url': get_article_url(article)
    }


def scrape_section(url, browser):
    sel = "ul.section-posts-list li"
    articles = browser.find_elements_by_css_selector(sel)
    article_data = [get_article_data(article) for article in articles]
    return article_data