<!-- Slide number: 1 -->

CLCheck Smart Auto Judgement

Ikhwanul Abiyu Dhiyya’ul Haq - 25110002

Firmware Design Department

UI Design Team

### Notes:
Good afternoon everyone. My name is Ikhwanul Abiyu Dhiyya’ul Haq.

Today, I would like to present my Permanency Project report as a Probation Employee in the Firmware Design Department, specifically within the UI Design Team.

<!-- Slide number: 2 -->

Probation Timeline Activities
01.

Job Description
02.
Presentation Content

Project Presentation
03.
Problem Background
Countermeasure and Requirement List
Improvement Implementation
Improvement Report

Probation Impression
04.

### Notes:
My presentation today covers four main agendas.

First, I will review my Probation Activities timeline.
Second, my Job Description.
Third, the core of this presentation: The Project itself, including the problem background and the solution I developed.
Finally, I will share my impressions during this probation period.

<!-- Slide number: 3 -->

Probation Timeline Activities
01.

<!-- Slide number: 4 -->

| Month | November | December |  |  |  | January |  |  |  | February |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Week | 4 | 1 | 2 | 3 | 4 | 1 | 2 | 3 | 4 | 1 | 2 |
| Join Date |  |  |  |  |  |  |  |  |  |  |  |
| HR Training |  |  |  |  |  |  |  |  |  |  |  |
| General Training |  |  |  |  |  |  |  |  |  |  |  |
| FW Training |  |  |  |  |  |  |  |  |  |  |  |
| UI Training |  |  |  |  |  |  |  |  |  |  |  |
| OJT: Before Release Evaluation Lucida-MDX |  |  |  |  |  |  |  |  |  |  |  |
| OJT: Before Release Evaluation Platini6-MG |  |  |  |  |  |  |  |  |  |  |  |
| Permanency Project |  |  |  |  |  |  |  |  |  |  |  |

![](Picture8.jpg)

![](Picture7.jpg)

![](Picture9.jpg)

### Notes:
Starting with the timeline. I joined in late November.

And all of the training from HR Training, General Training, FW Training, UI Training already completed by at least 50%

For On-the-Job Training, I was involved in the 'Before Release Evaluation' for two models: Lucida-MDX and Platini6-MG.

<!-- Slide number: 5 -->

Job Description
02.

<!-- Slide number: 6 -->

Placed on GUI Section - Standalone Team (EkaT)
Module:
Home
Copy
Fax
Scan
Tray
JobCancel
Reaction
TextPrint
InputAppli
Left Document
Job Description

### Notes:
I am placed in the GUI Section as part of the Standalone Team (EkaT). Eka-san

My responsibilities cover maintaining and developing various standalone modules, including Home, Copy, Fax, Scan, and several others listed here

<!-- Slide number: 7 -->

Project Presentation
03.

### Notes:
Now, I would like to move to the main topic: My Improvement Project.

<!-- Slide number: 8 -->

Problem Background

### Notes:

<!-- Slide number: 9 -->

Problem Background
| Model | Count of QTAS related to Baseline |
| --- | --- |
| Chloe | 1 |
| Cate/Cruise2 | 1 |
| Lionel3 | 1 |
| Naiad8 | 2 |
CLCheck has been performed…

BUT! there are still 5 QTAS / Bug Tickets related to the CLCheck!
Doing CLCheck is Time Consuming… can take about 4 - 20 hrs to perform!
Checks Performed + Time Consuming → Why do Quality Issues Persist?

### Notes:
The background of this project comes from a recurring quality issue.

Even though we perform a ‘CLCheck' process, we still found 5 Bug Tickets (QTAS) related to CLCheck

Furthermore, the manual checking process takes a very long time, between 4 to 20 hours per module depending on complexity.

So, the big question is: 'Checks Performed + Time Consuming → Why do Quality Issues Persist?'

<!-- Slide number: 10 -->

Problem Background

There is a process called CLCheck (must finish before SDR1A)

### Notes:
To give context, 'Baseline Check' is a critical verification activity that happen and must finish before SDR1A

<!-- Slide number: 11 -->

Base Model Release Stream
Main Stream

01/12/2025

01/02/2026
What is CLCheck?
Must Check the Code
. . . .
. . . .
Must check the Code

Target Model
Today!
This Guarantees:
Consistency (Follows the proven structure of Base/Prev. Model)
Stability (Fewer unintended bugs)

### Notes:
CLCheck is a code verification process performed prior to development or implementation.

It involves checking the base model stream and the main stream preceding the target model.

This process allows us to guarantee consistency and stability.

<!-- Slide number: 12 -->

1

01.
Define FileList Document path from File List Check

2

02.
Define Preset File path (from UI Development Plan File)

