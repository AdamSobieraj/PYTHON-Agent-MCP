<!-- Page 1 -->

ISO 20022

# Introduction to ISO 20022 – Universal financial industry message scheme

---

<!-- Page 2 -->

# Agenda

- ISO 20022:
  - The value proposition
  - The standard
  - The actors
  - The registration process
  - The repository
- ISO 20022 registration platform
- Interoperability within the financial industry

---

<!-- Page 3 -->

# The ISO 20022 value proposition (1/5)

**Objective**
To enable communication interoperability between financial institutions , their market infrastructures and their end-user communities

**Major obstacle**
Numerous overlapping standardization initiatives looking at XML financial messages:
MDL, FIX, FinXML, VRXML, RIXML, XBRL, FpML, IFX, TWIST,
RosettaNet, OAGi, ACORD, etc.

---

<!-- Page 4 -->

# The ISO 20022 value proposition
(2/5)

## Proposed solution

A single standardisation approach (methodology, process, repository) to be used by all financial standards initiatives

# ISO 20022

---

<!-- Page 5 -->

# ... (partial text at top)
## (3/5)

**Convergence** into ONE standard is the long term objective...

[Image: Electrical socket] [Image: Prohibited plug symbol]

... but in the interim several standards need to **coexist** to enable quick response to competitive pressures and regulatory demands

---

<!-- Page 6 -->

# The ISO 20022 value proposition (4/5)

## Growth adds exponential complexity and expense...

| Left | Right |
|---|---|
| EDIFACT | RosettaNet |
| IFX | SWIFT |
| OAGi | Proprietary format |
| TWIST | |

**42 interfaces = n * (n-1)**

**Without common building blocks:**
- Point-to-point connection
- Data is mapped directly from one application to another
- Costly, unsalable and difficult to implement and maintain
- Process, routing, rules logic needs to be coded to specific message types

---

<!-- Page 7 -->

# The ISO 20022 Value proposition (5/5)

Standardized implementation reduces cost, time to effect change and improves overall performance...

**EDIFACT** **RosettaNet**

**IFX** **SWIFT**

**Canonical Message Model (i.e. ISO 20022)**

**OAGi** **Proprietary format**

**TWIST**

14 interfaces = n * 2

**Canonical message model** =
- True process integration
- Reduced brittleness, faster to respond to change
- Shared message services – single/shared parser, message independent rules engine, etc.
- Unified monitoring / audit trail

ISO aims at long term **convergence**,

---

<!-- Page 8 -->

# Illustrating business modelling

ISO

Date
Account
Order

All institutions have
their own sets of
data objects

ISO standardizes common
data objects...

Order
Date
Date

...and groups them into 'syntax-
neutral' message models, which...

ASN.1

... can be 'transformed' in
message formats in the
desired syntax

---

<!-- Page 9 -->

# The ISO 20022 Recipe
## Main ingredients (1/2)

- Modelling-based standards development
  - Syntax-independent business standard
  - Validated by the industry
- Syntax-specific design rules for XML and ASN.1
  - Predictable and ‘automatable’
  - Protect standard from technology evolution
- Reverse engineering approach
  - Protect industry investment and ease interoperability
  - Prepare for future migration

---

<!-- Page 10 -->

# The ISO 20022 Recipe
## Main ingredients (2/2)

- Development / registration process
  - Clearly identified activities and roles
  - Business experts and future users involved upfront
  - Technical experts involved when required
- Repository on the ISO 20022 website
  - Business Process Catalogue & Data Dictionary
  - Outside of official standard (maintained by registration bodies)

www.iso20022.org

---

<!-- Page 11 -->

# The eight parts of ISO 20022

| Part 1: Metamodel |
| Part 2: UML profile |
| Part 3: Modelling |
| Part 4: XML schema generation |
| Part 5: Reverse engineering |
| Part 6: Message transport characteristics |
| Part 7: Registration |
| Part 8: ASN.1 generation |
| Copies can be obtained from www.iso.org |

---

<!-- Page 12 -->

# ISO 20022: The actors (1/2)

- Registration Management Group, RMG
  - Approve business justifications for new message standards
  - Approve new member entities
  - Create Standard Evaluation Groups (SEGs)
