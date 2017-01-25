#   Template for 15-110 Homework #9
#
#   Problems #2 and #3: 2-3.courseSchedule.py
#
#
#   WRITTEN BY (NAME & ANDREW ID):Moosuk    moosukk and Abhik Bhaval
#
#   15-110 section:N

import urllib2

def substringBetween(string, leftDelimiter, rightDelimiter):
  index1 = string.find(leftDelimiter) + len(leftDelimiter)
  index2 = string.find(rightDelimiter)
  substring = string[index1:index2]
  return substring

# Reads the content of a web page at a specified URL
# Parameters:
#   url: a string with the URL of the page to be fetched
# Returns: a list containing the lines of the fetched web page
def grabWebPage(url):
    urlHandler = urllib2.urlopen(url)
    lines = urlHandler.readlines()
    urlHandler.close()
    return lines

# Checks if a given string can be safely converted into a positive float.
# Parameters:
#   s: the string to be checked
# Returns: True if the string represents a positive float, False otherwise
def isValidNumberString(s):
  if len(s) == 0:
    return False
  for c in s:
    if c not in "0123456789.":
      return False
  return True


# Prints all the courses (number, title, and credit units) offered
# in a department at CMU
# Parameters:
#   htmlSchedule: list of strings with the html code of the online schedule
#   department: string with the two-digit code of a CMU department
#               (e.g., "15" is Computer Science)
# Returns: nothing
def printCoursesInDepartment(htmlSchedule, department):
    print "----------------------------------------"
    print "Courses in department:", department
    for line in htmlSchedule:
      if isValidNumberString(substringBetween(line, "<TD NOWRAP>", "</TD>")) == True:
        print substringBetween(line, "<TD NOWRAP>", "</TD>"), substringBetween(line, "</TD><TD>", "</TD><TD NOWRAP>")
      
      
        
        
        
    
    #
    # Print all the courses here
    #
    print "----------------------------------------"


# Prints a selection of CMU courses (number, title, and credit units)
# from the given list of departments, totaling at least 40 credit units.
# Parameters:
#   htmlSchedule: list of strings with the html code of the online schedule
#   departments: list of strings with two-digit department codes
# Returns: nothing
def printCourseSelection(htmlSchedule, departments):
    minUnits = 40
    totalUnits = 0
    print "----------------------------------------"
    print "Selection of courses from these departments:", departments
    #
    # Print your selection of courses here
    #
    print "Total credit units: " + str(totalUnits)
    print "----------------------------------------"


# BONUS
def printMinCourseSelection(htmlSchedule, departments):
    return


# CMU schedule on the web
url = "https://enr-apps.as.cmu.edu/assets/SOC/sched_layout_spring.htm"
page = grabWebPage(url)

# Make sure you test your function with other departments too
printCoursesInDepartment(page, "15")
# Example output:
"""
----------------------------------------
Courses in department: 15
15075 Computer Science Co-Op 0-36
15090 Computer Science Practicum 3.0
15101 Exploring Programming with Alice 10.0
15102 Exploring Programming with Graphics 10.0
15110 Principles of Computing 10.0
15121 Introduction to Data Structures 10.0
15122 Principles of Imperative Computation 10.0
15123 Effective Programming in C and UNIX 9.0
15150 Principles of Functional Programming 10.0
15199 Special Topics: Discovering Logic 3.0
15211 Fundamental Data Structures and Algorithms 12.0
15212 Principles of Programming 12.0
15213 Introduction to Computer Systems 12.0
15221 Technical Communication for Computer Scientists 9.0
15251 Great Theoretical Ideas in Computer Science 12.0
15295 Special Topic: Competition Programming and Problem Solving 3-6
15296 Special Topic: Understanding and Broadening the Images of Computing 6.0
15302 Special Topic: iSTEP: Technology Field Research in Developing Communities 3,6
15312 Foundations of Programming Languages 12.0
15319 Introduction to Cloud Computing 6.0
15322 Introduction to Computer Music 9.0
15385 Computer Vision 9.0
15386 Neural Computation 9.0
15392 Special Topic: Secure Programming 9-12
15397 Special Topic: Project Course in Pen-Based Computing 9.0
15410 Operating System Design and Implementation 12.0
15413 Software Engineering Practicum 12.0
15418 Parallel Computer Architecture and Programming 12.0
15437 Web Application Development 12.0
15440 Distributed Systems 12.0
15441 Computer Networks 12.0
15451 Algorithm Design and Analysis 12.0
15453 Formal Languages, Automata, and Computability 9.0
15462 Computer Graphics 12.0
15464 Technical Animation 12.0
15468 Special Topic: Advanced Parallel Graphics 9.0
15494 Special Topic: Cognitive Robotics 12.0
15498 Special Topic: Information Forensics 12.0
15502 Technology and Global Development 9.0
15519 Independent Study in Programming Systems 3-18
15529 Independent Study in Human-Computer Interaction 3-18
15539 Independent Study in Computer Science Pedagogy 3-18
15549 Independent Study in Computer Systems 3-18
15559 Independent Study in Theoretical Computer Science 3-18
15569 Independent Study in Graphics 3-18
15579 Independent Study in Robotics 3-18
15589 Independent Study in Artificial Intelligence 3-18
15599 Undergraduate Thesis Research 3-18
15610 Engineering Complex, Large-Scale Computer Systems 12.0
15637 Web Application Development 12.0
15645 Special Topic: New Robotics Ventures 12.0
15668 Special Topic: Advanced Parallel Graphics 12.0
15685 Computer Vision 12.0
15686 Neural Computation 12.0
15697 Graduate Reading and Research 1-48
15712 Advanced Operating Systems and Distributed Systems 12.0
15745 Optimizing Compilers for Modern Architectures 12.0
15746 Advanced Storage Systems 12.0
15750 Graduate Algorithms 12.0
15754 Machine-based Complexity Theory: 12.0
15780 Graduate Artificial Intelligence 12.0
15781 Machine Learning 12.0
15812 Programming Language Semantics 12.0
15817 Introduction to Model Checking 6.0
15818 Special Topics in Software Systems: 6.0
15819 Advanced Topics in Programming Languages:: 12.0
15845 Current Research Issues in Computer Systems 2.0
15849 Advanced Topics in Computer Systems: 12.0
15855 An Intensive Introduction to Computational Complexity Theory 12.0
15859 Special Topics in Theory: 12.0
15891 V-Unit in Computer Science 1-36
15894 Technically Speaking 12.0
15990 Computer Science Colloquium 0.0
15997 Graduate Reading and Research 1-60
15998 Practicum in Computer Science 1-36
----------------------------------------
"""

# Make sure you test your function with other departments too
printCourseSelection(page, ["15","31", "03"])
# Example output (your selection of courses may be different):
"""
----------------------------------------
Selection of courses from these departments: ['15', '31', '03']
15090 Computer Science Practicum 3.0
31105 Air Force Leadership Laboratory 0.0
03101 Biological Sciences First Year Seminars 3.0
15101 Exploring Programming with Alice 10.0
31106 Air Force Leadership Laboratory 0.0
03116 Phage Genomics Research 6.0
15102 Exploring Programming with Graphics 10.0
31107 Air Force Leadership Laboratory 0.0
03121 Modern Biology 9.0
Total credit units: 41.0
----------------------------------------
"""

