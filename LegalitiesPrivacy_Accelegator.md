# Legalities and Privacy

    The following section will document the legalities involved in using
Accelegator.  Because Accelegator is a program that will import sensitive
information that is protected under FERPA (The Family Educational Rights and
Privacy Act), a detailed discussion of the possible legal and privacy
implications is necessary if Accelegator is implemented at both Allegheny
College and other schools, as our software team intends it to be.
    FERPA is a “Federal law that protects the privacy of student education
records. The law applies to all schools that receive funds under an applicable
program of the U.S. Department of Education.”[1]  This program’s intended use is
to best serve faculty members who, under FERPA distinction, “Have legitimate
educational interest,” or who need to access the student’s records for, “Audit
or evaluation purposes.”[2]  While FERPA is most relevant to the release of
student information to that student’s parents or guardians, it is also necessary
to explore as a legal issue since the Accelegator program files student’s
records and reflections and stores them within what could be considered a
penetrable program.  Our area of concern lies within the accessibility of
Accelegator: who receives access to student records, how is access granted, and
how are students’ rights maintained under FERPA?
    Allegheny College strongly upholds the laws outlined in FERPA.  It complies
with all established standards and specifically states that, “No one outside the
College community shall have access to, nor will the College disclose, any
information from a student’s educational records without the written consent of
the student, except to persons who are permitted access under the Act.”[3]
Allegheny College defines educational records as, “Records directly related to a
student, which are maintained by Allegheny College, such as admissions
materials, transcripts/grades, student conduct records, financial
records/billing statements, emails, and financial aid information.”[4]  In
regard to faculty members at Allegheny College, the College’s Privacy Policy
states that, “A College official has a legitimate educational interest if the
information requested is necessary for that official in performing a task that
is specified in his/her position description or contract agreement or is
performing a task related to the student’s education.”[5]  In developing
Accelegator, the software team closely abided by the guidelines set forth both
by Allegheny College and FERPA to assure that students’ rights will continue to
be protected.
    The characteristic of Accelegator that could most easily be questioned
regarding FERPA and Allegheny College’s Privacy Policy is access to students’
information. Thus, the design of the program is as follows: Each Academic
Advisor will have access to their advisees’ records.  This is no different than
how the system has functioned for the past 200 years, where the Advisor keeps
all records of their students under lock and key in their office. However,
rather than a physical “lock and key” to ensure a student’s privacy, our
software team implemented Google API and its corresponding security features.
This allows students to securely respond to a form that requests educational
records defined by Allegheny College which is then imported into the Accelegator
program.  As a result, Advisors can easily access and search for student’s
records, digitalizing and streamlining the advising process.
    As our software team found it most efficient to gather information from
students via a Google Form, we then needed a Google API to be able to access
this information somewhere in the Accelegator program.  Google offers the
mechanism called OAuth 2.0 client IDs to create unique identifiers.  This
mechanism creates an access token, containing a unique identifier, that then
enables “A third party-party application to obtain limited access to an HTTP
service, either on behalf of a resource owner by orchestrating an approval
interaction between the resource owner and the HTTP service, or by allowing the
third-party application to obtain access on its own behalf.”[6]  In this case,
the third- party application would be the Academic Advisor accessing the
Accelegator program on behalf of our software development team.  OAuth 2.0 is
imported to spreadsheet.py, while the security information, containing the
private_key_id, private_key, and client_email are found in AGAuthKey.json.  This
file, AGAuthKey.json, is the file that would be used to give Academic Advisors
the authorization to see their specific advisees’ information.
    According to OAuth 2.0 Threat Model and Security Considerations,
authorization codes are secure due to their simplicity in authentication of
clients.[7]  This is not to say that Accelegator cannot be attacked or that the
program is impenetrable, because the authorization code could be authorized on
an attacker’s protected resources.  However, for the level of security needed to
ensure students’ rights under FERPA, OAuth 2.0 is perfectly able to ensure that
only Academic Advisors have access to their advisees’ information because the
authorization code is shared only with specific college faculty who are legally
obliged to keep students’ information, and therefore the authorization code,
private. Accelegator would revolutionize the efficiency of advising.  Rather
than Advisors shuffling through files of papers in their myriad of filing
cabinets looking for the right yet coffee- stained outdated student file, they
could have access to all of their advisees’ information at the click of a
button.  While this access does come with the responsibility of adhering to both
FERPA and Allegheny College’s Privacy Policy, the implementation of OAuth 2.0
ensures that only those Advisors who are legally allowed to access the student’s
information will be able it access it.  This security measure will ensure that
Accelegator and the information that students provide is being privately handled
and only accessed by Academic Advisors.

## Footnotes

[1] U.S. Department of Education, "Parents' Guide to the Family Educational
Rights and Privacy Act: Rights Regarding Children’s Education Records," U.S.
Department of Education, October 2007, , accessed October 28, 2017,
<https://www2.ed.gov/policy/gen/guid/fpco/brochures/parents.html>.

[2] Ibid.

[3]Allegheny College, "Privacy Policy," Allegheny College Registrar, April 15,
1997, , accessed October 26, 2017,
<http://sites.allegheny.edu/registrar/academic-policies/privacy-policy/>.

[4] Ibid.

[5] Ibid.

[6] E. Hammar-Lahav et
al., "The OAuth 2.0 Authorization Protocol draft-ietf-oauth-v2-17," Internet
Engineering Task Force, July 8, 2011, , accessed October 26, 2017,
<https://tools.ietf.org/html/draft-ietf-oauth-v2-17>.

[7] T. Lodderstedt et al., "OAuth 2.0 Threat Model and Security
Considerations," Internet Engineering Task Force, January 2013, , accessed
October 26, 2017, <https://tools.ietf.org/html/rfc6819>.

## Bibliography

Bibliography
Allegheny College. "Privacy Policy." Allegheny College Registrar.
April 15, 1997. Accessed October 26, 2017.
<http://sites.allegheny.edu/registrar/academic-policies/privacy-policy/>.

Hammar-Lahav, E., Yahoo!, D. Recordon,
Facebook, D. Hardt, and Microsoft. "The OAuth 2.0 Authorization Protocol draft-
ietf-oauth-v2-17." Internet Engineering Task Force. July 8, 2011. Accessed
October 26, 2017. <https://tools.ietf.org/html/draft-ietf-oauth-v2-17>.

Lodderstedt, T., Deutsche Telekom AG, M. McGloin, IBM, P. Hunt, and Oracle
Corporation. "OAuth 2.0 Threat Model and Security Considerations." Internet
Engineering Task Force. January 2013. Accessed October 26, 2017.
<https://tools.ietf.org/html/rfc6819>.

U.S. Department of Education. "Parents'
Guide to the Family Educational Rights and Privacy Act: Rights Regarding
Children’s Education Records." U.S. Department of Education. October 2007.
Accessed October 28, 2017.
<https://www2.ed.gov/policy/gen/guid/fpco/brochures/parents.html>.