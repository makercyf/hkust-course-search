# hkust-course-search
Searching the latest information of HKUST courses

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
1. PHYS
2. math1012
3. COMP 1022P
4. phys electromagnetic waves
5. ISOM -a critical government sustainable competitiveness optimizing
6. 2121
7. python
8. -A management derivatives bond finance instruments equity

### Sample output
1. Search the course with subject (e.g. COMP, MATH, PHYS)
```
user@ubuntu:~$ python3 ust.py
Search: PHYS
Searching...

Course code: PHYS 1001
Course title: Physics and the Modern Society
Credit: 3 Credit(s)
Exclusion(s): Level 3 or above in HKDSE 1/2x Physics or HKDSE 1x Physics; any PHYS courses at 1100-level or above
Description: This course is for students with no physics background. Course content: Principle of scientific theories and methods, Aristotle's law, Newtonian mechanics. Thermal physics, heat engine, energy crisis and global warming. Nature of waves and the physics of hearing and vision. Electricity and magnetism, electromagnetic waves and telecommunication. Relativity, quantum physics, nuclear energy and semiconductor. Developments and outlook of contemporary physics.

<snipped>

Course code: PHYS 4813
Course title: Contemporary Applications of Physics: Atmospheric Physics - Making Sense of Weather and Climate
Credit: 1 Credit(s)
Prerequisite(s): PHYS 3032
Corequisite(s): PHYS 4050
Description: Atmospheric physics is a fascinating application of physics that has been part of our daily life since the last century. An accurate daily weather forecast in the modern era relies not only on our intellectual understanding of the atmosphere, but also on the real-time monitoring and numerical modelling of atmospheric motions. Both of them are fruitful applications of atmospheric physics. In recent decades, there has been growing concern over human impacts on global climate. The wide-ranging claims of human-induced climate change have to be supported by scientific theories and evidence. Atmosphere physics plays a central role in such debates as the atmosphere is a core component of the climate system. This course offers both conceptual and quantitative discussions of the fundamental physical processes that shape our weather and climate.

user@ubuntu:~$
```

2. Search the course with subject and course code
```
user@ubuntu:~$ python3 ust.py
Search: math1012
Searching...

Course code: MATH 1012
Course title: Calculus IA
Credit: 4 Credit(s)
Co-list with: MATH 1013
Exclusion(s): Level 3 or above in HKDSE Mathematics Extended Module M1 or M2; AL Pure Mathematics; AL Applied Mathematics; MATH 1003, MATH 1013, MATH 1014, MATH 1020, MATH 1023, MATH 1024
Description: This is an introductory course in one-variable calculus, the first in the Calculus I and II sequence, designed for students that have not taken HKDSE Mathematics Extended Module M1 or M2. Topics include functions and their limits, continuity, derivatives and rules of differentiation, applications of derivatives, and basic integral calculus.

user@ubuntu:~$ python3 ust.py
Search: COMP 1022P
Searching...

Course code: COMP 1022P
Course title: Introduction to Computing with Java
Credit: 3 Credit(s)
Exclusion(s): COMP 1021, COMP 1022Q (prior to 2020-21),  COMP 2011, COMP 2012H, ISOM 3320
Mode of Delivery: None
Description: This course is designed to equip students with the fundamental concepts of programming elements and data abstraction using Java. Students will learn how to write procedural programs using variables, arrays, control statements, loops, recursion, data abstraction and objects using an integrated development environment.

user@ubuntu:~$
```

3. Search the course with subject and keyword
```
user@ubuntu:~$ python3 ust.py
Search: phys electromagnetic waves
Searching...

Course code: PHYS 1001
Course title: Physics and the Modern Society
Credit: 3 Credit(s)
Exclusion(s): Level 3 or above in HKDSE 1/2x Physics or HKDSE 1x Physics; any PHYS courses at 1100-level or above
Description: This course is for students with no physics background. Course content: Principle of scientific theories and methods, Aristotle's law, Newtonian mechanics. Thermal physics, heat engine, energy crisis and global warming. Nature of waves and the physics of hearing and vision. Electricity and magnetism, electromagnetic waves and telecommunication. Relativity, quantum physics, nuclear energy and semiconductor. Developments and outlook of contemporary physics.

Course code: PHYS 1114
Course title: General Physics II
Credit: 3 Credit(s)
Prerequisite(s): (PHYS 1111 OR PHYS 1112 OR PHYS 1312) AND (level 3 or above in HKDSE Mathematics Extended Module M1/M2 OR MATH 1012 OR MATH 1013 OR MATH 1020 OR MATH 1023)
Exclusion(s): PHYS 1314
Description: This course targets students who have learned the most basic knowledge in physics in high school. Students with more advanced physics background should consider taking PHYS 1314. This course employs a calculusâs law, electric field and potential, Gaussâ law, capacitance, circuits, magnetic force and field, Ampereâs law, electromagnetic induction, AC circuit, Maxwellâs equations, electromagnetic waves, geometric optics, interference and diffraction. Students without the prerequisite may seek instructorâs approval for enrolling in the course. For students under the 4-year degree only.

user@ubuntu:~$
```

