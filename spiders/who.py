import requests
from bs4 import BeautifulSoup


def who_spider():
    """ Scrape faqs from who website """
    WHO_URL = "https://www.who.int/csr/disease/coronavirus_infections/faq_dec12/en/"
    who_faqs_page = requests.get(WHO_URL)

    soup = BeautifulSoup(who_faqs_page.content, "html.parser")

    faqs_container = soup.find(id="primary")
    questions = faqs_container.find_all("h3", class_="section_head1")
    answers = faqs_container.find_all("span")

    # Remove the first span item that contains a date
    answers.pop(0)

    faqs = dict(
        zip(
            [question.text for question in questions],
            [answer.text for answer in answers],
        )
    )

    return faqs