- Standards Evaluation Groups, SEGs
  - Represent users in specific financial areas
  - Validate new candidate messages and change requests

---

<!-- Page 13 -->

# ISO 20022: The actors (2/2)

- Registration Authority, RA
  - Ensure compliance
  - Maintain and publish ISO 20022 Repository
- Technical Support Group, TSG
  - Assist RMG, SEGs, RA and submitting organisations

---

<!-- Page 14 -->

ISO 20022

## The registration process (1/2)

**RMG monitors**

| Step | Description |
|---|---|
| Submitting organisation | Financial industry group or standards body |
| Business justification | Business justification |
| RMG | Project approval and allocation to a SEG → *Candidate ISO 20022 messages* |
| Submitting organisation & RA | Development and provisional registration |
| SEG | Business validation |
| RA | Official registration and publication → *ISO 20022 messages* |
| Submitting organisation & users | Optional pilot testing or first implementers |

---

<!-- Page 15 -->

# Yearly maintenance process

| Timing | Step | Description |
|---|---|---|
| **By June 1** | Users CRs | Users introduce Change Requests to the RA |
| By July 7 | SEG | SEG screens Change Requests (CRs) |
| By August 21 | Submitting organisation | Submitting organisation prepares 'Maintenance Change Request' with each CR implementation |
| By October 1 | SEG | SEG approval/rejection |
| By December 1 | Submitting organisation & RA | Development of candidate new versions<br>Provisional publication |
| By February 1 | SEG | Validation of new versions |
| **By February - May** | RA | Registration and publication |

---

<!-- Page 16 -->

# Repository

- Data Dictionary
  - Business Concepts
  - Message Concepts
  - Data Types
- Business Process Catalogue
  - Financial business process models
  - Financial business transactions, including messages
  - XML or ASN.1 message schemas

---

<!-- Page 17 -->

# Using ISO 20022 Modeling to teach interoperability

ISO

Date
Account
Order
Date

All institutions have their own sets of data objects

ISO standardizes common data objects...

...and groups them into 'syntax-neutral' message models, which...

... can be 'transformed' in message formats in the desired syntax

XML

---

<!-- Page 18 -->

# ISO 20022 compliance at network level

**ISO**

| Component | Label |
|---|---|
| ISO 20022 Dictionary | |
| ISO 20022 message models | |
| physical message representation | |

**Repository**
- Dictionary
- Catalogue

**Card payments**

**Payments clearing & settlement**

**ISO 20022 ASN.1 syntax**

**ISO 20022 XML syntax**

---

<!-- Page 19 -->

# ISO 20022 compliance at model level

**ISO**

| | |
|---|---|
| **ISO 20022 Dictionary** | Repository / Dictionary / Catalogue |
| **ISO 20022 message models** | **ISO 20022 compliant** |
| **physical message representation** | Card payments → Payments settlement |
| | other syntax → ISO 20022 syntax |
| ISO 20022 compliant using a domain specific syntax | ISO 20022 compliant |

**ISO 20022 Dictionary**

**ISO 20022 message models**

**physical message representation**

Repository
Dictionary
Catalogue

**ISO 20022 compliant**

**Card payments**

**Payments settlement**

other syntax

**ISO 20022 syntax**

ISO 20022 compliant using a domain specific syntax

ISO 20022 compliant

---

<!-- Page 20 -->

# Interoperability in the customer to-bank payment domain

IFX format
Bank A

Proprietary format
Bank B

Customer A

SWIFT
MT 101
Bank C

Let us look at a concrete example from payments area:

---

<!-- Page 21 -->

# customer-to-bank payment domain

Customer A
IFX format

Customer B
Proprietary format

Customer C
SWIFT
MT 101

Bank A

---

<!-- Page 22 -->

bank payment domain

**ISO 2022 Core Payment Kernel model**

- Proprietary
- TWIST
- OAGi
- SWIFT MT
- IFX

The reverse engineering produces a canonical ISO 2022

---

<!-- Page 23 -->

# Interoperability in the customer to bank payment domain

ISO

Core Payment Kernel
IFX
MT 101
ISO 20022
MT 101
IFX
Core Payment Kernel

Adopting ISO 20022 facilitates convergence and co-existence

---

<!-- Page 24 -->

Additional information available from
[www.iso20022.org](www.iso20022.org)