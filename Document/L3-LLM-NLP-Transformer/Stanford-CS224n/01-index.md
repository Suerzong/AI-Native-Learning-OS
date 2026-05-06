[CS224N Home](index.html)

  * [Coursework](index.html#coursework)
  * [Schedule](index.html#schedule)
  * [Office Hours](office_hours.html)
  * [Final projects](project.html)
  * [Lecture Videos](https://canvas.stanford.edu/courses/217005/external_tools/69960)
  * [Ed Forum](https://edstem.org/us/courses/90535/discussion/7488560)

[ ](http://nlp.stanford.edu/) [ ](http://stanford.edu/)

# CS224N: Natural Language Processing with Deep Learning

### Stanford / Winter 2026

Natural language processing (NLP) is a crucial part of artificial intelligence (AI), modeling how people share information. In recent years, deep learning approaches have obtained very high performance on many NLP tasks. In this course, students gain a thorough introduction to cutting-edge neural networks for NLP.

### Instructors

[ Diyi Yang ](https://cs.stanford.edu/~diyiy/)

[ Yejin Choi ](https://yejinc.github.io/)

### Course Staff

[ John Cho (Course Manager) ](mailto:johncho@stanford.edu)

Swati Dube Batra (Course Manager Advisor)

### Teaching Assistants

[ Julie Kallini (Head TA) ](https://juliekallini.com/)

[ Ahmed Ahmed ](https://ai.stanford.edu/~ahmedah/)

[ David Anugraha ](https://davidanugraha.github.io/)

[ Luke Bailey ](https://lukebailey181.github.io/)

[ Sarah Chen ](https://scholar.google.com/citations?user=IVnb6XQAAAAJ&hl=en)

[ Caroline Choi ](https://cchoi1.github.io/)

[ Advit Deepak ](https://www.linkedin.com/in/advitdeepak/)

[ Nevin George ](https://www.linkedin.com/in/nevingeorge4)

[ Simon Kim ](https://sekim12.github.io/)

[ Ali Sartaz Khan ](https://www.linkedin.com/in/ali-sartaz-khan-9334011a3/)

[ Arpandeep Khatua ](https://arpandeep.com/)

[ Alisa Levin ](https://www.linkedin.com/in/alisa-levin/)

[ Shicheng Liu ](https://george1459.github.io/)

[ Wei Liu ](https://liuwei283.github.io/)

[ Minsik Oh ](https://minsik-ai.github.io/)

[ Chenglei Si ](https://noviscl.github.io/)

[ Mirac Suzgun ](https://sites.google.com/view/msuzgun)

[ Tristan Thrush ](http://www.tristanthrush.com/)

[ Fang Wu ](https://smiles724.github.io/)

[ Qinan Yu ](https://yuqinan.github.io/)

## Logistics

  * **Lectures:** are on Tuesday/Thursday 4:30 PM - 5:50 PM Pacific Time in [NVIDIA Auditorium](https://goo.gl/maps/hRjQYd6MqxB2). The lectures will also be livestreamed on [Canvas](https://canvas.stanford.edu/) via Panopto.
  * **Lecture videos for enrolled students:** are posted on [Canvas](https://canvas.stanford.edu/courses/217005/external_tools/69960) (requires login) shortly after each lecture ends. Unfortunately, it is not possible to make these videos viewable by non-enrolled students.
  * **Publicly available lecture videos and versions of the course:** Complete videos for the CS224N course are available (free!) on [the CS224N 2024 YouTube playlist](https://www.youtube.com/playlist?list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D). Anyone is welcome to enroll in [XCS224N: Natural Language Processing with Deep Learning](https://online.stanford.edu/courses/xcs224n-natural-language-processing-deep-learning), the Stanford Artificial Intelligence Professional Program version of this course, throughout the year (medium fee, community TAs and certificate). Stanford students enroll normally in CS224N and others can also enroll in [CS224N via Stanford online](https://online.stanford.edu/courses/cs224n-natural-language-processing-deep-learning) (high cost, limited enrollment, gives Stanford credit). The lecture slides and assignments are updated online each year as the course progresses. We are happy for anyone to use these resources, and we are happy to get acknowledgements.
  * **Office hours** : Hybrid format with remote (over Zoom) or in person options. Information [here](office_hours.html).
  * **Contact** : Students should ask _all_ course-related questions in the Ed forum, where you will also find announcements. You will find the course Ed on the course Canvas page or in the header link above. For external enquiries, emergencies, or personal matters that you don't wish to put in a private Ed post, you can email us at _cs224n-staff-win2526@cs.stanford.edu_. Please send all emails to this mailing list - do not email the instructors directly.

## Content

### What is this course about?

Natural language processing (NLP) or computational linguistics is one of the most important technologies of the information age. Applications of NLP are everywhere because people communicate almost everything in language: web search, advertising, emails, customer service, language translation, virtual agents, medical reports, politics, etc. In the 2010s, deep learning (or neural network) approaches obtained very high performance across many different NLP tasks, using single end-to-end neural models that did not require traditional, task-specific feature engineering. In the 2020s amazing further progress was made through the scaling of Large Language Models, such as ChatGPT. In this course, students will gain a thorough introduction to both the basics of Deep Learning for NLP and the latest cutting-edge research on Large Language Models (LLMs). Through lectures, assignments and a final project, students will learn the necessary skills to design, implement, and understand their own neural network models, using the [Pytorch](https://pytorch.org/) framework.

> _âTake it. CS221 taught me algorithms. CS229 taught me math. CS224N taught me how to write machine learning models.â_ â A CS224N student on Carta

### Previous offerings

Below you can find archived websites and student project reports from previous years. **Disclaimer: assignments change from year to year; please do not do assignments from previous years!**

**CS224N Websites** : [Winter 2025](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1254/) / [Spring 2024](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246) / [Winter 2024](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1244) / [Winter 2023](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1234) / [Winter 2022](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1224) / [Winter 2021](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1214) / [Winter 2020](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1204) / [Winter 2019](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1194) / [Winter 2018](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1184) / [Winter 2017](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1174) / [Autumn 2015](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1162) / [Autumn 2014](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1152) / [Autumn 2013](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1142) / [Autumn 2012](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1132) / [Autumn 2011](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1122) / [Winter 2011](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1114) / [Spring 2010](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1106) / [Spring 2009](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1096) / [Spring 2008](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1086) / [Spring 2007](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1076) / [Spring 2006](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1066) / [Spring 2005](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1056) / [Spring 2004](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1046) / [Spring 2003](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1036) / [Spring 2002](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1026) / [Spring 2000](https://web.stanford.edu/class/archive/cs/cs224n/manning.499)
---
**CS224N Lecture Videos** : [Spring 2024](https://www.youtube.com/playlist?list=PLoROMvodv4rOaMFbaqxPDoLWjDaRAdP9D) / [Winter 2023](https://www.youtube.com/playlist?list=PLoROMvodv4rMFqRtEuo6SGjY4XbRIVRd4) / [Winter 2021](https://www.youtube.com/playlist?list=PLoROMvodv4rOSH4v6133s9LFPRHjEmbmJ) / [Winter 2019](https://www.youtube.com/playlist?list=PLoROMvodv4rOhcuXMZkNm7j3fVwBBY42z) / [Winter 2017](https://www.youtube.com/playlist?list=PL3FW7Lu3i5Jsnh1rnUwq_TcylNr7EkRe6)
**CS224N Reports** : [Winter 2024](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1244/project.html) / [Winter 2023](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1234/project.html) / [Winter 2022](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1224/project.html) / [Winter 2021](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1214/project.html) / [Winter 2020](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1204/project.html) / [Winter 2019](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1194/project.html) / [Winter 2018](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1184/reports.html) / [Winter 2017](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1174/reports.html) / [Autumn 2015 and earlier](http://nlp.stanford.edu/courses/cs224n/)
**CS224d Reports** : [Spring 2016](http://cs224d.stanford.edu/reports_2016.html) / [Spring 2015](http://cs224d.stanford.edu/reports_2015.html)

### Prerequisites

  * **Proficiency in Python**

All class assignments will be in Python (using [NumPy](https://numpy.org/) and [PyTorch](https://pytorch.org)). If you need to remind yourself of Python, or you're not very familiar with NumPy, you can come to the Python review session in week 1 (listed in the [schedule](#schedule)). If you have a lot of programming experience but in a different language (e.g. C/C++/Matlab/Java/Javascript), you will probably be fine.

  * **College Calculus, Linear Algebra** (e.g. MATH 51, CME 100)

You should be comfortable taking (multivariable) derivatives and understanding matrix/vector notation and operations.

  * **Basic Probability and Statistics** (e.g. CS 109 or equivalent)

You should know the basics of probabilities, gaussian distributions, mean, standard deviation, etc.

  * **Foundations of Machine Learning** (e.g. CS221, CS229, CS230, or CS124)

We will be formulating cost functions, taking derivatives and performing optimization with gradient descent. If you already have basic machine learning and/or deep learning knowledge, the course will be easier; however it is possible to take CS224N without it. There are many introductions to ML, in webpage, book, and video form. One approachable introduction is Hal Daumeâs in-progress [_A Course in Machine Learning_](https://web.archive.org/web/20250114002202/http://ciml.info/dl/v0_99/ciml-v0_99-all.pdf). Reading the first 5 chapters of that book would be good background. Knowing the first 7 chapters would be even better!

### Reference Texts

The following texts are useful, but none are required. All of them can be read free online.

  * Dan Jurafsky and James H. Martin. [Speech and Language Processing (2024 pre-release)](https://web.stanford.edu/~jurafsky/slp3/)
  * Jacob Eisenstein. [Natural Language Processing](https://github.com/jacobeisenstein/gt-nlp-class/blob/master/notes/eisenstein-nlp-notes.pdf)
  * Yoav Goldberg. [A Primer on Neural Network Models for Natural Language Processing](http://u.cs.biu.ac.il/~yogo/nnlp.pdf)
  * Ian Goodfellow, Yoshua Bengio, and Aaron Courville. [Deep Learning](http://www.deeplearningbook.org/)
  * Delip Rao and Brian McMahan. [Natural Language Processing with PyTorch](https://searchworks.stanford.edu/view/13241676) (requires Stanford login).
  * Lewis Tunstall, Leandro von Werra, and Thomas Wolf. [Natural Language Processing with Transformers](https://transformersbook.com/)

If you have no background in neural networks but would like to take the course anyway, you might well find one of these books helpful to give you more background:

  * Michael A. Nielsen. [Neural Networks and Deep Learning](http://neuralnetworksanddeeplearning.com)
  * Eugene Charniak. [Introduction to Deep Learning](https://mitpress.mit.edu/books/introduction-deep-learning)



## Coursework

**Disclaimer: Coursework is tentative and subject to change!**

### Assignments (48%)

There are four weekly assignments, which will improve both your theoretical understanding and your practical skills. All assignments contain both written questions and programming parts. In office hours, TAs may look at studentsâ code for assignments 1 and 2, but not for assignments 3 and 4.

  * **Credit** :
    * Assignment 1 (6%): Introduction to word vectors
    * Assignment 2 (14%): Neural network foundations, calculating tensor derivatives, dependency parsing
    * Assignment 3 (14%): Self-attention and Transformers
    * Assignment 4 (14%): Large language model benchmarking and evaluation
  * **Deadlines** : All assignments are due on either a Tuesday or a Thursday _before class_ (i.e. before 4:30pm). All deadlines are listed in the [schedule](#schedule).
  * **Submission** : Assignments are submitted via [Gradescope](https://www.gradescope.com/courses/1208404). You will be able to access the course Gradescope page on Canvas. If you need to sign up for a Gradescope account, please use your _@stanford.edu_ email address. Further instructions are given in each assignment handout. _Do not email us your assignments_.
  * **Late start** : If the result gives you a higher grade, we will not use your assignment 1 score, and we will give you an assignment grade based on counting each of assignments 2â4 at 16%.
  * **Collaboration** : Study groups are allowed, but students must understand and complete their own assignments, and hand in one assignment per student. If you worked in a group, please put the names of the members of your study group at the top of your assignment. Please ask if you have any questions about the collaboration policy.
  * **Honor Code** : We expect students to not look at solutions or implementations online. Like all other classes at Stanford, we take the student [Honor Code](https://ed.stanford.edu/academics/masters-handbook/honor-code) seriously. We sometimes use automated methods to detect overly similar assignment solutions.

### Final Project (49%)

The Final Project offers you the chance to apply your newly acquired skills towards an in-depth application. Students have two options: the **Default Final Project** (in which students tackle a predefined task, namely implementing a minimalist version of GPT-2) or a **Custom Final Project** (in which students choose their own project involving human language and deep learning). Examples of both can be seen on the [Spring 2024 website](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1246/project.html). _Note: TAs may not look at students' code for either the default or custom final projects. The Spring 2024 Default Final Project was based on BERT and has now been replaced with GPT-2._

#### Important information

  * **Credit** : For both default and custom projects, credit for the final project is broken down as follows:
    * Project proposal (8%)
    * Project milestone (6%)
    * Project poster (3%)
    * Project report (32%)
  * **Deadlines** : The project proposal, milestone and report are all due at 4:30pm. All deadlines are listed in the [schedule](#schedule).
  * **Default Final Project** : In this project, students implement parts of the GPT-2 architecture and use it to tackle 3 downstream tasks. Similar to previous years, the code is in PyTorch.
  * **Project advice** [[lecture slides](slides_w26/cs224n-2026-lecture06-final-project.pdf)] [[custom project tips](project/custom-final-project-tips.pdf)]: The _Practical Tips for Final Projects_ lecture provides guidance for choosing and planning your project. To get project advice from staff members, first look at each staff member's areas of expertise on the [office hours page](office_hours.html#staff). This should help you find a staff member who is knowledgable about your project area.
  * **Ethics-related questions** : For guidance on projects dealing with ethical questions, or ethical questions that arise during your project, please contact Wanheng Hu (_wanhenghu@stanford.edu_) or Justin Shin (_justinjs@stanford.edu_).

#### Practicalities

  * **Team size** : Students may do final projects solo, or in teams of up to 3 people. We strongly recommend you do the final project in a team. Larger teams are expected to do correspondingly larger projects, and you should only form a 3-person team if you are planning to do an ambitious project where every team member will have a significant contribution.
  * **Contribution** : In the final report we ask for a statement of what each team member contributed to the project. Team members will typically get the same grade, but we may differentiate in extreme cases of unequal contribution. You can contact us in confidence in the event of unequal contribution.
  * **External collaborators** : You can work on a project that has external (non CS224N student) collaborators, but you must make it clear in your final report which parts of the project were your work.
  * **Sharing projects** : You can share a single project between CS224N and another class, but we expect the project to be accordingly bigger, and you must declare that you are sharing the project in your project proposal.
  * **Mentors** : Every custom project team has a mentor, who gives feedback and advice during the project. Default project teams do not have mentors. A project may have an external (i.e., not course staff) mentor; otherwise, we will assign a CS224N staff mentor to custom project teams after project proposals.
  * **Computing resources** : All teams will receive compute credits thanks to kind donations by Google, Kimi, Modal, and Qwen!
  * **Using external resources** : The following guidelines apply to all projects (though the default project has some more specific rules, details provided in the _Honor Code_ section of the [handout](project_w25/CS_224n__Default_Final_Project__Build_GPT_2.pdf)):
    * You can use any deep learning framework you like (PyTorch, TensorFlow, etc.)
    * More generally, you may use any existing code, libraries, etc. and consult any papers, books, online references, etc. for your project. However, you must cite your sources in your writeup and clearly indicate which parts of the project are your contribution and which parts were implemented by others.
    * Under no circumstances may you look at another CS224N group's code, or incorporate their code into your project.

### Participation (3%)

We appreciate everyone being actively involved in the class! There are several ways of earning participation credit, which is capped at 3%:

  * **Attending guest speakers' lectures** :
    * In the second half of the class, we have four invited speakers. Our guest speakers make a significant effort to come lecture for us, so (both to show our appreciation and to continue attracting interesting speakers) we do not want them lecturing to a largely empty room. As such, we encourage students to attend these virtual lectures live, and participate in Q&A.;
    * All students get 0.375% per speaker (1.5% total) for either attending the guest lecture in person, or by writing a reaction paragraph if you watched the talk remotely; details will be provided. Students do not need to attend lecture live to write these reaction paragraphs; they may watch asynchronously.
  * **Completing feedback surveys** : We will send out two feedback surveys (mid-quarter and end-of-quarter) to help us understand how the course is going, and how we can improve. Each of the two surveys are worth 0.5%.
  * **Ed participation** : The top ~20 contributors to Ed will get 3%; others will get credit in proportion to the participation of the ~20th person.
  * **Karma point** : Any other act that improves the class, like helping out another student in office hours or writing a useful guide for students on some topic, which a CS224N TA or instructor notices and deems worthy: 1%

### Late Days

  * Each student has 6 late days to use. A late day extends the deadline 24 hours. You can use up to 3 late days per assignment (including all four assignments, project proposal, project milestone, and project final report).
  * Once you have used all 6 late days, the penalty is 1% off the final course grade for each additional late day.
  * **Project proposal and milestone (late days are NOT shared):** Late days are applied individually and are not pooled across the team. If a student does not have enough late days remaining, that student receives a 1% deduction to their total course grade for each late day they are short â this penalty applies only to that student.
  * **Final project report (late days CAN be shared):** Late days may be pooled across team members. For example, in a team of three students, the team's total available late days is the sum of each member's remaining late days, divided by three to determine how many days late the team can submit. _At the top of your final report, you must state how many late days your team is pooling and which team members have late days remaining._

### Regrade Requests

If you feel you deserved a better grade on an assignment, you may submit a regrade request on Gradescope within 3 days after the grades are released. Your request should briefly summarize why you feel the original grade was unfair. Your TA will reevaluate your assignment as soon as possible, and then issue a decision. If you are still not happy, you can ask for your assignment to be regraded by an instructor. **Disclaimer: the course staff reserve the right to regrade your entire assignment in addition to the specific questions you request. Submit regrade requests at your own risk.**

### Credit/No credit enrollment

If you take the class credit/no credit then you are graded in the same way as those registered for a letter grade. The only difference is that, providing you reach a C- standard in your work, it will simply be graded as CR.

### All students welcome

We are committed to doing what we can to work for equity and to create an inclusive learning environment that actively values the diversity of backgrounds, identities, and experiences of everyone in CS224N. We also know that we will sometimes make missteps. If you notice some way that we could do better, we hope that you will let someone in the course staff know about it.

### Well-Being and Mental Health

If you are experiencing personal, academic, or relationship problems and would like to talk to someone with training and experience, reach out to the [Counseling and Psychological Services (CAPS)](https://vaden.stanford.edu/caps-and-wellness) on campus. CAPS is the universityâs counseling center dedicated to student mental health and wellbeing. Phone assessment appointments can be made at CAPS by calling 650-723-3785, or by accessing the VadenPatient portal through the Vaden website.

### Auditing the course

In general we are happy to have auditors if they are a member of the Stanford community (registered student, official visitor, staff, or faculty). If you are interested, email us at _cs224n-staff-win2526@cs.stanford.edu_. If you want to actually master the material of the class, we very strongly recommend that auditors do all the assignments. However, due to high enrollment, we cannot grade the work of any students who are not officially enrolled in the class.

### Students with Documented Disabilities

We assume that all of us learn in different ways, and that the organization of the course must accommodate each student differently. We are committed to ensuring the full participation of all enrolled students in this class. If you need an academic accommodation based on a disability, you should initiate the request with the [Office of Accessible Education (OAE)](https://oae.stanford.edu/). The OAE will evaluate the request, recommend accommodations, and prepare a letter for faculty. Students should contact the OAE as soon as possible and at any rate in advance of assignment deadlines, since timely notice is needed to coordinate accommodations. Students should also send your accommodation letter to either the staff mailing list (_cs224n-staff-win2526@cs.stanford.edu_) or make a private post on Ed, as soon as possible.

**OAE accommodations for group projects:** OAE accommodations will not be extended to collaborative assignments.

### AI Tools Policy

Students are required to independently submit their solutions for CS224N homework assignments. Collaboration with generative AI tools such as Co-Pilot and ChatGPT is allowed, treating them as collaborators in the problem-solving process. However, the direct solicitation of answers or copying solutions, whether from peers or external sources, is strictly prohibited.

**Employing AI tools to substantially complete assignments or exams will be considered a violation of the Honor Code.** For additional details, please refer to the Generative AI Policy Guidance [here](https://communitystandards.stanford.edu/generative-ai-policy-guidance).

### Sexual violence

Academic accommodations are available for students who have experienced or are recovering from sexual violence. If you would like to talk to a confidential resource, you can schedule a meeting with the Confidential Support Team or call their 24/7 hotline at: 650-725-9955. Counseling and Psychological Services also offers confidential counseling services. Non-confidential resources include the Title IX Office, for investigation and accommodations, and the SARA Office, for healing programs. Students can also speak directly with the teaching staff to arrange accommodations. Note that university employees â including professors and TAs â are required to report what they know about incidents of sexual or relationship violence, stalking and sexual harassment to the Title IX Office. Students can learn more at [https://vaden.stanford.edu/sexual-assault](are recovering from).



## Schedule

Updated lecture **slides** will be posted here shortly before each lecture. Lecture **notes** will be uploaded a few days after most lectures. The notes (which cover approximately the first half of the course content) give supplementary detail beyond the lectures.

**Disclaimer: Schedule is tentative and subject to change!**
**Disclaimer: Assignments change; please do not do old assignments. We will give no points for doing last year's assignments.**

Date | Description | Course Materials | Events | Deadlines
---|---|---|---|---
**Week 1**

Tue Jan 6 | History of NLP
[[intro slides](slides_w26/cs224n-2026-lecture01-intro.pdf)] [[history slides](slides_w26/cs224n-2026-lecture01-history.pdf)]  |  Suggested Readings:

  1. [Human Language Understanding & Reasoning](https://www.amacad.org/publication/daedalus/human-language-understanding-reasoning)

|  Assignment 1 **out**
[[code](assignments_w26/a1.zip)]  |
Thu Jan 8 | Word Vectors
[[slides](slides_w26/cs224n-2026-lecture02-wordvecs.pdf)] [[notes 1](readings/cs224n_winter2023_lecture1_notes_draft.pdf)] [[notes 2](readings/cs224n-2019-notes02-wordvecs2.pdf)]  |  Suggested Readings:

  1. [Efficient Estimation of Word Representations in Vector Space](http://arxiv.org/pdf/1301.3781.pdf) (original word2vec paper)
  2. [Distributed Representations of Words and Phrases and their Compositionality](http://papers.nips.cc/paper/5021-distributed-representations-of-words-and-phrases-and-their-compositionality.pdf) (negative sampling paper)
  3. [GloVe: Global Vectors for Word Representation](http://nlp.stanford.edu/pubs/glove.pdf) (original GloVe paper)
  4. [Improving Distributional Similarity with Lessons Learned from Word Embeddings](http://www.aclweb.org/anthology/Q15-1016)
  5. [Evaluation methods for unsupervised word embeddings](http://www.aclweb.org/anthology/D15-1036)

Additional Readings:
  1. [A Latent Variable Model Approach to PMI-based Word Embeddings](http://aclweb.org/anthology/Q16-1028)
  2. [Linear Algebraic Structure of Word Senses, with Applications to Polysemy](https://transacl.org/ojs/index.php/tacl/article/viewFile/1346/320)
  3. [On the Dimensionality of Word Embedding](https://papers.nips.cc/paper/7368-on-the-dimensionality-of-word-embedding.pdf)

|  |
Fri Jan 9 | Python Review Session
[[slides](slides_w25/2024 CS224N Python Review Session Slides.pptx.pdf)] [[colab](https://colab.research.google.com/drive/1hxWtr98jXqRDs_rZLZcEmX_hUcpDLq6e?usp=sharing)]  |  __Time 1:30pm-2:50pm
Location NVIDIA Auditorium  |  |
**Week 2**

Tue Jan 13 | Backpropagation and Neural Network Basics
[[slides](slides_w26/cs224n-2026-lecture03-neuralnets.pdf)] [[notes](readings/cs224n-2019-notes03-neuralnets.pdf)]  |  Suggested Readings:

  1. [matrix calculus notes](readings/gradient-notes.pdf)
  2. [Review of differential calculus](readings/review-differential-calculus.pdf)
  3. [CS231n notes on network architectures](http://cs231n.github.io/neural-networks-1/)
  4. [CS231n notes on backprop](http://cs231n.github.io/optimization-2/)
  5. [Derivatives, Backpropagation, and Vectorization](http://cs231n.stanford.edu/handouts/derivatives.pdf)
  6. [Learning Representations by Backpropagating Errors](http://www.iro.umontreal.ca/~vincentp/ift3395/lectures/backprop_old.pdf) (seminal Rumelhart et al. backpropagation paper)

Additional Readings:
  1. [Yes you should understand backprop](https://medium.com/@karpathy/yes-you-should-understand-backprop-e2f06eab496b)
  2. [Natural Language Processing (Almost) from Scratch](http://www.jmlr.org/papers/volume12/collobert11a/collobert11a.pdf)

|  Assignment 2 **out**
[[code](assignments_w26/a2.zip)]
[[handout](assignments_w26/a2.pdf)]
[[latex template](assignments_w26/a2_tex.zip)]  | Assignment 1 **due**
Thu Jan 15 | Language Models and RNNs
[[slides](slides_w26/cs224n-2026-lecture04-rnnlm.pdf)] [[notes](readings/cs224n-2019-notes05-LM_RNN.pdf)]  |  Suggested Readings:

  1. [Learning long-term dependencies with gradient descent is difficult](https://ieeexplore.ieee.org/document/279181) (one of the original vanishing gradient papers)
  2. [On the difficulty of training Recurrent Neural Networks](https://arxiv.org/pdf/1211.5063.pdf) (proof of vanishing gradient problem)
  3. [Vanishing Gradients Jupyter Notebook](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1174/lectures/vanishing_grad_example.html) (demo for feedforward networks)
  4. [Attention Is All You Need](https://arxiv.org/abs/1706.03762.pdf)
|  |
Fri Jan 16 | PyTorch Tutorial Session
[[colab](https://colab.research.google.com/drive/1Pz8b_h-W9zIBk1p2e6v-YFYThG1NkYeS?usp=sharing)]  |  __ Time 1:30pm-2:50pm
Location NVIDIA Auditorium  |  |
**Week 3**

Tue Jan 20 | Transformers
[[slides](slides_w26/cs224n-2026-lecture05-transformers.pdf)] [[notes](readings/cs224n-self-attention-transformers-2023_draft.pdf)]  |  Suggested Readings:

  1. [Attention Is All You Need](https://arxiv.org/abs/1706.03762.pdf)
  2. [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
  3. [Transformer (Google AI blog post)](https://ai.googleblog.com/2017/08/transformer-novel-neural-network.html)
  4. [Layer Normalization](https://arxiv.org/pdf/1607.06450.pdf)
  5. [Image Transformer](https://arxiv.org/pdf/1802.05751.pdf)
  6. [Music Transformer: Generating music with long-term structure](https://arxiv.org/pdf/1809.04281.pdf)
  7. [Jurafsky and Martin Chapter 9 (The Transformer)](https://web.stanford.edu/~jurafsky/slp3/9.pdf)


Thu Jan 22 | Final Projects: Custom and Default; Practical Tips
[[slides](slides_w26/cs224n-2026-lecture06-final-project.pdf)]  |  Suggested Readings:

  1. [Practical Methodology](https://www.deeplearningbook.org/contents/guidelines.html) (_Deep Learning_ book chapter)

| Assignment 3 **out**
[[code](assignments_w26/a3.zip)]
[[handout](assignments_w26/a3.pdf)]
[[latex template](assignments_w26/a3_tex.zip)]
| Assignment 2 **due**
**Week 4**

Tue Jan 27 | Pretraining (Scaling, Systems, Data)
[[slides](slides_w26/cs224n-2026-lecture07-pretraining.pdf)]  |  Suggested Readings:

  1. [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/pdf/1810.04805.pdf)
  2. [Contextual Word Representations: A Contextual Introduction](https://arxiv.org/abs/1902.06006.pdf)
  3. [The Illustrated BERT, ELMo, and co.](http://jalammar.github.io/illustrated-bert/)
  4. [Jurafsky and Martin Chapter 10 (Masked Language Models)](https://web.stanford.edu/~jurafsky/slp3/10.pdf)
  5. [The Llama 3 Herd of Models](https://arxiv.org/abs/2407.21783)

|  |
Thu Jan 29 |  Post-training (RLHF, SFT, DPO) [[slides](slides_w26/cs224n-2026-lecture08-posttraining.pdf)]  |  Suggested Readings:

  1. [Aligning language models to follow instructions](https://openai.com/research/instruction-following)
  2. [Scaling Instruction-Finetuned Language Models](https://arxiv.org/abs/2210.11416)
  3. [AlpacaFarm: A Simulation Framework for Methods that Learn from Human Feedback](https://arxiv.org/abs/2305.14387)
  4. [How Far Can Camels Go? Exploring the State of Instruction Tuning on Open Resources](https://arxiv.org/abs/2306.04751)
  5. [Direct Preference Optimization: Your Language Model is Secretly a Reward Model](https://arxiv.org/abs/2305.18290)

| Project Proposal **out**
[[handout](project/Project_Proposal_Instructions.pdf)]

Default Final Project **out**
[[handout](project/DFP_Instructions.pdf)]  |
**Week 5**

Tue Feb 3 |  Efficient Adaptation (Prompting + PEFT)
[[slides](slides_w26/cs224n-2026-lecture09-peft.pdf)]  |  Suggested Readings:

  1. [Language Models are Few-Shot Learners](https://arxiv.org/abs/2005.14165)
  2. [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903)
  3. [The Lottery Ticket Hypothesis: Finding Sparse, Trainable Neural Networks](https://arxiv.org/abs/1803.03635)
  4. [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)
  5. [Parameter-Efficient Transfer Learning for NLP](https://arxiv.org/abs/1902.00751)

|  |
Thu Feb 5 |  Agents, Tool Use, and RAG
[[slides](slides_w26/cs224n-2026-lecture10-rag-agents.pdf)]  |  Suggested Readings:

  1. [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
  2. [Language Agents: Foundations, Prospects, and Risks](https://language-agent-tutorial.github.io/)
  3. [Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401)
  4. [Toolformer: Language Models Can Teach Themselves to Use Tools](https://arxiv.org/abs/2302.04761)

| Assignment 4 **out**
[[code](assignments_w26/a4.zip)]
[[handout](assignments_w26/a4.pdf)]
[[latex template](assignments_w26/a4_tex.zip)]  | Assignment 3 **due**
Fri Feb 6 | Hugging Face Transformers Tutorial Session
[[slides](materials/hf_transformers_tutorial.pdf)] [[colab](https://colab.research.google.com/drive/1FyCMNTXfirWbJ18GuIT_JiTW0gwrxI3O?usp=sharing)]  |  __ Time 1:30pm-2:50pm
Location NVIDIA Auditorium  |  |
**Week 6**

Tue Feb 10 |  Benchmarking and Evaluation [[slides](slides_w26/cs224n-2026-lecture11-evaluation.pdf)]  |  Suggested Readings:

  1. [Challenges and Opportunities in NLP Benchmarking](https://www.ruder.io/nlp-benchmarking/)
  2. [Measuring Massive Multitask Language Understanding](https://arxiv.org/abs/2009.03300)
  3. [Holistic Evaluation of Language Models](https://arxiv.org/abs/2211.09110)
  4. [AlpacaEval](https://tatsu-lab.github.io/alpaca_eval/)

|  | Project Proposal & Mentor Form **due**

Thu Feb 12 |  Reasoning 1
[[slides](slides_w26/cs224n-2026-lecture12-reasoning-part1.pdf)]  |  Suggested Readings:

  1. [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://arxiv.org/abs/2201.11903)
  2. [Self-Consistency Improves Chain of Thought Reasoning in Language Models](https://arxiv.org/abs/2203.11171)
  3. [DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning](https://arxiv.org/abs/2501.12948)
  4. [DAPO: An Open-Source LLM Reinforcement Learning System at Scale](https://arxiv.org/abs/2503.14476)

|  |
**Week 7**

Tue Feb 17 | Reasoning 2
[[slides](slides_w26/cs224n-2026-lecture13-reasoning-part2.pdf)]  |  Suggested Readings:

  1. [Let's Verify Step by Step](https://arxiv.org/abs/2305.20050)
  2. [Fast Inference from Transformers via Speculative Decoding](https://arxiv.org/abs/2211.17192)
  3. [Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters](https://arxiv.org/abs/2408.03314)
  4. [RoFormer: Enhanced Transformer with Rotary Position Embedding](https://arxiv.org/abs/2104.09864)

| Project Milestone **out** [[handout](project/Project_Milestone_Instructions.pdf)]  | Final Project Proposals **returned**
Thu Feb 19 | Guest Lecture: Tokenization and Multilinguality (by [Julie Kallini](https://juliekallini.com/)) [[slides](slides_w26/cs224n-2026-lecture14-guest-julie-tokenization-multilinguality.pdf)]  |  Suggested readings:

  1. [Jurafsky & Martin Chapter 2](https://web.stanford.edu/~jurafsky/slp3/2.pdf)
  2. [Neural Machine Translation of Rare Words with Subword Units](https://arxiv.org/pdf/1508.07909)
  3. [Unsupervised Cross-lingual Representation Learning at Scale](https://aclanthology.org/2020.acl-main.747.pdf)
  4. [Do All Languages Cost the Same? Tokenization in the Era of Commercial Language Models](https://aclanthology.org/2023.emnlp-main.614.pdf)

|  | Assignment 4 **due**
**Week 8**

Tue Feb 24 | Guest Lecture: Interpretability (by [Been Kim](https://beenkim.github.io/))  |  Suggested readings:

  1. [Because we have LLMs, we Can and Should Pursue Agentic Interpretability](https://arxiv.org/abs/2506.12152)
  2. [The Pareto Frontier of Human-Centered AI](https://medium.com/@beenkim/the-pareto-frontier-of-human-centered-ai-54f90ba5872c)
  3. [Bridging the humanâAI knowledge gap through concept discovery and transfer in AlphaZero](https://www.pnas.org/doi/10.1073/pnas.2406675122)
  4. [We Can't Understand AI Using our Existing Vocabulary](https://arxiv.org/abs/2502.07586)
  5. [Neologism Learning for Controllability and Self-Verbalization](https://arxiv.org/abs/2510.08506)

| Final Project Report Instructions **out**
[[Instructions](project/Project_Report_Instructions.pdf)]  |
Thu Feb 26 | Social and Broader Impacts of NLP (Risks)
[[slides](slides_w26/cs224n-2026-lecture16-impact-on-humanity.pdf)]  |  |  | Final Project Milestone **due**
Fri Feb 27 | _
|  |  | **Course Withdrawal Deadline**
**Week 9**

Tue Mar 3 | Guest Lecture: Multimodality (by [Luke Zettlemoyer](https://homes.cs.washington.edu/~lsz/))
| Suggested readings:

  1. [Visual Sketchpad: Sketching as a Visual Chain of Thought for Multimodal Language Models](https://visualsketchpad.github.io/)
  2. [Chameleon: Mixed-Modal Early-Fusion Foundation Models](https://arxiv.org/abs/2405.09818)
  3. [Transfusion: Predict the Next Token and Diffuse Images with One Multi-Modal Model](https://arxiv.org/abs/2408.11039)
  4. [Mixture-of-Transformers: A Sparse and Scalable Architecture for Multi-Modal Foundation Models](https://arxiv.org/abs/2411.04996)

Optional readings:
  1. [Scaling Laws for Generative Mixed-Modal Language Models](https://arxiv.org/abs/2301.03728)
  2. [Scaling Autoregressive Multi-Modal Models: Pretraining and Instruction Tuning](https://arxiv.org/abs/2309.02591)
  3. [Retrieval Augmented Multimodal Language Modeling](https://arxiv.org/abs/2211.12561)
  4. [LMFusion: Adapting Pretrained Language Models for Multimodal Generation](https://arxiv.org/abs/2412.15188)
  5. [OneFlow: Concurrent Mixed-Modal and Interleaved Generation with Edit Flows](https://arxiv.org/abs/2510.03506)
  6. [Multimodal RewardBench: Holistic Evaluation of Reward Models for Vision Language Models](https://arxiv.org/abs/2502.14191)
  7. [Reconstruction Alignment Improves Unified Multimodal Models](https://arxiv.org/abs/2509.07295)

|  | Final Project Milestones **returned**
Thu Mar 5 | Guest Lecture: Tinker and LoRA Without Regret (by [John Schulman](http://joschu.net/))  |  |
**Week 10**

Tue Mar 10 | Open Questions in NLP 2026 [[slides](slides_w26/cs224n-2026-lecture19-open-questions.pdf)]  |  |  |
Thu Mar 12 | No Lecture  |  |  | Final project **due**
Mon Mar 16 | Final Project Poster Session  |  __Time 12:15pm-3:15pm
Location AOERC
ALL On-campus students must attend in person!  |  | [[Printing guide](https://docs.google.com/document/d/1J8-TVVvndimSwq3jGzpMO_OtPAx_EaU9nUiiPUQdVpY)]

## Sponsors

We are grateful to our sponsors for their generous support of CS224N.
