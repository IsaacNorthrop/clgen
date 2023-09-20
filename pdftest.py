# Isaac Northrop, isaac.northrop88@gmail.com, gsnap88, github.com/gsnap88

from fpdf import FPDF
from datetime import date
import re
import os

# --- Sample Letter ---
# Defines general letter to be used as well as locations to substitute the
# the current date, the company name, the company location and the job title.

letter = """
-DATE-
-COMPANY-
-LOCATION-

To Whom it May Concern,

        My name is Isaac Northrop. I am a Software Engineering student at the University of Victoria, 
and I am applying for the -JOB- co-op. I am looking for a 4 or 8-month co-op term with 
-COMPANY-. I am applying for this position to continue developing my skills in 
the software industry. The skills I have refined working as a Full Stack Developer for Voith Paper 
in Germany and as a Wildland Firefighter make me a great candidate for this position. 
        During my time at Voith, I developed software development and project management skills. I 
learned how to work with React.js, Django and PostgreSQL to design and build an application to run 
with a paper roll measurement device. I then utilized Docker to deploy this application to a 
testing environment. Over the course of this project, I collaborated with engineers in different 
fields within my team to design the application according to the device specification. I also 
presented our project to various managers to obtain additional resources to further the prototype. 
In addition, I managed a GitLab repository with the project, and established documentation standards
and software prototypes that will be used by future team members and interns alike. Moreover, I 
actively managed this project through Teams and Slack, and communicated daily progress reports to 
my supervisor, adhering to internal deadlines. 
        While working with the BC Wildfire Service, I developed a strong work ethic and the ability to 
work in a team. I worked with many teams of varying sizes to extinguish forest fires around the 
province. I established a strong work ethic and attention to detail while working long hours in 
difficult conditions. I also developed strong oral and written communication skills by taking orders 
from supervisors and communicating hazards to other workers to ensure overall safety. I learned to 
adapt to a rapidly changing work environment, as well as quickly learning new skills to complete 
tasks more quickly and efficiently.
        Over the course of my degree, I have developed basic skills in C, Python, Java. I am also 
developing skills in C++ and FreeRTOS on STM Microcontrollers through my involvement with 
the UVIC Formula Team.
        Thank you for your consideration. I would be happy to discuss my skills in a more formal 
setting.  I can be contacted at 250-617-0549, or by email at isaac.northrop88@gmail.com.

Sincerely,

Isaac Northrop
"""

# --- Substitute Values ---
# Acquire values for date through datetime libray, and company, location and
# job through user input. If any input is over 20 characters, the program
# produces an error.

today = date.today()
trig = 1
while(trig):
    job = input('Enter Job Title: ')
    if(len(job) <= 20):
        trig = 0
    else:
        print("Error: Input must be under 20 characters. Try again.")
trig = 1
while(trig):
    company = input('Enter Company Name: ')
    if(len(company) <= 20):
        trig = 0
    else:
        print("Error: Input must be under 20 characters. Try again.")
trig = 1
while(trig):
    location = input('Enter Location: ')
    if(len(location) <= 20):
        trig = 0
    else:
        print("Error: Input must be under 20 characters. Try again.")

# --- Substitute ---
# Use regex to substitute the correct values into the letter.

letter = re.sub('-DATE-', today.strftime('%B %d, %Y'), letter)
letter = re.sub('-COMPANY-', company, letter)
letter = re.sub('-LOCATION-', location, letter)
letter = re.sub('-JOB-', job, letter)

# --- PDF Header ---
# Using the FPDF libary, create a pdf and a page, define a header with the
# proper font.

pdf = FPDF()
pdf.add_page()
pdf.set_font('Times', 'B', 26)
pdf.set_margins(18, 18, 18)
pdf.set_x(80)
pdf.cell(40, 12, 'Isaac Northop', 0, 2, 'C')
pdf.set_font('Times', '', 11)
pdf.cell(40, 6, '1735 Garnet Road - Victoria, BC - 250-617-0549 - isaac.northrop88@gmail.com', 0, 2, 'C')

# --- PDF Body ---
# Set the body font, then go through the letter letter by letter and append
# them to a string. If the letter happens to be a newline, create a new cell
# and reset the string. Put signature at bottom of page.

pdf.set_font('Times', '', 12)
line = ''
for i in letter:
    if i == '\n':
        pdf.cell(40, 6, line, 0, 1, 'L')
        line = ''
    line = line + i
pdf.image('sig.png', None, 248, 33.6, 21)

# --- File Definition ---
# Define a general filename, then sub in the job name and company. Make a pdf
# file with the generated name and open it.

filename = '-JOB- - -COMPANY- - Isaac Northrop.pdf'
filename = re.sub('-JOB-', job, filename)
filename = re.sub('-COMPANY-', company, filename)
pdf.output(filename, 'F')
os.startfile(filename)
