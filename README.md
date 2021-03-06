# Accelegator

Accelegator is an adaptive advising tool written to help advisors help their
students. The program takes information on individual and multiple advisees,
analyzing, compiling, and displaying it for the advisor in a helpful manner.
The user need only send out questionnaires to the advisees and, once submitted,
Accelegator will read in and use the information for the user.

## Installation

Accelegator is a python 3 program and, therefore uses [pip][1] for installation.
Type the following commands before running:

[1]: https://pip.pypa.io/en/stable/installing

```shell
pip3 install --user --upgrade pip
pip3 install --user -r requirements.txt
```

## Initial Setup

To begin, we need to make sure that the OAuth client for python has been isntalled.
Inside the repository folder open up a terminal (or for windows users cmd). In the
terminal use the command:

`python3 -m pip install --user gspread oauth2client`

### Creating a Google Form

In your Google account online, go to Google Drive and create a new Google Sheets
spreadsheet and a Google form. In the Form, create a questionaire to with the
information you wish to obtain from students. After you have at least one submission
of the form go to the responses tab:

![Response Tab](https://i.imgur.com/ctAYBmq.png)

Now, click on the green icon with the white cross through it
"![Sheet](https://i.imgur.com/mFFCicS.png "Click this to link")"
to link the form to the Google Sheet. If you need to change the destination, you
can click on the three dot icon menu
"![Destination](https://i.imgur.com/T9AaNPQ.png "Click this to change destination")"
to the and select "Select response destination"

### Creating a Service Account

For our program to use your new spreadsheet, you’ll need to create a service account
and OAuth2 credentials from the Google API Console. To begin:

1. Go to the [Google APIs Console.](https://console.developers.google.com/apis/dashboard)
1. Create a new project.
1. Click Enable API. Search for and enable the Google Drive API.
1. Create credentials for a Web Server to access Application Data.
1. Under "Are you using Google App Engine or Google Compute Engine?",
  select "No, I am not using them."
1. Name the service account and grant it a Project Role of Editor.
1. Download the `.json` file.
1. Copy the `.json` file to your code directory and rename it to `AGAuthKey.json`

![Credit to twilio.com for the GIF](https://www.twilio.com/blog/wp-content/uploads/2017/02/google-developer-console.gif)

And finally, there is one last step to link the `.json` file with the spreadsheet.

1. Open up the newly created `AGAuthKey.json`
1. Next to the row labeled **"Client_email"**,
  copy the email without the quotation marks
1. Open the spreadsheet created with our Google Form earlier
1. Go to **Share** and paste the email into the people field and hit **Send**

Create a Google Sheets spreadsheet and a Google Form in Google Drive.  After you
have at least one submission of the Form, you can go to the responses tab and
click on the green icon with the white cross through it.  This will enable you
to link the Sheet to the Form.  You can either create a new Sheet or link to a
preexisting one.  If you need to change the destination, you can click on the
three dot icon menu to the right of the green icon and select "Select response
destination".

Open the `.json` file in the `accelegator` repository and find the `"client-email"`.
Copy the quoted text that looks like an email address.  Return to the Sheet and
open the sharing options.  Paste the address and click send.

In order to run Accelegator, the `.json` file for the program, AGAuthKey.json,
must be in the root directory of the Accelegator product. The file can be found
in the Google Drive folder for Accelegator and must be downloaded by the user.
The reason for the `.json` file is that this program analyzes confidential
information and so by having this file, only those with permission can actually
run the program and gain access to the information.

Within `defaults.py`, update the `DEFAULT_WORKBOOK` constant to the name of your
Sheet.

## Usage

To initially run Accelegator enter

```
python3 accelegator.py
```

at the root directory.  After starting the program, the user will be prompted
to "Enter number of first textual question to be analyzed". For the original
form being used, the number is 10 and the user must input `10`.
The reason for this is that the gensim analysis must begin at the first
textual question and runs through the last question. By adding this option, if
the form is ever edited so that the first textual question is in a different
position, the user can specify where the analysis should begin instead of
having to edit the source code.

Following that, the user may enter any viable command to execute a specific
feature of the product. It is recommended to run `help` at first in order
to see the possible commands.

While the commands possible for Accelegator are listed under `help`, a brief
overview is provided to better explain them.

If you wish to understand what each command means, use:
`help` and then type the name of the command.

The commands are as follows:
`list`
`show`
`search`
`write`
`gensim`

An example is `help list`.
This will show the description of the command and the arguments of the
command (if available).

Another example is `help show`.  This command will tell you the how the
`<email>` must be written to interact with the program.  It also lists each of
the `<field>`s that you can search by.

Command:
`list`

This command succintly lists the email addresses of the professor's advisees.

Command:
`show`

This command is accompanied by
`email` , entered as `show <email>`

which then brings up the student submission form in its entirety.  It can also
be used as `show <email> <field>` where `field`is a word command that is one
of the `field`s shown in `help show`.  In that case, it would bring up a
specific answer from the student's submission form.

Command:
`search`

This command, when accompanied with a `keyword` allows the professor to search
for specific terms that their students have used.  For example, many of the
textual questions refer to academic, personal, and career interests.  If the
professor learned of a great internship opportunity for students who are
interested in cyber security and wanted to reach out to his advisees to make
them aware of it, they could focus their outreach by using the `search`
command. Specifically, the professor could enter `search security` where
search is the command and security is the keyword.

Command:
`write`

This command could be used in a myriad of scenarios.  One example of how to
use it is if the professor was preparing for an adviser meeting with one
particular student.  To pull up the most recent form that said student
submitted for review, the professor could enter the command
`write show <studentEmail>`.
This would then prompt the professor to name the file where they wanted the
information to be stored.  Once saved, the advisor could use this file of
information as a guide to the conversation that would ensue. `write` could
also be used to print out the list of advisees or to print out a list of
advisees interested in a certain topic.  This command is useful if the
professor wishes to store information from the program in a different file.

Accelegator also analyzes advisee questionnaires and uses natural language
processing to compile and sort the information for advisors.

Along with the NLP, Accelegator uses Latent Dirichlet Allocation (LDA) to
analyze data by specific question, every question, specific person, every
person or all the data with textual results.

Run LDA with the command:
`gensim <target> <field>`

Where target = `person` or `question`
and field = `<email>@allegheny.edu` or `question number`.You could also leave
this blank for analysis for every entry in the target.

In order to run, at minimum, ``<target>`` needs to be declared. This is also
case sensitive.

The visual of the LDA analysis represents all of the words that are related to
each other. If they reach a certain level of relevance to each other they will
appear in a group together. If the user hovers over the circle that is a
topic, they will see every word that is in the relevant topic and the
frequency of each word. The LDA also produces a textual output, it shows the
actual values of how related the words are to the topic. The higher the number
is the more related the words are.

See AccelegatorLDavis_Analysis.md for more information about how to interpret
this visualization.

### Legalities and Privacy

See Accelegator_Legalities.md file for information.

### Search Queries and Field

Accelegator in an interactive information program. Once the general
information has been compiled, users may search for more specified information
on advisees including groups of similar advisees, skills, and more.

### Commands

Accelegator has command options for a better user experience such as help and
quit. Help displays all the possible commands for the program and when another
command is added following help (ie >>>help show) the program will explain to
the user how to use that command and the arguments that it may require in order
to be run.

## Testing

Functions have been tested throughout this system to allow conformation that
the system is working correctly.

### Running the Test Suite

To run the test suite, run the following commands in Accelegator's root
directory:

```shell
pytest tests
```

### Automatic Linting

The linting automatically checks to ensure Accelegator's code is up to pep8
standards. If linting errors occur run the following command to perform
automatic linting:

```shell
autopep8 --in-place --aggressive --aggressive *.py
```

If the autolinting tool cannot fix every error, it will display where each
error is in the program and what the error type is in order for the user to
address it properly.

### Test Coverage

Test coverage is being addressed by Coveralls so that when Travis-CI runs, it
can evaluate the overall coverage of the test suite.

### Activating Travis-CI

Travis can only be implemented by admin accounts. Admin users can activate
Travis by creating a .travis.yml file in the project's root directory.

## Questions or Comments

Any problems regarding Accelegator can be written in the issues link at the
top of the site.

[![Coverage Status](https://coveralls.io/repos/github/Accelegator/accelegator/badge.svg?branch=master)](https://coveralls.io/github/Accelegator/accelegator?branch=master)