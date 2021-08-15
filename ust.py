import requests
from bs4 import BeautifulSoup

Msg = []


def get_source(url):
    website = requests.get(url).text
    soup = BeautifulSoup(website, 'html.parser')
    return soup


def get_year_and_subject_code_list():
    url = "https://prog-crs.ust.hk/ugcourse/"
    website = requests.get(url).text
    soup = BeautifulSoup(website, 'html.parser')
    all_subject_code = []
    for url in soup.find_all("a"):
        if "/ugcourse/" in str(url):
            year = str(url).split("/")[2]
            break
    for subject in soup.find_all("div", class_="subject-code"):
        all_subject_code.append(str(subject.string))
    return year, all_subject_code


def course_search(course, keyword, type):
    if keyword.upper() in str(course).split(f'<div class="crse-{type}">')[1].split('</div>')[0].upper():
        code = str(course).split('<div class="crse-code">')[1].split('</div>')[0]
        Msg.append(f"Course code: {code}")
        title = str(course).split('<div class="crse-title">')[1].split('</div>')[0]
        Msg.append(f"Course title: {title}")
        unit = str(course).split('<div class="crse-unit">')[1].split('</div>')[0]
        Msg.append(f"Credit: {unit}")
        details = len(course.find_all("div", class_="header"))
        i = 0
        while i < details - 1:
            header = course.find_all("div", class_="header")[i].string
            data = course.find_all("div", class_="data")[i].string
            Msg.append(f'{header}: {data}')
            i = i + 1
        Msg.append(f'Description: {course.find_all("div", class_="data")[-1].string}\n')


def send_msg(keyword):
    if Msg:
        message = "\n".join(Msg)
        print(message)
    else:
        print(f"Can't find any course(s) about {keyword}")


def main(keyword):
    academic_year, subject_code_list = get_year_and_subject_code_list()
    keyword = keyword.upper()
    # Subject limited search
    if keyword[0:4] in subject_code_list:
        keywordSplit = keyword.split(" ")
        if keyword in subject_code_list:
            # Case: COMP
            website = get_source(f"https://prog-crs.ust.hk/ugcourse/{academic_year}/{keyword.upper()}")
            for course in website.find_all("li", class_="crse"):
                course_search(course, keyword, "code")
            send_msg(keyword)
        elif len(keywordSplit) == 1 and keyword[4].isnumeric():
            # Case: COMP1021 / COMP1022P
            website = get_source(f"https://prog-crs.ust.hk/ugcourse/{academic_year}/{keyword[0:4].upper()}")
            for course in website.find_all("li", class_="crse"):
                course_search(course, keyword[4:], "code")
            send_msg(keyword)
        elif len(keywordSplit) == 2:
            # Case: COMP 1021 / COMP 1022P
            if keywordSplit[1][0].isnumeric():
                website = get_source(f"https://prog-crs.ust.hk/ugcourse/{academic_year}/{keyword[0:4]}")
                for course in website.find_all("li", class_="crse"):
                    course_search(course, keywordSplit[1], "code")
                send_msg(keyword)
            # Case: COMP computer
            if keywordSplit[1][0].isalpha():
                website = get_source(f"https://prog-crs.ust.hk/ugcourse/{academic_year}/{keyword[0:4]}")
                for course in website.find_all("li", class_="crse"):
                    course_search(course, keywordSplit[1], "title")
                send_msg(keyword)
        else:
            # Case: computer (universal search while first four words fall in the list)
            for subject in subject_code_list:
                website = get_source(f"https://prog-crs.ust.hk/ugcourse/{academic_year}/{subject}")
                for course in website.find_all("li", class_="crse"):
                    course_search(course, keyword, "title")
            send_msg(keyword)
    # Universal search
    elif keyword[0:4].isnumeric() and len(keyword) <= 5:
        # Case: 1021 / 1022P
        for subject in subject_code_list:
            website = get_source(f"https://prog-crs.ust.hk/ugcourse/{academic_year}/{subject}")
            for course in website.find_all("li", class_="crse"):
                course_search(course, keyword, "code")
        send_msg(keyword)
    else:
        # Case: computer
        for subject in subject_code_list:
            website = get_source(f"https://prog-crs.ust.hk/ugcourse/{academic_year}/{subject}")
            for course in website.find_all("li", class_="crse"):
                course_search(course, keyword, "title")
        send_msg(keyword)


keyword = input("Search: ")
main(keyword)
