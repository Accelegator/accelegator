# Accelegator

Accelegator is a professor advisor tool written to help advisors help their
students. The program takes information on individual advisees, analyses it and
compiles it, and then displays it for the advisor in a helpful manner.
Accelegator can also take the information on multiple students, analyses,
compile and compare, and then display. The user need only send out qustionnaires
to the advisees and, once submitted, Accelegator will read in and check the
information for the user.

## Installation

Accelegator is a python 3 program and, therefore uses [pip](https://pip.pypa.io/en/stable/installing/) for installation. Type the
following commands before running:

```shell
pip install --upgrade pip
pip install -r requirements.txt
```

## Initial Setup

Install gspread as well as oauth2client in your root directory in the repository
using the command:

```shell
python3 -m pip install --user gspread oauth2client
```

---

## Usage

Accelegator analysis advisee questionnaires and uses natural language processing
to compile and sort the information for advisors.

### Legalities and Privacy

See LegalitiesPrivacy_Accelegator.md file for information.

### Search Queries and Field

Accelegator in an interactive information program. Once the general information
has been compiled, users may search for more specified information on advisees
including groups of similar advisees, skills, and more.

### (what other features do they have???)

---

## Testing

### Functions Tested

The test suite verifies Accelegator's functions. The first function that is
tested is ___________

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

---

## Questions or Comments
Any problems regarding Accelegator can be written in the issues link at the top
of the site.
