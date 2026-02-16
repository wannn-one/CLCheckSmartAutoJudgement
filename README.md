# CLCheck Smart Auto Judgement

## Table of Contents

- [Problem Background](#problem-background)
- [Key Features](#key-features)
- [Prequisites](#prequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Troubleshooting](#troubleshooting)

## Problem Background

CLCheck is a code verification process performed prior to development or implementation. It involves checking the base model stream and the main stream preceding the target model. This process allows us to guarantee consistency (Follows the proven structure of Base/Prev. Model) and stability (Fewer unintended bugs)

The background of this project comes from a recurring quality issue. Even though we perform a CLCheck process, we still found **5 Bug Tickets (QTAS)** related to CLCheck. Doing CLCheck is Time Consuming… It can take about 4 - 20 hrs to perform!

So, the big question is: 

**Checks Performed + Time Consuming → Why do Quality Issues Persist?**

For complete details, please refer to the [CLCheck Smart Auto Judgement Presentation](https://docs.google.com/presentation/d/1I4yGyIBSaPX_9GuGddMnIEqhRb79oVyf/edit?usp=sharing&ouid=116182938001219593981&rtpof=true&sd=true). 

Please download the document for a better reading experience.

## Key Features

- **Seamless Perforce Integration**: Automatically pulls file content (`p4 print`) based on Target CL and previous revisions without manual checkout.

- **Smart Logic Detection**: 

    - **Enum, Array, List Check**: Able to detect the insertion or deletion of items in the middle of a list.

    - **Non-functional Check (Comments, Whitespace, Tabs)**: Able to identify non-functional changes (such as comments) that have zero impact on the code logic.

    - **Report Generation**: Able to generate reports containing "Necessity of Evaluation," "Implementation or Not," and "Reason.

- **Modern GUI**: User-friendly interface based on `CustomTkinter`

## Prequisites

Before running the application, ensure your computer has:

1. **Python 3.12** or newer
2. **Perforce (P4) CLI Client** installed and added to system PATH enviroment variable
3. **P4 Login Access**: You mus perform a `p4 login` in the terimnal / P4V before running the tool

## Installation

Later

## Usage



## Project Structure

The project uses a clean MVC (Model-View-Controller) architecture for easy maintenance:

```
CLCheckSmartAutoJudgement/
├── main.py                     # Application Entry point
├── requirements.txt            # Dependency list
├── config/
│   └── settings.py             # Configuration (Colors, Regex, Ignore List)
├── core/                       # Core Logic & Drivers
│   ├── p4_connector.py         # Driver for P4 CLI communication
│   ├── logic_evaluator.py      # Checking Algorithm (Checksheet Logic)
│   └── excel_processor.py      # I/O Excel Handler (Pandas)
└── src/                        # Application Architecture
    ├── model/
        └── model.py                # Business Logic Orchestrator
    ├── view/
        └── view.py                 # UI Code (CustomTkinter)
    └── controller/
        └── controller.py           # Bridge between UI and Logic + Threading
```

## Troubleshooting

- Error: P4 CLI not reachable!
    - Ensure p4 can be run from the Command Prompt (CMD). Add the Perforce installation folder to Windows Environment Variables.
    
- Error: Session Expired
    - Open P4V, login with your APO

## Author
**Ikhwanul Abiyu D. - iei25110002**
<br>
F/W Design Department - GUI