3
03.
Define the preset number (stream path to check)

4
Define CLCheck Start and CLCheck End
04.
6

Inspect every modification occurring within that specific range
06.

5

05.
List up every file path from perforce to the excel (Already automated with existing tool)

How?

### Notes:
The process involves 6 steps. We define the files

Define the UI Development Plan file

Define the preset number

Define the CL Start & CL End

List up every file path from perforce to excel. Its already automated with existing tool, thanks to yudi-san

And we have to inspect every modification occurring within that specific range

Klik

However, the bottleneck lies in Step 6. This is where we have to list up every file and inspect every single modification line-by-line manually.

<!-- Slide number: 13 -->

![A screenshot of a computer AI-generated content may be incorrect.](Picture35.jpg)
Let’s take a look how to do the actual CLCheck...
Does the code need to evaluate?
Click this cell filled with CL Number
Does the code need to fix?
Fill the reason of judgement

| File Path | Target CL | Necessity of Evaluation | Implementation or Not | Inspection Result | Reason |
| --- | --- | --- | --- | --- | --- |
| //source\_Triforce/…/Window/UIPresetWindow.h | 1055459 |  |  |  |  |

Y/N
Y/N
Whatever the reason of evaluation…
Designer had to fill this before SDR1A
Designer had to fill this before SDR1A
SDR1A

### Notes:
Let’s take a look how  to do the actual CLCheck…

So first, you have to click this cell, the one with numbers. And after that, you have to inspect the code modification

After judging this file, you have to fill the necessity of evaluation column and the implementation or not, and don’t forget to add the reason of judgement

And you have to do this before SDR1A

Next…

<!-- Slide number: 14 -->

![A screenshot of a computer AI-generated content may be incorrect.](Picture14.jpg)

After SDR1A…
Does the code resulting bug?

| File Path | Target CL | Necessity of Evaluation | Implementation or Not | Inspection Result | Reason |
| --- | --- | --- | --- | --- | --- |
| //source\_Triforce/…/Window/UIPresetWindow.h | 1055459 |  |  |  |  |
What if….
Y
OK/NG
N
Whatever the reason of evaluation…

Designer had to fill this before SDR2

SDR2

### Notes:
After SDR1A, you have to fill the inspection result, is it OK/NGIf its OK, just go to the implementation

If its NG, please fix the modification so the code become OK in the judgementAnd designer do this before SDR2

That’s the example of 1 item, what if?

<!-- Slide number: 15 -->

Current Condition
| File Path | Target CL | Necessity of Evaluation | Implementation or Not | Inspection Result | Reason |
| --- | --- | --- | --- | --- | --- |
| //source\_Triforce/…/Window/UIPresetWindow.h | 1055459 |  |  |  |  |
| //source\_Triforce/…/Window/UIPresetWindow.cpp | 1055459 |  |  |  |  |
| //source\_Triforce/…/Appli/UIHomeApp.h | 1055459 |  |  |  |  |
| //source\_Triforce/…/Controller/UIHomeController.h | 1055459 |  |  |  |  |
| //source\_Triforce/…/Controller/UIHomeController.cpp | 1055459 |  |  |  |  |
| //source\_Triforce/…/Model/Home/UIHomeCustom.h | 1055459 |  |  |  |  |
| //source\_Triforce/…/Taurus/Window/Home/SEG\_BIJ\_/UIHomeWindow.cpp | 1055459 |  |  |  |  |
| etc until the last list... | etc until the last CL... |  |  |  |  |
N
N
Whatever the reason of evaluation…
Whatever the reason of evaluation…
N
N
Whatever the reason of evaluation…
Y
N
Whatever the reason of evaluation…
N
Y
Whatever the reason of evaluation…
N
Y
Whatever the reason of evaluation…
Y
Y
Whatever the reason of evaluation…
N
N

### Notes:
What if you have to

click,
judge,
fill,
Type the reason (repeat x3)

Until the end of the list,
until the end of the stream to check

Well, it’s a big problem to consider.

<!-- Slide number: 16 -->

How Bug Happened?
After Designer Implementation
→
→
→
→
→
→
???
→
???
→
???
→
Before…
→
→
→
→
→
→
| Table B |
| --- |
| Copy |
| Fax |
| Mail |
| DPC |
| Folder |
| Box |
| Card |
| PC |
| Memory |
| Table A |
| --- |
| Copy |
| Fax |
| Mail |
| Folder |
| PC |
| Memory |
| Table A |
| --- |
| Copy |
| Fax |
| Mail |
| Folder |
| PC |
| Memory |
| Table B |
| --- |
| Copy |
| Fax |
| Mail |
| Folder |
| PC |
| Memory |

