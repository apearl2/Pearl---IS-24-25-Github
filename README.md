Project Timeline:


9/30 - Create user interface for Intended major, and safety attributes, basic UI

10/1 - Add tuition cutoff, generate report in console for selected attributes, started to work on storing importance values as variables

10/2 - More work on importance

10/3 - Download PyCharm

10/5-10/6 - Importance radio value works, begin learning about web scraping using Beautiful soup

10/13- Ability to search google and get any desired URL (CODE REUSABILITY), beginning to parse HTML data from Princeton Review (Niche doesn’t work yet) using python string methods

10/14 - Finish string methods for rankings, final list generated for any Princeton Review ranking (with about 4 errors per 25)

10/19 -> Created function to create finalList to assign names and points (works for 2 lists so far) and cleaned up main function as well as ----Errors in list

10/20 -> Revised rankingA() function to ensure all colleges (tested with 4 PrincetonReview functions) are show in finalList once with their proper values
#And started making code to return ordered list of College Factual Rankings (turns out to be way easier than Princeton Review)
            
10/21 -> Built CollegeFactual() function up to generating a newrankList

10/24 -> rankingA() now works with CollegeFactual Function,             Started working with Flask

10/26 -> Started more learning about flask, reportA() function works for first~20 colleges

10/27 -> averageA() functions works all the time now, began working on way to join the two lists from C and P together

10/30 -> converted college variables from CF and P functions to uniform strings

10/31 -> Video of current functionality

11/2 -> (Marked as ### in program) Used functionality of listA() function combined with google to compile complete lists of all colleges that might come up, and then now able to convert them without using google
        #Program now runs (with all 14 attributes) in about 45 seconds

11-3 -> Add project to GitHub, first Flask project with user input

11/4 -> Began building first HTML templates and putting rest of python into Flask program
	Downloaded python 3.13.0     (previously using python 3.8)
Whole program works with first 3 college factual attributes

11/5 -> Put rest of attributes (P) into front end
#TODO figure out way to ensure calculate() function gets all attribute selections before running content of function
	Might have to break up HTML pages to run CF, and then P attributes
            Could be recording everything past main url as string, then using string methods
	Research more on Request library from Flask https://flask.palletsprojects.com/en/stable/api/#flask.Request

11/6 -> Revised method for taking input broken into 3 page stages: home, in_progress, and results. New structure now works for all 3 college factual attributes

11/7 -> Created called variable to ensure string is only split when CF/P functions are actually
	New structure works through joinA() for all 14 attributes.

