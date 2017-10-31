# accelegator

## Data to be collected from advisees

### Booleans

These will be asked in Google Forms as "Yes/No" questions.

- Resume
  - Do you have an updated resume?
- Cover letter
  - Have you ever written a cover letter?
- Four year plan
  - Do you have an updated four year plan?

### Numbers

- Dates of advising meetings

We may look into how to interface with Google Calendar to collect meeting
dates.

### Strings

This will be asked through a dropdown menu: Ex. "Fall 2017", "Spring 2018",
...

- Intended graduation year
  - What is your intended graduation year?

The following data will be collected through a text field.

- Student ID
  - What is your student ID?
- Preferred name
  - What is your preferred name?
- GitHub account
  - What is your GitHub account username? Leave blank if you do not have
    one.
- Website
  - What is your professional website URL? Leave blank if you do not have
    one.
- LinkedIn account
  - What is your LinkedIn URL? Leave blank if you do not have one.
- Professional Twitter account
  - What is your professional Twitter account? Leave blank if you do not
    have one or if you do not use Twitter for professional purposes.
- Favorite classes in major
  - What are your favorite classes that you have taken for your major?
    List their numbers.
- Favorite classes not in major
  - What are your favorite classes that you have taken outside of your
    major? List their numbers.
- Career plan
  - What is your career plan or goal?
- Academic interests
  - What are your academic interests? What topics excite you?
- Personal interests
  - What are your personal, non-academic interests? What extracurricular
    activities are you involved in?
- Technical strengths
  - What are your technical strengths? What skills would you list on your
    resume?
- Technical weaknesses
  - What skills would you like to improve?
- Academic status update
  - How is school going?
- Personal status update
  - How is life going?
- Questions for advisor
  - Do you have any questions for your advisor?



## Usage

See the file titled "LegalitiesPrivacy_Accelegator.md" for more details on the
security and privacy information contained within Accelegator's system.

## First Time Use

Ensure that you have installed gspread and oauth2client installed in the root
directory of the repository.  In the terminal use the command:

```shell
python3 -m pip install --user gspread oauth2client
```

Create a Google Sheets spreadsheet and a Google Form in Google Drive.  In the
Form, create questions that you wish to know about your students. These can be
multi choice, short answer and yes/no. After you have at least one submission of
the Form, you can go to the responses tab and click on the green icon with the
white cross through it.  This will enable you to link the Sheet to the Form.  
You can either create a new Sheet or link to a pre-existing one.  If you need to
change the destination, you can click on the three dot icon menu to the right of
the green icon and select "Select response destination".

Open the `AGAuthKey.json` file which may be distributed to you directly and find
the `"client-email:"` section within.
Copy the quoted text that looks like an email address.  Return to the Sheet and
open the sharing options.  Paste the address and click send.  Alternatively, if
you would like to create your own service account for confidentiality and
security, follow the tutorial found at [www.twilio.com](https://www.twilio.com/blog/2017/02/an-easy-way-to-read-and-write-to-a-google-spreadsheet-in-python.html)
to create a personal service account.

Within `defaults.py`, update the `DEFAULT_WORKBOOK` constant to the name of your
Sheet.

---

### Dependencies
```shell
pip install --user pandas pytest flake8 ansicolors
```