| File Path | Target CL | Necessity of Evaluation | Implementation or Not | Inspection Result | Reason |
| --- | --- | --- | --- | --- | --- |
| //source\_Triforce/…/Window/UIPresetWindow.h | 1055459 |  |  |  |  |
N
N

No need evaluation
OK
Y
Y
Critical: Index shifted!
NG

### Notes:
Here is a specific example of how bug happens.

Imagine we have two tables that map to each other one-to-one: Copy links to Copy, Fax links to Fax, et cetera.

Then, a designer inserts a new item right in the middle of the table. As a result, as you can see here, the mapping shifts: Folder now points to DPC, PC points to Folder, and Memory points to Box.

This is the direct result of a judgment error by the designer. They marked the check as: 'N, N, OK, No need evaluation.’

In reality, the correct judgment should have been: 'Y, Y, NG (Not Good), Critical: Index shifted.

<!-- Slide number: 17 -->

Why is QTAS related to CLCheck still passing through SoftGi?

Man
Method
Material
Machine

Index shifts are invinsible (changes/additions to enum items, arrays, add/change BTO)
The current verification mechanism is based on sampling, leaving a risk of non-sample files slipping through
Designers experience fatigue when performing manual checks with numerous check items
Limitations of the diff tool: it only highlights syntax changes, but does not highlight the impact

Knowledge gap between new and old designers
Checking depends on manual line-by-line diff

### Notes:
Why do bugs still escape? I analyzed this using 4M:

Man: Designers get fatigued checking thousands of lines, and there is a knowledge gap for new members.

Method: We rely on sampling, so some files might be skipped.

Machine: The current Diff Tool only highlights syntax changes (text), not logic impact.

Material: Index shifts are often 'invisible' in the diff tool."

<!-- Slide number: 18 -->

Countermeasure & Requirement List

<!-- Slide number: 19 -->

Problem Solution
| Solution Choice | Advantage | Disadvantage |
| --- | --- | --- |
| Checksheet Based | CLCheck has standards → maintains quality | High Cycle Time. Since the current process is already time-consuming, adding a checksheet makes it take even longer. |
| Peer Review (Cross-Check) | Double Filter. The PIC and SubPIC of the module cross-check each other's CLCheck results. | Double Cost. The time required for CLCheck becomes increasingly long. |
| System Logic Validation | CLCheck has standards, but since tools perform the check → errors are almost impossible. | Requires time to refine and perfect the tool. |

### Notes:
There is 3 solution I offer for this problem, there is a checksheet based, peer review, and system logic validation. I’m choosing system logic validation because of its advantage, had a big quality impact, and the disadvantage just requires time to refine and perfect the tool.

<!-- Slide number: 20 -->

Method Selection Matrix
| Consideration | Office Automation | Full Desktop App | Portable Modular App |
| --- | --- | --- | --- |
| Development Complexity | Low (Current tool using VBA) | Very High (Complex Architecture) | Low (Structured MVC but Lightweight) |
| Deployment | Manual (Copy File Excel) | Complex (Need Installer/Setup) | Portable (Just run .exe file) |
| Maintainability | Low (Hard to Debug) | Medium (Need recompile) | High (Modular Architecture) |
| Performance | Slow (Excel Limit) | Fast | Fast |

Office Automation:          Continue using existing modified tools to enable the improvement (smart judgement)
Full Desktop App:             Migrate all existing tools to the new desktop app
Portable Modular App:    The smart judgement app will be created separately from the existing tool

### Notes:
And for the method selection matrix, there is 3 method too,

office automation which is Continue using existing modified tools to enable the improvement

Full desktop app is Migrate all existing tools to the new desktop app

And last is portable modular app which is The smart judgement app will be created separately from the existing tool

<!-- Slide number: 21 -->

Conclusion Countermeasure: System Logic Validation
From the countermeasure requirements above, we obtain requirements from our tool:
| No. | Check Item | Explanation |
| --- | --- | --- |
| 1. | Enum, Array, List Check | The tool must be able to detect the insertion or deletion of items in the middle of a list. |
| 2. | BTO & Preprocessor Check | The tool must be able to read the relevant BTO and its associated preprocessors. |
| 3. | Non-functional Check (Comments, Whitespace, Tabs) | The tool must be able to identify non-functional changes (such as comments) that have zero impact on the code logic. |
| 4. | Validation of “Copy Up” | The tool must be able to determine when a piece of code qualifies as a “Copy Up.” |
| 5. | Report Generation | The tool must be able to generate reports containing "Necessity of Evaluation," "Implementation or Not," and "Reason." |

### Notes:
And, From the countermeasure requirements above, we obtain requirements from our tool

But due to the limitations of time, i only able to make the MVP tool for these items

For the remaining, i need some times because of its complexity

<!-- Slide number: 22 -->

