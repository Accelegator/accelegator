# Accelegator

Accelegator is a professor advisor tool written to hekp advisors help their students. The prograg takes information on inidvidual adviees , analyses it andd compiles it, and then displayes it for the advisor in a helpful manner. Accelegator can also take the information on multiple students, analyse, compile and compaire, and then display. The user need only send out qustionaires to the advisees and, once submitted, Accelegator will read in and check the information for the user.

## Installation

Accelegator is a python 3 program and, therefore uses [pip](https://pip.pypa.io/en/stable/installing/) for installation. Type the following commands before running:

```shell
pip install --upgrade pip
pip install -r requirements.txt
```

## Initial Setup

Install gspread as well as oauth2client in yur root directory in the repository using the command:

```shell
python3 -m pip install --user gspread oauth2client
```

---

## Usage

Accelegator analysis advisee questionaires and uses natraul language progessint to compile and sort the information fot advisors.

### Legalities and Privacy

See LegalitiesPrivacy_Accelegator.md file for information.

### Search Quries and Feild

Accelegator in an interactive inpormation program. Once the general information has been compiled, users may search for more specified information on advisees including groups of sililar advisees, skills, and more.

### (what other features do they have???)

---

## Testing

### Functions Tested

The test suite verifies Accelegator's functions. The first function that is tested is ___________

### Running the Test Suite

To run the test suite, run the following commands in Aggelegators root directory:

```shell
pytest tests
```

### Automatic Linting

The linting automatically checks to ensure Accelegator's code is up to pep8 standards. If linting errors occur run the following command to prform automatic linting:

```shell
autopep8 --in-place --aggressive --aggressive *.py
```

### Test Coverage

Test coverage is being adressed by Coveralls so that when Travis-CI runs, it can evaluste the overall coverage of the test suite.

### Activating Travis-CI

---

## Questions or Comments
