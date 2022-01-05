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


def course_search(course, keyword, category, split):
    if split:
        i = 0
        for word in keyword:
            if word.upper() in str(course).split(f'<div class="crse-{category}">')[1].split('</div>')[0].upper():
                i = i + 1
            for description in course.find_all("div", class_="data"):
                if word.upper() in str(description).upper():
                    i = i + 1
        if i == len(keyword):
            code = str(course).split('<div class="crse-code">')[1].split('</div>')[0]
            course_search(course, code, "code", False)
    elif keyword.upper() in str(course).split(f'<div class="crse-{category}">')[1].split('</div>')[0].upper():
        code = str(course).split('<div class="crse-code">')[1].split('</div>')[0]
        if f"Course code: {code}" not in Msg:
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
    print("Searching...\n")
    academic_year, subject_code_list = get_year_and_subject_code_list()
    keyword_input = keyword
    keyword = keyword.upper()
    # Subject limited search
    if keyword[0:4] in subject_code_list:
        keywordSplit = keyword.split(" ")
        if keyword in subject_code_list:
            # Case: COMP
            website = get_source(f"https://prog-crs.ust.hk/ugcourse/{academic_year}/{keyword.upper()}")
            for course in website.find_all("li", class_="crse"):
                course_search(course, keyword, "code", False)
            send_msg(keyword_input)
        elif len(keywordSplit) == 1 and keyword[4].isnumeric():
            # Case: COMP1021 / COMP1022P
            website = get_source(f"https://prog-crs.ust.hk/ugcourse/{academic_year}/{keyword[0:4].upper()}")
            for course in website.find_all("li", class_="crse"):
                course_search(course, keyword[4:], "code", False)
            send_msg(keyword_input)
        elif len(keywordSplit) == 2:
            # Case: COMP 1021 / COMP 1022P
            if keywordSplit[1][0].isnumeric():
                website = get_source(f"https://prog-crs.ust.hk/ugcourse/{academic_year}/{keyword[0:4]}")
                for course in website.find_all("li", class_="crse"):
                    course_search(course, keywordSplit[1], "code", False)
                send_msg(keyword_input)
            # Case: COMP computer
            elif len(keywordSplit[0]) == 4 and keywordSplit[1][0].isalpha():
                website = get_source(f"https://prog-crs.ust.hk/ugcourse/{academic_year}/{keyword[0:4]}")
                for course in website.find_all("li", class_="crse"):
                    course_search(course, keywordSplit[1], "title", False)
                    for description in course.find_all("div", class_="data"):
                        if keywordSplit[1] in str(description).upper():
                            code = str(description.find_parents("li")).split('<div class="crse-code">')[1].split('</div>')[0]
                            course_search(course, code.split()[1], "code", False)
                send_msg(keyword_input)
            else:
                # Case: computer animation / electromagnetic waves
                for subject in subject_code_list:
                    website = get_source(f"https://prog-crs.ust.hk/ugcourse/{academic_year}/{subject}")
                    for course in website.find_all("li", class_="crse"):
                        course_search(course, keyword, "title", False)
                        for description in course.find_all("div", class_="data"):
                            if keyword.upper() in str(description).upper():
                                code = str(description.find_parents("li")).split('<div class="crse-code">')[1].split('</div>')[0]
                                course_search(course, code.split()[1], "code", False)
                send_msg(keyword_input)
        elif len(keywordSplit[0]) == 4 and keywordSplit[1] == "-A":
            # Case: isom -a government sustainable competitiveness optimizing
            website = get_source(f"https://prog-crs.ust.hk/ugcourse/{academic_year}/{keyword[0:4]}")
            for course in website.find_all("li", class_="crse"):
                course_search(course, keywordSplit[2:], "title", True)
            send_msg(keyword_input)
        else:
            # Case: phys electromagnetic waves
            website = get_source(f"https://prog-crs.ust.hk/ugcourse/{academic_year}/{keyword[0:4]}")
            for course in website.find_all("li", class_="crse"):
                course_search(course, keyword[5:], "title", False)
                for description in course.find_all("div", class_="data"):
                    if keyword[5:] in str(description).upper():
                        code = str(description.find_parents("li")).split('<div class="crse-code">')[1].split('</div>')[0]
                        course_search(course, code.split()[1], "code", False)
            send_msg(keyword_input)
    # Universal search
    elif keyword[0:4].isnumeric() and len(keyword) <= 5:
        # Case: 1021 / 1022P
        for subject in subject_code_list:
            website = get_source(f"https://prog-crs.ust.hk/ugcourse/{academic_year}/{subject}")
            for course in website.find_all("li", class_="crse"):
                course_search(course, keyword, "code", False)
        send_msg(keyword_input)
    elif keyword[0:2] == "-A":
        # Case: -a critical government sustainable competitiveness optimizing
        keywordSplit = keyword.split(" ")
        for subject in subject_code_list:
            website = get_source(f"https://prog-crs.ust.hk/ugcourse/{academic_year}/{subject}")
            for course in website.find_all("li", class_="crse"):
                course_search(course, keywordSplit[1:], "title", True)
        send_msg(keyword_input)
    else:
        # Case: python
        for subject in subject_code_list:
            website = get_source(f"https://prog-crs.ust.hk/ugcourse/{academic_year}/{subject}")
            for course in website.find_all("li", class_="crse"):
                course_search(course, keyword, "title", False)
                for description in course.find_all("div", class_="data"):
                    if keyword.upper() in str(description).upper():
                        code = str(description.find_parents("li")).split('<div class="crse-code">')[1].split('</div>')[0]
                        course_search(course, code.split()[1], "code", False)
        send_msg(keyword_input)


keyword = input("Search: ")
main(keyword)
