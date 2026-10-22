<!-- Page 1 -->

This Cross-Border Payment Reporting plus (CBPR+) User Handbook is intended to document and explain a variety of ISO 20222 payment related topics, as well as provide practical use cases to ensure a common understanding and adoption of ISO 20222 within the payment industry.
The SWIFT FINplus service will support CBPR+ messages on the SWIFT network traditionally associated with correspondent banking (many-to-many). These messages may be exchanged either between Agents in the same country or between Agents in

The use cases focus on a core topics where other relevant messages may also be referred to within the use case, it may also be necessary to consider other documented use cases, in order to capture a wider variation of scenarios.

**Note:**

This document jointly developed with the CBPR+ group continues to evolve online with the **Standards Release** as:

* CBPR+ continue to develop market practice guidelines for additional message.
* Inaccuracies are identified and corrected.
* Further use cases and/or explanation needs are identified

---

<!-- Page 2 -->

| Page 2 | Updated – note |
| :--- | :--- |
| Page 5 | Updated – new messages added to index |
| Page 6 | Updated – new messages added to index |
| Page 11 | Updated – correction of Intermediary code |
| Page 33 | Updated – new messages and Usage Ids added |
| Page 40 | Updated – new pain message added to index |
| Page 45 | Updated – recognition of Payment Initiation relay rulebook |
| Page 107 | Updated – recognition of Payment Initiation relay rulebook |
| Page 122 | Updated – additional use cases in the index |
| Page 126 | New – use case |
| Page 134 | New – use case |
| Page 135-182 | New – pain.008 message section |
| Page 184 | Update – new messages added to index |
| Page 204 | Update – removed refer to Wait For Settlement Market Practice |
| Page 351 | New – new high level message flow |
| Page 371 | Updated – new messages added to index |
| Page 379-380 | New – pacs.003 use cases |
| Page 400 | Updated – additional guidance on ultimate parties on the return |
| Page 423 | Updated – correct to Agent description in Step 7 |
| Page 458-488 | New – pacs.010 Margin Collection section |
| Page 489-529 | New – pacs.003 Customer Direct Debit section |
| Page 530 | Updated – new message added to index |
| Page 674 | Updated – removed reference to SR 2023 |
| Page 682 | Updated – moved reference to multiple notification, now at an *Item* level |
| Page 691 | Updated – reference to multiple notification item Rule |
| Page 698-716 | New – camt.058 Notice to Received Cancellation section |
| Page 743 | Updated - new message added to index |
| Page 764 | Updated - use case id correction |
| Page 774-795 | New – Customer Cancellation Request section |
| Page 823-839 | New – Cheque message sections |

The following icons dignity changes to slide from the previous iteration.

---

<!-- Page 3 -->

- Message type and direction
- Optional Message type and direction
- Focal Message type and direction
- pacs Debtor
- pacs Creditor
- pacs.008 Ultimate Debtor
- pacs.008 Ultimate Creditor
- Initiating party on behalf of the Debtor
- Agent
- Agent processing legacy format during a coexistence period
- Market Infrastructure
- Exception & Investigation Case Assigner
- Exception & Investigation Case Assignee
- Statement Account Owner
- Statement Account Servicer
- Statement Authorised Party
- Shortcut to other part of document
- Extra attention is needed
- Legacy FIN MT message
- gpi Tracker
- gpi
- Payment Initiation (pain)
- Payment Clearing and Settlement (pacs)
- Cash Management Reporting (camt)
- Cash Management Exception & Investigations (camt)
- Focus message
- Element Hierarchy Path
- Nested Element
- Element Choice
- Nested Element involving a choice
- New slide since last iteration
- Slide updated since last iteration

---

<!-- Page 4 -->

# Table of Contents

1. Introduction to ISO 20222
2. Business Application Header
3. Payment Initiation (pain)
   - pain.001 - Interbank Customer Credit Transfer Initiation
   - pain.002 - Interbank Customer Payment Status Report
   - pain.008 – Customer Direct Debit Initiation `new for SP2023`
4. Payment, Clearing and Settlement (pacs) messages
   - pacs.002 – Financial Institution to Financial Institution Payment Status Report
   - pacs.004 – Payment Return
   - pacs.003 – Financial Institution to Financial Institution Customer Direct Debit `new for SP2023`
   - pacs.008 - Financial Institution to Financial Institution Customer Credit Transfer
   - pacs.009 (core) - Financial Institution Credit Transfer
   - pacs.009 (cov) - Financial Institution 'Cover' Credit Transfer
   - pacs.009 (adv) – Financial Institution 'Advice' Credit Transfer

---

<!-- Page 5 -->

# Table of Contents (continued)

**5. Cash Management Reporting (camt) messages**

*camt.052 - Bank to Customer Account Report*

*camt.053 - Bank to Customer Statement*

*camt.054 - Bank to Customer Debit Credit Notification*

*camt.057 – Notification to Receive*

*camt.058 – Notification to Receive Cancellation Advice* `new for SP2023`

**6. Cash Management Exception & Investigation (camt) messages**

*camt.029 - Resolution of Investigation*

*camt.055 – Customer Payment Cancellation Request* `new for SP2023`

*camt.056 - FI to FI Cancellation Request*

**7. Cheques**

*camt.107 – Cheque Presentment Notification* `new for SP2023`

*camt.108 – Cheque Cancellation or Stop Notification* `new for SP2023`

*camt.109 – Cheque Cancellation or Stop Report* `new for SP2023`

---

<!-- Page 6 -->

# Introduction to ISO 20022

---

<!-- Page 7 -->

ISO 20022 introduces a
fundamental change to the
traditional language used by the
payments industry for several
decades. It also describes
participants (i.e., parties) to a
business transaction differently
based upon the business domain
(area) being described, in a similar
way you may describe a person as a
colleague, parent or sibling
depending upon the context you
wish to describe them. This section
is designed to capture and explain
some of the differences.

---

<!-- Page 8 -->

# Domains

Payment and Cash Management
Securities
Trade Services
Foreign Exchange
Card Payment

## Message Definitions

| | |
|---|---|
| **acmt** | Account Management |
| **auth** | Authorities |
| **camt** | Cash Management |
| **pacs** | Payment Clearing and Settlement |
| **pain** | Payment Initiation |
| **remt** | Payment Remittance Advice |

# Message Sets

```
Message Sets
  Message Definition
    Domain
```

---
camt.052 Bank to Customer Account Report
camt.053 Bank to Customer Statement
camt.054 Bank to Customer Debit Credit Notification
camt.056 FI to FI Payment Cancellation Request
camt.057 Notification to Receive
---
pacs.002 FI to FI Payment Status Report
pacs.004 Payment Return
pacs.008 FI to FI Customer Credit Transfer
pacs.009 Financial Institution Credit Transfer
---
pain.001 Customer Credit Transfer Initiation
pain.002 Customer Payment Status Report
pain.012 Creditor Payment Activation Request

> **ISO 20022 catalogue messages hierarchically beginning with a Business Domain, contain a various sets of Message Definitions, which in turn contain a variety of Message Sets.**
>
> for example:
>
> - Payment and Cash Management
>   - Payments Clearing and Settlement

---

<!-- Page 9 -->

`4!a . 3!c . 3!n . 2!n`

- 4 → Business area
- 3 → Message identifier/functionality
- 3 → Variant
- 2 → Version

| Example |
|---|
| pacs.008.001.08 |

- pacs → Payments Clearing and Settlement
- 008 → FI To FI Customer Credit Transfer
- 001 → Variant 1
- 08 → Version 8

---

<!-- Page 10 -->

introduced in
ISO 2022
`:AA`
pain format
equivalent

## Payment Initiation (pain)

- **Ultimate Debtor**
- **Forwarding Agent**
- **Debtor**
- **Initiating Party**
- `:50a`

## Payments Clearing & Settlement (pacs)

**Previous Instructing Agents**
`:72:/INS/`

**Reimbursement Agents**
`:53a` `:54a` `:55a`

**Intermediary Agents**
`:56a` `:72:/INT/`

**Debtor Agent**
`:52a`

**Instructing Agent**
`Sender`

**Instructed Agent**
`Receiver`

**Creditor Agent**
`:57a`

## Cash Management (camt)

- **Ultimate Creditor**
- **Creditor**
- `:59a`

---

<!-- Page 11 -->

The diagram attempts to explain the construct of an ISO 20022 message sent across the SWIFT network using the **FINplus** service (which is designated to support various ISO 20022 business domains on SWIFT Interact)

Within the CBPR+ User Handbook the predominant focus is on the **Request Payload**, as this is where the business information is contained. However, it is worth noting that a network provider will have additional containers around the Request Payload to perform functionality on its network. This diagram presents the additional containers on the SWIFT network such as the Request Header often referred to as the Technical Header of the message.

| Diagram Structure | Annotation |
| :--- | :--- |
| **Exchange Request** | |
| &nbsp;&nbsp;&nbsp;&nbsp;**Request** | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**RequestHeader** | SWIFTNet Headers |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**RequestPayload** | Envelope - container for the business message |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Application Header** | The business message comprises the application header and 'business' document |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Document** | |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**MX Message Instance** | The 'business' document contains the MX message instance (or ISO 20022 message instance) |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Crypto** | |

<br>

| Diagram Structure | Annotation |
| :--- | :--- |
| `<AppHdr> ... </AppHdr>` | ISO 20022 Business Application Header |
| `<Document> ...` | ISO 20022 Message |
| *(Combined Block)* | **Business Message** |

---

<!-- Page 12 -->

## XML Elements

An XML instance or document contains data in elements and nested elements (elements which contain other elements) corresponding to the hierarchy imposed by the XML schema. In the CBPR+ Usage Guidelines we often refer to the element hierarchy by levels (to understand the nested relationship) whereby a Level 2 element effectively is a sub-element or child of another element. For example in a pacs.008 Customer Credit Transfer the *Interbank Settlement Date* is a sub-element (Level 2) of the *Credit Transfer Transaction Information* element (Level 1).

| Credit Transfer Transaction Information | Interbank Settlement Amount |
|---|---|
| | Interbank Settlement Date |

## Naming conventions

An XML element is named according to the following rules:

- The name can contain letters, numbers, and other characters, but must not start with a number or punctuation mark.
- The name must not start with XML, xml, or Xml.
- The name must not contain any spaces.

## MX naming conventions

There are some generic naming rules that apply to most items in the database.

- The names of all items in the database use the upper CamelCase convention, as follows:
  - Each word starts with a capital letter.
  - There are no white spaces between words.
- A name may be made up of multiple words, each consisting of alphanumeric characters.
- Words use British English vocabulary.
- All names must start with an alphabetic character.
- All characters that follow the first characters must be letters or numbers.

| Min | Max | Element Multiplicity |
|---|---|---|
| 1 | 1 | Required element |
| 0 | 1 | Optional element |
| 0 | * | Unlimited element occurences |

## Example of a Street Name element: `<StrNm>Oxford Street</StrNm>`

## MX message element multiplicity (occurences)

---

<!-- Page 13 -->

## Empty XML Elements

An empty XML element is an element that contains no data content and therefore is described as empty. Although this makes little business sense, this is a known feature of XML. It typically only occurs where a nested element beneath a parent element allows for various element options but does not either enforce the use of an element with a minimum of 1 occurrence or does not have a rule defining the presence of at this one of the nested element.

A common example of this is in payment message is Financial Institution.

| Element |  |  |
|---|---|---|
| v ◉ **Financial Institution Identification** | 1 | 1 |
| &nbsp;&nbsp;&nbsp;&nbsp;> ◉ **BICFI** | 0 | 1 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;> ◉ Clearing System Member Identification | 0 | 1 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;◉ LEI | 0 | 1 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;◉ Name | 0 | 1 |
| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;> ◉ Postal Address | 0 | 1 |

Whereby technically it is possible to provide just Financial Institution without BICFI, or Name and Postal Address as an example i.e., <FinInstId></FinInstId>

In the **FINPlus** service Message Validation (Mval) will validate the messages to ensure empty XML elements are not provided, i.e., ensure where business data should be provided within a nested element, it is provided.

---

<!-- Page 14 -->

MyStandards describes the element's context by its path whereby each element is divided by a forward slash (/). For example the pacs.008 Town Name within the Debtor Postal Address is described as /Document/FIToFICstmrCdtTrf/CdtTrfTxInf/Dbtr/PstlAdr/TwnNm

Within the CBPR+ a similar Path principal is often used to visualize an element being explained, where the name is expanded rather than describing the element in an XML naming convention.

For example to describe the pacs.008 Payment Identification, the following is displayed on the bottom right hand side of the page to explain Payment Identification is an element below Credit Transfer Transaction Information.

Credit Transfer Transaction Info > Payment Identification

In this way the CBPR+ User Hand Book uses three main icon to explain the relationships between element, by display the icon after the element name.

- To visualise an element which has nested elements beneath it
- To visualise an element which has a choice associated with it i.e., a Code where a choice of which code can be determined
- To visualise an element which is nested and has a choice associated with it. For example, an Identification where a choice must be made between an Organisation Identification and a Private Identification element which is nested, but where both cannot be used together.

---

<!-- Page 15 -->

# CBPR+

Cross-border Payments and Reporting Plus (CBPR+) specifications define how ISO 20022 is used for cross-border payments and cash reporting on the Swift network. Conformance to CBPR+ specifications will be validated by Swift messaging services and therefore, as it is imperative that users implement the specifications correctly. The resources available on this page aim to help Swift's community to understand and implement CBPR+ specifications.

Learn more about ISO 20022 Readiness >

CBPR+ Usage Guidelines and Readiness Portal | CBPR+ Translation Portal

## Additional resources

Find out how ISO 20022 is used for cross-border payments and cash reporting on the Swift network.

## Document centre

| | | |
| :--- | :--- | :--- |
| **CBPR+ user handbook**<br>Explains how CBPR+ usage Guidelines support common business scenarios in cross-border payment and reporting processes.<br>Download > | **Data integrity market practice guidance**<br>This document describes market practice to report consistent or missing payment information using the MT messaging standard.<br>Download > | **CBPR+ and HVPS+ alignment**<br>Lists the similarities and differences between the two market practice sets.<br>Download > |
| **Derived data mapping guidance**<br>Provides guidance on how to populate information from one messaging standard to the other enhanced message.<br>Download > | **MT / MX equivalence table**<br>Documents the CBPR+ usage Guidelines supported on Swift select MT/IX service in comparison with the equivalent MT message.<br>Download > | **Lessons learnt since go-live**<br>This document intends to provide guidance to the community regarding observations that may be described before or after the migration.<br>Download > |
| **Samples library**<br>**CBPR+ sample messages**<br>Sample messages with to test the use cases described in the CBPR+ user Handbook.<br>Learn more > | **In-flow translation service sample messages**<br>Sample test messages for the in-flow translation service.<br>Learn more > | |

https://www2.swift.com/mystandards/#/c/cbpr/landing

---

<!-- Page 16 -->

Cross Border Payments and Reporting Plus

PUBLISHED | MyStandards

CBPR+

CBPRPlus-pacs.008.001.08_FIToFICustomerCreditTransfer 🔒

CBPRPlus_ISO 20022 Portfolio, November 2022, Release 2.0 [ Technical version: 1 , Version: V2.0 FOR IMPLEMENTATION , Format: MX , Status: Final ]

**Usage identifier:** swift.cbprplus.01 **Version:** V2.0 FOR IMPLEMENTATION **Status:** Final

Content | Result View | History | Sample Messages

☐ Show raw tags

Many of the CBPRPlus Usage Guidelines have useful key principals and additional information. These can be expanded in MyStandards by clicking on 'show details' in the middle of the Usage Guideline description pane.

**Show details**

| | Cross Border Payments and Reporting Plus (CBPR+) | Function |
|---|---|---|
| Technical version | 1 | |
| Version | V2.0 FOR IMPLEMENTATION | |
| Status | Final | |
| Standard | pacs.008.001.08 | |
| Format | MX | |
| Usage identifier | swift.cbprplus.01 | |
| Download | For direct download | For PDF generation |
| Description | | |
| Description | Usage: | |

Hide details

IA. AGENTS IDENTIFICATION RECOMMENDATION

- If BIC is present, then (Name & Postal Address) is NOT allowed (ClearingSystemMemberIdentification and LEI may complement) - However, in case of conflicting information, the BIC will always take precedence
- If BIC is absent, (Name & Postal Address) or ClearingSystemMemberIdentification must be present and both are allowed together.

Note: "Instructing financial agent" must be identified with a BIC - Clearing system members identification and LEI are optional

IB. DESTINATION - PARTY IDENTIFICATION RECOMMENDATION

- If BIC is present, then (Name and Postal Address) is NOT allowed (other elements remain optional) - However, in case of conflicting information, BIC will always take precedence.

---

<!-- Page 17 -->

Traditionally in the Legacy FIN standard rules related to a message were described as either ***Network Validation Rules*** – those validated by the network, or ***Usage rules*** – rules not validated by the network. FIN also has the concept of ***Usage Guidelines*** – guideline to recommend a best practice.

In ISO 20022 there are similar rules (described in a different way) within a baseline message, and potentially within a dedicated Usage Guideline (e.g. CBPR plus)

Within CBPR+ Usage Guideline specification the rules dedicate to CBPR+ are often described as:

**Formal Rules** which are validated on the network, these are identified by the word **Rule** appended to the rule description. For example: ⚠️ ***Rule "CBPR_Party_Name_Any_BIC_FormalRule"***

**Textual Rules** which are not validated on the network, these are identified by with the word **TextualRule** appended to the rule description. For example: ⚠️ ***Rule "CBPR_Agent_Option_1_TextualRule"***

**Guideline Rules** which provide recommended best practice, these are identified by the word **Guideline** appended to the rule description. For example: ⚠️ ***Rule "CBPR_Purpose_Guideline"***

Rules inherited from the baseline message and validated on the SWIFT network are referred to in the Usage Guidelines as a **CrossElementSimpleRule** and a **CrossElementComplexRule**

---

<!-- Page 18 -->

`<Short issuer organisation>.<Business context>[.<Business context>] n times.<version>`
`1-10 chars`   `1 char`   `1-10 chars`   `1 char`   `1-10 chars`   `1 char`   `2 chars`
**A**           **B**           **C, D,...**          **E**
`Total max 35 char`

- Type: **String**
- Max allowed size: **35 characters**
- Structure:
    - Must contain minimum **A** & **B**, optionally followed by **1 or more additional business context elements (C, D, ...)**.
    - Always **ends with version element E** (format "nn", e.g., "01")
    - Each element is separated by a period "."
    - Length of **each text element can vary up to max 10 characters**. Total length, including periods, cannot exceed 35 chars.
    - Consistency enforced by lightweight SWIFT review/registration: E.g., "ecb" to represent the ECB, not "eucb"
    - **Lowercase** alphanumerical characters only

In CBPR+ the Usage Identifier is captured *within the Business Application Header, Business Service element*. More detail can be found in the dedicated Business Application Header chapter of this document.

---

<!-- Page 19 -->

Many ISO 20022 message use data elements represented by codes. Such codes are often externalised from the message itself, enabling maintenance of the code list on a quarterly basis without requiring a new message version.
Some data element may also be embedded in the message.

example of Charge Bearer in pacs.008 v8
which uses embedded codes

```
v >= Charge Bearer                                1  1
    + Borne By Debtor [DEBT]
    + Borne By Creditor [CRED]
    >= Shared [SHAR]
    + Following Service Level [SLEV]
```

example of Return Reason Information in
pacs.004 v9 which uses externalised codes

```
v v Return Reason Information                     0  *
    > 0 Originator                                0  1
    v >= Reason                                   0  1
        >= Code                                   1  1
            o Proprietary                         1  1
```

**Type**
ExternalReturnReasonCode (based on string)
- min.length: 1
- max.length: 4

**Definition**
Reason for the return, as an external reason code

| ExternalReturnReasonCode | ST01 | InvalidA... |
| :--- | :--- | :--- |
| ExternalReturnReasonCode | ST02 | ChqRejecte... |
| ExternalReturnReasonCode | EX01 | ChqAmount... |
| ExternalReturnReasonCode | EX03 | BalanceNot... |
| ExternalReturnReasonCode | EX05 | DeferralNot... |
| ExternalReturnReasonCode | EML1 | EMVUability... |
| ExternalReturnReasonCode | ERN1 | ERNCodeNot... |
| ExternalReturnReasonCode | PF02 | InvalidAuth... |
| ExternalReturnReasonCode | FOCB | FallbackCar... |

Proprietary Codes may also be available for certain data elements.
These are typically inherited from legacy formats and require
definitions in user documentation as these are not captured in the
baseline ISO 20022 standards

---

<!-- Page 20 -->

| All SWIFT ISO MX message elements (fields) which are defined (by data Type) as text are restricted to FIN X Characters: <br><br> **a-z A-Z 0-9 - ? : ( ) , . ' + .** | Special characters are additionally allowed in: <br>• All party (agents and non-agents) Name and Address elements. <br>• The Related Remittance Information element <br>• The Remittance Information (structured & unstructured) element <br>• The Email Address where included as part of a Proxy elements <br>• City of Birth and Province of Birth elements nested in Private Identification <br><br> List of special characters: | Currencies in the payments should be expressed in ISO Currency Codes only (3-Characters, e.g. EUR) | Translation of any special character: <br> **#&%*="^_{}[]$><** <br> into MT messages will be represented by a . (**Full Stop**) <br><br> $ ! \ % <br> < # ] * <br> > & [ = |

---

<!-- Page 21 -->

**Point-to-point** refers to data passed within a message from one party to the next. This data will not necessarily be passed in subsequent messages.

> For example: the *Instruction Identification* element contains a reference meaningful to the party sending a message, subsequent messages in a payment transaction chain can expect the *Instruction Identification* to be replaced by a reference meaningful to the party sending that message leg.

**End-to-end** refers to data passed throughout the transaction life cycle i.e. within a message from one party to the next and continued in subsequent messages.

> For example: the *UETR* element contains a Unique End-to-end Transaction Reference in accordance with the UUID version 4 standards. This same reference is used in all messages related to the payment transaction.

---

<!-- Page 22 -->

ISO 20022 messages have a number of elements associated with Agents which allow for these Agents to be referenced by a variety of Financial Institution identifiers.
More commonly the ISO 9362 Financial Institution BIC (*BICF*) is considered the best practice de facto standard for 'many to many' / correspondent banking payments. However other options include:
*Clearing System Member Identifiers* when accompanied with the *Clearing System Identification*.
*LEI* (Legal Entity Identifier)
*Name* and either structured or unstructured *Postal Address*.

| Financial Institution Identification |
|---|
| BICFI |
| Clearing System Member Id → Clearing System Id |
| LEI |
| Name |

Back to previous page

---

<!-- Page 23 -->

Two common elements to ISO 20022 messages are *Date* and *DateTime*.

CBPR+ usage guidelines *DateTime* elements mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
> For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)
note - milliseconds are optional.

The ISO 20022 *Date* elements allow the date to include an offset. As a data model, shared by other business domains, an offset date can provide great business clarity, such as something expiring at the end of a business date. However, in payments such a date offset provides little business value, whereby should an offset be include with the date, this offset should be ignored.

---

<!-- Page 24 -->

| Country | Code Name | MT Clearing System code | ISO 20022 Clearing System Identification |
| :--- | :--- | :---: | :---: |
| **Australia** | Australian Bank State Branch Code (BSB) | AU | AUBSB |
| **Austria** | Austrian Bankleitzahl | AT | ATBLZ |
| **Canada** | Canadian Payments Association Payment Routing Number | CC | CAPCA |
| **China** | Bank Branch Code used in China | CN | CNAPS |
| **Germany** | German Bankleitzahl | BL | DEBLZ |
| **Greece** | Hellenic Bank Identification Code | GR | GRBIC |
| **Hong Kong** | Hong Kong Bank Code | HK | HKNCC |
| **India** | Indian Financial System Code | IN | INFSC |
| **Ireland** | Irish National Clearing Code | IE | IENCC |
| **Italy** | Italian Domestic Identification Code | IT | ITNCC |
| **Japan** | Japan Zengin Clearing Code | JP | JPZGN |
| **New Zealand** | New Zealand National Clearing Code | NZ | NZNCC |
| **Poland** | Polish National Clearing Code | PL | PLKNR |
| **Portugal** | Portuguese National Clearing Code | PT | PTNCC |
| **Russia** | Russian Central Bank Identification Code | RU | RUCBC |
| **South Africa** | South African National Clearing Code | ZA | ZANCC |
| **Spain** | Spanish Domestic Interbanking Code | ES | ESNCC |
| **Switzerland** | Swiss Clearing Code (BC Code) | SW | CHBCC |
| **Switzerland** | Swiss Clearing Code (SIG Code) | SW | CHSIG |
| **Taiwan** | Financial Institution Code | TW | TWNCC |
| **UK** | UK Domestic Sort Code | GB | GBBSB |

For translation rules and comparison purposes this table provides a list of published MT National Clearing System codes against their equivalent ISO 20022 Clearing System Identification in the external code list.

---

<!-- Page 25 -->

# Business Application Header

---

<!-- Page 26 -->

Min 0 – Max 1

The head.001 Business Application Header **Character Set** element declares the character set, in addition to Latin, that is contained in the Business Document e.g. the pacs.008.

| | |
|---|---|
| Ж œ | The **Character Set** element uses the UnicodeChartsCode string to declare an additional character set, for example **Cyrillic** (Unicode range: 0400-04FF). |
| 图 ب | This allows the party for which the message is addressed *To* to know in advance the additional character set contained within the Business Document. In this way the message can be routed to a specific application to process the Character Set or handled as an exception if the Character Set is not appropriate for that business transaction. |

🔍 Extending character sets is not intended in CBPR+ from the initial implementation of the service. This element is intended for use once extended character sets are implemented, whereby the string represented in this element can enable any necessary network validations, such as a closed user group for that character set.

---

<!-- Page 27 -->

Min 1 – Max 1

The head.001 Business Application Header **_From_** element identifies the BIC of the party who created the Business Document (e.g. pacs.008). Additional optional information on this party may also be captured within this nested element, where the BIC takes precedence should the information be inconsistent with the BIC.

A choice must be made for the BIC depending on the party it represents.
**_Financial Institution Identification_** which identifies a Financial Institution, and may be further complemented with
*   **_Clearing System Member Identification_**
*   **_LEI_**
as an additional identification.

From
Organisation Identifier

---

<!-- Page 28 -->

Min 1 – Max 1

The head.001 Business Application Header *To* element identifies the BIC of the party who will ultimately process the Business Document (e.g. pacs.008) Additional optional information on this party may also be captured within this nested element, where the BIC takes precedence should the information be inconsistent with the BIC.

A choice must be made for the BIC depending on the party it represents.
***Financial Institution Identification*** which identifies a Financial Institution, and may be further complemented with
* ***Clearing System Member Identification***
* ***LEI***
as an additional identification.

To
Organisation Identifier

---

<!-- Page 29 -->

Min 1 – Max 1
The head.001 Business Application Header **Business Message Identifier** element contains the *Message Identification* captured within the Business Document's Group Header. The content of this element should match the Business Document to avoid incorrect routing by the recipient.

**Business Application Header**
Business Message Identifier | 1A245878..

**Business Document**
Group Header
Message Identification | 1A245878..

---

<!-- Page 30 -->

Min 1 – Max 1

The head.001 Business Application Header ***Message Definition Identifier*** element contains the name of the Business Document. The content of this element should match the Business Document to avoid incorrect routing by the recipient.

**Business Application Header**

| Message Definition Identifier | pacs.009.001.08 |
|---|---|

**Business Document**

| `<Document "pacs.009.001.08">` |
|---|
| Group Header |

---

<!-- Page 31 -->

Min 1 – Max 1

The head.001 Business Application Header **Business Service** element is used to identify administered services on the SWIFT network. The data represented in this elements is referred to as a *Usage Identifier*. For CBPR+ examples are provided below, these values may be used together with the *Message Definition Identifier* to determine routing rules to specific applications without having to open the business document.

| **Message Definition Identifier** | **Business Service** | **Business Use Case** |
| :--- | :--- | :--- |
| pacs.009.001.08 | *swift.cbprplus.cov.01* | Financial Institution (Cover) Credit Transfer |
| pacs.009.001.08 | *swift.cbprplus.01* | Serial Financial Institution Credit Transfer |
| pacs.008.001.08 | *swift.cbprplus.stp.01* | STP Customer Credit Transfer |

The **Business Service** is also intended to be incremented for the same message version, when an updated Usage Guideline is released. For example a new restriction is applied to the pacs.009.001.08 Usage Guideline, the **Business Service** swift.cbprplus.cov.02 and swift.cbprplus.02 will be used to reflect these new Guidelines and allow network validate.

**Note:** when a new message (Message Definition Identifier) version is introduced the numeric value for the

---

<!-- Page 32 -->

| Message Definition Identifier | Business Service |
|---|---|
| pain.001.001.09 | sw.ifc.cbprplus.02 |
| pain.002.001.10 | sw.ifc.cbprplus.02 |
| pain.008.001.03 | sw.ifc.cbprplus.01 |
| pacs.002.001.10 | sw.ifc.cbprplus.02 |
| pacs.003.001.08 | sw.ifc.cbprplus.01 |
| pacs.004.001.09 | sw.ifc.cbprplus.02 |
| pacs.008.001.08 | sw.ifc.cbprplus.02 |
| pacs.008.001.08 (STP/STP EU) | sw.ifc.cbprplus.stp.02 |
| pacs.009.001.08 (advice) | sw.ifc.cbprplus.02 |
| pacs.009.001.08 (core) | sw.ifc.cbprplus.02 |
| pacs.009.001.08 (cov) | sw.ifc.cbprplus.cov.02 |
| pacs.010.001.03 | sw.ifc.cbprplus.02 |
| pacs.010.001.03 (Margin Collection) | sw.ifc.cbprplus.col.01 |
| camt.029.001.09 | sw.ifc.cbprplus.02 |
| camt.052.001.08 | sw.ifc.cbprplus.02 |
| camt.053.001.08 | sw.ifc.cbprplus.02 |
| camt.054.001.08 | sw.ifc.cbprplus.02 |
| camt.055.001.08 | sw.ifc.cbprplus.01 |
| camt.056.001.08 | sw.ifc.cbprplus.02 |

| Message Definition Identifier | Business Service |
|---|---|
| camt.058.001.08 | sw.ifc.cbprplus.01 |
| camt.060.001.05 | sw.ifc.cbprplus.02 |
| camt.107.001.01 | sw.ifc.cbprplus.01 |
| camt.108.001.01 | sw.ifc.cbprplus.01 |
| camt.109.001.01 | sw.ifc.cbprplus.01 |

The data represented in the Business Service, together with the Message Definition Identifier has a number of roles, in addition to the routing rules referred to on the previous page.

This data value:

- Identifiers explicitly the Usage Guideline within a library of guideline. For example an application may have various pacs.008 libraries within a collection, for which only one of these is appropriate to be used to identify data requirements or perform validation.
- is also populated in the Request Header of the InterAct message in the **Request Sub Type** element which allow the service (F/Nplus for CBPR++) to apply network validation rules.

---

<!-- Page 33 -->

Min 0 – Max 1

The head.001 Business Application Header **_Market Practice_** element is used to identify administered services on the SWIFT network.

This element is currently not foreseen to be used by CBPR+.

---

<!-- Page 34 -->

Min 1 – Max 1

The head.001 Business Application Header *Creation Date* captures the date and time which the Business Application Header was created.

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset `YYYY-MM-DDThh:mm:ss.sss+-hh:mm`
> For example: `2002-10-10T12:00:00-05:00` (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- Page 35 -->

Min 0 – Max 1

The head.001 Business Application Header *Copy Duplicate* indicator is used as a choice to identify scenarios where a message was previously sent.

**COPY** is used to represent a copy of a message being sent to an additional party. This scenario is only associated with camt reporting messages.

**DUPL** is used to represent a duplicate of a previously sent camt reporting message. To receive a duplicate payment message, Interact message retrieval should be utilised.

**CODU** is used to represent a duplicate of a previously sent **COPY** message. This scenario is only associated with camt reporting messages.

---

<!-- Page 36 -->

Min 0 – Max 1
The head.001 Business Application Header ***Possible Duplicate*** element is used as a flag to indicate that if the party who will ultimately process the Business Document (e.g. pacs.008) received the original, then it should perform necessary actions to avoid processing this Business Message again.

This element is represented by a Yes/No Boolean, whereby **true** represent this is a Possible Duplicate.
It is not necessary to represent **false** (No) the absence of this optional element itself indicates that this is not considered a Possible Duplicate.

The FINplus Technical Header has an element **PDIndicator** (Possible Duplicate Indicator) which uses a Yes/No Boolean. This may be populated by the network interface to identify a message it considers may be a possible duplicate.

---

<!-- Page 37 -->

Min 0 – Max 1

The head.001 Business Application Header **Priority** element allows a choice of Business Message Priority Code to indicate the priority which may be applied to the business message.

This element must represent the priority code of the business document (instance) which is only applicable for pac messages. The pac message priority is captured in the Payment Type Priority/Instruction Priority.

---

<!-- Page 38 -->

Min 0 – Max 1

The head.001 Business Application Header *Related* nested element enables the capture of the Business Application Header from a related Business Document. For example, in a pacs.004 Payment Return the *Related* Business Application Header from the original message can be included. This could allow the receiver to apply specific routing to the message, based on the related information i.e., return of a pacs.009 cov may be routed to different payment engine than a core pacs.009.

The following elements are nested within the Related element. Where used these contain the original data from the related Business Application Header:

- **From** Min 1 – Max 1
- **To** Min 1 – Max 1
- **Business Message Identifier** Min 1 – Max 1
- **Message Definition Identifier** Min 1 – Max 1
- **Business Service** Min 0 – Max 1
- **Creation Date** Min 1 – Max 1
- **Copy Duplicate** Min 0 – Max 1
- **Priority** Min 0 – Max 1

---

<!-- Page 39 -->

[pain.001 - Interbank Customer Credit Transfer initiation](pain.001 - Interbank Customer Credit Transfer initiation)
[pain.002 – Interbank Customer Payment Status Report](pain.002 – Interbank Customer Payment Status Report)
[pain.008 – Customer Direct Debit Initiation](pain.008 – Customer Direct Debit Initiation)

---

<!-- Page 40 -->

# Interbank Customer
# Credit Transfer Initiation

---

<!-- Page 41 -->

ISO 20222 message element $\rightarrow$ MT Field Name & Tag option

**Group Header**
> **Message Identification**
> **Initiating Party** – where different from **Debtor**
> **Forwarding Agent**

**Payment Information**
> **Payment Information Identification**
> **Requested Execution Date**
> **Debtor**
> **Debtor Agent**

**Credit Transfer Transaction Information**
> **Payment Identification**
> **Amount**
> **Charge Bearer**
> **Creditor Agent**
> **Creditor**

**Sequence A** – General Information:
> **Sender’s Reference** (Field 20)
> **Instructing Party** (Field 50 C or L)

Message **Sender** in a ‘relay’ scenario

**Sequence A** – General Information:
> **Customer Specified Reference** (Field 21R)
> **Requested Execution Date** (Field 30)
> **Ordering Customer** (Field 50 F, G or H)*
> **Account Servicing Institution** (Field 52 A or C)*

**Sequence B** – Transaction Details:
> **Transaction Reference** (Field 21)
> **Currency/Transaction Amount** (Field 32D)
> **Details of Charges** (Field 71A)
> **Account With Institution** (Field 57 A, C or D)
> **Beneficiary** (Field 59 no letter, A or F)

---

<!-- Page 42 -->

pain.001

- Group Header
- Payment Information
- Credit Transfer Transaction Information

The pain.001 message is composed of three blocks:

- **Group Header** contains a set of characteristics that relates to all individual transaction.
- **Payment Information** contains a set of characteristics that relates to the debit side of the transaction, such as Debtor and Debtor Agent.
- **Credit Transfer Transaction Information** contains, among others, elements related to the credit side of the transaction, such as Creditor and Creditor Agent.

Payment messages in a many-to-many payment are considered as a single transaction.

---

<!-- Page 43 -->

Debtor
Initiating Party*
Forwarding Agent
Debtor Agent
Creditor Agent
Creditor

pain.001**
FINplus pain.001
pain.002
FINplus pain.002
pacs.008
pacs.002
camt.053

*Initiating Party may alternative represent an authorised party such as a head office
**or other proprietary method for instructing a payment initiation request.

FINplus Customer Credit Transfer Initiation message is sent by the Initiating Party to the Forwarding Agent or the Debtor Agent. It is used to request movement of funds from the debtor account to a creditor. There are three common use cases:
1. *Relay.* The pain.001 message is sent by the Initiating party (the Debtor or authorised party) to the Forwarding Agent which acts as a concentrating financial institution. It will forward the pain.001 message to the Debtor Agent

---

<!-- Page 44 -->

**Diagram Entities and Flows**

*   **Entities:**
    *   Debtor
    *   Initiating Party (FI)
    *   Debtor Agent (A)
    *   Creditor Agent (B)
    *   Creditor

*   **Message Flows:**
    *   `FINplus pain.001` (Initiating Party $\rightarrow$ Debtor Agent)
    *   `FINplus pain.002` (Debtor Agent $\rightarrow$ Initiating Party)
    *   `pacs.008` (Debtor Agent $\rightarrow$ Creditor Agent)
    *   `pacs.002` (Creditor Agent $\rightarrow$ Debtor Agent)
    *   `camt.053` (Creditor Agent $\rightarrow$ Creditor)

**Note**

> This use case may not apply to all Financial Institution, depending on the products and service provided by that Financial Institution to their customer

**Description**

FINplus Customer Credit Transfer Initiation message is sent by the Initiating Party to the Forwarding Agent or the Debtor Agent. It is used to request movement of funds from the debtor account to a creditor. There are three common use cases:

2. **Authorised Party Initiation:** The pain.001 message is sent by the Financial Institution as an Initiating Party to the Debtor Agent to initiate a payment on behalf of the Debtor who is the account holder. For example, a FI Initiates: a liquidity sweep on behalf of a corporate customer or payment from the Debtor account based on Tri-party agreement (agreement from the Debtor with the Debtor

---

<!-- Page 45 -->

Debtor
Initiating Party
Debtor Agent
Creditor Agent
Creditor

Interbank pain.001
Interbank pain.002
pac s.008
pac s.002
pac s.008
pac s.002
camt.053

Interbank Customer Credit Transfer Initiation message is sent by the Initiating Party to the Forwarding Agent or the Debtor Agent. It is used to request movement of funds from the debtor account to a creditor. There are three common use cases:
3. **Financial Institution Payment Initiation** (to non-FI) : The pain.001 message is sent by the Financial Institution as both the Debtor and Initiating Party to initiate a payment from their account with the Debtor Agent to move funds to a non-Financial Institution Creditor

---

<!-- Page 46 -->

The following descriptions are defined in the ISO 20022 Standard for core parties participating in an Interbank Customer Credit Transfer Initiation relationship.

**Forwarding Agent** - "Financial institution that receives the instruction from the initiating party and forwards it to the next agent in the payment chain for execution". Applicable for pain.001 use case 1 only

**Initiating Party** – "Party that initiates the payment." which may be the **Debtor** or a Party acting on behalf of the Debtor e.g., the Agent initiating a liquidity sweep service

**Debtor Agent** - "Financial institution servicing an account for the debtor."

**Creditor Agent** - "Financial institution servicing an account for the creditor."

**Debtor** - "Party that owes an amount of money to the (ultimate) creditor."

**Creditor** - "Party to which an amount of money is due."

---

<!-- Page 47 -->

# Group Header

---

<!-- Page 48 -->

# pain.001 Interbank Customer Credit Transfer Initiation – Message Identification

`Min 1 – Max 1`

Each ISO20222 payment message has a **Message Identification** element, located in the Group Header. This **35 character** identifier is a point-to-point reference used to unambiguously identify the message.

For the Payment Initiation (pain) messages the *Message Identification* has no exact equivalent in the legacy MT payment message. However, the Sender's Reference (Field 20) could be considered as a similar comparison where a pain message contains a single Transaction.

> Each transaction's *Credit Transfer Transaction Information* contains a variety of nested *Payment Identification* elements to capture reference related to the individual transaction such as a UETR (Unique End-to-end Transaction Reference).

> For a relay scenario, Forwarding Agent should respect the Message ID provided by the Initiating Party (Debtor or authorized third party) of the pain.001.

---

<!-- Page 49 -->

# pain.001 Interbank Customer Credit Transfer Initiation – Creation Date Time

`Min 1 = Max 1`

The pain.001 message **Creation Date Time** captures the date and time which the message was created.

It is defined by *ISO Date Time* with mandatory date and time components expressed in the following formats:

1. Universal Time Coordinated (UTC) time **YYYY-MM-DDThh:mm:ss.sssZ**
2. Local time with UTC offset **YYYY-MM-DDThh:mm:ss.sss+/-hh:mm**
3. Local time format **YYYY-MM-DDThh:mm:ss.sss**

Unlike other CBPR+ messages, the interbank pain.001 message is more flexible in defining the date and time elements. The most recommended representation is Local time with UTC offset which was mandated by CBPR+ (2ⁿᵈ option). Otherwise use UTC time (1ˢᵗ option). Decimal fractions of seconds with 3 digits. Milliseconds are optional.

Group Header: Creation Date Time

---

<!-- Page 50 -->

# pain.001 Interbank Customer Credit Transfer Initiation – Authorisation

**Min 0 – Max 2**

The pain.001 message **Authorisation** allows the Initiating Party to specify if a file requires either File Level or Transaction Level approval by additional security provisions, such as digital signature or user key. The *Authorisation* uses an embedded code set or free text form. It has no exact equivalent in the legacy MT payment message, however, the Authorisation (Field 25) could be considered as a similar comparison.

| Code | Description | Description |
| :--- | :--- | :--- |
| ILEV | Instruction Level Authorisation | File requires all customer transactions to be authorised or approved. |
| FDET | File Level Authorisation Details | Additional file level approval, with the ability to view both the payment information block and supporting transaction detail. |
| FSUM | File Level Authorisation Summary | Additional file level approval, with the ability to view only the payment information block. |
| AUTH | Pre Authorised File | File has been pre-authorised or approved within the originating customer environment and no further approval is required. |

For single transactions in the CBPR+ usage guidelines, the most applicable code will be ILEV for Instruction Level Authorisation. The use of Authorisation is only allowed when bilaterally agreed.

---

<!-- Page 51 -->

pain.001 Interbank Customer Credit Transfer Initiation – Number of Transactions

Min 1 – Max 1

The pain.001 message *Number of Transactions* captures the number of individual transaction contained within the message.

🧮 The number of transactions in CBPR+ payment usage guidelines is fixed to 1.

💡 Single transactions in the CBPR+ payment usage guidelines enable a transaction to be managed and unlocks highly automated, frictionless, instant payments, supporting the next generation of innovation.

---

<!-- Page 52 -->

# pain.001 Interbank Customer Credit Transfer Initiation – Initiating Party

Initiating Party
Debtor
Authorised Party
Forwarding Agent / FI

For the second and the third use case, BIC of the Initiating Party is required.

Min 1 – Max 1

The **Initiating Party** can either be the **Debtor** or an Authorised Party who initiates payment transactions on behalf of the *Debtor*. The Initiating Party can be, for example, the Head Office which has the authority to debit the account of its subsidiary. In the centralization model, the *Initiating Party* can also be a payment factory or shared service center or third-party agent, which has authority to send the message on behalf of the *Debtor*.

There are three common use cases in the context of interbank pain.001 message:

1. **Relay:** The *Initiating Party*, which is either the *Debtor* themselves or authorised party, sends the pain.001 message to the **Forwarding Agent** which acts as a concentrating financial institution. It will forward the pain.001 message to the **Debtor Agent**. This is commonly known as a relay scenario. Whereby the Forwarding Agent is performing a technical role in the payment transaction, they would not be represented in the payment, clearing and settlement message.

2. **Authorised Party:** The *Initiating Party* is the **Financial Institution** which has the authority to send the pain.001 message on behalf of the *Debtor*, e.g., multi-bank liquidity sweeps.

3. **Financial Institution Payment Initiation:** The *Initiating Party* is the **Financial Institution** which is the *Debtor* who initiate a payment from their account to move

---

<!-- Page 53 -->

pain.001 Interbank Customer Credit Transfer Initiation – Initiating Party

The *Initiating Party* can either be the **Debtor** or an authorised party, such as Financial Institution, in the context of interbank pain.001. Sub elements describe the *Initiating Party* in greater detail.

Mandatory *Name* where Postal Address is provided.

**Name**

**Postal Address**

**Initiating Party**

Nested element capturing *structured* Postal Address including at least Town Name and Country if used.

- Department
- Sub Department
- Street Name
- Building Number
- Building Name
- Floor
- Post Box
- Room
- Post Code
- Town Name
- Town Location Name
- District Name
- Country Sub Division

Nested element capturing the various types of identifiers, e.g., **BIC**, LEI etc. **BIC** is mandatory for an Authorised Party initiation and FI payment initiation.

**Identification**

Optional element to capture the Initiating Party's ISO country code of residence

**Country of Residence**

**Contact Details**

---

<!-- Page 54 -->

pain.001 Interbank Customer Credit Transfer Initiation – Forwarding Agent

Min 0 – Max 1

The *Forwarding Agent* is mandatory in a relay scenario whereby the *Initiating Party* (the *Debtor* or authorised third party) has to provide **Business Identifier Code** (BIC FI) of the *Forwarding Agent* in the original pain.001 message. The Forwarding Agent acts as a concentrating financial institution and forwards the pain.001 message to the *Debtor Agent* for execution.

Other options to identify the *Forwarding Agent* include:

- Clearing System Member ID
- LEI (Legal Entity Identifier)

```
                    +--------+
                    | BICFI  |
                    +--------+
                    +-------------------+
+-------------------+ Clearing          +------------------+
|                   | System            |                  |
| Financial         | Member Id <------>| Clearing         |
| Institution       +-------------------+ System Id        |
| Identification    +--------+          +------------------+
|                   | LEI    |
|                   +--------+
+-------------------+--------+
                    | Various sub-
                    | element |
                    +--------+
```

For the use cases of Authorised Party initiation and FI payment initiation, Forwarding Agent is not required.

---

<!-- Page 55 -->

# Payment Information

---

<!-- Page 56 -->

The CBPR+ pain.001 Interbank Usage Guideline aligns to the Usage Guideline of CGI-MP, to remain interoperable. It is important to recognise that the CGI Postal Address allows the Postal Address information to be captured as both structured and unstructured (address line) data, of which the Country Code within the Postal Address is mandatory.
As a payment initiation could instruct various types of Payment Methods settled across various Clearing Methods, it should also be recognized that the Usage Guideline specification of those instructions need to be adhered to, which may need some enrichment or repair of the data from the payment initiation message.
Postal Address is a good example of such data enrichment or repair, where many domestic payment methods exclusively support unstructured postal addresses. Likewise, CBPR+ and HVPS+ payments consider structured and unstructured postal addresses to be mutually exclusive. i.e., only one or the other may be used.

**CGI-MP** payment Initiation/
**CBPR+** payment initiation interbank

Structured | Unstructured

pain.001

Unstructure — Many domestic proprietary payments

Structured | Unstructured — **CBPR+** payments

---

<!-- Page 57 -->

Min 1 – Max 1

The Interbank Customer Credit Transfer Initiation **Payment Information Identification** provides a mandatory element to identify the payment initiation.

This 35 character identifier is a point-to-point reference used to unambiguously identify the payment information group within the message. It is also known as a batch reference number if the message contains multiple transactions.

For single transactions in the CBPR+ usage guidelines, the value in Payment Information Identification is the same as the Message Identification of the Group Header.

---

<!-- Page 58 -->

Min 1 - Max 1

The pain.001 message *Payment Method* specifies the means of payment that will be used to move the amount of money. One of the following payment method codes must be used:

| Code | Name | Definition |
| :--- | :--- | :--- |
| CHK | Cheque | Written order to a bank to pay a certain amount of money from one person to another person. |
| TRF | Credit Transfer | Transfer of an amount of money in the books of the account servicer. |

---

<!-- Page 59 -->

The pain message **Payment Type Information** provides a set of optional elements where the payment type can be described.

# Payment Type Information

**Instruction Priority**
Min 0 – Max 1

A choice of imbedded codes representing the urgency considered by the instructing party. This point-to-point information may be used by the instructed party to differentiate the processing

**Service Level**
Min 0 – Max 3

A nested element which may either use an external ISO Service Level code or a proprietary code. It is used to identify a particular agreed service level which should be applied to the payment. Where a service level is not agreed, it may be ignored.

**Local Instrument**
Min 0 – Max 1

A nested element which may either use an external ISO Local Instrument code or a proprietary code. It can be used in combination with Service Level to identify the type of local instrument. For example, INST – Instant Credit Transfer for SEPA Service Level.

Note: the ISO instrument codes are registered by specific community group (captured in the code list)

**Category Purpose**

A nested element which may either use an external ISO Category Purpose code or a proprietary code. It is used to identify the category of payment. For example, DIVI is the payment of dividends.

---

<!-- Page 60 -->

# pain.001 Interbank Customer Credit Transfer Initiation – Requested Execution Date

| Min 1 – Max 1 |
|---|

The pain.001 message mandatory **Requested Execution Date** element, captures the date and time at which the initiating party requests the clearing agent to process the payment.

It is the date on which the debtor's account is debited. If payment by cheque, the date when the cheque must be generated by the bank. It is defined by either *ISO Date* expressed in the *YYYY-MM-DD format* or *ISO Date Time* below:

1. Universal Time Coordinated (UTC) time YYYY-MM-DDThh:mm:ss.sssZ
2. Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+-hh:mm
3. Local time format YYYY-MM-DDThh:mm:ss.sss

Unlike other CBPR+ messages, the interbank pain.001 message is more flexible in defining the date and time elements. The most recommended representation is Local time with UTC offset which was mandated by CBPR+ (2ⁿᵈ option). Otherwise use UTC time (1ˢᵗ option). Decimal fractions of seconds with 3 digits. Milliseconds are optional.

---

<!-- Page 61 -->

# pain.001 Interbank Customer Credit Transfer Initiation – Pooling Adjustment Date

`Min 0 – Max 1`

The pain.001 message optional **Pooling Adjustment Date** element, is used for the correction of the value date of a cash pool movement that has been posted with a different value date.

It is defined by *ISO Date* expressed in the *YYYY-MM-DD format*

This element is not widely used in the payment industry. For the use case of interbank, it is even less likely to be utilized.

Payment Information > Pooling Adjustment Date

---

<!-- Page 62 -->

The ISO 20022 pain messages describes the party whose account is debited for a transaction as the **Debtor**. `Min 1 – Max 1`
The *Debtor* sub elements describe the *Debtor* in greater detail.

Mandatory **Name** (where a BIC identifier is not provided) by which the party is known
**Name**

Nested element capturing either structured or unstructured *Debtor* address details.
Note: Structured address is strongly recommended with mandatory Town Name and Country
**Postal Address**
**Debtor**

Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc.
**Identification**

Optional element to capture the *Debtor*'s ISO country code of residence
**Country of Residence**

| Department |
| :--- |
| Sub Department |
| Street Name |
| Building Number |
| Building Name |
| Floor |
| Post Box |
| Room |
| Post Code |
| Town Name |
| Town Location Name |
| District Name |
| Country Sub Division |
| Country → Code |
| Address Line |

---

<!-- Page 63 -->

The pain.001 <span style="background-color:#99D9F0;">Min 1 – Max 1</span> ***Debtor Account*** is used to capture the account information for which debit entry will be made as a result of the transaction, which will be also reflected in their account Statement.

The ***Debtor Account*** uses a variety of nested elements to capture information related to the account.

| | |
|---|---|
| <span style="background-color:#99D9F0;">Min 1 – Max 1</span> | ***Identification*** identifies the account maintained at the Debtor Agent (Account Servicing Institution) |
| <span style="background-color:#99D9F0;">Min 0 – Max 1</span> | ***Type*** uses the external Cash Account Type code list to identify the type of account |
| <span style="background-color:#99D9F0;">Min 0 – Max 1</span> | ***Currency*** identifies the currency of the account, recommended. |
| <span style="background-color:#99D9F0;">Min 0 – Max 1</span> | ***Name*** identifies the name of the account as assigned by the Debtor Agent (Account Servicing Institution) |
| <span style="background-color:#99D9F0;">Min 0 – Max 1</span> | ***Proxy*** captures an alternative identification of the account number such as an email address. This element has further nested ***Type*** which is a choice of external code list or proprietary code and ***Identification*** which are both mandatory where the Proxy element is used. |

Indication of Currency of the Debtor Account is recommended in case of multi-currency

---

<!-- Page 64 -->

Min 1 – Max 1

The **Debtor Agent** is a static role in the pain.001 Customer Credit Transfer Initiation. This agent maintains a relationship with their customers, the *Debtor*.

![](https://i.imgur.com/placeholder1.png)

![](https://i.imgur.com/placeholder2.png) Note: Although the ***Debtor Agent***, ***Creditor Agent***, ***Debtor*** and ***Creditor*** all maintain static roles in the pain messages, the description of these parties change in the reporting messages (camt) where the Debtor Agent and Creditor Agent become the Statement Account Servicer and the Debtor and Creditor become the Statement Account Owner. This will be explored further in the camt Cash Management Reporting section.

![](https://i.imgur.com/placeholder3.png) For Agent Identification, BIC is preferred, alternatively Clearing Member ID together with Name and Address may be provided

---

<!-- Page 65 -->

Min 0 – Max 1
The pain.001 *Debtor Agent Account* is used to capture the account information related to the Debtor Agent.

The *Debtor Agent Account* uses a variety of nested elements to capture information related to the account.

Min 1 – Max 1 *Identification* identifies the account maintained at the Account Servicing Institution
Min 0 – Max 1 *Type* uses the external Cash Account Type code list to identify the type of account
Min 0 – Max 1 *Currency* identifies the currency of the account
Min 0 – Max 1 *Name* identifies the name of the account as assigned by the Account Servicing Institution
Min 0 – Max 1 *Proxy* captures an alternative identification of the account number such as an email address. This element has further nested *Type* which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used.

Debtor Agent and Creditor Agent are Financial Institutions, therefore the nested elements *Name* and *Proxy* are unlikely to be used.

---

<!-- Page 66 -->

Min 0 – Max 1

The ***Instruction for Debtor Agent*** element within the pain.001 message optionally provides information related to the processing of the payment.

The ***Instruction for Debtor Agent*** element offers a maximum of 140 characters to further information related to the processing of the payment instruction, that may need to be acted upon by the *Debtor Agent*, depending on bilateral agreement.

---

<!-- Page 67 -->

Ultimate Party
Ultimate Debtor
Ultimate Creditor

Min 0 – Max 1 Min 0 – Max 1
The pain.001 message introduces ***Ultimate Debtor*** and ***Ultimate Creditor***. The ***Ultimate Debtor*** element should not be confused with an ***Initiating Party*** who may send a payment initiation request on behalf of the ***Debtor***, for example, Payment Factory.

CBPR+ premise is that an ***Ultimate Debtor*** has no financial regulated direct account relationship with the corresponding Debtor. Likewise, an ***Ultimate Creditor*** has no financial regulated account relationship with the corresponding Creditor.

The ***Ultimate Debtor*** and ***Ultimate Creditor*** can be identified by a combination of Name and structured address or Organisation ID (e.g., BIC, LEI), Private ID and Country Of Residence.

Ultimate Debtor exists at the Payment Information Level and Transaction Level. Since CBPR+ interbank pain.001 is restricted to single transaction, Ultimate Debtor should be used at the Transaction Level unless bilaterally determined.

---

<!-- Page 68 -->

Min 0 – Max 1

The **Charge Bearer** element exists at the Payment Information level and Transaction level. It uses an embedded code to specify which party/parties would bear any charges associated with processing the payment transaction. This element is comparable with MT Field 71A ‘Details of Charges’

| Charge Bearer (0..1) | Code | Description | ISO 20022 |
|---|---|---|---|
| | CRED | Creditor | |
| | DEBT | Debtor | |
| | SHAR | Shared | |

| 71A: Details of Charges | Code | Description | MT 101 |
|---|---|---|---|
| | BEN | Beneficiary | |
| | OUR | Our Customer Charges | |
| | SHA | Shared Charges | |

Charge Bearer at the Payment Information Level and the Transaction Level is mutually exclusive. It should be used at the Transaction Level unless bilaterally determined.

---

<!-- Page 69 -->

# pain.001 Interbank Customer Credit Transfer Initiation – Charges Account

The pain.001 optional **Min 0 – Max 1** ***Charges Account*** element, which is used to process charges associated with a transaction.

Charges account should be used when charges have to be booked to an account different from the account identified in debtor's account.

This element is not widely used in the payment industry.

---

<!-- Page 70 -->

pain.001 Interbank Customer Credit Transfer Initiation – Charges Account Agent

Min 0 – Max 1

The pain.001 optional **Charges Account Agent** element, which is used to specify the agent that services a charges account.

Charges account agent should only be used when the charges account agent is different from the debtor agent.

This element is not widely used in the payment industry. It should also be noted that the ChargesAccountAgentRule inherited from the base message should be ignored as the optional Branch of DebtorAgent is removed from this Usage Guideline.

---

<!-- Page 71 -->

# Credit Transfer Transaction Information

---

<!-- Page 72 -->

Min 1 – Max 1

The pain.001 message contains **_Payment Identification_** which provides a set of elements to identify the payment of which several are mandatory elements.

## Payment Identification

- **Instruction Identification** (Min 0 – Max 1)
  a **point-to-point reference** of 35 characters long will be returned to account statements if provided by the initiating party.
  Note: Instruction Id is mandatory in other CBPR+ messages as it maps directly with the mandatory Sender's Reference (Field 20) of the legacy MT payment messages.

- **End to End Identification** (Min 1 – Max 1)
  an **end-to-end reference** provided by the _Debt or_ which must be passed unchanged throughout the payment and reported to the Creditor.
  note: if the Debtor has not provide an end-to-end identifier, the Debtor Agent may populate "**NOTPROVIDED**" to comply the mandatory need of this element.

- **UETR** (Min 1 – Max 1)
  the **Unique End-to-end Transaction Reference** created using the UUID v4 standard. This reference must be passed unchanged throughout the payment, it may also be created by the Debtor within their Payment Initiation request, and also included in reporting messages.

Credit Transfer Transaction Information

---

<!-- Page 73 -->

The pain.001 **Payment Type Information** provides a set of optional elements where the payment type can be described.

**Instruction Priority**
Min 0 – Max 1

A choice of imbedded codes representing the urgency considered by the instructing party. This point-to-point information may be used by the instructed party to differentiate the processing

**Service Level**
Min 0 – Max 3

A nested element which may either use an external ISO Service Level code or a proprietary code. It is used to identify a particular agreed service level which should be applied to the payment. Where a service level is not agreed, it may be ignored.

**Payment Type Information**

**Local Instrument**
Min 0 – Max 1

A nested element which may either use an external ISO Local Instrument code or a proprietary code. It can be used in combination with Service Level to identify the type of local instrument. For example, INST – Instant Credit Transfer for SEPA Service Level.

Note: the ISO instrument codes are registered by specific community group (captured in the code list)

**Category Purpose**

A nested element which may either use an external ISO Category Purpose code or a proprietary code. It is used to identify the category of payment. For example, DIVI is the payment of dividends.

Credit Transfer Transaction Information

---

<!-- Page 74 -->

# pain.001 Interbank Customer Credit Transfer Initiation – Currency and Amount

Min 1 – Max 1

The pain.001 nested **Amount** element has a choice of either ***Instructed Amount*** or ***Equivalent Amount*** to capture the amount and currency of the Customer Credit Transfer Initiation.

**Instructed Amount**

The ***Instructed Amount*** captures currency and amount of money to be moved between the Debtor and Creditor, before deduction of charges, expressed in the currency as ordered by the initiating party. This amount has to be transported unchanged through the transaction chain. This element is comparable with the legacy Field 33B.

**Equivalent Amount**

The ***Equivalent Amount*** *nested* element captures currency and ***Amount*** of money to be moved between the Debtor and Creditor, before deduction of charges, and is expressed in the currency of the Debtor's account. The ***Currency Of Transfer*** element capture the equivalent currency to be transferred which the first agent will convert the credit transfer into.

---

<!-- Page 75 -->

pain.001 Interbank Customer Credit Transfer Initiation – Exchange Rate Information

`Min 0 – Max 1`

The pain.001 **Exchange Rate Information** element provides details on the currency exchange rate and contract.

**Exchange Rate Information**

- **Unit Currency** — Currency in which the rate of exchange is expressed in a currency exchange. For example, 1GBP = xxxCUR, the unit currency is GBP.
- **Exchange Rate** — The factor used for conversion of an amount from one currency to another. This reflects the price at which one currency was bought with another currency.
- **Rate Type** — Specifies the type used to complete the currency exchange, such as SPOT, SALE or AGRD (Agreed).
- **Contract** — Unique and unambiguous reference to the foreign

Credit Transfer Transaction Information ⌄

---

<!-- Page 76 -->

Min 0 – Max 1

The **Charge Bearer** element exists at the Payment Information level and Transaction level. It uses an embedded code to specify which party/parties would bear any charges associated with processing the payment transaction. This element is comparable with MT Field 71A ‘Details of Charges’

| Charge Bearer (0..1) | Code | Description | ISO 20022 |
| :--- | :--- | :--- | :--- |
| | CRED | Creditor | |
| | DEBT | Debtor | |
| | SHAR | Shared | |

| 71A: Details of Charges | Code | Description | MT 101 |
| :--- | :--- | :--- | :--- |
| | BEN | Beneficiary | |
| | OUR | Our Customer Charges | |
| | SHA | Shared Charges | |

Charge Bearer at the Payment Information Level and the Transaction Level is mutually exclusive. It should be used at the Transaction Level unless bilaterally determined.

Credit Transfer Transaction Information

---

<!-- Page 77 -->

Min 0 – Max 1

The **Cheque Instruction** information block contains a set of elements needed to issue a cheque. The following types of cheques are commonly used in the market:

| Cheque Type | Code | Description |
| :--- | :--- | :--- |
| Bank Cheque | BCHQ | Cheque drawn on the account of the debtor's financial institution, which is debited on the debtor's account when the cheque is issued. These cheques are printed by the debtor's financial institution and payment is guaranteed by the financial institution. Synonymis 'cashier's cheque'. |
| Customer Cheque | CCHQ | Cheque drawn on the account of the debtor and debited on the debtor's account when the cheque is cashed. Synonym is 'corporate cheque'. |
| Draft | DRFT | A guaranteed bank cheque with a future value date (do not pay before], which in commercial terms is a 'negotiable instrument': the beneficiary can receive early payment from any bank under subtraction of a discount. The ordering customer's account is debited on value date. |

The **Delivery Method** element specifies the method to be used in delivering the cheque by the *Debtor Agent*. For example, a code CRCD is used to courier the cheque to the *Creditor*.

Credit Transfer Transaction Information

---

<!-- Page 78 -->

Ultimate Party
Ultimate Debtor
Ultimate Creditor

Min 0 – Max 1
Min 0 – Max 1

The pain.001 message introduces *Ultimate Debtor* and *Ultimate Creditor*. The *Ultimate Debtor* element should not be confused with an *Initiating Party* who may send a payment initiation request on behalf of the *Debtor*, for example, Payment Factory.

CBPR+ premise is that an *Ultimate Debtor* has no financial regulated direct account relationship with the corresponding Debtor. Likewise, an *Ultimate Creditor* has no financial regulated account relationship with the corresponding Creditor.

The *Ultimate Debtor* and *Ultimate Creditor* can be identified by a combination of Name and structured address or Organisation ID (e.g., BIC, LEI), Private ID and Country Of Residence.

Ultimate Debtor exists at the Payment Information Level and Transaction Level. Since CBPR+ interbank pain.001 is restricted to single transaction, Ultimate Debtor should be used at the Transaction Level unless bilaterally determined.

Credit Transfer Transaction Information

---

<!-- Page 79 -->

Min 0 – Max 1

The pain.001 has three optional **_Intermediary Agent (1,2 and 3)_** elements. These agents represent the agent(s) that exist between the _Debtor Agent_ and the _Creditor Agent_.

- If more than one intermediary agent is present, then **_Intermediary Agent 1_** identifies the agent between the _Debtor Agent_ and the **_Intermediary Agent 2_.**
- If more than two intermediary agents are present, then **_Intermediary Agent 2_** identifies the agent between the **_Intermediary Agent 1_** and the **_Intermediary Agent 3._**
- If **_Intermediary Agent 3_** is present, then it identifies the agent between the **_Intermediary Agent 2_** and the _Creditor Agent._

More commonly the ISO 9362 Financial Institution **_Business Identifier Code_** is considered the best practice de factor standard for 'many to many' / correspondent banking payments.

Other options to identify the **_Intermediary Agent_** include:
- Clearing System Member ID
- LEI (Legal Entity Identifier)
- Name and either structured, or unstructured Postal Address

Credit Transfer Transaction Information
- Intermediary Agent 1
- Intermediary Agent 2

---

<!-- Page 80 -->

pain.001 Interbank Customer Credit Transfer Initiation – Intermediary Agent Account

Min 0 – Max 1

The pain.001 *Intermediary Agent (1,2 and 3) Accounts* are used to capture the account information related to these Agents.

The *Intermediary Agent Account* uses a variety of nested elements to capture information related to the account.

| Constraint | Element | Description |
|---|---|---|
| Min 1 – Max 1 | **Identification** | identifies the account maintained at the Account Servicing Institution. |
| Min 0 – Max 1 | **Type** | uses the external Cash Account Type code list to identify the type of account. |
| Min 0 – Max 1 | **Currency** | identifies the currency of the account. |
| Min 0 – Max 1 | **Name** | identifies the name of the account as assigned by the Account Servicing Institution. |
| Min 0 – Max 1 | **Proxy** | captures an alternative identification of the account number such as an email address. This element has further nested **Type** which is a choice of external code list or proprietary code and **Identification** which are both mandatory where the Proxy element is used. |

Credit Transfer Transaction Information

Intermediary Agent Account 1

Intermediary Agent Account 2

Intermediary Agent is a Financial Institution, therefore the nested

---

<!-- Page 81 -->

Min 0 – Max 1
The **_Creditor Agent_** is a static roles in the pain.001 Customer Credit Transfer Initiation. This agent maintain a relationship with their customers, the _Creditor_.

![](images/image_01.png)

Note: Although the **_Debtor Agent_**, **_Creditor Agent_**, **_Debtor_** and **_Creditor_** all maintain static roles in the pain messages, the description of these parties change in the reporting messages (camt) where the Debtor Agent and Creditor Agent become the Statement Account Servicer and the Debtor and Creditor become the Statement Account Owner. This will be explored further in the camt Cash Management Reporting section.

---

<!-- Page 82 -->

The pain.001 *Min 0 – Max 1* **Creditor Agent Account** is used to capture the account information related to the *Creditor Agent*.

The **Creditor Agent Account** uses a variety of nested elements to capture information related to the account.

| | |
|---|---|
| Min 1 – Max 1 | **Identification** identifies the account maintained at the Account Servicing Institution |
| Min 0 – Max 1 | **Type** uses the external Cash Account Type code list to identify the type of account |
| Min 0 – Max 1 | **Currency** identifies the currency of the account |
| Min 0 – Max 1 | **Name** identifies the name of the account as assigned by the Account Servicing Institution |
| Min 0 – Max 1 | **Proxy** captures an alternative identification of the account number such as an email address. This element has further nested **Type** which is a choice of external code list or proprietary code and **Identification** which are both mandatory where the Proxy element is used. |

Debtor Agent and Creditor Agent are Financial Institutions, therefore

---

<!-- Page 83 -->

The ISO 2022 pain messages describe the *Creditor* as the party whose account was credited for a transaction. The *Creditor* sub elements describe the *Creditor* in greater detail.

Min 1 – Max 1

Mandatory *Name* (where a BIC identifier is not provided) by which the party is known

**Name**

**Creditor**

Nested element capturing either structured or unstructured *Creditor* address details.

**Postal Address**

Note: Structured address is strongly recommended with mandatory Town Name and Country

Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc.

**Identification**

Optional element to capture the *Creditor*'s ISO country code of residence

**Country of Residence**

**Postal Address Tree:**
*   Postal Address
    *   Department
    *   Sub Department
    *   Street Name
    *   Building Number
    *   Building Name
    *   Floor
    *   Post Box
    *   Room
    *   Post Code
    *   Town/Name
    *   Town Location Name
    *   District Name
    *   Country Sub Division
    *   Country
        *   Code
    *   Address Line

---

<!-- Page 84 -->

The pain.001 *<u>Creditor Account</u>* is used to capture the account information for which credit entry will be made as a result of the transaction, which will be also reflected in their account Statement.

The *<u>Creditor Account</u>* uses a variety of nested elements to capture information related to the account.

`Min 1 – Max 1` *<u>Identification</u>* identifies the account maintained at the Creditor Agent (Account Servicing Institution)

`Min 0 – Max 1` *<u>Type</u>* uses the external Cash Account Type code list to identify the type of account

`Min 0 – Max 1` *<u>Currency</u>* identifies the currency of the account

`Min 0 – Max 1` *<u>Name</u>* identifies the name of the account as assigned by the Creditor Agent (Account Servicing Institution)

`Min 0 – Max 1` *<u>Proxy</u>* captures an alternative identification of the account number such as an email address. This element has further nested *<u>Type</u>* which is a choice of external code list or proprietary code and *<u>Identification</u>* which are both mandatory where the Proxy element is used.

Creditor Account is not required for cheque payments.

---

<!-- Page 85 -->

Min 0 - Max 1    Min 0 - Max 1

The pain.001 message introduces **Ultimate Debtor** and **Ultimate Creditor**. The **Ultimate Debtor** element should not be confused with an **Initiating Party** who may send a payment initiation request on behalf of the **Debtor**, for example, Payment Factory.

CBPR+ premise is that an **Ultimate Debtor** has no financial regulated direct account relationship with the corresponding Debtor. Likewise, an **Ultimate Creditor** has no financial regulated account relationship with the corresponding Creditor.

The **Ultimate Debtor** and **Ultimate Creditor** can be identified by a combination of Name and structured address or Organisation ID (e.g., BIC, LEI), Private ID and Country Of Residence.

Credit Transfer Transaction Information

---

<!-- Page 86 -->

Min 0 – Max 2

The **_Instruction for Creditor Agent_** element within the pain.001 message optionally provides information related to the processing of the payment for the Creditor Agent.

The **_Instruction for Creditor Agent_** element offers a multiplicity of up to 2 occurrences of information. This element enables:
➢ the use of an embedded choice of code to describe the instruction (e.g. CHQB – Pay Creditor by Cheque)
➢ free format _instruction information_
➢ or both, where the free format complements the code.
The use of this element may be **bilaterally** agreed with the _Creditor Agent_. It must be passed on throughout the life cycle of the transaction until the payment reaches the _Credit Agent_.

Credit Transfer Transaction Information

---

<!-- Page 87 -->

# ISO 20022 Programme

## Quality data, quality payments

## CBPR+ User Handbook

SR 2023 Edition
March 2023

---

<!-- Page 88 -->

Min 0 – Max 1

The ***Instruction for Debtor Agent*** element within the pain.001 message optionally provides information related to the processing of the payment.

The ***Instruction for Debtor Agent*** element offers a maximum of 140 characters to further information related to the processing of the payment instruction, that may need to be acted upon by the *Debtor Agent*, depending on bilateral agreement.

Credit Transfer Transaction Information

---

<!-- Page 89 -->

Min 0 – Max 1

The **Purpose** element within the pain.001 message captures the reason for the payment transaction which may either use an external ISO **Purpose code** or a proprietary code.

The purpose is used to capture the nature of the payment, e.g., **IVPT** Invoice Payment, **FEES** Payment of Fees etc. and should not be confused with Regulatory Reporting codes. By definition this information is typically defined by the *Debtor*.

The externalised Purpose code set is classified by the purpose, for example commercial, for which the numerous codes within the classification are each described by Name and Definition.
For example, **LIMA** is classified within the Cash Management categorisation, with the *Name* **Liquidity Management** described as a **Bank initiated account transfer to support zero target balance management, pooling or sweeping.**

*Category Purpose* also captures a high-level purpose, which unlike *Purpose* is less granular but can trigger special processing e.g., Category Purpose code SALA 'Salary Payment' may trigger a reporting process which restricts sensitive data i.e., individual salary names.

Credit Transfer Transaction Information

---

<!-- Page 90 -->

Min 0 – Max 10
The *Regulatory Reporting* block within the pain.001 message is nested to capture regulatory and statutory information needed to report to the appropriate authority/s.

Min 0 – Max 1
The *Debit Credit Reporting Indicator* utilises an embedded choice of code to indicate whether the regulatory reporting applies to the:
* DEBT (debit)
* CRED (credit)
* BOTH

Min 0 – Max 1
The *Authority* element captures the *Name* and *Country* code of the Authority/Entity requiring the regulatory reporting information.

Min 0 – Max 9
The *Details* element provides the detail on the regulatory reporting information.

Credit Transfer Transaction Information > Regulatory Reporting >
Debit Credit Reporting Indicator
Authority

---

<!-- Page 91 -->

Min 0 – Max 1

The pain.001 nested **Tax** element captures information related to tax. The tax information block is applicable when tax information is used by the clearing or the local regulatory authority(s).

This element caters for two main types of tax related payments:

- Tax payment obligation that is required to be transmitted with a payment
- Information that accompanies an actual payment of a tax obligation

The follow nested elements may be used to capture detailed tax information:

Min 0 – Max 1 | Min 0 – Max 1 | Min 0 – Max 1 | Min 0 – Max 1 | Min 0 – Max 1 | Min 0 – Max 1
---|---|---|---|---|---
Creditor | Debtor | Administration Zone | Reference Number | Method | Total Taxable Base Amount

Min 0 – Max 1 | Min 0 – Max 1 | Min 0 – Max 1 | Min 0 – Max *
---|---|---|---
Total Tax Amount | Date | Sequence Number | Record

Tax information block is also available within the Structured Remittance Information block which is applicable when tax information is used by the creditor as part of remittance information.

---

<!-- Page 92 -->

Min 0 – Max 10

The *Related Remittance Information* element within the pain.001 message is nested to provide information related to the handling of remittance information.

Min 0 – Max 1

The *Remittance Identification* captures a unique reference assigned by the initiating party of the payment to identify the remittance information sent separately from the payment instruction.

Min 0 – Max*

The *Remittance Location Details* uses a set of nested elements to provide information on either the location of or the delivery of remittance information.

- *Method* requires a code from an embedded list to detail the method used to deliver the remittance advice information e.g. *EMAL* (email)
- *Electronic Address* provides an electronic address for which an agent is to send the remittance information to e.g. the email address. It may also reference a URL where remittance information may be deposited or retrieved.
- *Postal Address* provides the postal address to which an agent is to send the remittance information

Unlike CBPR+ pacs messages, in the interbank pain.001 message, Related Remittance Information and Remittance Identification are non-mutually exclusive due to a corporate use case of populating both information blocks for detailing remittance advices which are part of value-added service offered by the *Debtor Agent*.

SCORE Guideline: If the Related Remittance Information is used, and a Remittance Identification is provided, it is recommended that the Remittance Identification equal the End To End Identification.

---

<!-- Page 93 -->

Min 0 – Max 1
The optional **Remittance Information** element within the pain.001 message is nested to provide either **Structured** or **Unstructured** information related to payment, such as invoices.

**Remittance Information** enables the matching/reconciliation of an entry that the payment is intended to settle.

Min 0 – Max 1
The **Unstructured** sub element captures free format *Remittance Information* which is restricted in interbank CBPR+ to 140 characters to ensure backward compatibility with the legacy MT message during coexistence.

Min 0 – Max *
The **Structured** element is nested capturing rich structured *Remittance Information*, and is unlimited in its multiplicity, but must not exceed 9,000 characters of business information (does not include the xml element identification)
The use of this nested element should be bilaterally/multilaterally agreed, to ensure end-to-end transportation of this data.

Recommend to refer to **CGI-MP Document Centre for Country**

Credit Transfer Transaction Information
Remittance Information
Structured

---

<!-- Page 94 -->

The bilaterally/multilaterally agreed **Remittance Information** which is **Structured** must not exceed 9,000 characters of business content (i.e. the information). This nested element is used to capture a variety of structured remittance information.

**Structured**

| Referral Document Information | Referral Document Amount | Creditor Reference Information | Invoice | Invoice | Tax Reimbursement | Garnishment Reimbursement | Additional Remittance Information |
|---|---|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | ... | ... | ... |

example of *Structured* invoice information

The **Creditor Remittance Information** is provided to the **Creditor** in the Cash Management Reporting messages' Remittance Information component, for example, the camt.053 Bank to Customer Statement.

| element names | | xml tag | business information |
|---|---|---|---|
| **Structured** | Reference Document Information | `<Strd>` | |
| | Type | `<RfrdDocInf>` | |
| | | `<Tp>` | |
| | Code Or Proprietary | `<CdOrPrtry>` | |
| | Code | `<Cd>` | CINV |
| | Number | `<Nb>` | A0000101 |
| | Related Date | `<Dt>` | 2019-10-29 |

In this example Referral Document Information and its nested elements have multiplicity which support up to 9,000 character of information. Whereby this element can be repeated to include more coded information such as another invoice.

Credit Transfer Transaction Information ✓
> Remittance Information

---

<!-- Page 95 -->

The **Creditor Reference** in the *Creditor Remittance Information* component in the structured remittance information is generated by *Creditor* to inform the *Debtor* who has to include the reference in the Remittance Information component of the pain.001.

Creditor Reference in the Structured Remittance Information is based on ISO 11649
* 2 letters "RF"
* 2 digits check digit
* 21 letters/digits creditor reference

Facilitates STP and auto-match with the creditor reference and its account receivable
* A vendor can add the creditor reference to its invoice. When a customer pays the invoice, they write the creditor reference instead of the invoice number in the payment message (e.g., MT 101 F70 which will be carried in MT 103)
* When the vendor receives the payment, it can auto-match the incoming credit entry and the creditor reference extracted from the statement (e.g., MT 940 F61/86)

SCORE Guideline: For Creditor Reference information, in instances where the Creditor Reference Type code is SCOR (Structured Communication Reference) and the Creditor Reference is structured in accordance with ISO 11649, the

Credit Transfer Transaction Information
Remittance Information

---

<!-- Page 96 -->

> Use case should be considered as a principal example whereby use case may be cross referenced e.g., a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases.

**Interbank Customer Credit Transfer Initiation - Relay**
Use Case pn.1.1.1 – High Level Payment Initiation Interbank 'relay' (pain.001)
Use Case pn.1.1.1.a – High Level Payment Initiation Interbank 'relay' (pain.001) Multi-bank Sweep
Use Case pn.1.1.2 – High Level Payment Initiation Interbank 'relay' (pain.001) involving a Payment Market Infrastructure

**Interbank Customer Credit Transfer Initiation – Authorised Party**
Use Case pn.1.2.1 – High Level Payment Initiation Interbank (pain.001) by an Authorised Party
Use Case pn.1.2.1.a. – High Level Payment Initiation Interbank (pain.001) FI-Initiated Sweep (Long position at the Secondary Account)
Use Case pn.1.2.1.b. – High Level Payment Initiation Interbank (pain.001) by an Authorised Party to pay themselves as the Creditor

**Interbank Customer Credit Transfer Initiation – Financial Institution**
Use Case pn.1.3.1 – High Level Payment Initiation Interbank (pain.001) Financial Institution Payment Initiation

---

<!-- Page 97 -->

In the interbank relay scenario, the Forwarding Agent relays the pain.001 message to the Debtor Agent which will debit the account of the Debtor and initiate a credit transfer.

**Sequence Diagram:**

1. (Initiating Party) → `pain.001` → (F)
2. (F) → `Interbank pain.001` → (A)
3. (A) → `pacs.008` → (B)
4. (B) → `camt.053` → (Creditor)

Return messages:
- (F) → `pain.002` → 1 (Initiating Party)
- (A) → `Interbank pain.002` → 3b (F)
- 3a (A)

**Legend:**

**1**
Initiating Party sends a payment instruction to the Forwarding Agent

**2**
Forwarding Agent (F) forwards the payment instruction to the Debtor Agent (A)

**3**
Debtor Agent (A) debits the account of Debtor and initiates a credit transfer by forwarding a local credit transfer message pacs.008

**3a**
Debtor Agent (A) provides a status update ACSP (accepted settlement in progress) to the

**3b**
Forwarding Agent (F) relays the status ACSP (accepted settlement in progress) to the Initiating Party, based upon a bilateral agreement

**4**
Creditor Agent (B) processes the payment and sends the statement to Creditor

---

<!-- Page 98 -->

In the interbank relay scenario, the Forwarding Agent relaying the pain.001 message to the Debtor Agent(s) in this case to sweep excess cash from the account of the Debtor and consolidate cash for a Corporate.

```
[1] Initiating Party --pain.001--> [2] Forwarding Agent (F) --Interbank pain.001--> [3] Debtor Agent (A) --pacs.008--> [4] Creditor Agent (B) --camt.053--> Creditor
        ^                                ^                                                                                          |
        |                                |                                                                                        |
        +----pain.002--------------------+<----------------Interbank pain.002-----------------------------------------------------+
```

| **1** | **3** | **3b** |
|---|---|---|
| Initiating Party sends a payment instruction to the Forwarding Agent to sweep excess funds from its subsidiary's account to the master account with Bank B | Debtor Agent (A) debits the account of Debtor and initiates a credit transfer by forwarding a local credit transfer message pacs.008 | Forwarding Agent (F) relays the status ACSP (accepted settlement in progress) to the Initiating Party, based upon a bilateral agreement |

| **2** | **3a** | **4** |
|---|---|---|
| Forwarding Agent (F) forwards the payment instruction to the | Debtor Agent (A) provides a status update ACSP (accepted settlement in progress) to the | Creditor Agent (B) processes the payment and notifies Creditor of a successful sweep through the |

---

<!-- Page 99 -->

## Market Infrastructure

In the interbank relay scenario, the Forwarding Agent relays the pain.001 message to the Debtor Agent which will debit the account of the Debtor initiate a credit transfer through a Payment Market Infrastructure.

**1** → `pain.001` → **2** (F) → `Interbank pain.001` → **3** (A) → `pacs.008` → (PMI) → `pacs.008` → **4** (B) →

`pain.002` ← **3b** (F) ← `Interbank pain.002` ← **3a** (A)

**1** Initiating Party sends a payment instruction to the Forwarding Agent

**2** Forwarding Agent (F) forwards the payment instruction to the Debtor Agent (A)

**3** Debtor Agent (A) debits the account of Debtor and initiates a credit transfer by forwarding a local credit transfer message pacs.008 to a Payment Market Infrastructure (PMI)

**3a** Debtor Agent (A) provides a status update ACSP (accepted settlement in progress) to the Forwarding Agent (F), based upon a bilateral

**3b** Forwarding Agent (F) relays the status ACSP (accepted settlement in progress) to the Initiating Party, based upon a bilateral agreement

**4** Creditor Agent (B) receives local credit transfer message via the Payment Market Infrastructure (PMI) and credits the Creditor

---

<!-- Page 100 -->

In the scenario Authorised Party Initiation, the Initiating Party (Agent I) initiates a payment from the Debtor's account based on Debit Authorisation already in place between the Debtor and the Debtor Agent

**Debit Authorisation**

**DA** As a pre-requisite the Debtor provides Debit Authorisation to Agent A, which allows Agent I to Initiate Payment from their account

**2** Agent (I) initiates a payment request (pain.001) to the Debtor Agent (A) to move fund from the Debtor's account, as an

**Interbank pain.001**

**3** Debtor Agent (A) debits the account of Debtor and initiates a credit transfer

**Interbank pain.002**

**3a** Debtor Agent (A) optionally provides a status update to the Initiating Party (Agent I), based upon a bilateral agreement

**pacs.008**

**pacs.002**

**4** Creditor Agent (B) receives the credit transfer message, credits the Creditor, and sends a camt.053 (statement) at the end of the business day to the Creditor. An optional status report is sent to the previous Agent based upon a bilateral agreement

**camt.053**

---

<!-- Page 101 -->

position at the Secondary Account)

In the interbank sweep scenario, the Initiating Party (Agent I) initiates the pain.001 message to the Debtor Agent to sweep excess cash from the account of the Debtor and consolidate the cash for a Corporate.

Sweep Contract
camt.052
Interbank pain.001
Interbank pain.002
pacs.008
pacs.002
camt.053

1 Agent I receives intraday balance report from Debtor Agent (A) on behalf of their mutual customer.

2 Agent (I) initiates a sweep on behalf of the Corporate by sending pain.001 to the Debtor Agent

3 Debtor Agent (A) debits the account of Debtor and initiates a credit transfer

3a Debtor Agent (A) optionally provides a status update to the Initiating Party (Agent I), based upon a bilateral agreement

4 Creditor Agent (B) receives credit transfer message, credits the Creditor, and sends a camt.053 (statement) at the end of the business day to the Creditor. An optional status report is sent to the previous Agent based upon a bilateral agreement

See use case p.8.1.2 for a sweeping contract with a short position

---

<!-- Page 102 -->

# pay themselves as the Creditor.

In the Authorised Party Initiation scenario, the Initiating Party (Agent I) initiates a payment from the Debtor's account based on Debit Authorisation already in place to move money to themselves as the Creditor

**Flow:**

1. (DA) Debit Authorisation → Agent I
2. Agent I → [Interbank pain.001] → Agent A (3)
   - [Interbank pain.002] ← Agent A (3a)
3. Agent A → [pacs.008] → Agent B (4)
   - [pacs.002] ← Agent B
4. Agent B → [camt.053] → Creditor (I)

**Step Descriptions:**

**DA** As a pre-requisite the Debtor provides Debit Authorisation to Agent I to Initiate Payment from their account with the Debtor Agent (A)

**2** Agent (I) initiates a payment request (pain.001) to the Debtor Agent (A) to move fund from the Debtor's account, as an authorised party, to

**3** Debtor Agent (A) debits the account of Debtor and initiates a credit transfer

**3a** Debtor Agent (A) optionally provides a status update to the Initiating Party (Agent I), based upon a bilateral agreement

**4** Creditor Agent (B) receives the credit transfer message, credits the Creditor, and sends a camt.053 (statement) at the end of the business day to the Creditor. An optional status report is sent to the previous Agent based upon a bilateral agreement

---

<!-- Page 103 -->

# Payment Initiation

The Initiating Party (Agent I) initiates a payment from their own account with the Debtor Agent to move the funds to a non-Financial Institution Creditor

**Flow diagram:**

`[I]` --(1) Interbank pain.001--> `[A]` --(2) pacs.008--> `[B]` --(3) camt.053--> `[Person]`

`[A]` --(2a) Interbank pain.002--> `[I]`

`[B]` --(2) pacs.002--> `[A]`

---

**1**
Agent (I), the Debtor, initiates a payment request (pain.001) to the Debtor Agent (A) to move funds from their own account

**2**
Debtor Agent (A) debits the account of Agent (I), the Debtor and initiates a credit transfer

**3**
Creditor Agent (B) receives credit transfer message, credits the Creditor, and sends the camt.053 (statement) at the end of the business day to the non-FI Creditor. An optional status report is sent to the previous Agent based upon a bilateral agreement

**2a**
Debtor Agent (A) optionally provides a status update to the Initiating Party (Agent I), based upon a bilateral agreement

---

<!-- Page 104 -->

# Interbank Customer
# Payment Status Report

---

<!-- Page 105 -->

pain.002

- Group Header
- Original Group Information And Status
- Original Payment Information And Status
- Transaction Information

The pain.002 message is composed of four building blocks:

- ***Group Header*** which contains a set of characteristics shared by all individual transactions in the message.
- ***Original Group Information and Status*** contains the group of transactions, to which the status report message refers to.
- ***Original Payment Information And Status*** contains information about the original payment information, to which the status report message refers.
- ***Transaction Information And Status*** provides information on the original transactions to which the status report message refers.

It is used to inform the previous party in the payment chain about the positive or negative status of an instruction. It is also used to report on a pending instruction.

---

<!-- Page 106 -->

Debtor
Initiating Party
Forwarding Agent
Debtor Agent*
Creditor Agent
Creditor

pain.001
pain.002**
Interbank pain.001
Interbank pain.002
pacs.008
pacs.002
camt.053

*Debtor Agent is the same as the Initiating Party who initiates the payment status report message.
**or other proprietary method for informing about the status of an instruction

Interbank Customer Payment Status Report message is sent by the Debtor Agent to the previous agent in the payment chain. It is used to provide notification of a rejected status, as required. The provision of a positive status is determined by a bilateral agreement between the agents. There are three common use cases:
1. *Relay.* The pain.002 message is sent by the Debtor Agent to the Forwarding Agent which acts as a concentrating financial institution. It will forward the pain.002 message to the Initiating Party.

---

<!-- Page 107 -->

Debtor
Initiating Party
Forwarding Agent
Debtor Agent*
Creditor Agent
Creditor

pain.001
pain.002**
FINPlus pain.001
FINPlus pain.002
pacs.008
pacs.002
camt.053

*Debtor Agent is the same as the Initiating Party who initiates the payment status report message.
**or other proprietary method for informing about the status of an instruction

FINPlus Customer Payment Status Report message is sent by the Debtor Agent to the previous agent in the payment chain. It is used to provide notification of a rejected status, as required. The provision of a positive status is determined by a bilateral agreement between the agents. There are three common use cases:

1. **Relay:** The pain.002 message is sent by the Debtor Agent to the Forwarding Agent which acts as a concentrating financial institution. It will forward the pain.002 message to the Initiating Party.

---

<!-- Page 108 -->

Debtor
Initiating Party
A
Debtor Agent
B
C
Creditor Agent
D
Creditor

Interbank.pain.001
Interbank.pain.002
pac s.008
pac s.002
camt.053

Interbank Customer Payment Status Report message is sent by the Debtor Agent to the previous agent in the payment chain. It is used to provide notification of a rejected status, as required. The provision of a positive status is determined by a bilateral agreement between the agents. There are three common use cases:
3 **Financial Institution Payment Initiation** (to non-FI) : The pain.002 message is sent by the Debtor Agent to the Debtor (Financial Institution) who requested to initiate a payment from their account with the Debtor Agent to move funds to a non-Financial Institution

---

<!-- Page 109 -->

Debtor

Debtor Agent

Creditor Agent

Forwarding Agent

Initiating Party

Creditor

| From | To | Message |
|---|---|---|
| Initiating Party | Forwarding Agent | pain.008** |
| Forwarding Agent | Creditor Agent | Interbank pain.008 |
| Creditor Agent | Forwarding Agent | Interbank pain.002 |
| Forwarding Agent | Initiating Party | pain.002 |
| Creditor Agent | Debtor Agent | pacs.003 |
| Debtor Agent | Creditor Agent | pacs.002 |
| Debtor Agent | Debtor | camt.053 |

\*Initiating Party may alternative represent an authorised party such as a head office

\*\*or other proprietary method for instructing a direct debit initiation request.

Interbank Customer Direct Debit Initiation message is sent by the Initiating Party to the Forwarding Agent or the Creditor Agent. It is used to request single or bulk collection(s) of funds from one or various debtor's account(s) to a creditor.

**Relay:** Interbank pain.008 message is sent by the Initiating party (the Creditor or authorised party) to the Forwarding Agent which acts as a concentrating financial institution. It will forward the pain.008 message to the Creditor Agent to initiate the direct debit instruction(s).

---

<!-- Page 110 -->

# Group Header

---

<!-- Page 111 -->

Min 1 – Max 1

Each ISO20022 payment message has a ***Message Identification*** element, located in the Group Header. This **35 character** identifier is a point-to-point reference used to unambiguously identify the message.

For Payment Initiation (pain) messages the Message Identification has no exact equivalent in the legacy MT payment message. However, the Sender's Reference (Field 20) could be considered as a similar comparison where a pain message contains a single Transaction.

Each transaction's *Credit Transfer Transaction Information* contains a variety of nested *Payment Identification* elements to capture reference related to the individual transaction such as a UETR (Unique End-to-end Transaction Reference).

For a relay scenario, Forwarding Agent should respect the Message ID provided by the Initiating Party (Debtor Agent) of the pain.002.

Group Header > Message Identification

---

<!-- Page 112 -->

The pain.001 message <span style="background-color: #cce5ff;">Min 1 – Max 1</span> *Creation Date Time* captures the date and time the message was created.

It is defined by *ISO Date Time* with mandatory date and time components expressed in the following formats:

1. Universal Time Coordinated (UTC) time YYYY-MM-DDThh:mm:ss.sssZ
2. Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
3. Local time format YYYY-MM-DDThh:mm:ss.sss

Unlike other CBPR+ messages, the interbank pain.001 message is more flexible in defining the date and time elements. The most recommended representation is Local time with UTC offset which was mandated by CBPR+ (2ⁿᵈ option). Otherwise use UTC time (1ˢᵗ option). Decimal fractions of seconds with 3 digits. Milliseconds are optional.

---

<!-- Page 113 -->

pain.002 Interbank Customer Payment Status Report – Initiating Party

Min 1 – Max 1

Initiating Party = Debtor Agent

Forwarding Agent
Authorised Party
FI Debtor

The *Initiating Party* in the context of interbank payment initiation report is always the **Debtor Agent** which initiates the pain.002 message. **Business Identifier Code** (BIC FI) is mandated to identify the *Initiating Party* in the pain.002 message. There are three use cases below:

1. **Relay:** The **Debtor Agent** sends the pain.002 message to the **Forwarding Agent** which acts as a concentrating financial institution. It will forward the pain.002 message to the original *Initiating Party* who can be the *Debtor* themselves or the Authorised Party. This is commonly known as a relay scenario.
2. **Authorised Party:** The **Debtor Agent** sends the pain.002 to the Financial Institution (**Initiating Party**) which has the authority to initiate a payment on behalf of the *Debtor*, e.g., multi-bank liquidity sweeps
3. **Financial Institution Payment Initiation:** The **Debtor Agent** sends the pain.002 to the Financial Institution which is the **Debtor** who initiate a payment from their account to move funds to a non-Financial Institution *Creditor*

---

<!-- Page 114 -->

pain.002 Interbank Customer Payment Status Report – Forwarding Agent

Min 0 – Max 1

The **Forwarding Agent** is mandatory in a relay scenario whereby the receiver of the pain.002 message is not the original Debtor. In this case, the *Initiating Party* (the *Debtor Agent*) has to provide **Business Identifier Code** (BIC FI) of the *Forwarding Agent* in the pain.002 message. The *Forwarding Agent* acts as a *concentrating financial institution* and forwards the *pain.002 message* to the *Debtor* or the *Initiating Party*.

Other options to identify the **Forwarding Agent** include:

* Clearing System Member ID
* LEI (Legal Entity Identifier)

```
                    +-------+
                    | BICFI |
                    +-------+
                       ^
+-------------------+   |   +----------------+
| Financial         |   +---| Clearing       |
| Institution       |-------| System         |----> Clearing System Id
| Identification    |   |   | Member Id      |
+-------------------+   |   +----------------+
                       |
                    +-------+
                    |  LEI  |
                    +-------+
```

For the use case of multi-bank liquidity sweeps, Forwarding Agent is not required.

---

<!-- Page 115 -->

# Original Group Information and Status

---

<!-- Page 116 -->

The pain.002 Customer Payment Status Report uses elements in the **Original Group Information and Status** to capture the message identifier and message name of the underlying payment the Payment Status Report relates to. The mandatory *Original Message Identification* contains the point-to-point reference, and the mandatory **Original Message Name Identification** contains the message name of the underlying payment being reported upon. Optionally the **Original Creation Date Time** can also be captured.

For example:

*Original Message Name Identification*

"pain.001.001.09" confirms the Status Report is of a pain.001 Customer Credit Transfer Initiation.

Original Message Identification must transport the Message Identification of the underlying payment (e.g., pain.001).

For a relay scenario, Forwarding Agent (F) should respect the Message ID provided by the Initiating Party of the pain.001 and pain.002.

| pain.001 | | Interbank pain.001 | |
|---|---|---|---|
| Message Identification | abcd1234 | Message Identification | abcd1234 |
| | | | |
| pain.002 | | Interbank pain.002 | |
| Message Identification | xyz9875 | Message Identification | xyz9875 |
| Original Message Identification | abcd1234 | Original Message Identification | abcd1234 |
| Original Message | | Original Message | |

---

<!-- Page 117 -->

## Identification

Min 1 – Max 1

The pain.002 Customer Payment Status Report uses element ***Original Payment Information Identification***, located in the Original Group Information and Status. This 35 character identifier is a point-to-point reference used to unambiguously identify the payment information group or batch reference if the message contains multiple transactions.

Since the interbank pain.001 and pain.002 usage guidelines are restricted to one single transaction, this value is the same as the Original Message ID of the Original Group Information And Status.

Original Payment Information and Status
Original Payment Information Identification

---

<!-- Page 118 -->

The pain.002 *Customer Payment Status Report* nested **Transaction Information And Status** element is used to capture information from the underlying payment that the *Payment Status Report* relates to.

| | |
|---|---|
| **Mandatory** element (in addition to *Original Message identification* and *Original Message Name Identification* described on the previous pages) include: | |
| **Original End to End Identification** | Min 1 – Max 1 |
| **Original UETR** | Min 1 – Max 1 |
| The following element is optional: | |
| **Original Instruction Identification** | Min 0 – Max 1 |

These *Original* elements enable the **Initiating Party** to associate the Payment Status with the payment they originally sent.

> Original Payment Information and Status
> Transaction Information and Status
> > Original End to End Identification
> > Original UETR

---

<!-- Page 119 -->

## Information

Min 1 – Max 1

The *pain.002 Customer Payment Status Report* **Transaction Status** utilizes the externalized ISO *Payment Transaction Status* code list to provide a status update on a *pain* message previously received. The *Transaction Status* element is arguably the most significant/core parts of the *pain.002* and optionally may further be complemented with **Status Reason Information**.

Min 0 – Max 1

The nested **Status Reason Information** enable the optional inclusion of:

**Originator** – the party that issues the status. Typically, the *pain.002* Initiating Party and therefore Originator is not necessary.

**Reason** – which utilises an ISO external Status Reason code. For example, **AC04** ‘Closed Account Number’ would complement a RJCT (Reject) Transaction Status.

**Additional Information** – a text element to provide further status reason information, necessary where the *Reason* code is NARR

Note: A *Reason* code must be provided where the **Transaction Status** RJCT (Reject) code is used.

---

<!-- Page 120 -->

| Code | Name | ISO Definition | High Level Use Case |
| :--- | :--- | :--- | :--- |
| ACCC | AcceptedSettlementCompleted | Settlement on the creditor's account has been completed. | Sent by **Creditor Agent** to confirm the settlement on the creditor's account |
| ACCP | AcceptedCustomerProfile | Preceding check of technical validation was successful. Customer profile check was also successful. | Sent by **any Agent** in the payment chain to confirm acceptance prior to technical validation. |
| ACFC | AcceptedFundsChecked | Preceding check of technical validation and customer profile was successful and an automatic fundscheck was positive. | Sent by **any Agent** in the payment chain to confirm the technical validation/ profile w as positive and automatic funds check was **positive**. |
| ACIS | AcceptedAndChequeIssued | Payment instruction to issue a cheque has been accepted, and the cheque has been issued but not yet been deposited or cleared. | Sent by **any Agent** in the payment chain to confirm a cheque has been issued as requested. |
| ACSC | AcceptedSettlementCompleted | Settlement has been completed. | Sent by the **Any Agent** to confirm settlement of a payment message leg. |
| ACSP | AcceptedSettlementInProcess | All preceding checks such as technical validation and customer profile were successful and therefore the payment initiation has been accepted for execution. | Sent by **any Agent** to the to confirm the payment is accepted following technical validations being successfully completed. |
| ACTC | AcceptedTechnicalValidation | Authentication and syntactical and semantical validation are successful | Sent by **any Agent** in the payment chain to the previous Agent to confirm the payment is accepted following technical validations being successfully completed. |
| ACWC | AcceptedWithChange | Instruction is accepted but a change will be made, such as date or remittance not sent. | Sent by **any Agent** in the payment chain to the previous Agent to confirm the payment is accepted following amendments being made. |
| ACWP | AcceptedWithoutPosting | Payment instruction included in the credit transfer is accepted without being posted to the creditor customer's account. | Sent by **Creditor Agent** to the previous Agent to confirm the acceptance of payment w ithout settlement on the creditor's account. |
| CPUC | CashPickedUpByCreditor | Cash has been picked up by the Creditor. | Sent by **Creditor Agent** to the previous Agent to confirm that the cash collection has been picked up by the Creditor. |
| PDNG | Pending | Payment instruction or individual transaction included in the payment initiation is pending. Further checks and status update will be performed. | Sent by **any Agent** in the payment chain to the previous Agent as an interim status w hilst other validations are performed. |
| RCV D | Received | Payment initiation has been received by the receiving agent. | Sent by **Any Agent** to the previous Agent as confirmation that their Customer |

---

<!-- Page 121 -->

The interbank pain.002 *Customer Payment Transaction Status* element facilitates updates from the *Debtor Agent* to the previous Agent, e.g., the *Forwarding Agent* or the payment originator (the *Debtor* / the *Initiating Party*) on changes to the status of the payment. Such Status Information messages (pain.002), with the exception of **reject code RJCT** which **is mandatory in CBPR+**, are bilateral agreed, where upon a variety of these Transaction Statuses may be used by the Instructed Agent at different stages of the payment processing.

This diagram illustrates the logical order in which these codes may be used during the processing of the Payment Initiation messages (pain) and the interbank Payment Clearing And Settlement message (pacs) and the role of the Agents in providing these status.

**Any Agent**

| Code |
| :--- |
| RCVD |
| ACTC |
| ACCP |
| ACFC |
| RJCT | ACWC |
| ACIS |
| ACSP |

PDNG

**Creditor Agent**

| Code |
| :--- |
| CPUC |
| ACWP |
| ACCC |

---

<!-- Page 122 -->

> Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases.

**Interbank Customer Payment Status Report – Relay**
Use Case pn.2.1.1 – High Level Payment Initiation Interbank ‘relay’ status report
Use Case pn.2.1.1.a – High Level Payment Initiation Interbank ‘relay’ status report Multi-bank Sweep
Use Case pn.2.1.2 – High Level Payment Initiation Interbank ‘relay’ status report involving a Payment Market Infrastructure
Use Case pn.2.1.3 – High Level Direct Debit Initiation Interbank ‘relay’ status report involving a Payment Market Infrastructure

**Interbank Customer Payment Status Report – Authorised Party**
Use Case pn.2.2.1 – High Level Payment Initiation Interbank status report for Authorised Party
Use Case pn.2.2.1.a – High Level Payment Initiation Interbank status report for FI-Initiated Sweep (Long position at the Secondary Account)
Use Case pn.2.2.1.b – High Level Payment Initiation Interbank status report for Authorised Party to pay themselves as the Creditor.

**Interbank Customer Payment Status Report – Financial Institution**
Use Case pn.2.3.1 – High Level Payment Initiation Interbank status report for Financial Institution Payment Initiation

**Interbank multiple Payment Status Reports**
Use Case pn.2.4.1 – High Level Payment Initiation Interbank ‘relay’ multiple status reports
Use Case pn.2.4.2 – High Level Rejection of an incomplete ‘relay’ Payment
Use Case pn.2.4.3 – High Level Direct Debit Initiation Interbank ‘relay’ multiple status reports involving a Payment Market Infrastructure

---

<!-- Page 123 -->

In the interbank relay scenario, the Debtor Agent sends the pain.002 message to the Forwarding Agent which relays the same information to the Initiating Party.

1. Initiating Party
   - pain.001
   - pain.002
2. Forwarding Agent (F)
   - Interbank pain.001
   - Interbank pain.002
3. Debtor Agent (A)
   - pacs.008
4. Creditor Agent (B)
   - camt.053
5. Creditor Party

1. Initiating Party sends a payment instruction to the Forwarding Agent
2. Forwarding Agent (F) forwards the payment instruction to the Debtor Agent (A)
3. Debtor Agent (A) debits the account of Debtor and initiates a credit transfer by forwarding a local credit transfer message pacs.008
3a. Debtor Agent (A) provides a status update ACSP (accepted settlement in progress) to the
3b. Forwarding Agent (F) relays the status ACSP (accepted settlement in progress) to the Initiating Party, based upon a bilateral agreement
4. Creditor Agent (B) receives the credit transfer message, credits the Creditor, and sends a camt.053

---

<!-- Page 124 -->

# Multi-bank Sweep

In the interbank relay scenario, the Debtor Agent sends the pain.002 message to the Forwarding Agent which relays the same information to the Initiating Party.

**Diagram Flow:**
*   **1** → `pain.001` → **F** (Bank)
*   **2** → `Interbank pain.001` → **A** (Bank)
*   **3** → `pacs.008` → **B** (Bank)
*   **4** → `camt.053` → **Initiating Party**
*   **3a** (from A) → `Interbank pain.002` → **F**
*   **3b** (from F) → `pain.002` → **1**

| **1** | **3** | **3b** |
| :--- | :--- | :--- |
| Initiating Party sends a payment instruction to the Forwarding Agent to sweep excess funds from its subsidiary's account to the master account with Bank B | Debtor Agent (A) debits the account of Debtor and initiates a credit transfer by forwarding a local credit transfer message pacs.008 | Forwarding Agent (F) relays the status ACSP (accepted settlement in progress) to the Initiating Party, based upon a

---

<!-- Page 125 -->

# a Payment Market Infrastructure

In the interbank relay scenario, the Debtor Agent sends the pain.002 message to the Forwarding Agent which relays the same information to the Initiating Party.

**Flow Diagram:**

1. Initiating Party → `pain.001` → 2. Forwarding Agent (F) → `Interbank pain.001` → 3. Debtor Agent (A) → `pacs.008` → Creditor Bank → `pacs.008` → 4. Creditor Agent (B) → Creditor Party
   - 2. Forwarding Agent (F) → `Interbank pain.002` (3b) → 1. Initiating Party (`pain.002`)
   - 3a. Debtor Agent (A) → 3b. Forwarding Agent (F)

**Legend:**

| Step | Description |
| :--- | :--- |
| **1** | Initiating Party sends a payment instruction to the Forwarding Agent |
| **2** | Forwarding Agent (F) forwards the payment instruction to the Debtor Agent (A) |
| **3** | Debtor Agent (A) debits the account of Debtor and initiates a credit transfer by forwarding a local credit transfer message pacs.008 to a Payment Market Infrastructure (PMI) |
| **3a** | Debtor Agent (A) provides a status update ACSP (accepted settlement in progress) to the Forwarding Agent (F), based upon a bilateral |
| **3b** | Forwarding Agent (F) relays the status ACSP (accepted settlement in progress) to the Initiating Party, based upon a bilateral agreement |
| **4** | Creditor Agent (B) receives local credit transfer message via the Payment Market Infrastructure and credits the Creditor |

---

<!-- Page 126 -->

# involving a Payment Market Infrastructure

In the interbank relay scenario, the Creditor Agent sends the pain.002 message to the Forwarding Agent which relays the same information to the Initiating Party.

4

3

2

1

B

A

F

Interbank pain.008

pain.008

pain.002

Interbank pain.002

3a

3b

pac s.003

pac s.003

1

Initiating Party sends a direct debit instruction to the Forwarding Agent

3

Creditor Agent (A) instructs a direct debit transaction by sending a local direct debit message pacs.003 to a Payment Market Infrastructure

3b

Forwarding Agent (F) relays the status ACSP (accepted settlement in progress) to the Initiating Party, based upon a bilateral agreement

2

Forwarding Agent (F) forwards the payment instruction to the Creditor Agent (A)

3a

Creditor Agent (A) provides a status update ACSP (accepted settlement in progress) to the Forwarding Agent (F), based upon

4

Debtor Agent (B) receives a local direct debit message via the Payment Market Infrastructure and debits the account of the Debtor

---

<!-- Page 127 -->

# Party

In the scenario Authorised Party Initiation, the Debtor Agent sends the pain.002 message to the Financial Institution which initiated a payment based on Debit Authorisation with the Debtor and the Debtor Agent.

**Diagram flow:**

- **DA** → Debit Authorisation
- **1** (Debtor) → **2** (Agent I) → Interbank pain.001 → **3** (Agent A) → pacs.008 → **4** (Agent B) → camt.053 → (Creditor)
- **3a** (Agent A) → Interbank pain.002 → (Agent I)
- pacs.002 (Agent B → Agent A)

**Step descriptions:**

- **DA** – As a pre-requisite the Debtor provides Debit Authorisation to Agent I to initiate Payment from their account with the Debtor Agent (A)
- **2** – Agent (I) initiates a payment request (pain.001) to the Debtor Agent (A) to move fund from the Debtor's account, as an
- **3** – Debtor Agent (A) debits the account of Debtor and initiates a credit transfer
- **3a** – Debtor Agent (A) optionally provides a status update to the Initiating Party (Agent I), based upon a bilateral agreement
- **4** – Creditor Agent (B) receives credit transfer message, credits the Creditor and optionally provided a status report to Debtor Agent based upon a bilateral agreement. It also sends the result of the sweep by camt.052 (intraday sweep) and or camt.053 (statement) to the Corporate

---

<!-- Page 128 -->

# Party: FI-Initiated Sweep (Long position at the Secondary Account)

In the scenario Authorised Party Initiation, the Debtor Agent sends the pain.002 message to the Financial Institution which initiated a liquidity sweep on behalf of a corporate customer based on the sweep contract

Sweep Contract → ① → ② → camt.052 → ① → ③ → ④

- ① Interbank pain.001
- ③a Interbank pain.002
- ③ pacs.008
- ④ pacs.002
- ④ camt.053

**1** Agent I receives intraday balance *report* from the Debtor Agent (A) on behalf of their mutual customer

**2** Agent (I) initiates a sweep on behalf of the Corporate by sending pain.001 to the Debtor Agent

**3** Debtor Agent (A) debits the account of Debtor and initiates a credit transfer

**3a** Debtor Agent (A) optionally provides a status update to the Initiating Party (Agent I), based upon a bilateral agreement

**4** Creditor Agent (B) receives credit transfer message, credits the Creditor, and sends a camt.053 (statement) at the end of the business day to the Creditor. An optional status report is sent to the previous Agent based upon a bilateral agreement

> See use case p.8.1.2 for a sweeping contract with a short position

---

<!-- Page 129 -->

# Party to pay themselves as the Creditor

In the scenario Authorised Party Initiation, the Initiating Party (Agent I) initiates a payment from the Debtor's account based on Debit Authorisation already in place to move money to themselves as the Creditor

**Diagram flow:**

- **DA** → Debit Authorisation
- **2** → Interbank pain.001 → (Debtor Agent I) → (Creditor Agent A)
- **3a** ← Interbank pain.002
- **3** → pacs.008 → (Creditor Agent B)
- **4** ← pacs.002
- **4** → camt.053 → (Creditor Agent I)

**Step descriptions:**

| Step | Description |
|------|-------------|
| **DA** | As a pre-requisite the Debtor provides Debit Authorisation to Agent I to Initiate Payment from their account with the Debtor Agent (A) |
| **2** | Agent (I) initiates a payment request (pain.001) to the Debtor Agent (A) to move fund from the Debtor's account, as an authorised party, to |
| **3** | Debtor Agent (A) debits the account of Debtor and initiates a credit transfer |
| **3a** | Debtor Agent (A) optionally provides a status update to the Initiating Party (Agent I), based upon a bilateral agreement |
| **4** | Creditor Agent (B) receives the credit transfer message, credits the Creditor, and sends a camt.053 (statement) at the end of the business day to the Creditor. An optional status report is sent to the Debtor Agent based upon a bilateral agreement |

---

<!-- Page 130 -->

# Institution Payment Initiation

In the scenario Financial Institution Payment Initiation, the Debtor Agent sends the pain.002 message to the Financial Institution which initiated a payment to a non-Financial Institution Creditor using their own account

```
[I] --Interbank pain.001--> [A] --pacs.008--> [B] --camt.053--> (Creditor)
  ^                           |
  |                           |
  +--Interbank pain.002 (2a)--+
                              +--pacs.002-->
```

**1** Agent (I), the Debtor, initiates a payment request (pain.001) to the Debtor Agent (A) to move funds from their own account

**2** Debtor Agent (A) debits the account of Agent (I), the Debtor and initiates a credit transfer

**3** Creditor Agent (B) receives credit transfer message, credits the Creditor, and optionally returns a status report to Debtor Agent based upon a bilateral agreement. It also sends camt.053 (statement) to the non-FI Creditor

**2a** Debtor Agent (A) optionally provides a status update to the Initiating Party (Agent I), based upon a bilateral agreement

---

<!-- Page 131 -->

In the interbank relay scenario, the Forwarding Agent provides multiple Payment Status Information updates (with different Transaction Status codes) where bilaterally agreed, throughout the payment processing lifecycle.

**Diagram Flow Labels:**
*   pain.001 (1)
*   Interbank pain.001 (2)
*   Interbank pain.002 (3)
*   Interbank pain.002 (4a)
*   pacs.008 (4)
*   camt.053 (5)
*   pain.002 (3a)
*   pain.002 (4b)

| Step 1 | Step 3 | Step 4 | Step 4b |
| :--- | :--- | :--- | :--- |
| **1**<br>Initiating Party sends a payment instruction to the Forwarding Agent | **3**<br>Debtor Agent (A) optionally provides a status update ACTC (accepted technical validations are successful) to the Forwarding Agent (F), based upon a bilateral agreement. | **4**<br>Debtor Agent (A) processes the payment and sends to the Creditor Agent (B) | **4b**<br>Forwarding Agent (F) relays a further status update ACSP (accepted settlement in progress), to the Initiating Party, based upon a bilateral agreement. |
| **2**<br>Forwarding Agent (F) forwards the payment instruction to the Debtor Agent (A) | **3a**<br>Forwarding Agent (F) relays the status ACTC (accepted technical | **4a**<br>Debtor Agent (A) optionally provides a further status update ACSP (accepted settlement in progress), to the Forwarding Agent | **5**<br>Creditor Agent (B) processes the |

---

<!-- Page 132 -->

In the interbank relay scenario, the Forwarding Agent provides multiple Payment Status Information updates (with different Transaction Status codes) where bilaterally agreed, throughout the payment processing lifecycle.

1 → pain.001 → 2 (F) → Interbank pain.001 → 3 (A) → pacs.008 → (B) → (Initiating Party / Creditor Agent)

3b ← pain.002 ← (F)
3a ← Interbank pain.002 ← (A)
4b ← pain.002 ← (F)
4a ← Interbank pain.002 ← (A)
pacs.002 ← (B)

+ Reject Reason | + Reject Reason | + Reject Reason

Where a **payment is rejected**, the use of the pain.002 status RJCT (Reject) with the ISO Status Reason Code is **mandatory**.

| 1 | Initiating Party sends a payment instruction to the Forwarding Agent |
|---|---|
| 2 | Forwarding Agent (F) relays the payment to the Debtor Agent (A) |
| 3 | Debtor Agent (A) processes the payment and sends to the Creditor Agent (C) |
| 3a | Debtor Agent (A) optionally provides a status update ACSP |
| 3b | Forwarding Agent (F) relays the status ACSP (accepted settlement in progress) to the Initiating Party, based upon a bilateral agreement. |
| 4a | Debtor Agent refund the Debtor's account and update the status RJCT with the reason code to the Forwarding Agent |
| 4b | Forwarding Agent (F) relays a further status update RJCT with |

---

<!-- Page 133 -->

## (pain.002) involving a Payment Market Infrastructure

In the interbank relay scenario, the Creditor Agent sends multiple status reports to the Forwarding Agent which relays the same information to the Initiating Party.

**Sequence diagram (left to right):**

- **3** — `pacs.003` / `pacs.002` (Creditor Agent B ↔ PMI)
- **3** — `pacs.003` / `pacs.002` / `pacs.002` (PMI ↔ Creditor Agent A)
- **3a** — `Interbank pain.002` (Creditor Agent A → Forwarding Agent F)
- **4a** — `Interbank pain.002` (Creditor Agent A → Forwarding Agent F)
- **2** — `Interbank pain.008` (Forwarding Agent F ↔ Creditor Agent A)
- **1** — `pain.008` / `pain.002` / `pain.002` (Forwarding Agent F ↔ Initiating Party)
- **3b** — `pain.002` (Forwarding Agent F → Initiating Party)
- **4b** — `pain.002` (Forwarding Agent F → Initiating Party)

> Where a direct debit is **rejected/returned**, the use of the pain.002 status RJCT (Reject) with the ISO Status Reason Code is **mandatory**.

**+ Reject Reason** (Creditor Agent B) · **+ Reject Reason** (Creditor Agent A) · **+ Reject Reason** (Forwarding Agent F)

**Step legend:**

| # | Description |
|---|-------------|
| 1 | Initiating Party sends a direct debit instruction to the Forwarding Agent |
| 2 | Forwarding Agent (F) forwards the payment instruction to the Creditor Agent (A) |
| 3 | Creditor Agent (A) instructs a direct debit transaction by sending a local direct debit message pacs.003 to a Payment Market Infrastructure (PMI) |
| 3a | Creditor Agent (A) provides a |
| 3b | Forwarding Agent (F) relays the status ACSP (accepted settlement in progress) to the Initiating Party, based upon a bilateral agreement |
| 4 | Having received the direct debit, PMI |
| 4a | Creditor Agent update the status RJCT with the reason code to the Forwarding Agent |
| 4b | Forwarding Agent (F) relays a |

---

<!-- Page 134 -->

# Interbank Customer
# Direct Debit Initiation

---

<!-- Page 135 -->

**ISO** ISO 2022 message element ➔ **MT** MT Field Name & Tag option

**Group Header**
> **Message Identification**
> **Initiating Party** – where different from **Creditor**
> **Forwarding Agent**

**Payment Information**
> **Payment Information Identification**
> **Requested Collection Date**
> **Creditor**
> **Creditor Agent**

**Direct Debit Transaction Information**
> **Payment Identification**
> **Instructed Amount**
> **Charge Bearer**
> **Mandate Identification**
> **Debtor Agent**
> **Debtor**

**Sequence A – General Information:**
> **Sender's Reference** (Field 20)
> **Instructing Party** (Field 50 C or L)

Message **Sender** in a 'relay' scenario

**Sequence A – General Information:**
> **Customer Specified Reference** (Field 21R)
> **Requested Execution Date** (Field 30)
> **Creditor** (Field 50 A or K)*
> **Creditor's Bank** (Field 52 A, C or D)*

**Sequence B – Transaction Details:**
> **Transaction Reference** (Field 21)
> **Currency and Transaction Amount** (Field 32B)
> **Details of Charges** (Field 71A)
> **Mandate Reference** (Field 21C)
> **Debtor's Bank** (Field 57 A, C or D)
> **Debtor** (Field 59 no letter or A)

---

<!-- Page 136 -->

```
┌─────────────────┐
│    pain.008     │
└─────────────────┘
        │
        ├── Group Header
        │
        ├── Payment Information
        │
        └── Direct Debit Transaction Information
```

The pain.008 message is composed of three blocks:

- **Group Header** contains a set of characteristics that relates to all individual transaction.
- **Payment Information** contains a set of characteristics that relates to the credit side of the transaction, such as Creditor and Creditor Agent.
- **Direct Debit Transaction Information** contains, among others, elements related to the debit side of the transaction, such as Debtor and Debtor Agent and optionally mandate related information.

Direct Debit Initiation relay messages in a many-to-many space allow for multiple transactions as they will be typically cleared by Automated Clearing House (ACH) batch processing system

---

<!-- Page 137 -->

Debtor — Debtor Agent (B) — Creditor Agent (A) — Forwarding Agent (F) — Initiating Party — Creditor

- **Interbank pain.008** (blue arrow, Forwarding Agent → Creditor Agent)
- **pain.008\*\*** (Initiating Party → Forwarding Agent)
- **pain.002** (dashed, Forwarding Agent → Initiating Party)
- **Interbank pain.002** (dashed, Creditor Agent ↔ Forwarding Agent)
- **pacs.003** (Debtor Agent → Creditor Agent)
- **pacs.002** (dashed, Creditor Agent → Debtor Agent)
- **camt.053** (Debtor Agent → Debtor)

\*Initiating Party may alternative represent an authorised party such as a head office
\*\*or other proprietary method for instructing a direct debit initiation request.

Interbank Customer Direct Debit Initiation message is sent by the Initiating Party to the Forwarding Agent or the Creditor Agent. It is used to request single or bulk collection(s) of funds from one or various debtor's account(s) to a creditor.

**Relay:** Interbank pain.008 message is sent by the Initiating party (the Creditor or authorised party) to the Forwarding Agent which acts as a concentrating financial institution. It will forward the pain.008 message to the Creditor Agent to initiate the direct debit instruction(s).

---

<!-- Page 138 -->

# Group Header

---

<!-- Page 139 -->

pain.008 Interbank Customer Direct Debit Initiation – Message Identification

Min 1 – Max 1

Each ISO20222 payment message has a **Message Identification** element, located in the Group Header. This **35 character** identifier is a point-to-point reference used to unambiguously identify the message.

For the Payment Initiation (pain) messages the *Message Identification* has no exact equivalent in the legacy MT payment message. However, the Sender's Reference (Field 20) could be considered as a similar comparison where a pain message contains a single Transaction.

> Each transaction's *Direct Debit Transaction Information* contains a variety of nested *Payment Identification* elements to capture reference related to the individual transaction such as a UETR (Unique End-to-end Transaction Reference).

> For a relay scenario, Forwarding Agent should respect the Message ID provided by the Initiating Party (Creditor or authorized third party) of the pain.008.

---

<!-- Page 140 -->

pain.008 Interbank Customer Direct Debit Initiation – Creation Date Time

Min 1 = Max 1

The pain.008 message *Creation Date Time* captures the date and time which the message was created.

It is defined by *ISO Date Time* with mandatory date and time components expressed in the following formats:

1. Universal Time Coordinated (UTC) time YYYY-MM-DDThh:mm:ss.sssZ
2. Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
3. Local time format YYYY-MM-DDThh:mm:ss.sss

Unlike other CBPR+ messages, the interbank pain.008 message is more flexible in defining the date and time elements. The most recommended representation is Local time with UTC offset which was mandated by CBPR+ (2ⁿᵈ option). Otherwise use UTC time (1ˢᵗ option). Decimal fractions of milliseconds with 3 digits are optional.

---

<!-- Page 141 -->

pain.008 Interbank Customer Direct Debit Initiation – Authorisation

Min 0 – Max 2

The pain.008 message **Authorisation** allows the Initiating Party to specify if a file requires either File Level or Transaction Level approval by additional security provisions, such as digital signature or user key. The *Authorisation* uses an embedded code set or free text form. It has no equivalent in the legacy MT direct debit message.

| Code | Description | Description |
| :--- | :--- | :--- |
| ILEV | Instruction Level Authorisation | File requires all customer transactions to be authorised or approved. |
| FDET | File Level Authorisation Details | Additional file level approval, with the ability to view both the payment information block and supporting transaction detail. |
| FSUM | File Level Authorisation Summary | Additional file level approval, with the ability to view only the payment information block. |
| AUTH | Pre Authorised File | File has been pre-authorised or approved within the originating customer environment and no further approval is required. |

For single transactions in the CBPR+ usage guidelines, the most applicable code will be ILEV for Instruction Level Authorisation. The use of Authorisation is only allowed when bilaterally agreed.

---

<!-- Page 142 -->

pain.008 Interbank Customer Direct Debit Initiation – Number of Transactions

Min 1 – Max 1

The pain.008 message *Number of Transactions* captures the number of individual transaction contained within the message.

> Multiple transactions are allowed in CBPR+ direct debit usage guidelines. However, it is recommended to have only one single direct debit transaction unless bilaterally determined.

> Single transactions in the CBPR+ direct debit usage guidelines enable a transaction to be managed and unlocks highly automated, frictionless, instant collection, supporting the next generation of innovation.

Group Header: Number of Transactions

---

<!-- Page 143 -->

# pain.008 Interbank Customer Direct Debit Initiation – Initiating Party

**Initiating Party**

**Creditor**

**Authorised Party**

**Forwarding Agent / FI**

Min 1 – Max 1

The **Initiating Party** can either be the **Creditor** or an Authorised Party who initiates direct debit transactions on behalf of the *Creditor*. The Initiating Party can be, for example, the Head Office which is authorised by its subsidiary to request for payment amount to be collected from the *Debtor*. In the centralization model, the *Initiating Party* can also be a payment factory or shared service centre or third party agent, which has authority to send the message on behalf of the *Creditor*.

In the interbank pain.008 'Relay' message use case: The *Initiating Party* sends the pain.008 message to the **Forwarding Agent** which acts as a concentrating financial institution. It will forward the pain.008 message to the **Creditor Agent**.

Initiating Party has a mandate (debit authority agreement) to debit the account of the Debtor.

---

<!-- Page 144 -->

# pain.008 Interbank Customer Direct Debit Initiation – Initiating Party

The *Initiating Party* can either be the *Creditor* or an authorised party, such as Financial Institution, in the context of interbank pain.008. Sub elements describe the *Initiating Party* in greater detail.

**Postal Address**
*   Department
*   Sub Department
*   Street Name
*   Building Number
*   Building Name
*   Floor
*   Post Box
*   Room
*   Post Code
*   Town Name
*   Town Location Name
*   District Name
*   Country Sub Division

Nested element capturing *structured* Postal Address including at least Town Name and Country if used.

Nested element capturing the various types of identifiers, e.g. BIC, LEI etc.

Optional element to capture the Initiating Party's ISO country code of residence

**Diagram Nodes:**
*   **Name**: Mandatory *Name* where Postal Address is provided.
*   **Postal Address**
*   **Identification**
*   **Country of Residence**
*   **Contact Details**
*   **Initiating Party**

---

<!-- Page 145 -->

# pain.008 Interbank Customer Direct Debit Initiation – Forwarding Agent

**Min 1 – Max 1**

The ***Forwarding Agent*** is mandatory in a relay scenario whereby the *Initiating Party* (the *Creditor* or authorised third party) has to provide ***Business Identifier Code*** (BICFI) of the *Forwarding Agent* in the pain.008 message. The Forwarding Agent acts as a concentrating financial institution and forwards the pain.008 message to the *Creditor Agent* for execution.

Other options to complement the identity of the ***Forwarding Agent*** include:

* Clearing System Member ID
* LEI (Legal Entity Identifier)

**Diagram nodes:**

* BICFI
* Clearing System Member Id
* Clearing System Id
* LEI
* Various sub-element
* Financial Institution Identification

---

<!-- Page 146 -->

# Payment Information

---

<!-- Page 147 -->

The CBPR+ pain.008 Interbank Usage Guideline aligns to the Usage Guideline of CGI-MP, to remain interoperable. It is important to recognise that the CGI Postal Address allows the Postal Address information to be captured as both structured and unstructured (address line) data, of which the Country Code within the Postal Address is mandatory.
As a payment initiation could instruct various types of Payment Methods settled across various Clearing Methods, it should also be recognized that the Usage Guideline specification of those instructions need to be adhered to, which may need some enrichment or repair of the data from the payment initiation message.
Postal Address is a good example of such data enrichment or repair, where many domestic payment methods exclusively support unstructured postal addresses. Likewise, CBPR+ and HVPS+ payments consider structured and unstructured postal addresses to be mutually exclusive. i.e., only one or the other may be used.

**CGI-MP** payment Initiation/
**CBPR+** payment initiation interbank

Structured Unstructured

pain.008

Unstructure

Many domestic proprietary payments

Structured Unstructured **CBPR+** payments

---

<!-- Page 148 -->

Min 1 – Max 1

The Interbank Customer Direct Debit Initiation **Payment Information Identification** provides a mandatory element to identify the payment information group within the message.

This 35 character identifier is a point-to-point reference used to unambiguously identify the payment information group within the message. It is also known as a batch reference number if the message contains multiple transactions.

For a single batch in the CBPR+ usage guidelines, the value in Payment Information Identification is the same as the Message Identification of the Group Header.

---

<!-- Page 149 -->

Min 1 - Max 1

The pain.008 message **_Payment Method_** specifies the means of payment that will be used to move the amount of money. The payment method code "DD" Direct Debit must be used.

| Code | Name | Definition |
| :--- | :--- | :--- |
| DD | Direct Debit | Collection of an amount of money from the Debtor's bank account by the Creditor. The amount of money and dates of collections may vary. |

---

<!-- Page 150 -->

Min 0 – Max 1

The pain.008 message ***Batch Booking*** identifies whether a single entry per individual transaction or a batch entry for the sum of the amounts of all transactions within the group of a message is requested.

> Batch booking is used to request for a consolidated credit entry on the Creditor's account.
> Where this optional element is not used, the default of single credit entries is applied on the Creditor's account.

Payment Information > Batch Booking

---

<!-- Page 151 -->

# pain.008 Interbank Customer Direct Debit Initiation – Requested Collection Date

Min 1 – Max 1

The pain.008 message mandatory **_Requested Collection Date_** element, captures the date at which the creditor requests that the amount of money is to be collected from the debtor.

It is defined by **_ISO Date_** expressed in the **_YYYY-MM-DD format._**

---

<!-- Page 152 -->

The ISO 2022 pain messages describe the *Creditor* as the party whose account was credited for a transaction. The *Creditor* sub elements describe the *Creditor* in greater detail.

`Min 1 – Max 1`

Mandatory **Name** (where a BIC identifier is not provided) by which the party is known

**Name**

**Postal Address**

- Department
- Sub Department
- Street Name
- Building Number
- Building Name
- Floor
- Post Box
- Room
- Post Code
- Town Name
- Town Location Name
- District Name
- Country Sub Division
- Country — `Code`
- Address Line

Nested element capturing either structured or unstructured *Creditor* address details.

Note: Structured address is strongly recommended with mandatory Town Name and Country

**Postal Address**

Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc.

**Identification**

# *Creditor*

Optional element to capture the *Creditor*'s ISO country code of residence

**Country of Residence**

---

<!-- Page 153 -->

The pain.008 *Creditor Account* is used to capture the account information for which credit entry will be made as a result of the transaction, which will be also reflected in their account Statement.

The *Creditor Account* uses a variety of nested elements to capture information related to the account.

Min 1 – Max 1 *Identification* identifies the account maintained at the Creditor Agent (Account Servicing Institution)

Min 0 – Max 1 *Type* uses the external Cash Account Type code list to identify the type of account

Min 0 – Max 1 *Currency* identifies the currency of the account, recommended.

Min 0 – Max 1 *Name* identifies the name of the account as assigned by the Creditor Agent (Account Servicing Institution)

Min 0 – Max 1 *Proxy* captures an alternative identification of the account number such as an email address. This element has further nested *Type* which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used.

Indication of Currency of the Creditor Account is recommended in case of multi-currency accounts

---

<!-- Page 154 -->

Min 1 – Max 1
The **Creditor Agent** is a static role in the pain.008 Customer Direct Debit Initiation. This agent maintains a relationship with their customers, the *Creditor*.

Note: Although the **Creditor Agent, Debtor Agent, Creditor and Debtor** all maintain static roles in the pain messages, the description of these parties change in reporting messages (camt) where the Creditor Agent and Debtor Agent become the Statement Account Servicer and the Creditor and the Debtor become the Statement Account Owner. This will be explored further in the camt Cash Management Reporting section.

For Agent Identification, BIC is preferred, alternatively Clearing Member ID together with Name and Address may be provided

---

<!-- Page 155 -->

Min 0 – Max 1
The pain.008 *Creditor Agent Account* is used to capture the account information related to the Creditor Agent.

The *Creditor Agent Account* uses a variety of nested elements to capture information related to the account.

Min 1 – Max 1 *Identification* identifies the account maintained at the Account Servicing Institution
Min 0 – Max 1 *Type* uses the external Cash Account Type code list to identify the type of account
Min 0 – Max 1 *Currency* identifies the currency of the account
Min 0 – Max 1 *Name* identifies the name of the account as assigned by the Account Servicing Institution
Min 0 – Max 1 *Proxy* captures an alternative identification of the account number such as an email address. This element has further nested *Type* which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used.

Creditor Agent and Debtor Agent are Financial Institutions, therefore the nested elements *Name* and *Proxy* are unlikely to be used.

---

<!-- Page 156 -->

pain.008 Interbank Customer Direct Debit Initiation – Charges Account

Min 0 – Max 1
The pain.008 optional ***Charges Account*** element, which is used to process charges associated with a transaction.

Charges account should be used when charges have to be booked to an account different from the account identified in debtor's account.

This element is not widely used in the payment industry.

---

<!-- Page 157 -->

# pain.008 Interbank Customer Direct Debit Initiation – Charges Account Agent

`Min 0 – Max 1`

The pain.008 optional *Charges Account Agent* element, which is used to specify the agent that services a charges account.

Charges account agent should only be used when the charges account agent is different from the creditor agent.

This element is not widely used in the payment industry.

Payment Information > Charges Account Agent

---

<!-- Page 158 -->

# Direct Debit Transaction Information

---

<!-- Page 159 -->

Min 1 – Max 1

The pain.008 message contains **Payment Identification** which provides a set of elements to identify the payment of which several are mandatory elements.

## Payment Identification

### Instruction Identification
Min 0 – Max 1

a **point-to-point reference** of 35 characters long will be returned to account statements if provided by the initiating party.

Note: Instruction Id is mandatory in other CBPR+ messages as it maps directly with the mandatory Sender's Reference (Field 20) of the legacy MT payment messages.

### End to End Identification
Min 1 – Max 1

an **end-to-end reference** provided by the *Initiating Party* which must be passed unchanged throughout the payment and reported to the *Creditor*.

note: if the *Initiating Party* has not provided an end-to-end identifier, the *Creditor Agent* may populate "NOT PROVIDED" to comply the mandatory need of this element.

### UETR
Min 1 – Max 1

the **Unique End-to-end Transaction Reference** created using the UUID v4 standard. This reference must be passed unchanged throughout the payment, it may also be created by the Creditor within their Payment Initiation request, and also included in reporting messages.

Direct Debit Transfer Transaction Information

---

<!-- Page 160 -->

The pain message **Payment Type Information** provides a set of optional elements where the payment type can be described.

## Payment Type Information

### Instruction Priority
`Min 0 – Max 1`

A choice of imbedded codes representing the urgency considered by the instructing party. This point-to-point information may be used by the instructed party to differentiate the processing

### Service Level
`Min 0 – Max 3`

A nested element which may either use an external ISO Service Level code or a proprietary code. It is used to identify a particular agreed service level which should be applied to the payment.

### Local Instrument
`Min 0 – Max 1`

A nested element which may either use an external ISO Local Instrument code or a proprietary code. It can be used in combination with Service Level to identify the type of local instrument. For example, CORE is a transaction related to SEPA Direct Debit Core.

> Note: the ISO instrument codes are registered by specific community group (captured in the code list)

### Sequence Type
`Min 0 – Max 1`

A nested element which uses an embedded code to identify the direct debit sequence, such as first, recurrent, final or one-off

### Category Purpose

A nested element which may either use an external ISO Category Purpose code or a proprietary code. It is used to identify the category of payment.

Direct Debit Transfer Transaction Information

---

<!-- Page 161 -->

# pain.008 Interbank Customer Direct Debit Initiation – Instructed Amount

`Min 1 – Max 1`

The pain.008 nested **Instructed Amount** element captures the amount of money to be moved between the Debtor and the Creditor before deduction of charges.

£ $ € ¥

**Instructed Amount**

The *Instructed Amount* captures currency and amount of money to be moved between the Debtor and Creditor, before deduction of charges, expressed in the currency as ordered by the initiating party. This amount has to be transported unchanged through the transaction chain. This element is comparable with both the legacy Field 33B and Field 32B.

🔭 For multiple transactions, the currency must be the same for each transaction.

*Direct Debit Transfer Transaction Information*

---

<!-- Page 162 -->

Min 0 – Max 1
The *Charge Bearer* element exists at the Direct Debit Transaction Information level. It uses an embedded code to specify which party/parties would bear any charges associated with processing the payment transaction. This element is comparable with MT Field 71A ‘Details of Charges’

| **Charge Bearer** (0..1) | **Code** | **Description** | **ISO 20022** |
| :--- | :--- | :--- | :--- |
| | CRED | Creditor | |
| | DEBT | Debtor | |
| | SHAR | Shared | |
| | SLEV | Following Service Level | |

| **71A: Details of Charges** | **Code** | **Description** | **MT 104** |
| :--- | :--- | :--- | :--- |
| | BEN | Beneficiary | |
| | OUR | Our Customer Charges | |
| | SHA | Shared Charges | |

Charge Bearer Code SLEV (Following Service Level) is not allowed in the CBPR+.pain.008 interbank.

Direct Debit Transaction Information

---

<!-- Page 163 -->

pain.008 Interbank Customer Direct Debit Initiation – Direct Debit Transaction

The pain.008 *Direct Debit Transaction* component provides information specific to the direct debit mandate.

**Direct Debit Transaction**

**Mandate Related Information** (Min 0 – Max 1)
Provides further details of the direct debit mandate signed between the creditor and the debtor. E.g., Mandate Identification, Date of Signature and Electronic Signature.

**Creditor Scheme Identification** (Min 0 – Max 1)
Credit party that signs the mandate, may be used if supported by the Direct Debit Schema. (see next page for additional detail on this nested element)

**Pre Notification Identification** (Min 0 – Max 1)
Unique and unambiguous identification of the pre-notification which is sent separately from the direct debit instruction.

**Pre Notification Date**
Date on which the creditor notifies the debtor about the amount and date on

Direct Debit Transaction Information

---

<!-- Page 164 -->

Min 0 – Max 1
The **Creditor Scheme Identification** element within the pain.008 message optionally provides information related to the credit party that signs the mandate who is different from the Creditor.

The **Creditor Scheme Identification** element offers the following options:

Name
Postal Address: Not used often
Identification
Country of Residence
Contact Details

CGI-MP: recommends the use of Creditor Scheme Identification only if supported by the Direct Debit Scheme.

Direct Debit Transaction Information

---

<!-- Page 165 -->

Ultimate Party
Ultimate Debtor
Ultimate Creditor

Min 0 – Max 1
Min 0 – Max 1
The pain.008 message introduces *Ultimate Creditor* and *Ultimate Debtor*. The *Ultimate Creditor* element should not be confused with an *Initiating Party* who may send a direct debit initiation request on behalf of the *Creditor*, for example, Payment Factory.

CBPR+ premise is that an *Ultimate Creditor* has no financial regulated direct account relationship with the corresponding Creditor. Likewise, an *Ultimate Debtor* has no financial regulated account relationship with the corresponding Debtor.

The *Ultimate Creditor* and *Ultimate Debtor* can be identified by a combination of Name and structured address or Organisation ID (e.g., BIC, LEI), Private ID and Country Of Residence.

In the context of direct debit, *Ultimate Creditor* and *Ultimate Debtor* are not commonly used.

Direct Debit Transaction Information

---

<!-- Page 166 -->

Min 1 – Max 1
The **Debtor Agent** is a static roles in the pain.008 Customer Direct Debit Initiation. This agent maintain a relationship with their customers, the *Debtor*.

Note: Although the **Debtor Agent, Creditor Agent, Debtor** and **Creditor** all maintain static roles in the pain messages, the description of these parties change in the reporting messages (camt) where the Debtor Agent and Creditor Agent become the Statement Account Servicer and the Debtor and Creditor become the Statement Account Owner. This will be explored further in the camt Cash Management Reporting section.

Direct Debit Transaction Information

---

<!-- Page 167 -->

The pain.008 **Debtor Agent Account** is used to capture the account information related to the *Debtor Agent*.

The **Debtor Agent Account** uses a variety of nested elements to capture information related to the account.

**Min 1 – Max 1** **Identification** identifies the account maintained at the Account Servicing Institution

**Min 0 – Max 1** **Type** uses the external Cash Account Type code list to identify the type of account

**Min 0 – Max 1** **Currency** identifies the currency of the account

**Min 0 – Max 1** **Name** identifies the name of the account as assigned by the Account Servicing Institution

**Min 0 – Max 1** **Proxy** captures an alternative identification of the account number such as an email address. This element has further nested **Type** which is a choice of external code list or proprietary code and **Identification** which are both mandatory where the Proxy element is used.

Debtor Agent and Creditor Agent are Financial Institutions, therefore

---

<!-- Page 168 -->

Min 1 – Max 1

The ISO 20222 pain messages describes the *Debtor* as the party whose account was debited for a transaction. The *Debtor* sub elements describe the *Debtor* in greater detail.

**Name** by which the party is known

Note: it is recommended to include the Postal Address together with the Name

**Postal Address**

Nested element capturing either structured or unstructured *Debtor* address details.

Note: Structured address is strongly recommended with mandatory Town Name and Country

**Identification**

Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc.

**Country of Residence**

Optional element to capture the *Debtor's* ISO country code of residence

| Postal Address |
| :--- |
| Department |
| Sub Department |
| Street Name |
| Building Number |
| Building Name |
| Floor |
| Post Box |
| Room |
| Post Code |
| Town Name |
| Town Location Name |
| District Name |
| Country Sub Division |
| Country → Code |
| Address Line |

**Debtor**

**Name**

**Postal Address**

**Identification**

**Country of Residence**

---

<!-- Page 169 -->

The pain.008 *Debtor Account* is used to capture the account information for which credit entry will be made as a result of the transaction, which will be also reflected in their account Statement.

The *Debtor Account* uses a variety of nested elements to capture information related to the account.

**Min 1 – Max 1** *Identification* identifies the account maintained at the Creditor Agent (Account Servicing Institution)

**Min 0 – Max 1** *Type* uses the external Cash Account Type code list to identify the type of account

**Min 0 – Max 1** *Currency* identifies the currency of the account

**Min 0 – Max 1** *Name* identifies the name of the account as assigned by the Creditor Agent (Account Servicing Institution)

**Min 0 – Max 1** *Proxy* captures an alternative identification of the account number such as an email address. This element has further nested *Type* which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used.

Direct Debit Transaction Information

---

<!-- Page 170 -->

Ultimate Party
Ultimate Debtor
Ultimate Creditor

Min 0 – Max 1
Min 0 – Max 1

The pain.008 message introduces *Ultimate Debtor* and *Ultimate Creditor*. The *Ultimate Debtor* element should not be confused with an *Initiating Party* who may send a payment initiation request on behalf of the *Debtor*, for example, Payment Factory.

CBPR+ premise is that an *Ultimate Debtor* has no financial regulated direct account relationship with the corresponding Debtor. Likewise, an *Ultimate Creditor* has no financial regulated account relationship with the corresponding Creditor.

The *Ultimate Debtor* and *Ultimate Creditor* can be identified by a combination of Name and structured address or Organisation ID (e.g., BIC, LEI), Private ID and Country Of Residence.

In the context of direct debit, Ultimate Creditor and Ultimate Debtor are not commonly used.

Direct Debit Transaction Information

---

<!-- Page 171 -->

Min 0 – Max 1

The ***Instruction for Creditor Agent*** element within the pain.008 message optionally provides information related to the processing of the direct debit.

The ***Instruction for Creditor Agent*** element offers a maximum of 140 characters to provide further information related to the processing of the direct debit instruction, that may need to be acted upon by the *Creditor Agent*, depending on bilateral agreement.

Direct Debit Transaction Information

---

<!-- Page 172 -->

Min 0 – Max 1

The **Purpose** element within the pain.008 message captures the reason for the payment transaction which may either use an external ISO **Purpose code** or a proprietary code.

The purpose is used to capture the nature of the payment, e.g., **IVPT** Invoice Payment, **FEES** Payment of Fees etc. and should not be confused with Regulatory Reporting codes. By definition this information is typically defined by the *Debtor*.

The externalised Purpose code set is classified by the purpose, for example commercial, for which the numerous codes within the classification are each described by Name and Definition. For example, **LOAR** is classified within the Finance categorisation, with the *Name* **Loan Repayment** described as a repayment of loan to lender.

*Category Purpose* also captures a high level purpose, which unlike *Purpose* is less granular but can trigger special processing e.g. *Category Purpose* code RPRE 'Represented' may trigger a representation of previously reversed or returned direct debit transactions.

Direct Debit Transaction Information

---

<!-- Page 173 -->

Min 0 – Max 10
The *Regulatory Reporting* block within the pain.008 message is nested to capture regulatory and statutory information needed to report to the appropriate authority/s.

Min 0 – Max 1
The *Debit Credit Reporting Indicator* utilises an embedded choice of code to indicate whether the regulatory reporting applies to the:
* DEBT (debit)
* CRED (credit)
* BOTH

Min 0 – Max 1
The *Authority* element captures the *Name* and *Country* code of the Authority/Entity requiring the regulatory reporting information.

Min 0 – Max 9
The *Details* element provides the detail on the regulatory reporting information.

Direct Debit Transaction Information > Regulatory Reporting >
Debit Credit Reporting Indicator
Authority
For the purpose of direct debit, *Regulatory Reporting* is not commonly used.

---

<!-- Page 174 -->

Min 0 - Max 1
The pain.008 nested *Tax* element captures information related to tax. The tax information block is applicable when tax information is used by the clearing or the local regulatory authority(s).

This element caters for two main types of tax related payments:
- Tax payment obligation that is required to be transmitted with a payment
- Information that accompanies an actual payment of a tax obligation

The follow nested elements may be used to capture detailed tax information:

Min 0 - Max 1 | Min 0 - Max 1 | Min 0 - Max 1 | Min 0 - Max 1 | Min 0 - Max 1 | Min 0 - Max 1
---|---|---|---|---|---
Creditor | Debtor | Administration Zone | Reference Number | Method | Total Taxable Base Amount

Min 0 - Max 1 | Min 0 - Max 1 | Min 0 - Max 1 | Min 0 - Max *
---|---|---|---
Total Tax Amount | Date | Sequence Number | Record

Tax information block is also available within the Structured Remittance Information block which is applicable when tax information is used by the creditor as part of remittance information.

---

<!-- Page 175 -->

Min 0 – Max 10

The *Related Remittance Information* element within the pain.008 message is nested to provide information related to the handling of remittance information.

Min 0 – Max 1

The *Remittance Identification* captures a unique reference assigned by the initiating party of the direct debit to identify the remittance information sent separately from the direct debit instruction.

Min 0 – Max 1

The *Remittance Location Details* uses a set of nested elements to provide information on either the location of or the delivery of remittance information.

- *Method* requires a code from an embedded list to detail the method used to deliver the remittance advice information e.g. *EMAIL* (email)
- *Electronic Address* provides an electronic address for which an agent is to send the remittance information to e.g. the email address. It may also reference a URL where remittance information maybe deposited or retrieved.
- *Postal Address* provides the postal address to which an agent is to send the remittance information

Unlike CBPR+ pacs messages, in the interbank pain.008 message, Related Remittance Information and Remittance Information are non-mutually exclusive due to a corporate use case of populating both information blocks for detailing remittance advices which are part of value-added service offered by the *Creditor Agent*.

---

<!-- Page 176 -->

Min 0 – Max 1

The optional **Remittance Information** element within the pain.008 message is nested to provide either **Structured** or **Unstructured** information related to payment, such as invoices.

**Remittance Information** enables the matching/reconciliation of an entry that the payment is intended to settle.

Min 0 – Max 1

The **Unstructured** sub element captures free format *Remittance Information* which is restricted in interbank CBPR+ to 140 characters to ensure backward compatibility with the legacy MT message during coexistence.

Min 0 – Max *

The **Structured** element is nested capturing rich structured *Remittance Information*, and is unlimited in its multiplicity, but must not exceed 9,000 characters of business information (does not include the xml element identification)

The use of this nested element should be bilaterally/multilaterally agreed, to ensure end-to-end transportation of this data.

| Direct Debit Transaction Information |
| :--- |
| > Remittance Information |
| > Structured |

---

<!-- Page 177 -->

The bilaterally/multilaterally agreed **_Remittance Information_** which is **_Structured_** must not exceed 9,000 characters of business content (i.e. the information). This nested element is used to capture a variety of structured remittance information.

**Structured**

| Referral Document Information | Referral Document Amount | Creditor Reference Information | Invoice | Invoice | Tax Reimbursement | Garnishment Reimbursement | Additional Remittance Information |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ... | ... | ... | ... | ... | ... | ... | ... |

example of **_Structured_** invoice information

The **_Creditor Remittance Information_** is provided by the **_Creditor_** in the Cash Management Reporting messages' Remittance Information component, for example, the camt.053 Bank to Customer Statement.

element names

| Structured | |
| :--- | :--- |
| Reference Document Information | `<RfrdDocInf>` |
| Type | `<Tp>` |
| Code Or Proprietary | `<CdOrPrtry>` |
| Code | `<Cd>` |
| Number | `<Nb>` |
| Related Date | `<Dt>` |

xml tag

business information

| CINV |
| :--- |
| A0000101 |
| 2019-10-29 |

In this example Referral Document Information and its nested elements have multiplicity which support up to 9,000 character of information. Whereby this element can be repeated to include more coded information such as another invoice.

Direct Debit Transaction Information
Remittance Information

---

<!-- Page 178 -->

The **_Creditor Reference_** in the _Creditor Reference Information_ component in the structured remittance information is generated by _Creditor_ to allow for the identification of the underlying documents and enable reconciliation by the Creditor upon receipt of the amount of money.

Creditor Reference in the Structured Remittance Information can be based on ISO 11649
* 2 letters "RF"
* 2 digits check digit
* 21 letters/digits creditor reference

By providing the Creditor Reference in the pain.008, such as invoice number for collection, it will facilitate STP and auto-match the incoming credit entry. The Creditor Reference can be extracted from the statement (e.g., camt.053 Structured Remittance information within the Transaction Details or MT 940 Field 61 or Field 86).

Equally the End-To-End Identification could perform a similar function

SCORE Guideline: For Creditor Reference information, in instances where the Creditor Reference Type code is SCOR (Structured Communication Reference) and the Creditor Reference is structured in accordance with ISO 11649, the

Direct Debit Transaction Information
Remittance Information

---

<!-- Page 179 -->

> Use case should be considered as a principle example whereby use case may be cross referenced e.g. a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases.

**Interbank Customer Direct Debit Initiation - Relay**
Use Case pn.8.1.1 – High Level Direct Debit Initiation Interbank 'relay' (pain.008)
Use Case pn.8.1.2 – High Level Direct Debit Initiation Interbank 'relay' (pain.008) involving a Payment Market Infrastructure

---

<!-- Page 180 -->

In the interbank relay scenario, the Forwarding Agent relays the pain.008 message to the Creditor Agent to request the collections of funds from the debtor's accounts for a creditor.

**Diagram Flow:**

- **1** (Initiating Party) → `pain.008` → **2** (Forwarding Agent F)
- **2** (Forwarding Agent F) → `Interbank pain.008` → **3** (Creditor Agent A)
- **3** (Creditor Agent A) → `pacs.003` → **4** (Debtor Agent B)
- **4** (Debtor Agent B) → `camt.053` → **3** (Creditor Agent A)
- **3** (Creditor Agent A) → `camt.053` → **3b** → **2** (Forwarding Agent F)
- **2** (Forwarding Agent F) → `pain.002` → **1** (Initiating Party)
- **3a** (Creditor Agent A) → `Interbank pain.002` → **2** (Forwarding Agent F)

**Steps:**

**1**
Initiating Party sends a direct debit instruction to the Forwarding Agent

**2**
Forwarding Agent (F) forwards the direct debit instruction to the Creditor Agent (A)

**3**
Creditor Agent (A) instructs Debtor Agent (B) to perform a direct debit transaction by sending a local direct debit message or pacs.003

**3a**
Creditor Agent (A) provides a status update ACSP (accepted settlement in progress) to the

**3b**
Forwarding Agent (F) relays the status ACSP (accepted settlement in progress) to the Initiating Party, based upon a bilateral agreement

**4**
Debtor Agent (B) processes the direct debit and sends the statement to Debtor

---

<!-- Page 181 -->

# Payment Market Infrastructure

In the interbank relay scenario, the Forwarding Agent relays the pain.008 message to the Creditor Agent to request the collection of funds from the debtor's accounts for a creditor (through a Payment Market Infrastructure).

**Diagram Flow:**

*   **1** $\xrightarrow{\text{pain.008}}$ **2**
*   **2** $\xrightarrow{\text{Interbank pain.008}}$ **3**
*   **3** $\xrightarrow{\text{pacs.003}}$ [Bank] $\xrightarrow{\text{pacs.003}}$ [Bank B] $\xrightarrow{\text{camt.053}}$ [Debtor]
*   **3a** $\xrightarrow{\text{camt.053}}$ **2**
*   **3b** $\xrightarrow{\text{camt.053}}$ **1**
*   **1** $\xrightarrow{\text{pain.002}}$ **2**
*   **2** $\xrightarrow{\text{Interbank pain.002}}$ **3**

**Step Descriptions:**

1.  **Initiating Party** sends a direct debit instruction to the **Forwarding Agent**
2.  **Forwarding Agent (F)** forwards the payment instruction to the **Creditor Agent (A)**
3.  **Creditor Agent (A)** instructs a direct debit transaction by sending a local direct debit message or pacs.003 to a **Payment Market Infrastructure**
3a. **Creditor Agent (A)** provides a status update ACSP (accepted settlement in progress) to the **Forwarding Agent (F)**, based upon
3b. **Forwarding Agent (F)** relays the status ACSP (accepted settlement in progress) to the **Initiating Party**, based upon a bilateral agreement
4.  **Debtor Agent (B)** receives a local direct debit message via the **Payment Market Infrastructure (PMI)** and debits the account of the

---

<!-- Page 182 -->

# Payment, Clearing and Settlement (pacs) messages

---

<!-- Page 183 -->

**Payments**

**pacs.008** - Financial Institution to Financial Institution Customer Credit Transfer

**pacs.009** - Financial Institution Credit Transfer

**pacs.009 (cov)** - Financial Institution 'Cover' Credit Transfer

**pacs.009 (adv)** – Financial Institution 'advice' of Credit Transfer

**Payment Rejection and Return**

**pacs.002** – Financial Institution To Financial Institution Payment Status Report

**pacs.004** – Payment Return

**Direct Debit Payments**

**pacs.010** - Interbank Direct Debit

**pacs.010 (col)** - Interbank Direct Debit Margin Collection

**pacs.003** - Financial Institution to Financial Institution Customer Direct Debit

---

<!-- Page 184 -->

# Financial Institution to Financial Institution Customer Credit Transfer

---

<!-- Page 185 -->

```
┌─────────────────────┐
│      pacs.008       │
└─────────────────────┘
         │
         ├── ┌─────────────────────────────┐
         │   │        Group Header         │
         │   └─────────────────────────────┘
         │
         └── ┌─────────────────────────────┐
             │  Credit Transfer            │
             │  Transaction Information    │
             └─────────────────────────────┘
```

The pacs.008 has two core sets of nested elements:

- ***Group Header*** which contains a set of characteristics that relates to all individual transaction
- ***Credit Transfer Transaction Information*** which contains elements providing information specific to the individual credit transfer transaction.

🔭 Payment messages in a many-to-many payment are considered as a single transaction.

---

<!-- Page 186 -->

A
B
C
D
pac.008
pac.002
pac.008
pac.002
pac.008
pac.002

The Financial Institution To Financial Institution Customer Credit Transfer message is sent by the Debtor Agent to the Creditor Agent, directly or through other agents and/or a payment clearing and settlement system. It is used to move funds from a Debtor account to a

---

<!-- Page 187 -->

# Group Header

---

<!-- Page 188 -->

Min 1 – Max 1

Each ISO 20222 payment message has a **Message Identification** element, located in the Group Header. This `35 character` identifier is a point-to-point reference used to unambiguously identify the message.

For Payment Clearing and Settlement (pacs) messages the Message Identification has no exact equivalent in the legacy MT payment message. However, the Sender's Reference (Field 20) could be considered a similar comparison where a pacs message contains a single Transaction.

Each transaction's *Credit Transfer Transaction Information* contains a variety of nested *Payment Identification* elements to capture reference related to the individual transaction such as a UETR (Unique End-to-end Transaction Reference)

---

<!-- Page 189 -->

Min 1 – Max 1

The pacs.008 message *Creation Date* captures the date and time which the message was created.

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
> For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- Page 190 -->

Min 1 – Max 1

The pacs.008 message **Number of Transactions** captures the number of individual transaction contained within the message.

The number of transactions in CBPR+ payment usage guidelines is fixed to 1.

Single transactions in the CBPR+ payment usage guidelines enable a transaction to be managed and unlocks highly automated, frictionless, instant payments, supporting the next generation of innovation.

---

<!-- Page 191 -->

The pacs.008 **Settlement Method** element within the Group Header **Settlement Information**, includes one of the embedded codes to indicate how the payment message will be settled.

> The **Settlement Method** *element* in the pacs.008 allows a choice of an embedded code.
>
> **COVE** indicate this Customer Credit Transfer will be settlement using a covering pacs.009 (COV). The Agents being used in the covering payment to reimburse the Instructed Agent can be provided in the dedicated Reimbursement Agent elements. This allows the Instructed Agent to identify the debit account on their books from the Reimbursement Agent account or look up the account related to the reimbursement agent.
>
> **INDA** indicate this Customer Credit Transfer will be settlement by the Instructed Agent (as the Account Servicing Institution) The account held at the Instructed Agent may captured in the dedicated **Settlement Account** element.
>
> **INGA** indicate this Customer Credit Transfer has already been settlement by the Instructing Agent, who has credited the Account they service for the Instructed Agent (as an Account Owner). The account held by the Instructed Agent with the Instructing Agent may captured in the dedicated **Settlement Account** element.

Settlement Method code CLRG is not part of CBPR+ specifications but instead used in Market Infrastructure specification (HVPS+)

---

<!-- Page 192 -->

![](https://i.imgur.com/placeholder1.png)

The pacs messages introduce the *Settlement Method* element within the Group Header *Settlement Information*. Settlement refers to the Agent whose role is to act as an Account Servicing Institution i.e. owns the account and provides service to the customer (Account Owner).
The Account Owner can be an Agent or another Party.
Traditionally an interbank account relationship may have been referred to as a Nostro/Vostro relationship or an Agent's account held on another Agent's books/ another Agent's account held on my books.
Typically the commonality of this can be simplified to the Agent who provides the official Account statement is servicing the account and therefore is the Agent responsible for performing the settlement.

## Why is it so important to understand which Agent Services the account ?

In ISO 20022, much like the legacy FIN process, each leg of a payment has a settlement component. Commonly one of these settlement legs occurs over a Market Infrastructure, who typically owns or instructs the settlement between the two Market Infrastructure participant Agents at a national Central Bank. In this case the Central Bank services both the Instructing Agent and Instructed Agent accounts which is represented by **CLRG** in the Settlement Method of a pacs message.
In a number of business Use Cases there are examples of additional legs, which may occur prior to or after a potential Market Infrastructure, where an Agent is responsible for the role to service an account and perform settlement of that leg.
This role is important as it determines the subsequent message behaviour

---

<!-- Page 193 -->

Your account with me

OR

My account with you

If we simplify a point-to-point message leg and look at when it is settled (booked using traditional language) we can ask ourselves: is the Instructing Agent's account held (serviced) on the books of the Instructed Agent or is the Instructing Agent holding (servicing) the account of the Instructed Agent.

Depending on the answer to this question, this determines the Settlement Method in a serial payment process.

Where the **InstructinG** Agent services the account and is responsible for settling the payment leg, the Settlement Method code **INGA** is used.

Where the **InstructeD** Agent services the account and is responsible for settling the payment leg, the Settlement Method code **INDA** is used.

## Payment transaction lifecycle

A → pacs.008 (INDA) → B → pacs.008 (CLRG) → C → pacs.008 (CLRG) → C → pacs.008 (INGA) → D

B ← C ← D

---

<!-- Page 194 -->

The relationship between the settlement of a payment leg and the message process flow is an important one. The state of settlement influences further messages in the process flow.

**INGA**

The pacs message sent by the Instructing Agent to the Instructed Agent has already been settled.

**Instructing Agent** may (for example) send

- a pacs.002 to the Previous Agent with status ACSC Accepted Settlement Complete.
- a camt.053 Customer Statement to the Instructed Agent (as Account Owner)

**Instructed Agent** can not Reject the pacs message received as it has already settled. The inability to process the pacs message further by the Instructed Agent must result in a pacs.004 Payment Return (which in turn triggers a Reverse Indicator on the Account Owners statement).

**Creditor Agent** having performed the settlement on the Creditor's account, camt reporting message may be used to report or notify on this credit entry.

**INDA**

The pacs message sent by the Instructing Agent to the Instructed Agent has **not** been settled.

**Instructing Agent** may (for example) send

- a pacs.002 to the Previous Agent with status ACSP Accepted Settlement in Progress

**Instructed Agent** may

- Reject the pacs message received, using a pacs.002, as it has not been settled.
- a camt.053 Customer Statement to the Instructing Agent (as Account Owner) Although an rejected entry will not appear in the camt.053

**Creditor Agent** of a pacs.009 (particularly in the cover scenario) may forward the pacs.009 to the Creditor, as the Creditor will perform the settlement (they are the Account Servicing Institution)

**CLRG**

The pacs message sent by the Instructing Agent to the Instructed Agent has **not** been settled. Settlement is performed by the **Market Infrastructure**.

**Instructing Agent** may (for example) send

- a pacs.002 to the Previous Agent with status ACSP Accepted Settlement in Progress

**Instructed Agent** may

- can not Reject the pacs message received as it has already settled. The inability to process the pacs message further by the Instructed Agent must result in a pacs.004 Payment Return.

**Market Infrastructure** may

---

<!-- Page 195 -->

# A

## Settlement Method
**INDA**

### pacs.008

| Instructing Agent: Agent A | Instructed Agent: Agent B |
|---|---|

# B

## Settlement Method
**INGA**

### pacs.008

| Instructing Agent: Agent B | Instructed Agent: Agent C |
|---|---|

### pacs.004

### pacs.004

### camt.053

### camt.053

**Return Reason**

**Return Reason**

> **Agent C is unable to process the payment. As the payment was already settled by the Instructing Agent (Settlement Method INGA) Agent C must use a pacs.004 to instruct the return of the payment**

Group Header Settlement Information Settlement Method

---

<!-- Page 196 -->

# Agent A

# Agent B

# Agent C

# Agent D

| | **A → B** | **B → C** | **C → D** |
|---|---|---|---|
| **Settlement Method** | INDA | INGA | INDA |
| **Forward Message** | pacs.008 | pacs.008 | pacs.008 |
| **Instructing Agent** | Agent A | Agent B | Agent C |
| **Instructed Agent** | Agent B | Agent C | Agent D |
| **Return Message** | pacs.004 / camt.053 | pacs.004 / camt.053 | pacs.002 |
| **Reason** | Return Reason | Return Reason | Reject Reason |

!

> **Agent D is unable to process the payment. As the payment has not been settled by themselves Instructed Agent (Settlement Method INDA) Agent D must use a pacs.002 to**

---

<!-- Page 197 -->

The pacs.008 message *Settlement Account* is a nested element as part of *Settlement Information*, this element identifies information related to an account used to settle the payment instruction.

Min 0 – Max 1
The *Settlement Account* identifies the account details maintained at the account servicing institution (Agent responsible for the settlement of the instruction as indicated in the *Settlement Method*)

- Min 1 – Max 1 *Identification* identifies the account maintained at the Debtor Agent (Account Servicing Institution)
- Min 0 – Max 1 *Type* uses the external Cash Account Type code list to identify the type of account
- Min 0 – Max 1 *Currency* identifies the currency if the account
- Min 0 – Max 1 *Name* identifies the name of the account as assigned by the Account Servicing Institution
- Min 0 – Max 1 *Proxy* captures an alternative identification of the account number such as an email address. This element has further nested *Type* which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used.

---

<!-- Page 198 -->

The pacs message captures a number of Reimbursement Agents as a sub element to **_Settlement Information_** these elements detail the Agent in the cover method who will process the pacs.009 cover.

These elements are similar in nature to the Field 53, 54 and 55 in legacy MT messages and are referred to as The **_Instructing Reimbursement Agent_**, **_Instructed Reimbursement Agent_** and **_Third Reimbursement Agent_**. Each of these reimbursement agents also has a dedicated account element to optionally capture their related account details.

Min 0 – Max 1

The **_Instructing Reimbursement Agent_** captures the Agent who will execute a covering payment (i.e. pacs.009 COV or domestic equivalent) often referred to as the currency correspondent. This optional element is comparable with the Field 53a in the legacy FIN message.

Min 0 – Max 1

The **_Instructing Reimbursement Agent Account_** captured the account related to this Reimbursement Agent. This element can be compared to the Party Identifier of the legacy Field 53.

---

<!-- Page 199 -->

**Min 0 – Max 1**

The **Instructed Reimbursement Agent** captures the Agent who will receive the covering payment (i.e., pacs.009 cov or domestic equivalent) and credit the account of the pacs.008 FI to FI Customer Credit Transfer *Instructed Agent*. This optional element is comparable with the Field 54a in the legacy FIN message.

**Min 0 – Max 1**

The **Instructed Reimbursement Agent Account** captured the account related to this Reimbursement Agent. This element can be compared to the Party Identifier of the legacy Field 54.

**Min 0 – Max 1**

The **Third Reimbursement Agent** captures an additional Agent who will receive the covering payment, where this is not the Agent detailed in the *Instructed Reimbursement Agent*. This optional element is comparable with the Field 55a in the legacy FIN message.

**Min 0 – Max 1**

The **Third Reimbursement Agent Account** captured the account related to this Reimbursement Agent. This element can be compared to the Party Identifier of the legacy Field 55.

---

<!-- Page 200 -->

# Credit Transfer Transaction Information

---

<!-- Page 201 -->

The pacs message *Payment Identification* provides a set of elements to identify the payment, of which several are mandatory elements

**Payment Identification**

- **Instruction Identification** `Min 1 – Max 1`
  a point-to-point reference restricted in CBPR+ to 16 character and directly comparable with the Sender's Reference (Field 20) of the legacy MT payment message.

- **End to End Identification** `Min 1 – Max 1`
  an end-to-end reference provided by the *Debtor* which must be passed unchanged throughout the payment and reported to the Creditor.
  note: if the Debtor has not provide an end-to-end identifier, the *Debtor Agent* may populate "NOTPROVIDED" to comply the mandatory need of this element.

- **UETR** `Min 1 – Max 1`
  the end-to-end Transaction Reference created using the UUIDv4 standard. This reference must be passed unchanged throughout the payment, it may also be created by the Debtor within their Payment Initiation request, and also included in reporting

---

<!-- Page 202 -->

The pacs message *Payment Identification* also provides a set of optional elements to identify the payment.

**Min 1 – Max 1**

## Payment Identification

### Transaction Identification
**Min 0 – Max 1**

an **end-to-end reference** assigned by the first Instructing Agent to identify the transaction.

### Clearing System Reference
**Min 0 – Max 1**

a **point-to-point reference** populated by a Payment Market Infrastructure, typically to the settlement leg of a clearing system transaction as a reference to the settled clearing transaction.

---

<!-- Page 203 -->

The pacs message *Payment Type Information* provides a set of optional elements where the payment type can be described.

## Payment Type Information

**Service Level** `Min 0 – Max 3`

A nested element which may either use an external ISO Service Level code or a proprietary code. It is used to identify a particular agreed\* service level which should be applied to the payment.

For example, code G001 can be used to identify a gpi Tracked Customer Credit Transfer similarly to Field 111 value 001 in the MT 103

**Instruction Priority** `Min 0 – Max 1`

a choice of imbedded codes representing the urgency considered by the Instructing Agent, this point-to-point information may be used by the Instructed Agent to differentiate the processing priority.

**Local Instrument** `Min 0 – Max 1`

A nested element which may either use an external ISO Local Instrument code or a proprietary code. It is used to identify the type of payment local instrument such as a Standing Order.

Note: the ISO instrument codes are registered by specific community group (captured in the code list)

**Clearing Channel** `Min 0 – Max 1`

a choice of imbedded codes representing the clearing channel to be used to process the payment. e.g., RTGS

**Category** `Min 0 – Max 1`

A nested element which may either use an external ISO Category Purpose code or a proprietary code. It is used to

---

<!-- Page 204 -->

The pacs.008 message has two key element to capture the amount of the Credit Transfer, **Interbank Settlement Amount** `Min1 – Max1` and **Interbank Settlement Date** `Min1 – Max1`

**Interbank Settlement Amount**

A mandated currency amount moved between the *Instructing Agent* and the *Instructed Agent*. This therefore is the point-to-point currency amount exchanged, comparable with the MT Field 32A

**Interbank Settlement Date**

A mandated date on which the *Interbank Settlement* should be executed between the *Instructing Agent* and the *Instructed Agent*. This therefore is the value date comparable with the MT Field 32A

🔍 Note: the relationship between Interbank Settlement Amount and Instructed Amount is an important one. Instructed Amount relates to the amount Instructed to be executed from the Debtor's account and only need to be captured in the Instructed Amount where the Interbank Settlement Amount is not the same currency amount

---

<!-- Page 205 -->

The pacs.008 message has three optional elements to capture the optional information related to the settlement of the instructions.

**Min 0 – Max 1**

The **Settlement Priority** provides an optional choice of embedded codes to indicate the instruction's settlement priority from the perspective of the Instructing Agent. This point-to-point information may be used by the Instructed Agent to identify the priority associated with the **Settlement Method** and should not be confused with the *Instruction Priority*.

Note: where **Settlement Method** of the pacs.008 is 'COVE' (settled via a covering pacs.009 COV) Settlement Priority is relevant to the covering payment not the pacs.008

**Min 0 – Max 1**

The **Settlement Time Indication** optionally captures the time settlement occurred at a transaction administrator such as a Market Infrastructure.
This DateTime can be captured in two nested elements, **Debit Date Time** and **Credit Date Time**.

**Min 0 – Max 1**

The **Settlement Time Request** optionally captures the time settlement is requested for the payment instruction by the Instructing Agent. This Time can be capture in four nested elements:
* **CLS Time** the time the amount must be credit to CLS Bank
* **Till Time** the time until which the payment may be settled

---

<!-- Page 206 -->

**Min 0 – Max 1**

The *Instructed Amount* captures currency and amount instructed by the Debtor. This conditional element is required when the **Interbank Settlement Amount** is not the same currency and/or amount as originally instructed by the Debtor. For example, a charge is taken, or the transactions is converted to another currency. This element is comparable with the legacy Field 33B.

**Min 0 – Max 1**

The *Exchange Rate* capture the factor (rate) used to convert an amount from one currency into another. This reflects the currency pair price at which one currency was bought with another currency.

As a best practice to provide consistency and transparency the *Exchange Rate* used to convert the *Instructed Amount* (base currency) to the *Interbank Settlement Amount* (quote currency) should use the *Instructed currency* as the whole unit to perform the exchange.

For example if *Instructed Amount* currency is CAD and the Interbank Settlement currency is USD the rate should reflected as 0.83 (CAD 1 equals USD 0.83)

Note: a number of Cross Element Rules exist which relate to the *Instructed Amount* element. For example if the *Instructed Amount* is present and the

---

<!-- Page 207 -->

Min 1 – Max 1

The mandated **Charge Bearer** element uses an embedded code that is used to specify which party/parties would bear any charges associated with processing the payment transaction. This element is comparable with MT Field 71A 'Details of Charges'

| Charge Bearer (1.1) | Code | Description | ISO 20022 |
|---|---|---|---|
| | CRED | Creditor | |
| | DEBT | Debtor | |
| | SHAR | Shared | |
| | SLEV | Service Level | |

| 71A: Details of Charges | Code | Description | MT 103 |
|---|---|---|---|
| | BEN | Beneficiary | |
| | OUR | Our Customer Charges | |
| | SHA | Shared Charges | |

Note: *Charge Bearer* code SLEV applies following rules agreed as part of a bilateral agreed Service Level or as part of a scheme (commonly used in Instant Payment schemes) This code has no equivalent in legacy MT messages. SLEV is removed from CBPR+ usage guideline specifications for the beginning of the coexistence period.

---

<!-- Page 208 -->

Min 0 – Max *    Min 1 – Max 1

The **Charges Information** element provides information on the charges to be paid by the **Charge Bearer**. This element is comparable with MT Fields: 71F 'Senders Charges' and 71G 'Receiver's Charges'

| Charge Information (0..*) | Amount |  |
|---|---|---|
|  | Currency |  |
|  | Agent | BICFI |
|  |  | Name |
|  |  | Structured Postal Address |

In addition to the legacy MT message the pacs.008 *Charge Information* mandate the *Agent*, this represent the Agent for who the Charges are either; due (pre-paid charges) or has taken a charge (deduct from the transaction)

CBPR+ best practice recommends the use of the structured Agent BIC.

As the **Charges Information** element is repetitive it can capture charges related to previous legs of the payment transaction.

Note: As the *Charge Information* element has the capability to capture both charges deducted and charges included i.e. pre-paid charges, the use of the *Interbank Settlement Amount* and *Instructed Amount* elements play an important role.
Also note: If Charge Bearer DEBT is provided only one optional occurrence of pre-paid charges is allowed.

---

<!-- Page 209 -->

# charges

**1** → **2** (pacs.008) → **3** (pacs.008) → **4** (pacs.008) → **5**

## 1
Debtor requests a payment for USD 100 specifying the charges should be shared

| Interbank Settlement Amount | USD 100 |
|---|---|
| Charge Bearer | Code | SHAR |

## 2
Debtor Agent executes the USD 100 payment charging the Debtor as commercially agreed.

| Interbank Settlement Amount | USD 100 |
|---|---|
| Charge Bearer | Code | SHAR |
| Charge Information | Amount | 10 |
| Charge Information | Currency | USD |
| Charge Information | Agent | BIC | BBBBUS3N |

## 3
Agent B processes the payment deducting their fee of USD 10

| Interbank Settlement Amount | USD 90 |
|---|---|
| Instructed Amount | USD 100 |
| Charge Bearer | Code | SHAR |
| Charge Information | Amount | 10 |
| Charge Information | Currency | USD |
| Charge Information | Agent | BIC | BBBBUS3N |

## 4
Agent C processes the payment deducting their fee of USD 5

| Interbank Settlement Amount | USD 85 |
|---|---|
| Instructed Amount | USD 100 |
| Charge Bearer | Code | SHAR |
| Charge Information | Amount | 10 |
| Charge Information | Currency | USD |
| Charge Information | Agent | BIC | BBBBUS3N |
| Charge | Amount | 5 |

---

<!-- Page 210 -->

# of charges

1.  **Debtor** -> **Agent A** --pacs.008--> **Agent B** --pacs.008--> **Agent C** --pacs.008--> **Agent D** -> **Creditor**

**1**
Debtor requests a payment for USD 100 specifying any charges will be borne by them, in accordance with their banking agreement.

**2**
Debtor Agent executes the USD 100 payment including a previous negotiated pre-payment of charges (USD 30). The Debtor is debited for USD 100 plus the Charges in accordance with their account agreement.

| Interbank Settlement Amount | USD 130 |
| :--- | :--- |
| Instructed Amount | USD 100 |
| Charge Bearer | Code: DEBT |
| Charge Information | Amount: 30 |
| | Currency: USD |

**3**
Agent B identifies the pre-payment of charges by the inclusion of their BIC in the Charge Information Agent element. Removing charge (USD 30), they forward the payment to the next Agent. The next Agent many request a charge.

| Interbank Settlement Amount | USD 100 |
| :--- | :--- |
| Charge Bearer | Code: DEBT |

**Pre-payment of charges** are identified by the inclusion of their BIC in the Charge Information Agent element of the payment message they receive

---

<!-- Page 211 -->

of multiple charges

1 ➔ 2 (pacs.008) ➔ 3 (pacs.008) ➔ 4 (pacs.008)
(A) ➔ (B) ➔ (C) ➔ (D)

1. Debtor requests a payment for USD 100 specifying any charges will be taken by them, in accordance with their banking agreement.

2. Debtor Agent executes the USD 100 payment including a previous negotiated pre-payment of charges (USD 30). The Debtor is debited for USD 100 plus the Charges in accordance with their account agreement.

3. Agent B identifies the pre-payment of charges by the inclusion of their BIC in the Charge Information Agent element. Removing charge (USD 30), they forward the payment, including USD 20 of pre-payment of charges of the next Agent.

4. Agent C identifies the pre-payment of charges by the inclusion of their BIC in the Charge Information Agent element. Removing this pre-payment of charges they forward the payment to the Next Agent and indicate they will bear the cost of any charge claims.

**Pre-payment of charges are identified by the instructed Agent by the inclusion of their BIC in the Charge Information Agent element of the payment message they receive**

| Interbank Settlement Amount | USD 130 |
| :--- | :--- |
| Instructed Amount | USD 100 |
| Charge Bearer | Code: DEBT |
| Charge Information | Amount: 30 |
| Charge Information | Currency: USD |
| Charge Information | Agent: BIC BBBBUS3N |

| Interbank Settlement Amount | USD 120 |
| :--- | :--- |
| Instructed Amount | USD 100 |
| Charge Bearer | Code: DEBT |
| Charge Information | Amount: 20 |
| Charge Information | Currency: USD |
| Charge Information | Agent: BIC CCCUS3N |

| Interbank Settlement Amount | USD 100 |
| :--- | :--- |
| Charge Bearer | Code: DEBT |

pre-payment of charges versus

---

<!-- Page 212 -->

ISO 20022 pac.008 message standards document “If ChargesInformation is present, then the currency of ChargesInformation/ChargesAmount is recommended to be the same as the currency of InterbankSettlementAmount”

| Interbank Settlement Amount received | Interbank Settlement Amount forwarded | Currency of Charge Information (where a charge occurs) |
| :--- | :--- | :--- |
| USD | USD | USD |
| USD | EUR | EUR |

ISO 20022 does not prevent Charges from being booked in a different currency, but for transparency the Charge should be represented within the Charge Information in the Interbank Settlement Amount Currency.

---

<!-- Page 213 -->

# charges

1 → **A** —pacs.008→ **B** —pacs.008→ **C** —pacs.008→ **D** → 2

**1** Debtor requests a payment for GBP 100 to be initiated from their USD account, specifying the charges should be borne by the Creditor

**2** Debtor Agent executes a payment for GBP 95 (GBP 100 minus a 5 GBP charge deducted as this is borne by the Creditor.

**3** Agent B processes the payment deducting their fee of GBP 10

| Interbank Settlement Amount | GBP 95 |
|---|---|
| Instructed Amount | GBP 100 |

| Charge Bearer | Code | CRED |
|---|---|---|
| Charge Information | Amount | 5 |
| | Currency | GBP |
| | Agent | BIC AAAAGB22 |

| Interbank Settlement Amount | GBP 85 |
|---|---|
| Instructed Amount | GBP 100 |

| Charge Bearer | Code | CRED |
|---|---|---|
| Charge Information | Amount | 5 |
| | Currency | GBP |
| | Agent | BIC AAAAGB22 |
| Charge Information | Amount | 10 |
| | Currency | GBP |

---

<!-- Page 214 -->

The pacs message can capture up to 3 Previous Instructing Agents, which represent an Agent who previously only played a dynamic role in the payment between the Debtor Agent and Creditor Agent.

**Min 0 – Max 1**
The *Previous Instructing Agent 1* captures the first historic Agent between the Debtor Agent and the Previous Instructing Agent 2 (where present) and the Instructing Agent. This optional element is comparable with the Field 72 first /INS/ occurrence in the legacy FIN message.

**Min 0 – Max 1**
The *Previous Instructing 1 Account* captured the account related between this Agent and Previous Instructing Agent 2 (where present) or the Instructing Agent. This optional element has not comparable field in the legacy FIN message

**Min 0 – Max 1**
The *Previous Instructing 2* captures the second Previous Instructing Agent between the Previous Instructing Agent 1 and the Previous Instructing Agent 3 (where present) and the Instructing Agent. This optional element is comparable with the Field 72 second /INS/ occurrence in the legacy FIN message.

**Min 0 – Max 1**
The *Previous Instructing 2 Account* captured the account related between this Agent and Previous Instructing Agent 2 (where present) or the Instructing Agent. This optional element has not comparable field in the legacy FIN message.

**Min 0 – Max 1**
The *Previous Instructing 3* captures the third Previous Instructing Agent between the Agent and the Instructing Agent. This optional element is comparable with the Field 72 third /INS/ occurrence in the legacy FIN message.

**Min 0 – Max 1**
The *Previous Instructing 3 Account* captured the account related between this Agent and Previous

---

<!-- Page 215 -->

Instructing
Agent: Agent A

Instructed
Agent: Agent B

pac.008

Instructing
Agent: Agent B

Instructed
Agent: Agent C

pac.008

*Instructing Agent* and *Instructed Agent* represent the Agents involved in the pac point-to-point message exchange. These roles therefore change on each payment leg.

*Instructing Agent* and *Instructed Agent* elements are required in all pac messages and are only available in the **Credit Transfer Information**

---

<!-- Page 216 -->

# Intermediary Agents

The ISO 20022 pacs messages have a number of optional Agent elements whose roles change throughout the life cycle of the payment. **Intermediate Agent** is an example of this, where these agents are classified in numeric order (i.e. *Intermediate Agent 1*). **Previous Instructing Agent** however is a static role which allows additional Previous Instructing Agent to be appended to the history of the payment.

The below diagram visualizes the change of Agent role at different stages of the payment transaction life cycle.

| Debtor | A | B | C | D | E | Creditor |
|---|---|---|---|---|---|---|
| Debtor | Instructing Agent & Debtor Agent | Instructed Agent | Intermediary Agent 1 | Intermediary Agent 2 | Creditor Agent | Creditor |
| Debtor | Debtor Agent | Instructing Agent | Instructed Agent | Intermediary Agent 1 | Creditor Agent | Creditor |
| Debtor | Debtor Agent | Previous Instructing Agent 1 | Instructing Agent | Instructed Agent | Creditor Agent | Creditor |
| Debtor | Debtor Agent | Previous Instructing Agent 1 | Previous Instructing Agent 2 | Instructing Agent | Creditor Agent & Instructed Agent | Creditor |

---

<!-- Page 217 -->

The pacs message can capture up to 3 Intermediary Agents, which play a dynamic role in the payment between the Debtor Agent and Creditor Agent.

Min 0 – Max 1
The **Intermediary Agent 1** captures the first Intermediary Agent between the Debtor Agent and Creditor Agent for who the Instructed Agent attempt to instruct the payment on to. This optional element is comparable with the Field 56a in the legacy FIN message.

Min 0 – Max 1
The **Intermediary Agent 1 Account** captured the account related to this Intermediary Agent, with the Instructed Agent. This element can be compared to the Party Identifier of the legacy Field 56a.

Min 0 – Max 1
The **Intermediary Agent 2** captures the second Intermediary Agent between the Intermediary Agent 1 and the Creditor Agent. This optional element has not comparable field in the legacy FIN message.

Min 0 – Max 1
The **Intermediary Agent 2 Account** captured the account related to this Intermediary Agent, with the Intermediary Agent 1. This optional element has not comparable field in the legacy FIN message.

Min 0 – Max 1
The **Intermediary Agent 3** captures the third Intermediary Agent between the Intermediary Agent 2 and the Creditor Agent. This optional element has not comparable field in the legacy FIN message.

Min 0 – Max 1
The **Intermediary Agent 3 Account** captured the account related to this Intermediary Agent, with the

---

<!-- Page 218 -->

authority to instruct payment from their Headquarter (HQ) settlement account.

Usually a serial payment is instructed through each Agent in a serial process. In some circumstances a branch of an Institution (Agent A) may be given Debit Authority to instruct payment from their Headquarters (Agent HQ) account with its currency correspondent (Agent B). In much the same way as if this had occurred serially, it is important that the payment instructed by Agent B correctly reflect Agent HQ as an Agent participating in the transaction, particularly if the payment is returned.

[Agent A] → **pacs.008** → [Agent B] → **pacs.008** → [Agent C] → **pacs.008** → [Agent D]

**1** [Agent HQ]

**1** Debtor Agent executes the payment using their Headquarters as the settlement account

| Interbank Settlement Amount | USD 100 |
|---|---|
| Settlement Account | Id | 12345 |
| Debtor Agent | AAAAGB2LABC |

**2** Agent B processes the payment debiting the account of Agent A Headquarters, and including them as the Previous Instructing Agent in the payment transaction.

| Interbank Settlement Amount | USD 100 |
|---|---|
| Settlement Account | 12345 |
| Debtor Agent | AAAAGB2LABC |

For transparency purpose Agent C (in this use case) has a responsibility to ensure the Agent associated with the Settlement Account is captured in the next payment leg as a Previous Instructing Agent. This also ensures, should a Payment Return occur, all the Agents can be correctly identified

---

<!-- Page 219 -->

The pacs.008 message introduces ultimate parties to the FI to FI Customer Credit Transfer message. The **Ultimate Debtor** element should not be confused with an *Initiating Party* who may send a payment initiation request on behalf of the Debtor. (see dedication section on *Initiating Party*)

**Ultimate Party**
**Ultimate Debtor**
**Ultimate Creditor**

➢ `Min 0 - Max 1` CBPR+ premise is that an **Ultimate Debtor** has no financial regulated direct account relationship with the corresponding *Debtor*.

➢ `Min 0 - Max 1` CBPR+ premise is that an **Ultimate Creditor** has no financial regulated direct account relationship with the corresponding *Creditor*.

An account is often used a term to recognise an ongoing customer relationship. Non Agent payment provider are typically not bound by the same regulatory oversight as an Agent (Financial Institution). They would therefore be classed as a Party to a payment, where the account relationship with their customer would classify their customer as an Ultimate (Debtor or Creditor depending on the payment scenario)

Credit Transfer Transaction Information ⓘ
Ultimate Creditor

---

<!-- Page 220 -->

# Debtor

An individual walks into a Money Transfer Bureau with relevant Private Identification (e.g. a passport) and requests a payment to be paid on their behalf to a Creditor. Having accepted payment for the transaction, the Money Transfer Bureau executes a payment initiation request to their Agent (Bank) as the Debtor, on behalf of the individual who is represented as the Ultimate Debtor.

**1** → **2** → **3** (A) —pacs.008→ (B) —pacs.008→ (C) —pacs.008→ (D) →

**1**
Ultimate Debtor requests a payment to be initiated on their behalf to the Creditor

**2**
Debtor requests a payment to be initiated on behalf of the Ultimate Debtor to the Creditor

**3**
Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries

| Ultimate Debtor | Name |
| :--- | :--- |
| | Postal Address |
| | Identification |
| | Country Of Residence |
| | **Organisation Identification** |
| | **Private Identification** |

---

<!-- Page 221 -->

# Creditor

A payments is initiated to credit a retirement care facility to pay the fees of one of its residents. The retirement facility is the Creditor of the payment transaction, whereby the resident of the facility is represented as the Ultimate Creditor (beneficiary of the services the fee is paying for)

1 → 2 → pacs.008 → pacs.008 → pacs.008 →

**1**
Debtor initiates a payment instruction to the Debtor Agent

**2**
Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries

Ultimate Creditor
- Name
- Postal Address
- Identification
- Country Of Residence
  - Organisation Identification
  - Private Identification

---

<!-- Page 222 -->

Initiating Party

Debtor

Third Party

Debtor Agent

Min 0 – Max 1

The **_Initiating Party_** of a payment is often the Min 1 – Max 1 **_Debtor_** themselves and therefore this optional element is not necessary. More often the _Initiating Party_ is a third party providing payment initiation services on behalf of the _Debtor_ (often referred to as a Third Party Provider) whereby the _Debtor_ maintains an account with the Debtor Agent but the Third Party Provider has authority to initiate payment on behalf of the _Debtor_. This is distinctly different from an Ultimate Party (such as _Ultimate Debtor_) who instructs the _Debtor_ to initiate a payment on their behalf.

In the context of a Direct Debit (pacs.003) or Request to Payment (pain.013) the _Initiating Party_ is often the _Creditor_, however the same context of a Third Party Provider can exist where the third party is responsible for collecting funds on behalf of the _Creditor_.

---

<!-- Page 223 -->

The ISO 2022 pacs messages describe the party debited for a transaction as the *Debtor*. The *Debtor* sub elements describe the *Debtor* in greater detail.

Mandatory *Name* (where a BIC identifier is not provided) by which the party is known

**Name**

**Postal Address**

- Department
- Sub Department
- Street Name
- Building Number
- Building Name
- Floor
- Post Box
- Room
- Post Code
- Town Name
- Town Location Name
- District Name
- Country Sub Division
- Country
  - Code

Nested element capturing either structured or unstructured *Debtor* address details

**Debtor**

Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc.

**Identification**

Optional element to capture the Debtor's ISO country code of residence

**Country of Residence**

---

<!-- Page 224 -->

The pacs.008 ***Debtor Account*** is used to capture the account information for which debit entry is/has been applied to the Debtor's account, which are also reflected in their account Statement.

The ***Debtor Account*** uses a variety of nested elements to capture information related to the account.

| Min 0 – Max 1 | ***Identification*** identifies the account maintained at the Debtor Agent (Account Servicing Institution) |
|---|---|
| Min 0 – Max 1 | ***Type*** uses the external Cash Account Type code list to identify the type of account |
| Min 0 – Max 1 | ***Currency*** identifies the currency of the account |
| Min 0 – Max 1 | ***Name*** identifies the name of the account as assigned by the Debtor Agent (Account Servicing Institution) |
| Min 0 – Max 1 | ***Proxy*** captures an alternative identification of the account number such as an email address. This element has further nested ***Type*** which is a choice of external code list or proprietary code and ***Identification*** which are both mandatory where the Proxy element is used. |

---

<!-- Page 225 -->

| ISO 2022 Debtor data element example | | | | | | Customer data record example |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Debtor | Name | | | | | JOHN HECTOR JOSEPH SMITH - MASTERSONS |
| | Postal Address | Department | | | | |
| | | Sub Department | | | | |
| | | Street Name | | | | HOOGSTRAAT |
| | | Building Number | | | | 6 |
| | | Post Code | | | | 1000 |
| | | Town Name | | | | BRUSSELS |
| | | Country | | | | BE |
| | Identification | Private Id | Other | Id | | 1111111111 |
| | | | | Scheme Name | Code | CCPT |
| Debtor Account | Identification | IBAN | | | | BE3000121637141 |

| MT - free format option |
| :--- |
| :50K:/BE3000121637141 |
| JOHN HECTOR JOSEPH SMITH - MASTERSONS |
| HOOGSTRAAT 6 BRUSSELS 1000 BELGIUM |
| PASSPORT 1111111111 |

| MT - structured option with risk of potential truncation & loss of info |
| :--- |
| :50F:/BE3000121637141 |
| 1/JOHN HECTOR JOSEPH SMITH - MASTER |
| 1/SONS |
| 2/HOOGSTRAAT 6 |
| 3/BE/BRUSSELS 1000 |

---

<!-- Page 226 -->

Min 1 – Max 1 Min 1 – Max 1
The **Debtor Agent** and **Creditor Agent** are static roles in the pacs.008 FI to FI Customer Credit Transfer. These agent maintain a relationship with their customers; the *Debtor* and *Creditor*.

Note: Although the **Debtor Agent, Creditor Agent, Debtor and Creditor** all maintain static roles in the pacs messages, the description of these parties change in the reporting messages (camt) where the Debtor Agent and Creditor Agent become the Statement Account Servicer and the Debtor and Creditor become the Statement Account Owner. This will be explored further in the camt Cash Management Reporting section.

Credit Transfer Transaction Information

---

<!-- Page 227 -->

# Account

Min 0 – Max 1 The **Debtor Agent Account** and **Creditor Agent Account** are used to capture the account information related to these Agents. The nature of this element implies there is an Agent or Agent in between the Debtor Agent and Creditor Agent in the payment transaction.

The **Debtor Agent Account** and **Creditor Agent Account** uses a variety of nested elements to capture information related to the account.

| Constraint | Element Description |
|---|---|
| Min 1 – Max 1 | **Identification** identifies the account maintained at the Account Servicing Institution |
| | **Type** uses the external Cash Account Type code list to identify the type of account |
| Min 0 – Max 1 | **Currency** identifies the currency of the account |
| Min 0 – Max 1 | **Name** identifies the name of the account as assigned by the Account Servicing Institution |
| Min 0 – Max 1 | **Proxy** captures an alternative identification of the account number such as an email address. This element has further nested **Type** which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used. |

Debtor Agent and Creditor Agent are a Financial Institution, therefore

---

<!-- Page 228 -->

The ISO 20022 pac messages describe the party credited for a transaction as the *Creditor*. The *Creditor* sub elements describe the *Creditor* in greater detail.

**Postal Address**
*   Department
*   Sub Department
*   Street Name
*   Building Number
*   Building Name
*   Floor
*   Post Box
*   Room
*   Post Code
*   Town Name
*   Town Location Name
*   District Name
*   Country Sub Division
*   Country
    *   Code

Nested element capturing either structured or unstructured *Creditor* address details

Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc.

Mandatory *Name* (where a BIC identifier is not provided) by which the party is known
**Name**

**Postal Address**

**Creditor**

**Identification**

Optional element to capture the Creditor's ISO country code of residence
**Country of Residence**

---

<!-- Page 229 -->

The `pacs.009` **Min 0 – Max 1** *Creditor Account* is used to capture the account information for which a credit entry is intended to be applied to the Creditor's account, which are also reflected in their account Statement.

The *Creditor Account* uses a variety of nested elements to capture information related to the account.

`Min 1 – Max 1` **Identification** identifies the account maintained at the Creditor Agent (Account Servicing Institution)

`Min 0 – Max 1` **Type** uses the external Cash Account Type code list to identify the type of account

`Min 0 – Max 1` **Currency** identifies the currency if the account

`Min 0 – Max 1` **Name** identifies the name of the account as assigned by the Creditor Agent (Account Servicing Institution)

`Min 0 – Max 1` **Proxy** captures an alternative identification of the account number such as an email address. This element has further nested **Type** which is a choice of external code list or proprietary code and **Identification** which are both mandatory where the Proxy element is used.

---

<!-- Page 230 -->

# Account

Min 0 – Max 1 The **Debtor Agent Account** and **Creditor Agent Account** are used to capture the account information related to these Agents. The nature of this element implies there is an Agent or Agent in between the Debtor Agent and Creditor Agent in the payment transaction.

The **Debtor Agent Account** and **Creditor Agent Account** uses a variety of nested elements to capture information related to the account.

| Constraint | Element Description |
|---|---|
| Min 1 – Max 1 | **Identification** identifies the account maintained at the Account Servicing Institution |
| | **Type** uses the external Cash Account Type code list to identify the type of account |
| Min 0 – Max 1 | **Currency** identifies the currency of the account |
| Min 0 – Max 1 | **Name** identifies the name of the account as assigned by the Account Servicing Institution |
| Min 0 – Max 1 | **Proxy** captures an alternative identification of the account number such as an email address. This element has further nested **Type** which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used. |

Debtor Agent and Creditor Agent are a Financial Institution, therefore

---

<!-- Page 231 -->

The *Instruction for Next Agent* and *Instruction for Creditor Agent* elements within the pacs.009 Financial Institution Credit Transfer optionally provides information related to the processing of the payment for these Agents.

**Min 0 – Max 2**

The *Instruction for Creditor Agent* element offers a multiplicity of up to 2 occurrences of information. This element enables:
> the use of 2 embedded **codes** to describe the instruction
> free format *instruction information*
> or both, where the free format complements the code.

The use of this element may be **bilaterally** agreed with the *Creditor Agent*. It must be passed on throughout the life cycle of the transaction until the payment reaches the *Credit Agent*.

**Min 0 – Max 6**

The *Instruction for Next Agent* element offers a multiplicity of up to 6 occurrences of information. This element is restricted to free format *instruction information* in CBPR+.
The element is used to provide instruction to the next Agent (which may not be the Creditor Agent)

Credit Transfer Transaction Information

---

<!-- Page 232 -->

**Min0 – Max1**

**Purpose**

The **Purpose** element within the pacs.008 FI to FI Customer Credit Transfer captures the reason for the payment transaction which may either use an external ISO **Purpose code** or a proprietary code. The purpose is used to capture the nature of the payment e.g. **IVPT** Invoice Payment, **FEES** Payment of Fees etc. and should not be confused with Regulatory Reporting codes. By definition this information is typically defined by the Debtor.

The externalised Purpose code set is classified by the purpose, for example commercial, for which the numerous codes within the classification are each described by Name and Definition.
For example: **GDSV** is classified within the Commercial categorisation, with the *Name* **Purchase Sale of Goods and Services** described as a *Transaction is related to purchase and sale of goods*.

*Category Purpose* also captures a high level purpose, which unlike *Purpose* is less granular but can trigger special processing e.g. Category Purpose code **SALA** ‘Salary Payment’ may trigger a reporting process which restricts sensitive data i.e., individual salary names.

Credit Transfer Transaction Information

---

<!-- Page 233 -->

Min 0 – Max 10
The **Regulatory Reporting** element within the pacs.008 FI to FI Customer Credit Transfer is nested to capture regulatory and statutory information needed to report to the appropriate authority/s.

Min 0 – Max 1
The **Debit Credit Reporting Indicator** utilises an embedded choice of code to indicate whether the regulatory reporting information applies to the:
- DEBT (debit)
- CRED (credit) or
- BOTH

Min 0 – Max 1
The **Authority** element captures the *Name* and *Country* code of the Authority/Entity requiring the regulatory reporting information.

Min 0 – Max 1
The **Details** element provides the detail on the regulatory reporting information.

Credit Transfer Transaction Information > Regulatory Reporting

---

<!-- Page 234 -->

The **<u>Related Remittance Information</u>** element within the pacs.008 FI to FI Customer Credit Transfer is nested to provide information related to the handling of remittance information. This information is typically provided by the Debtor in the payment initiation request.

Min 0 – Max 1

The **<u>Remittance Identification</u>** captures a unique reference assigned by the initiating party of the payment to identify the remittance information sent separately from the payment instruction.

Min 0 – Max 2

The **<u>Remittance Location Details</u>** uses a set of nested elements to provide information on either the location of or the delivery of remittance information.

- **<u>Method</u>** requires a code from an embedded list to detail the method used to deliver the remittance advise information e.g. *EMAL* (email)
- **<u>Electronic Address</u>** provides an electronic address for which an agent is to send the remittance information to e.g. the email address. It may also reference a URL where remittance information may be deposited or retrieved.
- **<u>Postal Address</u>** provides the postal address to which an agent is to send the remittance information

Remittance advices are typically considered as a traditional value added service provided by the Debtor Agent to the Debtor, in order to provide *Remittance Information* to the Creditor. By nature this element can travel end-to-end within the pain, pacs and camt reporting messages.

**<u>Remittance Information</u>** is a dedicated element used both within the pacs and camt reporting messages, whereby this information can travel end-to-end using ISO 20022. *Related Remittance Information* and *Remittance Information* are mutually exclusive (can't both be present)

---

<!-- Page 235 -->

The optional *Remittance Information* element within the pacs.008 FI to FI Customer Credit Transfer is nested to provide either *Structured* or *Unstructured* information related to payment, such as invoices.

Min 0 – Max 1
*Remittance Information* enable the matching/reconciliation of an entry that the payment is intended to settle

Min 0 – Max 1
The *Unstructured* sub element captures free format *Remittance Information* which is restricted in CBPR+ to 140 characters to ensure backward compatibility with the legacy MT message during coexistence.

Min 0 – Max *
The *Structured* element is nested capturing rich structured *Remittance Information*, and is unlimited in its multiplicity, but must not exceed 9,000 characters of business information (does not include the xml element identification)
The use of this nested element should be *bilaterally/multilaterally* agreed, to ensure end-to-end transportation of this data.

Related *Remittance Information* and *Remittance Information* are

---

<!-- Page 236 -->

The bilaterally/multilaterally agreed **_Remittance Information_** which is **_Structured_** must not exceed 9,000 characters of business content (i.e. the information). This nested element is used to capture a variety of structured remittance information.

**Structured**

| Referred Document Information | Referred Document Amount | Creditor Remittance Information | Invoker | Invoice | Tax Reimbursement | Garnishment Reimbursement | Additional Remittance Information |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| ... | ... | ... | ... | ... | ... | ... | ... |

example of **_Structured_** invoice information

The **_Creditor Remittance Information_** is provided to the **_Creditor_** in the Cash Management Reporting messages' Remittance Information component, for example, the camt.053 Bank to Customer Statement.

element names

| Structured | |
| :--- | :--- |
| Reference Document Information | `<RfdDocInf>` |
| Type | `<Tp>` |
| Code Or Proprietary | `<CdOrPrtry>` |
| Code | `<Cd>` |
| Number | `<Nb>` |
| Related Date | `<Dt>` |

xml tag

business information

| CINV |
| :--- |
| A0000101 |
| 2019-10-29 |

In this example Referred Document Information and it nested elements has multiplicity which support up to 9,000 character of information. Whereby this element can be repeated to include more coded information such as another invoice.

Credit Transfer Transaction Information

Remittance Information

---

<!-- Page 237 -->

Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases.

**Serial Financial Institution to Financial Institution to Customer Credit Transfer**
Use Case p.8.1.1 – High Level FI to FI Customer Credit Transfer (pacs.008) settled over a Payment Market Infrastructure
Use Case p.8.1.2 – High Level FI to FI Customer Credit Transfer (pacs.008) Sweeps (Short position at the Secondary Account)
**Cover Method Financial Institution to Financial Institution to Customer Credit Transfer**
Use Case p.8.2.1 - High Level FI to FI Customer Credit Transfer settled using the cover method (pacs.009 COV) over a Payment Market Infrastructure
Use Case p.8.2.2 - High Level FI to FI Customer Credit Transfer involved a serial leg into a cover method (pacs.009 COV)
Use Case p.8.2.3 - High Level FI to FI Customer Credit Transfer involved a serial leg in and out of a cover method (pacs.009 COV)
Use Case p.8.2.4 - High Level FI to FI Customer Credit Transfer involved a serial leg out of a cover method (pacs.009 COV)

---

<!-- Page 238 -->

# Market Infrastructure

**Diagram Flow:**
1 → 2 (pac s.008 / pac s.002) → 3 (pac s.008 / pac s.002) → 4 (pac s.008) → 5 (pac s.008 / pac s.002) → 6
*Settlement Complete*

**Step Details:**

**1**
Debtor initiates a payment instruction to the Debtor Agent.

**2**
Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries, who are direct participants of the Payment

**3**
Agent B processes the payment on Agent C, via the Payment Market Infrastructure.

**4**
Payment Market Infrastructure, settles the payment between Agent B and Agent C as direct participants of the Market Infrastructure, and provides a

**5**
Agent C processes the payment onto Agent D.

**6**
Agent D credits the account of the Creditor, and may optionally provide a notification e.g. credit notification in addition to an

---

<!-- Page 239 -->

# Authorised Party

**Diagram Flow:**
*   **DA**: Debit Authorisation
*   **2**: Interbank pain.001 / Interbank pain.002
*   **3**: pacs.008 / pacs.002
*   **4**: camt.053

**Step Descriptions:**

**DA**
As a pre-requisite the Debtor provides Debit Authorisation to Agent I to Initiate Payment from their account with the Debtor Agent (A)

**2**
Agent (I) initiates a payment request (pain.001) to the Debtor Agent (A) to move fund from the Debtor's account, as an

**3**
Debtor Agent (A) debits the account of Debtor and initiates a credit transfer

**3a**
Debtor Agent (A) optionally provides a status update to the Initiating Party (Agent I), based upon a bilateral agreement

**4**
Creditor Agent (B) receives the credit transfer message, credits the Creditor, and sends a camt.053 (statement) at the end of the business day to the Creditor. An optional status report is sent to the previous Agent based upon a bilateral agreement

**Note:**
See use case pn.1.2.1 for an Authorised Party Payment.

---

<!-- Page 240 -->

# (pacs.009 COV) over a Payment Market Infrastructure

**Diagram flow (top row):** Agent → (1) → Agent A → (2a) `pacs.008` → Agent D → (7) → Creditor
**Return flow:** Agent D → (2b) `pacs.002` → Agent A
**Diagram flow (bottom row):** Agent A → (2b) `pacs.009 cov` / `pacs.002` → Agent B → (3) `pacs.009 cov` / `pacs.002` → Payment Market Infrastructure → (4) `pacs.009 cov` → Agent C → (5) → (6) `camt.053` / `camt.054` → Agent D
**Settlement Complete**

1. Debtor initiates a payment instruction to the Debtor Agent

2a. Debtor Agent (A) initiates a payment using the cover method to the Creditor Agent (D)

2b. In parallel the Debtor Agent (A) initiates a covering payment to credit the account of Agent (D) with their correspondent (Agent

3. Agent B processes the payment on Agent C, via the Payment Market Infrastructure

4. Payment Market Infrastructure, settles the payment between Agent B and Agent C as direct participants of the Market Infrastructure, and provides a settlement confirmation to Agent B

5. Agent C receives the payment and credits the account of Agent D

6. Agent C produces an end of day account statement report. An optional real time notification e.g. advice of credit may have also been created at the time of the credit posting

7. Agent D reconciles the covering funds and credits the account of the Creditor, and may optionally provide a notification e.g. credit notification

---

<!-- Page 241 -->

# method (pac.009 COV)

**1** Debtor initiates a payment instruction to the Debtor Agent

**2** Debtor Agent (A) initiates a payment using the serial method towards the Creditor Agent (E)

**3a** Agent B initiates a payment using the cover method towards the Creditor Agent (E) by sending a direct pac.008 to Agent E who they have business relationship with

**3b** In parallel the Agent (B) initiates a covering payment to credit the account of Agent (E) with their correspondent (Agent D)

**4** Agent E receives the payment instruction and credits the account of the Creditor, and may optionally provide a notification e.g. credit notification. Alternatively, they may have chosen to await until settlement occurred in Step 6 based upon their risk appetite.

**5** Agent C processes the payment on Agent D, using a correspondent banking business relationship

**6** Agent D receives the payment and credits the account of Agent E. Agent D produces an end of day account statement report. An optional real time notification e.g. advice of credit may have also been created at the time of the credit posting

Diagram message labels: pac.008, pac.002, pac.009 cov, camt.053, camt.054

Agents: A, B, C, D, E

---

<!-- Page 242 -->

# of a cover method (pacs.009 COV)

**Diagram message flow (nodes A → B → E → F, with C → D):**

- 1: (Debtor) → A
- 2: A → B `pacs.008` / B → A `pacs.002`
- 3a: B → E `pacs.008` / E → B `pacs.002`
- 3b: B → C `pacs.009 cov` / C → B `pacs.002`
- 4: C → D `pacs.009 cov` / D → C `pacs.002`
- 5: D → E `camt.052` / E → D `camt.056`
- 6: E → F `pacs.008` / F → E `pacs.002`
- 7: F → (Creditor)

**1**
Debtor initiates a payment instruction to the Debtor Agent

**2**
Debtor Agent (A) initiates a payment using the serial method towards the Creditor Agent (F)

**3a**
Agent B initiates a payment using the cover method towards the Creditor Agent (F) by sending a direct pacs.008 to Agent E who they have business relationship with.

**3b**
In parallel the Agent (B) initiates a covering payment to credit the account of Agent (E) with their correspondent banking business relationship

**4**
Agent E receives the payment instruction and process the payment on to Agent F. Alternatively they may have chosen to await until settlement occurred in Step 6 based upon their risk appetite.

**5**
Agent C processes the payment on Agent D, using a correspondent banking business relationship

**6**
Agent D receives the payment and credits the account of Agent E. Agent D produces an end of day account statement report. An optional real time notification e.g. advice of credit may have also been created at the time of the credit posting

**7**
Agent F receives the payment and credits the account of the Creditor, and may optionally provide a notification e.g. credit notification.

---

<!-- Page 243 -->

# cover method (pacs.009 COV)

**Flow diagram (sequence of messages between agents):**

- **1** Debtor → Agent **A**
- **2a** Agent **A** → Agent **D** : `pacs.008` (return `pacs.002`)
- **2b** Agent **A** → Agent **B** : `pacs.009 cov` (return `pacs.002`)
- **3** Agent **B** → Agent **D** : `camt.052` / `camt.054`
- **4** Agent **D** → Agent **E** : `pacs.008` (return `pacs.002`)
- **5** Agent **B** → Agent **C** : `pacs.009 cov` (return `pacs.002`)
- **6** Agent **C** → Agent **D**
- **4** Agent **E** → Creditor

**Step descriptions:**

**1**
Debtor initiates a payment instruction to the Debtor Agent

**2a**
Debtor Agent (A) initiates a payment using the cover method towards the Creditor Agent (E) by sending a direct pacs.008 to Agent D who they have business relationship with

**2b**
In parallel the Agent (A) initiates a covering payment to credit the account of Agent (D) with their correspondent (Agent C)

**3**
Agent D receives the payment instruction and process the payment on to Agent E. Alternatively they may have chosen to await until settlement occurred in Step 6 based upon their

**4**
Agent E receives the payment and credits the account of the Creditor, and may optionally provide a notification e.g. credit notification.

**5**
Agent B processes the payment on Agent C, using a correspondent banking business relationship

**6**
Agent C receives the payment and credits the account of Agent D. Agent C produces an end of day account statement report. An optional real time notification e.g. advice of credit may have also been created at the time of the credit posting

---

<!-- Page 244 -->

# Financial Institution to Financial Institution Customer Credit Transfer

---

<!-- Page 245 -->

pacs.008

- Group Header
- Credit Transfer Transaction Information

The pacs.008 STP has two core sets of nested elements:

- **Group Header** which contains a set of characteristics that relates to all individual transaction
- **Credit Transfer Transaction Information** which contains elements providing information specific to the individual credit transfer transaction.

Payment messages in a many-to-many payment are considered as a single transaction. The pacs.008 STP is a message who's Usage Guideline has been further restricted by remove elements considered

---

<!-- Page 246 -->

A

B

C

D

pacs.008 STP

pacs.002

pacs.008 STP

pacs.002

pacs.008 STP

pacs.002

The Financial Institution To Financial Institution Customer Credit Transfer message is sent by the Debtor Agent to the Creditor Agent, directly or through other agents and/or a payment clearing and settlement system. It is used to move funds from a Debtor account to a

---

<!-- Page 247 -->

The pacs.008 STP message has enhance STP feature over and above the pacs.008 and legacy MT 103 STP. At a high level the key difference between the pacs.008 and pacs.008 STP are summarized.

| | **pac.008** | **pac.008** |
| :--- | :---: | :---: |
| **Business Application Header** | | |
| **Business Service** | `swift.cbprplus.02` | `swift.cbprplus.stp.02` |
| **Credit Transfer Transaction Information** | | |
| Previous Instructing Agent 1 <br> Previous Instructing Agent 2 <br> Previous Instructing Agent 3 <br> Intermediary Agent 1 <br> Intermediary Agent 2 <br> Intermediary Agent 3 <br> Debtor Agent <br> Creditor Agent | Financial Institution identifiers: <br> • BIC <br> • Clearing System Member Id <br> • LEI <br> • Name <br> • Postal Address | Financial Institution identifiers: <br> • BIC <br> • Clearing System Member Id <br> • LEI <br> ~~Name~~ *removed* <br> ~~Postal Address~~ *removed* |
| Debtor <br> Creditor | `Account optional` | `Addition Debtor and Creditor IBAN rules` |
| Creditor Account | `Elements optional` | `Account mandatory` |
| Instruction for Next Agent <br> Instruction for Creditor Agent | | ~~Instruction for Next Agent~~ *removed* <br> ~~Instruction for Creditor Agent~~ *removed* |

---

<!-- Page 248 -->

# Financial Institution
# Credit Transfer

---

<!-- Page 249 -->

| **pac.009** | **pac.009 (COV)** |
| :--- | :--- |
| Group Header | Group Header |
| Credit Transfer Transaction Information | Credit Transfer Transaction Information |
| | Underlying Customer Credit Transfer |

The pac.009 has two main use cases:

* as a core Financial Institution Credit Transfer message.
* As a **COV** where it is used as cover of (to settle) a pac.008.

The pac.009 therefore contain information of the underlying Customer Credit Transfer (pac.008) for use in the cover scenario, which is the key attribute to differentiate between these two use cases.

The pac.009 may also be used as a **ADV** where it is sent as an advice and is settled using the pac.009 as a core message.

---

<!-- Page 250 -->

A B C D

| From | To | Message |
|------|----|---------|
| A | B | pac.009 |
| B | A | pac.002 |
| B | C | pac.009 |
| C | B | pac.002 |
| C | D | camt.053 |

The Financial Institution Credit Transfer message is sent by a Debtor Financial Institution to a Creditor Financial Institution, directly or through other agents and/or a payment clearing and settlement system. It is used to move funds from a debtor account to a creditor, where both Debtor and Creditor are **Financial Institutions**.

---

<!-- Page 251 -->

# Group Header

---

<!-- Page 252 -->

Each ISO 20022 payment message has a **Min1 - Max1** ***Message Identification*** element, located in the Group Header. This **35 character** identifier is a point-to-point reference used to unambiguously identify the message.

For Payment Clearing and Settlement (pacs) messages the Message Identification has no exact equivalent in the legacy MT payment message. However, the MT 202 Sender's Reference (Field 20) could be considered a similar comparison where a pacs message contains a single Transaction.

Each transaction's *Credit Transfer Transaction Information* contains a variety of nested *Payment Identification* elements to capture reference related to the individual transaction such as a UETR (Unique End-to-end Transaction Reference)

---

<!-- Page 253 -->

Min 1 - Max 1

The pacs.009 message ***Creation Date*** captures the date and time which the message was created.

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset `YYYY-MM-DDThh:mm:ss.sss+/-hh:mm`
> For example: `2002-10-10T12:00:00-05:00` (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- Page 254 -->

Min 1 – Max 1

The pacs.009 message **Number of Transactions** captures the number of individual transaction contained within the message.

The number of transactions in CBPR+ payment usage guidelines is fixed to 1.

Single transactions in the CBPR+ payment usage guidelines enable a transaction to be managed and unlocks highly automated, frictionless, instant payments, supporting the next generation of innovation.

Group Header: Number of Transactions

---

<!-- Page 255 -->

Min 1 – Max 1
The pacs.009 **Settlement Method** element within the Group Header *Settlement Information*, includes one of the embedded codes to indicate how the payment message will be settled.

The *Settlement Method* element in the pacs.009 allows a choice of an embedded code.

**INDA** indicate this Customer Credit Transfer will be settlement by the Instructed Agent (as the Account Servicing Institution) The account held at the Instructed Agent may captured in the dedicated **Settlement Account** element.
**INGA** indicate this Customer Credit Transfer has already been settlement by the Instructing Agent, who has credited the Account they service for the Instructed Agent (as an Account Owner). The account held by the Instructed Agent with the Instructing Agent may captured in the dedicated **Settlement Account** element.

Settlement Method code CLRG is not part of CBPR+ specifications but instead used in Market Infrastructure specification (HVPS+)

---

<!-- Page 256 -->

The pacs.009 message *Settlement Account* is a nested element as part of *Settlement Information*, this element identifies information related to an account used to settle the payment instruction.

Min 0 – Max 1
The *Settlement Account* identifies the account details maintained at the account servicing institution (Agent responsible for the settlement of the instruction as indicated in the *Settlement Method*)

Min 1 – Max 1
*Identification* identifies the account maintained at the Debtor Agent (Account Servicing Institution)

Min 0 – Max 1
*Type* uses the external Cash Account Type code list to identify the type of account

Min 0 – Max 1
*Currency* identifies the currency if the account

Min 0 – Max 1
*Name* identifies the name of the account as assigned by the Account Servicing Institution

Min 0 – Max 1
*Proxy* captures an alternative identification of the account number such as an email address. This element has further nested *Type* which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used.

---

<!-- Page 257 -->

# Credit Transfer Transaction Information

---

<!-- Page 258 -->

The pacs message *Payment Identification* provides a set of elements to identify the payment, of which several are mandatory elements

**Payment Identification**

**Instruction Identification**
Min 1 – Max 1

a *point-to-point reference* restricted in CBPR+ to 16 character and directly comparable with the Sender's Reference (Field 20) of the legacy MT payment message.

**End to End Identification**
Min 1 – Max 1

an *end-to-end reference* provided by the *Debtor* which must be passed unchanged throughout the payment and reported to the Creditor.

note: for a pacs.009 COV the end-to-end id is provided by the Debtor from the pacs.008 instruction id.

In a pacs.009 COR if the Debtor has not provide an end-to-end identifier, the *Debtor Agent* may populate "NOTPROVIDED" to comply the mandatory need of this element.

**UETR**
Min 1 – Max 1

the *end-to-end Transaction* Reference created using the UUIDv4 standard. This reference must be passed unchanged throughout the payment, it may also be created by the Debtor within their Payment Initiation request, and also included in reporting

---

<!-- Page 259 -->

Min 1 – Max 1

The `pac` message ***Payment Identification*** also provides a set of optional elements to identify the payment.

## Payment Identification

**Transaction Identification**
Min 0 – Max 1
an **end-to-end reference** assigned by the first Instructing Agent to identify the transaction.

**Clearing System Reference**
Min 0 – Max 1
a **point-to-point reference** populated by a Payment Market Infrastructure, typically to the settlement leg of a clearing system transaction as a reference to the settled clearing transaction.

---

<!-- Page 260 -->

The pacs message *Payment Type Information* provides a set of optional elements where the payment type can be described.

**Min 0 – Max 1**

a choice of imbedded codes representing the urgency considered by the Instructing Agent, this point-to-point information may be used by the Instructed Agent to differentiate the processing priority.

**Instruction Priority**
Min 0 – Max 1

**Service Level**
Min 0 – Max 3

A nested element which may either use an external ISO Service Level code* or a proprietary code. It is used to identify a particular agreed service level which should be applied to the payment.

For example, code G001 can be used to identify a gpi Tracked Cover Transfer similarly to Field 111 value 001 in the MT 202 COV

**Local Instrument**
Min 0 – Max 1

A nested element which may either use an external ISO Local Instrument code or a proprietary code. It is used to identify the type of payment local instrument such as a Standing Order.

Note: the ISO instrument codes are registered by specific community group (captured in the code list)

a choice of imbedded codes representing the clearing channel to be used to process the payment. e.g., RTGS

**Clearing Channel**
Min 0 – Max 1

**Payment Type Information**

**Category**

A nested element which may either use an external ISO Category Purpose code or a proprietary code. It is used to

---

<!-- Page 261 -->

The pacs.009 message (unlike the pacs.008) has only one element to capture the amount of the Credit Transfer, **Interbank Settlement Amount**.

**Min 1 – Max 1**

**Interbank Settlement Amount**

A mandated *currency amount* moved between the *Instructing Agent* and the *Instructed Agent*. This therefore is the point-to-point currency amount exchanged, comparable with the MT Field 32A

**Min 1 – Max 1**

**Interbank Settlement Date**

A mandated *date* on which the *Interbank Settlement* should be executed between the *Instructing Agent* and the *Instructed Agent*. This therefore is the **value date** comparable with the MT Field 32A

Note: the Financial Institution Credit Transfer (pacs.009) has no *Instructed Amount* element, *Exchange Rate* or *Charger Bearer* (unlike the pacs.008) as the Instructed Settlement Amount is expected to be transferred across the end-to-end payment chain without any charges being applied or currency conversions.

---

<!-- Page 262 -->

# Request

The pacs.009 message has three optional elements to capture the optional information related to the settlement of the instructions.

**Min 0 – Max 1**

The **Settlement Priority** provides an optional choice of embedded codes to indicate the instruction's settlement priority from the perspective of the Instructing Agent. This point-to-point information may be used by the Instructed Agent to identify the priority associated with the **Settlement Method** and should not be confused with the *Instruction Priority*.

> Note: Where the **Settlement Method** of the pacs.009 is 'INDA' (settled performed by the Instructed Agent) this indicates the Settlement Priority. Code 'INGA' implies settlement has already occurred for this point-to-point payment and therefore the Settlement Priority is not necessary.

**Min 0 – Max 1**

The **Settlement Time Indication** optionally captures the time settlement occurred at a transaction administrator such as a Market Infrastructure. This DateTime can be captured in two nested elements, **Debit Date Time** and **Credit Date Time**.

**Min 0 – Max 1**

The **Settlement Time Request** optionally captures the time settlement is requested for the payment instruction by the Instructing Agent. This Time can be capture in four nested elements:

- **CLS Time** the time the amount must be credit to CLS Bank
- **Till Time** the time until which the payment may be settled

---

<!-- Page 263 -->

The pacs message can capture up to 3 Previous Instructing Agents, which represent an Agent who previously only played a dynamic role in the payment between the Debtor Agent and Creditor Agent.

`Min 0 – Max 1`
The **_Previous Instructing Agent 1_** captures the first historic Agent between the Debtor Agent and the Previous Instructing Agent 2 (where present) and the Instructing Agent. This optional element is comparable with the Field 72 first /INS/ occurrence in the legacy FIN message.

`Min 0 – Max 1`
The **_Previous Instructing Agent 1 Account_** captured the account related between this Agent and Previous Instructing Agent 2 (where present) or the Instructing Agent. This optional element has not comparable field in the legacy FIN message

`Min 0 – Max 1`
The **_Previous Instructing Agent 2_** captures the second Previous Instructing Agent between the Previous Instructing Agent 1 and the Previous Instructing Agent 3 (where present) and the Instructing Agent. This optional element is comparable with the Field 72 second /INS/ occurrence in the legacy FIN message.

`Min 0 – Max 1`
The **_Previous Instructing Agent 2 Account_** captured the account related between this Agent and Previous Instructing Agent 2 (where present) or the Instructing Agent. This optional element has not comparable field in the legacy FIN message.

`Min 0 – Max 1`
The **_Previous Instructing Agent 3_** captures the third Previous Instructing Agent between the Agent and the Instructing Agent. This optional element is comparable with the Field 72 third /INS/ occurrence in the legacy FIN message.

`Min 0 – Max 1`
The **_Previous Instructing Agent 3 Account_** captured the account related between this Agent and Previous

---

<!-- Page 264 -->

#

A

B

C

D

pac.009

Instructing Agent: Agent A

Instructed Agent: Agent B

pac.009

Instructing Agent: Agent B

Instructed Agent: Agent C

*Instructing Agent* and *Instructed Agent* represent the Agents involved in the pac point-to-point message exchange. These roles therefore change on each payment leg.

*Instructing Agent* and *Instructed Agent* elements are required in all pac messages and are only available in the **Credit Transfer Information**

Credit Transfer Transaction Information

Instructing Agent

---

<!-- Page 265 -->

# Intermediary Agents

The ISO 20022 pacs messages have a number of optional Agent elements whose roles change throughout the life cycle of the payment. **Intermediary Agent** is an example of this, where these agents are classified in numeric order (i.e. *Intermediary Agent 1*). **Previous Instructing Agent** however is a static role which allows additional Previous Instructing Agent to be appended to the history of the payment.

The below diagram visualizes the change of Agent role at different stages of the payment transaction life cycle.

| A | B | C | D | E | F | G |
|---|---|---|---|---|---|---|
| Debtor | Instructing Agent & Debtor Agent | Instructed Agent | Intermediary Agent 1 | Intermediary Agent 2 | Creditor Agent | Creditor |
| Debtor | Debtor Agent | Instructing Agent | Instructed Agent | Intermediary Agent 1 | Creditor Agent | Creditor |
| Debtor | Debtor Agent | Previous Instructing Agent 1 | Instructing Agent | Instructed Agent | Creditor Agent | Creditor |
| Debtor | Debtor Agent | Previous Instructing Agent 1 | Previous Instructing Agent 2 | Instructing Agent | Creditor Agent & Instructed Agent | Creditor |

---

<!-- Page 266 -->

The pacs message can capture up to 3 Intermediary Agents, which play a dynamic role in the payment between the Debtor Agent and Creditor Agent.

Min 0 – Max 1
The **Intermediary Agent 1** captures the first Intermediary Agent between the Debtor Agent and Creditor Agent for who the Instructed Agent attempt to instruct the payment on to. This optional element is comparable with the Field 56a in the legacy FIN message.

Min 0 – Max 1
The **Intermediary Agent 1 Account** captured the account related to this Intermediary Agent, with the Instructed Agent. This element can be compared to the Party Identifier of the legacy Field 56a.

Min 0 – Max 1
The **Intermediary Agent 2** captures the second Intermediary Agent between the Intermediary Agent 1 and the Creditor Agent. This optional element has not comparable field in the legacy FIN message.

Min 0 – Max 1
The **Intermediary Agent 2 Account** captured the account related to this Intermediary Agent, with the Intermediary Agent 1. This optional element has not comparable field in the legacy FIN message.

Min 0 – Max 1
The **Intermediary Agent 3** captures the third Intermediary Agent between the Intermediary Agent 2 and the Creditor Agent. This optional element has not comparable field in the legacy FIN message.

Min 0 – Max 1
The **Intermediary Agent 3 Account** captured the account related to this Intermediary Agent, with the

---

<!-- Page 267 -->

The ISO 20022 pacs messages describe the Agent whose account is debited for a transaction as the *Debtor*. The *Debtor* sub elements describe the *Debtor* in greater detail.

- Department
- Sub Department
- Street Name
- Building Number
- Building Name
- Floor
- Post Box
- Room
- Post Code
- Town Name
- Town Location Name
- District Name
- Country Sub Division
- Country
  - Code

Postal Address

The BIC which identifies the *Debtor*
**BICFI**

Information used to identify a Debtor by a clearing system identifier.
**Clearing System Member Id**

Legal entity identifier of the financial institution.
**LEI**

**Debtor**

*Name* by which the Agent is known
**Name**

Nested element capturing either structured or unstructured *Debtor* address details
**Postal Address**

---

<!-- Page 268 -->

The pacs.009 *Debtor Account* is used to capture the account information for which debit entry is/has been applied to the Debtor's account, which are also reflected in their account Statement.

The *Debtor Account* uses a variety of nested elements to capture information related to the account.

**Min 1 – Max 1** *Identification* identifies the account maintained at the Debtor Agent (Account Servicing Institution)

**Min 0 – Max 1** *Type* uses the external Cash Account Type code list to identify the type of account

**Min 0 – Max 1** *Currency* identifies the currency if the account

**Min 0 – Max 1** *Name* identifies the name of the account as assigned by the Debtor Agent (Account Servicing Institution)

**Min 0 – Max 1** *Proxy* captures an alternative identification of the account number such as an email address. This element has further nested *Type* which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used.

the pacs.009 the Debtor is a Financial Institution, therefore the nested

---

<!-- Page 269 -->

Min 0 – Max 1 Min 0 – Max 1

The **_Debtor Agent_** and **_Creditor Agent_** are static roles in the pacs.009 FI to FI Customer Credit Transfer. These agent maintain a relationship with their customers; the _Debtor_ and _Creditor_. However, unlike the pacs.008 Debtor Agent and Creditor Agent are optional, which cover the scenario where the Debtor and Creditor (as Financial Institutions) maintain a direct Nostro/Vostro account relationship.

Note: Where the _Debtor_ and _Creditor_ maintain a relationship with the same intermediary counterpart. It is recommended that this Agent is captured in the **_Creditor Agent_** element to align with translation from the legacy MT message.

Credit Transfer Transaction Information

---

<!-- Page 270 -->

# Account

The pacs.009 **Debtor Agent Account** and **Creditor Agent Account** is used to capture the account information related to these Agents. The nature of this element implies there is an Agent or Agent in between the Debtor Agent and Creditor Agent in the payment transaction.

The **Debtor Agent Account** and **Creditor Agent Account** uses a variety of nested elements to capture information related to the account.

| | |
|---|---|
| Min 1 – Max 1 | **Identification** identifies the account maintained at the Creditor Agent (Account Servicing Institution) |
| Min 0 – Max 1 | **Type** uses the external Cash Account Type code list to identify the type of account |
| Min 0 – Max 1 | **Currency** identifies the currency if the account |
| Min 0 – Max 1 | **Name** identifies the name of the account as assigned by the Creditor Agent (Account Servicing Institution) |
| Min 0 – Max 1 | **Proxy** captures an alternative identification of the account number such as an email address. This element has further nested **Type** which is a choice of external code list or proprietary code and **Identification** which are both mandatory where the Proxy element is used. |

Debtor Agent and Creditor Agent are a Financial Institutions, therefore

---

<!-- Page 271 -->

The ISO 20022 pacs messages describe the Agent whose account is credited for a transaction as the **Creditor**. The *Creditor* sub elements describe the *Creditor* in greater detail.

| Postal Address |
|---|
| Department |
| Sub Department |
| Street Name |
| Building Number |
| Building Name |
| Floor |
| Post Box |
| Room |
| Post Code |
| Town Name |
| Town Location Name |
| District Name |
| Country Sub Division |
| Country → Code |
| Address Line |

The BIC which identifies the *Creditor* — **BICFI**

Information used to identify a Debtor by a clearing system identifier. — **Clearing System Member Id**

Legal entity identifier of the financial institution. — **LEI**

**Creditor**

*Name* by which the Agent is known — **Name**

Nested element capturing either structured or unstructured Debtor address details — **Postal Address**

---

<!-- Page 272 -->

The pacs.009 *Creditor Account* is used to capture the account information for which a credit entry is intended to be applied to the Creditor's account, which are also reflected in their account Statement.

The *Creditor Account* uses a variety of nested elements to capture information related to the account.

**Min 1 – Max 1** *Identification* identifies the account maintained at the Creditor Agent (Account Servicing Institution)

**Min 0 – Max 1** *Type* uses the external Cash Account Type code list to identify the type of account

**Min 0 – Max 1** *Currency* identifies the currency if the account

**Min 0 – Max 1** *Name* identifies the name of the account as assigned by the Creditor Agent (Account Servicing Institution)

**Min 0 – Max 1** *Proxy* captures an alternative identification of the account number such as an email address. This element has further nested *Type* which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used.

the pacs.009 the Creditor is a Financial Institution, therefore the

---

<!-- Page 273 -->

The **_Instruction for Next Agent_** and **_Instruction for Creditor Agent_** elements within the pacs.009 Financial Institution Credit Transfer optionally provides information related to the processing of the payment for these Agents.

![](icon-info)

> **Min 0 – Max 2**
> The **_Instruction for Creditor Agent_** element offers a multiplicity of up to 2 occurrences of information. This element enables:
> ➢ the use of 2 embedded **codes** to describe the instruction
> ➢ free format _instruction information_
> ➢ or both, where the free format complements the code.
> The use of this element may be **bilaterally** agreed with the _Creditor Agent_. It must be passed on throughout the life cycle of the transaction until the payment reaches the _Creditor Agent_.
>
> ![](icon-link)
> _The Creditor of the pacs.009 ADV is captured in the pacs.009 (used to settle the pacs.009 ADV) Instruction for Creditor Agent, Instruction Information element preceded by /UDLC/ (UnDerLying Creditor) to provide party transparency in the settlement message._

> **Min 0 – Max 6**
> The **_Instruction for Next Agent_** element offers a multiplicity of up to **6** occurrences of information. This element is restricted to free format _instruction information_ in CBPR+.
> The element is used to provide instruction to the next Agent (which may not be the Creditor Agent)

Credit Transfer Transaction Information ⓘ

---

<!-- Page 274 -->

Min 0 – Max 2

An **Instruction for Creditor Agent** elements within the pacs.009 Financial Institution Credit Transfer, used to settle a pacs.009 Financial Institution Credit Transfer Advice (ADV), provides information related to the Creditor in the advice message (Underlying Creditor).

The *Creditor* of the pacs.009 ADV are commonly captured in one of the following ways:
* As a BIC (**BICFI**) either on its own, or
* As a **Clearing System Member Identification** or a **LEI** with **Name**, and **Postal Address**

> **pacs.009 Instruction for Creditor Agent/Instruction Information.**
> Up to 2 occurrences of Instruction Information may be provided. The last available occurrence of *Instruction Information*, preceded by /UDLC/, must be used to capture the Underlying Creditor provided in the pacs.009 ADV.

| pacs.009 ADV Creditor/Financial Institution | Data example |
|---|---|
| BICFI | ABCDGB22 |
| Clearing System Member Identification | Clearing System Identification | GBDCSC |
| | Member Identification | 205050 |
| LEI | 123456ABCDEFG2T54 |
| Name | ABC BANK |
| Address | Various Structured elements | 252 HIGH STREET LONDON EC1 1WX GB |
| | Unstructured line | 252HIGH STREET |

| pacs.009 Instruction for Creditor Agent/Instruction Information | |
|---|---|
| /UDLC/ABCDGB22 | **BICFI** only. |
| OR | |
| /UDLC/ABC BANK LONDON GB | **Name** and structured **Postal Address** (TownName and Country Code should be prioritised). |
| OR | |
| /UDLC/ABC BANK LONDON EC1 1WX GB | **Name** and unstructured **Address Line** (TownName and Country Code should be prioritised, where possible). |

---

<!-- Page 275 -->

The <span style="background-color:#d9e8f5;">Min 0 – Max 1</span> **Purpose** elements within the pacs.009 Financial Institution Credit Transfer capture the reason for the payment transaction which may either use an external ISO **Purpose code** or a proprietary code. The purpose is used by the capture the nature of the payment e.g., **CORT** Trade Settlement Payment, **CFEE** Cancellation Fees etc. and should not be confused with Regulatory Reporting codes present in the pacs.008.

The externalised Purpose code set is classified by the purpose, for example commercial, for which the numerous codes within the classification are each described by Name and Definition.
For example:
**OTCD** is classified within the Collateral categorisation, with the *Name* **OTC Derivatives** described as a **Cash collateral related to over-the-counter (OTC) Derivatives** - in general for example contracts which are traded and privately negotiated.

*Category Purpose* also captures a high level purpose, which unlike *Purpose* is less granular but can trigger special processing e.g., Category Purpose code **SECU** 'Securities' may trigger pacs.002 *Payment Status Report* to provide update on the progress of the payment to the previous Agent.

Credit Transfer Transaction Information

---

<!-- Page 276 -->

The optional *Remittance Information* element within the pacs.009 Financial Institution Credit Transfer is nested to provide *Unstructured* information related to payment.

**Min 0 – Max 1**
*Remittance Information* enable the matching/reconciliation of an entry that the payment is intended to settle

**Min 0 – Max 1**
The *Unstructured* sub element captures free format *Remittance Information* which is restricted in CBPR+ to 140 characters to ensure backward compatibility with the legacy MT message during coexistence.

Note: unlike the pacs.008 *Remittance Information* can only be captured in an *Unstructured* element in the pacs.009 Financial Institution Credit Transfer. *Remittance Information* is however a dedicated element used both within the pacs and camt reporting messages, whereby this information can travel end-to-end using ISO 2022

Credit Transfer Transaction Info > Remittance Information >

---

<!-- Page 277 -->

> Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases.

**Serial Financial Institution Payments**
Use Case p.9.1.1 – High Level Financial Institution Credit Transfer (pacs.009) settled over a Payment Market Infrastructure
Use Case p.9.1.2 - High Level Financial Institution Credit Transfer (pacs.009) pre-advised settled using pacs.009.

---

<!-- Page 278 -->

# Payment Market Infrastructure

**Diagram Flow:**

1.  **A** → `pacs.009` → **B**
    **B** → `pacs.002` → **A**
2.  **B** → `pacs.009` → **C**
    **C** → `pacs.002` → **B**
    *(Settlement Complete)*
3.  **C** → `pacs.009` → **D**
4.  **D** → `camt.053` → **C**
    **C** → `camt.054` → **D**

---

**1**
Debtor initiates a payment instruction to the Debtor Agent

**2**
Agent B processes the payment on Agent C, via the Payment Market Infrastructure.

**3**
Payment Market Infrastructure, settles the payment between Agent B and Agent C as direct participants of the Market Infrastructure, and provides a settlement confirmation to Agent B

**4**
Agent C credits the account of the Creditor (Agent D), and may optionally provide a notification e.g. credit notification in addition to an account statement (camt.054) in addition to a customer statement (camt.053)

---

<!-- Page 279 -->

# pacs.009 (advice)

**Flow / Message labels:** A → B → E (pacs.009 (ADV)); E → F (camt.054); B → C (pacs.009); C → B (pacs.002); C → D (pacs.009); D → C (pacs.002); D → E (camt.053, camt.054).

**1**
Debtor initiates a payment instruction to the Debtor Agent

**2a**
Debtor Agent (B) provided a notification to Creditor Agent (E) using a pacs.009 advice to indicate a 'pre-advice and provides the related payment details (in step 2b) This provides Agent E the ability to take the payment amount into their position, particularly where final settlement in step 5 occur after their business day. (i.e. time zone differences between the various Agent in the payment chain.

**2b**
In parallel the Debtor Agent (B) initiates a payment to credit the account of Agent (E) as the creditor in the pacs.009 settlement message

**3**
Agent C processes the payment on to Agent D

**4**
Agent D credits the account of Agent E and should provide a notification e.g. credit notification (camt.054) in addition to a customer statement (camt.053)

**5**
Agent E receives the payment and credits the account of Agent F as the Creditor, and may optionally provide a notification e.g. credit notification.

---

<!-- Page 280 -->

# Financial Institution
# Credit Transfer

---

<!-- Page 281 -->

pacs.009 (ADV)

Group Header

Credit Transfer Transaction Information

The pacs.009 advice is used to pre-advice an Agent of a fund movement toward the Creditor.

The core pacs.009 is used to perform the settlement of this pre-advice message.

---

<!-- Page 282 -->

pac.009
pac.009 ADV
pac.002
pac.009
pac.002
camt.053

The Financial Institution Credit Transfer (advice) message is sent by a Debtor Agent to a Creditor Agent, directly. In this context the pac.009 ADV is used as a direct advice message.
It is used to move funds from a debtor account to a creditor, where both Debtor and Creditor are **Financial Institutions**.

To provide party transparency in the pac.009 ADV, the **Debtor** of the pac.009 ADV remains the **Debtor** of

---

<!-- Page 283 -->

# Group Header

---

<!-- Page 284 -->

Each ISO 20022 payment message has a **Min1 - Max1** ***Message Identification*** element, located in the Group Header. This **35 character** identifier is a point-to-point reference used to unambiguously identify the message.

For Payment Clearing and Settlement (pacs) messages the Message Identification has no exact equivalent in the legacy MT payment message. However, the MT 202 Sender's Reference (Field 20) could be considered a similar comparison where a pacs message contains a single Transaction.

Each transaction's *Credit Transfer Transaction Information* contains a variety of nested *Payment Identification* elements to capture reference related to the individual transaction such as a UETR (Unique End-to-end Transaction Reference)

---

<!-- Page 285 -->

Min 1 - Max 1

The pacs.009 message ***Creation Date*** captures the date and time which the message was created.

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset `YYYY-MM-DDThh:mm:ss.sss+/-hh:mm`
> For example: `2002-10-10T12:00:00-05:00` (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- Page 286 -->

Min 1 – Max 1

The pacs.009 message **Number of Transactions** captures the number of individual transaction contained within the message.

The number of transactions in CBPR+ payment usage guidelines is fixed to 1.

Single transactions in the CBPR+ payment usage guidelines enable a transaction to be managed and unlocks highly automated, frictionless, instant payments, supporting the next generation of innovation.

Group Header: Number of Transactions

---

<!-- Page 287 -->

Min 1 – Max 1

The pacs.009 **Settlement Method** element within the Group Header *Settlement Information*, includes one of the embedded codes to indicate how the payment message will be settled.

The **Settlement Method** *element* in the pacs.009 ADV is fixed to **COVE**. This indicate this advice of Financial Institution Credit Transfer will be settlement using a covering pacs.009.

Like the pacs.008, the Agents being used in the covering payment to reimburse the Instructed Agent can be provided in the dedicated Reimbursement Agent elements. This allows the Instructed Agent to identify the debit account on their books from the Reimbursement Agent account or look up the account related to the reimbursement agent.

---

<!-- Page 288 -->

The pacs message captures a number of Reimbursement Agents as a sub element to **_Settlement Information_** these elements detail the Agent in the cover method who will process the pacs.009 cover. These elements are similar in nature to the Field 53, 54 and 55 in legacy MT messages and are referred to as The **_Instructing Reimbursement Agent_**, and **_Instructed Reimbursement Agent_**. Each of these reimbursement agents also has a dedicated account element to optionally capture their related account details.

> Min 0 – Max 1
> The **_Instructing Reimbursement Agent_** captures the Agent who will execute a covering payment (i.e. pacs.009 COV or domestic equivalent) often referred to as the currency correspondent. This optional element is comparable with the Field 53a in the legacy FIN message.

> Min 0 – Max 1
> The **_Instructing Reimbursement Agent Account_** captured the account related to this Reimbursement Agent. This element can be compared to the Party Identifier of the legacy Field 53.

> Min 0 – Max 1
> The **_Instructed Reimbursement Agent_** captures the Agent who will receive the covering payment (i.e., pacs.009 cov or domestic equivalent) and credit the account of the pacs.008 FI to FI Customer Credit Transfer *Instructed Agent*. This optional element is comparable with the Field 54a in the legacy FIN message.

> Min 0 – Max 1
> The **_Instructed Reimbursement Agent Account_** captured the account related to this Reimbursement Agent. This element can be compared to the Party Identifier of the legacy Field 54.

---

<!-- Page 289 -->

# Credit Transfer Transaction Information

---

<!-- Page 290 -->

The pacs message *Payment Identification* provides a set of elements to identify the payment, of which several are mandatory elements

**Instruction Identification**
Min 1 – Max 1

- a point-to-point reference restricted in CBPR+ to 16 character and directly comparable with the Sender's Reference (Field 20) of the legacy MT payment message.
- Note: this reference must be transported in the *End-to-End Identification* of the pacs.009 message used to settle the pacs.009 ADV

**End to End Identification**
Min 1 – Max 1

- an end-to-end reference provided by the *Debtor* which must be passed unchanged throughout the payment and reported to the Creditor.
- note: In a pacs.009 ADV if the Debtor has not provide an end-to-end identifier, the *Debtor Agent* may populate "NOTPROVIDED" to comply the mandatory need of this element.

**UETR**
Min 1 – Max 1

- the end-to-end *Transaction* Reference created using the UUIDv4 standard. This reference must be passed unchanged throughout the payment, it may also be created by the Debtor within their Payment Initiation request, and also included in reporting

---

<!-- Page 291 -->

Min 1 – Max 1

The `pac` message ***Payment Identification*** also provides a set of optional elements to identify the payment.

## Payment Identification

**Transaction Identification**
Min 0 – Max 1
an **end-to-end reference** assigned by the first Instructing Agent to identify the transaction.

**Clearing System Reference**
Min 0 – Max 1
a **point-to-point reference** populated by a Payment Market Infrastructure, typically to the settlement leg of a clearing system transaction as a reference to the settled clearing transaction.

---

<!-- Page 292 -->

The pacs message **Payment Type Information** provides a set of optional elements where the payment type can be described.

a choice of imbedded codes representing the urgency considered by the Instructing Agent, this point-to-point information may be used by the Instructed Agent to differentiate the processing priority.

**Instruction Priority**
Min 0 – Max 1

a choice of imbedded codes representing the clearing channel to be used to process the payment. e.g., RTGS

**Clearing Channel**
Min 0 – Max 1

# Payment Type Information

**Service Level**
Min 0 – Max 3

A nested element which may either use an external ISO Service Level code* or a proprietary code. It is used to identify a particular agreed service level which should be applied to the payment.

For example, code G001 can be used to identify a gpi Tracked Cover Transfer similarly to Field 111 value 001 in the MT 202 COV

**Local Instrument**
Min 0 – Max 1

A nested element which may either use an external ISO Local Instrument code or a proprietary code. It is used to identify the type of payment local instrument such as a Standing Order.

Note: the ISO instrument codes are registered by specific community group (captured in the code list)

**Category**

A nested element which may either use an external ISO Category Purpose code or a proprietary code. It is used

---

<!-- Page 293 -->

## Date

The pacs.009 message (unlike the pacs.008) has only one element to capture the amount of the Credit Transfer, **Interbank Settlement Amount**.

`Min 1 – Max 1`

**Interbank Settlement Amount**

A mandated **currency amount** moved between the *Instructing Agent* and the *Instructed Agent*. This therefore is the point-to-point currency amount exchanged, comparable with the MT Field 32A

**Interbank Settlement Date**

A mandated **date** on which the *Interbank Settlement* should be executed between the *Instructing Agent* and the *Instructed Agent*. This therefore is the **value date** comparable with the MT Field 32A

Note: the Financial Institution Credit Transfer (pacs.009) has no *Instructed Amount* element, *Exchange Rate* or *Charger Bearer* (unlike the pacs.008) as the Instructed Settlement Amount is expected to be transferred across the end-to-end payment chain without any charges being applied or currency conversions.

---

<!-- Page 294 -->

## & Request

The pacs.009 message has three optional elements to capture the optional information related to the settlement of the instructions.

**Min 0 - Max 1**

The **Settlement Priority** provides an optional choice of embedded codes to indicate the instruction's settlement priority from the perspective of the Instructing Agent. This point-to-point information may be used by the Instructed Agent to identify the priority associated with the **Settlement Method** and should not be confused with the *Instruction Priority*.

Note: As the **Settlement Method** of the pacs.009 (ADV) is 'COVE' (settled via a covering pacs.009) Settlement Priority is relevant to the covering payment not the pacs.009 ADV

**Min 0 - Max 1**

The **Settlement Time Indication** optionally captures the time settlement occurred at a transaction administrator such as a Market Infrastructure.
This DateTime can be captured in two nested elements, **Debit Date Time** and **Credit Date Time**.

**Min 0 - Max 1**

The **Settlement Time Request** optionally captures the time settlement is requested for the payment instruction by the Instructing Agent. This Time can be capture in four nested elements:
* **CLS Time** the time the amount must be credit to CLS Bank
* **Till Time** the time until which the payment may be settled
* **From Time** the time from which the payment may be settled

---

<!-- Page 295 -->

#

A

B

C

D

pac.009

Instructing Agent: Agent A

Instructed Agent: Agent B

pac.009

Instructing Agent: Agent B

Instructed Agent: Agent C

*Instructing Agent* and *Instructed Agent* represent the Agents involved in the pac point-to-point message exchange. These roles therefore change on each payment leg.

*Instructing Agent* and *Instructed Agent* elements are required in all pac messages and are only available in the **Credit Transfer Information**

Credit Transfer Transaction Information

Instructing Agent

---

<!-- Page 296 -->

# Intermediary Agents

Unlike the other pacs.009 messages in the CBPR+ collection, the pacs.009 ADV message is exchanged directly between the Debtor Agent (as an Instructing Agent) and Creditor Agent (as an Instructed Agent). The roles of previous Instructing Agents and Intermediary Agents are therefore irreverent in the pacs.009 (ADV)

| A | B | C | D | E | F | G |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Debtor | Instructing Agent & Debtor Agent | Instructed Agent | Intermediary Agent 1 | Intermediary Agent 2 | Creditor Agent | Creditor |
| Debtor | Debtor Agent | Instructing Agent | Instructed Agent | Intermediary Agent 1 | Creditor Agent | Creditor |
| Debtor | Debtor Agent | Previous Instructing Agent 1 | Instructing Agent | Instructed Agent | Creditor Agent | Creditor |
| Debtor | Debtor Agent | Previous Instructing Agent 1 | Previous Instructing Agent 2 | Instructing Agent | Creditor Agent & Instructed Agent | Creditor |

---

<!-- Page 297 -->

The ISO 20022 pacs messages describe the Agent whose account is debited for a transaction as the *Debtor*. The *Debtor* sub elements describe the *Debtor* in greater detail.

- Department
- Sub Department
- Street Name
- Building Number
- Building Name
- Floor
- Post Box
- Room
- Post Code
- Town Name
- Town Location Name
- District Name
- Country Sub Division
- Country
  - Code

Postal Address

The BIC which identifies the *Debtor*
**BICFI**

Information used to identify a Debtor by a clearing system identifier.
**Clearing System Member Id**

Legal entity identifier of the financial institution.
**LEI**

**Debtor**

*Name* by which the Agent is known
**Name**

Nested element capturing either structured or unstructured *Debtor* address details
**Postal Address**

---

<!-- Page 298 -->

The pacs.009 *Debtor Account* is used to capture the account information for which debit entry is/has been applied to the Debtor's account, which are also reflected in their account Statement.

The *Debtor Account* uses a variety of nested elements to capture information related to the account.

**Min 1 – Max 1** *Identification* identifies the account maintained at the Debtor Agent (Account Servicing Institution)

**Min 0 – Max 1** *Type* uses the external Cash Account Type code list to identify the type of account

**Min 0 – Max 1** *Currency* identifies the currency if the account

**Min 0 – Max 1** *Name* identifies the name of the account as assigned by the Debtor Agent (Account Servicing Institution)

**Min 0 – Max 1** *Proxy* captures an alternative identification of the account number such as an email address. This element has further nested *Type* which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used.

the pacs.009 the Debtor is a Financial Institution, therefore the nested

---

<!-- Page 299 -->

Min 0 – Max 1 Min 0 – Max 1
The ***Debtor Agent*** and ***Creditor Agent*** are static roles in the pacs.009 FI to FI Customer Credit Transfer. These agent maintain a relationship with their customers; the ***Debtor*** and ***Creditor***. However, unlike the pacs.008 Debtor Agent and Creditor Agent are optional, which cover the scenario where the Debtor and Creditor (as Financial Institutions) maintain a direct Nostro/Vostro account relationship.

Note: Where the ***Debtor*** and ***Creditor*** maintain a relationship with the same intermediary counterpart. It is recommended that this Agent is captured in the ***Creditor Agent*** element to align with translation from the legacy MT message.

Credit Transfer Transaction Information

---

<!-- Page 300 -->

# Agent Account

The pacs.009 **Min 0 – Max 1** *Debtor Agent Account* and *Creditor Agent Account* is used to capture the account information related to these Agents. The nature of this element implies there is an Agent or Agent in between the Debtor Agent and Creditor Agent in the payment transaction.

The *Debtor Agent Account* and *Creditor Agent Account* uses a variety of nested elements to capture information related to the account.

**Min 1 – Max 1** *Identification* identifies the account maintained at the Creditor Agent (Account Servicing Institution)

**Min 0 – Max 1** *Type* uses the external Cash Account Type code list to identify the type of account

**Min 0 – Max 1** *Currency* identifies the currency if the account

**Min 0 – Max 1** *Name* identifies the name of the account as assigned by the Creditor Agent (Account Servicing Institution)

**Min 0 – Max 1** *Proxy* captures an alternative identification of the account number such as an email address. This element has further nested *Type* which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used.

Debtor Agent and Creditor Agent are a Financial Institutions, therefore

---

<!-- Page 301 -->

The ISO 20022 pacs messages describe the Agent whose account is credited for a transaction as the **Creditor**. The *Creditor* sub elements describe the *Creditor* in greater detail.

| Postal Address |
|---|
| Department |
| Sub Department |
| Street Name |
| Building Number |
| Building Name |
| Floor |
| Post Box |
| Town |
| Post Code |
| Town Name |
| Town Location Name |
| District Name |
| Country Sub Division |
| Country — Code |
| Address Line |

The BIC which identifies the *Creditor* — **BICFI**

Information used to identify a Debtor by a clearing system identifier. — **Clearing System Member Id**

Legal entity identifier of the financial institution. — **LEI**

**Creditor**

*Name* by which the Agent is known — **Name**

The *Creditor* of the pacs.009 ADV is captured in the pacs.009 (used to settle the pacs.009 ADV) Instruction for Creditor Agent. Instruction Information element preceded by /UDLC/ (UDLDelegating Creditor) to provide party

Nested element capturing either structured or unstructured Debtor address details. — **Postal Address**

---

<!-- Page 302 -->

pacs.009

`Min 0 – Max 1` The **_Creditor Account_** is used to capture the account information for which a credit entry is intended to be applied to the Creditor's account, which are also reflected in their account Statement.

The **_Creditor Account_** uses a variety of nested elements to capture information related to the account.

`Min 1 – Max 1` **_Identification_** identifies the account maintained at the Creditor Agent (Account Servicing Institution)

`Min 0 – Max 1` **_Type_** uses the external Cash Account Type code list to identify the type of account

`Min 0 – Max 1` **_Currency_** identifies the currency if the account

`Min 0 – Max 1` **_Name_** identifies the name of the account as assigned by the Creditor Agent (Account Servicing Institution)

`Min 0 – Max 1` **_Proxy_** captures an alternative identification of the account number such as an email address. This element has further nested **_Type_** which is a choice of external code list or proprietary code and **_Identification_** which are both mandatory where the Proxy element is used.

For the pacs.009 the Creditor is a Financial Institution, therefore the

---

<!-- Page 303 -->

The *Instruction for Next Agent* and *Instruction for Creditor Agent* elements within the pacs.009 Financial Institution Credit Transfer optionally provides information related to the processing of the payment for these Agents.

Min 0 – Max 2

The *Instruction for Creditor Agent* element offers a multiplicity of up to 2 occurrences of information. This element enables:
➢ the use of 2 *embedded codes* to describe the instruction
➢ free format *instruction information*
➢ or both, where the free format complements the code.
The use of this element may be *bilaterally* agreed with the *Creditor Agent*. It must be passed on throughout the life cycle of the transaction until the payment reaches the *Credit Agent*.

Min 0 – Max 6

The *Instruction for Next Agent* element offers a multiplicity of up to 6 occurrences of information. This element is restricted to free format *instruction information* in CBPR+.
The element is used to provide instruction to the next Agent (which may not be the Creditor Agent)

Credit Transfer Transaction Information

---

<!-- Page 304 -->

The **Min 0 – Max 1** **Purpose** elements within the pacs.009 Financial Institution Credit Transfer capture the reason for the payment transaction which may either use an external ISO **Purpose code** or a proprietary code. The purpose is used by the capture the nature of the payment e.g. **CORT** Trade Settlement Payment, **CFEE** Cancellation Fees etc. and should not be confused with Regulatory Reporting codes present in the pacs.008.

The externalised Purpose code set is classified by the purpose, for example commercial, for which the numerous codes within the classification are each described by Name and Definition.
For example:
**OTCD** is classified within the Collateral categorisation, with the *Name* **OTC Derivatives** described as a **Cash collateral related to over-the-counter (OTC) Derivatives** - in general for example contracts which are traded and privately negotiated.

*Category Purpose* also captures a high level purpose, which unlike *Purpose* is less granular but can trigger special processing e.g. Category Purpose code **SECU** ‘Securities’ may trigger pacs.002 *Payment Status Report* to provide update on the progress of the payment to the previous Agent.

Credit Transfer Transaction Information

---

<!-- Page 305 -->

The optional *Remittance Information* element within the pacs.009 Financial Institution Credit Transfer is nested to provide *Unstructured* information related to payment.

**Min 0 – Max 1**
*Remittance Information* enable the matching/reconciliation of an entry that the payment is intended to settle

**Min 0 – Max 1**
The *Unstructured* sub element captures free format *Remittance Information* which is restricted in CBPR+ to 140 characters to ensure backward compatibility with the legacy MT message during coexistence.

Note: unlike the pacs.008 *Remittance Information* can only be captured in an *Unstructured* element in the pacs.009 Financial Institution Credit Transfer. *Remittance Information* is however a dedicated element used both within the pacs and camt reporting messages, whereby this information can travel end-to-end using ISO 2022

Credit Transfer Transaction Info > Remittance Information >

---

<!-- Page 306 -->

> Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases.

**Financial Institution Advice Payments**
Use Case p.9.1.2.a - High Level Financial Institution Credit Transfer (pacs.009) pre-advised using pacs.009 (advc)
Use Case p.9.1.2.b - High Level Financial Institution Credit Transfer (pacs.009) pre-advised using pacs.009 (advc)

---

<!-- Page 307 -->

# pacs.009 (advice)

**Diagram flow (nodes A → B → C → D → E → F):**

- A → B : `pacs.009`
- B → E : `pacs.009 (ADV)`
- E → F : `camt.054` / `camt.053`
- B ↔ C : `pacs.009` / `pacs.002`
- C → D : `pacs.009` / `pacs.002`
- D → E : `camt.054` / `camt.053`

**Step 1**

Debtor initiates a payment instruction to the Debtor Agent

**Step 2a**

Debtor Agent (B) provided a notification to Creditor Agent (E) using a pacs.009 advice to indicate a 'pre-advice and provides the related payment details (in step 2b) This provides Agent E the ability to take the payment amount into their position, particularly where final settlement in step 5 occur after their business day. (i.e. time zone differences between the various Agent in the payment chain.

**Step 2b**

In parallel the Debtor Agent (B) initiates a payment to credit the account of Agent (E) as the creditor in the pacs.009 settlement message

**Step 3**

Agent C processes the payment on to Agent D

**Step 4**

Agent D credits the account of Agent E and should provide a notification e.g. credit notification (camt.054) in addition to a customer statement (camt.053)

**Step 5**

Agent E receives the payment and credits the account of Agent F as the Creditor, and may optionally provide a notification e.g. credit notification.

---

<!-- Page 308 -->

# pacs.009 (advice)

**Diagram flow (message labels on connections):**

- A → B : `pacs.009`
- B → E : `pacs.009 (ADV)`
- B ↔ C : `pacs.009` / `pacs.002`
- C ↔ D : `pacs.009` / `pacs.002`
- D ↔ E : `pacs.009` / `camt.053`
- E ↔ F : `camt.054` / `camt.053`

**Step markers on diagram:** 1 (A), 2a (B→E), 2b (B↔C), 3 (C), 4 (D), 5 (E)

---

**1**
Debtor initiates a payment instruction to the Debtor Agent

**2a**
Debtor Agent (B) provided a notification to Creditor Agent (E) using a pacs.009 advice to indicate a 'pre-advice and provides the related payment details (in step 2b) This provides Agent E the ability to take the payment amount into their position, particularly where final settlement in step 5 occur after their business day. (i.e. time zone differences between the various Agent in the payment chain.

**2b**
In parallel the Debtor Agent (B) initiates a payment to credit the account of Agent (E) as the creditor in the pacs.009 settlement message

**3**
Agent C processes the payment on to Agent D

**4**
Agent D processes the payment on to Agent E (as the Account Servicing Institution, Settlement method INDA)

**5**
Agent E receives the payment and credits the account of Agent F as the Creditor, and may optionally provide a notification e.g. credit notification.

---

<!-- Page 309 -->

# Financial Institution
# Credit Transfer (Cover)

---

<!-- Page 310 -->

## pac s.009

- Group Header
- Credit Transfer Transaction Information

## pac s.009 (COV)

- Group Header
- Credit Transfer Transaction Information
- Underlying Customer Credit Transfer

The pac s.009 has two main use cases:

- as a core Financial Institution Credit Transfer message
- As a **COV** where it is used as cover of (to settle) a pac s.008.

The pac s.009 therefore contain information of the underlying Customer Credit Transfer (pac s.008) for use in the cover scenario, which is the key attribute to differentiate between these two use cases.

---

<!-- Page 311 -->

A B C D

A → B: `pacs.009`
B → A: `pacs.002`
B → C: `pacs.009`
C → B: `pacs.002`
C → D: `camt.053`

The Financial Institution Credit Transfer message is sent by a Debtor Financial Institution to a Creditor Financial Institution, directly or through other agents and/or a payment clearing and settlement system. It is used to move funds from a debtor account to a creditor, where both Debtor and Creditor are **Financial Institutions**.

---

<!-- Page 312 -->

roles between messages

pacs.008
pacs.002
pacs.009 cov
pacs.002
pacs.009 cov
pacs.002
camt.054
camt.053

| Party | pacs.008 | pacs.009 cov |
|---|---|---|
| | Debtor | Underlying Debtor |
| | Debtor Agent | Debtor |
| | Creditor Agent | Creditor |
| | Creditor | Underlying Creditor |

The Financial Institution Credit Transfer cover message is sent by a Debtor Financial Institution to a Creditor Financial Institution, directly or through other agents and/or a payment clearing and settlement system. It is important to recognise that some **roles change** between these parallel messages.

---

<!-- Page 313 -->

roles between messages

D — DA — D — CA — C

pacs.008
pacs.002
pacs.009 cov
pacs.002
pacs.009 cov
pacs.002
pacs.009 cov
camt.053
camt.054

| Party | pacs.008 | pacs.009 cov |
|---|---|---|
|  | Debtor D | Underlying Debtor D |
|  | Debtor Agent DA | Debtor D |
|  | Creditor | Creditor C |

The correspondent banking cover payment method utilises both the pacs.008 and pacs.009 cov as a whole transaction, whereby the UETR element within these messages contain the **same** UETR which effectively interlink the messages. As an interlinked message it is important to understand the

---

<!-- Page 314 -->

# Group Header

---

<!-- Page 315 -->

Each ISO 20022 payment message has a **Min1 - Max1** ***Message Identification*** element, located in the Group Header. This **35 character** identifier is a point-to-point reference used to unambiguously identify the message.

For Payment Clearing and Settlement (pacs) messages the Message Identification has no exact equivalent in the legacy MT payment message. However, the MT 202 Sender's Reference (Field 20) could be considered a similar comparison where a pacs message contains a single Transaction.

Each transaction's *Credit Transfer Transaction Information* contains a variety of nested *Payment Identification* elements to capture reference related to the individual transaction such as a UETR (Unique End-to-end Transaction Reference)

---

<!-- Page 316 -->

Min 1 - Max 1

The pacs.009 message ***Creation Date*** captures the date and time which the message was created.

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset `YYYY-MM-DDThh:mm:ss.sss+/-hh:mm`
> For example: `2002-10-10T12:00:00-05:00` (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- Page 317 -->

## Transactions

Min 1 – Max 1

The pacs.009 message **_Number of Transactions_** captures the number of individual transaction contained within the message.

🧮 The number of transactions in CBPR+ payment usage guidelines is fixed to 1.

💡 Single transactions in the CBPR+ payment usage guidelines enable a transaction to be managed and unlocks highly automated, frictionless, instant payments, supporting the next generation of innovation.

Group Header: Number of Transactions

---

<!-- Page 318 -->

Min 1 – Max 1
The pacs.009 **Settlement Method** element within the Group Header **Settlement Information**, includes one of the embedded codes to indicate how the payment message will be settled.

The **Settlement Method** element in the pacs.009 allows a choice of an embedded code.

**INDA** indicate this Customer Credit Transfer will be settlement by the Instructed Agent (as the Account Servicing Institution) The account held at the Instructed Agent may captured in the dedicated **Settlement Account** element.
**INGA** indicate this Customer Credit Transfer has already been settlement by the Instructing Agent, who has credited the Account they service for the Instructed Agent (as an Account Owner). The account held by the Instructed Agent with the Instructing Agent may captured in the dedicated **Settlement Account** element.

Settlement Method code CLRG is not part of CBPR+ specifications but instead used in Market Infrastructure specification (HVPS+)

---

<!-- Page 319 -->

The pacs.009 message *Settlement Account* is a nested element as part of *Settlement Information*, this element identifies information related to an account used to settle the payment instruction.

Min 0 – Max 1
The *Settlement Account* identifies the account details maintained at the account servicing institution (Agent responsible for the settlement of the instruction as indicated in the *Settlement Method*)

Min 1 – Max 1
*Identification* identifies the account maintained at the Debtor Agent (Account Servicing Institution)

Min 0 – Max 1
*Type* uses the external Cash Account Type code list to identify the type of account

Min 0 – Max 1
*Currency* identifies the currency if the account

Min 0 – Max 1
*Name* identifies the name of the account as assigned by the Account Servicing Institution

Min 0 – Max 1
*Proxy* captures an alternative identification of the account number such as an email address. This element has further nested *Type* which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used.

---

<!-- Page 320 -->

# Credit Transfer Transaction Information

---

<!-- Page 321 -->

The pacs message *Payment Identification* provides a set of elements to identify the payment, of which several are mandatory elements

**Payment Identification**

**Instruction Identification**
Min 1 – Max 1

a **point-to-point reference** restricted in CBPR+ to 16 character and directly comparable with the Sender's Reference (Field 20) of the legacy MT payment message.

**End to End Identification**
Min 1 – Max 1

an **end-to-end reference** provided by the *Debtor* which must be passed unchanged throughout the payment and reported to the Creditor.

> note: for a pacs.009 COV the end-to-end id is provided (by the Debtor) from the pacs.008 Instruction id.
> In a pacs.009 COR if the Debtor has not provided an end-to-end identifier, the *Debtor Agent* may populate "NOTPROVIDED" to comply the mandatory need of this element.

**UETR**
Min 1 – Max 1

the **end-to-end Transaction** Reference created using the UUIDv4 standard. This reference must be passed unchanged throughout the payment, it may also be created by the Debtor within their Payment Initiation request, and also included in reporting

---

<!-- Page 322 -->

(continued)

Min 1 – Max 1

The pacs message **_Payment Identification_** also provides a set of optional elements to identify the payment.

**Payment Identification**

- **Transaction Identification** (Min 0 – Max 1)
  an **end-to-end reference** assigned by the first Instructing Agent to identify the transaction.

- **Clearing System Reference** (Min 0 – Max 1)
  a **point-to-point reference** populated by a Payment Market Infrastructure, typically to the settlement leg of a clearing system transaction as a reference to the settled clearing transaction.

---

<!-- Page 323 -->

# Information

The pacs message **Payment Type Information** provides a set of optional elements where the payment type can be described.

**Instruction Priority** (Min 0 – Max 1)

a choice of imbedded codes representing the urgency considered by the Instructing Agent, this point-to-point information may be used by the Instructed Agent to differentiate the processing priority.

**Service Level** (Min 0 – Max 3)

A nested element which may either use an external ISO Service Level code or a proprietary code. It is used to identify a particular agreed service level which should be applied to the payment.

For example, code G001 can be used to identify a gpi Tracked Cover Transfer similarly to Field 111 value 001 in the MT 202 COV

**Local Instrument** (Min 0 – Max 1)

A nested element which may either use an external ISO Local Instrument code or a proprietary code. It is used to identify the type of payment local instrument such as a Standing Order.

Note: the ISO instrument codes are registered by specific community group (captured in the code list)

**Clearing Channel** (Min 0 – Max 1)

a choice of imbedded codes representing the clearing channel to be used to process the payment. e.g., RTGS

**Category**

A nested element which may either use an external ISO Category Purpose code or a proprietary code. It is used to

---

<!-- Page 324 -->

## Date

The pacs.009 message (unlike the pacs.008) has only one element to capture the amount of the Credit Transfer, **Interbank Settlement Amount**.

**Min 1 – Max 1**

**Interbank Settlement Amount**

A mandated *currency amount* moved between the *Instructing Agent* and the *Instructed Agent*. This therefore is the point-to-point currency amount exchanged, comparable with the MT Field 32A

**Min 1 – Max 1**

**Interbank Settlement Date**

A mandated *date* on which the *Interbank Settlement* should be executed between the *Instructing Agent* and the *Instructed Agent*. This therefore is the *value date* comparable with the MT Field 32A

Note: the Financial Institution Credit Transfer (pacs.009) has no *Instructed Amount* element, *Exchange Rate* or *Charger Bearer* (unlike the pacs.008) as the Instructed Settlement Amount is expected to be transferred across the end-to-end payment chain without any charges being applied or currency conversions.

---

<!-- Page 325 -->

# Request

The pacs.009 message has three optional elements to capture the optional information related to the settlement of the instructions.

**Min 0 - Max 1**

The **Settlement Priority** provides an optional choice of embedded codes to indicate the instruction's settlement priority from the perspective of the Instructing Agent. This point-to-point information may be used by the Instructed Agent to identify the priority associated with the **Settlement Method** and should not be confused with the *Instruction Priority*.

> Note: Where the **Settlement Method** of the pacs.009 is 'INDA' (settled performed by the Instructed Agent) this indicates the Settlement Priority. Code 'INGA' implies settlement has already occurred for this point-to-point payment and therefore the Settlement Priority is not necessary.

**Min 0 - Max 1**

The **Settlement Time Indication** optionally captures the time settlement occurred at a transaction administrator such as a Market Infrastructure. This DateTime can be captured in two nested elements, **Debit Date Time** and **Credit Date Time**.

**Min 0 - Max 1**

The **Settlement Time Request** optionally captures the time settlement is requested for the payment instruction by the Instructing Agent. This Time can be capture in four nested elements:

- **CLS Time** the time the amount must be credit to CLS Bank
- **Till Time** the time until which the payment may be settled
- **From Time** the time from which the payment may be settled

---

<!-- Page 326 -->

# Agents

Instructing Agent: Agent A
Instructed Agent: Agent B
Instructing Agent: Agent B
Instructed Agent: Agent C

*pacs.009*
*pacs.009*

**Instructing Agent** and **Instructed Agent** represent the Agents involved in the pacs point-to-point message exchange. These roles therefore change on each payment leg.

*Instructing Agent* and *Instructed Agent* elements are required in all pacs messages and are only available in the **Credit Transfer Information**

Credit Transfer Transaction Information
Instructing Agent

---

<!-- Page 327 -->

The pacs message can capture up to 3 Previous Instructing Agents, which represent an Agent who previously only played a dynamic role in the payment between the Debtor Agent and Creditor Agent.

`Min 0 – Max 1`
The **_Previous Instructing Agent 1_** captures the first historic Agent between the Debtor Agent and the Previous Instructing Agent 2 (where present) and the Instructing Agent. This optional element is comparable with the Field 72 first /INS/ occurrence in the legacy FIN message.

`Min 0 – Max 1`
The **_Previous Instructing Agent 1 Account_** captured the account related between this Agent and Previous Instructing Agent 2 (where present) or the Instructing Agent. This optional element has not comparable field in the legacy FIN message

`Min 0 – Max 1`
The **_Previous Instructing Agent 2_** captures the second Previous Instructing Agent between the Previous Instructing Agent 1 and the Previous Instructing Agent 3 (where present) and the Instructing Agent. This optional element is comparable with the Field 72 second /INS/ occurrence in the legacy FIN message.

`Min 0 – Max 1`
The **_Previous Instructing Agent 2 Account_** captured the account related between this Agent and Previous Instructing Agent 2 (where present) or the Instructing Agent. This optional element has not comparable field in the legacy FIN message.

`Min 0 – Max 1`
The **_Previous Instructing Agent 3_** captures the third Previous Instructing Agent between the Agent and the Instructing Agent. This optional element is comparable with the Field 72 third /INS/ occurrence in the legacy FIN message.

`Min 0 – Max 1`
The **_Previous Instructing Agent 3 Account_** captured the account related between this Agent and Previous

---

<!-- Page 328 -->

# Intermediary Agents

The ISO 20022 pacs messages have a number of optional Agent elements whose roles change throughout the life cycle of the payment. **Intermediary Agent** is an example of this, where these agents are classified in numeric order (i.e., *Intermediary Agent 1*). **Previous Instructing Agent** however is a static role which allows additional Previous Instructing Agent to be appended to the history of the payment.

The below diagram visualizes the change of Agent role at different stages of the payment transaction life cycle.

A | B | C | D | E | F | G

| | | | | | | |
|---|---|---|---|---|---|---|
| Debtor | Instructing Agent & Debtor Agent | Instructed Agent | Intermediary Agent 1 | Intermediary Agent 2 | Creditor Agent | Creditor |
| Debtor | Debtor Agent | Instructing Agent | Instructed Agent | Intermediary Agent 1 | Creditor Agent | Creditor |
| Debtor | Debtor Agent | Previous Instructing Agent 1 | Instructing Agent | Instructed Agent | Creditor Agent | Creditor |
| Debtor | Debtor Agent | Previous Instructing Agent 1 | Previous Instructing Agent 2 | Instructing Agent | Creditor Agent & Instructed Agent | Creditor |

---

<!-- Page 329 -->

The pacs message can capture up to 3 Intermediary Agents, which play a dynamic role in the payment between the Debtor Agent and Creditor Agent.

Min 0 – Max 1
The **Intermediary Agent 1** captures the first Intermediary Agent between the Debtor Agent and Creditor Agent for who the Instructed Agent attempt to instruct the payment on to. This optional element is comparable with the Field 56a in the legacy FIN message.

Min 0 – Max 1
The **Intermediary Agent 1 Account** captured the account related to this Intermediary Agent, with the Instructed Agent. This element can be compared to the Party Identifier of the legacy Field 56a.

Min 0 – Max 1
The **Intermediary Agent 2** captures the second Intermediary Agent between the Intermediary Agent 1 and the Creditor Agent. This optional element has not comparable field in the legacy FIN message.

Min 0 – Max 1
The **Intermediary Agent 2 Account** captured the account related to this Intermediary Agent, with the Intermediary Agent 1. This optional element has not comparable field in the legacy FIN message.

Min 0 – Max 1
The **Intermediary Agent 3** captures the third Intermediary Agent between the Intermediary Agent 2 and the Creditor Agent. This optional element has not comparable field in the legacy FIN message.

Min 0 – Max 1
The **Intermediary Agent 3 Account** captured the account related to this Intermediary Agent, with the

---

<!-- Page 330 -->

The ISO 20222 pacs messages describe the Agent whose account is debited for a transaction as the *Debtor*. The *Debtor* sub elements describe the *Debtor* in greater detail.

## Postal Address

- Department
- Sub Department
- Street Name
- Building Number
- Building Name
- Floor
- Post Box
- Room
- Post Code
- Town Name
- Town Location Name
- District Name
- Country Sub Division
- Country
  - Code

## Debtor

**BICFI**
The BIC which identifies the Debtor

**Clearing System Member Id**
Information used to identify a Debtor by a clearing system identifier.

**LEI**
Legal entity identifier of the financial institution.

**Name**
*Name* by which the Agent is known

**Postal Address**
Nested element capturing either structured or unstructured Debtor address details

---

<!-- Page 331 -->

The pacs.009 *Debtor Account* is used to capture the account information for which debit entry is/has been applied to the Debtor's account, which are also reflected in their account Statement.

The *Debtor Account* uses a variety of nested elements to capture information related to the account.

**Min 1 – Max 1** *Identification* identifies the account maintained at the Debtor Agent (Account Servicing Institution)

**Min 0 – Max 1** *Type* uses the external Cash Account Type code list to identify the type of account

**Min 0 – Max 1** *Currency* identifies the currency if the account

**Min 0 – Max 1** *Name* identifies the name of the account as assigned by the Debtor Agent (Account Servicing Institution)

**Min 0 – Max 1** *Proxy* captures an alternative identification of the account number such as an email address. This element has further nested *Type* which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used.

the pacs.009 the Debtor is a Financial Institution, therefore the nested

---

<!-- Page 332 -->

Min 0 – Max 1 Min 0 – Max 1
The **Debtor Agent** and **Creditor Agent** are static roles in the pacs.009 FI to FI Customer Credit Transfer. These agent maintain a relationship with their customers; the *Debtor* and *Creditor*. However, unlike the pacs.008 Debtor Agent and Creditor Agent are optional, which cover the scenario where the Debtor and Creditor (as Financial Institutions) maintain a direct Nostro/Vostro account relationship.

Note: Where the *Debtor* and *Creditor* maintain a relationship with the same intermediary counterpart. It is recommended that this Agent is captured in the **Creditor Agent** element to align with translation from the legacy MT message.

Credit Transfer Transaction Information

---

<!-- Page 333 -->

# Agent Account

The pacs.009 **Min 0 – Max 1** *Debtor Agent Account* and *Creditor Agent Account* is used to capture the account information related to these Agents. The nature of this element implies there is an Agent or Agent in between the Debtor Agent and Creditor Agent in the payment transaction.

The *Debtor Agent Account* and *Creditor Agent Account* uses a variety of nested elements to capture information related to the account.

| | |
|---|---|
| **Min 1 – Max 1** | **Identification** identifies the account maintained at the Creditor Agent (Account Servicing Institution) |
| **Min 0 – Max 1** | **Type** uses the external Cash Account Type code list to identify the type of account |
| **Min 0 – Max 1** | **Currency** identifies the currency if the account |
| **Min 0 – Max 1** | **Name** identifies the name of the account as assigned by the Creditor Agent (Account Servicing Institution) |
| **Min 0 – Max 1** | **Proxy** captures an alternative identification of the account number such as an email address. This element has further nested **Type** which is a choice of external code list or proprietary code and **Identification** which are both mandatory where the Proxy element is used. |

Debtor Agent and Creditor Agent are Financial Institutions, therefore

---

<!-- Page 334 -->

The ISO 20022 pacs messages describe the Agent whose account is credited for a transaction as the **Creditor**. The *Creditor* sub elements describe the *Creditor* in greater detail.

| Postal Address |
|---|
| Department |
| Sub Department |
| Street Name |
| Building Number |
| Building Name |
| Floor |
| Post Box |
| Room |
| Post Code |
| Town Name |
| Town Location Name |
| District Name |
| Country Sub Division |
| Country → Code |
| Address Line |

The BIC which identifies the *Creditor* — **BICFI**

Information used to identify a Debtor by a clearing system identifier. — **Clearing System Member Id**

Legal entity identifier of the financial institution. — **LEI**

**Creditor**

*Name* by which the Agent is known — **Name**

Nested element capturing either structured or unstructured Debtor address details — **Postal Address**

---

<!-- Page 335 -->

The pacs.009 *Min 0 – Max 1* **Creditor Account** is used to capture the account information for which a credit entry is intended to be applied to the Creditor's account, which are also reflected in their account Statement.

The **Creditor Account** uses a variety of nested elements to capture information related to the account.

*Min 1 – Max 1* **Identification** identifies the account maintained at the Creditor Agent (Account Servicing Institution)

*Min 0 – Max 1* **Type** uses the external Cash Account Type code list to identify the type of account

*Min 0 – Max 1* **Currency** identifies the currency if the account

*Min 0 – Max 1* **Name** identifies the name of the account as assigned by the Creditor Agent (Account Servicing Institution)

*Min 0 – Max 1* **Proxy** captures an alternative identification of the account number such as an email address. This element has further nested **Type** which is a choice of external code list or proprietary code and **Identification** which are both mandatory where the Proxy element is used.

the pacs.009 the Creditor is a Financial Institution, therefore the

---

<!-- Page 336 -->

The *Instruction for Next Agent* and *Instruction for Creditor Agent* elements within the pacs.009 Financial Institution Credit Transfer optionally provides information related to the processing of the payment for these Agents.

**Min 0 – Max 2**

The *Instruction for Creditor Agent* element offers a multiplicity of up to 2 occurrences of information. This element enables:
- the use of 2 embedded **codes** to describe the instruction
- free format *instruction information*
- or both, where the free format complements the code.

The use of this element may be *bilaterally* agreed with the *Creditor Agent*. It must be passed on throughout the life cycle of the transaction until the payment reaches the *Credit Agent*.

**Min 0 – Max 6**

The *Instruction for Next Agent* element offers a multiplicity of up to 6 occurrences of information. This element is restricted to free format *instruction information* in CBPR+.
The element is used to provide instruction to the next Agent (which may not be the Creditor Agent)

Credit Transfer Transaction Information

---

<!-- Page 337 -->

The **Min 0 – Max 1** **Purpose** elements within the pacs.009 Financial Institution Credit Transfer capture the reason for the payment transaction which may either use an external ISO **Purpose code** or a proprietary code. The purpose is used by the capture the nature of the payment e.g. **CORT** Trade Settlement Payment, **CFEE** Cancellation Fees etc. and should not be confused with Regulatory Reporting codes present in the pacs.008.

The externalised Purpose code set is classified by the purpose, for example commercial, for which the numerous codes within the classification are each described by Name and Definition.
For example:
**OTCD** is classified within the Collateral categorisation, with the *Name* **OTC Derivatives** described as a **Cash collateral related to over-the-counter (OTC) Derivatives** - in general for example contracts which are traded and privately negotiated.

*Category Purpose* also captures a high level purpose, which unlike *Purpose* is less granular but can trigger special processing e.g. Category Purpose code **SECU** ‘Securities’ may trigger pacs.002 *Payment Status Report* to provide update on the progress of the payment to the previous Agent.

Credit Transfer Transaction Information

---

<!-- Page 338 -->

The optional *Remittance Information* element within the pacs.009 COV Financial Institution Credit Transfer is nested to provide *Unstructured* information related to payment.

`Min 0 – Max 1`
*Remittance Information* enable the matching/reconciliation of an entry that the payment is intended to settle.

`Min 0 – Max 1`
The *Unstructured* sub element captures free format *Remittance Information* which is restricted in CBPR+ to 140 characters to ensure backward compatibility with the legacy MT message during coexistence.

Note: the pacs.008 *Remittance Information* is captured in the pacs.009 COV within the *Underlying Customer Credit Transfer, Remittance Information* element.
The *Remittance Information* in the pacs.009 COV is for *Creditor* this message (often the Creditor Agent of the pacs.008) As this information is not present in the pacs.008 it is unlikely the pacs.009 COV remittance information will be used.

---

<!-- Page 339 -->

# Transfer

The **Underlying Customer Credit Transfer** element is used when the pacs.009 *Financial Institution Credit Transfer* message is being utilized to cover a pacs.008 *FI to FI Customer Credit Transfer*. The information contained within this nested element relates directly to the information exchanged between the Instructing Agent and Instructed Agent of the pacs.008 *FI to FI Customer Credit Transfer* and can be compared with Sequence B of the legacy MT 202 COV.

When utilizing the **Underlying Customer Credit Transfer** nested element as part of a pacs.009 *Financial Institution Credit Transfer* cover message the:

| Element | Constraint |
| :--- | :--- |
| ➢ **Debtor** | Min 1 – Max 1 |
| ➢ **Debtor Agent** | Min 1 – Max 1 |
| ➢ **Creditor Agent** | Min 1 – Max 1 |
| ➢ **Creditor** | Min 1 – Max 1 |

are all mandatory elements.

Note: *Instruction for Creditor Agent* from the Underlying

---

<!-- Page 340 -->

Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases.

**Cover Method Financial Institution Payments**

Use Case p.9.2.1 - High Level Customer Credit Transfer (pacs.008) settled using the cover method (pacs.009 COV)

Use Case p.9.2.2 - High Level Customer Credit Transfer (pacs.008) settled using the cover method (pacs.009 COV) over a Payment Market Infrastructure

Use Case p.9.2.3 - High Level Customer Credit Transfer (pacs.008) settled using the cover method (pacs.009 COV) where an incorrect intermediary is used

Use Case p.9.2.4 - High Level FI to FI Customer Credit Transfer involved a serial leg into a cover method (pacs.009 COV)

Use Case p.9.2.5 - High Level FI to FI Customer Credit Transfer involved a serial leg in and out of a cover method (pacs.009 COV)

Use Case p.9.2.6 - High Level FI to FI Customer Credit Transfer involved a serial leg out of a cover method (pacs.009 COV)

---

<!-- Page 341 -->

# method (pacs.009 COV)

**1**
Debtor initiates a payment instruction to the Debtor Agent

**2a**
Debtor Agent (A) initiates a payment using the cover method to the Creditor Agent (D)

**2b**
In parallel the Debtor Agent (A) initiates a covering payment to credit the account of Agent (D) who become the Creditor of the cover payment (pacs.009 cov). Agent A's role also changes in the cover payment where it becomes the Debtor, whereby Agent A's account with their correspondent / Agent D's debited

**3**
Agent B processes the payment on to Agent C

**4**
Agent C receives the payment and credits the account of Agent D as the Creditor

**5**
Agent C produces an end of day account statement report. An optional real time notifications e.g. advice of credit may have also been created at the time of the credit posting

**6**
Agent D reconciles the covering funds and credits the account of the Creditor, and may optionally provide a notification e.g. credit notification

**Message labels:** pacs.008, pacs.002, pacs.009 cov, camt.053, camt.064

---

<!-- Page 342 -->

# method (pacs.009 COV) over a Payment Market Infrastructure

**Message flow (arrows):**

- A → D: `pacs.008`
- D → A: `pacs.002`
- A → B: `pacs.009 cov`
- B → A: `pacs.002`
- B → C: `pacs.009 cov`
- C → B: `pacs.002`
- C → D: `pacs.009 cov`
- D → C: `camt.053`
- C → D: `camt.054`
- Settlement Complete

**Step descriptions:**

| Step | Description |
|------|-------------|
| 1 | Debtor initiates a payment instruction to the Debtor Agent |
| 2a | Debtor Agent (A) initiates a payment using the cover method to the Creditor Agent (D) |
| 2b | In parallel the Debtor Agent (A) initiates a covering payment to credit the account of Agent (D) with their correspondent (Agent |
| 3 | Agent B processes the payment on Agent C, via the Payment Market Infrastructure |
| 4 | Payment Market Infrastructure, settles the payment between Agent B and Agent C as direct participants of the Market Infrastructure, and provides a settlement confirmation to Agent B |
| 5 | Agent C receives the payment and credits the account of Agent D |
| 6 | Agent C produces an end of day account statement report. An optional real time notifications e.g. advice of credit may have also been created at the time of the credit posting |
| 7 | Agent D reconciles the covering funds and credits the account of the Creditor, and may optionally provide a notification e.g. credit notification |

---

<!-- Page 343 -->

method (pac.009 COV) where an incorrect intermediary is used.

**Diagram flow (message arrows):** `pac.008` / `pac.002` · `pac.009 cov` / `pac.002` · `pac.009 cov` / `pac.002` · `camt.052` / `camt.004`

**Agents:** A → B → Z → C → D

---

**1**
Debtor initiates a payment instruction to the Debtor Agent

**2a**
Debtor Agent (A) initiates a payment using the cover method to the Creditor Agent (D)

**2b**
In parallel the Debtor Agent (A) initiates a covering payment to credit the account of Agent (D) who become the Creditor of the cover payment (pac.009 cov). Agent A's role also changes in the cover payment where it becomes the Debtor, whereby Agent A's account with their correspondent (Agent B) is debited

**3**
Agent B processes the payment on to Agent Z

**3** (⚠)
Agent Z receives the payment and recognises they do not hold the account of Agent D as the Creditor. Agent Z reject the cover payment (pac.009 cov) using a

**4**
Recognising the error Agent B re-processes the payment on to Agent C using the same UETR (correcting the error in step 3)

**5**
Agent C receives the payment and credits the account of Agent D. Agent C produces an end of day account statement report. An optional real time notifications e.g. advice of credit may have also been created at the time of the credit posting

**6**
Agent D reconciles the covering funds and credits the account of the Creditor, and may optionally provide a notification

---

<!-- Page 344 -->

# method (pacs.009 COV)

**Sequence flow (diagram):**

- **1:** Debtor → Agent **A**
- **2:** Agent **A** → Agent **B** (`pacs.008` / `pacs.002`)
- **3a:** Agent **B** → Agent **E** (`pacs.008` / `pacs.002`)
- **3b:** Agent **B** → Agent **C** (`pacs.009 cov`)
- **5:** Agent **C** → Agent **D** (`pacs.002`)
- **6:** Agent **D** → Agent **E** (`camt.053` / `camt.054`)
- **4:** Agent **E** → Creditor

---

**1**
Debtor initiates a payment instruction to the Debtor Agent

**2**
Debtor Agent (A) initiates a payment using the serial method towards the Creditor Agent (E)

**3a**
Agent B initiates a payment using the cover method towards the Creditor Agent (E) by sending a direct pacs.008 to Agent E who they have business relationship with

**3b**
In parallel the Agent (B) initiates a covering payment to credit the account of Agent (E) with their correspondent (Agent D)

**4**
Agent E receives the payment instruction and credits the account of the Creditor, and may optionally provide a notification e.g. credit notification. Alternatively, they may have chosen to await until settlement occurred in Step 6 based upon their risk appetite.

**5**
Agent C processes the payment on Agent D, using a correspondent banking business relationship

**6**
Agent D receives the payment and credits the account of Agent E. Agent D produces an end of day account statement report. An optional real time notification e.g. advice of credit may have also been created at the time of the credit posting

---

<!-- Page 345 -->

# of a cover method (pacs.009 COV)

**Sequence diagram (message flow):**

- **1** → **2** (Debtor Agent **A**) — `pacs.008` / `pacs.002`
- **2** → **3a / 3b** (Agent **B**) — `pacs.008` / `pacs.002`
- **3a / 3b** → **4** (Agent **E**) — `pacs.009 cov` / `pacs.002`
- **4** → **5** (Agent **C**) — `pacs.009 cov` / `pacs.002`
- **5** → **6** (Agent **D**) — `camt.053` / `camt.054`
- **6** → **7** (Agent **F**) — `pacs.008` / `pacs.002`
- **7** → Creditor

**Step descriptions:**

1. Debtor initiates a payment instruction to the Debtor Agent

2. Debtor Agent (A) initiates a payment using the serial method towards the Creditor Agent (F)

3a. Agent B initiates a payment using the cover method towards the Creditor Agent (F) by sending a direct pacs.008 to Agent E who they have business relationship with.

3b. In parallel the Agent (B) initiates a covering payment to credit the account of Agent (E) with their correspondent banking business relationship

4. Agent E receives the payment instruction and process the payment on to Agent F. Alternatively they may have chosen to await until settlement occurred in Step 6 based upon their risk appetite.

5. Agent C processes the payment on Agent D, using a correspondent banking business relationship

6. Agent D receives the payment and credits the account of Agent E. Agent D produces an end of day account statement report. An optional real time notification e.g. advice of credit may have also been created at the time of the credit posting

7. Agent F receives the payment and credits the account of the Creditor, and may optionally provide a notification e.g. credit notification.

---

<!-- Page 346 -->

# cover method (pacs.009 COV)

**Sequence / message flow**

- Debtor → **(1)** → Agent **A**
- Agent **A** → **(2a)** → Agent **D** — `pacs.008` / `pacs.002`
- Agent **A** → **(2b)** → Agent **B** — `pacs.009 cov` / `pacs.002`
- Agent **B** → **(5)** → Agent **C** — `pacs.009 cov` / `pacs.002`
- Agent **C** → **(6)** → Agent **D** — `camt.053` / `camt.054`
- Agent **D** → **(3)** → Agent **E** — `pacs.008` / `pacs.002`
- Agent **E** → **(4)** → Creditor

**Step descriptions**

1. Debtor initiates a payment instruction to the Debtor Agent

2a. Debtor Agent (A) initiates a payment using the cover method towards the Creditor Agent (E) by sending a direct pacs.008 to Agent D who they have business relationship with

2b. in parallel the Agent (A) initiates a covering payment to credit the account of Agent (D) with their correspondent (Agent C)

3. Agent D receives the payment instruction and process the payment on to Agent E. Alternatively they may have chosen to await until settlement occurred in Step 6 based upon their

4. Agent E receives the payment and credits the account of the Creditor, and may optionally provide a notification e.g. credit notification.

5. Agent B processes the payment on Agent C, using a correspondent banking business relationship

6. Agent C receives the payment and credits the account of Agent D. Agent C produces an end of day account statement report. An optional real time notification e.g. advice of credit may have also been created at the time of the credit posting

---

<!-- Page 347 -->

# FI to FI Payment
# Status Report

---

<!-- Page 348 -->

pacs.002

- Group Header
- Transaction Information And Status

The Financial Institution To Financial Institution Payment Status Report message is sent by an instructed agent to the previous party in the payment chain. It is used to inform this party about the positive or negative status of an instruction. It is also used to report on a pending instruction

---

<!-- Page 349 -->

# Customer Payment (pacs.008)

**Participants:** A | B | C

**Messages / Flow:**

- pain.001
- pain.002
- pacs.008
- pacs.002
- pacs.008
- pacs.002
- pacs.004
- pacs.002

**Annotations:**

- Reject & Reason
- Return & Reason

**Note (right):** CBPR+ restricted the pacs.002 to a single transaction

> The code list representing the *Payment Transaction Status* is part of the ISO 20022 external code list

> The FitOFlPaymentStatusReport message is sent by an instructed agent to the previous party in the payment chain. It is used to inform this party about the positive or negative status of an

---

<!-- Page 350 -->

Debtor

Debtor Agent

Creditor Agent

Initiating Party

Creditor

pain.008\*\*

pain.002

pacs.003

pacs.002

camt.053

\*Initiating Party may alternative represent an authorised party such as a head office

\*\*or other proprietary method for instructing a direct debit initiation request.

**The FIToFIPaymentStatusReport message is sent by an instructed agent to the previous party in the payment chain. It is used to inform this party about the positive or negative status of an instruction. It is also used to report on a pending instruction.**

---

<!-- Page 351 -->

# Group Header

---

<!-- Page 352 -->

Min 1 – Max 1

Each ISO 20022 payment message has a **Message Identification** element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message.

For Payment Clearing and Settlement (pacs) messages the Message Identification has no exact equivalent in the legacy MT payment message. However, the Sender's Reference (Field 20) could be considered a similar comparison where a pacs message contains a single Transaction.

Group Header > Message Identification

---

<!-- Page 353 -->

Min 1 – Max 1

The pacs.002 message *Creation Date* captures the date and time which the message was created.

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
> For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- Page 354 -->

# Transaction Information and Status

---

<!-- Page 355 -->

Min 1 – Max 1

The pac s.002 FI to FI Payment Status Report uses elements in the ***Original Group Information*** to capture the message identifier and message name of the underlying payment the *Payment Status Report* relates to. The mandatory ***Original Message Identification*** contains the point-to-point reference, and the mandatory ***Original Message Name Identification*** contains the message name of the underlying payment being reported upon. Optionally the ***Original Creation Date Time*** can also be captured.

For example:
***Original Message Name Identification*** “pac s.008.001.08” confirms the Status Report is of a pac s.008 Financial Institution to Financial Institution Customer Credit Transfer. Where as “pac s.009.001.08” confirms the Status Report is of a pac s.009 Financial Institution Credit Transfer.

|  |  |  |
|---|---|---|
|  | **pacs.008** → |  |
|  | Message Identification | abcd1234 |
| **Group Header** | Message Identification | xyz9875 |
| **Original Group Information** | Original Message Identification | abcd1234 |
|  | ← **pacs.002** |  |
|  | Original Message ... |  |

Note: the xx in the CBPR+ Usage Guideline represents the message version of the message

---

<!-- Page 356 -->

The `pacs.002 FI to FI Payment Status Report` also uses a number of other **Original** elements in the **_Transaction Information And Status_** to capture information from the underlying payment that the _Payment Status Report_ relates to.

| | |
|---|---|
| **Original Instruction Identification** | **Original End to End Identification** |
| **Original UETR** | **Original Transaction Identification** |

**Mandatory** element (in addition to _Original Message identification_ and _Original Message Name Identification_ described on the previous page) include:

**_Original End to End Identification_** `Min 1 – Max 1`
**_Original UETR_** `Min 1 – Max 1`

Optionally **_Original Transaction Identification_** `Min 0 – Max 1` and **_Original Instruction Identification_** `Min 0 – Max 1` may also be used.

These _Original_ elements enables the **_Instructed Agent_** in the `pacs.002 Payment Status Report` to associate the Payment Status with the payment they originally sent.

| Transaction Information and Status ✅ |
|---|
| Original Instruction Identification |
| Original End to End Identification |

---

<!-- Page 357 -->

The pacs.002 *FI to FI Payment Status Report* **Transaction Status** utilizes the externalized ISO *Payment Transaction Status* code list to provide a status update on a pacs message previously received. The *Transaction Status* element is arguable the most significant/core parts of the pacs.002 and optionally may further be complimented with **Status Reason Information**.

The nested **Status Reason Information** enable the optional inclusion of:
**Originator** – the party that issues the status. Typically, the pacs.002 Instructing Agent and therefore Originator is not necessary.
**Reason** – which utilizes either an ISO external Status Reason code or a proprietary reason. For example, **AC04** ‘Closed Account Number’ would compliment a RJCT (Reject) Transaction Status.
**Additional Information** – a text element to provide further status reason information, necessary where the *Reason* code is NARR

Note: A **Reason** code must be provided where the **Transaction Status** RJCT (Reject) code is used.

The next two slides take a look at:
* The code relevant to CBPR+ Payment Statuses, the codes description and the High Level Use Case.
* Logical order in which these codes may be used in one or multiple Payment Status Report updates.

---

<!-- Page 358 -->

| Code | Name | ISO Definition | High Level Use Case |
| :--- | :--- | :--- | :--- |
| ACCC | AcceptedSettlementCompleted | Settlement on the creditor's account has been completed. | Sent by **Creditor Agent** to confirm the settlement on the creditor's account |
| ACCP | AcceptedCustomerProfile | Preceding check of technical validation was successful. Customer profile check was also successful. | Sent by **any Agent** in the payment chain to confirm acceptance prior to technical validation. |
| ACFC | AcceptedFundsChecked | Preceding check of technical validation and customer profile was successful and an automatic fundscheck was positive. | Sent by **any Agent** in the payment chain to confirm the technical validation/ profile w as positive and automatic funds check was **positive**. |
| ACIS | AcceptedAndChequeIssued | Payment instruction to issue a cheque has been accepted, and the cheque has been issued but not yet been deposited or cleared. | Sent by **any Agent** in the payment chain to confirm a cheque has been issued as requested. |
| ACSC | AcceptedSettlementCompleted | Settlement has been completed. | Sent by the **Any Agent** to confirm settlement of a payment message leg. |
| ACSP | AcceptedSettlementInProcess | All preceding checks such as technical validation and customer profile were successful and therefore the payment initiation has been accepted for execution. | Sent by **any Agent** to the to confirm the payment is accepted following technical validations being successfully completed. |
| ACTC | AcceptedTechnicalValidation | Authentication and syntactical and semantical validation are successful | Sent by **any Agent** in the payment chain to the previous Agent to confirm the payment is accepted following technical validations being successfully completed. |
| ACWC | AcceptedWithChange | Instruction is accepted but a change will be made, such as date or remittance not sent. | Sent by **any Agent** in the payment chain to the previous Agent to confirm the payment is accepted following amendments being made. |
| ACWP | AcceptedWithoutPosting | Payment instruction included in the credit transfer is accepted without being posted to the creditor customer's account. | Sent by **Creditor Agent** to the previous Agent to confirm the acceptance of payment w ithout settlement on the creditor's account. |
| CPUC | CashPickedUpByCreditor | Cash has been picked up by the Creditor. | Sent by **Creditor Agent** to the previous Agent to confirm that the cash collection has been picked up by the Creditor. |
| PDNG | Pending | Payment instruction or individual transaction included in the payment initiation is pending. Further checks and status update will be performed. | Sent by **any Agent** in the payment chain to the previous Agent as an interim status w hilst other validations are performed. |
| RCV D | Received | Payment initiation has been received by the receiving agent. | Sent by **Any Agent** to the previous Agent as confirmation that their Customer |

---

<!-- Page 359 -->

The pacs.002 *Payment Transaction Status* element facilitates updates to the previous Agent on changes to the status of the payment. Such Status Information messages (pacs.002), with the exception of **reject code RJCT** which is **mandatory in CBPR+**, are bilateral agreed, where upon a variety of these Transaction Statuses may be used by the Instructed Agent at different stages of the payment processing.

This diagram illustrates the logical order in which these codes may be used during the processing of the Payment Clearing And Settlement message (pacs) and the role of the Agent in providing these status.

**Any Agent**

RCVD
ACTC
ACCP
ACFC
RJCT
ACWC
ACIS
ACSP

**PDNG**

CPUC
ACWP
ACCC

**Creditor Agent**

---

<!-- Page 360 -->

## Definitions and High Level Use Cases

| Code | Name | ISO Definition | High Level Use Case |
|---|---|---|---|
| AC01 | IncorrectAccountNumber | Format of the account number specified is not correct or Account number is missing | Sent by **Instructed Agent** when a settlement account number is incorrect |
| AC02 | InvalidDebtorAccountNumber | Debtor account number invalid or missing | Sent by **Instructed Agent** when Debtor account number is incomplete |
| AC04 | ClosedAccountNumber | Account number specified has been closed on the bank of account's books | Sent by **Creditor Agent** when the Creditor account number is closed |
| AC06 | BlockedAccount | Account specified is blocked, prohibiting posting of transactions against it. | Sent by **Creditor Agent** when Creditor account is blocked from posting credit entries. Sent by **Instructed Agent** when a settlement account is blocked |
| AC07 | ClosedCreditorAccountNumber | Creditor account number closed | Sent by **Creditor Agent** when account number is closed. *CBPPlus recommend using AC04, but support AC07 to remain interoperable with other clearing systems.* |
| AC13 | InvalidDebtorAccountType | Debtor account type is missing or invalid | Sent by **Instructed Agent** when Debtor account type element is incorrect |
| AGNT | IncorrectAgent | Agent in the payment workflow is incorrect | Sent by **Instructed Agent** when an agent in the payment transaction has an incorrect identification element |
| AG01 | TransactionForbidden | Transaction forbidden on this type of account (formerly NoAgreement) | Sent by **Instructed Agent** when the type of payment transaction is not allowed for the specified account |
| AG07 | UnsuccessfulDirectDebit | Debtor account cannot be debited for a generic reason. Code value may be used in general purposes and as a replacement for AM04 if debtor bank does not reveal its customer's insufficient funds for privacy reasons | Sent by **Debtor Agent** of a Direct Debit message, when debtor account can not be debited |
| AM02 | NotAllowedAmount | Specific transaction/message amount is greater than allowed maximum | Sent by **Instructed Agent** when payment amount is above an allowed amount. For example the clearing system with a upper amount threshold |

---

<!-- Page 361 -->

## Definitions and High Level Use Cases

| Code | Name | ISO Definition | High Level Use Case |
|---|---|---|---|
| AM03 | NotAllowedCurrency | Specified message amount is a non processable currency outside of existing agreement | Sent by **Instructed Agent** when the currency of the payment is not allowed within the existing business agreement |
| AM04 | InsufficientFunds | Amount of funds available to cover specified message amount is insufficient. | Sent by **Instructed Agent** when there is not sufficient funds to settle the payment transaction. |
| AM05 | Duplication | Payment is a duplicate of another payment | Sent by **Instructed Agent** when the payment is a duplicate. CBP+Plus recommend using *DUPL*, but support *AM05* to remain interoperable with other clearing systems. |
| AM06 | TooLowAmount | Specified transaction amount is less than agreed minimum. | Sent by **Instructed Agent** when the payment amount is below a minimum amount. |
| AM07 | BlockedAmount | Amount specified in message has been blocked by regulatory authorities | Sent by **Instructed Agent** when the payment amount is blocked by regulators |
| AM09 | WrongAmount | Amount received is not the amount agreed or expected | Sent by **Instructed Agent** when the payment amount is incorrect |
| BE01 | InconsistentWithEndCustomer | Identification of end customer is not consistent with associated account number (formerly CreditorConsistency). | Sent by **Creditor Agent** when there is an inconsistency between the Creditor's identification and the account number |
| BE04 | MissingCreditorAddress | Specification of creditor's address, which is required for payment, is missing/not correct (formerly IncorrectCreditorAddress). | Sent by **Instructed Agent** when the Creditor's address is missing. Sent by **Creditor Agent** when the Creditor's address is incorrect |
| BE05 | UnrecognisedInitiatingParty | Party who initiated the message is not recognised by the end customer. | Sent by **Creditor Agent** when the initiating party is unknown to the beneficiary |
| BE07 | MissingDebtorAddress | Specification of debtor's address, which is required for payment, is missing/not correct. | Sent by **Instructed Agent** when the address of the Debtor is missing or incorrect |

---

<!-- Page 362 -->

## Definitions and High Level Use Cases

| Code | Name | ISO Definition | High Level Use Case |
|---|---|---|---|
| BE10 | InvalidDebtorCountry | Debtor country code is missing or invalid | Sent by **Instructed Agent** when the country code of the Debtor is missing or incorrect |
| BE11 | InvalidCreditorCountry | Creditor country code is missing or invalid | Sent by **Instructed Agent** when the country code of the Creditor is missing or incorrect |
| BE16 | InvalidDebtorIdentificationCode | Debtor or Ultimate Debtor identification code missing or invalid | Sent by **Instructed Agent** when the identification of the Debtor or Ultimate Debtor is missing or incorrect |
| BE17 | InvalidCreditorIdentificationCode | Creditor or Ultimate Creditor identification code missing or invalid | Sent by the **Instructed Agent** when the identification of the Creditor or Ultimate Creditor is missing or incorrect |
| CN01 | AuthorisationCancelled | Authorisation is cancelled. | Sent by **Instructed Agent** when a third party debit authorisation has been cancelled or is not in place. |
| CNOR | Creditor bank is not registered | Creditor bank is not registered under this BIC in the Clearing Settlement Mechanism (CSM) | Sent by **Instructed Agent** when the Creditor Agent is not reachable in the Market Infrastructure (CSM) and an appropriate correspondent can not be determined. |
| CURR | IncorrectCurrency | Currency of the payment is incorrect | Sent by the **Creditor Agent** when the **Interbank Settlement Amount** Currency is not the same as the Creditor account currency and a currency conversion is not accepted on the Creditor's account. |
| CUST | RequestedByCustomer | Cancellation requested by the Debtor | Sent by **Instructed Agent** upon request by Debtor. CBPPlus recommend using FC0R, but support CUST to remain interoperable with other clearing systems. |
| DT01 | InvalidDate | Invalid date (eg. wrong or missing settlement date) | Sent by **Instructed Agent** when the settlement date is in the past and an agreement is in place to reject rather than apply the next possible value date. |
| DT04 | FutureDateNotSupported | Future date not supported | Sent by **Instructed Agent** when a future settlement date is not supported or appear to be an error e.g. is the wrong year. |

---

<!-- Page 363 -->

# Definitions and High Level Use Cases

| Code | Name | ISO Definition | High Level Use Case |
|---|---|---|---|
| DUPL | DuplicatePayment | Payment is a duplicate of another payment | Sent by **Instructed Agent** when the payment is a duplicate |
| ERIN | ERIOptionNotSupported | The Extended Remittance Information (ERI) option is not supported. | Sent by **Instructed Agent** when extended Remittance information (**Related Remittance Information**) is not supported or bilaterally/multilaterally agreed |
| ED05 | SettlementFailed | Settlement of the transaction has failed. | Sent by **Instructed Agent** when the settlement of payment has failed or been unsuccessful. |
| FF03 | InvalidPaymentTypeInformation | Payment Type Information is missing or invalid. Generic usage if cannot specify Service Level or Local Instrument code | Sent by **Instructed Agent** when the Payment Type Information (**Instruction Priority, Clearing Channel**) provided for the payment is incorrect or not supported. |
| FF04 | InvalidServiceLevelCode | Service Level code is missing or invalid | Sent by **Instructed Agent** when the Payment Type Information **Service Level** provided for the payment is incorrect or not supported |
| FF05 | InvalidLocalInstrumentCode | Local Instrument code is missing or invalid | Sent by **Instructed Agent** when the Payment Type Information **Local Instrument** provided for the payment is incorrect or not supported |
| FF06 | InvalidCategoryPurposeCode | Category Purpose code is missing or invalid | Sent by **Instructed Agent** when the Payment Type Information **Category Purpose** provided for the payment is incorrect or not supported |
| FF07 | InvalidPurpose | Purpose is missing or invalid | Sent by **Instructed Agent** when the **Purpose** provided for the payment is either missing or incorrect |
| FOCR | FollowingCancellationRequest | Return following a cancellation request | Sent by **Instructed Agent** that has accepted a payment cancellation request (cant.056) and subsequently is rejecting the unsettled payment instruction. |
| FR01 | Fraud | Returned as a result of fraud. | Sent by **Instructed Agent** when the payment is identified as fraudulent. |
| MR01 | NoMandate | No Mandate | Sent by **Instructed Agent** when a Direct Debit message has no mandate in |

---

<!-- Page 364 -->

## Definitions and High Level Use Cases

| Code | Name | ISO Definition | High Level Use Case |
|---|---|---|---|
| MD02 | MissingMandatoryInformationInMandate | Mandate related information data required by the scheme is missing. | Sent by **Instructed Agent** when information required by the clearing scheme is missing. |
| MD05 | CollectionNotDue | Creditor or creditor's agent should not have collected the direct debit | Sent by **Instructed Agent** when a Direct Debit collection was not due |
| MD07 | EndCustomerDeceased | End customer is deceased. | Sent by **Creditor Agent** when the Creditor or Ultimate Creditor is deceased |
| MS02 | NotSpecifiedReasonOnCustomerGenerated | Reason has not been specified by end customer | Sent by **Creditor Agent** where instructed to reject by the Creditor, but no reason was specified |
| MS03 | NotSpecifiedReasonOnAgentGenerated | Reason has not been specified by agent. | Sent by **Instructed Agent** but no reason is specified |
| NARR | Narrative | Reason is provided as narrative information in the additional reason information. | Sent by **Instructed Agent** the reason is provided as narrative information. Only to be used where no other code is appropriate (i.e. exceptional circumstances) |
| NOAS | NoAnswerFromCustomer | No response from Beneficiary | Sent by **Instructed Agent** when the Creditor did not respond to query for additional information in order that the payment could be credited e.g. currency control documentation. |
| NOCM | Not compliant (more generic) | Customer account is not compliant with regulatory requirements, for example FICA (in South Africa) or any other regulatory requirements which render an account inactive for certain processing. | Sent by **Instructed Agent** when the Creditor account is not compliant with certain regulatory requirements. |
| RC01 | BankIdentifierIncorrect | Bank Identifier code specified in the message has an incorrect format (formerly IncorrectFormatForRoutingCode). | Sent by **Instructed Agent** when an incorrect BIC has been used in the payment |
| RC03 | InvalidDebtorBankIdentifier | Debtor bank identifier is invalid or missing | Sent by **Instructed Agent** when the Debtor Agent identification is incorrect or |

---

<!-- Page 365 -->

# Definitions and High Level Use Cases

| Code | Name | ISO Definition | High Level Use Case |
|---|---|---|---|
| RC04 | InvalidCreditorBankIdentifier | Creditor bank identifier is invalid or missing | Sent by **Instructed Agent** when the Creditor Agent identification is incorrect or missing |
| RC08 | InvalidClearingSystemMemberIdentifier | ClearingSystemMemberIdentifier is invalid or missing. Generic usage if cannot specify between debit or credit account | Sent by **Instructed Agent** when the clearing system member identification for an Agent is incorrect |
| RC11 | InvalidIntermediaryAgent | Intermediary Agent is invalid or missing | Sent by **Instructed Agent** when the intermediary agent identification is incorrect |
| RF01 | NotUniqueTransactionReference | Transaction reference is not unique within the message. | Sent by **Instructed Agent** when the transaction reference (UETR and Instruction Identification) are not unique |
| RR01 | Missing Debtor Account or Identification | Specification of the debtor's account or unique identification needed for reasons of regulatory requirements is insufficient or missing | Sent by **Instructed Agent** when the Debtor identification or debtor account is missing, or the information provided are not sufficient |
| RR02 | Missing Debtor Name or Address | Specification of the debtor's name and/or address needed for regulatory requirements is insufficient or missing. | Sent by **Instructed Agent** since the Debtor name or Address is missing, or information provided is not sufficient |
| RR03 | Missing Creditor Name or Address | Specification of the creditor's name and/or address needed for regulatory requirements is insufficient or missing. | Sent by **Instructed Agent** since the Creditor name or Address is missing, or information provided is not sufficient |
| RR04 | Regulatory Reason | Regulatory Reason | Sent by **Instructed Agent** due to any unspecified regulatory reason |
| RR05 | Regulatory Information Invalid | Regulatory or Central Bank Reporting information missing, incomplete or invalid. | Sent by **Instructed Agent** when the reporting information required by the central bank or reporting authority is missing or not complete |

---

<!-- Page 366 -->

## Definitions and High Level Use Cases

| Code | Name | ISO Definition | High Level Use Case |
|---|---|---|---|
| RR07 | RemittanceInformationInvalid | Remittance information structure does not comply with rules for payment type. | Sent by **Instructed Agent** since the remittance information is incorrect |
| RR08 | RemittanceInformationTruncated | Remittance information truncated to comply with rules for payment type. | Sent by **Instructed Agent** where the Structured Remittance Information has not been bilaterally or multilaterally agreed, which or has resulted in truncation |
| RR09 | InvalidStructuredCreditReference | Structured creditor reference invalid or missing. | Sent by **Instructed Agent** when the structure of the creditor reference in the remittance information is invalid or missing |
| RR11 | InvalidDebtorAgentServiceID | Invalid or missing identification of a bank proprietary service. | Sent by **Instructed Agent** where the proprietary identification for the Debtor is invalid or not understood |
| RR12 | InvalidPartyID | Invalid or missing identification required within a particular country or payment type. | Sent by **Instructed Agent** where a proprietary party identification is considered invalid or not understood |
| RUTA | ReturnUponUnableToApply | Return following investigation request and no remediation possible. | Sent by **Instructed Agent** that is unsatisfied with the outcome of the unable to apply request and is subsequently rejecting the payment instruction. Alternatively it can be used by the original **Creditor Agent** when the creditor is unable to apply the transaction |
| TM01 | InvalidCutOffTime | Associated message, payment information block, or transaction was received after agreed processing cut-off time. | Sent by **Instructed Agent** when the message was received after the agreed processing cut off time and an agreement is in place to reject rather than apply the next possible value date. |
| UPAY | UnduePayment | Payment is not justified. | Sent by **Instructed Agent** the payment is undue |

---

<!-- Page 367 -->

Definitions and High Level Use Cases

| Code | Name | ISO Definition | High Level Use Case |
|---|---|---|---|
| G004 | CreditPendingFunds | In a FIToFI Customer Credit Transfer: Credit to the creditor's account is pending, status Originator is waiting for funds provided via a cover. Update will follow from the Status Originator. | Optionally sent by **the Creditor Agent** when the cover has not been settled at the creditor agent account at the reimbursement agent |

---

<!-- Page 368 -->

Min 0 – Max 1

The pacs.002 FI to FI Payment Status Report optional **Effective Interbank Settlement Date** allows a choice of *Date* or *Date Time* to confirm when a point-to-point transaction is completed/effectuated.

When *Date Time* is chosen CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+-hh:mm
➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

---

<!-- Page 369 -->

Instructing Agent: Agent A
Instructed Agent: Agent B
pacs.008

Instructing Agent: Agent B
Instructed Agent: Agent C
pacs.008

pacs.004

Instructed Agent: Agent A
Instructing Agent: Agent B

pacs.002

Instructed Agent: Agent B
Instructing Agent: Agent C

**Instructing Agent** and **Instructed Agent** represent the Agents involved in the pacs point-to-point message exchange. These roles therefore change on each payment leg.

Instructing Agent and Instructed Agent elements are required in all pacs messages

Credit Transfer Transaction Information > Instructing Agent

---

<!-- Page 370 -->

Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases.

**Serial Financial Institution to Financial Institution to Customer Credit Transfer**
Use Case p.2.1.1 – High Level Payment Status Information (pacs.002) of multiple Payment Transaction Status updates
Use Case p.2.1.2 – High Level Rejection of an incomplete Customer Credit Transfer (pacs.008)
**Serial Financial Institution Credit Transfer**
Use Case p.2.2.1 – High Level Rejection of an incomplete Financial Institution Credit Transfer (pacs.009)
**Cover Method Financial Institution to Financial Institution to Customer Credit Transfer**
Use Case p.2.3.1.a – High Level Rejection of an incomplete payment using the cover method
Use Case p.2.3.1.b – High Level Rejection of an incomplete payment using the cover method
**Financial Institution Direct Debit**
Use Case p.2.4.1 – High Level Status Information of a Financial Institution Direct Debit
Use Case p.2.4.2 – High Level Rejection of a Financial Institution Direct Debit
**Financial Institution to Financial Institution Customer Direct Debit**
Use Case p.2.5.1 – High Level FI to FI Customer Direct Debit (pacs.003) successful settlement
Use Case p.2.5.2 – High Level FI to FI Customer Direct Debit (pacs.003) unsuccessful settlement

---

<!-- Page 371 -->

# Transaction Status updates

An agent may provide multiple Payment Status Information updates (with different Transaction Status codes) where bilaterally agreed, throughout the payment processing lifecycle i.e. from receipt through to onward processing.

**Flow:**
1. Debtor → Agent A
2. Agent A → Agent B (pac.008)
3. Agent B → Agent A (pac.002)
4. Agent B → Agent A (pac.002)
5. Agent B → Agent C (pac.008)
6. Agent C → Agent D (pac.008)
7. Agent D → Creditor

**Step Descriptions:**

1. Debtor initiates a payment instruction to the Debtor Agent

2. Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries

3. Agent B provides a status update ACTC (accepted technical validations are successful) to Agent A, based upon a bilateral agreement.

4. Agent B provides a further status update ACSP (accepted settlement in progress) to Agent A, based upon a bilateral agreement.

5. Agent B processes the payment on Agent C

Where a **payment is rejected**, the use of the pac.002

---

<!-- Page 372 -->

```
1 ➜ (A) ──pac.008──▶ (B) ──pac.008──▶ (C) ──pac.008──▶ (D) ──▶ 2
        ◀──pac.004──        ◀──pac.004──        ◀──pac.002──

(6) + Return Reason      + Return Reason      + Reject Reason
```

| 1 | 3 | 5 |
|---|---|---|
| Debtor initiates a payment instruction to the Debtor Agent | Agent B processes the payment on Agent C | ! Having received the payment Agent D recognises the payment can not be completed as requested e.g. the Creditor's account is closed. Agent D rejects the payment to Agent C using a Status information message (pac.002) also including the return reason code. | Agent C return funds to Agent B, together with the reason code for return. |
| 2 | 4 | 6 |
| Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries | Agent C processes the payment on Agent D | Agent B return funds to Agent A, together with the reason code for return. |
```

---

<!-- Page 373 -->

# (pacs.009)

**Sequence flow (A → B → C → D, with E as Creditor):**

- **1** A → B
- **2** B → C — `pacs.009`
- **3** C → D — `pacs.009`
- **5** B → A — `pacs.004`
- **4** D → C — `pacs.002`
- Callout: **+ Return Reason**
- Callout: **+ Reject Reason**
- **!** (exception)

---

**1** Agent A as the Debtor initiates a payment instruction to the Debtor Agent (Agent B)

**2** Agent C processes the payment onto Agent D

**!** Having received the payment Agent D recognises the payment can not be completed as requested e.g. the Creditor's account is closed. Agent D rejects the payment to Agent C using a Status Information message (pacs.002) also including the reject code.

**4** Agent C return funds to Agent B, together with the reason code for return.

**2** Debtor Agent (B) debits the account of Agent A and initiates a serial payment towards the Creditor (Agent E) using Agents C as an intermediary.

**5** Agent B advises Agent A of the return of payment together with the reason using camt.053 and may optionally provide a notification e.g. credit notification.

---

<!-- Page 374 -->

# 1

Debtor initiates a payment instruction to the Debtor Agent

# 2a

Debtor Agent (A) initiates a payment using the cover method to the Creditor Agent (D)

# 2b

In parallel the Debtor Agent (A) initiates a covering payment to credit the account of Agent (D) with their correspondent (Agent C)

# !

Having received the payment with settlement method COVE Agent D recognises (prior to the settlement via pacs.009 COV) the payment can not be completed as requested e.g. the Creditor's account is closed. Agent

# 3

Agent B processes the payment on Agent C

# 4

Agent C receives the payment and credits the account of Agent D

# 5

Agent C produces an end of day account statement report. An optional real time notifications e.g. credit notification

# 6b

Agent D requests the return of covering funds, together with the reason for return, having already rejected the pacs.008

# 7

Agent C return of covering funds to Agent B, together with the reason code for return.

# 8

Agent B return of covering funds to

---

**Message flow labels:**

- `pacs.008` (A → D)
- `pacs.002` (D → A)
- `pacs.009 cov` (A → B)
- `pacs.004` (B → A)
- `pacs.009 cov` (B → C)
- `pacs.004` (C → B)
- `camt.053` (C → D)
- `pacs.004` (D → C)

**Annotations:**

- `+ Reject Reason`
- `+ Return Reason` (at A)
- `+ Return Reason` (at B)
- `+ Return Reason` (at C)

**Note box:**

post-settlement returns see pacs.004 use case p.4.3.1.a and p.4.3.1.b

---

<!-- Page 375 -->

## Sequence Diagram – Nodes & Messages

**Agents:** A (Debtor Agent) · B · C · D (Creditor Agent)

**Messages (arrows):**
- A → D : `pacs.008`
- D → A : `pacs.002`
- A → B : `pacs.009 cov` / `pacs.004`
- B → C : `pacs.009 cov` / `pacs.004`
- C → D : `pacs.009 cov` / `pacs.002`

**Annotations:** `+ Reject Reason` · `+ Return Reason` (×2)

---

## Step Legend

**1**
Debtor initiates a payment instruction to the Debtor Agent

**2a**
Debtor Agent (A) initiates a payment using the cover method to the Creditor Agent (D)

**2b**
In parallel the Debtor Agent (A) initiates a covering payment to Agent (D) as the Creditor of the pacs.009 cov

**3**
Agent B processes the payment

**4**
Agent C receives the payment and credits their internal account with Agent D. Agent C forwards a pacs.009 cov with Settlement Method INDA (indicating Agent D is responsible for the settlement of this leg of the payment transaction.

**5**
Having not settled the pacs.009 cov Agent D rejects the covering funds, together with the reason for rejection.

**6**
Agent C returns the settled covering funds to Agent B, together with the reason code for return.

**7**
Agent C returns the settled covering funds to Agent B, together with the

---

> **Note (step 4 / rejection path):** Having received the payment Agent D recognises the payment can not be completed as requested e.g. the Creditor's account is closed. Having not

> **Reference box:** post-settlement return see pacs.004 use case p.4.3.1.a

---

<!-- Page 376 -->

# (pacs.010)

**Diagram Labels:**
*   Agent A
*   Agent B
*   Agent C
*   Agent D
*   Agent E
*   Messages: pacs.010, pacs.002, pacs.009, pacs.009, camt.053
*   Steps: 1, 1a, 2, 3, 4

**Step Descriptions:**

**1**
Agent E initiates a Direct Debit instruction to debit Agent A's account

**1a**
Agent B provides a positive status update to Agent E

**2**
Debtor Agent (B) initiates a serial payment towards the Creditor Agent (E) using Agents B & C as intermediaries

**3**
Agent C processes the payment on Agent D

**4**
Agent D credits the account of the Creditor (Agent E), and may optionally provide a notification e.g. credit notification in addition to an account statement (camt.053)

---

<!-- Page 377 -->

pacs.010

pacs.002

1

Agent D initiates a Direct Debit instruction to debit Agent A's account

!

Debtor Agent (B) rejects the instruction, using a pacs.002, as no mandate agreement is in place.

---

<!-- Page 378 -->

camt.053

pacs.003

pacs.002

pain.008

pain.002

Settlement Complete

1

Creditor initiates a direct debit instruction to the Creditor Agent

2

Creditor Agent (A) initiates a direct debit collection by sending a pacs.003 message to the Debtor Agent with the settlement method "INDA"

3

The Debtor Agent debits the account of the Debtor, and may optionally provide a notification e.g. debit notification in addition to an account statement (camt.053). The Debtor Agent also provides a status update ACSC (accepted settlement completed) to the Creditor Agent.

4

Creditor Agent (A) relays the status ACSC (accepted settlement completed) to the Initiating Party, based upon a bilateral agreement

---

<!-- Page 379 -->

### Diagram Labels

**1**
pain.008

**2**
pacs.002

**3**
pacs.003

**4**
pain.002

Reject Reason

A
B
!

---

### Step Descriptions

**1**
Creditor initiates a direct debit instruction to the Creditor Agent

**2**
Creditor Agent (A) initiates a direct debit collection by sending a pacs.003 message to the Debtor Agent with the settlement method "INDA"

**3**
The Debtor Agent fails to debit the account of the Debtor (e.g., account is closed). The Debtor Agent provides a status update RJCT (Rejected) with the rejection reason information.

**4**
Creditor Agent (A) relays the status RJCT (Rejected) to the Initiating Party with the rejection reason information

---

<!-- Page 380 -->

# Payment Return

---

<!-- Page 381 -->

| pacs.008 | pacs.009 cov | pacs.004 |
| :--- | :--- | :--- |
| Group Header | Group Header | Group Header |
| Credit Transfer Transaction Information | Credit Transfer Transaction Information | Transaction Information |
| | Underlying Customer Credit | Original Group Information |
| | | Original Transaction Reference |

In a similar structure to the pacs.009 (cov) underlying Customer Credit Transfer, the pacs.004 Payment Return message has amongst other elements Original Group Information which captures original information such as the Original UETR and Original Interbank Settlement Amount etc. and an Original Transaction Reference which contain the key elements of the original payment e.g. Debtor, Creditor etc.

---

<!-- Page 382 -->

# FI Customer Payment (pacs.008)

**Diagram Labels:**
*   pacs.008
*   pacs.002
*   pacs.008
*   pacs.002
*   Reject & Reason
*   pacs.004
*   Return & Reason
*   pacs.002

**The PaymentReturn message is sent by an agent to the previous agent in the payment chain to undo a payment previously settled.**

In the unlikely event that a pacs.004 is instructed by mistake, the best practice is to allow the Payment Return

---

<!-- Page 383 -->

# Group Header

---

<!-- Page 384 -->

Each ISO 20022 payment message has a **Min1 - Max1** ***Message Identification*** element, located in the Group Header. This **35 character** identifier is a point-to-point reference used to unambiguously identify the message.

For Payment Clearing and Settlement (pacs) messages the Message Identification has no exact equivalent in the legacy MT payment message. However, the MT 202 Sender's Reference (Field 20) could be considered a similar comparison where a pacs message contains a single Transaction.

Each transaction's *Credit Transfer Transaction Information* contains a variety of nested *Payment Identification* elements to capture reference related to the individual transaction such as a UETR (Unique End-to-end Transaction Reference)

---

<!-- Page 385 -->

Min 1 - Max 1

The pacs.004 message *Creation Date* captures the date and time which the message was created.

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
> For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- Page 386 -->

Min 1 – Max 1

The pacs.004 message **Number of Transactions** captures the number of individual transaction contained within the message.

The number of transactions in CBPR+ payment usage guidelines is fixed to 1.

Single transactions in the CBPR+ payment usage guidelines enable a transaction to be managed and unlocks highly automated, frictionless, instant payments, supporting the next generation of innovation.

---

<!-- Page 387 -->

Min 1 – Max 1
The pacs.004 ***Settlement Method*** element within the Group Header ***Settlement Information***, includes one of the embedded codes to indicate how the payment message will be settled.

The ***Settlement Method*** element in the pacs.004 allows a choice of an embedded code.

**INDA** indicate this Customer Credit Transfer will be settlement by the Instructed Agent (as the Account Servicing Institution) The account held at the Instructed Agent may captured in the dedicated ***Settlement Account*** element.
**INGA** indicate this Customer Credit Transfer has already been settlement by the Instructing Agent, who has credited the Account they service for the Instructed Agent (as an Account Owner). The account held by the Instructed Agent with the Instructing Agent may captured in the dedicated ***Settlement Account*** element.

Settlement Method code CLRG is not part of CBPR+ specifications but instead used in Market Infrastructure specification (HVPS+)

---

<!-- Page 388 -->

The pacs.004 message **Settlement Account** is a nested element as part of **Settlement Information**, this element identifies information related to an account used to settle the payment instruction.

Min 0 – Max 1
The **Settlement Account** identifies the account details maintained at the account servicing institution (Agent responsible for the settlement of the instruction as indicated in the **Settlement Method**)

- Min 1 – Max 1 **Identification** identifies the account maintained at the Debtor Agent (Account Servicing Institution)
- Min 0 – Max 1 **Type** uses the external Cash Account Type code list to identify the type of account
- Min 0 – Max 1 **Currency** identifies the currency if the account
- Min 0 – Max 1 **Name** identifies the name of the account as assigned by the Account Servicing Institution
- Min 0 – Max 1 **Proxy** captures an alternative identification of the account number such as an email address. This element has further nested **Type** which is a choice of external code list or proprietary code and **Identification** which are both mandatory where the Proxy element is used.

---

<!-- Page 389 -->

# Transaction Information

---

<!-- Page 390 -->

Min 0 – Max 1

The pacs.004 message **_Return Identification_** captures a point-to-point reference used to unambiguously identify the Payment Return message, created by the **_Instructing Agent_** in the **_Return Chain_**.

The 35 character return identifier could be considered similar to the legacy Sender's Reference (Field 20) of an MT return payment message.

---

<!-- Page 391 -->

Min 0 – Max 1

The pacs.004 *Payment Return* uses elements in the **Original Group Information** to capture the message identifier and message name of the underlying payment the *Payment Return* relates to. The mandatory **Original Message Identification** contains the point-to-point reference, and the mandatory **Original Message Name Identification** contains the message name of the underlying payment being returned. Optionally the **Original Creation Date Time** can also be captured.

For example:

*Original Message Name Identification* “pacs.008.001.xx” confirms the return is of a pacs.008 Financial Institution to Financial Institution Customer Credit Transfer. Where as “pacs.009.001.xx” confirms the return is of a pacs.009 Financial Institution Credit Transfer.

| | |
|---|---|
| **pacs.008** | |
| Message Identification | abcd1234 |
| **pacs.004** | |
| **Group Header** | Message Identification | xyz9875 |
| **Original Group Information** | Original Message Identification | abcd1234 |
| | Original Message | |

Note: the xx in the CBPR+ Usage Guideline represents the message version of the message

---

<!-- Page 392 -->

The *pacs.004 Payment Return* also uses a number of other **Original** elements in the **Transaction Information** to capture information from the underlying payment that the *Payment Return* relates to. **Mandatory** element examples of this (in addition to *Original Message identification* and *Original Message Name Identification* described on the previous page) include:

| | |
|---|---|
| **Original End to End Identification** | **Original UETR** |
| **Original Interbank Settlement Date** | **Original Interbank Settlement Amount** |

These Original elements enables the **Instructed Agent** in the *pacs.004 Payment Return* to re-associate the Return with the payment they originally sent.

Transaction Information
Original End to end Identification
Original UETR

---

<!-- Page 393 -->

# Settlement Date

The **_Returned Interbank Settlement Amount_** `Min 1 - Max 1` and subsequent **_Interbank Settlement Date_** `Min 1 - Max 1` are mandatory elements in the *pacs.004 Payment Return*, these elements are used to capture the currency and amount being returned together with the settlement date of the Payment Return.

The **_Returned Interbank Settlement Amount_** may be a different amount than the **_Original Interbank Settlement Amount_** (amount received the Agent instructing the *Payment Return*) for example a charge may have been levied for processing the *Payment Return* or the Payment Return is a partial amount for overpayment or partial refund

In this case the **_Returned Instructed Amount_** should be equal to the **_Interbank Settlement Amount_**, on the first leg of the *Payment Return*. Charge levied should also be captured in the **_Charge Information_** element.

Transaction Information
Returned Interbank Settlement Amount

---

<!-- Page 394 -->

The pacs.004 message has two optional elements to capture the optional information related to the settlement of the instructions.

**Min 0 – Max 1**
The **_Settlement Priority_** provides an optional choice of embedded codes to indicate the instruction's settlement priority from the perspective of the Instructing Agent. This point-to-point information may be used by the Instructed Agent to identify the priority associated with the **_Settlement Method_** and should not be confused with the _Instruction Priority_.
Note: Where the **_Settlement Method_** of the pacs.004 is 'INDA' (settled performed by the Instructed Agent) this indicates the Settlement Priority. Code 'INGA' implies settlement has already occurred for this point-to-point payment and therefore the Settlement Priority is not necessary.

**Min 0 – Max 1**
The **_Settlement Time Indication_** optionally captures the time settlement occurred at a transaction administrator such as a Market Infrastructure.
This DateTime can be captured in two nested elements, **_Debit Date Time_** and **_Credit Date Time_**.

---

<!-- Page 395 -->

Min 0 – Max 1
The ***Returned Instructed Amount*** captures currency and amount instructed by the ***Debtor*** in the ***Return Chain***. This conditional element is required when the ***Returned Interbank Settlement Amount*** is not the same currency and/or amount as originally instructed by the ***Debtor***. For example a charge is taken or the transactions is converted to another currency.

Min 0 – Max 1
The ***Exchange Rate*** capture the factor (rate) used to convert an amount from one currency into another. This reflects the currency pair price at which one currency was bought with another currency.

---

<!-- Page 396 -->

Min 1 – Max 1
The pacs.004 *Charge Bearer* element uses an embedded code that is used to specify which party/parties would bear any charges associated with processing the payment transaction. This element is comparable with MT Field 71A 'Details of Charges'

**ISO 20022**

| **Charge Bearer (1.1)** | **Code** | **Description** |
| :--- | :--- | :--- |
| | CRED | Creditor |
| | SHAR | Shared |

**MT 103**

| **71A: Details of Charges** | **Code** | **Description** |
| :--- | :--- | :--- |
| | BEN | Beneficiary |
| | SHA | Shared Charges |

Note: *Charge Bearer* code DEBT (implying the **Return Chain**, Debtor will bear any charges) is removed from the CBPR+ pacs.004. Should a non-CBPR+ Payment Return be received with Charge Bearer DEBT, it is recommended to use SHAR in any onward processed Payment Return.

---

<!-- Page 397 -->

Min 0 – Max *

The **Charges Information** element provides information on the return charges to be paid by the **Charge Bearer**. This element is comparable with MT Fields: 71F 'Senders Charges' and 71G 'Receiver's Charges', although pre-paid charges (legacy 71G 'Receiver's Charges' are an unlikely use case for Payment Returns

Min 0 – Max 1

| Charge Information (0..*) | Amount | In addition to the legacy MT message the pacs.004 *Charge Information* mandate the *Agent*, this represent the *Agent* who has taken a charge (deduct from the transaction) |
|---|---|---|
| | Currency | CBPR+ best practice recommends the use of the structured Agent BIC. |
| | Agent | BICFI |
| | | Name |
| | | Structured Postal Address |

As the **Charges Information** element is repetitive it can capture charges related to previous legs of the Payment Return transaction chain.

Note: *Charge Information* element is required where a charge is taken on the Payment Return. A charge for returning an incomplete payment by the originator of the Payment Return (Return Chain Debtor) is common practice. It is encouraged that Agents who processed the original payment transaction consider the total operation cost when defining their payment cost recovery model. Whereby further charges on Return Payments should be avoided.

---

<!-- Page 398 -->

[User Icon] [Bank A Icon] [Bank B Icon] [Bank C Icon] [Bank D Icon] [User Icon]

**Instructing Agent: Agent A** &rarr; **Instructed Agent: Agent B**
`pac.008`

**Instructed Agent: Agent A** &larr; **Instructing Agent: Agent B**
`pac.004`

**Instructing Agent: Agent B** &rarr; **Instructed Agent: Agent C**
`pac.008`

**Instructed Agent: Agent B** &larr; **Instructing Agent: Agent C**
`pac.004`

**Instructing Agent: Agent C** &rarr; **Instructed Agent: Agent D**
`pac.008`

**Instructed Agent: Agent C** &larr; **Instructing Agent: Agent D**
`pac.002`

***Instructing Agent*** and ***Instructed Agent*** represent the Agents involved in the pac point-to-point message exchange. These roles therefore change on each payment leg.

**Transaction Information** &check;
&rsaquo; **Instructing Agent**

---

<!-- Page 399 -->

Min 1 – Max 1

The mandatory **Return Chain** element captures all the parties involved in the return transaction, in much the same way the underlying payment message captures all the parties involved in a payment.

In this element the **role** of the various parties **change**, to reflect the fact the payment is now a *Payment Return*, for example, the *Creditor Agent* of the underlying payment may become the *Debtor Agent* of the *Payment Return*.

Although Ultimate Debtor and Ultimate Creditor are present in the Return chain it is extremely unlikely one of these Parties would be involved in the return chain and can only do so if present as an Ultimate Party in the original payment.

| | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| **original** | Debtor | Debtor Agent (A) | Previous Instructing Agent 1 (B) | Previous Instructing Agent 2 (C) | Instructing Agent (D) | 💵 | Instructed Agent & Creditor Agent (E) | Creditor |
| **return chain** | Creditor | Creditor Agent (A) | Intermediary Agent 2 (B) | Intermediary Agent 1 (C) | Instructed Agent (D) | 💵 | Debtor Agent & Instructing Agent (E) | Debtor |

Note: the static Previous Instructing Agent roles in the original payment transition to Intermediary Agent roles in the return chain

---

<!-- Page 400 -->

Arguably the most common example of a Payment Return is where it is initiated by the Creditor Agent of the original payment, this Agent's role the become the mandatory Debtor in the **Return Chain** element (as they owe the money to the party the return is intended for).
Recognising that the original Creditor is not party to the return, for example, they might be a known customer of the original Creditor Agent whereby a reject or return code 'AC01' may be used. In this way the original Creditor was not involved in the Payment Return.

| Chain | Flow |
|---|---|
| original | Debtor → Debtor Agent (A) → Previous Instructing Agent 1 (B) → Previous Instructing Agent 2 (C) → Instructing Agent (D) → $ → Instructed Agent & Creditor Agent (E) → Creditor |
| return chain | Creditor ← Creditor Agent (A) ← Intermediary Agent 2 (B) ← Intermediary Agent 1 (C) ← Debtor Agent & Instructed Agent (D) ← $ ← Debtor & Instructing Agent (E) |

**Note:** the static Previous Instructing Agent roles in the original payment transition to Intermediary

---

<!-- Page 401 -->

Various other Payment Return use cases exist where the common principal is the initiator of the Payment Return becomes the mandatory Debtor in the **Return Chain** element (as they owe the money to the party the return is intended for). And the mandatory Creditor in the **Return Chain** element is the party the payment is being returned to.

| | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|---|---|---|---|---|---|---|---|
| **original** | Debtor | Debtor Agent (A) | Instructing Agent (B) | Instructed Agent (C) | Intermediary Agent 1 (D) | Creditor Agent (E) | Creditor |
| **return chain** | Creditor | Creditor Agent (A) | Debtor Agent & Instructed Agent (B) | Debtor & Instructing Agent (C) | | | |

> **Note:** a party Rejecting the payment using a pacs.002 would not be considered to be involved in the Payment Return as they would not owe money to the party the return is intended for.

---

<!-- Page 402 -->

The **Min 1 – Max 1**
The ***Return Reason Information*** element captures detailed information on the return reason. Within this element:

* the ***Originator*** element helps identify the party who initiated the request to return the payment. This party would have been included in the underlying payment and may also be included the pacs.004 *Return Chain*.
* the ***Reason*** is mandatory and is represented by an externalised ***Code*** choice (🔗)
* the ***Additional Information*** element may also be included to provide ***further*** details on the reason for return.

The code list representing the *Return Reason* is part of the ISO 20022 external code list

Transaction Information > Return Reason Information >
> Originator

---

<!-- Page 403 -->

## Definitions and High Level Use Cases

| Code | Name | ISO Definition | High Level Use Case |
|---|---|---|---|
| A C01 | IncorrectAccountNumber | Format of the account number specified is not correct or Account number is missing | Sent by **any Agent** when a settlement account number is incorrect |
| A C02 | InvalidDebtorAccountNumber | Debtor account number invalid or missing | Sent by **any Agent** when Debtor account number is incomplete |
| A C04 | ClosedAccountNumber | Account number specified has been closed on the bank of account's books | Sent by **Creditor Agent** when the Creditor account number is closed |
| A C06 | BlockedAccount | Account specified is blocked, prohibiting posting of transactions against it. | Sent by **Creditor Agent** when Creditor account is blocked from posting credit entries. Sent by **any Agent** when a settlement account is blocked |
| A C07 | ClosedCreditorAccountNumber | Creditor account number closed | Sent by **Creditor Agent** when account number is closed. *CBPPlus recommended using AC04, but support AC07 to remain interoperable with other clearing systems.* |
| A C13 | InvalidDebtorAccountType | Debtor account type is missing or invalid | Sent by **any Agent** when Debtor account type element is incorrect |
| A GNT | IncorrectAgent | Agent in the payment workflow is incorrect | Sent by **any Agent** when an agent in the payment transaction has an incorrect identification element |
| A G01 | TransactionForbidden | Transaction forbidden on this type of account (formerly NoAgreement) | Sent by **any Agent** when the type of payment transaction is not allowed for the specified account |
| A G07 | UnsuccessfulDirectDebit | Debtor account cannot be debited for a generic reason. Code value may be used in general purposes and as a replacement for AM04 if debtor bank does not reveal its customer's insufficient funds for privacy reasons | Sent by **Debtor Agent** of a Direct Debit message, when debtor account can not be debited. |
| A M02 | NotAllowedAmount | Specific transaction/message amount is greater than allowed maximum | Sent by **any Agent** when payment amount is above an allowed amount. For example the clearing system with a upper amount threshold. |

---

<!-- Page 404 -->

| Code | Name | ISO Definition | High Level Use Case |
| :--- | :--- | :--- | :--- |
| AM03 | NotAllowedCurrency | Specified message amount is a non processable currency outside of existing agreement | Sent by **any Agent** when the currency of the payment is not allowed within the existing business agreement |
| AM04 | InsufficientFunds | Amount of funds available to cover specified message amount is insufficient. | Sent by **any Agent** when there is not sufficient funds to settle the payment transaction. |
| AM05 | Duplication | Payment is a duplicate of another payment | Sent by **any Agent** when the payment is a duplicate. CBPPlus *recommend using DUPL, but support AM05 to remain interoperable with other clearing systems.* |
| AM06 | TooLowAmount | Specified transaction amount is less than agreed minimum. | Sent by **any Agent** when the payment amount is below a minimum amount. |
| AM07 | BlockedAmount | Amount specified in message has been blocked by regulatory authorities | Sent by **any Agent** when the payment amount is blocked by regulators |
| AM09 | WrongAmount | Amount received is not the amount agreed or expected | Sent by **any Agent** when the payment amount is incorrect |
| BE01 | InconsistentWithEndCustomer | Identification of end customer is not consistent with associated account number (formerly CreditorConsistency). | Sent by **Creditor Agent** when there is an inconsistency between the Creditor's identification and the account number |
| BE04 | MissingCreditorAddress | Specification of creditor's address, which is required for payment, is missing/not correct (formerly IncorrectCreditorAddress). | Sent by **any Agent** when the Creditor's address is missing Sent by **Creditor Agent** when the Creditor's address is incorrect |
| BE05 | UnrecognisedInitiatingParty | Party who initiated the message is not recognised by the end customer | Sent by **Creditor Agent** when the initiating party is unknown to the beneficiary |
| BE07 | MissingDebtorAddress | Specification of debtor's address, which is required for payment, is missing/not correct. | Sent by **any Agent** when the address of the Debtor is missing or incorrect |

---

<!-- Page 405 -->

## Definitions and High Level Use Cases

| Code | Name | ISO Definition | High Level Use Case |
|---|---|---|---|
| BE10 | InvalidDebtorCountry | Debtor country code is missing or invalid | Sent by **any Agent** when the country code of the Debtor is missing or incorrect |
| BE11 | InvalidCreditorCountry | Creditor country code is missing or invalid | Sent by **any Agent** when the country code of the Creditor is missing or incorrect |
| BE16 | InvalidDebtorIdentificationCode | Debtor or Ultimate Debtor identification code missing or invalid | Sent by **any Agent** when the identification of the Debtor or Ultimate Debtor is missing or incorrect |
| BE17 | InvalidCreditorIdentificationCode | Creditor or Ultimate Creditor identification code missing or invalid | Sent by the **any Agent** when the identification of the Creditor or Ultimate Creditor is missing or incorrect |
| CN01 | AuthorisationCancelled | Authorisation is cancelled. | Sent by **any Agent** when a third party debit authorisation has been cancelled or is not in place. |
| CNOR | Creditor bank is not registered | Creditor bank is not registered under this BIC in the Clearing Settlement Mechanism (CSM) | Sent by **any Agent** when the Creditor Agent is not reachable in the Market Infrastructure (CSM) and an appropriate correspondent can not be determined. |
| CURR | IncorrectCurrency | Currency of the payment is incorrect | Sent by the **Creditor Agent** when the **Interbank Settlement Amount** Currency is not the same as the Creditor account currency and a currency conversion is not accepted on the Creditor's account. |
| CUST | RequestedByCustomer | Cancellation requested by the Debtor | Sent by **any Agent** upon request by Debtor. CBPPplus recommend using **FOCR**, but support **CUST** to remain interoperable with *other clearing systems*. |
| DT01 | InvalidDate | Invalid date (eg, wrong or missing settlement date) | Sent by **any Agent** when the settlement date is in the past and an agreement is in place to reject rather than apply the next possible value date. |
| DT04 | FutureDateNotSupported | Future date not supported | Sent by **any Agent** when a future settlement date is not supported or appear to be an error e.g. is the r wrong year. |

---

<!-- Page 406 -->

Definitions and High Level Use Cases

| Code | Name | ISO Definition | High Level Use Case |
|---|---|---|---|
| DUPL | DuplicatePayment | Payment is a duplicate of another payment | Sent by **any Agent** when the payment is a duplicate |
| ERIN | ERIOptionNotSupported | The Extended Remittance Information (ERI) option is not supported. | Sent by **any Agent** when extended **Remittance information (Related Remittance Information)** is not supported or bilaterally/multilaterally agreed |
| ED05 | SettlementFailed | Settlement of the transaction has failed. | Sent by **any Agent** when the settlement of payment has failed or been unsuccessful. |
| FF03 | InvalidPaymentTypeInformation | Payment Type Information is missing or invalid. Generic usage if cannot specify Service Level or Local Instrument code | Sent by **any Agent** when the Payment Type Information (**Instruction Priority, Clearing Channel**) provided for the payment is incorrect or not supported. |
| FF04 | InvalidServiceLevelCode | Service Level code is missing or invalid | Sent by **any Agent** when the Payment Type Information **Service Level** provided for the payment is incorrect or not supported |
| FF05 | InvalidLocalInstrumentCode | Local Instrument code is missing or invalid | Sent by **any Agent** when the Payment Type Information **Local Instrument** provided for the payment is incorrect or not supported |
| FF06 | InvalidCategoryPurposeCode | Category Purpose code is missing or invalid | Sent by **any Agent** when the Payment Type Information **Category Purpose** provided for the payment is incorrect or not supported |
| FF07 | InvalidPurpose | Purpose is missing or invalid | Sent by **any Agent** when the **Purpose** provided for the payment is either missing or incorrect |
| FOCR | FollowingCancellationRequest | Return following a cancellation request | Sent by **any Agent** that has accepted a payment cancellation request (camt.056) and subsequently is rejecting the unsettled payment instruction. |
| FR01 | Fraud | Returned as a result of fraud. | Sent by **any Agent** when the payment is identified as fraudulent. |
| MP04 | No Mandate | No Mandate | Sent by **any Agent** when a Direct Debit message has no mandate in place |

---

<!-- Page 407 -->

## Definitions and High Level Use Cases

| Code | Name | ISO Definition | High Level Use Case |
|---|---|---|---|
| MD02 | MissingMandatoryInformationInMandate | Mandate related information data required by the scheme is missing. | Sent by **any Agent** when information required by the clearing scheme is missing. |
| MD05 | CollectionNotDue | Creditor or creditor's agent should not have collected the direct debit | Sent by **any Agent** when a Direct Debit collection was not due |
| MD07 | EndCustomerDeceased | End customer is deceased. | Sent by **Creditor Agent** when the Creditor or Ultimate Creditor is deceased |
| MS02 | NotSpecifiedReasonOnCustomerGenerated | Reason has not been specified by end customer | Sent by **Creditor Agent** where instructed to reject by the Creditor, but no reason was specified |
| MS03 | NotSpecifiedReasonOnAgentGenerated | Reason has not been specified by agent. | Sent by **any Agent** but no reason is specified |
| NARR | Narrative | Reason is provided as narrative information in the additional reason information. | Sent by **any Agent** the reason is provided as narrative information. **Only to be used where no other code is appropriate** (i.e. exceptional circumstances) |
| NOAS | NoAnswerFromCustomer | No response from Beneficiary | Sent by **any Agent** when the Creditor did not respond to query for additional information in order that the payment could be credited e.g. currency control documentation. |
| NOCM | Not compliant (more generic) | Customer account is not compliant with regulatory requirements, for example FICA (in South Africa) or any other regulatory requirements which render an account inactive for certain processing. | Sent by **any Agent** when the Creditor account is not compliant with certain regulatory requirements. |
| RC01 | BankIdentifierIncorrect | Bank identifier code specified in the message has an incorrect format (formerly IncorrectFormatForRoutingCode). | Sent by **any Agent** when an incorrect BIC has been used in the payment |
| RC03 | InvalidDebtorBankIdentifier | Debtor bank identifier is invalid or missing | Sent by **any Agent** when the Debtor Agent identification is incorrect or missing |

---

<!-- Page 408 -->

# Definitions and High Level Use Cases

| Code | Name | ISO Definition | High Level Use Case |
| :--- | :--- | :--- | :--- |
| RC04 | InvalidCreditorBankIdentifier | Creditor bank identifier is invalid or missing | Sent by **any Agent** when the Creditor Agent identification is incorrect or missing |
| RC08 | InvalidClearingSystemMemberIdentifier | ClearingSystemMemberIdentifier is invalid or missing. Generic usage if cannot specify between debit or credit account | Sent by **any Agent** when the clearing system member identification for an Agent is incorrect |
| RC11 | InvalidIntermediaryAgent | Intermediary Agent is invalid or missing | Sent by **any Agent** when the intermediary agent identification is incorrect |
| RF01 | NotUniqueTransactionReference | Transaction reference is not unique within the message. | Sent by **any Agent** when the transaction reference (UETR and Instruction Identification) are not unique |
| RR01 | Missing Debtor Account or Identification | Specification of the debtor's account or unique identification needed for reasons of regulatory requirements is insufficient or missing | Sent by **any Agent** when the Debtor identification or debtor account is missing, or the information provided are not sufficient |
| RR02 | Missing Debtor Name or Address | Specification of the debtor's name and/or address needed for regulatory requirements is insufficient or missing. | Sent by **any Agent** since the Debtor name or Address is missing, or information provided is not sufficient |
| RR03 | Missing Creditor Name or Address | Specification of the creditor's name and/or address needed for regulatory requirements is insufficient or missing. | Sent by **any Agent** since the Creditor name or Address is missing, or information provided is not sufficient |
| RR04 | Regulatory Reason | Regulatory Reason | Sent by **any Agent** due to any unspecified regulatory reason |
| RR05 | Regulatory Information Invalid | Regulatory or Central Bank Reporting information missing, incomplete or invalid. | Sent by **any Agent** when the reporting information required by the central bank or reporting authority is missing or not complete |

---

<!-- Page 409 -->

Definitions and High Level Use Cases

| Code | Name | ISO Definition | High Level Use Case |
|---|---|---|---|
| RR07 | RemittanceInformationInvalid | Remittance information structure does not comply with rules for payment type. | Sent by **any Agent** since the remittance information is incorrect |
| RR08 | RemittanceInformationTruncated | Remittance information truncated to comply with rules for payment type. | Sent by **any Agent** where the Structured Remittance Information has not been bilaterally or multilaterally agreed, which or has resulted in truncation |
| RR09 | InvalidStructuredCreditOrReference | Structured creditor reference invalid or missing. | Sent by **any Agent** when the structure of the creditor reference in the remittance information is invalid or missing |
| RR11 | InvalidDebtorAgentServiceID | Invalid or missing identification of a bank proprietary service. | Sent by **any Agent** where the proprietary identification for the Debtor is invalid or not understood |
| RR12 | InvalidPartyID | Invalid or missing identification required within a particular country or payment type. | Sent by **any Agent** where a proprietary party identification is considered invalid or not understood |
| RUTA | ReturnUponUnableToApply | Return following investigation request and no remediation possible. | Sent by **any Agent** that is unsatisfied with the outcome of the unable to apply request and is subsequently rejecting the payment instruction. Alternatively it can be used by the original **Creditor Agent** when the creditor is unable to apply the transaction |
| TM01 | InvalidCutOffTime | Associated message, payment information block, or transaction was received after agreed processing cut-off time. | Sent by **any Agent** when the message was received after the agreed processing cut off time and an agreement is in place to reject rather than apply the next possible value date. |
| UPAY | UnduePayment | Payment is not justified. | Sent by **any Agent** the payment is undue |

---

<!-- Page 410 -->

Min 0 – Max 1

The **Original Transaction Reference** optionally capture elements related to the original transactions. The inclusion of this element is particularly useful where the *Payment Return* includes an Agent not party to the original transaction, or where a significant time lapse has occurred between the original payment and the *Payment Return* i.e., information may have been archived by Agent in the Return chain. CBPR+ has two rules describing when the Original Transaction Reference should be used.

The *Amount* within the nesting of this Original Transaction Reference element only allows for the *Instructed Amount*, as instructed by the Debtor in the original payment initiation request. If the *Instructed Amount* was present in the original payment, populating this data is simple. However, we should also recognise the *Instructed Amount* is not always present (and in fact is not available in the pacs.009), whereby this value should represent the amount in the *Interbank Settlement Amount* of the pacs message being returned. The use of *Instructed Amount* is best described in the pacs.008 [Currency and Amount section](#).

🔍 **Note:** the role of Parties and Agent in Original element remain unchanged unlike elements such as the Return chain

Transaction Information > Original Transaction Reference >

---

<!-- Page 411 -->

```
[User] → [A] --pac.008--> [B] --pac.008--> [C] --pac.008--> [D] → [User]
         [A] <--pac.004-- [B] <--pac.004-- [C] <--pac.002-- [D] !

[A] + Return Reason
[B] + Return Reason
[C] + Reject Reason

Within the Payment Return (pac.004)
- the *Original Group Information* element is used to refers to original message for which the return relates to. e.g. based upon the above example pac.008 as the original message would be included in the pac.004
- the *Transaction Information > Original UETR* element would include UETR of the payment message received. i.e. the **same UETR is used on the Payment Return**.
- the *Original Transaction Reference* element includes detail from the *Original Message Name Identification* e.g. the Debtor of the original pac.008.001.xx
- the *Return Chain* element includes the parties in the return payment chain, noting the parties reverse (i.e. change role) from the original payment whereby the *Debtor* of the original payment becomes the *Creditor* in the Return Chain
```

---

<!-- Page 412 -->

Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases.

**Serial Customer Payments**
Use Case p.4.1.1 – Payment Return (pacs.004) of an incomplete Customer Credit Transfer (pacs.008)
Use Case p.4.1.2 – Payment Return (pacs.004) of a complete Customer Credit Transfer (pacs.008)
Use Case p.4.1.2.a – Partial Payment Return (pacs.004) of a complete Customer Credit Transfer (pacs.008)
Use Case p.4.1.2.b – Refund Payment of a complete Customer Credit Transfer (pacs.008)
Use Case p.4.1.3 - Payment Return (pacs.004) of an incomplete Customer Credit Transfer (pacs.008) involving a Market Infrastructure

**Serial Financial Institution Payments**
Use Case p.4.2.1 - Payment Return (pacs.004) of an incomplete Financial Institution Credit Transfer (pacs.009)
Use Case p.4.2.2 - Payment Return (pacs.004) of a complete Financial Institution Credit Transfer (pacs.009)
Use Case p.4.2.3 - Payment Return (pacs.004) of an incomplete Financial Institution Credit Transfer (pacs.009) involving a Market Infrastructure

**Cover Method Payments**
Use Case p.4.3.1.a - Payment Return (pacs.004) of an incomplete payment using the cover method
Use Case p.4.3.1.b - Payment Return (pacs.004) of an incomplete payment using the cover method
Use Case p.4.3.2 - Payment Return (pacs.004) of a complete payment using the cover method
Use Case p.4.3.2.a - Payment Return (pacs.004) of a complete payment using the cover method
Use Case p.4.3.3 - Payment Return (pacs.004) of an incomplete cover payment

---

<!-- Page 413 -->

# (pacs.008)

1 → 2 → 3 → 4 → 5 → 6

- **1** (Debtor) → **2** (Agent A) `pacs.008` → **3** (Agent B) `pacs.008` → **4** (Agent C) `pacs.008` → **5** (Agent D) → (Creditor)
- **2** (Agent A) `pacs.004` ← **3** (Agent B) `pacs.004` ← **4** (Agent C) `pacs.004` ← **5** (Agent D)
- **+ Return Reason** (under step 2/3)
- **+ Return Reason** (under step 3/4)
- **+ Return Reason** (under step 4/5)

---

**1**
Debtor initiates a payment instruction to the Debtor Agent

**2**
Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries

**3**
Agent B processes the payment on Agent C

**4**
Agent C processes the payment on Agent D

**!**
Having received the payment Agent D recognises the payment can not be completed as requested e.g. the Creditor's account is closed. Agent D return the payment to Agent C (as the original payment had already settled) together with the return reason.

**5**
Agent C return funds to Agent B, together with the reason code for return.

**6**
Agent B return funds to Agent A, together with the reason code for return.

---

<!-- Page 414 -->

## Flow Diagram

`Debtor (1) → Agent A (2) → Agent B (3) → Agent C (4) → Creditor (5)`

- **Forward messages (top arrows):** `pac.008` (A→B, B→C, C→D)
- **Return messages (bottom arrows):** `pac.004` (B→A [8], C→B [7], D→C [6])
- **Return Reason callouts:** `+ Return Reason` (steps 8, 7, 6)

| Step 1 | Step 3 | Step ! | Step 7 |
|---|---|---|---|
| **1**<br>Debtor initiates a payment instruction to the Debtor Agent | **3**<br>Agent B processes the payment on Agent C | **!**<br>Creditor determines that they wish to return the payment e.g. they are unable to apply, and instructs their bank (Agent D) to return the payment together with the reason. | **7**<br>Agent C return funds to Agent B, together with the reason code for return. |
| **2**<br>Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries | **4**<br>Agent C processes the payment on Agent D | **6**<br>Agent D returns the payment to Agent C using a Payment Return message (pac.004) also including the return reason code. | **8**<br>Agent B return funds to Agent A, together with the reason code for return. |
| | **5**<br>Agent D credits the account of the Creditor, and may optionally | | |

---

<!-- Page 415 -->

# (pacs.008)

**Payment flow (forward – pacs.008):**

Debtor → **1** → Agent **A** → **2** `pacs.008` → Agent **B** → **3** `pacs.008` → Agent **C** → **4** `pacs.008` → Agent **D** → **5** → Creditor

**Return flow (backward – pacs.004):**

Creditor → **6** `pacs.004` → Agent **C** → **7** `pacs.004` → Agent **B** → **8** `pacs.004` → Agent **A** → Debtor

- **6** `pacs.004` — **+ Return Reason**
- **7** `pacs.004` — **+ Return Reason**
- **8** `pacs.004` — **+ Return Reason**

---

**1** Debtor initiates a payment instruction to the Debtor Agent

**2** Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries

**3** Agent B processes the payment on Agent C

**4** Agent C processes the payment on Agent D

**5** Agent D credits the account of the Creditor, and may optionally

**!** Creditor determines that they wish to partially return the payment e.g. they were over paid or provide a partial refund, and instructs their bank (Agent D) to partially return the payment together with the reason.

**6** Agent D returns the payment to Agent C using a Payment Return

**7** Agent C return funds to Agent B, together with the reason code for return.

**8** Agent B return funds to Agent A, together with the reason code for return.

---

<!-- Page 416 -->

1 → 2 → **pac.008** → 3 → **pac.008** → 4 → **pac.008** → 5 → !

(A) (B) (C) (D)

**1**
Debtor initiates a payment instruction to the Debtor Agent

**2**
Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries

**3**
Agent B processes the payment on Agent C

**4**
Agent C processes the payment on Agent D

**5**
Agent D credits the account of the Creditor, and may optionally provide a notification e.g. credit notification in addition to an account statement (camt.053)

**!**
Creditor determines that they wish to refund the payment e.g. they could not provide the goods or services paid for. They instruct a new payment from their bank account.

In some circumstances the Creditor may take it upon themselves to provide a refund, using a new payment. Equally the period the original payment is store prior to data archive, particularly by the Creditor

---

<!-- Page 417 -->

# (pac s.008) involving a Market Infrastructure

**Diagram annotations**

1 → 2 → 3 → 4

- Agent **A** → `pac s.008` → Market Infrastructure → `pac s.008` → Agent **B**
- Market Infrastructure → `pac s.004` → Agent **A**
- Market Infrastructure → `pac s.004` → Agent **B**
- **+ Return Reason** (at step 2)
- **+ Return Reason** (at step 3)
- Legend: **pre-settlement reject see pac s.002 section**

**Step descriptions**

**1**
Debtor initiates a payment instruction to the Debtor Agent

**2**
Debtor Agent (A) initiates a serial payment towards the Creditor Agent (B) using the local currency ISO 2022 Market Infrastructure

**3**
The payment is **settled** via the local ISO 2022 Market Infrastructure, whereby the payment is forwarded to the Creditor Agent (B)

**!**
Having received the payment Agent B recognises the payment can not be completed as requested e.g. the Creditor's account is closed. Agent B returns the payment to Agent A using a Payment Return message (pac s.004) also including the return reason code.

**4**
The Market Infrastructure returns the payment performing the necessary settlement posting between Agent B and Agent A.

---

<!-- Page 418 -->

# (pacs.009)

**Sequence flow (Agents A → B → C → D → E):**

- **1** A → B : `pacs.009`
- **2** B → C : `pacs.009`
- **3** C → D : `pacs.009`
- **4** D → C : `pacs.002`  *(+ Reject Reason)*
- **5** C → B : `pacs.004`  *(+ Return Reason)*
- B → A : `camt.053`

---

**1** Agent A as the Debtor initiates a payment instruction to the Debtor Agent (Agent B)

**2** Debtor Agent (B) debits the account of Agent A and initiates a serial payment towards the Creditor (Agent E) using Agents C as an intermediary.

**3** Agent C processes the payment onto Agent D

**!** Having received the payment instruction Agent D recognises the payment can not be completed as requested e.g. the Creditor's account is closed. Agent D rejects the payment to Agent C using a Status Information message (pacs.002) also including the return reject code.

**4** Agent C return funds to Agent B, together with the reason code for return.

**5** Agent B advises Agent A of the return of payment together with the reason using camt.053 and may optionally provide a notification e.g. credit notification.

---

<!-- Page 419 -->

# (pacs.009)

**Payment Flow Diagram**

Agent A → (1) `pacs.009` / `camt.053` (5) → Agent B → (2) `pacs.009` / `pacs.004` (4) → Agent C → (3) `camt.053` / `pacs.004` (1) → Agent D

- `pacs.004` (B→C): **+ Return Reason**
- `pacs.004` (C→D): **+ Return Reason**

---

**1** Agent A as the Debtor initiates a payment instruction to the Debtor Agent (Agent B)

**2** Debtor Agent (B) debits the account of Agent A and initiates a serial payment towards the Creditor (Agent D) using Agents C as an intermediary.

**3** Creditor Agent (C) credits the account of Agent D and may optionally provide a notification e.g. credit notification, in addition to an account statement (camt.053)

**!** Having received the payment Agent D recognises the payment is incorrect e.g. the wrong amount was received . Agent D sends a Payment Return to Agent C including the return reason.

**4** Agent C return funds to Agent B, together with the reason code for return.

**5** Agent B advises Agent A of the return of payment together with the reason using the camt.053 and may optionally provide a notification e.g. credit notification.

---

<!-- Page 420 -->

# Transfer (pacs.009) involving a Market Infrastructure

**Flow:** A →(pacs.009)→ B →(pacs.009)→ C →(pacs.009)→ D
**Returns:** D →(camt.053)→ A ; C →(pacs.004, + Return Reason)→ B ; B →(pacs.004, + Return Reason)→ A

1. Agent A as the Debtor initiates a payment instruction to the Debtor Agent (Agent B)

2. Debtor Agent (B) debits the account of Agent A and initiates a serial payment towards the Creditor (Agent D) using the local currency ISO 20022 Market Infrastructure.

3. The payment is settled via the local ISO 20022 Market Infrastructure, whereby the payment is forwarded to the Creditor Agent (C)

4. Agent C returns the payment to Agent B, together with the reason code for the return

5. The payment return is settled via the local ISO 20022 Market Infrastructure, whereby the payment return is forwarded to the Creditor Agent (B)

6. Agent B advises Agent A of the return of payment together with the reason using the camt.053 and may optionally provide a notification e.g. credit notification.

! Having received the payment Agent C recognises the payment can not be completed as requested e.g. the Creditor's account is closed. Agent C returns the payment towards Agent B using a Payment Return message (pacs.004) also including the return reason code.

---

<!-- Page 421 -->

1
Debtor initiates a payment instruction to the Debtor Agent

2a
Debtor Agent (A) initiates a payment using the cover method to the Creditor Agent (D)

2b
In parallel the Debtor Agent (A) initiates a covering payment to create an account of Agent (D) with their correspondent (Agent C)

3
Agent B processes the payment

4
Agent C receives the payment and credits the account of Agent D

5
Agent C produces an end of day account statement report. An optional real time notifications e.g. credit notification (camt.054) may have also been created at the time of the credit posting

6
Agent D instructs the return of settled covering funds, together with the reason for return.

7
Agent C returns the **settled** covering funds to Agent B, together with the reason code for return.

8
Agent D returns the **settled** covering funds to Agent B, together with the

**Diagram Flow & Labels:**

*   **1** → **2a**: `pacs.008`
*   **2b** → **3**: `pacs.009 cov`
*   **3** → **8**: `pacs.004`
*   **8** → **4**: `pacs.004 cov`
*   **4** → **7**: `pacs.004`
*   **7** → **5**: `camt.053`
*   **5** → **6**: `pacs.004`

**+ Return Reason** (associated with steps 2b, 3, 5, 6)

**Note (Step 6):**
pre-settlement rejects see pacs.004 use case p.2.3.1

**Note (Bottom):**
Having received the payment, Agent D recognises the payment can not be

---

<!-- Page 422 -->

# Sequence Diagram

**Participants:** Debtor → Agent A → Agent B → Agent C → Agent D → Creditor

## Message Flow

- **A → D:** `pacs.008`
- **D → A:** `pacs.002`
- **A → B:** `pacs.009 cov`
- **B → A:** `pacs.004` (+ Return Reason)
- **B → C:** `pacs.009 cov`
- **C → B:** `pacs.004` (+ Return Reason)
- **C → D:** `pacs.009 cov`
- **D → C:** `pacs.002` (+ Reject Reason)

## Steps

**1**
Debtor initiates a payment instruction to the Debtor Agent

**2a**
Debtor Agent (A) initiates a payment using the cover method to the Creditor Agent (D).

**2b**
In parallel the Debtor Agent (A) initiates a covering payment to Agent (D) as the Creditor of the pacs.009 cov

**3**
Agent B processes the payment

**4**
Agent C receives the payment and credits their internal account with Agent D. Agent C forwards a pacs.009 cov with Settlement Method INDA (indicating Agent D is responsible for the settlement of this leg of the payment transaction.

**5**
Having not settled the pacs.009 cov Agent D rejects the covering funds, together with the reason for rejection.

**6**
Agent C returns the settled covering funds to Agent B, together with the reason code for return.

**7**
Agent B returns the settled covering funds to Agent A, together with the

> **Note:** post-settlement return see pacs.004 use case p.4.3.1.a

---

<!-- Page 423 -->

```
1
Debtor initiates a payment instruction to the Debtor Agent

2a
Debtor Agent (A) initiates a payment using the cover method to the Creditor Agent (D)

2b
In parallel the Debtor Agent (A) initiates a covering payment to credit the account of Agent (D) with their correspondent (Agent C)

3
Agent B processes the payment

4
Agent C receives the payment and credits the account of Agent D

5
Agent C produces an end of day account statement report. An optional real-time notification e.g.

6
Agent D reconciles the covering funds and credits the account of the Creditor, and may optionally provide a notification e.g., credit notification (camt.054)

7
Agent D requests the return of covering funds, together with the return reason.

8
Agent C return of covering funds to Agent B, together with the reason code for return.

9
Agent B return of covering funds to

!
Creditor determines that they wish to return the payment e.g. they are

+ Return Reason

+ Return Reason

+ Return Reason

[Flow]
1 → A → 2a → pacs.008 → D → 6 → !
A → 2b → pacs.009 cov / pacs.004 → B → 3
B → 4 / 5 → pacs.009 cov / pacs.004 → C → 8
C → 7 → camt.053 / camt.054 → D
```

---

<!-- Page 424 -->

1
Debtor initiates a payment instruction to the Debtor Agent

2a
Debtor Agent (A) initiates a payment using the cover method to the Creditor Agent (D)

2b
In parallel the Debtor Agent (A) initiates a covering payment to credit the account of Agent (D) with their correspondent (Agent C)

3
Agent B processes the payment

4
Agent C receives the payment and credits the account of Agent D

5
Agent C produces an end of day account statement report. An optional real time notifications e.g. credit notification

6
Agent D reconciles the covering funds and processes the payment onto Agent E

7
Agent E credits the account of the Creditor, and may optionally provide a notification e.g., credit

8
Agent E determines that they wish to return the payment e.g. they are unable to apply, and instructs their bank (Agent E) to return the payment together with the reason.

9
Agent D returns the **original** pacs.009 cov. using a pacs.004 together with the reason for return.

10
Agent C return of covering funds to Agent B, together with the reason code for return.

**Message flows (arrows):**

- A → D: `pacs.008`
- A → B: `pacs.009 cov`
- B → A: `pacs.004` + Return Reason
- B → C: `pacs.009 cov`
- C → B: `pacs.004` + Return Reason
- C → D: `pacs.005`
- D → C: `pacs.004` + Return Reason
- D → E: `pacs.008`
- E → D: `pacs.004` + Return Reason

**Step markers:** 1, 2a, 2b, 3, 4, 5, 6, 7, 8, 9, 10, 11

**Agents:** A (Debtor Agent), B, C, D (Creditor Agent), E (Creditor)

---

<!-- Page 425 -->

# Sequence Diagram – Cover Payment / Return Flow

**Actors:** A (Debtor Agent) · B · C · D (Creditor Agent)

**Message flow (top diagram):**

- `1` → A
- `2a` / `6`: A → D  `pacs.008`  /  `camt.056`
- `2b`: A → B  `pacs.009 cov`
- `5`: B → A  `pacs.004`  → **+ Return Reason**
- `3`: B → C  `pacs.009 cov`
- `4`: C → B  `pacs.002`  → **+ Reject Reason**

> **Note (green box):** See use case p.8.2.1 for the cover payment sample c.29.2.2 for case resolution and p.56.2.2 for payment return

---

## Step Descriptions

**1**
Debtor initiates a payment instruction to the Debtor Agent

**2a**
Debtor Agent (A) initiates a payment using the cover method to the Creditor Agent (D)

**2b**
In parallel the Debtor Agent (A) initiates a covering payment to credit the account of Agent (D) with their correspondent (Agent C)

**3**
Agent B processes the payment on Agent C

**!**
Agent C receives the payment and recognises the payment can not be completed as requested e.g. the Agent D does not maintain an account with them.

**4**
Agent C rejects the covering funds to Agent B, together with the reason code for rejection.

**5**
Agent B return of covering funds to Agent A, together with the reason code for return.

**6**
Agent A initiates a Request for Cancellation include the Cancellation

---

<!-- Page 426 -->

# Financial Institution
# Direct Debit

---

<!-- Page 427 -->

pacs.010

- Group Header
- Credit Instruction

The pacs.010 has two core sets of nested elements:

- ***Group Header*** which contains a set of characteristics that relates to the transaction
- ***Credit Instruction*** which contains elements providing information specific to direct debit transaction information and credit instruction.

Typically a Direct Debit message in a many-to-many payment (FINplus service) would be considered a point-to-point message, successfully resulting in a payment transaction which may be exchange over various messages.

---

<!-- Page 428 -->

A B C

secl.010

pacs.010

pacs.002

camt.053 camt.053

The Financial Institution Direct Debit message (pacs.010) is sent by a Financial Institution, directly or through another agent, to the Debtor Agent. It is used to instruct the Debtor Agent to move funds from the Debtor's account to the Creditor, where both Debtor and Creditor are financial institutions.

---

<!-- Page 429 -->

A B C D

secl.010

pacs.010

pacs.002

camt.053

pacs.009

camt.053

The Financial Institution Direct Debit message (pacs.010) is sent by a Financial Institution, directly or through another agent, to the Debtor Agent. It is used to instruct the Debtor Agent to move funds from the Debtor's account to the Creditor, where both Debtor and Creditor are financial institutions.

---

<!-- Page 430 -->

# Group Header

---

<!-- Page 431 -->

Min 1 – Max 1

Each ISO 20022 payment message has a **Message Identification** element, located in the Group Header. This **35 character** identifier is a point-to-point reference used to unambiguously identify the message.

For Payment Clearing and Settlement (pacs) messages the Message Identification has no exact equivalent in the legacy MT payment message. However, the Sender's Reference (Field 20) could be considered a similar comparison where a pacs message contains a single Transaction.

Group Header > Message Identification

---

<!-- Page 432 -->

Min 1 – Max 1

The pacs.010 message *Creation Date Time* captures the date and time which the message was created.

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
> For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- Page 433 -->

Min 1 – Max 1

The pacs.0010 message **Number of Transactions** captures the number of individual transaction contained within the message.

The number of transactions in CBPR+ payment usage guidelines is fixed to 1.

Single transactions in the CBPR+ payment usage guidelines enable a transaction to be managed and unlocks highly automated, frictionless, instant payments, supporting the next generation of innovation.

---

<!-- Page 434 -->

# Credit Instruction

---

<!-- Page 435 -->

Min 1 – Max 1

The Financial Institution Direct Debit **Credit Identification** provides a mandatory element to identify the Direct Debit instruction.

**Unique reference** assigned by the account servicer to unambiguously identify the account report. Directly comparable with the *Transaction Reference Number* (Field 20) of the legacy MT Financial Markets Direct Debit message.

Credit Instruction > Credit Identifier

---

<!-- Page 436 -->

A B C D

`pac s.010`

**Instructed Agent: Agent B**

**Instructing Agent: Agent D**

`pac s.009` `pac s.009`

*Instructing Agent* and *Instructed Agent* represent the Agents involved in the pac s point-to-point message exchange. These roles therefore change on each message leg.

*Instructing Agent* and *Instructed Agent* elements are required in all pac s messages and is only available in the **Credit Instruction**.

Credit Instruction
Instructing Agent

---

<!-- Page 437 -->

Min 0 – Max 1
The **Creditor Agent** is a static role in the pacs messages. This agent maintain a relationship with their customer, the *Creditor*. Like the pacs.009 the Creditor Agent is optional, which cover the scenario where the Debtor and Creditor (as Financial Institutions) maintain a direct Nostro/Vostro account relationship, or where the Debtor Agent maintain the account of both the Debtor and Creditor.

Min 0 – Max 1
Where the **Creditor Agent** is utilised the **Creditor Agent Account** may optionally be used to capture the account of the Creditor Agent with the Agent immediate before them in the transaction chain (the Agent Serving their account)
This would only apply where the message includes a *Creditor Agent*, however CBPPlus does not recommend to use this element unless mandated within a community or bilaterally agreed.

Credit Instruction
> Creditor Agent

---

<!-- Page 438 -->

The ISO 20022 pacs messages describe the Agent whose account is credited for a transaction as the *Creditor*. The *Creditor* sub elements describe the *Creditor* in greater detail.

**Postal Address** structure:

- Department
- Sub Department
- Street Name
- Building Number
- Building Name
- Floor
- Post Box
- Room
- Post Code
- Town Name
- Town Location Name
- District Name
- Country Sub Division
- Country → Code
- Address Line

| Node | Description |
|---|---|
| **BICFI** | The BIC which identifies the *Creditor* |
| **Clearing System Member Id** | Information used to identify a Debtor by a clearing system identifier. |
| **Creditor** | (central entity) |
| **LEI** | Legal entity identifier of the financial institution. |
| **Name** | *Name* by which the Agent is known |
| **Postal Address** | Nested element capturing either structured or unstructured *Creditor* address details |

---

<!-- Page 439 -->

The Financial Institution Direct Debit **Crededor Account** provides a optional element to identify the Creditor's Account for which the Direct Debit instruction intends to instruct the movement of money to.

`Min 0 – Max 1`

**Identification**

a unique *Identification* for the account, between the Account Servicer and Account Owner. The element is further nested by choice of *IBAN* or *Other* to capture the account.

`Min 1 – Max 1`

**Type**

An element which may either use an external ISO **Cash Account Type code** or a proprietary code. It is used to identifier a particular type of account.

**Currency**

The **Currency** for which the account is held. This is identified using the three characters **ISO currency code**.

**Name**

The Name of the Account, as Assigned by the servicing institution.

**Account**

A nested element which contains a Proxy Identifier together with the Proxy Type and a description. It is used to identify a **ISO 20022 Account Type**.

---

<!-- Page 440 -->

Min 1 – Max 1

The Financial Institution Direct Debit message **_Direct Debit Transaction Information_** nested element captures information related to the Debit part of the transaction, such as the Debtor, the amount and settlement date.

It is important to recognise that the data elements contained in this part of the Direct Debit message are identical the pacs.009 Financial Institution Credit Transfer message which represents the next stage of the journey should the Direct Debit be accepted.

_From a business perspective authorisation of a direct debit instruction can be predetermined in a couple of ways (as CBPR+ is not operating a Direct Debit scheme). Either **third party debt authority** could be granted to the Agent instructing of the Direct Debit, or the **Payment Identification** could be used to capture a static or incremental value (i.e. a mandate) to determine if the_

| Credit Instruction ▾ |
|---|
| Direct Debit Transaction Information ▸ |

---

<!-- Page 441 -->

Min 1 – Max 1

The pacs message **_Payment Identification_** provides a set of elements to identify the payment, of which several are mandatory elements

**_Payment Identification_**

**_Instruction Identification_**
Min 1 – Max 1

a **point-to-point reference** restricted in CBPR+ to 16 character and directly comparable with the Sender's Reference (Field 20) of the legacy MT payment message.

**_End to End Identification_**
Min 1 – Max 1

an **end-to-end reference** provided by the _Creditor_ which must be passed unchanged throughout the payment and reported back to the Creditor.

note: if the Creditor has not provide an end-to-end identifier, the _Creditor Agent_ may populate "NOTPROVIDED" to comply the mandatory need of this element.

**UETR**
Min 1 – Max 1

the **end-to-end Transaction** Reference created using the UUIDv4 standard. This reference must be passed unchanged throughout the payment, it may also be created by the Creditor within their Direct Debit Initiation request, and also included in reporting

---

<!-- Page 442 -->

(continued)

The pacs message *Payment Identification* `Min 1 – Max 1` also provides a set of optional elements to identify the direct debit transaction.

**Payment Identification**

- **Transaction Identification** `Min 0 – Max 1` — an **end-to-end reference** assigned by the first Instructing Agent to identify the transaction.

- **Clearing System Reference** `Min 0 – Max 1` — a **point-to-point reference** populated by a Payment Market Infrastructure, typically to the settlement leg of a clearing system transaction as a reference to the settled clearing transaction.

---

<!-- Page 443 -->

The Financial Institution Direct Debit message **Payment Type Information** provides a set of optional elements where the payment type can be described.

## Instruction Priority
Min 0 – Max 1

a choice of imbedded codes representing the urgency considered by the Instructing Agent, this point-to-point information may be used by the Instructed Agent to differentiate the processing priority.

## Service Level
Min 0 – Max 3

A nested element which may either use an external ISO Service Level code or a proprietary code. It is used to identify a particular agreed service level which should be applied to the payment.

## Payment Type Information

## Local Instrument
Min 0 – Max 1

A nested element which may either use an external ISO Local Instrument code or a proprietary code. It is used to identify the type of payment local instrument such as a Standing Order.

Note: the ISO instrument codes are registered by specific community group (captured in the code list)

## Category Purpose
Min 0 – Max 1

A nested element which may either use an external ISO

Credit Instruction
Direct Debit Transaction Information

---

<!-- Page 444 -->

The pacs.010 message (unlike the pacs.008) has one element to capture the amount of the Transfer, ***Interbank Settlement Amount***. `Min 1 – Max 1`

**Interbank Settlement Amount**

A mandated currency amount moved between the *Instructing Agent* and the *Instructed Agent*. This therefore is the point-to-point currency amount exchanged, comparable with the MT Field 32

🔭 Note: the Financial Institution Direct Debit (pacs.010) has no *Instructed Amount* element, *Exchange Rate* or *Charger Bearer*(like the pacs.009) as the Instructed Settlement Amount is expected to be transferred across the end-to-end payment chain without any charges being applied or currency conversions.

Credit Instruction ✓

---

<!-- Page 445 -->

Min 1 – Max 1

The Financial Institution Direct Debit message *Interbank Settlement Date* captures the *Date* the transaction is completed/effectted.

This *Date* element use ISODate YYYY-MM-DD

For example: 2002-10-10 (10 October 2002)

Credit Instruction

---

<!-- Page 446 -->

Min 0 – Max 1

The Financial Institution Direct Debit message *Settlement Time Request* captures the requested settlement time as a choice of nested elements.

Where *Settlement Time Request* is used the nested:
- **CLS Time** Min 0 – Max 1
- **Till Time** Min 0 – Max 1
- **From Time** Min 0 – Max 1
- **Reject Time** Min 0 – Max 1

may be used to capture information related to this time.

Credit Instruction

---

<!-- Page 447 -->

The ISO 20222 pacs messages describe the Agent whose account is debited for a transaction as the *Debtor*. The *Debtor* sub elements describe the *Debtor* in greater detail.

## Postal Address

- Department
- Sub Department
- Street Name
- Building Number
- Building Name
- Floor
- Post Box
- Room
- Post Code
- Town Name
- Town Location Name
- District Name
- Country Sub Division
- Country
  - Code

## Debtor

**BICFI**
The BIC which identifies the Debtor

**Clearing System Member Id**
Information used to identify a Debtor by a clearing system identifier.

**LEI**
Legal entity identifier of the financial institution.

**Name**
*Name* by which the Agent is known

**Postal Address**
Nested element capturing either structured or unstructured Debtor address details

---

<!-- Page 448 -->

The Financial Institution Direct Debit message **Debit Account** `Min 0 - Max 1` also provides an number of optional nested element to identify the account for which debit and credit entries have been made.

**Identification** `Min 1 - Max 1` (∞)
a unique *Identification* for the account, between the Account Servicer and Account Owner. The element is further nested by choice of *IBAN* or *Other* to capture the account.

**Type** (∞)
An element which may either use an external ISO *Cash Account Type code* or a proprietary code. It is used to identify a particular type of account.

**Currency**
The *Currency* for which the account is held. This is identified using the three characters *ISO currency code*.

**Name** (→)
The Name of the Account, as Assigned by the servicing institution.

**Account** (→)

A nested element which contains a Proxy Identifier together with the Proxy

---

<!-- Page 449 -->

Min 0 – Max 1
The *Debtor Agent* is a static role in the pacs messages. This agent maintain a relationship with their customer, the *Debtor*. Like the pacs.009 the Debtor Agent is optional, which cover the scenario where the Debtor and Creditor (as Financial Institutions) maintain a direct Nostro/Vostro account relationship, or where the Debtor Agent maintain the account of both the Debtor and Creditor.

Min 0 – Max 1
Where the *Debtor Agent* is utilised the *Debtor Agent Account* may optionally be used to capture the account of the Debtor Agent with the Agent immediate after them in the transaction chain (the Agent Serving their account)
This would only apply where the message includes a *Debtor Agent*, however CBP+plus does not recommend to use this element unless mandated within a community or bilaterally agreed.

Credit Instruction
Debtor Agent

---

<!-- Page 450 -->

The *Instruction for Debtor Agent* elements within the pacs.010 Financial Institution Direct Debit optionally provides information related to the processing of the direct debit instruction.

Min 0 – Max 1

The *Instruction for Debtor Agent* element offers a occurrence of free format information.

The use of this element should be **bilaterally** agreed with the *Debtor Agent* to maximize the ability to Straight Through Process the instruction.

Credit Instruction

---

<!-- Page 451 -->

| Min0 – Max1 |
| :--- |
| **Purpose** |

The **Purpose** elements within the `pacs.010` Financial Institution Direct Debit capture the reason for the payment transaction which would result from a successful direct debit. This element may either use an external ISO **Purpose code** or a proprietary code.
The purpose is used by the capture the nature of the payment e.g. **CORT** Trade Settlement Payment, **CFEE** Cancellation Fees etc. and should not be confused with Regulatory Reporting codes.

The externalised Purpose code set is classified by the purpose, for example commercial, for which the numerous codes within the classification are each described by Name and Definition.
For example:
**OTCD** is classified within the Collateral categorisation, with the *Name* **OTC Derivatives** described as a **Cash collateral related to over-the-counter (OTC) Derivatives - in general for example contracts which are traded and privately negotiated.**

Credit Instruction

---

<!-- Page 452 -->

The optional *Remittance Information* element within the pacs.010 Financial Institution Direct Debit is nested to provide *Unstructured* information related to payment.

> **Min 0 – Max 1**
> *Remittance Information* enable the matching/reconciliation of an entry that the payment is intended to settle
>
> > **Min 0 – Max 1**
> > The *Unstructured* sub element captures free format *Remittance Information* which is restricted in CBPR+ to 140 characters to ensure backward compatibility with the legacy MT message during coexistence.

Note: like the pacs.009 *Remittance Information* can only be captured in an *Unstructured* element.
*Remittance Information* is however a dedicated element used both within the pacs and camt reporting messages, whereby this information can travel end-to-end using ISO 20022

---

<!-- Page 453 -->

Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases.

**Financial Institution Direct Debt**

Use Case p.10.1.1 - High Level Payment of a Financial Institution Direct Debt (pacs.010)

Use Case p.10.1.1.a - High Level Book movement of a Financial Institution Direct Debt (pacs.010)

Use Case p.10.1.2 - High Level Rejection of a Financial Institution Direct Debt (pacs.010)

---

<!-- Page 454 -->

pacs.010
1
pacs.002
A
camt.053
2a
B
pacs.009
2
C
pacs.009
3
D
camt.053
4
E

**1** Agent E initiates a Direct Debit instruction to debit Agent A's account

**2** Debtor Agent (B) initiates a serial payment towards the Creditor Agent (E) using Agents B & C as intermediaries

**2a** Debtor Agent (B) debits the Debtor (Agent A) optionally provide a notification e.g. credit notification in addition to an account statement (camt.053)

**3** Agent C processes the payment on Agent D

**4** Agent D credits the account of the Creditor (Agent E), and may optionally provide a notification e.g. credit notification in addition to an account statement (camt.053)

---

<!-- Page 455 -->

| 1 | 2a | 2b |
|---|---|---|
| Agent E initiates a Direct Debit instruction to debit Agent A's account | Debtor Agent (B) debits the Debtor (Agent A) optionally provide a notification e.g. credit notification in addition to an account statement (camt.053) | Agent B credits the account of the Creditor (Agent C), and may optionally provide a notification e.g. credit notification in addition to an account statement (camt.053) |

**Sequence diagram messages:**

- **1** → `pacs.010` (C → B)
- `pacs.002` (B → C)
- `camt.053` (B → C)
- `camt.053` (B → A)

**Participants:** A, B, C

---

<!-- Page 456 -->

pacs.010

pacs.002

A

B

C

D

E

1

Agent D initiates a Direct Debit instruction to debit Agent A's account

!

Debtor Agent (B) rejects the instruction, using a pacs.002, as no mandate agreement is in place.

---

<!-- Page 457 -->

# Financial Institution Direct Debit – Margin Collection

---

<!-- Page 458 -->

```
pacs.010
├── Group Header
└── Credit Instruction
```

The pacs.010 has two core sets of nested elements:

- **Group Header** which contains a set of characteristics that relates to the transaction
- **Credit Instruction** which contains elements providing information specific to direct debit transaction information and credit instruction.

🔍 The Financial Institution Direct Debit Margin Collection is designed to allow a Central Counterpart to collect money by triggering a payment. Whereby the pacs.010 Debit transfer the money to the Creditor using a pacs.009. Unlike the pacs.010 Financial Institution Direct Debit additional Credit Instruction elements are allowed in this Usage Guideline.
The Financial Institution Direct Debit Margin Collection can be used for

---

<!-- Page 459 -->

# A B C D

| Message | From | To |
| :--- | :--- | :--- |
| secl.010 | D | A |
| pacs.010 | D | B |
| pacs.002 | B | D |
| pacs.009 | B | C |
| camt.053 | C | D |

The Financial Institution Direct Debit message (pacs.010) is sent by a Financial Institution, directly or through another agent, to the Debtor Agent. It is used to instruct the Debtor Agent to move funds from the Debtor's account to the Creditor, where both Debtor and Creditor are financial institutions.

---

<!-- Page 460 -->

# Group Header

---

<!-- Page 461 -->

Min 1 – Max 1

Each ISO 20022 payment message has a **Message Identification** element, located in the Group Header. This **35 character** identifier is a point-to-point reference used to unambiguously identify the message.

For Payment Clearing and Settlement (pacs) messages the Message Identification has no exact equivalent in the legacy MT payment message. However, the Sender's Reference (Field 20) could be considered a similar comparison where a pacs message contains a single Transaction.

Group Header > Message Identification

---

<!-- Page 462 -->

Min 1 – Max 1

The pacs.010 message *Creation Date Time* captures the date and time which the message was created.

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
> For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- Page 463 -->

Min 1 – Max 1

The pacs.0010 message ***Number of Transactions*** captures the number of individual transaction contained within the message.

🧮 The number of transactions in CBPR+ payment usage guidelines is fixed to 1.

💡 Single transactions in the CBPR+ payment usage guidelines enable a transaction to be managed and unlocks highly automated, frictionless, instant payments, supporting the next generation of innovation.

---

<!-- Page 464 -->

# Credit Instruction

---

<!-- Page 465 -->

Min 1 – Max 1

The Financial Institution Direct Debit **Credit Identification** provides a mandatory element to identify the Direct Debit instruction.

Unique reference assigned by the account servicer to unambiguously identify the account report. Directly comparable with the *Transaction Reference Number* (Field 20) of the legacy MT Financial Markets Direct Debit message.

---

<!-- Page 466 -->

Min 0 – Max 1

The pacs message ***Payment Type Information*** provides a set of optional elements where the payment type can be described. These elements are applied to the pacs.009 which results from this message.

**Payment Type Information**

**Instruction Priority**
Min 0 – Max 1

a choice of imbedded codes representing the urgency considered by the Instructing Agent, this point-to-point information may be used by the Instructed Agent to differentiate the processing priority.

**Category Purpose**
Min 0 – Max 1

A nested element which may either use an external ISO Category Purpose code or a proprietary code. It is used to identify the category of payment. For example, SECU Transaction is the payment of securities.

---

<!-- Page 467 -->

# Agents

Instructed
Agent: Agent B

Instructing
Agent: Agent D

pacs.010

pacs.009

pacs.009

***Instructing Agent*** and ***Instructed Agent*** represent the Agents involved in the pacs point-to-point message exchange. These roles therefore change on each message leg.

*Instructing Agent* and *Instructed Agent* elements are required in all pacs messages and is only available in the **Credit Instruction**.

Credit Instruction
Instructing Agent

---

<!-- Page 468 -->

The pacs message can capture up to 3 Intermediary Agents, which play a dynamic role in the payment between the Debtor Agent and Creditor Agent.

Min 0 – Max 1
The **Intermediary Agent 1** captures the first Intermediary Agent between the Debtor Agent and Creditor Agent for who the Instructed Agent attempt to instruct the payment on to. This optional element is comparable with the Field 56a in the legacy FIN message.

Min 0 – Max 1
The **Intermediary Agent 1 Account** captured the account related to this Intermediary Agent, with the Instructed Agent. This element can be compared to the Party Identifier of the legacy Field 56a.

Min 0 – Max 1
The **Intermediary Agent 2** captures the second Intermediary Agent between the Intermediary Agent 1 and the Creditor Agent. This optional element has not comparable field in the legacy FIN message.

Min 0 – Max 1
The **Intermediary Agent 2 Account** captured the account related to this Intermediary Agent, with the Intermediary Agent 1. This optional element has not comparable field in the legacy FIN message.

Min 0 – Max 1
The **Intermediary Agent 3** captures the third Intermediary Agent between the Intermediary Agent 2 and the Creditor Agent. This optional element has not comparable field in the legacy FIN message.

Min 0 – Max 1
The **Intermediary Agent 3 Account** captured the account related to this Intermediary Agent, with the

---

<!-- Page 469 -->

## Agent Account

`Min 0 – Max 1`

The **_Creditor Agent_** is a static role in the pacs messages. This agent maintain a relationship with their customer, the **_Creditor_**. Like the pacs.009 the Creditor Agent is optional, which cover the scenario where the Debtor and Creditor (as Financial Institutions) maintain a direct Nostro/Vostro account relationship, or where the Debtor Agent maintain the account of both the Debtor and Creditor.

`Min 0 – Max 1`

Where the **_Creditor Agent_** is utilised the **_Creditor Agent Account_** may optionally be used to capture the account of the Creditor Agent with the Agent immediate before them in the transaction chain (the Agent Serving their account)
This would only apply where the message includes a *Creditor Agent*, however CBPRplus does not recommend to use this element unless mandated within a community or bilaterally agreed.

Credit Instruction
Creditor Agent

---

<!-- Page 470 -->

The ISO 20022 pacs messages describe the Agent whose account is credited for a transaction as the *Creditor*. The *Creditor* sub elements describe the *Creditor* in greater detail.

**Postal Address** structure:

- Department
- Sub Department
- Street Name
- Building Number
- Building Name
- Floor
- Post Box
- Room
- Post Code
- Town Name
- Town Location Name
- District Name
- Country Sub Division
- Country → Code
- Address Line

| Node | Description |
|---|---|
| **BICFI** | The BIC which identifies the *Creditor* |
| **Clearing System Member Id** | Information used to identify a Debtor by a clearing system identifier. |
| **Creditor** | (central entity) |
| **LEI** | Legal entity identifier of the financial institution. |
| **Name** | *Name* by which the Agent is known |
| **Postal Address** | Nested element capturing either structured or unstructured *Creditor* address details |

---

<!-- Page 471 -->

The Financial Institution Direct Debt **Creditor Account** `Min 0 – Max 1` provides an optional element to identify the Creditor's Account for which the Direct Debit instruction intends to instruct the movement of money to.

**Identification** `Min 1 – Max 1`
a unique *Identification* for the account, between the Account Servicer and Account Owner. The element is further nested by choice of *IBAN* or *Other* to capture the account.

**Type**
An element which may either use an external ISO *Cash Account Type code* or a proprietary code. It is used to identifier a particular type of account.

**Currency**
The *Currency* for which the account is held. This is identified using the three characters *ISO currency code*.

**Name**
The Name of the Account, as Assigned by the servicing institution.

A nested element which contains a Proxy Identifier together with the Proxy

---

<!-- Page 472 -->

## Information

Min 1 – Max 1

The Financial Institution Direct Debit message **_Direct Debit Transaction Information_** nested element captures information related to the Debit part of the transaction, such as the Debtor, the amount and settlement date.

It is important to recognise that the data elements contained in this part of the Direct Debit message are identical the pacs.009 Financial Institution Credit Transfer message which represents the next stage of the journey should the Direct Debit be accepted.

_From a business perspective authorisation of a direct debit instruction can be predetermined in a couple of ways (as CBPR+ is not operating a Direct Debit scheme). Either **third party debt authority** could be granted to the Agent instructing of the Direct Debit, or the **Payment Identification** could be used to capture a static or incremental value (i.e. a mandate) to determine if the_

Credit Instruction ▼
Direct Debit Transaction Information >

---

<!-- Page 473 -->

Min 1 – Max 1

The pacs message **_Payment Identification_** provides a set of elements to identify the payment, of which several are mandatory elements

**_Payment Identification_**

**_Instruction Identification_**
Min 1 – Max 1

a **point-to-point reference** restricted in CBPR+ to 16 character and directly comparable with the Sender's Reference (Field 20) of the legacy MT payment message.

**_End to End Identification_**
Min 1 – Max 1

an **end-to-end reference** provided by the _Creditor_ which must be passed unchanged throughout the payment and reported back to the Creditor.

note: if the Creditor has not provide an end-to-end identifier, the _Creditor Agent_ may populate "NOTPROVIDED" to comply the mandatory need of this element.

**UETR**
Min 1 – Max 1

the **end-to-end Transaction** Reference created using the UUIDv4 standard. This reference must be passed unchanged throughout the payment, it may also be created by the Creditor within their Direct Debit Initiation request, and also included in reporting

---

<!-- Page 474 -->

(continued)

The pacs message *Payment Identification* `Min 1 – Max 1` also provides a set of optional elements to identify the direct debit transaction.

**Payment Identification**

- **Transaction Identification** `Min 0 – Max 1` — an **end-to-end reference** assigned by the first Instructing Agent to identify the transaction.

- **Clearing System Reference** `Min 0 – Max 1` — a **point-to-point reference** populated by a Payment Market Infrastructure, typically to the settlement leg of a clearing system transaction as a reference to the settled clearing transaction.

---

<!-- Page 475 -->

The Financial Institution Direct Debit message **Payment Type Information** provides a set of optional elements where the payment type can be described. These elements apply to the debit transaction, whereby the Credit Instruction has it own Payment Type Information.

a choice of imbedded codes representing the urgency considered by the Instructing Agent, this point-to-point information may be used by the Instructed Agent to differentiate the processing priority.

**Instruction Priority**
Min 0 – Max 1

**Payment Type Information**

**Service Level**
Min 0 – Max 3

A nested element which may either use an external ISO Service Level code or a proprietary code. It is used to identify a particular agreed service level which should be applied to the payment.

**Local Instrument**
Min 0 – Max 1

A nested element which may either use an external ISO Local Instrument code or a proprietary code. It is used to identify the type of payment local instrument such as a Standing Order.

Note: the ISO instrument codes are registered by specific community group (captured in the code list)

**Category Purpose**
Min 0 – Max 1

A nested element which may either use an external ISO

Credit Instruction
Direct Debit Transaction Information

---

<!-- Page 476 -->

The pac.010 message (unlike the pac.008) has one element to capture the amount of the Transfer, *Interbank Settlement Amount*.

`Min 1 – Max 1`

**Interbank Settlement Amount**

A mandated *currency amount* moved between the *Instructing Agent* and the *Instructed Agent*. This therefore is the point-to-point currency amount exchanged, comparable with the MT Field 32

Note: the Financial Institution Direct Debit (pac.010) has *no Instructed Amount* element, *Exchange Rate* or *Charger Bearer*(like the pac.009) as the Instructed Settlement Amount is expected to be transferred across the end-to-end payment chain without any charges being applied or currency conversions.

Credit Instruction

---

<!-- Page 477 -->

Min 1 – Max 1

The Financial Institution Direct Debit message *Interbank Settlement Date* captures the *Date* the transaction is completed/effectted.

This *Date* element use ISODate YYYY-MM-DD

For example: 2002-10-10 (10 October 2002)

Credit Instruction

---

<!-- Page 478 -->

Min 0 – Max 1

The Financial Institution Direct Debit message *Settlement Time Request* captures the requested settlement time as a choice of nested elements.

Where *Settlement Time Request* is used the nested:
- **CLS Time** Min 0 – Max 1
- **Till Time** Min 0 – Max 1
- **From Time** Min 0 – Max 1
- **Reject Time** Min 0 – Max 1

may be used to capture information related to this time.

Credit Instruction

---

<!-- Page 479 -->

The ISO 20222 pacs messages describe the Agent whose account is debited for a transaction as the *Debtor*. The *Debtor* sub elements describe the *Debtor* in greater detail.

## Postal Address

- Department
- Sub Department
- Street Name
- Building Number
- Building Name
- Floor
- Post Box
- Room
- Post Code
- Town Name
- Town Location Name
- District Name
- Country Sub Division
- Country
  - Code

## Debtor

**BICFI**
The BIC which identifies the Debtor

**Clearing System Member Id**
Information used to identify a Debtor by a clearing system identifier.

**LEI**
Legal entity identifier of the financial institution.

**Name**
*Name* by which the Agent is known

**Postal Address**
Nested element capturing either structured or unstructured Debtor address details

---

<!-- Page 480 -->

The Financial Institution Direct Debit message **Debit Account** `Min 0 - Max 1` also provides an number of optional nested element to identify the account for which debit and credit entries have been made.

**Identification** `Min 1 - Max 1`
a unique **Identification** for the account, between the Account Servicer and Account Owner. The element is further nested by choice of *IBAN* or *Other* to capture the account.

**Type**
An element which may either use an external ISO **Cash Account Type code** or a proprietary code. It is used to identify a particular type of account.

**Currency**
The **Currency** for which the account is held. This is identified using the three characters **ISO currency code**.

**Name**
The Name of the Account, as Assigned by the servicing institution.

**Account**

A nested element which contains a Proxy Identifier together with the Proxy

---

<!-- Page 481 -->

## Agent Account

Min 0 – Max 1

The ***Debtor Agent*** is a static role in the pacs messages. This agent maintain a relationship with their customer, the ***Debtor***. Like the pacs.009 the Debtor Agent is optional, which cover the scenario where the Debtor and Creditor (as Financial Institutions) maintain a direct Nostro/Vostro account relationship, or where the Debtor Agent maintain the account of both the Debtor and Creditor.

Min 0 – Max 1

Where the ***Debtor Agent*** is utilised the ***Debtor Agent Account*** may optionally be used to capture the account of the Debtor Agent with the Agent immediate after them in the transaction chain (the Agent Serving their account)

This would only apply where the message includes a *Debtor Agent*, however CBP+plus does not recommend to use this element unless mandated within a community or bilaterally agreed.

Credit Instruction

Debtor Agent

---

<!-- Page 482 -->

The *Instruction for Debtor Agent* elements within the pacs.010 Financial Institution Direct Debit optionally provides information related to the processing of the direct debit instruction.

**Min 0 – Max 1**

The *Instruction for Debtor Agent* element offers a occurrence of free format information.

The use of this element should be **bilaterally** agreed with the *Debtor Agent* to maximize the ability to Straight Through Process the instruction.

Credit Instruction

---

<!-- Page 483 -->

| Min0 – Max1 |
| :--- |
| **Purpose** |

The **Purpose** elements within the `pacs.010` Financial Institution Direct Debit capture the reason for the payment transaction which would result from a successful direct debit. This element may either use an external ISO **Purpose code** or a proprietary code.
The purpose is used by the capture the nature of the payment e.g. `CCPC` CCP Cleared Initial Margin and should not be confused with Regulatory Reporting codes.

The externalised Purpose code set is classified by the purpose, for example commercial, for which the numerous codes within the classification are each described by Name and Definition.
For example:
OTCD is classified within the Collateral categorisation, with the *Name* **OTC Derivatives** described as a **Cash collateral related to over-the-counter (OTC) Derivatives - in general for example contracts which are traded and privately negotiated.**

Credit Instruction

---

<!-- Page 484 -->

The optional *Remittance Information* element within the pacs.010 Financial Institution Direct Debit is nested to provide *Unstructured* information related to payment.

> **Min 0 – Max 1**
> *Remittance Information* enable the matching/reconciliation of an entry that the payment is intended to settle
>
> > **Min 0 – Max 1**
> > The *Unstructured* sub element captures free format *Remittance Information* which is restricted in CBPR+ to 140 characters to ensure backward compatibility with the legacy MT message during coexistence.

Note: like the pacs.009 *Remittance Information* can only be captured in an *Unstructured* element.
*Remittance Information* is however a dedicated element used both within the pacs and camt reporting messages, whereby this information can travel end-to-end using ISO 20022

Credit Instruction / Remittance Information

---

<!-- Page 485 -->

> Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases.

**Financial Institution Direct Debit**
Use Case p.10.2.1 - High Level Payment Of A Financial Institution Direct Debit (pacs.010)
Use Case p.10.2.2 - High Level Rejection Of A Financial Institution Direct Debit (pacs.010)

---

<!-- Page 486 -->

# (pacs.010)

**Diagram Flow:**

- Agent **A**
- Agent **B** (Step 2)
- Agent **C** (Step 3)
- Agent **D** (Step 4)
- Agent **E** (Step 1)

**Message Flow:**

- **pacs.010**: E → B (blue arrow, top)
- **pacs.002**: B → E (dashed arrow)
- **pacs.009**: B → C
- **pacs.009**: C → D
- **camt.053**: D → E

**Step Descriptions:**

1. Agent E initiates a Direct Debit instruction to debit Agent A's account

2. Debtor Agent (B) initiates a serial payment towards the Creditor Agent (E) using Agents B & C as intermediaries

3. Agent C processes the payment on Agent D

4. Agent D credits the account of the Creditor (Agent E), and may optionally provide a notification e.g. credit notification in addition to an account statement (camt.053)

---

<!-- Page 487 -->

(pacs.010)

![Diagram](diagram)

Agents: A, B, C, D, E

- Arrow E → B: `pacs.010` (1)
- Arrow B → E: `pacs.002`
- Marker near B: !

**1**
Agent D initiates a Direct Debit instruction to debit Agent A's account

**!**
Debtor Agent (B) rejects the instruction, using a pacs.002, as no mandate agreement is in place.

---

<!-- Page 488 -->

# Financial Institution to
# Financial Institution
# Customer Direct Debit

---

<!-- Page 489 -->

pacs.003

- Group Header
- Direct Debit Transaction Information

The pacs.003 has two core sets of nested elements:

- ***Group Header*** which contains a set of characteristics that relates to all individual transaction
- ***Direct Debit Transaction Information*** which contains elements providing information specific to the individual direct debit transaction.

🔭 Payment messages in a many-to-many payment are considered as a single transaction.

---

<!-- Page 490 -->

Debtor
Debtor Agent
Creditor Agent
Initiating Party
Creditor

pain.008**
pain.002
pacs.003
pacs.002
camt.053

*Initiating Party may alternative represent an authorised party such as a head office
**or other proprietary method for instructing a direct debit initiation request.

The Financial Institution To Financial Institution Customer Direct Debit message is sent by the Creditor Agent to the Debtor Agent, directly or through other agents and/or a payment clearing and settlement system.
It is used to collect funds from a Debtor account for a Creditor, whereby one or both of these Parties are non-Financial Institutions.

---

<!-- Page 491 -->

# Group Header

---

<!-- Page 492 -->

Min 1 – Max 1

Each ISO 20022 payment message has a **Message Identification** element, located in the Group Header. This `35 character` identifier is a point-to-point reference used to unambiguously identify the message.

For Payment Clearing and Settlement (pacs) messages the Message Identification has no exact equivalent in the legacy MT payment message. However, the Sender's Reference (Field 20) could be considered a similar comparison where a pacs message contains a single Transaction.

Each transaction's *Direct Debit Transaction Information* contains a variety of nested *Payment Identification* elements to capture reference related to the individual transaction such as a UETR (Unique End-to-end Transaction Reference)

---

<!-- Page 493 -->

Min 1 – Max 1

The pacs.003 message *Creation Date* captures the date and time which the message was created.

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
> For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- Page 494 -->

Min 1 – Max 1

The pacs.003 message **Number of Transactions** captures the number of individual transaction contained within the message.

The number of transactions in CBPR+ payment usage guidelines is fixed to 1.

Single transactions in the CBPR+ payment usage guidelines enable a transaction to be managed and unlocks highly automated, frictionless, instant payments, supporting the next generation of innovation.

---

<!-- Page 495 -->

Min 1 – Max 1

The pacs.003 **Settlement Method** element within the Group Header **Settlement Information**, includes one of the embedded codes to indicate how the payment message will be settled.

The *Settlement Method element* in the pacs.003 allows a choice of an embedded code.

**INDA** indicate this Customer Direct Debit will be settled by the Instructed Agent (as the Account Servicing Institution) The account held at the Instructed Agent may captured in the dedicated **Settlement Account** element.

**INGA** indicate this Customer Direct Debit has already been settled by the Instructing Agent, who has credited the Account they service for the Instructed Agent (as an Account Owner). The account held by the Instructed Agent with the Instructing Agent may captured in the dedicated **Settlement Account** element.

Settlement Method code CLRG is not part of CBPR+ specifications but instead used in Market Infrastructure specification

---

<!-- Page 496 -->

The pacs.003 message *Settlement Account* is a nested element as part of *Settlement Information*, this element identifies information related to an account used to settle the direct debit instruction.

**Min 0 – Max 1**
The *Settlement Account* identifies the account details maintained at the account servicing institution (Agent responsible for the settlement of the instruction as indicated in the *Settlement Method*)

**Min 1 – Max 1** *Identification* identifies the account maintained at the Debtor Agent (Account Servicing Institution)

**Min 0 – Max 1** *Type* uses the external Cash Account Type code list to identify the type of account

**Min 0 – Max 1** *Currency* identifies the currency if the account

**Min 0 – Max 1** *Name* identifies the name of the account as assigned by the Account Servicing Institution

**Min 0 – Max 1** *Proxy* captures an alternative identification of the account number such as an email address. This element has further nested *Type* which is a choice of external code list or proprietary code and *Identification* which are both mandatory where the Proxy element is used.

---

<!-- Page 497 -->

# Direct Debit Transaction Information

---

<!-- Page 498 -->

The pacs message **_Payment Identification_** `Min 1 – Max 1` provides a set of elements to identify the payment, of which several are mandatory elements

## Payment Identification

**Instruction Identification** `Min 1 – Max 1`
a `point-to-point reference` restricted in CBPR+ to 16 character and directly comparable with the Sender's Reference (Field 20) of the legacy MT payment message.

**End to End Identification** `Min1 – Max 1`
an `end-to-end reference` provided by the _Creditor_ which must be passed unchanged throughout the payment and reported back to the Creditor.

note: if the Creditor has not provide an end-to-end identifier, the _Creditor Agent_ may populate `"NOTPROVIDED"` to comply the mandatory need of this element.

**UETR** `Min 0 – Max 1`
the `end-to-end Transaction` Reference created using the UUIDv4 standard. This reference must be passed unchanged throughout the payment, it may also be created by the Creditor within their Direct Debit Initiation request, and also included in reporting

---

<!-- Page 499 -->

The pacs message *Payment Identification* also provides a set of optional elements to identify the direct debit transaction.

**Payment Identification**

*   **Transaction Identification** (Min 0 – Max 1)
    an *end-to-end reference* assigned by the first Instructing Agent to identify the transaction.

*   **Clearing System Reference** (Min 0 – Max 1)
    a *point-to-point reference* populated by a Payment Market Infrastructure, typically to the settlement leg of a clearing system transaction as a reference to the settled clearing transaction.

---

<!-- Page 500 -->

The pacs message **Payment Type Information** provides a set of optional elements where the payment type can be described.

## Payment Type Information

**Service Level**
Min 0 – Max 3

A nested element which may either use an external ISO Service Level code* or a proprietary code. It is used to identify a particular agreed service level which should be applied to the payment.

**Instruction Priority**
Min 0 – Max 1

a choice of imbedded codes representing the urgency considered by the Instructing Agent, this point-to-point information may be used by the Instructed Agent to differentiate the processing priority.

**Local Instrument**
Min 0 – Max 1

A nested element which may either use an external ISO Local Instrument code or a proprietary code. It is used to identify the type of payment local instrument such as a Standing Order.

Note: the ISO instrument codes are registered by specific community group (captured in the code list)

**Clearing Channel**
Min 0 – Max 1

a choice of imbedded codes representing the clearing channel to be used to process direct debits.

**Category**

A nested element which may either use an external ISO Category Purpose code or a proprietary code. It is used to identify the

---

<!-- Page 501 -->

The pacs.003 message has two key element to capture the amount of the Credit Transfer, ***Interbank Settlement Amount*** and ***Interbank Settlement Date***.

**Interbank Settlement Amount**

A mandated currency amount moved between the *Instructing Agent* and the *Instructed Agent*. This therefore is the point-to-point currency amount exchanged, comparable with the MT Field 32B

**Interbank Settlement Date**

A mandated date on which the *Interbank Settlement* should be executed between the *Instructing Agent* and the *Instructed Agent*. This therefore is the value date comparable with the MT Field 30

Note: the relationship between Interbank Settlement Amount and Instructed Amount is an important one. Instructed Amount relates to the amount Instructed to be debited from the Debtor's account and only need to be captured in the Instructed Amount where the Interbank Settlement Amount is not the same currency amount

---

<!-- Page 502 -->

The pacs.003 message has two optional elements to capture the information related to the settlement of the instructions.

**Min 0 – Max 1**

The **Settlement Priority** provides an optional choice of embedded codes to indicate the instruction's settlement priority from the perspective of the Instructing Agent. This point-to-point information may be used by the Instructed Agent to identify the priority associated with the **Settlement Method** and should not be confused with the *Instruction Priority*.

Note: where **Settlement Priority** of the pacs.003 is 'URGT' (Urgent) means the highest priority possible to process the direct debit settlement and the amount of money becomes available to the Creditor Agent.

**Min 0 – Max 1**

The **Settlement Time Indication** optionally captures the time settlement occurred at a transaction administrator such as a Market Infrastructure.
This DateTime can be captured in two nested elements, **Debit Date Time** and **Credit Date Time**.

---

<!-- Page 503 -->

**Min 0 – Max 1**

The **_Instructed Amount_** captures currency and amount instructed by the Creditor. This conditional element is required when the **_Interbank Settlement Amount_** is not the same currency and/or amount as originally instructed by the _Creditor_. For example, a charge is taken, or the transactions is converted to another currency. This element is comparable with the legacy Field 33B.

**Min 0 – Max 1**

The **_Exchange Rate_** captures the factor (rate) used to convert an amount from one currency into another. This reflects the currency pair price at which one currency was bought with another currency.

Note: a number of Cross Element Rules exist which relate to the _Instructed Amount_ element. For example, if the _Instructed Amount_ is present and the

---

<!-- Page 504 -->

Min 1 – Max 1

The mandated *Charge Bearer* element uses an embedded code that is used to specify which party/parties would bear any charges associated with processing the payment transaction. This element is comparable with MT Field 71A 'Details of Charges'

| **Charge Bearer (1.1)** | **Code** | **Description** | ISO 20022 |
|---|---|---|---|
| | CRED | Creditor | |
| | DEBT | Debtor | |
| | SHAR | Shared | |
| | SLEV | Service Level | |

| **71A: Details of Charges** | **Code** | **Description** | MT 104 |
|---|---|---|---|
| | BEN | Beneficiary | |
| | OUR | Our Customer Charges | |
| | SHA | Shared Charges | |

Note: SLEV is removed from CBPR+ usage guideline specifications.

---

<!-- Page 505 -->

Min 0 – Max *    Min 1 – Max 1

The **Charges Information** element provides information on the charges to be paid by the **Charge Bearer**. This element is comparable with MT Fields: 71F 'Senders Charges' and 71G 'Receiver's Charges'

| Charge Information (0..*) | Amount | |
|---|---|---|
| | Currency | |
| | Agent | BICF |
| | | Name |
| | | Structured Postal Address |

In addition to the legacy MT message the pacs.003 *Charge Information* mandate the *Agent*, this represent the Agent for who the Charges are either; due (pre-paid charges) or has taken a charge (deduct from the transaction)

CBPR+ best practice recommends the use of the structured Agent BIC.

As the **Charges Information** element is repetitive it can capture charges related to previous legs of the payment transaction.

Note: As the *Charge Information* element has the capability to capture both charges deducted and charges included i.e. pre-paid charges, the use of the *Interbank Settlement Amount* and *Instructed Amount* elements play an important role.

---

<!-- Page 506 -->

# pacs.003 Pro II Customer Direct Debit – Requested Collection Date

Min 1 – Max 1

The pacs.003 message mandatory **Requested Collection Date** element, captures the date on which the creditor requests that the amount of money is to be collected from the debtor.

It is defined by *ISO Date* expressed in the *YYYY-MM-DD format*.

Direct Debit Transaction Information

---

<!-- Page 507 -->

The `pac.003` **Direct Debit Transaction** component provides information specific to the direct debit mandate.

**Mandate Related Information**
Min 0 – Max 1
Provides further details of the direct debit mandate signed between the creditor and the debtor. E.g., Mandate Identification, Date of Signature and Electronic Signature.

**Creditor Scheme Identification**
Min 0 – Max 1
Credit party that signs the mandate, may be used if supported by the Direct Debit Scheme. (see next page for additional detail on this nested element)

**Pre Notification Identification**
Min 0 – Max 1
Unique and unambiguous identification of the pre-notification which is sent separately from the direct debit instruction.

**Pre Notification Date**
Date on which the creditor notifies the debtor about the amount and date on

Direct Debit Transaction Information

---

<!-- Page 508 -->

Min 0 – Max 1
The **Creditor Scheme Identification** element within the pacs.003 message optionally provides information related to the credit party that signs the mandate who is different from the Creditor.

The **Creditor Scheme Identification** element offers the following options:

Name
Postal Address: Not used often
Identification
Country of Residence
Contact Details

CGI-MP: recommends the use of Creditor Scheme Identification only if supported by the Direct Debit Scheme.

Direct Debit Transaction Information

---

<!-- Page 509 -->

The ISO 20022 pacs messages describe the party credited for a transaction as the **Creditor**. The **Creditor** sub elements describe the **Creditor** in greater detail. Min 1 – Max 1

| Tree Structure | Description |
| :--- | :--- |
| Department | |
| Sub Department | |
| Street Name | |
| Building Number | |
| Building Name | |
| Floor | |
| Post Box | |
| Room | |
| Post Code | |
| Town Name | |
| Town Location Name | |
| District Name | |
| Country Sub Division | |
| Country | Code |
| Postal Address | Nested element capturing either structured or unstructured *Creditor* address details |
| | Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc. |

Mandatory *Name*, where a BIC identifier is not provided, by which the party is known

**Name**

**Postal Address**

# Creditor

**Identification**

Optional element to capture the Creditor's ISO country code of residence

**Country of Residence**

---

<!-- Page 510 -->

The pacs.003 **_Creditor Account_** is used to capture the account information for which a credit entry is intended to be applied to the Creditor's account, which are also reflected in their account Statement.

The **_Creditor Account_** uses a variety of nested elements to capture information related to the account.

Min 1 – Max 1 **_Identification_** identifies the account maintained at the Creditor Agent (Account Servicing Institution)

Min 0 – Max 1 **_Type_** uses the external Cash Account Type code list to identify the type of account

Min 0 – Max 1 **_Currency_** identifies the currency if the account

Min 0 – Max 1 **_Name_** identifies the name of the account as assigned by the Creditor Agent (Account Servicing Institution)

Min 0 – Max 1 **_Proxy_** captures an alternative identification of the account number such as an email address. This element has further nested **_Type_** which is a choice of external code list or proprietary code and **_Identification_** which are both mandatory where the Proxy element is used.

---

<!-- Page 511 -->

Min 1 – Max 1 Min 1 – Max 1
The **_Debtor Agent_** and **_Creditor Agent_** are static roles in the pacs.003 FI to FI Customer Direct Debit. These agent maintain a relationship with their customers; the _Debtor_ and _Creditor_.

Note: Although the **_Debtor Agent, Creditor Agent, Debtor and Creditor_** all maintain static roles in the pacs messages, the description of these parties change in the reporting messages (camt) where the Debtor Agent and Creditor Agent become the Statement Account Servicer and the Debtor and Creditor become the Statement Account Owner. This will be explored further in the camt Cash Management Reporting section.

Direct Debit Transaction Information

---

<!-- Page 512 -->

# Account

The pacs.003 **Debtor Agent Account** and **Creditor Agent Account** are used to capture the account information related to these Agents. The nature of this element implies there is an Agent or Agent in between the Debtor Agent and Creditor Agent in the direct debit transaction.

The **Debtor Agent Account** and **Creditor Agent Account** use a variety of nested elements to capture information related to the account.

*   `Min 1 – Max 1` **Identification** identifies the account maintained at the Account Servicing Institution
*   `Min 0 – Max 1` **Type** uses the external Cash Account Type code list to identify the type of account
*   `Min 0 – Max 1` **Currency** identifies the currency of the account
*   `Min 0 – Max 1` **Name** identifies the name of the account as assigned by the Account Servicing Institution
*   `Min 0 – Max 1` **Proxy** captures an alternative identification of the account number such as an email address. This element has further nested **Type** which is a choice of external code list or proprietary code and **Identification** which are both mandatory where the Proxy element is used.

Debtor Agent and Creditor Agent are a Financial Institution, therefore

---

<!-- Page 513 -->

The `pacs.003` message introduces ultimate parties to the FI to FI Customer Direct Debit message. The **Ultimate Creditor** element should not be confused with an **Initiating Party** who may send a direct debit initiation request on behalf of the Creditor. (see dedication section on *Initiating Party*)

Ultimate Party
Ultimate Debtor
Ultimate Creditor

> `Min 0 - Max 1` CBPR+ premise is that an **Ultimate Debtor** has no financial regulated direct account relationship with the corresponding *Debtor*.

> `Min 0 - Max 1` CBPR+ premise is that an **Ultimate Creditor** has no financial regulated direct account relationship with the corresponding *Creditor*.

An account is often used a term to recognise an ongoing customer relationship. Non Agent payment provider are typically not bound by the same regulatory oversight as an Agent (Financial Institution). They would therefore be classed as a Party to a payment, where the account relationship with their customer would classify their customer as an Ultimate (Debtor or Creditor depending on the payment scenario)

Direct Debit Transaction Information
> Ultimate Creditor

---

<!-- Page 514 -->

Initiating Party
Debtor
Third Party
Debtor Agent

Min 0 – Max 1
The **Initiating Party** of a direct debit is often the Min 1 – Max 1 **Creditor** themselves and therefore this optional element is not necessary. More often the *Initiating Party* is a third party providing direct debit collection services on behalf of the *Creditor* (often referred to as a Third Party Provider) whereby the *Creditor* maintains an account with the Creditor Agent but the Third Party Provider has authority to initiate collection on behalf of the Creditor. This is distinctly different from an Ultimate Party (such as *Ultimate Creditor*) who instructs the *Creditor* to initiate a collection on their behalf.

In the context of a Direct Debit (pacs.003) or Request to Payment (pain.013) the *Initiating Party* is often the *Creditor*, however the same context of a Third Party Provider can exist where the third party is responsible for collecting funds on behalf of the *Creditor*.

Direct Debit Transaction Info - Initiating Party

---

<!-- Page 515 -->

Instructed Agent: Agent B
Instructing Agent: Agent A
pac.003

***Instructing Agent*** and ***Instructed Agent*** represent the Agents involved in the pac point-to-point message exchange. These roles therefore change on each payment leg.

***Instructing Agent*** and ***Instructed Agent*** elements are required in all pac messages and are available in the **Direct Debit Transaction Information**

Direct Debit Transaction Information > Instructing Agent

---

<!-- Page 516 -->

The pacs message can capture up to 3 Intermediary Agents, which play a dynamic role in the payment between the Debtor Agent and Creditor Agent.

Min 0 – Max 1
The **Intermediary Agent 1** captures the first Intermediary Agent between the Debtor Agent and Creditor Agent for who the Instructed Agent attempt to instruct the payment on to. This optional element is comparable with the Field 56a in the legacy FIN message.

Min 0 – Max 1
The **Intermediary Agent 1 Account** captured the account related to this Intermediary Agent, with the Instructed Agent. This element can be compared to the Party Identifier of the legacy Field 56a.

Min 0 – Max 1
The **Intermediary Agent 2** captures the second Intermediary Agent between the Intermediary Agent 1 and the Creditor Agent. This optional element has not comparable field in the legacy FIN message.

Min 0 – Max 1
The **Intermediary Agent 2 Account** captured the account related to this Intermediary Agent, with the Intermediary Agent 1. This optional element has not comparable field in the legacy FIN message.

Min 0 – Max 1
The **Intermediary Agent 3** captures the third Intermediary Agent between the Intermediary Agent 2 and the Creditor Agent. This optional element has not comparable field in the legacy FIN message.

Min 0 – Max 1
The **Intermediary Agent 3 Account** captured the account related to this Intermediary Agent, with the

---

<!-- Page 517 -->

The ISO 20222 pacs messages describe the party debited for a transaction as the **Debtor**. The **Debtor** sub elements describe the *Debtor* in greater detail. Min 1 – Max 1

Mandatory *Name* (where a BIC identifier is not provided) by which the party is known

**Name**

Department
Sub Department
Street Name
Building Number
Building Name
Floor
Post Box
Room
Post Code
Town Name
Town Location Name
District Name
Country Sub Division
Country
Code
Postal Address

Nested element capturing either structured or unstructured *Debtor* address details

**Postal Address**

**Debtor**

Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc.

**Identification**

Optional element to capture the Debtor's ISO country code of residence

**Country of Residence**

---

<!-- Page 518 -->

[Min 1 – Max 1]
The pacs.003 mandatory ***Debtor Account*** is used to capture the account information for which debit entry is/has been applied to the Debtor's account, which are also reflected in their account Statement.

The ***Debtor Account*** uses a variety of nested elements to capture information related to the account.

[Min 1 – Max 1] ***Identification*** identifies the account maintained at the Debtor Agent (Account Servicing Institution)

[Min 0 – Max 1] ***Type*** uses the external Cash Account Type code list to identify the type of account

[Min 0 – Max 1] ***Currency*** identifies the currency of the account

[Min 0 – Max 1] ***Name*** identifies the name of the account as assigned by the Debtor Agent (Account Servicing Institution)

[Min 0 – Max 1] ***Proxy*** captures an alternative identification of the account number such as an email address. This element has further nested ***Type*** which is a choice of external code list or proprietary code and ***Identification*** which are both mandatory where the Proxy element is used.

---

<!-- Page 519 -->

A children sports clubs (Creditor), collects its monthly membership fee via direct debit, against the parents (Debtor) of one of its members (Ultimate Debtor).

```
[Creditor]  <--  [Creditor Agent]  <--  camt.053  <--  [B]  <--  pacs.003  <--  [A]  <--  pain.008  <--  [Debtor]
                                              (DR / CR)        (4)        (3)        (2)        (1)
                                              [B]  -->  pacs.002  -->  [A]  -->  pain.002  -->  [Debtor]
```

**1** Sports club, the Creditor who has a mandate* with the Debtor, initiates a direct debit instruction by sending a pain.008 message to their bank, Creditor Agent (A).

**2** Agent A, the Creditor Agent, initiates a direct debit instruction by sending a pacs.003 message to the Debtor Agent (B).

**3** Debtor Agent (B) debits the account of the Debtor, credits the account of the Creditor Agent and confirms the direct debit status using a pain.002.

**4** Debtor, receives a statement from their bank confirming the monthly Debit Debit, for their child (Ultimate Debtors) sports club membership fee, has debited either account.

---

<!-- Page 520 -->

Min0 – Max1

The **Purpose** element within the pacs.003 FI to FI Customer Direct Debit captures the reason for the direct debit transaction which may either use an external ISO **Purpose code** or a proprietary code.
The purpose is used to capture the nature of the payment e.g. **IVPT** Invoice Payment, **FEES** Payment of Fees etc. and should not be confused with Regulatory Reporting codes. By definition this information is typically defined by the Creditor.

The externalised Purpose code set is classified by the purpose, for example commercial, for which the numerous codes within the classification are each described by Name and Definition.
For example, **LOAR** is classified within the Finance categorisation, with the *Name* **Loan Repayment** described as a repayment of loan to lender.

*Category Purpose* also captures a high level purpose, which unlike *Purpose* is less granular but can trigger special processing e.g. Category Purpose code SALA 'Salary Payment' may trigger a reporting process which restricts sensitive data i.e., individual salary names.

Direct Debit Transaction Information

---

<!-- Page 521 -->

Min 0 – Max 10
The *Regulatory Reporting* element within the pacs.003 FI to FI Customer Direct Debit is nested to capture regulatory and statutory information needed to report to the appropriate authority/s.

Min 0 – Max 1
The *Debit Credit Reporting Indicator* utilises an embedded choice of code to indicate whether the regulatory reporting information applies to the:
* DEBT (debit)
* CRED (credit) or
* BOTH

Min 0 – Max 1
The *Authority* element captures the *Name* and *Country* code of the Authority/Entity requiring the regulatory reporting information.

Min 0 – Max 1
The *Details* element provides the detail on the regulatory reporting information.

Direct Debit Transaction Information > Regulatory Reporting

---

<!-- Page 522 -->

The **_Related Remittance Information_** element within the pacs.003 FI to FI Customer Direct Debit is nested to provide information related to the handling of remittance information. This information is typically provided by the Creditor in the direct debit initiation request.

Min 0 – Max 1
The **_Remittance Identification_** captures a unique reference assigned by the initiating party of the collection to identify the remittance information sent separately from the direct debit instruction.

Min 0 – Max 2
The **_Remittance Location Details_** uses a set of nested elements to provide information on either the location of or the delivery of remittance information.
*   **_Method_** requires a code from an embedded list to detail the method used to deliver the remittance advice information e.g. **_EMAIL_** (email)
*   **_Electronic Address_** provides an electronic address for which an agent is to send the remittance information to e.g. the email address. It may also reference a URL where remittance information may be deposited or retrieved.
*   **_Postal Address_** provides the postal address to which an agent is to send the remittance information

Remittance advices are typically considered as a traditional value added service provided by the Creditor Agent to the Creditor, in order to facilitate reconciliation for the Creditor. By nature this element can travel end-to-end within the pain, pacs and camt reporting messages.
**_Remittance Information_** is a dedicated element used both within the pacs and camt reporting messages, whereby this information can travel end-to-end using ISO 20022. **_Related Remittance Information_** and **_Remittance Information_** are mutually exclusive (can't both be present)
Business examples are emerging where information is externalised using a URL repository solution.

---

<!-- Page 523 -->

The optional *Remittance Information* element within the pacs.003 FI to FI Customer Direct Debit is nested to provide either *Structured* or *Unstructured* information related to direct debit collections, such as invoices.

Min 0 – Max 1
*Remittance Information* enable the matching/reconciliation of an entry that the direct debit is intended to settle

Min 0 – Max 1
The *Unstructured* sub element captures free format *Remittance Information* which is restricted in CBPR+ to 140 characters to ensure backward compatibility with the legacy MT message during coexistence.

Min 0 – Max *
The *Structured* element is nested capturing rich structured *Remittance Information*, and is unlimited in its multiplicity, but must not exceed 9,000 characters of business information (does not include the xml element identification)
The use of this nested element should be *bilaterally/multilaterally* agreed, to ensure end-to-end transportation of this data.

Related *Remittance Information* and *Remittance Information* are

---

<!-- Page 524 -->

The bilaterally/multilaterally agreed **Remittance Information** which is *Structured* must not exceed 9,000 characters of business content (i.e. the information). This nested element is used to capture a variety of structured remittance information.

Structured
*   Referred Document Information
*   Referred Document Amount
*   Creditor Reference Information
*   Invoker
*   Invoice
*   Tax Reimbursement
*   Garnishment Reimbursement
*   Additional Remittance Information

example of *Structured* invoice information

The **Creditor Remittance Information** is provided to the **Creditor** in the Cash Management Reporting messages' Remittance Information component, for example, the camt.053 Bank to Customer Statement.

| Structured | <strd> | |
| :--- | :--- | :--- |
| Reference Document Information | <RfrdDocInf> | |
| Type | <Tp> | |
| Code Or Proprietary | <CdOrPrtry> | |
| Code | <Cd> | CINV |
| Number | <Nb> | A0000101 |
| Related Date | <Dt> | 2019-10-29 |

element names

xml tag

business information

In this example Referred Document Information and it nested elements has multiplicity which support up to 9,000 character of information. Whereby this element can be repeated to include more coded information such as another invoice.

Direct Debit Transaction Information
> Remittance Information

---

<!-- Page 525 -->

> Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases.

**Serial Financial Institution to Financial Institution Customer Direct Debit**
Use Case p.3.1.1 – High Level FI to FI Customer Direct Debit (pacs.003) successful settlement
Use Case p.3.1.2 – High Level FI to FI Customer Direct Debit (pacs.003) unsuccessful settlement

---

<!-- Page 526 -->

1
pain.008
pain.002
2
pacs.003
pacs.002
3
camt.053
Settlement Complete
4

1. Creditor initiates a direct debit instruction to the Creditor Agent

2. Creditor Agent (A) initiates a direct debit collection by sending a pacs.003 message to the Debtor Agent with the settlement method "INDA"

3. The Debtor Agent debits the account of the Debtor, and may optionally provide a notification e.g. debit notification in addition to an account statement (camt.053). The Debtor Agent also provides a status update ACSC (accepted settlement completed) to the Creditor Agent.

4. Creditor Agent (A) relays the status ACSC (accepted settlement completed) to the Initiating Party, based upon a bilateral agreement

---

<!-- Page 527 -->

3
pacs.003
pacs.002
2
pain.008
1
pain.002
4
Reject Reason
!

1
Creditor initiates a direct debit instruction to the Creditor Agent

2
Creditor Agent (A) initiates a direct debit collection by sending a pacs.003 message to the Debtor Agent with the settlement method "INDA"

3
The Debtor Agent fails to debit the account of the Debtor (e.g., account is closed). The Debtor Agent provides a status update RJCT (Rejected) with the rejection reason information.

4
Creditor Agent (A) relays the status RJCT (Rejected) to the Initiating Party with the rejection reason information

---

<!-- Page 528 -->

# Cash Management Reporting (Camt) messages

---

<!-- Page 529 -->

## Cash Management Reporting

[camt.052 - Bank to Customer Account Report](#)

[camt.053 - Bank to Customer Statement](#)

[camt.054 - Bank to Customer Debit Credit Notification](#)

[camt.057 – Notification To Receive](#)

[camt.058 – Notification To Receive Cancellation Advice](#)

[camt.060 – Account Report Request](#)

---

<!-- Page 530 -->

# Bank to Customer
# Account Report

---

<!-- Page 531 -->

# camt.052

- Group Header
- Report

The Bank To Customer Account Report message is sent by the account servicer to an account owner or to a party authorised by the account owner to receive the message. It can be used to inform the account owner, or authorised party, of:

- entries reported to the account (Intraday Statement)
- account balance information (Account Balance Report)
- or both.
- for a given point in time.

The Bank To Customer Account Report is restricted to a single account statements per InterAct message (100,000 bytes)

This message must be bilaterally agreed between the Account Servicing Institution and the Account owner, and is establish by an BMA business profile

---

<!-- Page 532 -->

pacs.008
camt.052
pacs.002
pacs.008
camt.052
camt.052
camt.052

Role of the Creditor Agent and Creditor in the payment changes by description in the Bank to Customer Account Report message to Account Servicer and Account Owner. Whereby the report is send by the Account Servicer to the Account Owner and or authorised party. This message is used to inform the account owner, or authorised party, of the entries

---

<!-- Page 533 -->

# Group Header

---

<!-- Page 534 -->

Each ISO 20022 cash management reporting message has a *Message Identification* element, located in the Group Header. This **35 character** identifier is a point-to-point reference used to unambiguously identify the message.

For Cash Management (camt) messages the *Message Identification* has no exact equivalent in the legacy MT Customer Statement message. However, the *Transaction Reference Number* (Field 20) could be considered a similar comparison.

Group Header > Message Identification

---

<!-- Page 535 -->

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+-hh:mm
> For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

Group Header Creation Date Time

---

<!-- Page 536 -->

Min 0 – Max 1

The Bank to Customer Account Report **Message Recipient** nested element provides details of the party authorised by the *Account Owner* to receive the Account Report.

This element **should only** be used to identify the *Message Recipient* when different from the account owner, which is implied by the usage of **COPY** in the *Copy Duplicate Indicator* within the nested Statement element.

Where **Message Recipient** is used the nested:

- **Name** Min 0 – Max 1
- **Postal Address** Min 0 – Max 1
- **Identification** Min 0 – Max 1
- **Contact Details** Min 0 – Max 1

may be used to capture information related to this party.

Group Header ⓘ Message Recipient ✓
Name

---

<!-- Page 537 -->

The Bank to Customer Account Report **Original Business Query** `Min 0 – Max 1` element identifies a query to generate a report, for example a camt.060 Account Reporting Request.

Where **Original Business Query** is used the original **Message identification** `Min 1 – Max 1` (i.e., the message identification of the camt.060 message) is required. Original **Message Name identification** `Min 0 – Max 1` and Original **Creation Date Time** `Min 0 – Max 1` may also be provided.

Group Header > Original Business Query > Message Identification

---

<!-- Page 538 -->

Min 0 – Max 1

The Bank to Customer Account Report **_Additional Information_** element represents further details related to the account statement.

In accordance to the usage in the camt.053 this element could be used to describe additional information to distinguish the different camt.052 usage i.e., where the report is only reporting an intraday balance, intraday entries or both. Unlike the camt.053 there is no recommended identification string to represent usage.

Additional Information is a textual element restricted in CBPR+ to 500 characters.

Group Header > Additional Information

---

<!-- Page 539 -->

report

---

<!-- Page 540 -->

Min 1 - Max 1

The Bank to Customer Account Report *Report* element provides information related to an account, most typically associated with intraday account entries and or accounting balances (where entries have been processed on the account). The report element can be used to advise entries reported to the account (Intraday Statement), account balance information (Account Balance Report) or both.

The *Report* element has been restricted to one account report. To report additional accounts to the Account Owner this would need to occur via a separate message in a similar way to the legacy MT 942.

It should also be noted the Account Report message is modelled identically to the Account Statement (camt.053) therefore where used as an intraday transaction report the content can be capture identically to the statement at the close of the business day.

Report

---

<!-- Page 541 -->

Similar to the legacy MT Intraday Reporting message (i.e., 942) the camt.052 Bank to Customer Account Report is constrained in CBPR+ by the FINPlus service's message size. Consideration therefore need to be given (when reporting transactional information) to identifying: the **report order**, the **report correlation** and the **last report page**.

**1**

Report Pagination
Page 1
Last Page No
Electronic Sequence Number 16
Legal Sequence Number 3
Account
Id 12345
Currency EUR
Entry
......

**2**

Report Pagination
Page 2
Last Page No
Electronic Sequence Number 16
Legal Sequence Number 3
Account
Id 12345
Currency EUR
Entry
......

**3**

Report Pagination
Page 3
Last Page Yes
Electronic Sequence Number 16
Legal Sequence Number 3
Account
Id 12345
Currency EUR
Balance
ITAV Interim Available
Entry
......

**Report Order:** identifying the order in which statements should be processed or reconciliated. Options:
Report Pagination

**Report Correlation:** identifying statement which relate to each other for a given statement period. Options:
Legal Sequence Number

**Last Report:** identifying when no further statements for a given period are expected i.e. period statement in finalised. Options:
Report Pagination, Last Page Indicator

---

<!-- Page 542 -->

Min 1 – Max 1

The Bank to Customer Account Report message ***Identification*** provides a mandatory element to identify the statement

Unique reference assigned by the account servicer to unambiguously identify the account report. Directly comparable with the *Transaction Reference Number* (Field 20) of the legacy MT statement message.

---

<!-- Page 543 -->

The Bank to Customer Account Report message **Report Pagination** element provides the page number of the report.

**Min 1 – Max 1**
**Min 1 – Max 1**
**Min 1 – Max 1**

***Report Pagination*** includes the **Page Number** and **Last Page indicator** elements.

**For example**, a *Page Number* of 2 represents the current account report, being the second page of the and implying a previous account report page had been sent. The *Last Page indicator* further implies whether more pages are expected

Noted: as **Report Pagination** is required, even if there is only one page to the report being sent. Both the **Page Number** and **Last Page indicator** will need to be provided i.e., 1 and Yes.

---

<!-- Page 544 -->

Min 0 – Max 1
The Bank to Customer Account Report message **Electronic Sequence Number** allows the *Account Servicer* to assign a number to each Report which should increment by 1 for each electronic statement report sent.

1. This element allows easy recognition of the Report order, equivalent to the legacy Field 28C Statement Number. The sequence should increment for each camt.052 message sent to the Account Owner or Authorised Party this number must be the same value where the statement continues over multiple pages (*Report Pagination*) of the report for a give account.

   Should this sequence number be reset by the *Account Servicer*, this should not occur more frequently than once a day. Likewise, this 18 digit counter could be incremented to its maximum value before it's reset.

2. The use of Electronic Sequence Number and the sequence reset logic should be bilaterally agreed been the *Account Servicer* and the *Account Owner*
   Either **Electronic Sequence Number** or **Legal Sequence Number**

---

<!-- Page 545 -->

The Bank to Customer Account Report message **Reporting Sequence** specifies the choice of identification sequences. This can be used as an alternative to the **Report Pagination** or **Electronic Sequence Number** as a way to identify the report order, which is not confined to numeric values.

Where used the **Reporting Sequence** mandate a choice of nested element:

- **From Sequence** identifies the start of a sequence range. `Min 0 – Max 1`
- **To Sequence** identifies the end of a sequence range. `Min 1 – Max 1`
- **From To Sequence** identifies the start and end of a sequence range. `Min 1 – Max*`
- **Equal Sequence** identifies a sequence. `Min 1 – Max*`
- **Not Equal Sequence** identifies a sequence to be excluded. `Min 1 – Max*`

The Reporting Sequence may be provided in the camt.060 Account Reporting request to specify, for example, a range of Statements to be sent. Alternatively, Account Reports can often be produced on a bilaterally agreed period basis.

---

<!-- Page 546 -->

Min 0 – Max 1

The Bank to Customer Account Report message ***Legal Sequence Number*** allows the *Account Servicer* to assign a number to each report which should increment by 1 for each Report sent.

Where the Intraday Account Report uses multiple camt.052 messages for a given report period the ***Legal Sequence Number*** must be the same number in each report message during that reporting period. This element can be considered an equivalent to the legacy Field 28C Statement Number

Either ***Electronic Sequence Number*** or ***Legal Sequence Number*** should be provided to enable the identification of a report number.

Report > Legal Sequence Number

---

<!-- Page 547 -->

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
> For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

Record Creation Date Time

---

<!-- Page 548 -->

The Bank to Customer Account Report message **<u>From to Date</u>** allows the *Account Servicer* to specify the start date time and end date time applicable to the intraday account entries and or accounting balances being reported.
For intraday account reports this is an important attribute that allows the account owner to understand the period for which the report applies. The element is not mandatory as the report may only contain the balance, whereby the report **<u>Creation DateTime</u>** may be used to identify the date and time associated to the balance.
Where **<u>From to Date</u>** is used the **<u>From Date Time</u>** and **<u>To Date Time</u>** become mandatory elements.
CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):
Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+-/hh:mm
➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Time as well as Eastern Standard Time in the U.S.)
All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- Page 549 -->

Min 0 – Max 1

The Bank to Customer Account Report message **_Copy Duplicate Indicator_** is used as a choice to identify additional reports from the original sent to the Account Owner.

**_COPY_** is used when a copy of the report is sent to an Authorised Third Party, such as a company head office, parent entity, or an institution providing additional service.

**_DUPL_** is used when a duplicate of the report is sent to the Account Owner, this resubmission may have been requested using the cant.060 or an alternative channel such as via internet banking or customer service request.

**_CODU_** is used when a duplicate of a report copy is sent to an Authorised Third Party, this resubmission may have been requested using the cant.060 or an alternative channel such as via internet banking or customer service request. It may also be requested by the Account Owner on behalf of the Authorised Third Party, depending on the arrangement in place with the Account Servicer.

---

<!-- Page 550 -->

Min 0 – Max 1

The Bank to Customer Account Report message **Reporting Source** allows the *Account Servicer* to define the source of the intraday account entry and or account balance report, typically associated with an application.

**Reporting Source** utilises the external Reporting Source code list. For example **ACCT** represents a statement or report based on accounting data, whereas **DEPT** represents a cash or deposit system.
Where the source of the statement is functionally required by the consumer of the statement i.e., the *Account Owner* or authorised *Third Party*, the codes used should be bilaterally agreed.

---

<!-- Page 551 -->

Min 1 – Max 1

The Bank to Customer Account Report message **Account** provides nested elements to identify the account for which debit and credit entries have been made. The following two mandatory elements are nested beneath *Account*.

**Account**

**Identification** — Min 1 – Max 1

a unique **Identification** for the account, between the Account Servicer and Account Owner. The element is further nested by choice of *IBAN* or *Other* to capture the account.

**Currency** — Min 1 – Max 1

The **Currency** for which the account is held. This is identified using the three characters *ISO currency code*.

Report > Account >

---

<!-- Page 552 -->

Min 1 – Max 1    Min 0 – Max 1

The Bank to Customer Account Report message mandatory **Account** also provides a number of optional nested element to identify the account for which debit and credit entries have been made.

## Account

- **Type**
  An element which may either use an external ISO **Cash Account Type code** or a proprietary code. It is used to identify a particular type of account.

- **Name**
  The Name of the Account, as Assigned by the servicing institution.

- **Proxy**
  A nested element which contains a Proxy Identifier together with the Proxy Type represented by either use an external ISO **Proxy Account Type code** or a proprietary code.

- **Owner**
  A nest element that contains the Party that legally owns the account.

---

<!-- Page 553 -->

The Bank to Customer Account Report message <sup>Min 0 – Max 1</sup> **Related Account** allows the identification of a related parent account for the account report. For example sweeping, pooling or virtual account for which the report is produced can identify the parent account they hierarchically relate to.

When **Related Account** is utilized, like **Account**, the <sup>Min 1 – Max 1</sup> **Identification** and <sup>Min 1 – Max 1</sup> **Currency** element become mandatory. Additionally, the nested <sup>Min 0 – Max 1</sup> *Type* element, <sup>Min 0 – Max 1</sup> *Name* and nested <sup>Min 0 – Max 1</sup> *Proxy* element are optionally available.

*Related Account* uses a variety of common elements described in more detail within the *Account* section.

Report > Related Account
Identification
Type

---

<!-- Page 554 -->

Min 0 – Max *

The Bank to Customer Account Report message **Interest** provides interest information that applies to the account.

**Interest**

- **Type**
  An element which may either use an embedded ISO *Interest Type code*: **INDY** (Intraday) **OVRN** (Over Night) or a proprietary code. It is used to identify a particular interest type.

- **Rate**
  The type of interest Rate defined as a *Percentage* and in an *Other* form. Validity Range optionally defines an *Amount*, *Credit Debit Indicator* and *Currency*.

- **From To Date**
  The date range for which interest has been calculated. *From Date Time* and *To Date Time* must be representing when using this element.

- **Reason**
  The optional Reason for which interest is applied.

- **Tax**
  Provides details on any tax applied to the Interest. Where optional

---

<!-- Page 555 -->

The Bank to Customer Account Report message optional **Balance** is a nested element to define the account balance at a specific point in time. The following four elements nested beneath *Balance* are mandatory

**Balance**

**Type**
A nested element which may either use an external ISO *Balance Type code* or a proprietary code. For example, OPAV – Opening Available. Additionally, a Sub Type represented by either use an external ISO *Balance Sub Type code* or a proprietary code, may be used.

**Amount**
Balance amount.

**Credit Debit Indicator**
Embedded code CRDT (Credit balance) DBIT (Debit balance)

**Date**
A nested element representing the *Date* and the *DateTime* (with UTC offset) of the balance.

---

<!-- Page 556 -->

*Balance Type* code are used within the nested *Balance* element to represent the type/s of balance being reported. In comparison the legacy MT 941 utilizes different Fields and Tag options to represent a number of these Balance Types. The below extract from the externalised ISO *Balance Type* code list compares the code with the population of the equivalent information in the Legacy MT 941 Balance Report.

| Code | Name | Definition | MT 941 Comparison |
| :--- | :--- | :--- | :--- |
| CLAV | ClosingAvailable | Closing balance of amount of money that is at the disposal of the account owner on the date specified. | Field 64 |
| CLBD | ClosingBooked | Balance of the account at the end of the pre-agreed account reporting period. It is the sum of the opening booked balance at the beginning of the period and all entries booked to the account during the pre-agreed account reporting period. | Field 62F |
| FWAV | ForwardAvailable | Forward available balance of money that is at the disposal of the account owner on the date specified. | Field 65 |
| INFO | Information | Balance for informational purposes. | No equivalent |
| ITAV | InterimAvailable | Available balance calculated in the course of the account service's business day, at the time specified, and subject to further changes during the business day. The interim balance is calculated on the basis of booked credit and debit items during the calculation time/period specified. | Field 64 |
| ITBD | InterimBooked | Balance calculated in the course of the account service's business day, at the time specified, and subject to further changes during the business day. The interim balance is calculated on the basis of booked credit and debit items during the calculation time/period specified. | Field 62F |
| OPAP | OpeningAvailable | Opening balance of amount of money that is at the disposal of the account owner on the date specified. | No equivalent |
| OPBD | OpeningBooked | Book balance of the account at the beginning of the account reporting period. It always equals the closing book balance from the previous report. | Field 60F |
| PBCD | PreviouslyClosedBooked | Balance of the account at the previously closed account reporting period. The opening booked balance for the new period has to equal to this balance. | No equivalent |
| XPCD | Expected | Usage: the previously booked closing balance should equal (inclusive of) the booked closing balance of the date it references and equal the actual booked opening balance of the current date. | No equivalent |

---

<!-- Page 557 -->

Min 1 – Max *

The Bank to Customer Account Report message mandatory *Balance* also provides the optional set of nested element to define a *Credit Line*

Min 0 – Max *

The true/false Boolean of *Included* to clearly determine whether the Credit Line Amount is included in the balance is mandatory in the set of Credit Line element.

Additionally, the following optional nested element may be used to identify:

- The *Type* of Credit Line, which may either use an external ISO *Credit Line Type code* or a proprietary code.
- A set of elements to provide *Credit Line* details
- The *Amount* (Currency and Amount) of the Credit Line
- The *Date* (nested as Date, DateTime) of the Credit Line, provided to distinguish where multiple Credit Line exist.

The final optional nested element within *Balance* is the *Availability* of the booked amount i.e., when it is available to be accessed.

| Report > Balance > | Type > |
|---|---|
|  | Credit Line > |
|  | Amount > |

The *Credit Line* element is unlimited (Max *) whereby more that one *Credit Line* may be reported, the *Date* becomes an important element to distinguish between different Credit Lines.

---

<!-- Page 558 -->

The Bank to Customer Account Report message optional `Min 0 – Max 1` **Transaction Summary** provides a set of nested element to summarize entry information. Where the intraday account entries and or accounting balances are reported using multiple camt.052 messages for a given reporting period the *Transaction Summary* should only be included on the first Report message (*Balance Type OPBD* with no *Balance Sub Type*) summarizing the whole Statement Report (entire statement period) This aligns with the Common Global Implementation (CGI) where a *Transaction Summary*, if provided, would appear before the first *Entry* elements.

Each of the following element allow an optional total of entries either as a **Number of Entries** and or as a **Sum**.

> **Total Entries**
>
> **Total Credit Entries**
>
> **Total Debit Entries**
>
> **Total Entries Per Bank Transaction Code**

In addition to the **Number of Entries** and **Sum**, the `Min 0 – Max *` **Total Entries Per Bank Transaction Code** requires the `Min 1 – Max 1` **Bank Transaction Code** element and optionally allows a variety of other optional elements.

> The **Total Entries Per Bank Transaction Code** element is unlimited (Max *) whereby more that one **Bank Transaction Code** may be summarised.

---

<!-- Page 559 -->

The Bank to Customer Account Report message optional **Entry** provides a significant variety of nested elements to represent the details associated with each **Entry**. For active accounts which have intraday entries posted across them, this set of nested elements is arguably the most relevant for the account owner and in many way is comparable with the MT 942 Field 61 Statement Line.

Unlike the legacy MT Interim Transaction Report message, the camt.052 has a number of dedicated elements to capture a variety of entry level data. It also has a number of enhancements on the legacy MT Interim Transaction Report message where parties in the payment and customer remittance information, as examples, can provided to the *Account Owner*.

| Min 0 – Max * | Entry Reference | Min 1 – Max 1 | Amount | Min 0 – Max 1 | Credit Debit Indicator ⇄ | Min 0 – Max 1 | Reversal Indicator ⇄ | Min 1 – Max 1 | Status ⇄ |
|---|---|---|---|---|---|---|---|---|---|
| Min 0 – Max 1 | Booking Date ⇄ | Min 1 – Max 1 | Value Date ⇄ | Min 0 – Max 1 | Account Servicer Reference › | Min 0 – Max * | Availability › | Min 1 – Max 1 | Bank Transaction Code |
| Min 0 – Max 1 | Commission Waiver Indicator › | Min 0 – Max 1 | Additional Information Indicator › | Min 0 – Max 1 | Amount Details › | Min 0 – Max 1 | Charges › | Min 0 – Max 1 | Technical Input Channel ⇄ |
| Min 0 – Max 1 |  | Min 0 – Max 1 |  | Min 0 – Max * |  | Min 0 – Max 1 | Additional |  | Report Entry › |

---

<!-- Page 560 -->

**Min 0 - Max 1**
**Entry Reference**
Unique reference for the booking entry, created by the Account Servicing Institution as a reference they assign to identify the entry posted to the account.

**Min 1 - Max 1**
**Amount**
Mandatory element representing the currency and amount of the entry. This can be compared to Field 61 subfield 4 and 5 of the legacy MT 942.

**Min 1 - Max 1**
**Credit Debit Indicator**
Mandatory element indicating whether the *Amount* entry is a **DBIT** (Debit) or **CRDT** (Credit) to the account. This can be compared to Field 61 subfield 3 of the legacy MT 942.

**Min 0 - Max 1**
**Reversal Indicator**
Indicates whether the entry is a result of a reversal. for example, an entry related to a pacs.004 Payment Return or reverses an error such as an incorrect value date applied to the entry. Where the *Reversal Indicator* is **Yes**, the *Credit Debit Indicator* should be the opposite of the original entry, for example original *Credit Debit Indicator* of **CRDT** would expect a reversal entry *Credit Debit Indicator* of **DBIT**. This can be compared to Field 61 subfield 3 of the legacy MT 942

---

<!-- Page 561 -->

**Min 1 – Max 1**
**Status**

Mandatory element representing the status using an external ISO Entry Status code for example BOOK is used to confirm the entry is booked.

> Status BOOK is the only status that can be reversed using the *Reverse Indicator*

**Min 0 – Max 1**
**Booking Date**

Mandatory choice of *Date* or *Date Time* the entry was posted to the *Account*. This can be compared to Field 61 subfield 2 of the legacy MT 942.

**Min 1 – Max 1**
**Value Date**

Mandatory choice of *Date* or *Date Time* the entry become available. This can be compared to Field 61 subfield 1 of the legacy MT 942.

> Noting CBPR+ usage guidelines mandate the time zone that the *Date Time* represents as an offset against Universal Time Coordinated (UTC)

**Min 0 – Max 1**
**Account Servicer Reference**

Additional optional Reference typically assigned by the Account Servicer's payment engine or accounting platform. This reference would be used to query an entry. This can be compared to Field 61 subfield 8 of the legacy MT 942.

**Min 0 – Max \***
**Availability**

Indicates when the booked amount is available i.e., when it is available to be accessed.

---

<!-- Page 562 -->

Min 1 – Max 1
**Bank Transaction Code**

The **Bank Transaction Code** is designed to deliver a harmonized set of codes, which should be applied in bank-to-customer cash account reporting information. The bank transaction code information allows the **account servicer** to correctly report a transaction, which in its turn will help **account owners** to perform their cash management and reconciliation operations.

Domain
Family
Sub-Family

The structure of the Bank Transaction Code has three levels:
**Domain:** Highest definition level to identify the sub-ledger. The domain defines the business area of the underlying transaction e.g., payment, securities etc.)
**Family:** Medium definition level e.g. type of payment; credit transfer, direct debit etc.
**Sub-family:** Lowest definition level e.g. type of cheques; draft etc.

Bank Transaction Codes are an external code set defined in the *Bank Transaction Code* combinations external code sets.

---

<!-- Page 563 -->

# Payouts Domain Families

| | | | Min 1 – Max 1 |
|---|---|---|---|
| **1.** | **Received Credit Transfers** | Receivable Credit Transfers are instructions to receive an amount of money from a del account owner. The receivable credit transfers are related to transactions received i account owner. | |
| **2.** | **Issued Credit Transfers** | Payable Credit Transfers are instructions to transfer an amount of money by the acco to a creditor. The payable credit transfers are related to instructions sent by the acco account owner. | |
| **3.** | **Received Cash Concentration** | Transaction is related to incoming cash movements that are related to cash management activities initiated by the owner of the sending account to optimise the return on the av funds. | |
| **4.** | **Issued Cash Concentration** | Transaction is related to outgoing cash movements that are related to cash managemen activities initiated by the owner of the account to optimise the return on the available f | |
| **5.** | **Received Direct Debits** | The Received Direct Debit transactions are related to instructions received by the acc to debit the account. | |
| **6.** | **Issued Direct Debits** | The Issued Direct Debit transactions are related to instructions sent by the account own collect an amount o | |
| **7.** | **Received Cheques** | Transaction is rela- from the cheque dr. | **Sub-Families for both Received and Issued Credit Transfers** |
| **8.** | **Issued Cheques** | Transaction is rela- | **Sub-Families for both Received and Issued Credit Transfers** |

| | **Internal Book Transfer** | **Definition** |
|---|---|---|
| | **Standing Order** | Transaction is a standing order – two different accounts within the same bank |
| | **Cross-Border Standing Order** | Transaction is a cross-border standing order |
| | **SEPA Credit Transfer Domestic Credit Transfer** | Transaction is a SEPA credit transfer <br> Transaction is a in-country domestic currency credit transfer |
| | **Cross-Border Credit Transfer** | Transaction is a cross-border credit transfer |
| | **Credit Transfer with agreed Commercial Information** | Transaction is a credit transfer including commercial information, i.e. additional informat agreed between the sender and the receiver. |
| | **Financial Institution Credit Transfer** | Transaction is a financial institution credit transfer, i.e. the debtor and creditor are financi institutions. |
| | **Priority Credit Transfer** | Transaction is a credit transfer defined with higher priority, e.g. a PRIURO credit transfer |
| | **Payroll/Salary Payment** | Transaction is related to the payment of a payroll salary |
| | **Cross-border** | Transaction is related to the payment of a cross-border payroll salary |

The description of **Bank Transaction Codes** are available to download from the ISO20022.org external code list page. These include the descriptions for Payments Domain Families and sub-families for both Received and Issued Credit Transfers.

https://www.iso20022.org/external_code_list_page

---

<!-- Page 564 -->

| **Bank Transaction Code - all permitted combinations of the BTC code sets** | | | | | | | |
|---|---|---|---|---|---|---|---|
| *All codes in light gray are defined as the generic codes available for all Domains and Families* | | | | | | | |
| Domain | Family | SubFamily | DomainCode | FamilyCode | SubFamilyCode | ExampleOfATransactionDomainCode | ExampleOfATransactionFamilyCode | ExampleOfATransactionSubFamilyCode | Status | StatusDate |
| Payments | Issued Credit Transfers | Cross-Border Credit Transfer | PMNT | ICDT | XBCT | | | | New | 27/4/2009 |
| Payments | Received Credit Transfers | Cross-Border Credit Transfer | PMNT | RCDT | XBCT | | | | New | 27/4/2009 |

Bank Transaction Codes are an external code set defined in the *Bank Transaction Code* combinations external code sets.
As an example a debit statement transaction which relates to a cross-border payment initiated from an account would be represented by:

| **Domain** | **Family** | **Sub-Family** |
|---|---|---|
| PMNT (Payment) | ICDT (Issued Credit Transfer) | XBCT (Cross-Border Credit Transfer) |

---

<!-- Page 565 -->

**Min 0 - Max 1**
**Commission Waiver Indicator**
Optional element indicating, as a Boolean, whether the entry is exempt from commission. This element is not typically associated with Correspondent Banking payments

**Min 0 - Max 1**
**Additional Information Indicator**
Optional element indicating whether the underlying transaction details are provided through a separate message. Where the ***Message Name Identification*** represents the message used to provide the additional information and ***Message Identification*** specifies the reference of the message that provides the additional information.

**Min 0 - Max 1**
**Amount Details**
Optional nested element which provides various elements to represent an aggregated (consolidated) original amount. Where individual transaction amounts can be represented, if required, within the ***Entry Detail*** set of elements.
This element is useful to capture original amount details where they are different to the ***Entry Amount***, for example the ***Instructed Amount*** of the payment can be included, together with a potential ***Currency Exchange*** rate, where necessary.

**Min 0 - Max 1**
**Charges**
Optional nested element to provide information on charges either pre-advised or taken from the entry.

Report > Entry >

---

<!-- Page 566 -->

**Min 0 – Max 1**

**Technical Input Channel**

Optional element which may either use an external ISO **Technical Input Channel code** or a proprietary code used to represent the technical channel used to input the entry.

**Min 0 – Max 1**

***Interest***

Optional nested element detailing any interest accrued as part of an aggregated (consolidated) entry amount.

**Min 0 – Max 1**

**Card Transactions**

Optional nested element which provides details associated with a card transaction such as the card number, card brand etc.

**Min 0 – Max 1**

**Entry Details**

Additional optional nested element containing details on the entry. See dedicated section on ***Entry Details.***

**Min 0 – Max 1**

**Additional Statement Information**

Additional optional element to represent further information related to the account statement

---

<!-- Page 567 -->

The Bank to Customer Account Report message optional **_Entry Details_** (Min 0 – Max *) provides a variety of nested elements to represent the details associated with each **_Entry_**.

**_Batch_** provides details on batched transactions such as the total **_Number of Transactions_** the batched entry (sometimes referred to as a consolidated entry) represents.
**_Transaction Details_** is a significant nested element which represents information on the underlying transaction.

---

<!-- Page 568 -->

When the Bank to Customer Account Report message optional **Entry Details** is utilized the nested **Transaction Details** element is mandatory.

**Transaction Details** has a variety of nested elements closely associated with **Entry** level elements. The **References** element however is nested to include a variety of references related to the entry including for example the **UETR**

| Min 1 – Max 1 | Min 1 – Max 1 | Min 1 – Max 1 | Min 0 – Max 1 | Min 0 – Max 1 | Min 0 – Max 1 | Min 0 – Max 1 | Min 0 – Max 1 |
|---|---|---|---|---|---|---|---|
| References | Amount | Credit Debit Indicator | Amount Details | Availability | Bank Transaction Code | Charges | Interest |

Additionally, **Transaction Details** also has a variety of elements capturing details from the underlying transaction, which amongst other business transactions includes payment transaction data. For example, **Remittance Information** and **Related Parties**

Report > Entry > Entry Details > Transaction Details

---

<!-- Page 569 -->

Min 0 - Max 1 Min 0 - Max 1
The Bank to Customer Account Report message **Related Parties** and **Related Agents** represents a set of optional nested elements related to the underlying transaction. Where the **Entry Details** (the set of elements *Related Parties/Agents* belongs to) relate to a Payment, Clearing and Settlement (pacs) message, parties in the pacs messages can be transferred into the Cash Management (camt) message.

| These **Related Parties** include : | These **Related Agents** include : |
| :--- | :--- |
| • *Instructing Party* | • *Instructing Agent* |
| • *Debtor* | • *Instructed Agent* |
| • *Debtor Account* | • *Debtor Agent* |
| • *Ultimate Debtor* | • *Creditor Agent* |
| • *Creditor* | • *Intermediary Agent 1* |
| • *Creditor Account* | • *Intermediary Agent 2* |
| • *Ultimate Creditor* | • *Intermediary Agent 3* |

**Trading Party** is also present in the **Related Parties** elements, and the following are present in the **Related Agents** elements: **Receiving Agents, Delivering Agent, Issuing Agent** and **Settlement Place**. Although these elements are not directly associated with a payment, as a Customer receiving an Account Report related to other Business Domains e.g. a Security

---

<!-- Page 570 -->

The Bank to Customer Account Report message *Entry Details* have a number of additional elements beyond *Related Parties* and *Related Agents* to capture information from the underlying payment.

These are:
* *Local Instrument*
* *Purpose*
* *Related Remittance Information*
* *Remittance Information*
* *Related Dates* such as the *Interbank Settlement Date*
* *Tax*

For *Payment Return* (pacs.004) it is also possible to capture *Return Information* which includes:
* The *Original Bank Transaction Code* of the original Entry
* The *Originator* of the return from the pacs.004
* And the *Reason* code.

*Remittance Information* as an end-to-end element should be passed unaltered from Payment Initiation (pain) into the Payment, Clearing and Settlement (pacs) message and onto the Bank to Customer Account Statement/Account Report (camt). The *Remittance Information* element is common to these message sets

---

<!-- Page 571 -->

It should also be mentioned that the Bank to Customer Account Report message *Entry Details* have a number of additional elements which capture information from transactions in other business domains beyond payments, as well as have an element to capture *Additional Transaction Information*.

These are:
- *Related Quantity*
- *Financial Instrument Identification*
- *Corporate Action*
- *Safekeeping Account*
- *Cash Deposit*
- *Card Transactions*

---

<!-- Page 572 -->

| Use case should be considered as a principal example whereby use case may be cross referenced |
|---|

**Bank to Customer Reports**
Use Case c.52.1.a – Bank to Customer Account Balance Report produced by the Creditor Agent
Use Case c.52.1.b – Bank to Customer Account Intraday Transaction Report produced by the Creditor Agent
Use Case c.52.1.b.1 – Bank to Customer Account Intraday Transaction Report's and Account Statement produced by the Creditor Agent
Use Case c.52.1.c – Bank to Customer Account Intraday Transaction and Balance Report produced by the Creditor Agent

> 🚩 Use Case camt.060 for requesting a Bank to Customer report

> 🚩 Use Case for copy or duplicate reports refer to camt.053 use cases

---

<!-- Page 573 -->

1 → 2 —`pacs.008`→ 3 —`pacs.008`→ 4 —`pacs.008`→ 5/6 —`camt.052`→

| 1 | 3 | 5 |
|---|---|---|
| Debtor initiates a payment instruction to the Debtor Agent | Agent B processes the payment on Agent C | Creditor Agent credits the account of the Creditor |
| 2 | 4 | 6 |
| Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries | Agent C processes the payment on Agent D | Creditor Agent as the Account Servicer produces and sends a balance report to either the Account Owner, or an authorised third party. |

---

<!-- Page 574 -->

# Creditor Agent

1 → 2 (A) --pac.008--> 3 (B) --pac.008--> 4 (C) --pac.008--> 5/6 (D) --camt.052--> Wallet

**1**
Debtor initiates a payment instruction to the Debtor Agent

**2**
Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries

**3**
Agent B processes the payment on Agent C

**4**
Agent C processes the payment on Agent D

**5**
Creditor Agent credits the account of the Creditor

**6**
Creditor Agent as the Account Servicer produces and sends a balance report to either the Account Owner, or an authorised third party.

---

<!-- Page 575 -->

# Statement produced by the Creditor Agent

1 → 2 (pacs.008) → 3 (pacs.008) → 4 (pacs.008) → 5 / 6 (camt.052 / camt.053) → 7

**1**
Debtor initiates a payment instruction to the Debtor Agent

**2**
Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries

**3**
Agent B processes the payment on Agent C

**4**
Agent C processes the payment on Agent D

**5**
Creditor Agent credits the account of the Creditor

**6**
Creditor Agent as the Account Servicer produces and sends several intraday transaction reports throughout the business day to either the Account Owner, or an authorised third party.

**7**
Creditor Agent C as the Account Servicer produces an Account Statement at the close of the business day reflecting all the transaction entries, include those provided in the intraday

---

<!-- Page 576 -->

# by the Creditor Agent

1 → 2 (A) —`pacs.008`→ 3 (B) —`pacs.008`→ 4 (C) —`pacs.008`→ 5/6 (D) —`camt.052`→

1. Debtor initiates a payment instruction to the Debtor Agent
2. Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries
3. Agent B processes the payment on Agent C
4. Agent C processes the payment on Agent D
5. Creditor Agent credits the account of the Creditor
6. Creditor Agent as the Account Servicer produces and sends a intraday transaction and balance report to either the Account Owner, or an authorised third party.

---

<!-- Page 577 -->

# Bank to Customer Statement

---

<!-- Page 578 -->

```
┌─────────────────────┐
│       camt.053      │
└─────────────────────┘
        │
        ├── ┌─────────────────────┐
        │   │    Group Header     │
        │   └─────────────────────┘
        │
        └── ┌─────────────────────┐
            │      Statement      │
            └─────────────────────┘
```

**The Bank To Customer Statement** message is sent by the account servicer to an account owner or to a party authorised by the account owner to receive the message. It is used to inform the account owner, or authorised party, of the entries booked to the account, and to provide the owner with balance information on the account at a given point in time

The Bank To Customer Account Statement is restricted to a single account statements per InterAct message (100,000 bytes) This message must be bilaterally agreed between the Account Servicing Institution and the Account owner, and is establish by an

---

<!-- Page 579 -->

### Sequence Diagram Flow

**Entities:**
*   Customer (Left)
*   Account Servicer A
*   Account Servicer B
*   Account Servicer C
*   Customer (Right)

**Message Flow:**
1.  Customer (Left) $\rightarrow$ Account Servicer A
2.  Account Servicer A $\rightarrow$ Customer (Left)
3.  Account Servicer A $\rightarrow$ Account Servicer B: `pac.008`
4.  Account Servicer B $\rightarrow$ Account Servicer A: `pac.002`
5.  Account Servicer A $\rightarrow$ Customer (Left): `camt.053`
6.  Account Servicer B $\rightarrow$ Account Servicer A: `camt.053`
7.  Account Servicer B $\rightarrow$ Account Servicer C: `pac.008`
8.  Account Servicer C $\rightarrow$ Account Servicer B: `camt.053`
9.  Account Servicer C $\rightarrow$ Customer (Right): `camt.053`

---

**Description:**
Role of the Creditor Agent and Creditor in the payment changes by description in the Bank to Customer Statement message to Account Servicer and Account Owner. Whereby the statement is send by the Account Servicer to the Account Owner and or authorised party. This message is used to inform the account owner, or authorised party, of the entries

---

<!-- Page 580 -->

Like the legacy MT Statement messages, the camt.053 Bank to Customer Account Statement is constrained in CBPR+ by the FINplus service's message size. Account Owner who needs to translate the camt.053 into the legacy MT 940 format has several considerations for the Account Serving Institution.

| **ISO 20022 message element** | **MT Field Name & (Tag option)** |
|---|---|
| Statement Identification | needed to create MT 940 Field 20 Transaction Reference Number |
| Legal Sequence Number | needed to create MT 940 Field 28C Statement Number |
| Statement Pagination | needed to create MT 940 Field 28C Sequence Number |
| Account (Identification) | needed to create MT 940 Field 25a Account Identification |
| Balance Type<br>OPBD (with no *Sub Type* INTM)<br>OPBD (with *Sub Type* INTM) | needed to create MT 940 Field 60F (first) Opening Balance<br>needed to create MT 940 Field 60M (intermediate) Opening Balance |
| Entry | used to create MT 940 Field 61 Statement Line<br>🔍 Note up to **190 Entry** occurrences will translate into a basic MT 940 (inside of the existing MT 940 message size) |
| Balance Type<br>CLBD (with no *Sub Type* INTM)<br>CLBD (with *Sub Type* INTM) | needed to create MT 940 Field 62F (final) Closing Balance<br>needed to create MT 940 Field 62M (intermediate) Closing Balance |

---

<!-- Page 581 -->

Interest rate changes on an account can be communicated using the camt.053. An Account Serving Institution who is considering the camt.053 to communicate such rate changes to the Account Owner may find the following comparison against the legacy MT 935 useful. However, compared the camt.053 to legacy MT, using the camt.053 is like combining the information of both the MT 935 and MT 940 together into one message.

**MT**

MT Field Name & (Tag option)

➔ **Transaction Reference Number** (Field 20)

➔ **Further Identification** (Field 13C) `NOT MAPPED`

➔ **Account Identification** (Field 25)

➔ **Effective Date of New Rate** (Field 30)

➔ **New Interest Rate** (Field 37F)

➔ **Sender To Receiver Information** (Field 72) `NOT MAPPED`

**ISO**

ISO 20022 message element

➔ **Group Header / Message Identification**

➔ **Statement / Account / Identification**

➔ **Statement / Interest / From Date**

➔ **Statement / Interest / Rate**

*Note - various other elements are mandatory in the camt.053 which are not derived from the payment instruction including : Message Identification, Creation Date Time, Statement Identification, Statement Pagination, Balance, Credit Debit Indicator, Status, Bank Transaction Code, ... often these data elements and potentially other optional elements will be generated by the bank application when creating the reporting message.*

---

<!-- Page 582 -->

# Group Header

---

<!-- Page 583 -->

Each ISO 20022 cash management reporting message has a *Message Identification* element, located in the Group Header. This **35 character** identifier is a point-to-point reference used to unambiguously identify the message.

For Cash Management (camt) messages the *Message Identification* has no exact equivalent in the legacy MT Customer Statement message. However, the *Transaction Reference Number* (Field 20) could be considered a similar comparison.

Group Header > Message Identification

---

<!-- Page 584 -->

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+-hh:mm
> For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

Group Header Creation Date Time

---

<!-- Page 585 -->

Min 0 – Max 1

The Bank to Customer Statement **_Message Recipient_** nested element provides details of the party authorised by the _Account Owner_ to receive the Account Statement.

This element **should** _only_ be used to identify the _Message Recipient_ when different from the account owner, which is implied by the usage of **COPY** in the _Copy Duplicate Indicator_ within the nested Statement element.

Where **_Message Recipient_** is used the nested:

*   **Name** Min 0 – Max 1
*   **Postal Address** Min 0 – Max 1
*   **Identification** Min 0 – Max 1
*   **Contact Details** Min 0 – Max 1

may be used to capture information related to this party.

Group Header ⓘ Message Recipient ✓
Name

---

<!-- Page 586 -->

The Bank to Customer Statement **Original Business Query** `Min 0 – Max 1` element identifies a query to generate a report, for example a camt.060 Account Reporting Request.

Where **Original Business Query** is used the original **Message identification** `Min 1 – Max 1` (i.e., the message identification of the camt.060 message) is required. Original **Message Name identification** `Min 0 – Max 1` and Original **Creation Date Time** `Min 0 – Max 1` may also be provided.

Group Header > Original Business Query >
Message Identification

---

<!-- Page 587 -->

Min 0 – Max 1

The Bank to Customer Statement **Additional Information** element represents further details related to the account statement.

Where the camt.053 is used for various end of cycle statement reporting (statement periods) the follow codes may be used to distinguish the different camt.053 usage:
/EODY/ for End of Day - Daily Statement
/EOWK/ for End of Week - Weekly Statement
/EOMH/ for End of Month - Monthly Statement
/EOYR/ for End of Year - Yearly Statement

Additional Information is a textual element restricted in CBPR+ to 500 characters.

Group Header > Additional Information

---

<!-- Page 588 -->

# Statement

---

<!-- Page 589 -->

Min 1 – Max 1

The Bank to Customer Account Statement **_Statement_** nested element reports information related to an account, most typically associated with account balances, and accounting entries (where entries have been processed on the account).

The *Statement* element has been restricted to one statements. To report additional account statements to the Account Owner this would need to occur via a separate message in a similar way to the legacy MT 940 or MT 950.

It should also be noted the Account Statement message is modelled identically to the Account Report (camt.052) therefore where an intraday transaction report is used the content can be capture identically to the statement at the close of the business day, in

Statement

---

<!-- Page 590 -->

Similar to the legacy MT Statement messages the camt.053 Bank to Customer Account Statement is constrained in CBPR+ by the FINplus service's message size. Consideration therefore need to be given to identifying; **the statement order**, **the statement correlation** and the **last statement page**.

1. camt.053
2. camt.053
3. camt.053

**1**

**Statement Pagination**
Page 1
Last Page **No**
Electronic Sequence Number **16**
Legal Sequence Number **3**
Account
Id **12345**
Currency **EUR**
Balance
**OPBD** (Opening Booked)
**CLBD** (Closing Booked)
Sub Type **INTM** (Interim)

**2**

**Statement Pagination**
Page 2
Last Page **No**
Electronic Sequence Number **16**
Legal Sequence Number **3**
Account
Id **12345**
Currency **EUR**
Balance
**OPBD** (Opening Booked)
Sub Type **INTM** (Interim)
**CLBD** (Closing Booked)
Sub Type **INTM** (Interim)

**3**

**Statement Pagination**
Page 3
Last Page **Yes**
Electronic Sequence Number **16**
Legal Sequence Number **3**
Account
Id **12345**
Currency **EUR**
Balance
**OPBD** (Opening Booked)
Sub Type **INTM** (Interim)
**CLBD** Closing Booked

**Statement Order:** identifying the order in which statements should be processed or reconstituted. Options:
Statement Pagination

**Statement Correlation:** identifying statement which relate to each other for a given statement period. Options:
Legal Sequence Number

**Last Statement:** identifying when no further statements for a given period are expected i.e. period statement in finalised. Options:
Statement Pagination, Last Page Indicator

---

<!-- Page 591 -->

Min 1 – Max 1

The Bank to Customer Statement message ***Identification*** provides a mandatory element to identify the statement

Unique reference assigned by the account servicer to unambiguously identify the account statement. Directly comparable with the *Transaction Reference Number* (Field 20) of the legacy MT statement message.

Statement Identifier

---

<!-- Page 592 -->

The Bank to Customer Statement message *Statement Pagination* element provides the page number of the statement.

`Min 1 – Max 1`

*Statement Pagination* includes the `Min 1 – Max 1` *Page Number* and `Min 1 – Max 1` *Last Page indicator* elements.

**For example** a *Page Number* of 2 represents the current account statement, being the second page of the and implying a previous account statement page had been sent. The *Last Page indicator* further implies whether more pages are expected

Note: Where Page Number is equal to 1 a Balance Type OPBD (Opening Booked) must be provided, without a sub type of INTM (Interim). Whereas if the Page Number is greater than 1 a Balance Type OPBD (Opening Booked) must be provided, with a sub type of INTM (Interim).
Where Last Page Indicator is true a Balance Type CLBD (Closing Booked) must be provided, without a sub type of INTM (Interim). Whereas if the Last Page Indicator is false a Balance Type CLBD (Closed Booked) must be provided, with a sub type of INTM (Interim).

---

<!-- Page 593 -->

Min 0 – Max 1
The Bank to Customer Statement message **Electronic Sequence Number** allows the *Account Servicer* to assign a number to each statement which should increment by 1 for each electronic statement report sent.

1.3.2.4.5
This element allows easy recognition of the statement order, equivalent to the legacy Field 28C Statement Number. The sequence should increment for each camt.053 electronic statement sent to the Account Owner or Authorised Party this number must be the same value where the statement continues over multiple pages (*Statement Pagination*) of the statement for a give account on a given day.

Should this sequence number be reset by the *Account Servicer*, this should not occur more frequently than once a year. Likewise, this 18 digit counter could be incremented to its maximum value before it's reset.

The use of Electronic Sequence Number and the sequence reset logic should be bilaterally agreed been the *Account Servicer* and the *Account Owner*.
Either **Electronic Sequence Number** or **Legal Sequence Number**

---

<!-- Page 594 -->

The Bank to Customer Statement message *Reporting Sequence* specifies the choice of identification sequences. This can be used as an alternative to the **Statement Pagination** or **Electronic Sequence Number** as a way to identify the statement order, which is not confined to numeric values.

Where used the *Reporting Sequence* mandate a choice of nested element:

- *From Sequence* identifies the start of a sequence range. `Min 1 – Max 1`
- *To Sequence* identifies the end of a sequence range. `Min 1 – Max 1`
- *From To Sequence* identifies the start and end of a sequence range. `Min 1 – Max*`
- *Equal Sequence* identifies a sequence. `Min 1 – Max*`
- *Not Equal Sequence* identifies a sequence to be excluded. `Min 1 – Max*`

The Reporting Sequence may be provided in the camt.060 Account Reporting request to specify, for example, a range of Statements to be sent. More traditionally Account Statements are generated automatically on an end of day cycle.

---

<!-- Page 595 -->

Min 0 – Max 1

The Bank to Customer Statement message ***Legal Sequence Number*** allows the ***Account Servicer*** to assign a number to each statement which should increment by 1 for each statement report sent.

Where the statement is reported using multiple camt.053 messages for a given statement period the ***Legal Sequence Number*** must be the same number in each statement message, as it can be used to correlate the statements.
Where a paper statement is a legal requirement, it may have a number different from the electronic sequential number. In this case the ***Legal Sequence Number*** element represents the sequence number of the paper statement.

Either ***Electronic Sequence Number*** or ***Legal Sequence Number*** must be provided to enable the identification of a statement number.

Statement > Legal Sequence Number

---

<!-- Page 596 -->

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset **YYYY-MM-DDThh:mm:ss.sss+/-hh:mm**
> For example: **2002-10-10T12:00:00-05:00** (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

Statement Creation Date Time

---

<!-- Page 597 -->

The Bank to Customer Statement message *From to Date* `Min 0 - Max 1` allows the Account Servicer to specify the start date time and end date time applicable to the statement.
Where *From to Date* is used the **From Date Time** `Min 1 - Max 1` and **To Date Time** `Min 1 - Max 1` become mandatory elements.

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+-hh:mm
➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- Page 598 -->

Min 0 – Max 1

The Bank to Customer Statement message ***Copy Duplicate Indicator*** is used as a choice to identify additional statement from the original sent to the Account Owner.

**COPY** is used when a copy of the statement is sent to an Authorised Third Party, such as a company head office, parent entity, or an institution providing additional service such as liquidity sweeping or statement consolidation.

**DUPL** is used when a duplicate of the statement is sent to the Account Owner, this resubmission may have been requested using the camt.060 or an alternative channel such as via internet banking or customer service request.

**CODU** is used when a duplicate of a statement copy is sent to an Authorised Third Party, this resubmission may have been requested using the camt.060 or an alternative channel such as via internet banking or customer service request. It may also be requested by the Account Owner on behalf of the Authorised Third Party, depending on the arrangement in place with the Account Servicer.

---

<!-- Page 599 -->

The Bank to Customer Statement message **Reporting Source** allows the *Account Servicer* to define the source of the statement, typically associated with an application.

Min 0 – Max 1

**Reporting Source** utilises the external Reporting Source code list. For example **ACCT** represents a statement or report based on accounting data, whereas **DEPT** represents a cash or deposit system.
Where the source of the statement is functionally required by the consumer of the statement i.e., the *Account Owner* or *Authorised Third Party*, the codes used should be bilaterally agreed.

---

<!-- Page 600 -->

The Bank to Customer Statement message **Account** provides nested elements to identify the account for which debit and credit entries have been made. The following two mandatory elements are nested beneath *Account*.

| Element | Description |
| :--- | :--- |
| **Identification** (Min 1 – Max 1) | a unique **Identification** for the account, between the Account Servicer and Account Owner. The element is further nested by choice of *IBAN* or *Other* to capture the account. |
| **Currency** (Min 1 – Max 1) | The **Currency** for which the account is held. This is identified using the three characters *ISO currency code*. |

**Account**

Statement > Account

---

<!-- Page 601 -->

Min 1 – Max 1

Min 0 – Max 1

The Bank to Customer Statement message mandatory **Account** also provides a number of optional nested element to identify the account for which debit and credit entries have been made.

**Account**

**Type**

An element which may either use an external ISO **Cash Account Type code** or a proprietary code. It is used to identify a particular type of account.

**Name**

The Name of the Account, as Assigned by the servicing institution.

**Proxy**

A nested element which contains a Proxy Identifier together with the Proxy Type represented by either use an external ISO **Proxy Account Type code** or a proprietary code.

**Owner**

A nest element that contains the Party that legally owns the account.

**Servicer**

A nested element which identifies the Financial Institution who manages

---

<!-- Page 602 -->

Min 0 – Max 1
The Bank to Customer Statement message *Related Account* allows the identification of a related parent account for the account statement. For example, sweeping, pooling or virtual account for which the statement is produced can identify the parent account they hierarchically relate to.

When *Related Account* is utilized, like *Account*, the *Identification* (Min 1 – Max 1) and *Currency* (Min 1 – Max 1) element become mandatory. Additionally the nested *Type* (Min 0 – Max 1) element, *Name* (Min 0 – Max 1) and nested *Proxy* (Min 0 – Max 1) element are optionally available.

*Related Account* uses a variety of common elements described in more detail within the *Account* section.

Statement > Related Account > Identification > Type

---

<!-- Page 603 -->

Min 0 – Max *

The Bank to Customer Statement message **Interest** provides interest information that applies to the account.

**Interest**

- **Type**
  An element which may either use an embedded ISO **Interest Type code**: **INDY** (Intraday) **OVRN** (Over Night) or a proprietary code. It is used to identify a particular interest type.

- **Rate**
  The type of interest Rate defined as a *Percentage* and in an *Other* form. Validity Range optionally defines an *Amount*, *Credit Debit Indicator* and *Currency*.

- **From To Date**
  The date range for which interest has been calculated. *From Date Time* and *To Date Time* must be representing when using this element.

- **Reason**
  The optional Reason for which interest is applied.

- **Tax**
  Provides details on any tax applied to the Interest. Where optional Identification and calculation details will follow the Rate.

---

<!-- Page 604 -->

The Bank to Customer Statement message mandatory `Min 1 – Max *` **Balance** provides nested element to define the account balance at a specific point in time. The following four elements nested beneath *Balance* are mandatory `Min 1 – Max 1`

- **Type**
  A nested element which may either use an external ISO *Balance Type code* or a proprietary code. For example, OPAV – Opening Available. Additionally, a Sub Type represented by either use an external ISO *Balance Sub Type code* or a proprietary code, may be used.
  > *Balance Sub Type code INTM is essential for identifying opening and closing balances in a statement sent over more than one message.*

- **Amount**
  Balance amount.

- **Credit Debit Indicator**
  Embedded code CRDT (Credit balance) DBIT (Debit balance)

- **Date**
  A nested element representing the *Date* and the *DateTime* (with UTC offset) of the balance.

---

<!-- Page 605 -->

*Balance Type* code are used within the nested *Balance* element to represent the type/s of balance being reported. In comparison the legacy MT 940 utilizes different Fields and Tag options to represent a number of these Balance Types. The below extract from the externalised ISO *Balance Type* code list compares the code with the population of the equivalent information in the Legacy MT 940 Customer Statement.

| Code | Sub Type | Name | Definition | MT 940 Comparison |
| :--- | :--- | :--- | :--- | :--- |
| **CLAV** | | *ClosingAvailable* | Closing balance of amount of money that is at the disposal of the account owner on the date specified. | Field 64 |
| | | *ClosingBooked* | Balance of the account at the end of the pre-agreed account reporting period. It is the sum of the opening booked balance at the beginning of the period and all entries booked to the account during the pre-agreed account reporting period. | Field 62F |
| **CLBD** | *INTM* | *ClosingBooked (Interim)* | Interim Balance of the account at the end of the pre-agreed account reporting page. It is the sum of the opening booked balance at the beginning of the period and all entries booked to the account during the pre-agreed account reporting page. | Field 62M |
| **FWAV** | | *ForwardAvailable* | Forward available balance of money that is at the disposal of the account owner on the date specified. | Field 65 |
| **INFO** | | *Information* | Balance for informational purposes. | No equivalent |
| **ITAV** | | *InterimAvailable* | Available balance calculated in the course of the account service's business day, at the time specified, and subject to further changes during the business day. The interim balance is calculated on the basis of booked credit and debit items during the calculation time/period specified. | No equivalent |
| **ITBD** | | *InterimBooked* | Balance calculated in the course of the account service's business day, at the time specified, and subject to further changes during the business day. The interim balance is calculated on the basis of booked credit and debit items during the calculation time/period specified. | No equivalent |
| **OPAV** | | *OpeningAvailable* | Opening balance of amount of money that is at the disposal of the account owner on the date specified. | No equivalent |
| **OPBD** | | *OpeningBooked* | Book balance of the account at the beginning of the account reporting period. It always equals the closing book balance from the previous report. | Field 60F |
| | *INTM* | *OpeningBooked (Interim)* | Interim Book balance of the account at the beginning of the account reporting page. It always equals the closing book balance from the previous report page. | Field 60M |
| **PRCD** | | *PreviouslyClosedBooked* | Balance of the account at the previously closed account reporting period. The opening booked balance for the new period has to be equal to this balance. | |
| | | | Usage: the previously booked closing balance should equal (inclusive date) the booked closing balance of the date it references and equal the actual booked opening balance of the current date. | Field 60F |

---

<!-- Page 606 -->

The Bank to Customer Statement message mandatory **Balance** `Min 1 – Max *` also provides the optional set of nested element to define a **Credit Line** `Min 0 – Max *`

> The true/false Boolean of *Included* to clearly determine whether the Credit Line Amount is included in the balance is mandatory in the set of Credit Line element.

Additionally, the following optional nested element may be used to identify:
- The **Type** of Credit Line, which may either use an external ISO **Credit Line Type code** or a proprietary code.
- A set of elements to provide **Credit Line** details
- The **Amount** (Currency and Amount) of the Credit Line
- The **Date** (nested as Date, DateTime) of the Credit Line, provided to distinguish where multiple Credit Line exist.

The final optional nested element within **Balance** is the **Availability** of the booked amount i.e., when it is available to be accessed.

> 🔍 The *Credit Line* element is unlimited (Max *) whereby more that one *Credit Line* may be reported, the *Date* becomes an important element to distinguish between different Credit Lines.

**Path:** Statement > Balance
- Type
- Credit Line
  - Amount

---

<!-- Page 607 -->

Min 0 – Max 1

The Bank to Customer Statement message optional **Transaction Summary** provides a set of nested element to summarize entry information. Where the statement is reported using multiple camt.053 messages for a given statement period the *Transaction Summary* should only be included on the opening Statement message (*Balance Type* OPBD with no *Balance Sub Type*) summarizing the whole Statement Report (entire statement period) This aligns with the Common Global Implementation (CGI) where a *Transaction Summary*, if provided, would appear before the first *Entry* elements.

Min 0 – Max *

Each of the following element allow an optional total of entries either as a **Number of Entries** and or as a **Sum**.

- Total Entries
- Total Credit Entries
- Total Debit Entries
- Total Entries Per Bank Transaction Code

Min 1 – Max 1

In addition to the **Number of Entries** and **Sum**, the **Total Entries Per Bank Transaction Code** requires the **Bank Transaction Code** element and optionally allows a variety of other optional elements.

Statement > Transaction Summary >

The **Total Entries Per Bank Transaction Code** element is unlimited (Max *) whereby more that one *Bank Transaction Code* may be summarised.

Total Entries >
Total Credit Entries >
Total Debit Entries >

---

<!-- Page 608 -->

The Bank to Customer Statement message optional **Entry** provides a significant variety of nested elements to represent the details associated with each *Entry*. For active accounts which have entries posted across them, this set of nested elements is arguably the most relevant for the account owner and in many way is comparable with the MT 940 Field 61 Statement Line.

Unlike the legacy MT Statement messages, the camt.053 has a number of dedicated elements to capture a variety of entry level data. It also has a number of enhancements on the legacy MT Statement message where parties in the payment and customer remittance information, as examples, can provided to the *Account Owner*.

| Min 0 – Max * | Min 1 – Max 1 | Min 1 – Max 1 | Min 0 – Max 1 | Min 1 – Max 1 |
|:---:|:---:|:---:|:---:|:---:|
| **Entry Reference** | **Amount** | **Credit Debit Indicator** | **Reversal Indicator** | **Status** |
| Min 0 – Max 1 | Min 1 – Max 1 | Min 0 – Max 1 | Min 0 – Max * | Min 1 – Max 1 |
| **Booking Date** | **Value Date** | **Account Servicer Reference** | **Availability** | **Bank Transaction Code** |
| Min 0 – Max 1 | Min 0 – Max 1 | Min 0 – Max 1 | Min 0 – Max 1 | Min 0 – Max 1 |
| **Commission Waiver Indicator** | **Additional Information Indicator** | **Amount Details** | **Charges** | **Technical Input Channel** |
| Min 0 – Max 1 | Min 0 – Max 1 | Min 0 – Max * | Min 0 – Max 1 | |
| | | | **Additional** | **Statement Entry** |

---

<!-- Page 609 -->

**Min 0 - Max 1**
**Entry Reference**
Unique reference for the booking entry, created by the Account Servicing Institution as a reference they assign to identify the entry posted to the account.

**Min 1 - Max 1**
**Amount**
Mandatory element representing the currency and amount of the entry. This can be compared to Field 61 subfield 4 and 5 of the legacy MT 940.
Amount element within CBPR+ allows up to 18 digits unlike the payment messages. It allows entries reported for non CBPR+ transactions to be reported.

**Min 1 - Max 1**
**Credit Debit Indicator**
Mandatory element indicating whether the **Amount** entry is a **DBIT** (Debit) or **CRDT** (Credit) to the account. This can be compared to Field 61 subfield 3 of the legacy MT 940.

**Min 0 - Max 1**
**Reversal Indicator**
Indicates whether the entry is a result of a reversal. for example, an entry related to a pacs.004 Payment Return or reverses an error such as an incorrect value date applied to the entry. Where the **Reversal Indicator** is **Yes**, the **Credit Debit Indicator** should be the opposite of the original entry, for example original **Credit Debit Indicator** of **CRDT** would expect a reversal entry **Credit Debit Indicator** of **DBIT**. This can be compared to Field 61 subfield 3 of the legacy MT 940

---

<!-- Page 610 -->

**Status** *(Min 1 – Max 1)*

Mandatory element representing the status using an external ISO *Entry Status* code for example **BOOK** is used to confirm the entry is booked.

> Status **BOOK** is the only status that can be reversed using the *Reverse Indicator*

**Booking Date** *(Min 0 – Max 1)*

Mandatory choice of *Date* or *Date Time* the entry was posted to the **Account**. This can be compared to Field 61 subfield 2 of the legacy MT 940.

**Value Date** *(Min 1 – Max 1)*

Mandatory choice of *Date* or *Date Time* the entry become available. This can be compared to Field 61 subfield 1 of the legacy MT 940.

> Noting CBPR+ usage guidelines mandate the time zone that the *Date Time* represents as an offset against Universal Time Coordinated (UTC)

**Account Servicer Reference** *(Min 0 – Max 1)*

Additional optional Reference typically assigned by the Account Servicer's payment engine or accounting platform. This reference would be used to query an entry. This can be compared to Field 61 subfield 8 of the legacy MT 940.

**Availability** *(Min 0 – Max 1)*

Indicates when the booked amount is available i.e., when it is available to be accessed.

---

<!-- Page 611 -->

Min 1 – Max 1
**Bank Transaction Code**

The **Bank Transaction Code** is designed to deliver a harmonized set of codes, which should be applied in bank-to-customer cash account reporting information. The bank transaction code information allows the **account service** to correctly report a transaction, which in its turn will help **account owners** to perform their cash management and reconciliation operations.

Domain
Family
Sub-Family

The structure of the Bank Transaction Code has three levels:
**Domain:** Highest definition level to identify the sub-ledger. The domain defines the business area of the underlying transaction e.g., payment, securities etc.)
**Family:** Medium definition level e.g. type of payment; credit transfer, direct debit etc.
**Sub-family:** Lowest definition level e.g. type of cheques; draft etc.

Bank Transaction Codes are an external code set defined in the *Bank Transaction Code* combinations external code sets.

---

<!-- Page 612 -->

# Payouts Domain Families

| | | | Min 1 – Max 1 |
|---|---|---|---|
| **1.** | **Received Credit Transfers** | Receivable Credit Transfers are instructions to receive an amount of money from a del account owner. The receivable credit transfers are related to transactions received i account owner. | |
| **2.** | **Issued Credit Transfers** | Payable Credit Transfers are instructions to transfer an amount of money by the acco to a creditor. The payable credit transfers are related to instructions sent by the acco account owner. | |
| **3.** | **Received Cash Concentration** | Transaction is related to incoming cash movements that are related to cash management activities initiated by the owner of the sending account to optimise the return on the av funds. | |
| **4.** | **Issued Cash Concentration** | Transaction is related to outgoing cash movements that are related to cash managemen activities initiated by the owner of the account to optimise the return on the available f | |
| **5.** | **Received Direct Debits** | The Received Direct Debit transactions are related to instructions received by the acc to debit the account. | |
| **6.** | **Issued Direct Debits** | The Issued Direct Debit transactions are related to instructions sent by the account own collect an amount o | |
| **7.** | **Received Cheques** | Transaction is rela- from the cheque dr. | **Sub-Families for both Received and Issued Credit Transfers** |
| **8.** | **Issued Cheques** | Transaction is rela- | **Sub-Families for both Received and Issued Credit Transfers** |

| | **Internal Book Transfer** | **Definition** |
|---|---|---|
| | **Standing Order** | Transaction is a standing order – two different accounts within the same bank |
| | **Cross-Border Standing Order** | Transaction is a cross-border standing order |
| | **SEPA Credit Transfer Domestic Credit Transfer** | Transaction is a SEPA credit transfer <br> Transaction is a in-country domestic currency credit transfer |
| | **Cross-Border Credit Transfer** | Transaction is a cross-border credit transfer |
| | **Credit Transfer with agreed Commercial Information** | Transaction is a credit transfer including commercial information, i.e. additional informat agreed between the sender and the receiver. |
| | **Financial Institution Credit Transfer** | Transaction is a financial institution credit transfer, i.e. the debtor and creditor are financi institutions. |
| | **Priority Credit Transfer** | Transaction is a credit transfer defined with higher priority, e.g. a PRIURO credit transfer |
| | **Payroll/Salary Payment** | Transaction is related to the payment of a payroll salary |
| | **Cross-border** | Transaction is related to the payment of a cross-border payroll salary |

The description of **Bank Transaction Codes** are available to download from the ISO20022.org external code list page. These include the descriptions for Payments Domain Families and sub-families for both Received and Issued Credit Transfers.

https://www.iso20022.org/external_code_list_page

---

<!-- Page 613 -->

| **Bank Transaction Code - all permitted combinations of the BTC code sets** | | | | | | | |
|---|---|---|---|---|---|---|---|
| *All codes in light gray are defined as the generic codes available for all Domains and Families* | | | | | | | |
| Domain | Family | SubFamily | DomainCode | FamilyCode | SubFamilyCode | ExampleOfATransactionDomainCode | ExampleOfATransactionFamilyCode | ExampleOfATransactionSubFamilyCode | Status | StatusDate |
| Payments | Issued Credit Transfers | Cross-Border Credit Transfer | PMNT | ICDT | XBCT | | | | New | 27/4/2009 |
| Payments | Received Credit Transfers | Cross-Border Credit Transfer | PMNT | RCDT | XBCT | | | | New | 27/4/2009 |

Bank Transaction Codes are an external code set defined in the *Bank Transaction Code* combinations external code sets.
As an example a debit statement transaction which relates to a cross-border payment initiated from an account would be represented by:

| **Domain** | **Family** | **Sub-Family** |
|---|---|---|
| PMNT (Payment) | ICDT (Issued Credit Transfer) | XBCT (Cross-Border Credit Transfer) |

---

<!-- Page 614 -->

**Min 0 – Max 1**
**Commission Waiver Indicator**
Optional element indicating, as a Boolean, whether the entry is exempt from commission. This element is not typically associated with Correspondent Banking payments

**Min 0 – Max 1**
**Additional Information Indicator**
Optional element indicating whether the underlying transaction details are provided through a separate message. Where the ***Message Name Identification*** represents the message used to provide the additional information and ***Message Identification*** specifies the reference of the message that provides the additional information.

**Min 0 – Max 1**
**Amount Details**
Optional nested element which provides various elements to represent an aggregated (consolidated) original amount. Where individual transaction amounts can be represented, if required, within the ***Entry Detail*** set of elements.
This element is useful to capture original amount details where they are different to the ***Entry Amount***, for example the ***Instructed Amount*** of the payment can be included, together with a potential ***Currency Exchange*** rate, where necessary.

**Min 0 – Max 1**
**Charges**
Optional nested element to provide information on charges either pre-advised or taken from the entry.

---

<!-- Page 615 -->

**Min 0 – Max 1**
**Technical Input Channel**
Optional element which may either use an external ISO **Technical Input Channel code** or a proprietary code used to represent the technical channel used to input the entry.

**Min 0 – Max 1**
***Interest***
Optional nested element detailing any interest accrued as part of an aggregated (consolidated) entry amount.

**Min 0 – Max 1**
**Card Transactions**
Optional nested element which provides details associated with a card transaction such as the card number, card brand etc.

**Min 0 – Max \***
**Entry Details**
Additional optional nested element containing details on the entry. See dedicated section on ***Entry Details***.

**Min 0 – Max 1**
**Additional Statement Information**
Additional optional element to represent further information related to the account statement

---

<!-- Page 616 -->

Min 0 – Max *
The Bank to Customer Statement message optional **_Entry Details_** provides a variety of nested elements to represent the details associated with each **_Entry_**.

**_Batch_** provides details on batched transactions such as the total **_Number of Transactions_** the batched entry (sometimes referred to as a consolidated entry) represents.
**_Transaction Details_** is a significant nested element which represents information on the underlying transaction.

Statement > Entry > Entry Details

---

<!-- Page 617 -->

Min 0 – Max * Min 1 – Max 1
When the Bank to Customer Statement message optional **Entry Details** is utilized the nested **Transaction Details** element is mandatory.

**Transaction Details** has a variety of nested elements closely associated with **Entry** level elements. The **References** element however is nested to include a variety of references related to the entry including for example the **UETR**

| Min 1 – Max 1 | Min 1 – Max 1 | Min 1 – Max 1 | Min 0 – Max 1 | Min 0 – Max * | Min 0 – Max 1 | Min 0 – Max 1 | Min 0 – Max 1 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **References** | **Amount** | **Credit Debit Indicator** | **Amount Details** | **Availability** | **Bank Transaction Code** | **Charges** | **Interest** |

Additionally, **Transaction Details** also has a variety of elements capturing details from the underlying transaction, which amongst other business transactions includes payment transaction data. For example, **Remittance Information** and **Related Parties**

Amount element within CBPR+ allows up to 18 digits unlike the payment messages. It allows entries reported for non CBPR+ transactions to be reported

Statement > Entry > Entry Details > Transaction Details

---

<!-- Page 618 -->

The Bank to Customer Statement message **Related Parties** and **Related Agents** represents a set of optional nested elements related to the underlying transaction. Where the **Entry Details** (the set of elements *Related Parties/Agents belongs to*) relate to a Payment, Clearing and Settlement (pacs) message, parties in the pacs messages can be transferred into the Cash Management (camt) message.

These **Related Parties** include :
*   *Instructing Party*
*   *Debtor*
*   *Debtor Account*
*   *Ultimate Debtor*
*   *Creditor*
*   *Creditor Account*
*   *Ultimate Creditor*

These **Related Agents** include :
*   *Instructing Agent*
*   *Instructed Agent*
*   *Debtor Agent*
*   *Creditor Agent*
*   *Intermediary Agent 1*
*   *Intermediary Agent 2*
*   *Intermediary Agent 3*

**Trading Party** is also present in the *Related Parties* elements, and the following are present in the *Related Agents* elements: **Receiving Agents, Delivering Agent, Issuing Agent and Settlement Place**. Although these elements are not directly associated with a payment, as a Customer receiving a Statement related to other Business Domains e.g. a Security

---

<!-- Page 619 -->

The Bank to Customer Statement message **_Entry Details_** have a number of additional elements beyond **_Related Parties_** and **_Related Agents_** to capture information from the underlying payment.

These are:
*   **_Local Instrument_**
*   **_Purpose_**
*   **_Related Remittance Information_**
*   **_Remittance Information_**
*   **_Related Dates_** such as the **_Interbank Settlement Date_**
*   **_Tax_**

For **_Payment Return_** (pac.004) it is also possible to capture **Return Information** which includes:
*   The **_Original Bank Transaction Code_** of the original Entry
*   The **_Originator_** of the return from the pac.004
*   And the **_Reason_** code.

**_Remittance Information_** as an end-to-end element should be passed unaltered from Payment Initiation (pain) into the Payment, Clearing and Settlement (pac) message and onto the Bank to Customer Account Statement (camt). The **_Remittance Information_** element is common to these message sets

---

<!-- Page 620 -->

It should also be mentioned that the Bank to Customer Statement message *Entry Details* have a number of additional elements which capture information from transactions in other business domains beyond payments, as well as have an element to capture **Additional Transaction Information**.

These are:
- *Related Quantity*
- *Financial Instrument Identification*
- *Corporate Action*
- *Safekeeping Account*
- *Cash Deposit*
- *Card Transactions*

---

<!-- Page 621 -->

> Use case should be considered as a principal example whereby use case may be cross referenced

**Bank to Customer Statements**
Use Case c.53.1.a – Bank to Customer Statement produced by the Creditor Agent
Use Case c.53.1.b – Bank to Customer Statement produced by the Debtor Agent
Use Case c.53.1.c – Bank to Customer Statement produced by an intermediary Agent
**Copy of Bank to Customer Statements**
Use Case c.53.2 – Bank to Customer Statement sent as an additionally copy to an authorised party
**Resent Bank to Customer Statements**
Use Case c.53.3 – Bank to Customer Statement resent a previously sent statement/s to the Account Owner
Use Case c.53.4 – Bank to Customer Statement resent a previously sent copy statement/s to an authorised party
**Forwarding of Bank to Customer Statements**
Use Case c.53.5 – Bank to Customer Statement sent to an authorised party who forward/provides on to the Account Owner (commonly referred to as an account concentrating model)

| | |
|---|---|
| 🚩 Use Case camt.060 for requesting a Bank to Customer statement | 🚩 Use Case for copy or duplicate reports refer to camt.053 use cases |

---

<!-- Page 622 -->

1 → 2 —`pacs.008`→ 3 —`pacs.008`→ 4 —`pacs.008`→ 5 —`camt.053`→ 6

**1**
Debtor initiates a payment instruction to the Debtor Agent

**2**
Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries

**3**
Agent B processes the payment on Agent C

**4**
Agent C processes the payment on Agent D

**5**
Creditor Agent credits the account of the Creditor

**6**
Creditor Agent as the Account Servicer produces and sends a statement to either the Account Owner, or an authorised third party.

---

<!-- Page 623 -->

1 → 2 `pacs.008` → 3 `pacs.008` → 4 `pacs.008` → 5 →

`camt.053` (6)

| # | Description |
|---|-------------|
| 1 | Debtor initiates a payment instruction to the Debtor Agent |
| 2 | Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries |
| 3 | Agent B processes the payment on Agent C |
| 4 | Agent C processes the payment on Agent D |
| 5 | Creditor Agent credits the account of the Creditor |
| 6 | Debtor Agent as the Account Servicer produces and sends a statement to either the Account Owner, or an authorised third party. |

---

<!-- Page 624 -->

[Debtor] (1) → [Agent A] (2) —`pac.008`→ [Agent B] (3) —`pac.008`→ [Agent C] (4) —`pac.008`→ [Agent D] (5) → [Creditor]
[Agent B] (3) —`camt.053`→ (6)

| **1** | **3** | **5** |
|---|---|---|
| Debtor initiates a payment instruction to the Debtor Agent | Agent B processes the payment on Agent C | Creditor Agent credits the account of the Creditor |
| **2** | **4** | **6** |
| Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries | Agent C processes the payment on Agent D | Intermediary Agent as the Account Servicer produces and sends a statement to either the Account Owner, or an authorised third party. |

---

<!-- Page 625 -->

1 $\rightarrow$ 2 $\xrightarrow{\text{pac.008}}$ 3 $\xrightarrow{\text{pac.008}}$ 4 $\xrightarrow{\text{pac.008}}$ 5
5 $\xrightarrow{\text{camt.053}}$ 6
5 $\xrightarrow{\text{camt.053}}$ 7

**1**
Debtor initiates a payment instruction to the Debtor Agent

**2**
Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries

**3**
Agent B processes the payment on Agent C

**4**
Agent C processes the payment on Agent D

**5**
Creditor Agent credits the account of the Creditor

**6**
Creditor Agent as the Account Servicer produces and sends a statement to the Account Owner.

**7**
Creditor Agent as the Account Servicer sends an additional copy of the statement to an authorised third part. COPY is populated in the Copy Duplicate indicates element within the

---

<!-- Page 626 -->

# Account Owner

**Flow:**

1. (Debtor) → 2. (Agent A) → `pac.008` → 3. (Agent B) → `pac.008` → 4. (Agent C) → `pac.008` → 5. (Agent D) → `camt.053` (6) / `camt.053` (8) → 7. (Account Owner / Wallet)

---

**1**
Debtor initiates a payment instruction to the Debtor Agent

**2**
Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries

**3**
Agent B processes the payment on Agent C

**4**
Agent C processes the payment on Agent D

**5**
Creditor Agent credits the account of the Creditor

**6**
Creditor Agent as the Account Servicer produces and sends a statement to the Account Owner.

**7**
Creditor as the Account Owner requests a previously sent statement message/s to be resent to them.

**8**
Creditor Agent as the Account Servicer re-sends a duplicate statement to the account owner. DUPL is populated in the Copy Duplicate Indicator element within the Bank to Customer Statement message (camt.053)

---

<!-- Page 627 -->

# authorised party

1 → 2 —`pac.008`→ 3 —`pac.008`→ 4 —`pac.008`→ 5 → 7
5 → 6 / 8 —`camt.053`→ 7

| 1 | 4 | 7 |
|---|---|---|
| Debtor initiates a payment instruction to the Debtor Agent | Agent C processes the payment on Agent D | Authorised third party requests a previously sent statement message/s to be resent to them. |
| 2 | 5 | 8 |
| Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries | Creditor Agent credits the account of the Creditor | Creditor Agent as the Account Servicer re-sends a duplicate statement to the authorised third party. CDDU is populated in the Copy Duplicate Indicator element within the Bank to Customer Statement message |
| 3 | 6 | |
| Agent B processes the payment | Creditor Agent as the Account Servicer produces and sends a statement to an authorised | |

---

<!-- Page 628 -->

the Account Owner (commonly referred to as an account concentrating model)

1 → 2 (pacs.008) → 3 (pacs.008) → 4 → 5 (camt.053) → 6

1. Debtor initiates a payment instruction to the Debtor Agent
2. Debtor Agent (A) initiates a serial payment towards the Creditor Agent (C) using Agents as an intermediary
3. Agent B processes the payment on Agent C
4. Creditor Agent credits the account of the Creditor
5. Creditor Agent as the Account Servicer produces and sends a statement to an authorised third part.
6. Authorised third part provides statement information to the Account Owner. Which could be the forwarded Camt.053 statement or the details via an alternative channel (e.g. host to host file, GUI etc.)

---

<!-- Page 629 -->

# Bank to Customer Debit Credit Notification

---

<!-- Page 630 -->

camt.054

Group Header

Notification

*The Bank To Customer Debit Credit Notification message is sent by the account servicer to an account owner or to a party authorised by the account owner to receive the message. It can be used to inform the account owner, or authorised party, of single or multiple debit and/or credit entries reported to the account*

The Bank to Customer Debit Credit Notification allows multiple Notifications per InterAct message (100,000 bytes) It is however recommended to report single notifications per transaction. This message must be bilaterally agreed between the Account Servicing Institution and the Account owner, and is establish by an

---

<!-- Page 631 -->

pacs.008
pacs.002
camt.054
camt.054
pacs.008
camt.054
camt.054

Role of the Agent/s, Debtor and Creditor in the payment changes by description in the Bank to Customer Debit Credit Notification message to Account Servicer and Account Owner. Whereby the notification is sent by the Account Servicerto the Account Owner and or authorised party.

---

<!-- Page 632 -->

*The Customer Debit Credit Notification*
are optionally provided between the account servicing institution and the account owner, or authorised (third) party.
These messages:
- are used to inform on debit and/or credit entries reported to an account.
- and may also be complemented by:
  - a *Status Information* message:
    - pacs.002 in Payment Clearing and Settlement, or
    - pain.002 in Payment Initiation.
  - or by a bank statement such as the camt.053 *Bank to Customer Statement Report*

pain.001
pain.002
camt.054
camt.053
camt.054
camt.053
pacs.008/pacs.009
pacs.002
camt.054
camt.053
camt.054
camt.053

---

<!-- Page 633 -->

# Group Header

---

<!-- Page 634 -->

Each ISO 20022 cash management reporting message has a *Message Identification* element, located in the Group Header. This **35 character** identifier is a point-to-point reference used to unambiguously identify the message.

For Cash Management (camt) messages the *Message Identification* has no exact equivalent in the legacy MT Customer Statement message. However the *Transaction Reference Number* (Field 20) could be considered a similar comparison.

Group Header > Message Identification

---

<!-- Page 635 -->

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+-hh:mm
> For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

Group Header Creation Date Time

---

<!-- Page 636 -->

Min 0 – Max 1

The Bank to Customer Debit Credit Notification **_Message Recipient_** nested element provides details of the party authorised by the _Account Owner_ to receive the Debit Credit Notification. This element **should only** be used to identify the _Message Recipient_ when different from the account owner, which is implied by the usage of **COPY** in the _Copy Duplicate Indicator_ within the nested Notification element.

Where **_Message Recipient_** is used the nested:

- **_Name_** Min 0 – Max 1
- **_Postal Address_** Min 0 – Max 1
- **_Identification_** Min 0 – Max 1
- **_Contact Details_** Min 0 – Max 1

May be used to capture information related to this party.

Group Header > Message Recipient
Name

---

<!-- Page 637 -->

The Bank to Customer Debit Credit Notification ***Original Business Query*** `Min 0 – Max 1` element identifies a query to generate a report, for example a camt.060 Account Reporting Request.

Where ***Original Business Query*** is used the original ***Message identification*** `Min 1 – Max 1` (i.e. the message identification of the camt.060 message) is required. Original ***Message Name identification*** `Min 0 – Max 1` and Original ***Creation Date Time*** `Min 0 – Max 1` may also be provided.

Group Header > Original Business Query >
Message Identification

---

<!-- Page 638 -->

The Bank to Customer Debit Credit Notification <span style="background-color: #87CEEB;">Min 0 – Max 1</span> ***Additional Information*** element represents further details related to the account statement.

The camt.054 may be used to indicate a particular type of notification, recognizing all transactions within the notification belong to the type indicated below:

***/LBOX/*** Lock Box

***/BULK/*** Bulk reporting (batch transaction with underlying transaction)

***/RTRN/*** Return report

***/CRED/*** Notification with Credit entries ONLY

Additional Information is a textual element restricted in CBPR+ to 500 characters.

<div align="right">Group Header ⓘ Additional Information</div>

---

<!-- Page 639 -->

# Notification

---

<!-- Page 640 -->

Min 0 – Max *

The Bank to Customer Debit Credit Notification ***Notification*** nested element captures debit and credit entry information for an account.

> 1
>
> The *Notification* element has a couple of options to notify on multiple Debits and or Credits. This can be achieved at either the **Notification** element itself which could principally report on more than one account held by the account owner with the Account Servicer or can be achieved at an **Entry** level.
> Notification of multiple Debits and or Credits is perhaps more associated with a timed or batch creation of the camt.054 Bank to Customer Debit Credit Notification. Whereas the more common example of a real-time notification produced at the point of an account posting would typically notify on a single *Entry*.

Notification ?

---

<!-- Page 641 -->

Min 1 – Max 1

The Bank to Customer Debit Credit Notification message ***Identification*** provides a mandatory element to identify the notification

*Unique reference* assigned by the account servicer to unambiguously identify the account statement. Directly comparable with the *Transaction Reference Number* (Field 20) of the legacy MT statement message.

Statement > Identification

---

<!-- Page 642 -->

Min 0 – Max 1
The Bank to Customer Debit Credit Notification message **Notification Pagination** element provides the page number of the notification.

Min 1 – Max 1    Min 1 – Max 1
Where **Notification Pagination** is used the **Page Number** and **Last Page indicator** elements are both mandatory.
**For example**, a *Page Number* of 2 represents the current account statement, being the second page of the and implying a previous account statement page had been sent. The *Last Page indicator* further implies whether more pages are expected

Either *Message Pagination* (Group Header) or *Notification Pagination* (Notification) may used but not both

---

<!-- Page 643 -->

Min 0 – Max 1

The Bank to Customer Debit Credit Notification message **Electronic Sequence Number** allows the *Account Servicer* to assign a number to each notification which should increment by 1 for each electronic notification report sent.

1 3
2 4
5

As a good practice this element allows easy recognition of the notification order, if not recognisable by other data within the notification, such as the **Notification** > *Identification* element.
Should this sequence number be reset by the *Account Servicer*, this should not occur more frequently than once a year. Likewise, this 18 digit counter could be incremented to its maximum value before it's reset.

The use of Electronic Sequence Number and the sequence reset logic should be bilaterally agreed been the *Account Servicer* and the *Account Owner*

Notification > Electronic Sequence Number

---

<!-- Page 644 -->

The Bank to Customer Debit Credit Notification message `Min 0 – Max 1` ***Reporting Sequence*** specifies the choice of identification sequences. This can be used as an alternative to the ***Statement Pagination*** or ***Electronic Sequence Number*** as a way to identify the statement order, which is not confined to numeric values.

Where used the ***Reporting Sequence*** mandate a choice of nested element:

**A** $\rightarrow$ **B**
$\downarrow$
**D** $\leftarrow$ **C**

*   ***From Sequence*** identifies the start of a sequence range. `Min 1 – Max 1`
*   ***To Sequence*** identifies the end of a sequence range. `Min 1 – Max 1`
*   ***From To Sequence*** identifies the start and end of a sequence range. `Min 1 – Max *`
*   ***Equal Sequence*** identifies a sequence. `Min 1 – Max *`
*   ***Not Equal Sequence*** identifies a sequence to be excluded. `Min 1 – Max *`

Although the Reporting Sequence may be provided in a camt.060 Account Reporting Request, the use of this message to request a Bank to Customer Debit Credit Notification is less compelling, whereby such notifications are typically triggered as the result of an account posting, rather than being requested.

---

<!-- Page 645 -->

Min 0 – Max 1

The Bank to Customer Debit Credit Notification message ***Legal Sequence Number*** allows the ***Account Servicer*** to assign a number to each notification which should increment by 1 for each notification report sent.

1 3
2

In the case of a real-time notification the ***Legal Sequence Number*** element has little value, unlike its use in a statement message.

Notification > Legal Sequence Number

---

<!-- Page 646 -->

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
> For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

Notification Creation Date Time

---

<!-- Page 647 -->

The Bank to Customer Debit Credit Notification message `Min 0 - Max 1` ***From to Date*** allows the *Account Servicer* to specify the start date time and end date time applicable to the notification.
Where ***From to Date*** is used the ***From Date Time*** `Min 1 - Max 1` and ***To Date Time*** `Min 1 - Max 1` become mandatory elements.

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
➢ For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- Page 648 -->

Min 0 – Max 1

The Bank to Customer Debit Credit Notification message ***Copy Duplicate Indicator*** is used as a choice to identify additional notification from the original sent to the Account Owner.

**COPY** is used when a copy of the notification is sent to an Authorised Third Party, such as a company head office, parent entity, or an institution providing additional service such as liquidity sweeping or statement consolidation.

**DUPL** is used when a duplicate of the notification is sent to the Account Owner, this resubmission may have been requested using the camt.060 or an alternative channel such as via internet banking or customer service request.

**CODU** is used when a duplicate of a notification copy is sent to an Authorised Third Party, this resubmission may have been requested using the camt.060 or an alternative channel such as via internet banking or customer service request. It may also be requested by the Account Owner on behalf of the Authorised Third Party, depending on the arrangement in place with the Account Servicer.

---

<!-- Page 649 -->

Min 0 – Max 1

The Bank to Customer Debit Credit Notification message **Reporting Source** allows the *Account Servicer* to define the source of the notification, typically associated with an application.

**Reporting Source** utilizes the external Reporting Source code list. For example, **ACCT** represents a notification based on accounting data, whereas **DEPT** represents a cash or deposit system.
Where the source of the notification is functionally required by the consumer of the notification i.e., the *Account Owner* or *authorised Third Party*, the codes used should be bilaterally agreed.

---

<!-- Page 650 -->

Min 1 – Max 1
The Bank to Customer Debit Credit Notification message **Account** provides nested elements to identify the account for which debit and credit entries have been made. The following two mandatory elements are nested beneath *Account*.

Min 1 – Max 1
**Identification** a unique *Identification* for the account, between the Account Servicer and Account Owner. The element is further nested by choice of *IBAN* or *Other* to capture the account.

Min 1 – Max 1
The **Currency** for which the account is held. This is identified using the three characters *ISO currency code*.

| Account | Identification | Currency |
|---|---|---|
| | | |

---

<!-- Page 651 -->

The Bank to Customer Debit Credit Notification message mandatory **Min 1 – Max 1** *Account* also provides a number of optional nested element to identify the account for which debit and credit entries have been made.

**Min 0 – Max 1**

*Account*

- *Type*: An element which may either use an external ISO **Cash Account Type code** or a proprietary code. It is used to identify a particular type of account.
- *Name*: The Name of the Account, as Assigned by the servicing institution.
- *Proxy*: A nested element which contains a Proxy Identifier together with the Proxy Type represented by either use an external ISO **Proxy Account Type code** or a proprietary code.
- *Owner*: A nest element that contains the Party that legally owns the account.

---

<!-- Page 652 -->

Min 0 – Max 1
The Bank to Customer Debit Credit Notification message **Related Account** allows the identification of a related parent account for the account notification. For example sweeping, pooling or virtual account for which the notification is produced can identify the parent account they hierarchically relate to.

Min 1 – Max 1    Min 1 – Max 1
When **Related Account** is utilized, like **Account**, the **Identification** and **Currency**
element become mandatory.
Additionally, the nested **Type** element, **Name** and nested **Proxy** element are optionally
Min 0 – Max 1    Min 0 – Max 1    Min 0 – Max 1
available.

*Related Account* uses a variety of common elements described in more detail
within the *Account* section.

Notification > Related Account
Identification
Type

---

<!-- Page 653 -->

The Bank to Customer Debit Credit Notification message `Min 0 - Max *` **Interest** provides interest information that applies to the account. Inclusion of such interest information is perhaps more common to the camt.053 Statement than a Debit Credit Notification.

**Interest**

- **Type** — An element which may either use an embedded ISO *Interest Type code*; **INDY** (Intraday) **OVRN** (Over Night) or a proprietary code. It is used to identify a particular interest type.

- **Rate** — The type of interest Rate defined as a *Percentage* and in an *Other* form. Validity Range optionally defines an *Amount*, *Credit Debit Indicator* and *Currency*.

- **From To Date** — The date range for which interest has been calculated. *From Date Time* and *To Date Time* must be representing when using this element.

- **Reason** — The optional Reason for which interest is applied.

- **Tax** — Provides details on any tax applied to the Interest. Where optional

---

<!-- Page 654 -->

Min 0 – Max 1
The Bank to Customer Debit Credit Notification message optional **_Transaction Summary_** provides a set of nested element to summarize entry information. More commonly the Bank to Customer Debit Credit Notification is reporting a single Debit or Credit transaction, where understandably the use of Transaction Summary provides little value.

Each of the following element allow an optional total of entries either as a **_Number of Entries_** and or as a **_Sum._**
➢ **Total Entries**
➢ **Total Credit Entries**
➢ **Total Debit Entries**
➢ **Total Entries Per Bank Transaction Code**

Min 0 – Max *
In addition to the **_Number of Entries_** and **_Sum,_** the **_Total Entries Per Bank Transaction Code_** requires the **_Bank Transaction Code_** Min 1 – Max 1 element and optionally allows a variety of other optional elements.

Notification > Transaction Summary >
Total Entries >
Total Credit Entries >
Total Debit Entries >

The **_Total Entries Per Bank Transaction Code_** element is unlimited (Max *) whereby more that one **_Bank Transaction Code_** may be summarised.

---

<!-- Page 655 -->

The Bank to Customer Debit Credit Notification message optional **Entry** provides a significant variety of nested elements to represent the details associated with each Debit or Credit **Entry**.

Unlike the legacy MT 900 MT 910 confirmation messages, the camt.054 has a number of dedicated elements to capture a variety of entry level data. It also has a number of enhancements on the legacy MT confirmation message where parties in the message and customer remittance information, as examples, can provided to the *Account Owner*.

| Min 0 – Max 1 | Min 1 – Max 1 | Min 1 – Max 1 | Min 0 – Max 1 | Min 1 – Max 1 |
|:---:|:---:|:---:|:---:|:---:|
| **Entry Reference** | **Amount** | **Credit Debit Indicator** | **Reversal Indicator** | **Status** |
| Min 0 – Max 1 | Min 0 – Max 1 | Min 0 – Max 1 | Min 0 – Max * | Min 1 – Max 1 |
| **Booking Date** | **Value Date** | **Account Servicer Reference** | **Availability** | **Bank Transaction Code** |
| Min 0 – Max 1 | Min 0 – Max 1 | Min 0 – Max 1 | Min 0 – Max 1 | Min 0 – Max 1 |
| **Commission Waiver Indicator** | **Additional Information Indicator** | **Amount Details** | **Charges** | **Technical Input Channel** |
| Min 0 – Max 1 | Min 0 – Max 1 | Min 0 – Max * | Min 0 – Max 1 | |
| | | | **Additional** | **Notification** ... **Entry** |

---

<!-- Page 656 -->

**Min 0 - Max 1**
**Entry Reference**
Unique reference for the booking entry, created by the Account Servicing Institution as a reference they assign to identify the entry posted to the account.

**Min 1 - Max 1**
**Amount**
Mandatory element representing the currency and amount of the entry. This can be compared to Field 32A of the legacy MT 900 and MT 910.

**Min 1 - Max 1**
**Credit Debit Indicator**
Mandatory element indicating whether the *Amount* entry is a **DBIT** (Debit) or **CRDT** (Credit) to the account.

**Min 0 - Max 1**
**Reversal Indicator**
Indicates whether the entry is a result of a reversal. for example, an entry related to a pacs.004 Payment Return or reverses an error such as an incorrect value date applied to the entry. Where the *Reversal Indicator* is **Yes**, the *Credit Debit Indicator* should be the opposite of the original entry, for example original *Credit Debit Indicator* of **CRDT** would expect a reversal entry *Credit Debit Indicator* of **DBIT**

---

<!-- Page 657 -->

**Min 1 – Max 1**
**Status**

Mandatory element representing the status using an external ISO ***Entry Status*** code for example BOOK is used to confirm the entry is booked.

> **Status BOOK is the only status that can be reversed using the *Reverse Indicator***

**Min 0 – Max 1**
**Booking Date**

Mandatory choice of ***Date*** or ***Date Time*** the entry was posted to the ***Account***.

**Min 0 – Max 1**
**Value Date**

Mandatory choice of ***Date*** or ***Date Time*** the entry become available. This can be compared to Field 32A of the legacy MT 900 and MT 910.

> Noting CBPR+ usage guidelines mandate the time zone that the ***Date Time*** represents as an offset against Universal Time Coordinated (UTC)

**Min 0 – Max 1**
**Account Servicer Reference**

Additional optional Reference typically assigned by the Account Servicer's payment engine or accounting platform. This reference would be used to query an entry.

**Min 0 – Max \***
**Availability**

Indicates when the booked amount is available i.e., when it is available to be accessed.

---

<!-- Page 658 -->

Min 1 – Max 1
**Bank Transaction Code**

The **Bank Transaction Code** is designed to deliver a harmonized set of codes, which should be applied in bank-to-customer cash account reporting information. The bank transaction code information allows the **account service** to correctly report a transaction, which in its turn will help **account owners** to perform their cash management and reconciliation operations.

Domain
Family
Sub-Family

The structure of the Bank Transaction Code has three levels:
**Domain:** Highest definition level to identify the sub-ledger. The domain defines the business area of the underlying transaction e.g., payment, securities etc.)
**Family:** Medium definition level e.g. type of payment; credit transfer, direct debit etc.
**Sub-family:** Lowest definition level e.g. type of cheques; draft etc.

Bank Transaction Codes are an external code set defined in the *Bank Transaction Code* combinations external code sets.

---

<!-- Page 659 -->

# descriptions

| | | **Pay-out Domain Families** | | **Min 1 – Max 1** |
|---|---|---|---|---|
| 1. | Received Credit Transfers | Receivable Credit Transfers are instructions to receive an amount of money from a del account owner. The receivable credit transfers are related to transactions received 1 account owner. | | The description of **Bank Transaction Codes** are available to download from the ISO20022.org external code list page. These include the descriptions for Payments Domain Families and sub-families for both Received and Issued Credit Transfers. |
| 2. | Issued Credit Transfers | Payable Credit Transfers are instructions to transfer an amount of money by the acco to a creditor. The payable credit transfers are related to instructions sent by the accoun | |
| 3. | Received Cash Concentration | Transaction is related to incoming cash movements that are related to cash management activities initiated by the owner of the sending account to optimise the return on the av funds. | |
| 4. | Issued Cash Concentration | Transaction is related to outgoing cash movements that are related to cash managemen activities initiated by the owner of the account to optimise the return on the available f | |
| 5. | Received Direct Debits | The Received Direct Debit transactions are related to instructions received by the acc to debit the account. | |
| 6. | Issued Direct Debits | The Issued Direct Debit transactions are related to instructions sent by the account own collect an amount o | |
| 7. | Received Cheques | Transaction is rela on the cheque dr. | |
| 8. | Issued Cheques | Transaction is rel | |

https://www.iso20022.org/external_code_list_page

| | **Sub-Families** | **Definition** |
|---|---|---|
| | **Internal Book Transfer** | Transaction is a transfer between –two different accounts within the same bank |
| | **Standing Order** | Transaction is a standing order. A standing order is an instruction given by a party having authority on the debtor's account to debit i.e. either debit account owner or originating pa account service, to process credit transfers at specified intervals during an implicit or ex period of time. It is given once, and is valid for an open or closed period of time. |
| | **Cross-Border Standing Order** | Transaction is a cross-border standing order |
| | **SEPA Credit Transfer Domestic Credit Transfer** | Transaction is a SEPA credit transfer Transaction is a in-country domestic currency credit transfer |
| | **Cross-Border Credit Transfer** | Transaction is a cross-border credit transfer |
| | **Credit Transfer with agreed Commercial Information** | Transaction is a credit transfer including commercial information, i.e. additional informat agreed between the sender and the receiver. |
| | **Financial Institution Credit Transfer** | Transaction is a financial institution credit transfer, i.e. the debtor and creditor are financi institutions. |
| | **Priority Credit Transfer** | Transaction is a credit transfer defined with higher priority, e.g. a PRIURO credit transfer |
| | **Payroll Salary Payment Cross-border** | Transaction is related to the payment of a payroll salary Transaction is related to the payment of a cross-border payroll salary |

---

<!-- Page 660 -->

# combinations

| **Bank Transaction Code - all permitted combinations of the BTC code sets** | | | | | | | | |
|---|---|---|---|---|---|---|---|---|
| *All codes in light gray are defined as the generic codes available for all Domains and Families* | | | | | | | | |
| Domain | Family | SubFamily | DomainCode | FamilyCode | ExampleOfATransactionDomainCode | SubFamilyCode | ExampleOfATransactionSubFamilyCode | Status | StatusDate |
| Payments | Issued Credit Transfers | Cross-Border Credit Transfer | PMNT | ICDT | XBCT | New | 27/4/2009 | | |
| Payments | Received Credit Transfers | Cross-Border Credit Transfer | PMNT | RCDT | XBCT | New | 27/4/2009 | | |

Bank Transaction Codes are an external code set defined in the *Bank Transaction Code combinations* external code sets.

As an example a debit notification which relates to a cross-border payment initiated from an account would be represented by:

| **Domain** | **Family** | **Sub-Family** |
|---|---|---|
| PMNT (Payment) | ICDT (Issued Credit Transfer) | XBCT (Cross-Border Credit Transfer |

---

<!-- Page 661 -->

**Min 0 – Max 1**
**Commission Waiver Indicator**
Optional element indicating, as a Boolean, whether the entry is exempt from commission. This element is not typically associated with Correspondent Banking payments

**Min 0 – Max 1**
**Additional Information Indicator**
Optional element indicating whether the underlying transaction details are provided through a separate message. Where the **Message Name Identification** represents the message used to provide the additional information and **Message Identification** specifies the reference of the message that provides the additional information.

**Min 0 – Max 1**
**Amount Details**
Optional nested element which provides various elements to represent an aggregated (consolidated) original amount. Where individual transaction amounts can be represented, if required, within the **Entry Detail** set of elements.
This element is useful to capture original amount details where they are different to the **Entry Amount**, for example the **Instructed Amount** of the payment can be included, together with a potential **Currency Exchange** rate, where necessary.

**Min 0 – Max 1**
**Charges**
Optional nested element to provide information on charges either pre-advised or taken from the entry.

Notification Entry

---

<!-- Page 662 -->

| Element | Description |
|---|---|
| **Min 0 – Max 1**<br>**Technical Input Channel** | Optional element which may either use an external ISO **Technical Input Channel code** or a proprietary code used to represent the technical channel used to input the entry. |
| **Min 0 – Max 1**<br>**Interest** | Optional nested element detailing any interest accrued as part of an aggregated (consolidated) entry amount. |
| **Min 0 – Max 1**<br>**Card Transactions** | Optional nested element which provides details associated with a card transaction such as the card number, card brand etc. |
| **Min 0 – Max \***<br>**Entry Details** | Additional optional nested element containing details on the entry. See dedicated section on *Entry Details*. |
| **Min 0 – Max 1**<br>**Additional Statement Information** | Additional optional element to represent further information related to the account statement |

Notification

---

<!-- Page 663 -->

The Bank to Customer Debit Credit Notification message optional **Entry Details** provides a variety of nested elements to represent the details associated with each *Entry*.

**Batch** provides details on batched transactions such as the total **Number of Transactions** the batched entry (sometimes referred to as a consolidated entry) represents.
**Transaction Details** is a significant nested element which represents information on the underlying transaction.

---

<!-- Page 664 -->

When the Bank to Customer Debit Credit Notification message optional <sup>Min 0 – Max *</sup> **Entry Details** is utilized the nested <sup>Min 1 – Max 1</sup> **Transaction Details** element is mandatory.

**Transaction Details** has a variety of nested elements closely associated with **Entry** level elements. The **References** element however is nested to include a variety of references related to the entry including for example the **UETR**

<sup>Min 1 – Max 1</sup> **Reference** → <sup>Min 1 – Max 1</sup> **Amount** → <sup>Min 1 – Max 1</sup> **Credit Debit Indicator** → <sup>Min 0 – Max 1</sup> **Amount Details** → <sup>Min 0 – Max 1</sup> **Availability** → <sup>Min 0 – Max 1</sup> **Bank Transaction Code** → <sup>Min 0 – Max 1</sup> **Charges** → <sup>Min 0 – Max 1</sup> **Interest**

Additionally **Transaction Details** also has a variety of elements capturing details from the underlying transaction, which amongst other business transactions includes payment transaction data. For example **Remittance Information** and **Related Parties**

Notification > Entry > Entry Details > Transaction Detail...

---

<!-- Page 665 -->

# Agents

The Bank to Customer Debit Credit Notification message **Related Parties** and **Relegated Agents** represents a set of optional nested elements related to the underlying transaction. Where the **Entry Details** (the set of elements *Related Parties/Agents* belongs to) relate to a Payment, Clearing and Settlement (pacs) message, parties in the pacs messages can be transferred into the Cash Management (camt) message.

| These **Related Parties** include : | These **Related Agents** include : |
| :--- | :--- |
| • *Instructing Party* | • *Instructing Agent* |
| • *Debtor* | • *Instructed Agent* |
| • *Debtor Account* | • *Debtor Agent* |
| • *Ultimate Debtor* | • *Creditor Agent* |
| • *Creditor* | • *Intermediary Agent 1* |
| • *Creditor Account* | • *Intermediary Agent 2* |
| • *Ultimate Creditor* | • *Intermediary Agent 3* |

**Trading Party** is also present in the *Related Parties* elements, and the following are present in the *Related Agents* elements: **Receiving Agents, Delivering Agent, Issuing Agent** and **Settlement Place**. Although these elements are not directly associated with a payment, as a Customer receiving a Statement related to other Business Domains e.g. a Security

---

<!-- Page 666 -->

The Bank to Customer Debit Credit Notification message *Entry Details* have a number of additional elements beyond *Related Parties* and *Related Agents* to capture information from the underlying payment.

These are:
* *Local Instrument*
* *Purpose*
* *Related Remittance Information*
* *Remittance Information*
* *Related Dates* such as the *Interbank Settlement Date*
* *Tax*

For *Payment Return* (pacs.004) it is also possible to capture *Return Information* which includes:
* The *Original Bank Transaction Code* of the original Entry
* The *Originator* of the return from the pacs.004
* And the *Reason* code.

*Remittance Information* as an end-to-end element should be passed unaltered from Payment Initiation (pain) into the Payment, Clearing and Settlement (pacs) message and onto the Bank to Customer Account Statement (camt). The Bank to Customer Debit Credit Notification may also capture this information. The

---

<!-- Page 667 -->

It should also be mentioned that the Bank to Customer Credit Debit Notification message **_Entry Details_** have a number of additional elements which capture information from transactions in other business domains beyond payments, as well as have an element to capture **_Additional Transaction Information._**

These are:
*   *Related Quantity*
*   *Financial Instrument Identification*
*   *Corporate Action*
*   *Safekeeping Account*
*   *Cash Deposit*
*   *Card Transactions*

---

<!-- Page 668 -->

| Use case should be considered as a principal example whereby use case may be cross referenced |
|---|

**Debit/Credit Notification related to a Serial Customer Payments**
Use Case c.54.1.1 – Customer Debit/Credit Notification (camt.054) of a Customer Credit Transfer (pacs.008)
**Debit/Credit Notification related to a Serial Financial Institution Payments**
Use Case c.54.2.1 – Customer Debit/Credit Notification (camt.054) of a FI to FI Credit Transfer (pacs.009)
**Debit/Credit Notification related to a Cover Method Payments**
Use Case c.54.3.1 – Customer Debit/Credit Notification (camt.054) of a payment using the cover method

---

<!-- Page 669 -->

(pacs.008)

1 → 2a → 3 → 4 → 5
(pacs.008) (pacs.008) (pacs.008)
2b ← camt.054
5 → camt.054

| 1 | Debtor initiates a payment instruction to the Debtor Agent |
|---|---|
| 2 | Debtor Agent (A) initiates a serial payment towards the Creditor Agent (D) using Agents B & C as intermediaries |
| 2b | Agent A provides a debit notification to the debtor using the camt.054 to confirm their account has been debited for the payment initiation request. This notification may complement additional status information or statement report messages |
| 3 | Agent B processes the payment on Agent C |
| 4 | Agent C processes the payment on Agent D |
| 5 | Agent D credits the account of the Creditor, providing a credit notification using the camt.054 |

---

<!-- Page 670 -->

(pacs.009)

1

Agent A as the Debtor initiates a payment instruction to the Debtor Agent (Agent B)

2

Debtor Agent (B) debits the account of Agent A and initiates a serial payment towards the Creditor (Agent D) using Agents C as an intermediary.

2a

pacs.009

3

camt.054

camt.053

2b

Debtor Agent (Agent B) provide a debit notification to the debtor using the camt.054 to confirm their account has been debited for the payment initiation request. This notification may be complemented by an additional status information message. But typically will be complement by an end of business day statement report messages

3

Creditor Agent (C) credits the account of Agent D and provides a credit notification (camt.054) in addition to an account statement (camt.053)

---

<!-- Page 671 -->

# method

**Message labels (arrows):** pacs.008 · pacs.002 · pacs.009.cov · camt.054 · camt.053

**1**
Debtor initiates a payment instruction to the Debtor Agent

**2a**
Debtor Agent (A) initiates a payment using the cover method to the Creditor Agent (D)

**2b**
In parallel the Debtor Agent (A) initiates a cover payment to credit the account of Agent (D) with their correspondent (Agent C)

**3a**
Agent B processes the payment

**3b**
Agent B provides a debit notification to Agent A using the camt.054 to confirm their account has been debited for the payment initiation request. This notification may be complimented by an additional status information message or statement report messages

**4**
Agent C receives the payment and credits the account of Agent D and provides a credit notification (camt.054)

**5**
Upon receipt of the credit notification (camt.054) confirming settlement of the covering payment, Agent D may chose to process the pacs.008 (if not already done so) and apply a credit to the

**6**
Agent C produces an end of day account statement report. An optional real time notifications e.g. advice of credit may have, also been created at the time of the credit posting

> Intraday Credit Notification is required when using the cover method unless an alternative

---

<!-- Page 672 -->

# Notification to Receive

---

<!-- Page 673 -->

# camt.057

- Group Header
- Notification

The *NotificationToReceive* message is sent by an account owner or by a party acting on the account owner's behalf to one of the account owner's account servicing institutions. It is an advance notice that the account servicing institution will receive funds to be credited to the account of the account owner. The *NotificationToReceive* message is used to advise the account servicing institution of funds that the account owner expects to have credited to its account.

The Notification to Receive message is the ISO 20022 equivalent of the legacy MT210 Notice to Receive. It can be cancelled using the camt.058 where in the meantime the legacy MT 292 can be used to request its cancellation.

---

<!-- Page 674 -->

A
B
pacs
camt.057
camt.058

Role of the Creditor Agent and Creditor in the payment changes description in the Notification to Receive message (camt.057). The Account Owner is typically the Creditor and the Account Servicer is typically the Creditor Agent. This will be followed up with a pacs transferring the funds to the Account Servicer on the expected value date.

---

<!-- Page 675 -->

payment message (pacs.008/pacs.009) and the Notification to Receive (camt.057)

A → B: pacs
B → A: pacs.002
B → C: pacs
C → B: pacs.002
C → D: pacs
D → C: pacs.002
D → (person): camt.053
(person) → D: camt.057

| Party | pacs | camt.057 |
|---|---|---|
| 👤 | Debtor | Debtor |
| 🏦 A | Debtor Agent | Debtor Agent |
| 🏦 B | Creditor Agent | Account Servicer |
| 👤 | Creditor | Account Owner |

The Parties defined within the Notification to Receive (camt.0057) provide advance information to the Account Servicer of information included in the payment message. Noting a Debtor must always be present in the camt.057 (it is mandatory in the pacs payment message) but Debtor Agent may not be provided (Debtor Agent is mandatory in the pacs.008 but not the pacs.009).

---

<!-- Page 676 -->

# Group Header

---

<!-- Page 677 -->

Each ISO 20022 cash management reporting message has a *Message Identification* element, located in the Group Header. This **35 character** identifier is a point-to-point reference used to unambiguously identify the message.

Min 1 – Max 1

The **Message Identification** in the Cash Management (camt) messages is equivalent to field 20 Transaction Reference Number of the MT 210 in the legacy MT Notice to Receive.

Group Header > Message Identification

---

<!-- Page 678 -->

Min 1 – Max 1
The camt.057 message *Creation Date Time* captures the date and time which the message was created.

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
> For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

Group Header > Creation Date Time

---

<!-- Page 679 -->

Min 0 – Max 1
The Notification to Receive **Message Sender** nested element provides details of the party that is sending the message, where the **Message Sender** is different from the account owner.

Where *Message Sender; Party* is used the nested:
* **Name** Min 0 – Max 1
* **Postal Address** Min 0 – Max 1
* **Identification** Min 0 – Max 1
* **Contact Details** Min 0 – Max 1
May be used to capture information related to this party.

Where *Message Sender; Agent* is used the nested *Financial Institution*:
* **BICFI** Min 1 – Max 1
* **Clearing System Member Identification** Min 0 – Max 1
* **LEI** Min 0 – Max 1
May be used to capture information related to this Agent.

Group Header > Message Sender
Name

---

<!-- Page 680 -->

# Notification

---

<!-- Page 681 -->

Min 1 – Max 1

The Notification to Receive ***Notification*** element contains nested elements to provide further details on the account notification such as the related parties, the expected amount to be received and value date of the expected receipt.

> 1
> The Notification nested element **Item** can contain multiple Credits. Where there is only one expected credit then only the Item element will contain the Item **Identification** and the **Amount**.

> Today the status of a camt.057 has no documented ISO 20022 reporting process, to the Account Owner by the Account Servicer.
> Generally, if the Account Servicer does not require notification the message will be ignored.

Notification ?

---

<!-- Page 682 -->

Min 1 – Max 1

The Notification to Receive message **Notification Identification** provides a mandatory element to identify the account notification.

Unique reference assigned by the account owner to unambiguously identify the account notification. There is no equivalent in the MT210. It is recommended that the Message Identification is repeated for the Notice to Receive Identification.

---

<!-- Page 683 -->

The Notification to Receive message **Account** element provides nested elements to identify the account – for which the credit entry has been made. The following two mandatory elements are nested beneath **Account**.

`Min 0 – Max 1`

**Identification** ∞
`Min 1 – Max 1`
a unique **Identification** for the account, between the Account Servicer and Account Owner. The element is further nested by choice of *IBAN* or *Other* to capture the account.

**Type** ∞
An element which may either use an external ISO **Cash Account Type code** or a proprietary code. It is used to identify a particular type of account.

**Currency**
The **Currency** for which the account is held. This is identified using the three characters **ISO currency code**.

**Name** ➤
The Name of the Account, as Assigned by the servicing institution.

A nested element which contains a Proxy Identifier together with the Proxy

---

<!-- Page 684 -->

Min 0 – Max 1 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&

---

<!-- Page 685 -->

Min 0 – Max 1
The Notification to Receive message **Related Account** element allows the identification of a related parent account for the account notification. For example sweeping, pooling or virtual account for which the notification is produced can identify the parent account they hierarchically relate to.
In the context of a Notification to Receive this element provides little business value.

Min 1 – Max 1 Min 0 – Max 1
When **Related Account** is utilized, like **Account**, the **Identification** and **Currency** element become mandatory. Additionally, the nested **Type** element, **Name** and nested **Proxy** element are optionally available.
Min 0 – Max 1 Min 0 – Max 1 Min 0 – Max 1

*Related Account* uses a variety of common elements described in more detail within the *Account* section.

Notification > Related Account > Identification > Type

---

<!-- Page 686 -->

Min 0 – Max 1
The *Notification to Receive* message **Total Amount** provides the sum of all the amounts of all the *Item* entries. Where utilised the *Item* element is a mandatory element which contains information about the expected receipt. The Notification to Receive can contain multiple items. **Expected Value Date** is the date on which the final receiving agent expects to receive the total amount. Min 0 – Max 1

The Total Amount provides a control total where there are multiple credits recorded within the Item element. The Total Amount element should not be used where there is a single expected credit.

The **Expected Value Date** takes the format YYYY-MM-DD

| | | |
|---|---|---|
| Notification > Total Amount | ✔ | |
| Notification > Expected Date | | |

---

<!-- Page 687 -->

The Notification to Receive message describes the **Party** or **Agent** that owes the amount of money as the **Debtor**. The following describes the *Debtor* nested **Party** elements in greater detail.

- Postal Address
  - Department
    - Sub Department
    - Street Name
    - Building Number
    - Building Name
    - Floor
    - Post Box
    - Room
    - Post Code
    - Town Name
    - Town Location Name
    - District Name
    - Country Sub Division
    - Country
      - Code

Nested element capturing either structured or unstructured *Debtor* address details

Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc.

Mandatory *Name* (where a BIC identifier is not provided) by which the party is known — **Name**

**Postal Address**

**Debtor**

**Identification**

Optional element to capture the Debtor's ISO country code of residence — **Country of Residence**

---

<!-- Page 688 -->

The Notification to Receive message describes the **Party** or **Agent** that owes the amount of money as the *Debtor*. The following describes the *Debtor* nested **Agent** elements in greater detail.

| Postal Address |
|---|
| Department |
| Sub Department |
| Street Name |
| Building Number |
| Building Name |
| Floor |
| Post Box |
| Room |
| Post Code |
| Town Name |
| Town Location Name |
| District Name |
| Country Sub Division |
| Country → Code |

The BIC which identifies the *Debtor* — **BICFI**

Information used to identify a Debtor by a clearing system identifier. — **Clearing System Member Id**

Legal entity identifier of the financial institution. — **LEI**

*Name* by which the Agent is known — **Name**

Nested element capturing either structured or unstructured *Debtor* address details. — **Postal Address**

# Debtor

---

<!-- Page 689 -->

**Min 0 – Max 1**

The ***Debtor Agent*** element in the camt.057 Notification to Receive captures the Debtor Agent of the payment i.e., the Financial Institution servicing an account for the Debtor. The ***Debtor Agent*** and ***Intermediary Agent*** elements allow the Treasury function at the Creditor Agent to chase up the actual payment if it fails to arrive at the scheduled time.

**Min 0 – Max 1**

The ***Intermediary Agent*** element in the camt.057 Notification to Receive capture the Intermediary agent between the Debtor Agent and the Account Servicer i.e. the Agent from whom the Creditor Agent expects to receive the payment from.

The ***Debtor Agent*** and ***Intermediary Agent*** elements allow the Treasury function at the Creditor Agent to chase up the actual payment if it fails to arrive at the scheduled time.

The ***Debtor Agent*** and ***Intermediary Agent*** elements allow the Account Servicing Institution's Treasury department to proactively follow up, as necessary, the actual payment if it fails to arrive by an expected time.

Notification

---

<!-- Page 690 -->

Min 1 – Max *

The Notification to Receive message mandatory *Item* element provides details of the expected amount on the account serviced by the account service. There is no equivalent field in the legacy MT210 Notice to Receive.

The various nested elements within the *Item* element are very useful in the case where there are multiple credits. The Creditor Agent will be able to reconcile the incoming receipts against the list of expected receipts detailed in the *Item* element and will be check completeness of all expected receipts and identify any missing receipts.

A single occurrence of *Item* should be used unless bilaterally agreed.

Notification > Item
Identification
Type

---

<!-- Page 691 -->

Min 1 – Max *
The Notification to Receive message mandatory **item** element provides details of the expected amount on the account serviced by the account servicer. There is no equivalent field in the legacy MT210 Notice to Receive.

Only the *Identification* and **Amount** elements are mandatory.

| Min 1 – Max 1 | Min 0 – Max 1 | Min 0 – Max 1 | Min 0 – Max 1 | Min 0 – Max 1 |
|---|---|---|---|---|
| Identification | End to End Identification | UETR | Account | Account Owner |
| Min 0 – Max 1 | Min 0 – Max 1 | Min 0 – Max 1 | Min 0 – Max * | Min 0 – Max 1 |
| Account Servicer | Related Account | Amount | Expected Value Date | Debtor |
| Min 0 – Max 1 | Min 0 – Max 1 | Min 0 – Max 1 | | |
| Debtor Agent | Intermediary Agent | Purpose | | |

Notification to Receive

---

<!-- Page 692 -->

| Use case should be considered as a principal example whereby use case may be cross referenced |
|---|

**Notification to Receive multiple receipts**

Use Case c.57.1.1 – Notification to Receive (camt.057) followed by Customer Credit Transfers (pacs.008)

Use Case c.57.1.2 – Notification to Receive (camt.057) followed by FI Credit Transfers (pacs.009)

Use Case c.57.1.3 – Notification to Receive (camt.057) where the receipt is settled by the cover method.

Use Case c.57.1.4 – Notification to Receive (camt.057) for a FI Credit Transfers cover (pacs.009 cov).

---

<!-- Page 693 -->

(pacs.008)

[Account Owner] —(2)→ [Agent A] —(3, pacs.008)→ [Agent B] —(4, pacs.008)→ [Account Servicer] —(5, camt.053)→ [Wallet]
[Account Servicer] ←(1, camt.057)— [Wallet]

**1**
Creditor is expecting to receive a payment from the Debtor. As the Account Owner sends a Notification to Receive to Agent C as Account Servicer.

**2**
Debtor initiates a payment instruction to the Debtor Agent (A).

**3**
Debtor Agent (A) initiates a serial payment towards the Creditor Agent (C) using Agents B as an intermediary.

**4**
Agent (B) processes the payment on to the Creditor Agent (C).

**5**
Creditor Agent (C) as Account Servicer sends and end of day statement to Creditor as Account Owner confirming accounting entries.

---

<!-- Page 694 -->

A (2) → pacs.009 → B (3) → pacs.009 → C (4) → camt.053 → D (1) ← camt.057 ← C

**1**
Creditor is expecting to receive a payment from Debtor. As the Account Owner sends a Notification to Receive to Agent C as Account Servicer.

**2**
Debtor (A) initiates a serial payment towards the Creditor Agent (C) using Agents (B) as an intermediary.

**3**
Agent (B) processes the payment on to the Creditor Agent (C).

**4**
Creditor Agent (C) as Account Servicer sends and end of day statement to Creditor as Account Owner confirming accounting entries.

---

<!-- Page 695 -->

method.

**Diagram flow (message labels on arrows):**

- 1 → A
- A → D : `pacs.008`
- A → B : `pacs.009 cov` (2b)
- B → C : `pacs.009 cov`
- C → D : `camt.053`
- D → C : `camt.057` (3)
- D → (Debtor)

**Step descriptions:**

**1**
Debtor initiates a payment instruction to the Debtor Agent

**2a**
Debtor Agent (A) initiates a payment using the cover method to the Creditor Agent (D)

**2b**
In parallel the Debtor Agent (A) initiates a covering payment to credit the account of Agent (D) who become the Creditor of the cover payment (pacs.009 cov). Agent A's role also changes in the cover payment where it becomes the Debtor, whereby Agent A's account with their correspondent (Agent D)is debited

**3**
Upon receipt of the pacs.008 advising settlement will occur via a cover payment. Agent D sends a Notification to Receive to Agent C.

**4**
Agent B processes the payment onto Agent C

**5**
Agent C receives the payment and credits the account of Agent D as the Creditor, producing an end of day account statement report. An optional real time notifications e.g. advice of credit may have also been created at the time of the credit posting.

---

<!-- Page 696 -->

cov).

1

2a

2b

pacs.008

pacs.009 cov

camt.057

camt.053

pacs.009 cov

pacs.009 cov

pacs.009 cov

**1**
Debtor initiates a payment instruction to the Debtor Agent

**2a**
Debtor Agent (A) initiates a payment using the cover method towards the Creditor Agent (D)

**2b**
In parallel the Debtor Agent (A) initiates a covering payment to credit the account of Agent (D) who become the Creditor of the cover payment (pacs.009 cov).

**3a**
Agent B processes the cover payment on to Agent E

**3b**
Agent B also sends a notification to receive on behalf of Agent D to notify Agent C a credit is expect on their account.

**4**
Agent E processes the cover payment on to Agent F.

**5**
Agent F processes the cover payment on to Agent C.

**6**
Agent C receives the cover payment (as the Creditor Agent) recognising they have also be Notified they would receive this payment (by camt.057). They apply credit to Agent D

---

<!-- Page 697 -->

# Notification to Receive Cancellation Advice

---

<!-- Page 698 -->

## camt.058

- Group Header
- Original Notification
- Cancellation Reason

The *Notification To Receive Cancellation Advice* message is sent by an account owner or by a party acting on the account owner's behalf to one of the account owner's account servicing institutions. It is used to advise the account servicing institution about the cancellation of a notification sent in a previous *Notification To Receive* message.

---

<!-- Page 699 -->

```
        [A: Bank]              [B: Document]              [Wallet]
           |                        |                          |
           |  - - - - [pacs] - - - >|                          |
           |                        |<------- [camt.057] ------|
           |                        |<======= [camt.058] ======|
```

**Role of the Creditor Agent and Creditor in the payment changes description in the Notification to Receive message (camt.057).** The Account Owner is typically the Creditor and the Account Servicer is typically the Creditor Agent. The Notification to Receive Cancellation Advice (camt.058) is used to request the cancellation of a previous Notification to Receive.

---

<!-- Page 700 -->

# Group Header

---

<!-- Page 701 -->

Each ISO 20022 cash management reporting message has a *Message Identification* element, located in the Group Header. This **35 character** identifier is a point-to-point reference used to unambiguously identify the message.

Min 1 – Max 1

The **Message Identification** in the Cash Management (camt) messages is equivalent to field 20 Transaction Reference Number of the MT 292 in the legacy MT Request for Cancellation.

Group Header > Message Identification

---

<!-- Page 702 -->

Min 1 - Max 1
The camt.058 message *Creation Date Time* captures the date and time which the message was created.

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+/-hh:mm
> For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

Group Header ⓘ Creation Date Time

---

<!-- Page 703 -->

The Notification to Receive Cancellation Advice **Message Sender** `Min 0 – Max 1` nested element provides details of the *Party* or *Agent* that is sending the message, where the *Message Sender* is different from the account owner.

This element has no equivalent in the legacy MT 292 Request for Cancellation.

Where **Message Sender**; *Party* is used the nested:
* **Name** `Min 0 – Max 1`
* **Postal Address** `Min 0 – Max 1`
* **Identification** `Min 0 – Max 1`
* **Contact Details** `Min 0 – Max 1`

May be used to capture information related to this party.

Where **Message Sender**; *Agent* is used the nested *Financial Institution*:
* **BICFI** `Min 1 – Max 1`
* **Clearing System Member Identification** `Min 0 – Max 1`
* **LEI** `Min 0 – Max 1`

May be used to capture information related to this Agent.

---

<!-- Page 704 -->

# Original Notification

---

<!-- Page 705 -->

Min 1 – Max 1

The Notification to Receive Cancellation Advice *Original Notification* element contains nested elements to provide further details on the original camt.057 notification to receive. such as the related parties, the expected amount to be received and value date of the expected receipt.

The *Original Notification* nested element enables the ability to reconcile this cancellation advice against the Notification originally received, so that appropriate action can be take to remove the advised currency and amount from predicted currency positions at the Account Servicer.

| **ISO** — Camt.057 | **ISO** — Camt.058 |
|---|---|
| *Group Header* | ***Original Notification*** |
| &gt; *Message Identification* | &gt; ***Original Message Identification*** |
| &gt; *Creation Date Time* | &gt; ***Original Creation Date Time*** |
| *Notification* | |
| &gt; *Identification* | &gt; ***Original Notification Identification*** |
| | &gt; ***Original Notification Reference*** |
| &gt; *Debtor* | &gt; ***Debtor*** |
| *Item* | &gt; ***Original Item*** |
| &gt; *Identification* | &gt;&gt; ***Original Item Identification*** |
| &gt; *End to End Identification* | &gt;&gt; ***Original End to End Identification*** |

---

<!-- Page 706 -->

Min 1 – Max 1

The Notification to Receive Cancellation Advice message *Original Message Identification* provides a mandatory element to identify the Message Identification from the original camt.057.

This **35 character** identifier is a point-to-point reference used to unambiguously identify the Notification to Receive message, capture in its group header.

Original Notification
Original Message Identification

---

<!-- Page 707 -->

Min 0 - Max 1

The camt.058 message *Original Creation Date Time* captures the date and time which the original Notification to Receive message was created.

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+-hh:mm
> For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

---

<!-- Page 708 -->

Min 1 – Max 1

The Notification to Receive Cancellation Advice message **Original Notification Identification** provides a mandatory element to identify the account notification.

Unique reference assigned by the account owner to unambiguously identify the original account notification.

Original Notification
Original Notification Identification

---

<!-- Page 709 -->

The Notification to Receive message describes the **Party** or **Agent** that owes the amount of money as the **Debtor**. The following describes the *Debtor* nested **Party** elements in greater detail.

- Postal Address
  - Department
    - Sub Department
    - Street Name
    - Building Number
    - Building Name
    - Floor
    - Post Box
    - Room
    - Post Code
    - Town Name
    - Town Location Name
    - District Name
    - Country Sub Division
    - Country
      - Code

Nested element capturing either structured or unstructured *Debtor* address details

Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc.

Mandatory *Name* (where a BIC identifier is not provided) by which the party is known — **Name**

**Postal Address**

**Debtor**

**Identification**

Optional element to capture the Debtor's ISO country code of residence — **Country of Residence**

---

<!-- Page 710 -->

The Notification to Receive message describes the **Party** or **Agent** that owes the amount of money as the *Debtor*. The following describes the *Debtor* nested **Agent** elements in greater detail.

| Postal Address |
|---|
| Department |
| Sub Department |
| Street Name |
| Building Number |
| Building Name |
| Floor |
| Post Box |
| Room |
| Post Code |
| Town Name |
| Town Location Name |
| District Name |
| Country Sub Division |
| Country → Code |

The BIC which identifies the *Debtor* — **BICFI**

Information used to identify a Debtor by a clearing system identifier. — **Clearing System Member Id**

Legal entity identifier of the financial institution. — **LEI**

*Name* by which the Agent is known — **Name**

Nested element capturing either structured or unstructured *Debtor* address details. — **Postal Address**

# Debtor

---

<!-- Page 711 -->

Min 0 – Max 1

The ***Debtor Agent*** element in the camt.058 Notification to Receive Cancellation Advice captures the Debtor Agent provided in the original Notification to Receive (camt.057) i.e., the Financial Institution servicing an account for the Debtor.

Debtor Agent may be provided within the ***Original Notification Reference*** nested element or within the ***Original Item*** nested element.

Original Notification

---

<!-- Page 712 -->

Min 1 - Max 1
The Notification to Receive Cancellation Advice *Original Item Reference* nested element captures the references of the Original Item in the original Notification to Receive message.

Min 1 - Max *
The *Original Item* nested element is repetitive as the original Notification to Receive message has the ability to notify on more than one item i.e. currency and amount expect.
The following elements are nested within *Original Item*, of which **Identification** and **Amount** are required.

Min 1 - Max 1: Identification
Min 0 - Max 1: End to End Identification
Min 0 - Max 1: UETR
Min 1 - Max 1: Amount
Min 1 - Max *: Expected Value Date
Min 0 - Max 1: Debtor
Min 0 - Max 1: Debtor Agent

Original Notification

28 Debtor is required either within the *Original Notification Reference*

---

<!-- Page 713 -->

# Cancellation Reason

---

<!-- Page 714 -->

The Notification to Receive Cancellation Advice <span style="background-color: #add8e6;">Min 1 – Max 1</span> **Cancellation Reason** nested element captures information associated with the reason for the Cancellation request.

<span style="background-color: #add8e6;">Min 0 – Max 1</span>
the **Originator** element helps identify the party who issued the Cancellation request. Typically, this element would be used to identify the Account Owner as the Originator of the request, where the Notification to Receive Cancellation Advice message captured a *Message Sender* acting on the account owner's behalf.

<span style="background-color: #add8e6;">Min 1 – Max 1</span>
the **Reason** is mandatory and represented by an embedded CBPR+ Cancellation **Code** choice ( )-
<span style="background-color: #add8e6;">Min 0 – Max 2</span>
The **Additional Information** element may also be included to provide further details on the Cancellation reason.

🧠 Note where Reason code NARR is used additional information must be provided to describe the reason for the Cancellation request.

---

<!-- Page 715 -->

Use case should be considered as a principal example whereby use case may be cross referenced

**Notification to Receive multiple receipts**

Use Case c.58.1.1 – Cancellation Advice for a Notification to Receive (camt.057) expecting a Customer Credit Transfers (pacs.008)

Use Case c.58.1.2 – Cancellation Advice for a Notification to Receive (camt.057) expecting a FI Credit Transfers (pacs.009)

Use Case c.58.1.3 – Cancellation Advice for a Notification to Receive (camt.057) where the receipt is settled by the cover method.

---

<!-- Page 716 -->

# Customer Credit Transfers (pacs.008)

[Account Owner] → [Agent A] → [Agent B] → [Agent C] → [Debtor]

Agent C → Agent B: `camt.057` (1)
Agent C → Agent B: `camt.058` (2)

**1** Creditor is expecting to receive a payment from the Debtor. As the Account Owner they send a Notification to Receive to Agent C as Account Servicer.

**2** Creditor subsequently understand the payment should not longer be expected for the given amount. They issue a cancellation advice to Agent C as Account Servicer, providing the reason NOLE (not longer expected).

---

<!-- Page 717 -->

# Transfers (pacs.009)

![Icon A](icon_a) ![Icon B](icon_b) ![Icon C](icon_c) ← camt.057 ① ![Icon D](icon_d)
← camt.058 ②

① Creditor is expecting to receive a payment from Debtor. As the Account Owner sends a Notification to Receive to Agent C as Account Servicer.

② Creditor subsequently understand the payment should no longer be expected for the given amount. They issue a cancellation advice to Agent C as Account Servicer, providing the reason NOLE (not longer expected).

---

<!-- Page 718 -->

is settled by the cover method.

```
[A] --pacs.008--> [D]
[A] --camt.056--> [D]
[A] --pacs.009 cov--> [B]
[B] --pacs.002--> [A]   (Rejected +Reason)
[D] --camt.052--> [C]
[D] --camt.058--> [C]
```

**1a**
Debtor Agent (A) initiates a payment using the cover method to the Creditor Agent (D)

**1b**
In parallel the Debtor Agent (A) initiates a covering payment to credit the account of Agent (D) who, become the Creditor of the cover payment (pacs.009 cov). Agent A's role also changes in the cover payment where it becomes the Debtor, whereby Agent A's account with their correspondent / Agent D's debited

**2**
Upon receipt of the pacs.008 advising settlement will occur via a cover payment. Agent D sends a Notification to Receive to Agent C.

**3**
Agent B rejects the payment advising Agent A

**4**
Agent A send a Request for Cancellation to Agent D including the reason COVR to confirm the cover payment was cancelled.

**5**
Agent D subsequently issue a cancellation advice to Agent C as Account Servicer, providing the reason NOLE (not longer expected)

---

<!-- Page 719 -->

# Account Reporting Request

---

<!-- Page 720 -->

camt.060

- Group Header
- Reporting Request

The **AccountReportingRequest** message is sent by the account owner, either directly or through a forwarding agent, to one of its account servicing institutions. It is used to ask the account servicing institution to send a report for the account owner's account:

- **BankToCustomerAccountReport** (camt.052) or
- **BankToCustomerStatement** (camt.053) or
- **BankToCustomerDebitCreditNotification** (camt.054).

Account reports are often configured by the Account Servicing Institution as part of a static configuration. The Account Report Request could however be used as an alternative mechanism to request reports on a frequent or ad hoc basis.

Account Report Request can contain multiple *Reporting Request* elements as the maximum multiplicity is unbounded. This effectively allows multiple

---

<!-- Page 721 -->

A
B
C
pac.008
pac.002
camt.060
camt report
camt.060
camt report
pac.008
camt.060
camt report
camt.060
camt report

Role of the Creditor Agent and Creditor in the payment changes by description in the Bank to Customer Report Request message to Account Servicer and Account Owner. Whereby the report request is sent by the Account Owner or authorised party to the Account Servicer. This message is used to request a report/s of the entries on an account, and/or to provide

---

<!-- Page 722 -->

# Group Header

---

<!-- Page 723 -->

Min 1 – Max 1

Each ISO 20022 cash management reporting message has a ***Message Identification*** element, located in the Group Header. This **35 character** identifier is a point to point reference used to unambiguously identify the message.

For Cash Management (camt) messages the ***Message Identification*** has no exact equivalent in the legacy MT Customer Statement message. However the *Transaction Reference Number* (Field 20) could be considered a similar comparison.

Group Header > Message Identification

---

<!-- Page 724 -->

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+-hh:mm
> For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

Group Header Creation Date Time

---

<!-- Page 725 -->

Min 0 – Max 1

The Account Report Request *Message Sender* nested element provides details of the party that is sending the request.

This element **should only** be used to identify the *Message Sender* when different from the account owner.

Where *Message Sender* is used, a choice of nested **Party** or **Agent** may be used to identify the Sender.

| **Party:** | |
|---|---|
| • **Name** | Min 0 – Max 1 |
| • **Postal Address** | Min 0 – Max 1 |
| • **Identification** | Min 0 – Max 1 |
| • **Country of Residency** | Min 0 – Max 1 |

**Agent:**

Take me to the Agent identification

Group Header Message Sender Party

---

<!-- Page 726 -->

# Reporting Request

---

<!-- Page 727 -->

Min 1 – Max *

The Account Reporting Request *Reporting Request* nested element capture the detail related the request.

Many **Account Servicing Institutions** service their **Account Owner** customers through statics account configuration/s. Whereby a variety of reports can be generated on either a time or event bases routine.

The *Reporting Request* may be used as either an alternative to a static configuration or to request ad hoc reports (whether that be an additional report to the statics configuration or to resend reports previous reported).

Reporting Request

---

<!-- Page 728 -->

Min 1 – Max 1

The Account Reporting Request message *Identification* provides a mandatory element to identify the Request

Unique reference assigned by the account owner (or Message Sender on behalf of the account owner) to unambiguously identify the account statement. Directly comparable with the *Transaction Reference Number* (Field 20) of the legacy MT request message.

---

<!-- Page 729 -->

Min 1 – Max 1

The Account Reporting Request message ***Requested Message Name Identification*** provides a mandatory element to identify the name of the report being request.

This element specifies which type of report is begin requested. The report is represented by its full name.
For example:
**camt.052.001.08** or
**camt.053.001.08** or
**camt.054.001.08**

Reporting Request

---

<!-- Page 730 -->

The Account Reporting Request message **<u>Account</u>** `Min 0 – Max 1` provides nested elements to identify the account for which the request relates to. A number of elements are nested beneath *Account*, of which the **<u>Identification</u>** element is mandatory.

a unique **<u>Identification</u>** `Min 1 – Max 1` for the account, between the Account Servicer and Account Owner. The element is further nested by choice of *IBAN* or *Other* to capture the account.

---

<!-- Page 731 -->

Min 1 – Max 1 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&

---

<!-- Page 732 -->

Min 0 – Max 1

The Account Reporting Request message *Account Owner* identifies the mandatory owner of the account that the Account Report Request relates to.

Where *Account Owner* is used, a choice of nested **Party** or **Agent** may be used to identify the owner.

**Party:**
- **Name** Min 0 – Max 1
- **Postal Address** Min 0 – Max 1
- **Identification** Min 0 – Max 1
- **Country of Residency** Min 0 – Max 1

**Agent:**

Take me to the Agent identification

Typically the Account Name (see the previous page) represents the Account Owner's Name in accordance with standard Know Your Customer (KYC). The mandatory Account Owner elements enables more detail to be captured such as an address for a Party or a BIC for an Agent

---

<!-- Page 733 -->

Min 0 – Max 1

The Account Reporting Request message *Account Servicer* provides an optional element to capture the Agent who is acting as an Account Servicing Institution. Typically, this would be the same Agent the Account Reporting Request is sent to, who is also identified in the Business Application Header.

**Financial Institution Identification:**

- *BICFI*
- *Clearing System Member Identification*
- *LEI*
- *Name*
- *Postal Address*

Take me to the Agent identification

---

<!-- Page 734 -->

The Account Reporting Request message **_Report Period_** `Min 0 – Max 1` provides the ability to specify the period for which the request relates. Where used this nested element captures a mandatory **_From to Date_** and an optionally **_From to Time_** `Min 0 – Max 1` element.

**_From to Date_** captures a mandatory **_From Date_** and an optional **_To Date_**. It allows the request to specify the date period for which the report is being requested.

All CBPR+ time elements need offset against UTC. Milliseconds are

`Reporting Request` `Report Period`

---

<!-- Page 735 -->

Min 0 – Max 1

The Account Reporting Request message ***Reporting Sequence*** specifies the choice of identification sequences. This can be used as an alternative to the ***Reporting Period*** to request a sequence of reports, where the Account Servicing Institution uses this element within the reports they provide.

```
[A] --> [B]
          |
          v
[D] <-- [C]
```

Where used the ***Reporting Sequence*** mandate a choice of nested element:

* ***From Sequence*** identifies the start of a sequence range. `Min 1 – Max 1`
* ***To Sequence*** identifies the end of a sequence range. `Min 1 – Max 1`
* ***From To Sequence*** identifies the start and end of a sequence range. `Min 1 – Max *`
* ***Equal Sequence*** identifies a sequence. `Min 1 – Max *`
* ***Not Equal Sequence*** identifies a sequence to be excluded. `Min 1 – Max *`

Report Request > Report Sequence >

---

<!-- Page 736 -->

The Account Reporting Request message *Requested Transaction Type* provides the ability to identify the specific type of transactions the request wishes to be reported.

`Min 0 – Max 1`

Where used the *Status* element and *Credit Debit Indicator* elements are mandatory.

`Min 1 – Max 1` `Min 1 – Max 1`

- *Status* is a nested element which may either use a choice of external ISO Entry Status code or a proprietary code. It is used to indicate the transaction entry status for which the requested reported should reflect.
- *Credit Debit Indicator* is a choice of embedded code to indicate whether Debit or Credit transaction entries should be reported.

An optional *Floor Limit* element may also be used. This element requests a minimum value, for which transaction entries above this value should be reported.

`Min 0 – Max 1`

Where used the *Amount* and *Credit Debit Indicator* elements are mandatory.

As a request for specific transaction type/s to be reported, typically this request would relate to a camt.052 Bank to Customer Account Report where the specified balance information is an intraday report. The use of the camt.060 Account Reporting Request and the ability to specify specific reporting requirements in the request is dependent on the Account Servicing Institution and should be bilaterally agreed by Account Owner

---

<!-- Page 737 -->

Min 0 – Max *
The Account Reporting Request message *Requested Balance Type* provides the ability to identify the specific type of balances the request wishes to be reported.

Min 1 – Max 1
Where used a choice of balance **Code** is mandatory which may either use a choice of external ISO Balance Type code or a proprietary code.

Min 0 – Max 1
An optional **Sub Type** element may also be used which a choice of external ISO Balance Sub Type code or a proprietary code.

As a request for specific balance type/s (or sub balance type/s) to be reported, typically this request would relate to a camt.052 Bank to Customer Account Report where the specified balance information is an intraday report. The use of the camt.060 Account Reporting Request and the ability to specify specific reporting requirements in the request is dependent on the Account Servicing Institution and should bilaterally agreed by Account Owner with them

---

<!-- Page 738 -->

| Use case should be considered as a principal example whereby use case may be cross referenced |
|---|

**Financial Institution Account Reporting Request**

Use Case c.60.1.1 – High Level Financial Institution daily Account Reporting Request

Use Case c.60.1.2 – Financial Institution interim Account Reporting Request

---

<!-- Page 739 -->

# Payment Flow Sequence

**Flow (top):**

`A (1)` → `B (2)` → `C (3)` → `D`

- A → B: `pac.009` (forward), `pac.002` (return)
- B → C: `pac.009` (forward), `pac.002` (return)
- C → D: `camt.060`, `camt.053`
- Step 3: **Settlement Complete**
- Step 5 / ⚠ near D

---

## Step Descriptions

**1**
Debtor initiates a payment instruction to the Debtor Agent

**2**
Agent B processes the payment on Agent C, via the Payment Market Infrastructure.

**3**
Payment Market Infrastructure, settles the payment between Agent B and Agent C as direct participants of the Market Infrastructure, and provides a settlement confirmation to Agent B

**4**
Agent C credits the account of the Creditor (Agent D)

**5**
Agent C produces a customer statement (camt.053) following the request from Agent D

**⚠**
Agent D requests a daily statement using a camt.060 not having an automatic statement produced by their account servicing institution

---

<!-- Page 740 -->

## Payment Flow Diagram

**Agents:** A → B → (Market Infrastructure) → C → D

**Message flow:**

- A ⇄ B: `pac.002`
- B → Market Infrastructure: `pac.009`
- Market Infrastructure → C: `pac.009`
- C → D: `camt.060`, `camt.052`, `camt.053`

**Settlement Complete** (linked to `pac.009`)

**Step markers:** 1 (A), 2 (B), 3 (Market Infrastructure), 4 (C), 5 (C), ⚠ (D)

---

**1**
Debtor initiates a payment instruction to the Debtor Agent

**2**
Agent B processes the payment on Agent C, via the Payment Market Infrastructure.

**3**
Payment Market Infrastructure, settles the payment between Agent B and Agent C as direct participants of the Market Infrastructure, and provides a settlement confirmation to Agent B

**4**
Agent C credits the account of the Creditor (Agent D)

**5**
Agent C produces a customer statement (camt.052) following the request from Agent D

**⚠**
Agent D requests an interim statement using a camt.060 (not having an automatic interim statement produced by their account servicing institution)

---

<!-- Page 741 -->

# Cash Management Exception & Investigation (camt) messages

---

<!-- Page 742 -->

[camt.029 – Resolution of Investigation](#)

[camt.055 – Customer Payment Cancellation Request](#)

[camt.056 – FI to FI Payment Cancellation Request](#)

---

<!-- Page 743 -->

# Resolution of Investigation

---

<!-- Page 744 -->

## camt.029

- Assignment
- Status
- Cancellation Details

The Resolution of Investigation message is sent by an Agent to respond to the Cancellation Request, either directly or serially through other agents.

The message is used to provide:
- final outcome of the case, whether positive or negative, or
- an interim update prior to the final outcome.

Following a positive acceptance of the Cancellation request. The appropriate payment message (pacs.002 or pacs.004) is used to reject or return a previously received payment.

---

<!-- Page 745 -->

A
B
C
pac.008
pac.002
camt.055
camt.056
camt.053
camt.029

The Resolution of Investigation message is sent by a case assigner to a case assignee. This message is used to provide a response to the cancellation request (interim or final). Following an accepted Cancellation request the return of any payment previous settled is necessary to trigger reversing account postings.

---

<!-- Page 746 -->

A
B
C
pac.008
pac.002
camt.055
camt.056
pac.008
camt.053
camt.029

The Resolution of Investigation message is sent by a case assigner to a case assignee. This message is used to provide a response to the cancellation request (interim or final). Following an accepted Cancellation request the return of any payment previous settled is necessary to trigger reversing account postings.

---

<!-- Page 747 -->

The camt.056 Payment Cancellation Request and camt.029 Resolution of Investigation messages have a number of identification elements, of which some are used for cross referencing. The below provides a high level overview.

Cancel & return my payment please

Customer X

CASE123 - STAT789

CASE123

STAT789

CASE123 - STAT789

OK, I can understand the mistake.

Customer Y

ISO

ISO

| **Camt.056 Payment Cancellation Request** | | | **Camt.029 Resolution of Investigation** | | |
|---|---|---|---|---|---|
| **element** | **description** | **example** | **element** | **description** | **example** |
| Assigner | Sender of the camt.056 | Agent B | Assigner | Sender of the camt.029 | Agent C |
| Assignee | Receiver of the camt.056 | Agent C | Assignee | Receiver of the camt.029 | Agent B |
| Assignment Identification | Unique Id generated by the assigner to identify the Payment Cancellation Request message | CASE123/1 | Assignment Identification | Unique Id generated by the assigner to identify the Resolution of Investigation message | STAT789/1 |
| Cancellation Identification | Optional Cancellation Id of the Agent sending (assigner) the Payment Cancellation Request message. | CASE123 | Cancellation Identification | Case Reference of the Agent sending (assigner) the Resolution of Investigation message. | STAT789 |
| Case Identification | Case Id of the Agent sending (assigner) the Payment Cancellation Request message. | CASE123 | Resolved (Original) Case Identification | Case Id of the original case the Resolution of Investigation is responding to. | CASE123 |
| Case Creator | Party who created the original cancellation request (who may be another Agent other than the current Assigner. | Agent A | Case Creator | Party who created the original cancellation request (who is the same original case creator in the Payment Cancellation Request) | Agent A |

---

<!-- Page 748 -->

# Assignment

---

<!-- Page 749 -->

Min 1 – Max 1

The Payment Cancellation Request message *Identification* provides a mandatory element to identify the Request

Unique reference assigned by the assigner to unambiguously identify the Cancellation request.
For Exceptions and Investigations messages the Identification has no exact equivalent in the legacy MT Exceptions and Investigations message. However, the Transaction Reference Number (Field 20) could be considered a similar comparison.
Directly comparable with the *Transaction Reference Number* (Field 20) of the legacy MT statement message.

---

<!-- Page 750 -->

Assignee Agent: Agent A

Assigner Agent: Agent B

pac.008

camt.056

camt.029

Assignee Agent: Agent B

Assigner Agent: Agent C

pac.008

camt.056

camt.029

**Assigner** and **Assignee** represent the Agents involved in the point-to-point investigation message exchange. These roles therefore change on each message leg.

Assignment

Assigner

---

<!-- Page 751 -->

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+-hh:mm
> For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

Group Header Creation Date Time

---

<!-- Page 752 -->

# Status

---

<!-- Page 753 -->

Min 1 – Max 1

The Resolution of Investigation *Confirmation* provides a mandatory element to specify the status of the Payment Cancellation Request's investigation.

The *Confirmation* element includes a choice of three embedded confirmation codes:

*   **CNCL** – The payment has been cancelled as requested. This status concludes the investigation, whereby a Payment Return may follow if funds need to be returned.
*   **PDCR** – The Investigation of the Payment Cancellation Request is pending, i.e. is under ongoing investigation to provide a final status confirmation. An additional *Cancellation Status Reason Information* should be provided to further clarify the current status. For example, a Status Reason code RQDA can be used to indicate debit authority has been requested from the Creditor.
*   **RJCR** – The Payment Cancellation Request is rejected. A status concluding the investigation which must include additional *Cancellation Status Reason Information* to provide an explanation as to why the request was rejected.

---

<!-- Page 754 -->

# Cancellation Details

---

<!-- Page 755 -->

Min 1 – Max 1

The Resolution of Investigation **Transaction Information and Status** is a mandatory nested element to capture information related to the original payment and to provide further information on the status reason Payment Cancellation Request's investigation.

As part of this nested element, information is captured to reference; the case the investigation is attempting to resolve, various original references related to the original payment and the investigation status information.

---

<!-- Page 756 -->

Min 1 – Max 1

The Resolution of Investigation message **_Cancellation Status Identification_** provides a mandatory element to identify the status update.

Unique reference assigned by the resolution assigner to unambiguously identify the Cancellation status.

For Exceptions and Investigations messages the _Cancellation Status Identification_ can be considered an equivalent in the legacy MT Directly comparable with the _Transaction Reference Number_ (Field 20) of the legacy MT statement message.

---

<!-- Page 757 -->

**Min 1 – Max 1**
The Resolution of Investigation message **Resolved Case** provides a mandatory nested element to identify the Resolved Case *Identification* and the **Creator** of the case.

**Min 1 – Max 1**
The **Identification** element captures the unique case reference assigned by the Payment Cancellation Request Assigner to unambiguously identify the Cancellation investigation case being resolved.
For Exceptions and Investigations messages this *Case Identification* can be considered an equivalent of the *Related Reference* (Field 21) of the legacy MT Answer message.

**Min 1 – Max 1**
The **Creator** element captures the party who created the Payment Cancellation Request investigation (see camt.056 Case Creator).
This mandatory party can represent as either an **Agent** i.e., the Bank who created the case or as a **Party** i.e., the customer (for example the Debtor) who created the request. This element has no equivalent in the legacy MT Request for Cancellation message.

---

<!-- Page 758 -->

The Resolution of Investigation uses elements in the **_Original Group Information_** (Min 1 – Max 1) to capture the message identifier and message name of the underlying payment for which the investigation relates to. The mandatory **_Original Message Identification_** contains the point-to-point reference from this payment, and the mandatory **_Original Message Name Identification_** contains the message name of the underlying payment. Optionally the **_Original Creation Date Time_** can also be captured.

For example:

*Original Message Name Identification* “pacs.008.001.08” confirms the investigation relates to a pacs.008 Financial Institution to Financial Institution Customer Credit Transfer. Where as “pacs.009.001.08” confirms the investigation relates to a pacs.009 Financial Institution Credit Transfer.

| A | B |
|---|---|
| → **pacs.008** → | |
| Message Identification | abcd1234 |
| ← **camt.056** ← | |
| ← **camt.029** ← | |
| Identification | xyz9875 |
| Original Message Identification | abcd1234 |
| Original Message | |

| Assignment | Identification |
|---|---|
| Cancellation Details | Original Group | Original Message Identification | abcd1234 |
| | | Original Message | |

Note: the xx in the CBPR+ Usage Guideline represents the message version of the message

---

<!-- Page 759 -->

The Resolution of Investigation also uses a number of other **Original** elements in the **Transaction Information** to capture information from the underlying payment that the Cancellation request relates to.

The Original elements enables the **Assignee** to identify the Payment which is being request to be cancelled. The following element (in addition to *Original Message identification* and *Original Message Name Identification* described on the previous page) are mandated:

**Original UETR** `Min 1 – Max 1`

The following element (in addition to *Original Message identification* and *Original Message Name Identification* described on the previous page) are optional:

| Element | Constraint |
|---|---|
| **Original End to End Identification** | `Min 0 – Max 1` |
| **Original Instruction Identification** | `Min 0 – Max 1` |
| **Original Transaction Identification** | `Min 0 – Max 1` |
| **Original Clearing System Reference** | `Min 0 – Max 1` |

Cancellation Details > Transaction Information and Status >

▼ Original Group Information

- Original Instruction Identification
- Original End to End Identification
- Original Transaction
- Original Clearing System Reference

---

<!-- Page 760 -->

Min 0 – Max 1
The Resolution of Investigation **Cancellation Status Reason Information** nested element captures the information related to the status reason of the Cancellation Resolution.

Min 0 – Max 1
**Originator** element helps identify the party who provided the Cancellation status. This party would have been included in the underlying payment and is also included in the pacs.004 *Return Chain*.

Min 0 – Max 1
the **Reason** for the Cancellation status, which is mandatory where the Resolution Status is RJCR, is represented by an embedded CBPR+ Cancellation *Code* choice (⇐)

Min 0 – Max 1
the **Additional Information** element may also be included to provide **further** details on the Cancellation reason.

Note where Reason code NARR is used additional information must be provided to describe the reason for the Cancellation request.

In the event that an **indemnity agreement** is need to be established, **INDM** should be indicated at the beginning of the Additional Information element. Any subsequent additional information may then

---

<!-- Page 761 -->

Min 0 – Max 1

Definitions and High Level Use Cases

The Resolution of Investigation **Reason** *element* is optional. CBPR+ have defined a sub-set of the ISO externalised code list which is represented as an embedded `Code` choice. This list ensures interoperability with the legacy FIN request for Cancellation message, which can be broadened after the coexistence period.

| Code | Name | Definition | Use Case |
| :--- | :--- | :--- | :--- |
| AC04 | Closed Account Number | Account number specified has been closed on the receiver's books. | Complimenting a Reject Status. Payment Cancellation Request can not be accepted as the Creditor has since closed their account. |
| AGNT | Agent Decision | Reported when the cancellation cannot be accepted because of an agent refuses to cancel. | Complimenting a Reject Status. Payment Cancellation Request can not be accepted as an Agent in the payment transaction does not accept the request. |
| AM04 | Insufficient Funds | Amount of funds available to cover specified message amount is insufficient. | Complimenting a Reject Status. Payment Cancellation Request can not be accepted as the Creditor has insufficient funds to perform the return payment. |
| ARDT | Already Returned | Cancellation not accepted as the transaction has already been returned. | Complimenting a Reject Status. Payment Cancellation Request can not be accepted as the payment has already return payment. |
| CUST | Customer Decision | Reported when the cancellation cannot be accepted because of a customer decision (Creditor). | Complimenting a Reject Status. Payment Cancellation Request can not be accepted as the Creditor does not provide authority to return the payment. i.e. believe the payment was justified. |
| INDM | Indemnity Request | Indemnity is required before funds can be returned | Complimenting a Pending or Reject Status. Payment Cancellation Request can not be accepted until an indemnity agreement is established. |

---

<!-- Page 762 -->

Definitions and High Level Use Cases

| LEGl | Legal Decision | Reported when the cancellation cannot be accepted because of regulatory rules. |  |
|---|---|---|---|
| NAAR | Narrative | Reason is provided as narrative information in the additional reason information. | Complimenting a **Reject** or **Pending** Status to provide further narrative *Additional Information*. |
| NOAS | No Answer From Customer | No response from beneficiary (to the cancellation request). | Complimenting a **Reject** Status. Payment Cancellation Request can not be accepted as the Creditor has not responded to a Debit Authority request to return the payment. |
| NOOR | No Original Transaction Received | Original transaction (subject to cancellation) never received. | Complimenting a **Reject** Status. Payment Cancellation Request can not be accepted as it is believed that the original payment was never received for the UETR and references provided. |
| PTNA | Passed To The Next Agent | Reported when the cancellation request cannot be accepted because the payment instruction has been passed to the next agent. | Complimenting a **Pending** Status. Payment has been onward processed to the next agent in the transaction. The Payment Cancellation Request has therefore been forward to this Agent, a further resolution message will be sent once this Agent provides a response. |
| RQDA | Requesting Debit Authority | Reported when authority is required by the Creditor to return the payment. | Complimenting a **Pending** Status. Payment has been credited to the creditor. Authority to Debit the Creditor and return the payment is being request. A further resolution message will be sent once the Creditor provides a response. |

---

<!-- Page 763 -->

Use case should be considered as a principal example whereby use case may be cross referenced

**Resolution of Investigation**

Use Case c.29.1.1 – High Level Resolution of Investigation (camt.029) of a completed Customer Credit Transfer (pacs.008)
Use Case c.29.1.1.a – High Level Resolution of Investigation (camt.029) of a completed Customer Credit Transfer (pacs.008) using Gpi Stop and Recall
Use Case c.29.1.2 – High Level Resolution of Investigation (camt.029) of an incomplete Customer Credit Transfer (pacs.008)
Use Case c.29.1.2.a – High Level Resolution of Investigation (camt.029) of an incomplete Customer Credit Transfer (pacs.008) using gpi Stop and Recall
Use Case c.29.2.1 – High Level Resolution of Investigation (camt.029) of a complete Customer Credit Transfers (pacs.008) settled using the cover method
Use Case c.29.2.2 – High Level Resolution of Investigation (camt.029) of an incomplete Customer Credit Transfers (pacs.008) settled using the cover method
Use Case c.29.2.3 – High Level Resolution of Investigation (camt.029) of a Customer Credit Transfers (pacs.008) where the cover is returned
Use Case c.29.3.1 – High Level Resolution of Investigation (camt.029) of a Financial Institution Credit Transfer (pacs.009)
Use Case c.29.4.1 – High Level Resolution of Investigation (camt.029) of a Financial Institution Credit Transfer advice (pacs.009 adv)

---

<!-- Page 764 -->

# Transfer (pacs.008)

pacs.008 / camt.056 — camt.029 (4)
pacs.008 / camt.056 — camt.029 (3)
pacs.008 — camt.029 (2)
pacs.008 / camt.056 — camt.029 (1)

**1**
Agent D provides a final outcome of the investigation to Agent C using the camt.029.

**2**
Debtor Agent (C) updates their case history and relays the outcome of the investigation to Agent B using the camt.029

**3**
Debtor Agent (B) updates their case history and relays the outcome of the investigation to Agent A using the camt.029

**4**
Debtor Agent (A) updates their case history and informs the customer of the outcome of the investigation.

> See use case p.8.1.1 for the original payment, c.56.1.1 for case resolution and p.4.1.3. for an example payment return

---

<!-- Page 765 -->

# Transfer (pacs.008) using gpi Stop and Recall

**Diagram Flow:**

*   **Top Row (gpi messages):**
    *   `3` $\xrightarrow{\text{camt.056}}$ `2` (gpi) $\xrightarrow{\text{camt.056}}$ `1`
    *   `2` (gpi) $\xrightarrow{\text{camt.029}}$ `3`
    *   `1` $\xrightarrow{\text{camt.029}}$ `2` (gpi)
*   **Bottom Row (pacs messages):**
    *   `A` $\xrightarrow{\text{pacs.008}}$ `B` $\xrightarrow{\text{pacs.008}}$ `C` $\xrightarrow{\text{pacs.008}}$ `D`

**Note (Right):**
See use case p.8.1.1 for the original payment, c.29.1.1 for case resolution and p.4.1.3. for an example payment return

**Step 1:**
Agent D provides an update on the investigation to the gpi Tracker using the camt.029.

**Step 2:**
gpi Tracker forwards the response to Agent A as the initiator of the original camt.056

**Step 3:**
Debtor Agent (A) updates their case history and informs the customer of the outcome of the investigation.

---

<!-- Page 766 -->

# Credit Transfer (pacs.008)

pacs.008
camt.056
pacs.008
camt.056
pacs.008
camt.029
camt.029

**1**
Agent C provides a final outcome of the investigation to Agent B using the camt.029

**2**
Debtor Agent (B) updates their case history, and relays the outcome of the investigation to

**3**
Debtor Agent (A) updates their case history and informs the customer of the outcome of the investigation.

See **use case** p.8.1.1 for the original payment, c.56.1.2 for case resolution and p.4.1.3. for an example payment return

---

<!-- Page 767 -->

# Credit Transfer (pacs.008) using gpi Stop and Recall

**Diagram Labels:**
*   3
*   camt.056
*   camt.029
*   gpi
*   2
*   camt.056
*   camt.029
*   1
*   A
*   pacs.008
*   B
*   pacs.008
*   C
*   pacs.008
*   D

**1**
Agent C provides an update on the investigation to the gpi Tracker using the camt.029.

**2**
gpi Tracker forwards the response to Agent A as the initiator of the original camt.056

**3**
Debtor Agent (A) updates their case history and informs the customer of the outcome of the investigation.

---

<!-- Page 768 -->

# Transfer (pacs.008) settled using a cover method

pacs.008
pacs.002
camt.056
camt.029
pacs.009 cov
pacs.002
pacs.009 cov
camt.053
camt.054
Settlement Complete

**1**
Debtor request their bank to recall a previous instructed payment, as the amount was incorrect.

**2**
Debtor Agent (A) assigns a Cancellation Request to Agent D (assignee) requesting the original pacs.008 is returned, using reason code AM09.

**3**
Agent D creates an investigation case. Recognising the payment has already been credited to the creditor. They request debit authority, proving the reason specified for the return request and update Agent A.
Once the outcome to the debit authorisation is know a final resolution to the investigation can be relayed and any necessary

See use case p.8.2.1 for the original payment, c.56.2.1 for case resolution and p.4.3.2 for an example payment return

---

<!-- Page 769 -->

# Credit Transfer (pacs.008) settled using a cover method.

**Diagram flow:**

- Person → **A** (bank) → **D** (bank) → Person
- A → B (bank) → (bank) → C (bank) → D
- Messages: `pacs.008`, `camt.056`, `camt.029`, `pacs.009 cov`, `pacs.002`, `camt.053`, `camt.054`
- **Settlement Complete**

> See use case p.8.2.1 for the original payment, c.29.2.1 for case resolution and p.4.3.2 for an example payment return

**1**
Debtor request their bank to recall a previous instructed payment, as the amount was incorrect.

**2**
Debtor Agent (A) assigns a Cancellation Request to Agent D (assignee) requesting the original pacs.008 is returned, using reason code AM09.

**3**
Agent D creates an investigation case. Recognising the payment has not been credited to the creditor. They update Agent A that the Cancellation Request is accepted and arrange the necessary return payment once the pacs.009 cov settlement is confirmed by Agent C

---

<!-- Page 770 -->

# Transfers (pacs.008) where the cover is returned

**Flow / Message sequence**

- **A** (Debtor Agent) → **D** (Creditor Agent): `pacs.008`, `camt.056`  *(step 1)*
- **D** → **A**: `camt.029`  *(step 2)*
- **A** → **B**: `pacs.009 cov`
- **B** → **A**: `pacs.004`  →  **+ Return Reason**
- **B** → **C**: `pacs.009 cov`  *(!)*
- **C** → **B**: `pacs.002`  →  **+ Reject Reason**

> **Note:** See use case p.8.2.1 for an example of a cover payment c.56.2.1 for case resolution and p.4.3.3 for payment return

---

**!** Agent C receives the payment and recognises the payment can not be completed as requested e.g. the Agent D does not maintain an account with them.

**1** Debtor Agent (A) assigns a Cancellation Request to Agent D (assignee) requesting the original pacs.008 is considered null and void, using reason code COVR.

**2** Agent D creates an investigation case. Recognising the cover payment will not be received to settle the pacs.008. As the creditor has not been credited in advance of cover settlement, a final resolution to the investigation can be provided. A payment return is not necessary.

---

<!-- Page 771 -->

# Credit Transfer (pacs.009)

**Diagram Flow:**

*   **A → B**: `pacs.009`, `pacs.002`, `camt.056`
*   **B → C**: `pacs.009`, `pacs.002`, `camt.056`
*   **C → D**: `pacs.009`, `camt.053`, `camt.054`
*   **C → B** (Step 1): `camt.029`
*   **B → A** (Step 2): `camt.029`

> **Note:** See use case p.9.1.1 for the cover payment sample c.56.3.1 for case resolution and p.4.2.3 for payment return

**1**
Agent C provides a final outcome of the investigation to Agent B using the camt.029.

**2**
Debtor Agent (B) updates their case history and informs the customer (Agent A) of the outcome of the investigation.

---

<!-- Page 772 -->

# Credit Transfer advice (pacs.009 adv)

**Diagram labels (sequence flow):**

- Node **A** → Node **B** (step **1**)
- Node **B** → Node **E** (step **2**): `pacs.009 (ADV)`, `camt.056`, `camt.029`
- Node **E** → Node **F** (step **3**): `camt.054`
- Node **B** ↔ Node **C**: `pacs.009`, `pacs.002`
- Node **C** ↔ Node **D**: `pacs.009`, `pacs.002`
- Node **D** ↔ Node **E**: `camt.053`, `camt.054`

> See use case p.9.1.2 for the cover payment sample c.56.4.1 for case resolution and p.4.2.3 for payment return

**1**
Debtor request their bank to recall a previous instructed payment, as the amount was incorrect.

**2**
Debtor Agent (A) assigns a Cancellation Request to Agent E (assignee) requesting the original pacs.008 is returned, using reason code AM09.

**3**
Agent E creates an investigation case. Recognising the payment has already been credited to the creditor. They request debit authority, proving the reason specified for the return request and update Agent B.
Once the outcome to the debit authorisation is know a final resolution to the investigation can be relayed and any necessary

---

<!-- Page 773 -->

# Customer Payment
# Cancellation Request

---

<!-- Page 774 -->

camt.055

- Assignment
- Underlying

The Customer Payment Cancellation Request message is sent by an Agent to request the Cancellation of a payment initiation request previous sent.

The message is sent either:
- directly to the Agent a previous Payment initiation request was sent to.

---

<!-- Page 775 -->

Debitors
Initiating Party
Forwarding Agent
Debtor Agent
Creditor Agent
Creditor

| pain.001 | Interbank pain.001 |
| pain.002 | Interbank pain.002 | pacs.008 |
| camt.055 | camt.055 | pacs.002 | camt.053 |
| camt.029 | camt.029 | camt.056 |
| | | camt.029 |

The CustomerPaymentCancellationRequest message is sent by a case creator/case assigner to a case assignee. This message is used to request the cancellation of an original payment instruction (pre or post settlement to the Creditor). The

---

<!-- Page 776 -->

# Initiation"

Debtor | Initiating Party | Debtor Agent | Creditor Agent | Creditor

| Initiating Party | Debtor Agent | Creditor Agent | Creditor |
|---|---|---|---|
| Interbank pain.001 | | | |
| | Interbank pain.002 | pacs.008 | |
| camt.055 | pacs.002 | camt.053 | |
| camt.029 | camt.056 | | |
| | camt.029 | | |

> **The CustomerPaymentCancellationRequest message is sent by a case creator/case assigner to a case assignee. This message is used to request the cancellation of an original payment instruction (pre or post settlement to the Creditor). The**

---

<!-- Page 777 -->

Debtor | Initiating Party | Debtor Agent | Creditor Agent | Creditor

- Interbank pain.001
- Interbank pain.002
- pacs.008
- camt.055
- pacs.002
- pacs.008
- camt.029
- camt.056
- pacs.002
- camt.053
- camt.029
- camt.056
- camt.029

The CustomerPaymentCancellationRequest message is sent by a case creator/case assigner to a case assignee. This message is used to request the cancellation of an original payment instruction (pre or post settlement to the Creditor). The

---

<!-- Page 778 -->

The camt.056 Payment Cancellation Request and camt.029 Resolution of Investigation messages have a number of identification elements, of which some are used for cross referencing. The below provides a high level overview.

Cancel & return my payment please

Customer X

CASE123

STAT789

CASE123
STAT789

OK, I can understand the mistake.

Customer Y

ISO

ISO

### Camt.055 Payment Cancellation Request

| element | description | example |
|---|---|---|
| Assigner | Sender of the camt.055 | Agent A |
| Assignee | Receiver of the camt.055 | Agent B |
| Assignment Identification | Unique Id generated by the assigner to identify the Payment Cancellation Request message | CASE123/1 |
| Cancellation Identification | Optional Cancellation Id of the Agent sending (assigner) the Payment Cancellation Request message. | CASE123 |
| Case Identification | Case Id of the Agent sending (assigner) the Payment Cancellation Request message. | CASE123 |
| Case Creator | Party who created the original cancellation request (who may be another Agent other than the current Assigner. | Agent A |

### camt.029 Resolution of Investigation

| element | description | example |
|---|---|---|
| Assigner | Sender of the camt.029 | Agent |
| Assignee | Receiver of the camt.029 | Agent A |
| Assignment Identification | Unique Id generated by the assigner to identify the Resolution of Investigation message | STAT789/1 |
| Cancellation Identification | Case Reference of the Agent sending (assigner) the Resolution of Investigation message. | STAT789 |
| Resolved Case Identification | Case Id of the original case the Resolution of Investigation is responding to. | CASE123 |
| Case Creator | Party who created the original cancellation request (who is the same original case creator in the Payment Cancellation Request) | Agent A |

---

<!-- Page 779 -->

# Assignment

---

<!-- Page 780 -->

Min 1 – Max 1

The Payment Cancellation Request message *Identification* provides a mandatory element to identify the Request

Unique reference assigned by the assigner to unambiguously identify the Cancellation request.
For Exceptions and Investigations messages the Identification has no exact equivalent in the legacy MT Exceptions and Investigations message. However, the Transaction Reference Number (Field 20) could be considered a similar comparison.
Directly comparable with the *Transaction Reference Number* (Field 20) of the legacy MT statement message.

---

<!-- Page 781 -->

pain.001
camt.055
camt.029
pacs.008
camt.056
camt.029

| Assigner Agent: Agent A | Assignee Agent: Agent B | Assigner Agent: Agent B | Assignee Agent: Agent C |
|---|---|---|---|

**Assigner** and **Assignee** represent the Agents involved in the point-to-point investigation message exchange. These roles therefore change on each message leg.

Assignment
Assigner

---

<!-- Page 782 -->

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+-hh:mm
> For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

Group Header Creation Date Time

---

<!-- Page 783 -->

# Underlying = Original Payment Information and Cancellation.

---

<!-- Page 784 -->

# Identification

Min 1 – Max 1

The Payment Cancellation Request message **Original Payment Information Identification** provides a mandatory element to identify the Original Payment Initiation Request

This **Unique reference** identifies the Payment Information Identification from the original Payment Initiation request.

Refer to the relevant Payment Information Identification element in the original message for details on that reference.

Link to Pain.001

Link to Pain.008

| Assignment | Identification | xyz9875 |
|---|---|---|
| Underlying | Original Payment Information Identification | abcd1234 |
| | Original Group Information | Original Message Identification | abcd1234 |
| | | Original Message Name Identification | pain.001.09.09 |

Underlying > Original Payment Information and Cancellation >

---

<!-- Page 785 -->

Min 1 – Max 1

The Payment Cancellation Request uses elements in the **Original Group Information** to capture the message identifier and message name of the underlying payment for which the Cancellation is being requested. The mandatory **Original Message Identification** contains the point-to-point reference from this payment, and the mandatory **Original Message Name Identification** contains the message name of the underlying payment. Optionally the **Original Creation Date Time** can also be captured.

For example:

*Original Message Name Identification* "pain.001.001.09" confirms the Cancellation request is for a pain.001 Interbank Customer Credit Transfer Initiation.

| | | |
|---|---|---|
| **pain.001** | | |
| Message Identification | abcd1234 | |
| Payment Information Identification | abcd1234 | |
| **camt.055** | | |
| **Assignment** | **Identification** | xyz9875 |
| **Underlying** | Original Payment Information Identification | abcd1234 |
| **Underlying** | **Original Group** | Original Message Identification | abcd1234 |
| | | Original Message Name... |

Note: the xx in the CBPR+ Usage Guideline represents the message version of the message

---

<!-- Page 786 -->

Min 0 – Max 1

The Payment Cancellation Request message ***Cancellation Identification*** provides an optional element to identify the Request

***Unique reference*** assigned by the assigner to unambiguously identify the Cancellation request.

For Exceptions and Investigations messages the *Cancellation Identification* can be considered an equivalent in the legacy MT Directly comparable with the *Transaction Reference Number* (Field 20) of the legacy MT statement message.

Underlying > Original Payment Information and Cancellation >
Transaction Identification > Cancellation Identification

---

<!-- Page 787 -->

Min 1 – Max 1
The Payment Cancellation Request message **_Case_** provides a mandatory nested element to identify the Case **_Identification_** and the **_Creator_** of the case.

Min 1 – Max 1
The **_Identification_** element captures a unique case reference assigned by the assigner to unambiguously identify the Cancellation investigation case. For Exceptions and Investigations messages the Case _Identification_ can be considered an equivalent of the _Transaction Reference Number_ (Field 20) of the legacy MT Request for Cancellation message.

Min 1 – Max 1
The **_Creator_** element captures the party who created the investigation. This mandatory party can represent as either an **_Agent_** i.e., the Bank who created the case or as a **_Party_** i.e., the customer (for example the Debtor) who created the request. In CBPR+ the creator is always expected to be an Agent. This element has no equivalent in the legacy MT Request for Cancellation message.

Underlying > Original Payment Information and Cancellation > Transaction Identification > Case

---

<!-- Page 788 -->

The Payment Cancellation Request also uses a number of other **Original** elements in the *Transaction Information* to capture information from the underlying payment that the Cancellation request relates to.

The Original elements enables the **Assignee** to identify the Payment which is being request to be cancelled. The following element (in addition to *Original Message identification* and *Original Message Name Identification*) are mandated:

| | |
|---|---|
| **Original End to End Identification** | Min 1 – Max 1 |
| **Original UETR** | Min 1 – Max 1 |
| **Original Instructed Amount** | Min 1 – Max 1 |

One of the following elements is also required depending on the Date element in the original message, where Original Request Execution Date relates to the pain.001 and Original Request Collection Date relates to the pain.008 :

| | |
|---|---|
| **Original Requested Execution Date** | Min 0 – Max 1 |
| **Original Request Collection Date** | Min 0 – Max 1 |

The following element is optional:

- Underlying
  - Original Payment Information and Cancellation
    - Transaction Information
      - Original Instruction Identification
      - Original End to End Identification
      - Original UETR
      - Original Instructed Amount
      - Original Requested Execution Date

---

<!-- Page 789 -->

The Payment Cancellation Request **Cancellation Reason Information** nested element captures information associated with the reason for the Cancellation request.

Min 0 – Max 1
**Originator** element helps identify the party who request the payment Cancellation. This party would have been included in the underlying payment and is also included the pacs.004 *Return Chain as the Creditor*.

Min 1 – Max 1
the **Reason** is mandatory and represented by an embedded CBPR+ Cancellation **Code** choice (↔)

Min 0 – Max 2
the **Additional Information** element may also be included to provide **further** details on the Cancellation reason.

🧠 Note where Reason code NARR is used additional information must be provided to describe the reason for the Cancellation request.

Underlying > Original Payment Information and Cancellation >
Transaction Information > Cancellation Reason Info >
> Originator
> Reason

---

<!-- Page 790 -->

Definitions and High Level Use Cases

Min 1 – Max 1

The Payment Cancellation Request **<u>Reason</u>** element is mandatory. CBPR+ have defined a sub-set of the ISO externalised code list which is represented as an embedded **Code** choice. This list ensures interoperability with the legacy FIN request for Cancellation message, which can be broadened *after* the coexistence period.

| Code | Name | Definition | Use Case |
| :--- | :--- | :--- | :--- |
| AGNT | Incorrect Agent | Agent in the payment workflow is incorrect. | A payment previous executed is identified as containing an incorrect correspondent (Agent) within the payment flow. A Cancellation request is generated so that the payment can be remediated following the successful return. |
| AM09 | Wrong Amount | Amount is not the amount agreed or expected. | The customer (Debtor) requests the initiation of a payment from their bank account, but subsequently realizes they had provided an incorrect amount. |
| CURR | Incorrect Currency | Currency of the payment is incorrect. | The customer (Debtor) requests the initiation of a payment from their bank account, but subsequently realizes they requested the wrong currency, as the payment has been executed. They request their bank to recall the funds so that the payment can be re-executed in the correct currency |
| CUST | Requested By Customer | Cancellation requested by the Debtor. | The customer (Debtor) requests the initiation of a payment from their bank account, but subsequently wishes to recall the payment. The exactly underlying reason for the customer request is either not specified by the customer or is not aligned to a more specific reason and therefore is not appropriate. |

---

<!-- Page 791 -->

(continued)

Definitions and High Level Use Cases

| Code | Name | Definition | Use Case |
|---|---|---|---|
| CUTA | Cancel Upon Unable To Apply | Cancellation requested because an investigation request has been received and no remediation is possible. | An error occurred in the original payment (such as incorrect information) which was highlighted as part of an Investigation query. The request to cancel complements a response to the Investigation. |
| DUPL | Duplicate Payment | Payment is a duplicate of another payment. | A customer (Debtor) requests the initiation of a payment from their bank account, but subsequently initiates a new (separate) payment request in duplication of a previous payment. Having realized the error, the customer requests the recall of the duplicate transaction. |
| FRAD | Fraudulent Origin | Cancellation requested following a transaction that was originated fraudulently. The use of the Fraudulent Origin code should be governed by jurisdictions. | Either the customer (Debtor) or a bank (Agent) in the payment transaction experiences an activity which causes a payment to be executed by alleged fraudulent means. |
| NARR | Narrative | Narrative reason provided in the Additional Information. | Used only where a more specific reason is not appropriate. Narrative description is provided. |
| TECH | Technical Problem | Cancellation requested following technical problems resulting in an erroneous transaction. | Either the customer (Debtor) or a bank (Agent) in the payment flow experiences a technology issue which causes data within a payment to be incorrect. |
| UPAY | Undue Payment | Payment is not justified. | Either the customer (Debtor) or a bank (Agent) in the payment flow experiences an activity which causes a payment to be executed under unexpected circumstances. |

---

<!-- Page 792 -->

| Use case should be considered as a principal example whereby use case may be cross referenced |
|---|

**Payment Cancellation Request**

Use Case c.55.1.1 –

---

<!-- Page 793 -->

In the interbank relay scenario, the Forwarding Agent relays the pain.008 message to the Creditor Agent to request the collections of funds from the debtor's accounts for a creditor.

**Message Flow Diagram**

Nodes (left → right): Customer — Bank **B** — Bank **A** (step 3) — Bank **F** (step 2) — Customer (step 1)

| From | To | Message | Direction |
|------|----|---------|-----------|
| Customer (1) | Bank F (2) | pain.008 | → F |
| Customer (1) | Bank F (2) | pain.002 (dashed) | → F |
| Bank F (2) | Customer (1) | camt.055 | → Customer |
| Bank F (2) | Customer (1) | camt.029 | → Customer |
| Bank F (2) | Bank A (3) | Interbank pain.008 | → A |
| Bank F (2) | Bank A (3) | Interbank pain.002 (dashed) | → A |
| Bank F (2) | Bank A (3) | camt.055 | → A |
| Bank A (3) | Bank F (2) | camt.029 | → F |
| Bank A (3) | Bank B | pacs.003 | → B |
| Bank A (3) | Bank B | camt.056 | → B |
| Bank B | Bank A (3) | camt.029 | → A |
| Bank B | Customer | camt.053 | → Customer |

**Step Descriptions**

1. Creditor request the recall a previous instructed Direct Debit collection, as the amount was incorrect.

2. Forwarding Agent (F) assigns a Customer Cancellation Request to Agent A (assignee) requesting the original pain.008 is cancelled, using reason code AM09.

3. Creditor Agent (A) assigns a Cancellation Request to Agent B (assignee) requesting the original pacs.003 is cancelled, using reason code AM09.

---

<!-- Page 794 -->

# Payment Market Infrastructure

In the interbank relay scenario, the Forwarding Agent relays the pain.008 message to the Creditor Agent to request the collection of funds from the debtor's accounts for a creditor (through a Payment Market Infrastructure).

**Diagram Flow & Messages:**

*   **Entities (Left to Right):** Creditor (Person), Agent B (Bank), Agent A (Bank), Forwarding Agent F (Bank), Debitor (Person)
*   **Top Message Flow:**
    *   pain.008 / pain.002
    *   Interbank pain.008 / Interbank pain.002
    *   pac.003 / pac.003
*   **Bottom Message Flow:**
    *   camt.056 / camt.029
    *   camt.055 / camt.029
    *   camt.055 / camt.029

**Legend:**

1.  **Creditor request the recall a previous instructed Direct Debit collection, as the amount was incorrect.**
2.  **Forwarding Agent (F) assigns a Customer Cancellation Request to Agent A (assignee) requesting the original pain.008 is cancelled, using reason code AM09.**
3.  **Creditor Agent (A) assigns a Cancellation Request to Agent B (assignee) requesting the original pac.003 is cancelled, using reason code AM09.**

---

<!-- Page 795 -->

# Financial Institution to Financial Institution Payment Cancellation Request

---

<!-- Page 796 -->

camt.056

- Assignment
- Underlying

The FI to FI Payment Cancellation Request message is sent by an Agent to request the Cancellation of a payment previous sent.

The message is sent either:
- directly (through the SWIFT Community CASE solution), or
- serially through other agents.

It is not recommended to request a Payment Cancellation Request (camt.056) of a Payment Return (pacs.004) instead an Exception and Investigation should be initiated to resolve this

---

<!-- Page 797 -->

A &nbsp;&nbsp;&nbsp;&nbsp; B &nbsp;&nbsp;&nbsp;&nbsp; C

pacs.008

pacs.002

camt.055 &nbsp;&nbsp;&nbsp;&nbsp; camt.056 &nbsp;&nbsp;&nbsp;&nbsp; camt.056 &nbsp;&nbsp;&nbsp;&nbsp; camt.053

camt.029 &nbsp;&nbsp;&nbsp;&nbsp; camt.029

> The FItToFIPaymentCancellationRequest message is sent by a case creator/case assigner to a case assignee. This message is used to request the cancellation of an original payment instruction (pre or post settlement to the Creditor). The FItToFIPaymentCancellationRequest message is exchanged between the payment Instruction Agent and the Instructed

---

<!-- Page 798 -->

```
→
A → B  pacs.008
B ⇢ A
B ⇢ A  pacs.002
→ A  camt.055
B → C  pacs.008
A → C  camt.056
C → →  camt.053
→ C
C → A  camt.029
A →
```

The FIToFIPaymentCancellationRequest message is sent by a case creator/case assigner to a case assignee. This message is used to request the cancellation of an original payment instruction (pre or post settlement to the Creditor). The FIToFIPaymentCancellationRequest message is exchanged between the payment Instruction Agent and the Instructed

---

<!-- Page 799 -->

The camt.056 Payment Cancellation Request and camt.029 Resolution of Investigation messages have a number of identification elements, of which some are used for cross referencing. The below provides a high level overview.

Cancel & return my payment please

Customer X

CASE123 - STAT789

CASE123

STAT789

CASE123 - STAT789

OK, I can understand the mistake.

Customer Y

ISO

ISO

| **Camt.056 Payment Cancellation Request** | | | **Camt.029 Resolution of Investigation** | | |
|---|---|---|---|---|---|
| **element** | **description** | **example** | **element** | **description** | **example** |
| Assigner | Sender of the camt.056 | Agent B | Assigner | Sender of the camt.029 | Agent C |
| Assignee | Receiver of the camt.056 | Agent C | Assignee | Receiver of the camt.029 | Agent B |
| Assignment Identification | Unique Id generated by the assigner to identify the Payment Cancellation Request message | CASE123/1 | Assignment Identification | Unique Id generated by the assigner to identify the Resolution of Investigation message | STAT789/1 |
| Cancellation Identification | Optional Cancellation Id of the Agent sending (assigner) the Payment Cancellation Request message. | CASE123 | Cancellation Identification | Case Reference of the Agent sending (assigner) the Resolution of Investigation message. | STAT789 |
| Case Identification | Case Id of the Agent sending (assigner) the Payment Cancellation Request message. | CASE123 | Resolved (Original) Case Identification | Case Id of the original case the Resolution of Investigation is responding to. | CASE123 |
| Case Creator | Party who created the original cancellation request (who may be another Agent other than the current Assigner. | Agent A | Case Creator | Party who created the original cancellation request (who is the same original case creator in the Payment Cancellation Request) | Agent A |

---

<!-- Page 800 -->

# Assignment

---

<!-- Page 801 -->

Min 1 – Max 1

The Payment Cancellation Request message *Identification* provides a mandatory element to identify the Request

Unique reference assigned by the assigner to unambiguously identify the Cancellation request.
For Exceptions and Investigations messages the Identification has no exact equivalent in the legacy MT Exceptions and Investigations message. However, the Transaction Reference Number (Field 20) could be considered a similar comparison.
Directly comparable with the *Transaction Reference Number* (Field 20) of the legacy MT statement message.

---

<!-- Page 802 -->

A

B

C

D

pac.008

camt.056

camt.029

**Assigner Agent: Agent A**

**Assignee Agent: Agent B**

pac.008

camt.056

camt.029

**Assigner Agent: Agent B**

**Assignee Agent: C**

***Assigner*** and ***Assignee*** represent the Agents involved in the point-to-point investigation message exchange. These roles therefore change on each message leg.

Assignment

Assigner

---

<!-- Page 803 -->

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+-hh:mm
> For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

Group Header Creation Date Time

---

<!-- Page 804 -->

# Underlying - Transaction Information

---

<!-- Page 805 -->

Min 0 – Max 1

The Payment Cancellation Request message **Cancellation Identification** provides an optional element to identify the Request

Unique reference assigned by the assigner to unambiguously identify the Cancellation request.

For Exceptions and Investigations messages the *Cancellation Identification* can be considered an equivalent in the legacy MT Directly comparable with the *Transaction Reference Number* (Field 20) of the legacy MT statement message.

Where Cancellation Identification is used this should represent the reference value as the **Case Identification**

Underlying > Transaction Information > Cancellation Identification

---

<!-- Page 806 -->

Min 1 – Max 1
The Payment Cancellation Request message **Case** provides a mandatory nested element to identify the Case *Identification* and the *Creator* of the case.

Min 1 – Max 1
The **Identification** element captures a unique case reference assigned by the assigner to unambiguously identify the Cancellation investigation case.
For Exceptions and Investigations messages the Case *Identification* can be considered an equivalent of the *Transaction Reference Number* (Field 20) of the legacy MT Request for Cancellation message.

Min 1 – Max 1
The **Creator** element captures the party who created the investigation. This mandatory party can represent as either an **Agent** i.e., the Bank who created the case or as a **Party** i.e., the customer (for example the Debtor) who created the request. In CBPR+ the creator is always expected to be an Agent.
This element has no equivalent in the legacy MT Request for Cancellation message.

Underlying > Transaction Information
> Case

---

<!-- Page 807 -->

The Payment Cancellation Request uses elements in the **Original Group Information** to capture the message identifier and message name of the underlying payment for which the Cancellation is being requested. The mandatory **Original Message Identification** contains the point-to-point reference from this payment, and the mandatory **Original Message Name Identification** contains the message name of the underlying payment. Optionally the **Original Creation Date Time** can also be captured.

For example:

*Original Message Name Identification* “pacs.008.001.08” confirms the Cancellation request is for a pacs.008 Financial Institution to Financial Institution Customer Credit Transfer. Where as “pacs.009.001.08” confirms the Cancellation request for a pacs.009 Financial Institution Credit Transfer.

Min 1 – Max 1

| | | |
|---|---|---|
| **Assignment** | Identification | xyz9875 |
| **Underlying** | **Original Group** | Original Message Identification | abcd1234 |
| | | Original Message |

Note: the xx in the CBPR+ Usage Guideline represents the message version of the message

---

<!-- Page 808 -->

The Payment Cancellation Request also uses a number of other **Original** elements in the *Transaction Information* to capture information from the underlying payment that the Cancellation request relates to.

The Original elements enables the **Assignee** to identify the Payment which is being request to be cancelled. The following element (in addition to *Original Message identification* and *Original Message Name Identification* described on the previous page) are mandated:

| | |
|---|---|
| **Original End to End Identification** | Min 1 – Max 1 |
| **Original UETR** | Min 1 – Max 1 |
| **Original Interbank Settlement Amount** | Min 1 – Max 1 |
| **Original Interbank Settlement Date** | Min 1 – Max 1 |

The following element (in addition to *Original Message identification* and *Original Message Name Identification* described on the previous page) are optional:

| | |
|---|---|
| **Original Instruction Identification** | Min 0 – Max 1 |
| **Original Transaction Identification** | Min 0 – Max 1 |
| **Original Clearing System Reference** | Min 0 – Max 1 |

Underlying > Transaction Information >
- Original Instruction Identification
- Original End to End Identification
- Original Transaction
- Original UETR
- Original Clearing System Reference
- Original Interbank Settlement Amount

---

<!-- Page 809 -->

The Payment Cancellation Request **Cancellation Reason Information** nested element captures information associated with the reason for the Cancellation request.

`Min 1 – Max 1`

the **Originator** element helps identify the party who request the payment Cancellation. This party would have been included in the underlying payment and is also included the pacs.004 *Return Chain as the Creditor*.

`Min 1 – Max 1`

the **Reason** is mandatory and represented by an embedded CBPR+ Cancellation **Code** choice (↵)

`Min 0 – Max 2`

the **Additional Information** element may also be included to provide **further** details on the Cancellation reason.

Note where Reason code NARR is used additional information must be provided to describe the reason for the Cancellation request.

`Underlying Transaction Information > Cancellation Reason Info`

In the event that the case assigner wishes it indicate a willingness to establish an **indemnity agreement** **INDM** should be indicated at the

- Originator
- Reason

---

<!-- Page 810 -->

Min 1 – Max 1

Definitions and High Level Use Cases

The Payment Cancellation Request **Reason** element is mandatory. CBPR+ have defined a sub-set of the ISO externalised code list which is represented as an embedded `Code` choice. This list ensures interoperability with the legacy FIN request for Cancellation message, which can be broadened *after* the coexistence period.

| Code | Name | Definition | Use Case |
| :--- | :--- | :--- | :--- |
| AGNT | Incorrect Agent | Agent in the payment workflow is incorrect. | A payment previous executed is identified as containing an incorrect correspondent (Agent) within the payment flow. A Cancellation request is generated so that the payment can be remediated following the successful return. |
| AM09 | Wrong Amount | Amount is not the amount agreed or expected. | The customer (Debtor) requests the initiation of a payment from their bank account, but subsequently realizes they had provided an incorrect amount. |
| COVR | Cover Cancelled Or Returned | Cover payments has either been returned or cancelled. | Identifies an Agent to request the Cancellation of a pacs message where settlement method was COVE and the covering payment has been cancelled or returned. |
| CURR | Incorrect Currency | Currency of the payment is incorrect. | The customer (Debtor) requests the initiation of a payment from their bank account, but subsequently realizes they requested the wrong currency, as the payment has been executed. They request their bank to recall the funds so that the payment can be re-executed in the correct currency |
| CUST | Requested By Customer | Cancellation requested by the Debtor. | The customer (Debtor) requests the initiation of a payment from their bank account, but subsequently wishes to recall the payment. The exactly underlying reason for the customer request is either not specified by the customer or is not aligned to a more specific reason and therefore is not

---

<!-- Page 811 -->

(continued)

Definitions and High Level Use Cases

| Code | Name | Definition | Use Case |
|---|---|---|---|
| CUTA | Cancel Upon Unable To Apply | Cancellation requested because an investigation request has been received and no remediation is possible. | An error occurred in the original payment (such as incorrect information) which was highlighted as part of an Investigation query. The request to cancel complements a response to the Investigation. |
| DUPL | Duplicate Payment | Payment is a duplicate of another payment. | A customer (Debtor) requests the initiation of a payment from their bank account, but subsequently initiates a new (separate) payment request in duplication of a previous payment. Having realized the error, the customer requests the recall of the duplicate transaction. |
| FRAD | Fraudulent Origin | Cancellation requested following a transaction that was originated fraudulently. The use of the Fraudulent Origin code should be governed by jurisdictions. | Either the customer (Debtor) or a bank (Agent) in the payment transaction experiences an activity which causes a payment to be executed by alleged fraudulent means. |
| NARR | Narrative | Narrative reason provided in the Additional Information. | Used only where a more specific reason is not appropriate. Narrative description is provided. |
| TECH | Technical Problem | Cancellation requested following technical problems resulting in an erroneous transaction. | Either the customer (Debtor) or a bank (Agent) in the payment flow experiences a technology issue which causes data within a payment to be incorrect. |
| UPAY | Undue Payment | Payment is not justified. | Either the customer (Debtor) or a bank (Agent) in the payment flow experiences an activity which causes a payment to be executed under unexpected circumstances. |

---

<!-- Page 812 -->

Use case should be considered as a principal example whereby use case may be cross referenced

**Payment Cancellation Request**

Use Case c.56.1.1 – High Level Payment Cancellation Request (camt.056) of a completed Customer Credit Transfer (pacs.008)

Use Case c.56.1.1.a – High Level Payment Cancellation Request (camt.056) of a completed Customer Credit Transfer (pacs.008) using gpi Stop and Recall

Use Case c.56.1.2 – High Level Payment Cancellation Request (camt.056) of an incomplete Customer Credit Transfer (pacs.008)

Use Case c.56.1.2.a – High Level Payment Cancellation Request (camt.056) of an incomplete Customer Credit Transfer (pacs.008) using gpi Stop and Recall

Use Case c.56.2.1 – High Level Payment Cancellation Request (camt.056) of a complete Customer Credit Transfers (pacs.008) settled using the cover method

Use Case c.56.2.2 – High Level Payment Cancellation Request (camt.056) of an incomplete Customer Credit Transfers (pacs.008) settled using the cover method

Use Case c.56.2.3 – High Level Payment Cancellation Request (camt.056) of a Customer Credit Transfers (pacs.008) where the cover is returned

Use Case c.56.3.1 – High Level Payment Cancellation Request (camt.056) of a Financial Institution Credit Transfer (pacs.009)

Use Case c.56.4.1 – High Level Payment Cancellation Request (camt.056) of a Financial Institution Credit Transfer advice (pacs.009 adv)

---

<!-- Page 813 -->

# Credit Transfer (pacs.008)

See use case p.8.1.1 for the original payment, c.29.1.1 for case resolution and p.4.1.3. for an example payment return

1. Debtor request their bank to recall a previous instructed payment, as the amount was incorrect.

2. Debtor Agent (A) assigns a Cancellation Request to Agent B (assignee) requesting the original pacs 008 is returned

3. Agent B creates an investigation case. Recognising the payment has already been onward processed. They update Agent A and assign a Cancellation Request directly to Agent C.

4. Agent C creates an investigation case. Recognising the payment has already been onward processed. They update Agent B and assign a Cancellation Request directly to Agent D.

5. Agent D creates an investigation case. Recognising the payment has already been credited to the creditor. They request debit authority, providing the reason specified for the return request and updates Agent C. Once the outcome to the debit authorisation is know a final resolution to the investigation can be relayed any necessary return payment is arrange.

---

<!-- Page 814 -->

# Credit Transfer (pacs.008) using gpi Stop and Recall

**Diagram Flow:**
*   **Top Path:** 2 $\rightarrow$ camt.056 $\rightarrow$ gpi $\rightarrow$ 3 $\rightarrow$ camt.056 $\rightarrow$ 4
*   **Return Path:** 4 $\rightarrow$ camt.029 $\rightarrow$ 3 $\rightarrow$ camt.029 $\rightarrow$ 2
*   **Main Path:** 1 $\rightarrow$ A $\rightarrow$ pacs.008 $\rightarrow$ B $\rightarrow$ pacs.008 $\rightarrow$ C $\rightarrow$ pacs.008 $\rightarrow$ D $\rightarrow$ User

**1**
Debtor request their bank to recall a previous instructed payment, as the amount was incorrect.

**2**
Debtor Agent (A) initiates a gpi Stop and Recall, requesting the original pacs.008 is returned, using reason code

**3**
gpi Tracker identifies the payment is complete and forwards a camt.056 to Agent D.

**4**
Agent D creates an investigation case. Recognising the payment has already been credited to the creditor. They request debit authority, providing the reason specified for the return request and updates the gpi Tracker.
Once the outcome to the debit authorisation is know a final resolution to the investigation can be provided and any necessary return payment is arrange.

> See use case p.8.1.1 for the original payment, c.29.1.1 for case resolution and p.4.1.3. for an example payment return

---

<!-- Page 815 -->

# Credit Transfer (pacs.008)

> See use case p.8.1.1 for the original payment, c.29.1.2 for case resolution and p.4.1.3. for an example payment return

**Diagram Flow Labels:**
*   pacs.008
*   camt.056
*   camt.029
*   pacs.008
*   camt.056
*   pacs.008
*   camt.029

**1**
Debtor request their bank to recall a previous instructed payment, as the amount was incorrect.

**2**
Debtor Agent (A) assigns a Cancellation Request to Agent B (assignee) requesting the original pacs.008 is returned

**3**
Agent B creates an investigation case. Recognising the payment has already been onward processed. They update Agent A and assign a Cancellation Request directly to Agent C.

**4**
Agent C creates an investigation case. Recognising the payment has not been onward processed. They update Agent B that the Cancellation Request is accepted any necessary return payment is arrange.

---

<!-- Page 816 -->

# Credit Transfer (pacs.008) using gpi Stop and Recall

**2** $\xrightarrow{\text{camt.056}}$ **gpi** $\xrightarrow{\text{camt.056}}$ **3**
$\xleftarrow{\text{camt.029}}$ $\xleftarrow{\text{camt.029}}$ **4**

**1** $\rightarrow$ **A** $\xrightarrow{\text{pacs.008}}$ **B** $\xrightarrow{\text{pacs.008}}$ **C** $\rightarrow$ **D**

**1**
Debtor request their bank to recall a previous instructed payment, as the amount was incorrect.

**2**
Debtor Agent (A) initiates a gpi Stop and Recall, requesting the original pacs.008 is returned, using reason code

**3**
gpi Tracker identifies the payment is incomplete and forwards a camt.056 to Agent C.

**4**
Agent C creates an investigation case. Recognising the payment has not been onward processed. They updates the gpi Tracker any necessary return payment is arrange.

---

<!-- Page 817 -->

# Transfer (pacs.008) settled using a cover method.

**Message flows (diagram):**

| From | To | Message |
|------|----|---------|
| Debtor | Agent A | (step 1) |
| Agent A | Agent D | pacs.008 |
| Agent D | Agent A | camt.056 |
| Agent D | Agent A | camt.029 |
| Agent A | Agent B | pacs.009 cov |
| Agent B | Agent A | pacs.002 |
| Agent B | Cover | pacs.009 cov |
| Cover | Agent C | pacs.009 cov |
| Agent C | Agent D | camt.053 |
| Agent C | Agent D | camt.054 |
| Agent D | Creditor | (step 3) |

**Settlement Complete**

> See use case p.8.2.1 for the original payment, c.29.2.1 for case resolution and p.4.3.2 for an example payment return

**1**
Debtor request their bank to recall a previous instructed payment, as the amount was incorrect.

**2**
Debtor Agent (A) assigns a Cancellation Request to Agent D (assignee) requesting the original pacs.008 is returned, using reason code AM09.

**3**
Agent D creates an investigation case. Recognising the payment has already been credited to the creditor. They request debit authority, proving the reason specified for the return request and update Agent A.
Once the outcome to the debit authorisation is know a final resolution to the investigation can be relayed and any necessary

---

<!-- Page 818 -->

# Credit Transfer (pacs.008) settled using a cover method.

**Diagram flow:**

- Person → **A** (bank) → **D** (bank) → Person
- A → B (bank) → (bank) → C (bank) → D
- Messages: `pacs.008`, `camt.056`, `camt.029`, `pacs.009 cov`, `pacs.002`, `camt.053`, `camt.054`
- **Settlement Complete**

> See use case p.8.2.1 for the original payment, c.29.2.1 for case resolution and p.4.3.2 for an example payment return

**1**
Debtor request their bank to recall a previous instructed payment, as the amount was incorrect.

**2**
Debtor Agent (A) assigns a Cancellation Request to Agent D (assignee) requesting the original pacs.008 is returned, using reason code AM09.

**3**
Agent D creates an investigation case. Recognising the payment has not been credited to the creditor. They update Agent A that the Cancellation Request is accepted and arrange the necessary return payment once the pacs.009 cov settlement is confirmed by Agent C

---

<!-- Page 819 -->

# Transfers (pacs.008) where the cover is returned

**Flow elements:**

- Node **A** (Debtor Agent) → Node **D** (Creditor Agent): `pacs.008`
- Node **D** → Node **A**: `camt.056`
- Node **A** → Node **B**: `pacs.009_cov`
- Node **B** → Node **A**: `pacs.004`
- Node **B** → Node **C**: `pacs.009_cov`
- Node **C** → Node **B**: `pacs.002`
- Node **D** → Node **A**: `camt.029`

**Annotations:**

- `+ Return Reason`
- `+ Reject Reason`

**Note:** See use case p.8.2.1 for the cover payment sample c.29.2.2 for case resolution and p.4.3.3 for payment return

---

**1** Agent C receives the payment and recognises the payment can not be completed as requested e.g. the Agent D does not maintain an account with them.

**1** Debtor Agent (A) assigns a Cancellation Request to Agent D (assignee) requesting the original pacs.008 is considered null and void, using reason code COVR.

**2** Agent D creates an investigation case. Recognising the cover payment will not be received to settle the pacs.008. As the creditor has not been credited in advance of cover settlement, a final resolution to the investigation can be provided. A payment return is not necessary.

---

<!-- Page 820 -->

# Institution Credit Transfer (pacs.009)

**Diagram Flow Labels:**
*   Node A to Node B: pacs.009, pacs.002, camt.056, camt.029
*   Node B to Node C: pacs.009, pacs.002, camt.056, camt.029
*   Node C to Node D: pacs.009, camt.053, camt.054

**Note:**
See use case p.9.1.1 for the cover payment sample c.29.3.1 for case resolution and p.4.2.3 for payment return

**1**
Debtor request their bank to recall a previous instructed payment, as the amount was incorrect.

**2**
Debtor Agent (A) assigns a Cancellation Request to Agent C (assignee) requesting the original pacs.009 is returned, using reason code AM09.

**3**
Agent C creates an investigation case. Recognising the payment has already been credited to the creditor. They request debit authority, proving the reason specified for the return request and update Agent C. Once the outcome to the debit authorisation is know a final resolution to the investigation can be relayed and any necessary return payment can be initiated.

---

<!-- Page 821 -->

# Credit Transfer advice (pacs.009 adv)

**Diagram flow (sequence):**

- **A** (1) → **B** (2) → **E** (3) → **F**
  - A → B: `pacs.009 (ADV)`
  - B → E: `camt.056`
  - E → B: `camt.029`
  - E → F: `camt.054`
- **B** (2) ↔ **C**
  - B → C: `pacs.009`
  - C → B: `pacs.002`
- **C** ↔ **D**
  - C → D: `pacs.009`
  - D → C: `pacs.002`
- **D** ↔ **E** (3)
  - D → E: `camt.053`
  - E → D: `camt.054`

> See use case p.9.1.2 for the cover payment sample c.29.4.1 for case resolution and p.4.2.3 for payment return

**1** Debtor request their bank to recall a previous instructed payment, as the amount was incorrect.

**2** Debtor Agent (A) assigns a Cancellation Request to Agent E (assignee) requesting the original pacs.008 is returned, using reason code AM09.

**3** Agent E creates an investigation case. Recognising the payment has already been credited to the creditor. They request debit authority, proving the reason specified for the return request and update Agent B. Once the outcome to the debit authorisation is know a final resolution to the investigation can be relayed and any necessary

---

<!-- Page 822 -->

camt.107 – Cheque Presentation Notification
camt.108 - Cheque Cancellation or Stop Request
camt.109 – Cheque Cancellation or Stop Report

---

<!-- Page 823 -->

# Cheque Presentation Notification

---

<!-- Page 824 -->

# camt.107

- Group Header
- Cheque

The ChequePresentationNotification message is sent by a drawer bank, or a bank acting on behalf of the drawer bank to the bank on which a cheque has been drawn (the drawee bank).

It is used to advise the drawee bank, or confirm to an enquiring bank, the details concerning the cheque referred to in the message.

The Cheque Presentation Notification is restricted to a single cheque per InterAct message.

---

<!-- Page 825 -->

Drawer Agent

Drawee Agent

camt.107

The Agent A (drawer agent) sends a ChequePresentmentNotification message to Agent B (the drawee agent).
The ChequePresentmentNotification message informs the drawee agent about the cheque submission.
The notification message facilitates the drawee agent to follow up the cheque submission and relevant business process.

---

<!-- Page 826 -->

# Group Header

---

<!-- Page 827 -->

Each ISO 20022 cash management message has a *Message Identification* element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message.

For Cash Management (camt) messages the *Message Identification* has no exact equivalent in the legacy MT Advice of Cheque message. However, the Sender's Reference (Field 20) could be considered a similar comparison.

Group Header > Message Identification

---

<!-- Page 828 -->

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+-hh:mm
> For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

Group Header Creation Date Time

---

<!-- Page 829 -->

The number of Cheques in CBPR+ cheque payment usage guidelines is fixed to 1.

Group Header > Number Of Cheques

---

<!-- Page 830 -->

Cheque

---

<!-- Page 831 -->

Min 1 – Max 1
The Cheque Presentation Notification *Cheque* nested element specifies the details of the Cheque.

12.200
Strg
This Cheque element has been restricted to one cheque occurrence.

Cheque

---

<!-- Page 832 -->

Min 1 - Max 1

The Cheque Presentation Notification ***Instruction Identification*** provides an optional element to identify unambiguously the instruction

Point to point reference that can be used between the Agent instructing the Cheque Presentation Notification and the Drawee Agent (Agent receiving this message) to refer to the individual instruction.

Cheque > *Instruction Identification*

---

<!-- Page 833 -->

Min 1 – Max 1

The Cheque Number Notification *Cheque Number* provides a mandatory element to identify unambiguously the Cheque.

1. **Unique and unambiguous number** for a cheque as assigned by the Drawee Agent. This cheque number is often found as part of the Magnetic Ink Character Recognition (MICR) encoding at the bottom of a cheque

Cheque > Cheque Number

---

<!-- Page 834 -->

The Cheque Presentation Notification has several element to capture a Date related to the cheque.

**Min 1 – Max 1**
The **Issue Date** is a mandatory element, and represents the date when the cheque was issued by the payer, or on behalf of the payer

**Min 0 – Max 1**
The **Stale Date** is an optional element and represents the date after which a cheque is no longer valid. The validity period of a cheque is calculated from the issue date on the face of the cheque. The period may be indicated on the face of the cheque itself such as "Valid for 90 days" or may be determined in accordance with domestic banking practice. Not all countries will have a validity period.

Cheque

---

<!-- Page 835 -->

Min 1 – Max 1
A mandated currency **Amount** of the cheque to be paid to the payee.

Min 0 – Max 1
The **Value Date** is an optional element, it is used to capture the **Date**, where different to the **Issue Date**, i.e., represents a date on the cheque in the future. The cheque Value Date describes the date in which the cheque amount becomes available to be deposited on the payee account.

The Value Date captured in the camt.107 is referred to as Effective Date in the camt.108

Cheque >
Amount >

---

<!-- Page 836 -->

Min 1 – Max 1

The Cheque Presentation Notification **Payer** captures the party that instructs the Drawee Agent to issues a cheque to pay a specific amount, upon presentation, to the payee. The Payer sub-element describe the Payer in greater detail.

Nested element capturing either structured or unstructured *Payer* address details

Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc.

Optional element to capture the Payee's ISO country code of residence

Mandatory *Name*

*Name*

*Postal Address*

*Payer*

*Identification*

*Country of Residence*

- Department
  - Sub Department
  - Street Name
  - Building Number
  - Building Name
  - Floor
  - Post Box
  - Room
  - Post Code
  - Town Name
  - Town Location Name
  - District Name
  - Country Sub Division

Postal Address

---

<!-- Page 837 -->

The Cheque Presentation Notification `Min 0 – Max 1` **Payer Account** is used to capture the account of the party that instructs the Drawee Agent to issues a cheque to pay a specific amount, upon presentation, to the payee.

The **Payer Account** uses a variety of nested elements to capture information related to the account.

`Min 0 – Max 1` **Identification** identifies the account maintained at the Drawer Agent (Account Servicing Institution)

`Min 0 – Max 1` **Type** uses the external Cash Account Type code list to identify the type of account

`Min 0 – Max 1` **Currency** identifies the currency of the account

`Min 0 – Max 1` **Name** identifies the name of the account as assigned by the Drawer Agent (Account Servicing Institution)

`Min 0 – Max 1` **Proxy** captures an alternative identification of the account number such as an email address. This element has further nested **Type** which is a choice of external code list or proprietary code and **Identification** which are both mandatory where the Proxy element is used.

---

<!-- Page 838 -->

The Cheque Presentment Notification <span style="background-color: #99ccff;">Min 0 – Max 1</span> **<span style="color: #006666;">Drawer Agent</span>** optionally captures the Agent who the cheque has been drawn on. This Agent is typically also the Agent from who the Cheque Presentment Notification is sent to the *Drawee Agent*.

<span style="background-color: #99ccff;">Min 0 – Max 1</span>
The **<span style="color: #006666;">Drawer Agent Account</span>** optionally captures the Drawer Agent's Account with the *Drawee Agent* and who would receive an order the pay the cheque upon presentation.

![Cheque image](cheque_image.png)

The Drawer Bank is typically identified on the cheque together with their Postal Address. The Drawer Agent's Account with the Drawee Agent is also often also identified on the cheque.

Cheque >
Drawer Agent

---

<!-- Page 839 -->

Min 1 – Max 1

The Cheque Presentation Notification *Payee* captures the party that should receive an amount of money as specified in the cheque. The Payee sub-element describe the Payee in greater detail.

Mandatory *Name*

**Name**

**Postal Address**

- Department
- Sub Department
- Street Name
- Building Number
- Building Name
- Floor
- Post Box
- Room
- Post Code
- Town Name
- Town Location Name
- District Name
- Country Sub Division
- Country — Code

Nested element capturing either structured or unstructured *Payee* address details

**Payee**

Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc.

*Identification*

Optional element to capture the Payee's ISO country code of residence

*Country of Residence*

---

<!-- Page 840 -->

> Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases.

**Serial Financial Institution to Financial Institution to Customer Credit Transfer**
Use Case c.107.1 – High Level Drawer Agent Cheque issuance to Payee, on their account with the Drawer Agent
Use Case c.107.2 - High Level Drawer Agent Cheque issuance to Payee, on their head office's account with the Drawer Agent

---

<!-- Page 841 -->

# Drawee Agent

**Diagram flow**

`Payer` →(1)→ `Drawer (A)` →(2a)→ `[Cheque 12,000]` →(4)→ `Payee`

`Drawer (A)` ⇄(2b: `cant 102` / `cant 023`)⇄ `Drawee (B)`

`Payee` →(4)→ `Agent (C)` →(5)→ `[Network]` →(6)→ `Drawee (B)`

**Step descriptions**

| Step | Description |
|------|-------------|
| 1 | Payer instructs the Drawer Agent to issue a cheque to the Payee |
| 2a | Drawer Agent (A) issues a cheque to the Payee drawn of their account at the Drawee Agent (B) |
| 2b | In parallel the Drawer Agent (A) initiates a Cheque Presentation Notification to the Drawee Agent (B) |
| 3 | The Drawee Agent (B) receives the Cheque Presentation Notification and store the information in anticipation for the cheque to be presented |
| 4 | Payee received the cheque and present it to their bank (Agent C) |
| 5 | Agent C receives the cheque deposit and present it into the domestic cheque clearing |
| 6 | Drawee Agent (B) receives the cheque presentation via the cheque clearing. They validate the presented cheque details again the information received on the Cheque Presentation Notification to conclude whether the cheque can be settled. |

---

<!-- Page 842 -->

# account with the Drawee Agent

**Entities:** Payer · Drawer · Payee · Drawee (Bank Agents: A, HO, B, C)

**Message labels on arrows:** `camt.107` (A → B) · `camt.053` (B → HO/Drawer)

---

**1**
Payer instructs their Bank (Agent A) to issue a cheque to the Payer

**2a**
Agent (A) issues a cheque to the Payee drawn of their head office's (HO) account at the Drawer Agent (B)

**2b**
In parallel the Agent (A) initiates a Cheque Presentation Notification to the Drawee Agent (B)

**3**
The Drawee Agent (B) receives the Cheque Presentation Notification and store the information in anticipation for the cheque to be presented

**4**
Payee received the cheque and present it to their bank (Agent C)

**5**
Agent C receives the cheque deposit and present it into the domestic cheque clearing

**6**
Drawee Agent (B) receives the cheque presentation via the cheque clearing. They validate the presented cheque details again the information received on the Cheque Presentation Notification to conclude whether the cheque can be settled.

---

<!-- Page 843 -->

# Cheque Cancellation or Stop Request

---

<!-- Page 844 -->

# camt.108

- Group Header
- Cheque

The Cheque Cancellation Or Stop Request message is sent by a drawer bank, or a bank acting on behalf of the drawer bank, to the agent on which a cheque has been drawn (the drawee bank) to request for the cancellation of the presentment and/or stop the payment of the cheque referred to in the message.

The Cheque Cancellation or Stop Report is restricted to a single cheque per InterAct message.

---

<!-- Page 845 -->

Drawer Agent

Drawee Agent

camt.107

camt.108

camt.109

The Agent A (Drawer Agent) sends a ChequeCancellationOrStopRequest message to Agent B (the Drawee Agent). The ChequeCancellationOrStopReques message requests the drawee agent to place a stop (refusal to settle) upon presentation of the cheque, effectively canceling the issued cheque.

---

<!-- Page 846 -->

# Group Header

---

<!-- Page 847 -->

Each ISO 20022 cash management message has a *Message Identification* element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message.

For Cash Management (camt) messages the *Message Identification* has no exact equivalent in the legacy MT Advice of Cheque message. However, the Sender's Reference (Field 20) could be considered a similar comparison.

Group Header > Message Identification

---

<!-- Page 848 -->

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+-hh:mm
> For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

Group Header Creation Date Time

---

<!-- Page 849 -->

The number of Cheques in CBPR+ cheque payment usage guidelines is fixed to 1.

Group Header > Number Of Cheques

---

<!-- Page 850 -->

Cheque

---

<!-- Page 851 -->

Min 1 – Max 1

The Cheque Cancellation or Stop Request **Cheque** nested element specifies the details of the Cheque.

12.200
Stop

This Cheque element has been restricted to one cheque occurrence.

Cheque

---

<!-- Page 852 -->

Min 0 – Max 1

The Cheque Cancellation or Stop Request *Instruction Identification* provides an optional element to identify unambiguously the instruction

**Point to point reference** that can be used between the Agent instructing the Cheque Cancellation or Stop Request and the Drawee Agent (Agent receiving this message) to refer to the individual instruction.

Cheque > Instruction Identification

---

<!-- Page 853 -->

Min 1 – Max 1

The Cheque Cancellation or Stop Request ***Original Instruction Identification*** provides an optional element to identify unambiguously the original instruction

**Point to point reference** that can be used to identify the original Cheque Presentment Notification between the Agent instructing the Cheque Presentment Notification and the Drawee Agent (Agent receiving this message) to refer to the individual instruction.

Cheque > *Original Instruction Identification*

---

<!-- Page 854 -->

Min 1 – Max 1

The Cheque Cancellation or Stop Request **_Cheque Number_** provides a mandatory element to identify unambiguously the Cheque.

1 3
4
2 5
**_Unique and unambiguous number_** for the cheque as assigned by the Drawee Agent. This cheque number is often found as part of the Magnetic Ink Character Recognition (MICR) encoding at the bottom of a cheque

Cheque > Cheque Number

---

<!-- Page 855 -->

The Cheque Cancellation or Stop Request has several element to capture a Date related to the cheque.

Min 1 – Max 1
The ***Issue Date*** is a mandatory element, and represents the date when the cheque was issued by the payer, or on behalf of the payer

Min 0 – Max 1
The ***Stale Date*** is an optional element and represents the date after which a cheque is no longer valid. The validity period of a cheque is calculated from the issue date on the face of the cheque. The period may be indicated on the face of the cheque itself such as "Valid for 90 days" or may be determined in accordance with domestic banking practice. Not all countries will have a validity period.

Cheque

---

<!-- Page 856 -->

A mandated currency <sup>Min 1 – Max 1</sup> **Amount** of the cheque to be paid to the payee.

The <sup>Min 0 – Max 1</sup> *Effective Date* is an optional element, it is used to capture the original **Value Date** (as provided in the camt.107), where different to the original **Issue Date**, i.e., represents a date on the cheque in the future. The cheque Value Date describes the date in which the cheque amount becomes available to be deposited on the payee account.

Cheque &gt;
Amount &gt;

---

<!-- Page 857 -->

Min 0 – Max 1

The Cheque Cancellation or Stop Request **_Drawer Agent_** optionally captures the Agent who the cheque has been drawn on. This Agent is typically also the Agent from who the Cheque Presentation Notification is sent to the **_Drawee Agent_**.

The **_Drawer Agent Account_** optionally captures the Drawer Agent's Account with the **_Drawee Agent_** and who would receive an order the pay the cheque upon presentation.

![](https://i.imgur.com/placeholder.png)

The Drawer Agent and Drawer Account elements where present should match that of the original camt.107 Cheque Presentation Notification.

Cheque >
Drawer Agent

---

<!-- Page 858 -->

Min0 – Max1
The Cheque Cancellation or Stop Request **Payee** captures the party that should receive an amount of money as specified in the cheque.
The Payee sub-element describe the Payee in greater detail.

**Postal Address**
*   Department
*   Sub Department
*   Street Name
*   Building Number
*   Building Name
*   Floor
*   Post Box
*   Room
*   Post Code
*   Town Name
*   Town Location Name
*   District Name
*   Country Sub Division
*   Country
    *   Code

Nested element capturing either structured or unstructured *Payee* address details

Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc.

Optional element to capture the Payee's ISO country code of residence

Mandatory *Name*
**Name**

**Postal Address**

**Payee**

*Identification*

*Country of Residence*

---

<!-- Page 859 -->

The Cheque Cancellation or Stop Request **Min 1 – Max 1** *Cheque Cancellation or Stop Reason* nested element captures information associated with the reason for the Cheque Cancellation or Stop request.

**Min 0 – Max 1**
the **Originator** element is a embedded code choice that helps identify the party who request the cheque cancellation or stop request. Where used this party would typically be the Payer (code **PAYR**) of the cheque.

**Min 1 – Max 1**
the **Reason** is mandatory and represented by an embedded CBPR+ Cancellation **Code** choice (—)

**Min 0 – Max 2**
the **Additional Information** element may also be included to provide **further** details on the cancellation or stop reason.

Note where Reason code **NARR** is used additional information must be provided to describe the reason for the Cheque Cancellation or Stop request.

Cheque > Cheque Cancellation or Stop Reason
> Originator
> Reason

---

<!-- Page 860 -->

> Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases.

**Serial Financial Institution to Financial Institution to Customer Credit Transfer**
Use Case c.108.1 – High Level Drawer Agent Cheque Cancellation or Stop request as a result of a lost cheque
Use Case c.108.2 – High Level Drawer Agent Cheque Cancellation or Stop request upon request of the Payer customer.

---

<!-- Page 861 -->

# lost cheque.

**Payer** → **Drawer (A)** → **Payee**

- Arrow 1: Payer to Drawer
- Arrow 2 (cant.108): Drawer to Drawee (B)
- Arrow (cant.107): Drawer to Drawee (B)
- Arrow (cant.107): Drawee (B) to Drawer
- Drawer (A) → [cheque 12.000] → [!]
- **Drawee (B)**
- **C**

> **Note:** See use case c.109.1.1 for an example the Cheque Cancellation or Stop Report

| 1 | 2 | 3 |
|---|---|---|
| Payer instructs the Drawer Agent they wish to cancel or stop a previously issued cheque, as the Payee informs them the cheque has been lost. | Drawer Agent (A) issues a cheque cancellation or stop request to the Drawee Agent (B) with reason code LOST | Drawee Agent (B) match the request to the previous Cheque Presentation Notification (cant.107). As the cheque has not been presented the status record is identified as not to be paid if presented, as a result of a cancellation/stop request. This is reported back to the Drawer Agent |

---

<!-- Page 862 -->

of the Payer customer.

Payer

Drawer

A

Payee

cant. 107

cant. 103

cant. 108

Drawee

B

C

See use case c.109.1.2 for an example the Cheque Cancellation or Stop Report

## 1

Payer instructs the Drawer Agent they wish to cancel or stop a previously issued cheque, as the Payer informs them they no longer wish to honour the cheque.

## 2

Drawer Agent (A) issues a cheque cancellation or stop request to the Drawee Agent (B) with reason code CUST

## 3

Drawee Agent (B) match the request to the previous Cheque Presentment Notification (cant. 107). As the cheque has already been presented and paid the cancellation/stop request can not be executed. This is reported back to the Drawer Agent (A) as rejected with additional information to explain the cheque has

---

<!-- Page 863 -->

# Cheque Cancellation or Stop Report

---

<!-- Page 864 -->

# camt.109

- Group Header
- Cheque

The Cheque Cancellation or Stop Report message is sent by the drawee agent (on which a cheque is drawn) to the drawer agent, or the agent acting on behalf of the drawer agent, to indicate what actions have been taken in attempting to cancel the presentment and/or stop the payment of the cheque referred to in the message.

The Cheque Cancellation or Stop Request is restricted to a single cheque per InterAct message.

---

<!-- Page 865 -->

Drawer Agent

Drawee Agent

| camt.107 |
| :--- |
| camt.108 |
| camt.109 |

The Agent B (Drawee Agent) sends a ChequeCancellationOrStopReport message to Agent A (the Drawer Agent). The ChequeCancellationOrStopReport message reports the outcome of a Cheque Cancellation or Stop Request.

---

<!-- Page 866 -->

# Group Header

---

<!-- Page 867 -->

Each ISO 20022 cash management message has a *Message Identification* element, located in the Group Header. This 35 character identifier is a point-to-point reference used to unambiguously identify the message.

For Cash Management (camt) messages the *Message Identification* has no exact equivalent in the legacy MT Advice of Cheque message. However, the Sender's Reference (Field 20) could be considered a similar comparison.

Group Header > Message Identification

---

<!-- Page 868 -->

CBPR+ usage guidelines mandate the time zone that the time represents as an offset against Universal Time Coordinated (UTC):

Local time with UTC offset YYYY-MM-DDThh:mm:ss.sss+-hh:mm
> For example: 2002-10-10T12:00:00-05:00 (noon/midday on 10 October 2002, Central Daylight Savings Time as well as Eastern Standard Time in the U.S.)

All CBPR+ time elements need offset against UTC. Milliseconds are optional.

Group Header Creation Date Time

---

<!-- Page 869 -->

The number of Cheques in CBPR+ cheque payment usage guidelines is fixed to 1.

Group Header > Number Of Cheques

---

<!-- Page 870 -->

Cheque

---

<!-- Page 871 -->

**Min 1 – Max 1**

The Cheque Cancellation or Stop Report ***Cheque*** nested element specifies the details of the Cheque.

12:00
Stop

This Cheque element has been restricted to one cheque occurrence.

Cheque ?

---

<!-- Page 872 -->

Min 0 – Max 1

The Cheque Cancellation or Stop Report ***Instruction Identification*** provides an optional element to identify unambiguously the instruction

**Point to point reference** that can be used between the Drawee Agent providing the Cheque Cancellation or Stop Report and the Drawee Agent (Agent receiving this message) to refer to the individual instruction.

Cheque > *Instruction Identification*

---

<!-- Page 873 -->

Min 1 - Max 1

The Cheque Cancellation or Stop Request **Original Instruction Identification** provides an optional element to identify unambiguously the original instruction

Point to point reference that can be used to identify the original Cheque Cancellation or Stop Request between the Agent instructing the Cheque Presentment Notification and the Drawee Agent (Agent receiving the request message) to refer to the individual request.

Cheque > Original Instruction Identification

---

<!-- Page 874 -->

Min 1 – Max 1

The Cheque Cancellation or Stop Request **Cheque Number** provides a mandatory element to identify unambiguously the Cheque.

4.2.5 **Unique and unambiguous number** for the cheque as assigned by the Drawee Agent. This cheque number is often found as part of the Magnetic Ink Character Recognition (MICR) encoding at the bottom of a cheque

Cheque > Cheque Number

---

<!-- Page 875 -->

The Cheque Cancellation or Stop Report has several element to capture a Date related to the cheque.

**Min 1 – Max 1**

The ***Issue Date*** is a mandatory element, and represents the date when the cheque was issued by the payer, or on behalf of the payer

**Min 0 – Max 1**

The ***Stale Date*** is an optional element and represents the date after which a cheque is no longer valid. The validity period of a cheque is calculated from the issue date on the face of the cheque. The period may be indicated on the face of the cheque itself such as "Valid for 90 days" or may be determined in accordance with domestic banking practice. Not all countries will have a validity period.

Cheque

---

<!-- Page 876 -->

A mandated currency <sup>Min 1 – Max 1</sup> **Amount** of the cheque to be paid to the payee.

The <sup>Min 0 – Max 1</sup> *Effective Date* is an optional element, it is used to capture the original **Value Date** (as provided in the camt.107), where different to the original **Issue Date**, i.e., represents a date on the cheque in the future. The cheque Value Date describes the date in which the cheque amount becomes available to be deposited on the payee account.

Cheque &gt;
Amount &gt;

---

<!-- Page 877 -->

Min 0 – Max 1

The Cheque Cancellation or Stop Request **_Drawer Agent_** optionally captures the Agent who the cheque has been drawn on. This Agent is typically also the Agent from who the Cheque Presentation Notification is sent to the **_Drawee Agent_**.

The **_Drawer Agent Account_** optionally captures the Drawer Agent's Account with the **_Drawee Agent_** and who would receive an order the pay the cheque upon presentation.

![](https://i.imgur.com/placeholder.png)

The Drawer Agent and Drawer Account elements where present should match that of the original camt.107 Cheque Presentation Notification.

Cheque >
Drawer Agent

---

<!-- Page 878 -->

Min0 – Max1
The Cheque Cancellation or Stop Request **Payee** captures the party that should receive an amount of money as specified in the cheque.
The Payee sub-element describe the Payee in greater detail.

**Postal Address**
*   Department
*   Sub Department
*   Street Name
*   Building Number
*   Building Name
*   Floor
*   Post Box
*   Room
*   Post Code
*   Town Name
*   Town Location Name
*   District Name
*   Country Sub Division
*   Country
    *   Code

Nested element capturing either structured or unstructured *Payee* address details

Nested element capturing the various types of identifiers for the party e.g. BIC, LEI etc.

Optional element to capture the Payee's ISO country code of residence

Mandatory *Name*
**Name**

**Postal Address**

**Payee**

*Identification*

*Country of Residence*

---

<!-- Page 879 -->

The Cheque Cancellation or Stop Request **Min 1 – Max 1** *Cheque Cancellation or Stop Reason* nested element captures information associated with the reason for the Cheque Cancellation or Stop request.

**Min 0 – Max 1**
the *Originator* element helps identify the party who request the cheque cancellation or stop request. Where used this party would typically be the Payer of the cheque.

**Min 1 – Max 1**
the *Status* is mandatory and represented by an embedded status *Code* choice
REJT (Rejected) or ACCP (Accepted)

**Min 0 – Max 2**
the *Additional Information* element may also be included to provide further details on the cancellation or stop reason.

Note where Status code REJT is used additional information must be provided to describe the reason for the rejection.

Cheque > Cheque Cancellation or Stop Reason
> Originator
> Reason

---

<!-- Page 880 -->

> Use case should be considered as a principal example whereby use case may be cross referenced e.g. a use case involving a Market Infrastructure can apply the Market Infrastructure legs to other use cases.

**Serial Financial Institution to Financial Institution to Customer Credit Transfer**
Use Case c.109.1 – High Level Drawer Agent Cheque Cancellation or Stop request as a result of a lost cheque
Use Case c.109.2 – High Level Drawer Agent Cheque Cancellation or Stop request upon request of the Payer customer.

---

<!-- Page 881 -->

# lost cheque.

Payer → Drawer → [Cheque 12.000] → !

Drawer ↔ Drawee
- c.108.1.107
- c.108.1.108
- c.108.1.109

Payee

**1** Drawee Agent (B) reports to the Drawer Agent (A) that the Cheque Cancellation or Stop request has been accepted.

See use case c.108.1.1 for an example the Cheque Cancellation or Stop Request

---

<!-- Page 882 -->

the Payer customer.

Payer → Drawer (A) → [12.000] → Payee

Drawer (A) ↔ Drawee (B)
- c.108.1.02
- c.108.1.03
- c.108.1.00 (1)

Payee → [12.000] → (C) → [network node] → Drawee (B)

**1** Drawee Agent (B) reports to the Drawer Agent (A) that the Cheque Cancellation or Stop request has been rejected. Additional Information is provided to explain that the cheque has already been presented and paid.

See use case c.108.1.2 for an example the Cheque Cancellation or Stop Request

---

<!-- Page 883 -->

SWIFT

www.swift.com