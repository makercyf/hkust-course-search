from telegram.ext import Updater, MessageHandler, Filters
from bs4 import BeautifulSoup
from sys import getsizeof
import requests



botToken = ""

operation = []

updater = Updater(token=botToken, use_context=True)
dispatcher = updater.dispatcher



def command(text):
    if text == "/start" or text == "/START":
        sendMsg(userID, "Yes, I am here.")
    if text == "/help" or text == "/HELP":
        sendMsg(userID, "Please check https://github.com/makercyf/hkust-course-search for acceptable input example.")



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
        if f"Course code: {code}" not in operation:
            operation.append(f"Course code: {code}")
            title = str(course).split('<div class="crse-title">')[1].split('</div>')[0]
            operation.append(f"Course title: {title}")
            unit = str(course).split('<div class="crse-unit">')[1].split('</div>')[0]
            operation.append(f"Credit: {unit}")
            details = len(course.find_all("div", class_="header"))
            i = 0
            while i < details - 1:
                header = course.find_all("div", class_="header")[i].string
                data = course.find_all("div", class_="data")[i].string
                operation.append(f'{header}: {data}')
                i = i + 1
            operation.append(f'Description: {course.find_all("div", class_="data")[-1].string}\n')



def send(keyword):
    if operation:
        message = "\n".join(operation)
        if getsizeof(message) > 4096:
            for i in range(0, getsizeof(message), 4096):
                sendMsg(chatID, message[i:i+4096])
        else:
            sendMsg(chatID, message)
        operation.clear()
    else:
        sendMsg(chatID, f"Can't find any course(s) about {keyword}")



def main(update, context):
    global chatID
    global userID
    global text
    global splitText
    global message
    global sendMsg
    sendMsg = context.bot.send_message
    message = update.message
    chatID = message["chat"]["id"]
    userID = message["from_user"]["id"]
    text = message["text"]
    splitText = text.split()
    academic_year, subject_code_list = get_year_and_subject_code_list()
    text_input = text
    text = text.upper()
    if text == "debug":
        sendMsg("[DEBUG] Working")
    elif text[0] == "/":
        command(text)
    # Subject limited search
    elif text[0:4] in subject_code_list:
        textSplit = text.split(" ")
        sendMsg(chatID, "Searching...")
        if text in subject_code_list:
            # Case: COMP
            website = get_source(f"https://prog-crs.ust.hk/ugcourse/{academic_year}/{text.upper()}")
            for course in website.find_all("li", class_="crse"):
                course_search(course, text, "code", False)
            send(text_input)
        elif len(textSplit) == 1 and text[4].isnumeric():
            # Case: COMP1021 / COMP1022P
            website = get_source(f"https://prog-crs.ust.hk/ugcourse/{academic_year}/{text[0:4].upper()}")
            for course in website.find_all("li", class_="crse"):
                course_search(course, text[4:], "code", False)
            send(text_input)
        elif len(textSplit) == 2:
            # Case: COMP 1021 / COMP 1022P
            if textSplit[1][0].isnumeric():
                website = get_source(f"https://prog-crs.ust.hk/ugcourse/{academic_year}/{text[0:4]}")
                for course in website.find_all("li", class_="crse"):
                    course_search(course, textSplit[1], "code", False)
                send(text_input)
            # Case: COMP computer
            elif len(textSplit[0]) == 4 and textSplit[1][0].isalpha():
                website = get_source(f"https://prog-crs.ust.hk/ugcourse/{academic_year}/{text[0:4]}")
                for course in website.find_all("li", class_="crse"):
                    course_search(course, textSplit[1], "title", False)
                    for description in course.find_all("div", class_="data"):
                        if textSplit[1] in str(description).upper():
                            code = str(description.find_parents("li")).split('<div class="crse-code">')[1].split('</div>')[0]
                            course_search(course, code.split()[1], "code", False)
                send(text_input)
            else:
                # Case: computer animation / electromagnetic waves
                for subject in subject_code_list:
                    website = get_source(f"https://prog-crs.ust.hk/ugcourse/{academic_year}/{subject}")
                    for course in website.find_all("li", class_="crse"):
                        course_search(course, text, "title", False)
                        for description in course.find_all("div", class_="data"):
                            if text.upper() in str(description).upper():
                                code = str(description.find_parents("li")).split('<div class="crse-code">')[1].split('</div>')[0]
                                course_search(course, code.split()[1], "code", False)
                send(text_input)
        elif len(textSplit[0]) == 4 and textSplit[1] == "-A":
            # Case: isom -a government sustainable competitiveness optimizing
            website = get_source(f"https://prog-crs.ust.hk/ugcourse/{academic_year}/{text[0:4]}")
            for course in website.find_all("li", class_="crse"):
                course_search(course, textSplit[2:], "title", True)
            send(text_input)
        else:
            # Case: phys electromagnetic waves
            website = get_source(f"https://prog-crs.ust.hk/ugcourse/{academic_year}/{text[0:4]}")
            for course in website.find_all("li", class_="crse"):
                course_search(course, text[5:], "title", False)
                for description in course.find_all("div", class_="data"):
                    if text[5:] in str(description).upper():
                        code = str(description.find_parents("li")).split('<div class="crse-code">')[1].split('</div>')[0]
                        course_search(course, code.split()[1], "code", False)
            send(text_input)
        # Universal search
    elif text[0:4].isnumeric() and len(text) <= 5:
        sendMsg(chatID, "Searching...")
        # Case: 1021 / 1022P
        for subject in subject_code_list:
            website = get_source(f"https://prog-crs.ust.hk/ugcourse/{academic_year}/{subject}")
            for course in website.find_all("li", class_="crse"):
                course_search(course, text, "code", False)
        send(text_input)
    elif text[0:2] == "-A":
        sendMsg(chatID, "Searching...")
        # Case: -a critical government sustainable competitiveness optimizing
        keywordSplit = text.split(" ")
        for subject in subject_code_list:
            website = get_source(f"https://prog-crs.ust.hk/ugcourse/{academic_year}/{subject}")
            for course in website.find_all("li", class_="crse"):
                course_search(course, keywordSplit[1:], "title", True)
        send(text_input)
    else:
        sendMsg(chatID, "Searching...")
        # Case: computer
        for subject in subject_code_list:
            website = get_source(f"https://prog-crs.ust.hk/ugcourse/{academic_year}/{subject}")
            for course in website.find_all("li", class_="crse"):
                course_search(course, text, "title", False)
                for description in course.find_all("div", class_="data"):
                    if text.upper() in str(description).upper():
                        code = str(description.find_parents("li")).split('<div class="crse-code">')[1].split('</div>')[0]
                        course_search(course, code.split()[1], "code", False)
        send(text_input)

main_handler = MessageHandler(Filters.text, main)
dispatcher.add_handler(main_handler)

updater.start_polling()