Improvement Implementation

<!-- Slide number: 23 -->

Workflow Before & After Improvement

Are there any remaining files?
START
END
Click the CL
Judge the change
Fill the excel with the judgement
Leader Review
NO
YES
Before
System Logic Validation Tool
START
END
Leader Review
After

### Notes:
This is the previous workflow. It starts by clicking the CL, judging the change, and filling the Excel sheet with the judgment.

If there are still remaining files in the list, the process repeats. If not, the designer submits it to the leader for review.

In the improved workflow, the entire CLCheck process is handled automatically by the System Logic Validation Tool. Once the tool finishes, the output is simply handed over to the leader for review.

<!-- Slide number: 24 -->

Improvement Report

<!-- Slide number: 25 -->

Improvement Effect
| No. | Problem Case / Issue | Problem Solving | Resolve |
| --- | --- | --- | --- |
| 1 | The diff tool currently in use doesn’t detect changes in logic/structure. It only detects changes in text. | Collect requirements when it filled with ‘N’ and when it is filled wit ‘Y’, then create tools that can make judgements based on the requirements created | Yes |

### Notes:
For the improvement effect, we go back to the problem case, which is : the diff tool is only detect changes in text, not logicwith current problem solving, the problem is resolved

<!-- Slide number: 26 -->

Project Timeline
| Month | January |  |  |  | February |  |  |  | March |  |  |  | April |  |  |  | May - July |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Week | 1 | 2 | 3 | 4 | 1 | 2 | 3 | 4 | 1 | 2 | 3 | 4 | 1 | 2 | 3 | 4 | 1 | 2 | 3 | 4 |
| Problem Survey |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Problem Fixation |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Concept Design |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Prototype Implementation |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Project Presentation |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Detail Design |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Study Requirement |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Implementation |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Evaluation #1 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Review |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Evaluation #2 |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Sharing Project |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
Tool Implementation Target Model:

Before Nifty SDR1A
Planned for sharing project at late July
Idul Fitri Holiday

### Notes:
And for the project timeline is like this

My highlight is on the sharing project that to be planned at late July

With the target of implementation before SDR1A of nifty

<!-- Slide number: 27 -->

Probation Impression
04.

<!-- Slide number: 28 -->

Probation Impression

Pros
Challenges

01.
Exposure to Professional Development Standards
01.
Complex Scope Management
02.
Language Barrier
02.
Supportive Team Environment
03.
Legacy System Adaptation
03.
New Technical Knowledge

### Notes:
So my probation impression mostly a positive things, (baca)

And for the challenges, is (Baca)

Languange barrier means some of SEC PIC cant use English, they only use Japanese, so that’s a challenge for me

<!-- Slide number: 29 -->

Thank you!
Any question?

<!-- Slide number: 30 -->

Appendix

<!-- Slide number: 31 -->

Survey Explanation
Purpose
Find proposed problem in UI activity and its countermeasure
Target
All UI Member (19 people)
List of Question
1. Based on UI Activity, which section is very complex?
*complex : take a long time/most mistake/difficult to do
2. What is the main problem which make you say, its section is complex?
3. How the main problem happen?

<!-- Slide number: 32 -->

Survey Result
15/19 UI Member have been interviewed

| Status | Count |
| --- | --- |
| Asked | 15 |
| Not Asked | 4 |

<!-- Slide number: 33 -->

Survey Result
Design section is very complex for 46% (6/19) UI member, especially on detail design
QTAS Problem Solving Process
UI V Process

| Section |
| --- |
| Reproduce |
| Analysis |
| Correction |
| Review |
| Unit Test |
| Section |
| --- |
| Design |
| Implementation |
| Evaluation |

<!-- Slide number: 34 -->

The Definition Trap (Chloe-FDV)
Quality Impact on existing QTAS (Bug Ticket)
Defect:  Wrong "Favorites" List Displayed / Index Shift (Ticket #50435)
Why Failed?
The Designer wrote logic to process an enum, but was unaware that the enum definition itself was missing a required Macro for the new model.
The Designer focused on the processing flow (.c) and assumed the enum list was complete, failing to cross-check the Definition File (.h) where the value was actually excluded.
Logic-Tracer Solution:
The tool validates that every enum value used in the Logic is actually Defined and Active (Macro check) in the Target Model's definition list.

<!-- Slide number: 35 -->

System Logic Validation

![A screenshot of a computer AI-generated content may be incorrect.](Picture41.jpg)
1
Main Feature: Upload the file and it will judge for you

1. Upload the CLCheck File after path retrieval
2
2. Click the red button

3. If it is safe, then ‘Necessity of Evaluation’ column will be filled with ‘N (No need)’, if not, then it will be filled with ‘Y’ with remarks filled in according to the risk message
3