4. Search the course with subject and relevant keywords in course title or/and course description
```
user@ubuntu:~$ python3 ust.py
Search: ISOM -a critical government sustainable competitiveness optimizing
Searching...

Course code: ISOM 1700
Course title: Critical Issues in Business Operations
Credit: 3 Credit(s)
Description: The course will focus on how business organizations should create and sustain value for different stakeholders in the society by designing, optimizing, and improving the operations. Successful businesses have demonstrated their sustainable competitiveness by maintaining a balanced view of economic prosperity, environmental stewardship, and social responsibility. This course will also examine how the changing perspectives of stakeholders (like government and consumers) affect the business decisions and operations.

user@ubuntu:~$
```

5. Search the course with course code
```
user@ubuntu:~$ python3 ust.py
Search: 2121
Searching...

Course code: MATH 2121
Course title: Linear Algebra
Credit: 4 Credit(s)
Prerequisite(s): A passing grade in AL Pure Mathematics / AL Applied Mathematics; OR MATH 1014 OR MATH 1020 OR MATH 1024
Exclusion(s): MATH 2111, MATH 2131, MATH 2350
Description: Vector space, matrices and system of linear equations, linear mappings and matrix forms, inner product, orthogonality, eigenvalues and eigenvectors, symmetric matrix.

user@ubuntu:~$
```

6. Search the course with keyword
```
user@ubuntu:~$ python3 ust.py
Search: python
Searching...

Course code: ACCT 4720
Course title: Equity Investment with Machine Learning
Credit: 3 Credit(s)
Prerequisite(s): ACCT 2010 AND ISOM 3400
Description: This course is designed for students interesting in the investment management business, especially for those who aspire to learn the application of quantitative and machine learning technology in equity investing. The course will cover a wide range of topics in equity investing, including quantitative investment process, multi-factor stock-selection models, portfolio construction methods, performance evaluation, and an introduction of applications of AI/machine learning technology in equity investing. This is a very hands-on course. Students will be required to conduct quantitative and machine learning analyses using Python. Prior knowledge in capital markets and python programing is required. For students in their third year of study and above.

<snipped>

Course code: SISP 1108
Course title: A First Step to Data Science with Python
Credit: 1 Credit(s)
Description: This course is offered under the program of the HKUST Summer Institute for Secondary School Students by the School of Science. This course provides fundamental concepts and techniques in the field of data science. Students in this course can take the first step in the world of data science by studying basic concepts in probability, statistics and programming. Some daily-life applications of statistics implemented with an open source package Python will also be discussed to expose students to practical issues of real-world data, e.g. in house pricing, in pricing exchange rates, in classification problems, etc.

user@ubuntu:~$
```

7. Search the course with relevant keywords in course title or/and course description
```
user@ubuntu:~$ python3 ust.py
Search: -A management derivatives bond finance instruments equity
Searching...

Course code: FINA 4403
Course title: International Finance
Credit: 3 Credit(s)
Prerequisite(s): FINA 3103
Description: An introduction to the fundamental principles of international financial management and investment.  Topics include: international financial markets and instruments; foreign exchange markets; foreign currency derivatives and currency risk; international capital budgeting; international bond and equity markets.

user@ubuntu:~$
```

## Application
### Host your own Telegram search bot
This telegram bot relies on the library [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) and Telegram Bot API.

You can install the package via PyPI  
```sh
pip3 install python-telegram-bot
```

You may follow the online tutorials to get your own bot Token, and then enter your own token inside the double quote of `ustBot.py` line 8
