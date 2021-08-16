# hkust-course-search
Searching the information of HKUST courses

## Requirements
1. [Requests](https://github.com/psf/requests)
2. [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/)

You can install the packages via PyPI  
```sh
pip3 install requests && pip3 install beautifulsoup4
```

## Usage
### Acceptable input example
The input is not case-sensitive.
1. COMP
2. comp1021
3. COMP 1021
4. comp computer
5. 1021
6. computer

### Sample output
1. Search the course with subject (e.g. COMP, MATH)
```
user@ubuntu:~$ python3 ust.py
Search: COMP
Course code: COMP 1001
Course title: Exploring Multimedia and Internet Computing
Credit: 3 Credit(s)
Exclusion(s): ISOM 2010, any COMP courses of 2000-level or above
Mode of Delivery: [BLD] Blended learning
Description: This course is an introduction to computers and computing tools. It introduces the organization and basic working mechanism of a computer system, including the development of the trend of modern computer system. It covers the fundamentals of computer hardware design and software application development. The course emphasizes the application of the state-of-the-art software tools to solve problems and present solutions via a range of skills related to multimedia and internet computing tools such as internet, e-mail, WWW, webpage design, computer animation, spread sheet charts/figures, presentations with graphics and animations, etc. The course also covers business, accessibility, and relevant security issues in the use of computers and Internet.

<snipped>

Course code: COMP 4981H
Course title: Final Year Thesis
Credit: 6 Credit(s)
Exclusion(s): COMP 4981
Description: Students are expected to conduct research under the supervision of a faculty member, summarize their work in an individual thesis and make a defense at the end. Credit load will be spread over the year. For students in the BEng in Computer Science and BEng in Computer Engineering programs under the four-year degree only. Instructor's approval is required for enrollment in the course.

user@ubuntu:~$
```

2. Search the course with subject and course code
```
user@ubuntu:~$ python3 ust.py
Search: comp1021
Course code: COMP 1021
Course title: Introduction to Computer Science
Credit: 3 Credit(s)
Exclusion(s): COMP 1022P, COMP 1022Q (prior to 2020-21), COMP 2011, COMP 2012H
Description: This course introduces students to the world of Computer Science. Students will experience a range of fun and interesting areas from the world of computing, such as game programming, web programming, user interface design and computer graphics. These will be explored largely by programming in the Python language.

user@ubuntu:~$
```

3. Search the course with subject and keyword
```
user@ubuntu:~$ python3 ust.py
Search: comp computer
Course code: COMP 1021
Course title: Introduction to Computer Science
Credit: 3 Credit(s)
Exclusion(s): COMP 1022P, COMP 1022Q (prior to 2020-21), COMP 2011, COMP 2012H
Description: This course introduces students to the world of Computer Science. Students will experience a range of fun and interesting areas from the world of computing, such as game programming, web programming, user interface design and computer graphics. These will be explored largely by programming in the Python language.

<snipped>

Course code: COMP 4901
Course title: Special Topics in Computer Science
Credit: 0-4 Credit(s)
Description: Selected topics of current interest to the Department not covered by existing courses. Offerings are announced each semester. May be graded by letter, P/F, or DI/PA/F for different offerings.

user@ubuntu:~$
```

4. Search the course with course code
```
Search: 1021
Course code: COMP 1021
Course title: Introduction to Computer Science
Credit: 3 Credit(s)
Exclusion(s): COMP 1022P, COMP 1022Q (prior to 2020-21), COMP 2011, COMP 2012H
Description: This course introduces students to the world of Computer Science. Students will experience a range of fun and interesting areas from the world of computing, such as game programming, web programming, user interface design and computer graphics. These will be explored largely by programming in the Python language.

Course code: HART 1021
Course title: A Contemporary Approach to Painting
Credit: 1 Credit(s)
Description: This introductory painting course covers the concepts, theories, problems and production of Contemporary Painting, as well as selected painting practices of the artists in the 20th and 21st century and the stories behind renowned paintings. Students will learn to use painting skills such as canvas preparation, paint application, color mixing as a medium of expression and communication. They will also use acrylic to create painting from still life and paint on unconventional surface in an experimental way. Critical thinking skills are developed through art work presentations, critique and an exhibition. Those interested in furthering the artistic skills and gaining hands-on experience with this art form may enroll in a separate non-credit co-curricular workshop.

user@ubuntu:~$
```

5. Search the course with keyword
```
user@ubuntu:~$ python3 ust.py
Search: computer
Course code: CIVL 4370
Course title: Computer Methods of Structural Analysis
Credit: 3 Credit(s)
Prerequisite(s): CIVL 3310
Description: Matrix formulation of structural analysis using stiffness method, solution of linear equations, applications to civil engineering structures, modeling of large and complex structural systems.

<snipped>

Course code: SISP 1313
Course title: Introduction to Computer-Aided Design and Manufacturing
Credit: 1 Credit(s)
Description: This short course will teach students some fundamental theories and technologies in computer-aided design and manufacturing. After taking this course, students will have a basic understanding of how today a product such as i-phone6's frame is designed on a computer and how it is machined on a numerical controlled (NC) machine. The teaching will be centered on hands-on labs: after an initial introduction of basic theories, students will learn how to use a commercial CAD software to design a product such as i-phone6's frame, how to write a NC program for machining it, and finally physically operate a 5-axis NC machine tool to execute the NC program to machine it.

user@ubuntu:~$
```
