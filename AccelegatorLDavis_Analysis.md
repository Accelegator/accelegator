## Understanding Accelegator and LDavis Visualization

Accelegator uses an R package for interactive topic model visualization.1 This
package is called LDavis and was designed by Carson Sievert from Iowa State
University and Kenneth E. Shirley from AT&T Labs Research.  In creating
LDavis, their goal was to create a visualization of topic-term relationships
so that the user could better understand the meaning, prevalence, and
relevance of the topics.2  While visualization based on Latent Dirichlet
Allocation is not necessarily a new concept in the world of visualizing
results, it certainly has been revolutionized by LDavis.

In providing information on how to analyze the results of the Accelegator
system, the following informative text will be primarily referencing Sievert
and Shirley’s joint paper titled LDavis: A method for visualizing and
interpreting topics.  The information will be available in two separate
sections: first, the structure of LDavis and second, how to analyze the
results.

The structure of LDavis, the visualization of the results garnered from
student submitted forms, has two distinct pieces.  The left panel of the
visualization model, “Presents a global view of the topic model” and shows
both prevalence and relatedness.3  The circles are plotted on a two-
dimensional plane where the centers of the circles are calculated by computing
the distance between the topics.4  Each topic’s overall prevalence is
demonstrated by the area of its circle, where topics are then sorted in
decreasing order of prevalence.5

The right panel is a horizontal barchart.  The bars represent, “The individual
terms that are the most useful for interpreting the currently selected topic
on the left”, or on the two-dimensional plane.  The barchart itself helps
users navigate the meaning of the topic.  Within each horizontal bar, two
colors are evident.  The first is blue and shows the corpus-wide frequency of
that specific term.  Corpus-wide refers to all of the text that has been
submitted to be evaluated.  In the case of Accelegator, it includes every
student submission and shows how frequently that term is used in the corpus of
the submissions. The red portion of the bar shows the topic-specific frequency
of the specific term in showing how frequently the term is used within one
specific topic, where each topic is denoted by a circle.

Specific to the LDavis structure is the importance of relevancy within the
visualization.  Sievert and Shirley derive relevancy mathematically, but the
term essentially gives weight to the number of terms in the vocabulary, the
marginal probability of the term in the corpus, and the weight given to the
probability of the term under the relative topic to its lift.  The importance
of relevancy is great in LDavis because terms can be distinctly identified as
relevant ranked solely by probability but have little meaning to understanding
the student submissions.  In adjusting Lambda from 0.0 to 1.0, one can see how
the barchart changes correspondingly.6  Sievert and Shirley suggest that
setting Lambda at 0.6 gives a much better visualization of frequent terms that
are also relevant to the topic with an estimated probability of correct
identification at 70%.7  This probability drops between 10-15% when Lambda is
not set at 0.6.

The uses of LDavis specifically in regard to Accelegator are as follows.  An
advisor wishing to know more about how their advisees responded on their
advisee submission forms can select a topic (circle on the left panel of the
visualization) which will reveal the most relevant terms for that topic
(represented as horizontal bars on the right panel of the visualization).
While Lambda is best set at 0.6 for correct identification of terms, the
professor can increase or decrease Lambda from 1 to 0 to, “Alter the rankings
of terms to aid topic interpretation.”8  A professor can then distinguish a
highly relevant term from less relevant terms by both its lift (depicted by a
high ratio of red bar to gray bar) and its probability (the length of the red
bar in its entirety).9

To view prevalence of topics, the advisor can then study the areas of the
circles that are proportional to the prevalence of the topics in the corpus.
The areas of these circles show the commonness of the topics in all of the
student submissions.  If the areas of the circles are small, the commonness of
the topics is low and might lead the advisor to believe that the student has
responded in multiple different ways to the questions that they were
presented.  If the circles are large, the advisor may be able to quickly
deduce that the commonness of topics is high and thus that students often
submitted answers on their forms that shared comments on the same topic.

While the best use for Accelegator may depend on each individual advisor, the
importance of Accelegator must be emphasized.  Accelegator and its
corresponding production of a LDavis visualization allows advisors to explore
terms and topics that are most helpful in advising students.  Either as a
brief overview before an advisor meeting, a way to group students together
based on their shared interest, or a means to search for students who may be
particularly interested in a job or internship opportunity, the visualization
immediately defines important terms and concepts such as "weakness,”
“interest,” “strength,” and “enjoy” which then can be linked to other frequent
terms such as “security,” “government,” “long-term,” and so on and so forth.
In this way, rather than pouring over dozens of advisees' files trying to
remember which student showed interest in working in cyber security for the
government, Accelegator analyzes the results for the advisor and displays them
in an easy to use and understand interactive visualization. Then, if an
advisor feels the need to isolate certain examples of when the student showed
interest in an “internship” at "Google,” they can individually search for
terms that manifest in topics and visualize which students showed interest in
such an opportunity.

Likewise, professors are also able to search for a specific student in
preparation of a meeting with them to review what their concerns, interests,
and career goals are based on the visualization created by LDavis.
Accelegator will revolutionize the world of student advising by providing
professors with clarity, focus, and a sense of direction when attempting to
offer students the best opportunities and personalized career and academic
counseling possible.

1 Carson Sievert and Kenneth E. Shirley, “LDavis: A method for visualizing and
interpreting topics,” in Proceedings of the Workshop on Interactive Language
Learning, Visualization, and Interfaces (Baltimore, MD: 2014 Association for
Computation Linguistics, 2014. Accessed November 2, 2017,
http://www.aclweb.org/anthology/W14-3110.

2 Ibid.

3 Ibid.

4 Ibid.

5 Ibid.

6 Ibid.

7 Ibid.

8 Ibid.

9 Ibid.


Bibliography

Sievert, Carson. "LDAvis: A method for visualizing and interpreting topic
models." American Statistical Association. 2014. Accessed November 2, 2017.
http://stat-graphics.org/movies/ldavis.html.

Sievert, Carson, and Kenneth E. Shirley. " Sievert, Carson, and Kenneth E.
Shirley. LDavis. Computer software. GitHub. 2014. Accessed November 2, 2017.
https://github.com/cpsievert/LDAvis/graphs/contributors.

LDAvis: A method for visualizing and interpreting topics." In Proceedings of
the Workshop on Interactive Language Learning, Visualization, and Interfaces,
63-70. Baltimore, MD: 2014 Association for Computational Linguistics, 2014.
Accessed November 2, 2017. http://www.aclweb.org/anthology/W14-3110.
