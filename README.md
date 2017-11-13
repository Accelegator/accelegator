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
pip3 install --upgrade pip
pip3 install -r requirements.txt --user
```

## Initial Setup

To begin, we need to make sure that the OAuth client for python has been isntalled. Inside the repository folder open up a terminal (or for windows users cmd). In the terminal use the command:

`python3 -m pip install --user gspread oauth2client`

### Creating a Google Form
In your Google account online, go to Google Drive and create a new Google Sheets spreadsheet and a Google form. In the Form, create a questionaire to with the information you wish to obtain from students. After you have at least one submission of the form go to the responses tab:

<img src="https://i.imgur.com/ctAYBmq.png" alt="Response Tab" height="207" width="481">

Now, click on the green icon with the white cross through "![Link to Sheet Image](https://i.imgur.com/mFFCicS.png "Click this to link")" it to link the form to the Google Sheet.  
If you need to change the destination, you can click on the three dot icon menu "![Change Destination Image](https://i.imgur.com/T9AaNPQ.png "Click this to change destination")" to the right of the green icon and select "Select response destination"

### Creating a Service Account
For our program to use your new spreadsheet, you’ll need to create a service account and OAuth2 credentials from the Google API Console.  To begin:

1. Go to the [Google APIs Console.](https://console.developers.google.com/apis/dashboard)
2. Create a new project.
3. Click Enable API. Search for and enable the Google Drive API.
4. Create credentials for a Web Server to access Application Data.
5. Under "Are you using Google App Engine or Google Compute Engine?" select No, I am not using them.
5. Name the service account and grant it a Project Role of Editor.
6. Download the `.json` file.
7. Copy the `.json` file to your code directory and rename it to `AGAuthKey.json`

<img src="https://www.twilio.com/blog/wp-content/uploads/2017/02/google-developer-console.gif" alt="Credit to twilio.com for this GIF" height="375" width="600">

And finally, there is one last step to link the `.json` file with the spreadsheet.

1. Open up the newly created `AGAuthKey.json`
2. Next to the row labeled **"Client_email"** copy the email without the quotation marks
3. Open the spreadsheet created with our Google Form earlier
4. Go to **Share** and paste the email into the people field and hit **Send**


------

## Usage

Accelegator analysis advisee questionnaires and uses natural language
processing to compile and sort the information for
advisors.

Along with the NLP, Accelegator uses Latent Dirichlet Allocation (LDA) to
analyze data by specific question, every question, specific person, every
person or all the data with textual results.

How to run:
`` gensim <target> <field> ``

Where target = `person` or `question`
and field = `<email>@allegheny.edu` or `question number` or leave this blank for
analysis for every entry in the target.

In order to run, at minimum, ``<target>`` needs to be declared. This is also
case sensitive.

### Legalities and Privacy

See LegalitiesPrivacy_Accelegator.md file for information.

### Search Queries and Field

Accelegator in an interactive information program. Once the general
information has been compiled, users may search for more specified information
on advisees including groups of similar advisees, skills, and more.

### Commands

Accelegator has command options for a better user experience such as help and
quit.

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

### Test Coverage

Test coverage is being addressed by Coveralls so that when Travis-CI runs, it
can evaluate the overall coverage of the test suite.

### Activating Travis-CI

Travis can only be implemented by admin accounts. Admin users can activate
Travis by creating a .travis.yml file in the project's root directory.

## Questions or Comments

Any problems regarding Accelegator can be written in the issues link at the
top of the site.
