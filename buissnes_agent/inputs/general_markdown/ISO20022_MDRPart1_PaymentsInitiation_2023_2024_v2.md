<!-- Page 1 -->

ISO 2022

## Payments Initiation - Maintenance 2023 - 2024

# Message Definition Report - Part 1

## Approved by the Payments SEG on 8th January 2024

This document provides information about the use of the messages for Payments Initiation and includes, for example, business scenarios and messages flows.

March 2024

---

<!-- Page 2 -->

Message Definition Report - Part 1                                                                                          Table of Contents

# Table of Contents

Table of Contents..................................................................................................................2

**1    Introduction**..................................................................................................................5
1.1    Terms and Definitions..................................................................................................5
1.2    Abbreviations and Acronyms.......................................................................................5
1.3    Document Scope and Objectives..................................................................................6
1.4    References..................................................................................................................6

**2    Scope and Functionality**................................................................................................7
2.1    Background..................................................................................................................7
2.2    Scope..........................................................................................................................7
2.3    Groups of MessageDefinitions and Functionality....................................................7

**3    BusinessRoles and Participants**....................................................................................8
3.1    Participants and BusinessRoles Definitions..............................................................8
3.2    BusinessRoles / Participants Table..............................................................................9

**4    BusinessProcess Description**......................................................................................10
4.1    Customer-to-Bank Payment Order..............................................................................10
4.2    Customer-to-Bank Direct Debit..................................................................................14

**5    Description of BusinessActivities**..............................................................................16
5.1    Customer to Bank Payment Order..............................................................................16
5.2    Customer-to-bank Direct Debit..................................................................................21

**6    BusinessTransactions**................................................................................................23
6.1    CustomerCreditTransferInitiation..............................................................................23
6.2    CustomerCreditTransferInitiation - Relay...................................................................26
6.3    CustomerDirectDebitInitiation and FIToFICustomerDirectDebit..............................29
6.4    Negative Customer and FIToFIPaymentStatusReport with Direct Debit...................31
6.5    Positive Customer and FIToFIPaymentStatusReport with Direct Debit...................34
6.6    PaymentReturn with Direct Debit..............................................................................35
6.7    Customer Payment Reversal with Direct Debit........................................................37

**7    Business Examples**...................................................................................................40
7.1    CustomerCreditTransferInitiation pain.001.001.12..................................................40
7.2    CustomerPaymentStatusReport pain.002.001.14 - 1................................................49
7.3    CustomerPaymentStatusReport pain.002.001.14 - 2................................................51
7.4    CustomerPaymentReversal pain.007.001.12...........................................................55
7.5    CustomerDirectDebitInitiation pain.008.001.11....................................................59

**8    Revision Record**.......................................................................................................67

---

<!-- Page 3 -->

Message Definition Report - Part 1                                                                                          Table of Contents

## Preliminary Note

The Message Definition Report (MDR) is made of three parts:

**MDR Part 1**

This describes the contextual background required to understand the functionality of the proposed message set. Part 1 is produced by the submitting organisation that developed or maintained the message set in line with an MDR Part 1 template provided by the ISO 20022 Registration Authority (RA) on [www.iso20022.org](http://www.iso20022.org).

**MDR Part 2**

This is the detailed description of each message definition of the message set. Part 2 is produced by the RA using the model developed by the submitting organisation.

**MDR Part 3**

This is an extract if the ISO 20022 Business Model describing the business concepts used in the message set. Part 3 is an Excel document produced by the RA.

---

<!-- Page 4 -->

# 1 Introduction

## 1.1 Terms and Definitions

The following terms are reserved words defined in ISO 20022 Edition 2013 – Part1. When used in this document, the UpperCamelCase notation is followed.

| Term | Definition |
|---|---|
| **BusinessRole** | Functional role played by a business actor in a particular BusinessProcess or BusinessTransaction. |
| **Participant** | Involvement of a BusinessRole in a BusinessTransaction. |
| **BusinessProcess** | Definition of the business activities undertaken by BusinessRoles within a BusinessArea whereby each BusinessProcess fulfils one type of business activity and whereby a BusinessProcess may include and extend other BusinessProcesses. |
| **BusinessTransaction** | Particular solution that meets the communication requirements and the interaction requirements of a particular BusinessProcess and BusinessArea. |
| **MessageDefinition** | Formal description of the structure of a message instance. |

**Note** When a MessageDefinition or message identifier is specified, it should include the variant and version number. However, in this document (except in the business examples section, if present), variant and version numbers are not included. In order to know the correct variant and version number for a MessageDefinition, the related Message Definition Report Part 2 document should be consulted.

## 1.2 Abbreviations and Acronyms

The following is a list of abbreviations and acronyms used in the document.

| Abbreviation/Acronyms | Definition |
|---|---|
| **ISTH** | International Standards Team Harmonisation |
| **CSTP** | Corporate Straight Through Processing Bank Group |
| **CAG** | Corporate Advisory Group |
| **ISITC** | International Securities Association for Institutional Trade Communication |
| **IFX** | Interactive Financial Exchange Forum |
| **TWIST** | Transaction Workflow Innovation Standards Team |
| **CBI** | Corporate Banking Interbancario |
| **OAGi** | Open Application Group |
| **MDR** | Message Definition Report |
| **MCR** | Maintenance Change Request |
| **SEG** | Standards Evaluation Group |
| **FI** | Financial Institution |
| **XML** | eXtensible Mark-up Language |

---

<!-- Page 5 -->

| Abbreviation/Acronyms | Definition |
|---|---|
| IBAN | International Bank Account Number |
| BIC | Business Identifier Code |
| ACH | Automated Clearing House |
| DD | Direct Debit |
| MRI | Mandate Related Information |
| etc. | Etcetera |

## 1.3 Document Scope and Objectives

This document is the first part of the Payments Initiation Message Definition Report (MDR) that describes the BusinessTransactions and underlying message set. For the sake of completeness, the document may also describe BusinessActivities that are not in the scope of the business processes covered in this document.

This document describes the following:

- the BusinessProcess scope
- the BusinessRoles involved in these BusinessProcesses

The main objectives of this document are as follows:

- to provide information about the messages that support the BusinessProcesses
- to explain the BusinessProcesses and BusinessActivities these messages have addressed
- to give a high level description of BusinessProcesses and the associated BusinessRoles
- to document the BusinessTransactions
- to provide business examples

The MessageDefinitions are specified in Message Definition Report Part 2.

## 1.4 References

| Document | Version | Date | Author |
|---|---|---|---|
| Customer to Bank Payment Initiation Business Justification | 2005 | 2005-09-23 | SWIFT, IFX, OAGI & TWIST as part of the IST Harmonization Team (ISTH) |
| ISO 20022 Maintenance Change Request (MCR #170) document (Payments Maintenance 2020/2021) | 2020 | 2020-08-31 | SWIFT |
| ISO 20022 Maintenance Change Request (MCR #208) document (Payments Maintenance 2022/2023) | 2022 | 2022-08-31 | SWIFT |
| ISO 20022 Maintenance Change Request (MCR #234) document (Payments Maintenance 2023/2024) | 2023 | 2023-08-31 | SWIFT |

---

<!-- Page 6 -->

# 2 Scope and Functionality

## 2.1 Background

This Message Definition Report covers a set of four MessageDefinitions developed by SWIFT in close collaboration with IFX, TWIST, OAGi and approved by the Payments Standards Evaluation Group (SEG).

These messages are specifically designed to support the customer-to-bank information flow.

## 2.2 Scope

The scope covers a set of messages, exchanged between a debtor and its bank or between a creditor and its bank, to initiate, collect, manage and monitor payments.

The CustomerCreditTransferInitiation and CustomerDirectDebitInitiation messages described in this document can be used for initiating either multiple payment orders or single transfers.

## 2.3 Groups of MessageDefinitions and Functionality

### 2.3.1 Groups

#### 2.3.1.1 Instruction Messages

**CustomerCreditTransferInitiation**

This message is used to request movement of funds from the debtor account to a creditor;

**CustomerDirectDebitInitiation**

This message is used to request the collection(s) of funds from one or more debtor's accounts for a creditor.

| MessageDefinition | Message Identifier |
|---|---|
| CustomerCreditTransferInitiation | pain.001 |
| CustomerDirectDebitInitiation | pain.008 |

#### 2.3.1.2 Related Messages

**CustomerPaymentReversal**

The message is used to reverse a payment previously executed

**CustomerPaymentStatusReport**

This message is used to inform on the positive or negative status of an instruction (either single or file) and to report on a pending instruction.

| MessageDefinition | Message Identifier |
|---|---|
| CustomerPaymentReversal | pain.007 |
| CustomerPaymentStatusReport | pain.002 |

### 2.3.2 Functionality Groups

See Message Definition Report Part 2 for the message scopes and formats.

---

<!-- Page 7 -->

# 3 BusinessRoles and Participants

A BusinessRole represents an entity (or a class of entities) of the real world, physical or legal, a person, a group of persons, a corporation. Examples of BusinessRoles: "Financial Institution", "Automated Clearing House", "Central Securities Depository".

A Participant is a functional role performed by a BusinessRole in a particular BusinessProcess or BusinessTransaction. Examples of Participants: the "user" of a system, "debtor", "creditor", "investor".

The relationship between BusinessRoles and Participants is many-to-many. One BusinessRole can be involved as different Participants at different moments in time or at the same time. Examples of BusinessRoles: "user", "debtor", "creditor", "investor". Different BusinessRoles can be involved as the same Participant.

In the context of Payments Initiation the high-level BusinessRoles and typical Participants can be represented as follows:

## 3.1 Participants and BusinessRoles Definitions

Participants

| Description | Definition |
|---|---|
| Debtor | Party that owes an amount of money to the (ultimate) creditor. In the context of the payment model, the debtor is also the debit account owner. |
| Creditor | Party to which an amount of money is due. In the context of the payment model, the creditor is also the credit account owner. |
| Ultimate Debtor | Ultimate party that owes an amount of money to the (ultimate) creditor. |
| Ultimate Creditor | Ultimate party to which an amount of money is due. |
| Debtor Agent | Financial institution servicing an account for the debtor. |
| Creditor Agent | Financial institution servicing an account for the creditor. |
| Forwarding Agent | Financial institution that receives the instruction from the initiating party and forwards it to the next agent in the payment chain for execution. |
| Initiating Party | Party initiating the payment to an agent. In the payment context, this can either be the debtor (in a credit transfer), the creditor (in a direct debit), or a party that initiates the payment on behalf of the debtor or creditor. |
| Account Owner | Party that legally owns the account. |
| Account Servicer | Party that manages the account on behalf of the account owner, that is manages the registration and booking of entries on the account, calculates balances on the account and provides information about the account. |
| Payment Clearing Agent (Instructing Agent) | Agent that instructs the next party in the payment chain to carry out the payment/instruction. |
| Payment Settlement Agent Instructed Agent) | Agent that executes the instruction upon the request of the previous party in the chain (either an agreement party, or a clearing agent). |
| Intermediary Agent | Agent between the debtor's agent and the creditor's agent. There can be several intermediary agents specified for the execution of a payment. |

---

<!-- Page 8 -->

**BusinessRoles**

| Description | Definition |
| :--- | :--- |
| Financial Institution | Organisation established primarily to provide financial services. |
| Clearing System | Specifies the system which plays a role in the clearing process. |
| Party | Entity involved in a payment. |

## 3.2 BusinessRoles / Participants Table

| Participants | BusinessRole Financial Institution | BusinessRole Clearing System | BusinessRole Party |
| :--- | :---: | :---: | :---: |
| Debtor | | | X |
| Creditor | | | X |
| Ultimate Debtor | | | X |
| Ultimate Creditor | | | X |
| Debtor Agent | X | X | |
| Creditor Agent | X | X | |
| Forwarding Agent | X | X | |
| Initiating Party | | | X |
| Account Owner | X | | X |
| Account Servicer | X | X | |
| Payment Clearing Agent | X | X | |
| Payment Settlement Agent | X | X | |
| Intermediary Agent | X | X | |

---

<!-- Page 9 -->

# 4 BusinessProcess Description

## 4.1 Customer-to-Bank Payment Order

This diagram represents the high level BusinessProcesses for the customer-to-bank payment.

**Process end-to-end payment**

- **Process customer-to-bank payment**
  - **Order customer-to-bank payment**
    - Actors: Ultimate Debtor, Instructing Party, Creditor, Debtor
    - Authorize customer-to-bank payment
  - **Accept customer-to-bank payment**
    - Actors: Forwarding Agent, Creditor Agent, Debtor Agent
    - Check customer-to-bank Payment authorisation
    - Validate customer-to-bank payment
    - Assess customer-to-bank Payment risk
    - **Generate regulatory reporting information**
      - Actors: Creditor Agent, Debtor Agent
  - **Clear customer-to-bank payment**
    - Actors: Forwarding Agent, Creditor Agent, Debtor Agent
    - Sort payment
    - Prepare onward interbook payment
  - **Settle customer-to-bank payment**
    - Actors: Debtor, Creditor, Creditor Agent, Debtor Agent
- **Process interbank payment**
- **Report**

---

<!-- Page 10 -->

## Process Customer-to-bank Payment

This BusinessProcess comprises all underlying sub-processes which are all related to the initiation and handling of customer-to-bank payments. The sub-processes are:

* order customer-to-bank payment
* accept customer-to-bank payment
* clear customer-to-bank payment
* settle customer-to-bank payment

### Order Customer-to-bank payment

| Item | Description |
|---|---|
| Definition | An initiating party orders to financial institution (debtor agent or forwarding agent) a payment related instruction. This may refer to an underlying business transaction (for example, an invoice). |
| Trigger | Decision has been made to make a payment (either by a person or a system). |
| Pre-conditions | The required (identifying) information is available to make a payment. |
| Post-conditions | The initiation party sends a CustomerCreditTransferInitiation message to the forwarding agent or debtor agent. |
| Role | Initiating party |

### Authorise Customer-to-Bank Payment

| Item | Description |
|---|---|
| Definition | The authorisation of a payment order by the initiating party. (An authorisation may be implicit if the system where the payment is generated has been approved to generate payments, as the preceding procedures are deemed satisfactory secure. The system will then generate a digital signature without manual intervention. An authorisation may be explicit, if procedures require human approval. The representation of this approval will be included in the payment order or sent to the forwarding or debtor agent as a separate message.) |
| Trigger | A payment order has been created. |
| Pre-conditions | The order payment process has completed and waits for authorisation. |
| Post-conditions | The payment order is authorised. |
| Role | Initiating party |

### Accept Customer-to-Bank Payment

| Item | Description |
|---|---|
| Definition | The payment acceptance includes the checking of the authorisation, the validation of the payment and the process risk assessment. |
| Trigger | Receipt of a payment order. |
| Pre-conditions | The Payment has been received |
| Post-conditions | The payment order has been accepted or rejected. |
| Role | Debtor agent, forwarding agent or creditor agent |

---

<!-- Page 11 -->

# Check Authorisation Customer-to-Bank Payment

| Item | Description |
|---|---|
| Definition | The forwarding or debtor agent checks if initiating party is allowed or entitled to do so as included in the authorisation specifications of the customer profile and the type of payment is in scope. (Authorisation procedures are in some countries required for legal reasons.) (The result of these authorisation procedures can, depending on the authorisation scenario defined, be included in the payment initiation order (for example, one or more signatures included in the payment initiation order), or can result in a dissociated authorisation message, sent by another party than the initiating party, which is referring to the payment initiation message.) |
| Trigger | Established authorisation procedures. |
| Pre-conditions | |
| Post-conditions | The payment will be accepted or rejected for validation and, when applicable, risk assessment. |
| Role | Debtor agent or forwarding agent |

## Validate Customer-to-Bank-payment

| Item | Description |
|---|---|
| Definition | Syntactical check in order to process the payment further. |
| Trigger | Receipt of payment order, positive authorisation check. |
| Pre-conditions | The agent has received the payment order and performed the necessary, Authorisation checks. Validation procedures have been established. |
| Post-conditions | The payment will be accepted for risk assessment, if necessary, or is executable. |
| Role | Debtor agent or forwarding agent |

## Assess Customer-to-Bank-Payment Risk

| Item | Description |
|---|---|
| Definition | Necessary risk checks in order to execute and process the payment further. It can be 'assess static risk', for example, checking of embargo, and 'assess dynamic risk' (check sufficient cash on account, cover received, etc.). |
| Trigger | The payment has been validated and risk criteria have been established. |
| Pre-conditions | Receipt of payment order, positive authorisation and validation check. |
| Post-conditions | The payment or is executable (all information is there to process the payment and the payment risk assessment has been checked). |
| Role | Debtor agent or creditor agent |

## Generate Regulatory Reporting Information

| Item | Description |
|---|---|
| Definition | Information from the payment transaction necessary to meet regulatory reporting requirements (for example, balance of payments reporting, reporting on money-laundering issues, etc.). |
| Trigger | There are regulatory reporting requirements. |
| Pre-conditions | The payment meets regulatory reporting criteria. |

---

<!-- Page 12 -->

| Item | Description |
|---|---|
| Post-conditions | Information for the regulatory reporting has been extracted based in the information in the payment. |
| Role | Debtor agent |

**Clear customer-to-bank payment**

| Item | Description |
|---|---|
| Definition | The agent remits the payment and prepares the information for the next agent in the interbank chain by sorting it and releasing it for onward interbank payment processing. |
| Trigger | Execution date. |
| Pre-conditions | The payment is accepted, the next credit party is not the creditor and the next clearing agent is determined. |
| Post-conditions | Onward interbank payment processing. |
| Role | Debtor agent |

**Settle customer-to-bank payment**

| Item | Description |
|---|---|
| Definition | Credit transfer between the debit party and the credit party. |
| Trigger | Execution date. |
| Pre-conditions | Instructed payment is executable (all information is there to process the payment and the payment validity has been checked). |
| Post-conditions | Transfer of ownership is performed between the debit party and the credit party. |
| Role | Debtor agent |

---

<!-- Page 13 -->

## 4.2 Customer-to-Bank Direct Debit

This diagram represents the high level BusinessProcesses for the direct debit.

**Process Direct Debit end-to-end**

- Manage Direct Debit Mandate
- Process customer-to-bank Direct Debit
  - Initiate collection of (all) off Direct Debit — Forwarding Agent, Initiating Agent, Creditor, Creditor Agent
  - Initiate collection of (all) customer Direct Debit — Forwarding Agent, Initiating Agent, Creditor, Creditor Agent
  - Process reject — Forwarding Agent, Initiating Agent, Creditor, Creditor Agent
  - Process reconciliation for refund — Forwarding Agent, Initiating Agent, Creditor, Creditor Agent
- Process Interbank Direct Debit
  - Process reversal — Forwarding Agent, Initiating Agent, Creditor, Creditor Agent
- Report
  - Process request for cancellation/Reversal — Forwarding Agent, Initiating Agent, Creditor, Creditor Agent

### Initiate Collection of Direct Debit

| Item | Description |
|---|---|
| Definition | The creditor will create the first/one-off instruction and send it to its bank. This first/one-off will differ from subsequent (recurrent) transactions: • The first/one-off instruction may be sent a number of days (as defined in the operating rules) in advance of the settlement date. • In addition to the regular debiting information, which may include the unique mandate reference and the creditor identification, the first/one-off debit instruction may also include information that identifies it as a first under a new mandate or as a one-off transaction |
| Trigger | Initiation of the collection. |
| Pre-conditions | Consensus to use as payment method and debtor authorisation to be debited by the creditor, notification of the debtor. |
| Post-conditions | Initiated collection of direct debit. |
| Role | Initiating Party |

### Reject

| Item | Description |
|---|---|
| Definition | Reconciles reject with the original instructions and identifies the reason for rejection. If the reject results from a formatting error, correct the data and resubmit for processing. |
| Trigger | Reconciliation of the reject. |
| Pre-conditions | Reject received. |
| Post-conditions | Reconciled reject. |
| Role | Creditor agent |

---

<!-- Page 14 -->

## Return/Request for Refund



<table>
  <tr>
    <th>Item</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Definition</td>
    <td>Returns are individual debits that have reached the debtor's agent and have been settled at the inter-bank level, but the debtor's agent is then unable to make the collection for one of a number of reasons, for example, account closed, no funds, customer dead, etc.<br/>The debtor has the unconditional right during "n" days after a debit to instruct its bank to revoke the debit. Following that instruction the debtor's account is credited by his bank and the debit is returned electronically through the clearing process to the creditor's agent.</td>
  </tr>
  <tr>
    <td>Trigger</td>
    <td>Return of a / request for refund.</td>
  </tr>
  <tr>
    <td>Pre-conditions</td>
    <td>Settled instruction subject for return / refund.</td>
  </tr>
  <tr>
    <td>Post-conditions</td>
    <td>Settled instruction / requested refund.</td>
  </tr>
  <tr>
    <td>Role</td>
    <td>Debtor?</td>
  </tr>
</table>



## Reversal



<table>
  <tr>
    <th>Item</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>Definition</td>
    <td>Creditor identifies the original instruction (or a file of instructions) and generates an offsetting transaction in favour of the debtor under quotation of the reversal reason.</td>
  </tr>
  <tr>
    <td>Trigger</td>
    <td>Trigger: reversal of the instruction.</td>
  </tr>
  <tr>
    <td>Pre-conditions</td>
    <td>Settled instruction subject to reversal (collected in error).</td>
  </tr>
  <tr>
    <td>Post-conditions</td>
    <td>Reversed instruction.</td>
  </tr>
  <tr>
    <td>Role</td>
    <td>Creditor agent</td>
  </tr>
</table>

---

<!-- Page 15 -->

# 5 Description of BusinessActivities

This section presents the different BusinessActivities within each BusinessProcess. The BusinessActivities of a process are described with activity diagrams.

**Legend**

| Symbol | Name | Definition |
|---|---|---|
| ● | Start Point | Shows where the lifecycle of the business process commences. |
| ⊙ | End Point | Shows where the lifecycle of the business process may ends. |
| ◇ | Lozenge (or diamond) | Indicates that a choice between several actions can be made. |
| — | Bar | Indicates that several actions are initiated in parallel. |

## 5.1 Customer to Bank Payment Order

In the customer-to-bank payment order(s), multiple participants can be present.

**Simple scenario:**

Debtor → Debtor Agent → Creditor Agent → Creditor

**Complex scenario:**

Ultimate Debtor → Debtor → Initiating Party → Debtor Agent → Creditor Agent → Creditor → Ultimate Creditor

(Initiating Party also connects via Forwarding Agent to Debtor Agent)

---

<!-- Page 16 -->

```
| Initiating Party / Debtor | Forwarding Agent | Debtor Agent | Creditor Agent | Creditor |
|---|---|---|---|---|
| 1. Prepare, authorise and send payment order(s) | 2. Receive and check authentication | | | |
| *Either the Payment Authorisation as set manually or with the payment order(s).* | 3.1 Technical validation | | | |
| | 3.2 Apply business rules | | | |
| | 3.3 Assess static / dynamic risk | | | |
| | 3.4 Rebuild and forward payment order(s) | 4. Receive and check authentication | | |
| | | 5.1 Technical validation | | |
| | | 5.2 Apply business rules | | |
| | | 5.3 Assess static / dynamic risk | | |
| | 6. Receive and forward Status Report | | | |
| | 7. Receive and forward Status Report | | | |
| | 8. Receive and forward Status Report | | | |
| 9. Reconcile and track Payment | 10. Receive and forward acceptance acknowledgement | 11. Send acceptance acknowledgement | 12. Confirm acceptance | |
| | 13. Receive and forward Status Report | | 14. Debit Customer Account and credit internal account | |
| | | 15. Prepare and send Debit Advice(s) | | |
| | | Is a Payment Name? — No → 16. Internal book keeping → 17. Print Cheques → 18. Execution Status | | |
| | | Yes → 19. Rebuild Payment Order(s) → 20. Internal book keeping → 21. Print Cheques | 22. Get cheques and credit transfers | 23. Receive cheques |
| | | | | 24. Reconciliation |
| | | | | 25. Receive account information |
| Reconciliation ongoing? — Yes → Investigation, claim and results → 26. Receive cheque | 27. Receive and forward Execution status | | | |

| Step | Description | Initiator |
|---|---|---|
| Prepare, authorise and send payment order(s) (1) | An initiating party collects the information necessary to initiate a payment to the forwarding or debtor agent. Depending on whether the initiating party is a corporate or an individual, the business information needed in the business process is slightly different. | Initiating Party/Debtor |
| Receive payment order and check authentication (2) | The forwarding agent, if present and debtor agent receive the payment orders from the previous party in the chain. | Forwarding Agent / Debtor Agent |
| Technical Validation (3.1), risk assessment (3.2), apply business rules (3.3) and prepare payment orders for | Necessary checks before processing the payment order further include, for example, syntactical validation. The debtor agent undertakes the necessary risk checks when the execution date is reached, in order to further process the payment. Examples of dynamic risk | Forwarding Agent / Debtor Agent |
```

---

<!-- Page 17 -->

| Step | Description | Initiator |
| :--- | :--- | :--- |
| onward transmission (3.4). | assessment are: is sufficient cash available, has cover been received, etc.<br>Examples of static risk assessment are: check limits, embargo, money laundering information, etc.<br>The forwarding agent (if any) or debtor agent will check business rules that he has logged for the initiating party sending the file. These business rules include information about the customer's profile: the type of transactions the customer is allowed to send, the authorisation procedures set up between customer and receiving agent, etc.<br>The forwarding agent rebuilds the payment order by:<br>• subtracting the failed/invalid individual payment instructions from the payment order he received<br>• building, if relevant, of several payment orders coming from different initiating parties or agents acting as forwarding agents. The merge criteria are defined by the bank | |
| Receive (and forward) status report (4) | The initiating party can receive from the forwarding and/or debtor agent different status reports for the payment order. The payment status report can be produced at different stages of the processing and may have a different business value (depending on the checks performed, for example, payment authentication, syntax validation, risk assessment.).<br>In the case of a relay scenario, there may be a duplication of payment status reports when, for example, a first risk analysis report is produced by the agent acting as a forwarding agent and a second risk analysis report be produced by the debtor agent (acting as the executing agent in that case). A payment status report can only cover the rejected items for a given payment order group or encompass both positive and negative, that is, rejections, acknowledgement for the items in the payment order group. It may optionally report on pre-agreed repair action taken by the bank.<br>At any stage, the payment status report expresses whether the payment order is accepted for further processing (that is, valid from a syntax, business content, risk analysis point of view) or rejected and the reason for rejection or whether the payment has been repaired and how.<br>Depending on the agreement between the initiating party and the debtor agent (or forwarding agent in relay scenario), the payment orders may be rejected as a whole or partially. The rejection criteria can be fixed as a percentage or an absolute number of individual rejected orders or other agreed criteria.<br>Consequently, if all the payment orders are rejected, a global status can be returned with the global reason.<br>In the case of a relay scenario, where the debtor agent generates the status report, it will first be the forwarding agent that receives the status report. The forwarding agent will then forward the status report to the initiating party. "Send negative status report" and "Send positive status reports" are subsets of 'send status report'. A negative | Initiating Party/ Debtor Agent / Forwarding Agent |

---

<!-- Page 18 -->

| Step | Description | Initiator |
|---|---|---|
|  | status report will only include rejected items; a positive status report will include accepted items and repaired items.<br>A 'generic' status report can include a combination of negative and positive status reports.<br>When the initiating party receives a negative status report (containing rejected items), based on the negative status message (reject) from the first or forwarding agent, the initiating party analyses the reason for rejection, corrects the information causing this reject and reverses the payment: he removes the payment from remittance in transit and resets the underlying invoices to payable again. |  |
| Confirm acceptance (5.1) and send (5.2), receive and/or forward (5.3) acceptance acknowledgement. | This acceptance acknowledgement signifies that the payment order (subject to prior information received through the various payment status reports) will be processed by the debtor agent and will trigger accounting entries on the debtor/initiating party account maintained at the debtor agent. | Debtor Agent / Forwarding Agent |
| Reconcile and track payment (6) | The initiating party will reconcile events coming from its information system (e.g. account receivables) with external information feeds (e.g. debit advices, account statement, acceptance notification).<br>This process aims at matching both internal and external views and identifying items for which further attention is required.<br>The reconciliation either ends the financial leg of a transaction (from payment inception to payment completion confirmation) when positive or leads to investigations or claims when negative. | Initiating Party / Debtor |
| Debit account and credit Internal account (7) | The debtor agent debits the account stipulated as being the debit account in the payment order. This includes currency conversion and charges if needed.<br>The debtor agent, after having successfully debited the debtor's account, credits internal accounts in order to transfer the provision necessary to process the payment order further. | Debtor Agent |
| Send, receive and/or forward debit advice (7.1) | The debit advice, prepared by the debtor agent, notifies the initiating party that the settlement has been performed, that is, that the debit entry has been passed on the account of the debtor/initiating party. The initiating party uses it for the reconciliation of entries vis-à-vis payment orders received/remitted.<br>The initiating party receives a notification from the debtor agent, (possibly through the forwarding agent - if any), that the debit entry has been passed on the account of the debtor (which may or may not be equal to the initiating party).<br>This debit advice will be further used for the reconciliation of entries vis-à-vis payment orders received/remitted.<br>The forwarding agent forwards to the initiating party a notification received from the debtor agent that the debit entry has been passed on the account of the debtor/initiating party.<br>This debit advice will be further used by the initiating party for the reconciliation of entries vis-à-vis payment orders | Debtor Agent / Forwarding Agent |

---

<!-- Page 19 -->

| Step | Description | Initiator |
|---|---|---|
| | received/remitted. | |
| Internal bookkeeping (8) | The debtor agent debits the internal account where the provision for further processing of the payment order has been blocked. The creditor agent credits the creditor's account in its books. | Debtor Agent / Creditor Agent |
| Print Cheques (9) | If the initiating party has asked the debtor agent to issue a cheque to pay the creditor, the debtor agent or creditor agent will print a cheque. | Debtor Agent / Creditor Agent |
| Rebuild payment order(s) (10) | The debtor agent rebuilds the payment order by:<br>• subtracting the failed/invalid individual payment instructions from the payment orders he received<br>• subtracting, if relevant, the 'on-us' individual payment instructions from the payment orders he received<br>• merging, if relevant, of several payment orders coming from different initiating parties or agents acting as forwarding agents. The merge criteria are defined by the bank<br>• re-building a consistent remittance | Debtor Agent |
| Send (11) / receive and forward (11.1) execution status | The initiating party optionally receives an execution status report from the debtor agent (possibly through the forwarding agent - if any).<br>The forwarding agent forwards to the initiating party a notification received from the debtor agent that the payment order file has been executed. Depending on the payment method requested and depending on the routing information contained in the payment order:<br>• the creditor(s) has/have been credited in the books of the debtor agent (for 'on-us' payments)<br>• the debtor agent has printed and sent cheques<br>• the debtor agent has sent off the payment orders which need to be further routed in the payment chain (for 'not on-us' payments)<br>If the creditor has an account in the books of the debtor agent (which is same as creditor agent then), this execution status is a 'final' execution status (that is, the creditor has been credited by his agent). In the other cases ('receive cheques'/and when the creditor has an account at a different agent than the debtor agent), the execution status is not yet 'final' - that is, the execution status does not include the actual confirmation of credit of the creditor by his agent - or cashing of cheque by the beneficiary. | Debtor Agent / Forwarding Agent |

---

<!-- Page 20 -->

## 5.2 Customer-to-bank Direct Debit

| Customer | Dealer | Dealer's Bank | Customer's Bank | Dealer's Bank |
|---|---|---|---|---|
| Select Direct Debit | Confirm Direct Debit | Direct Debit Order | Process Direct Debit | Debit Account |
| | | | Credit Account | Direct Debit Instruction |
| Notify Customer | Direct Debit Confirmation | Direct Debit Order | Direct Debit Instruction | Direct Debit Order |
| | | | | Direct Debit Instruction |

## Return Direct Debit

| Customer | Dealer | Dealer's Bank | Customer's Bank | Dealer's Bank |
|---|---|---|---|---|
| Direct Debit Order | Process Direct Debit | Debit Account | Direct Debit Instruction | Select Direct Debit |
| | | | | Confirm Direct Debit |
| | Direct Debit Instruction | | Direct Debit Instruction | Direct Debit Order |
| | | | | Direct Debit Instruction |

---

<!-- Page 21 -->

# Request Refund of Direct Debit

| Customer | Bank | Customer's Bank | HUB (where funds are held by) | Settlement Agent | Sender's Bank |
|---|---|---|---|---|---|
| ● Start | | | | | |
| Request Refund | | | | | refund request? ◇ |
| Confirm and Authorise | | | | | Approve/Reject Refund |
| Approved? ◇ | | | | | Authorise the Request for Refund |
| ● Authorised Request | | | | | Issue Direct Debit Refund |
| Requested Refund Direct Debit | Process Customer Request | | Refund (Direct Debit) Payment Instruction | Confirm and Process Refund Maker to Instruction | |
| | Approve/Reject Claim | Debit Sender Direct Debit | Apply to Customer's Account | | |
| ● Refund not Successful | | | | | |
| | Approve/Reject Claim | | | Return to Creditor | |
| ● | | | | | |
| Requested Credit Entry | | | | | Return Credit |
| ● Refunded Credit Entry | | | | | |

**Flow connections:**

- Start → Request Refund → Confirm and Authorise → (Approved? Yes) → Authorised Request → Requested Refund Direct Debit → Process Customer Request → Approve/Reject Claim → Debit Sender Direct Debit → Refund (Direct Debit) Payment Instruction → Apply to Customer's Account → Refund not Successful / Requested Credit Entry → Refunded Credit Entry.
- Request Refund → refund request? (Sender's Bank) → Approve/Reject Refund → Authorise the Request for Refund → Issue Direct Debit Refund → Confirm and Process Refund Maker to Instruction → Return to Creditor / Return Credit.
- Approve/Reject Claim → (Refund? No) → Refund not Successful.
- Approve/Reject Claim → (Refund? Yes) → Requested Credit Entry.

---

<!-- Page 22 -->

# 6 BusinessTransactions

This section describes the message flows based on the activity diagrams documented above. It shows the typical exchanges of messages in the context of a BusinessTransaction.

## 6.1 CustomerCreditTransferInitiation

The CustomerCreditTransferInitiation message is sent from the initiating party to the debtor agent. Depending on the service level agreed between the debtor agent and the initiating party, the debtor agent may send a CustomerPaymentStatusReport message to inform the initiating party of the status of the initiation.

A number of additional message flows have been included to illustrate the complete end-to-end execution of the CustomerCreditTransferInitiation. However, these messages are out of scope. These message flows are:

**Account information from debtor agent to initiating party**

Depending on the service level agreed, the debtor agent may provide the initiating party with a BankToCustomerDebitCreditNotification ('notification') and/or BankToCustomerAccountReport/BankToCustomerStatement ('statement') once the payment has been executed and the debit entry has been posted to the debtor account. The logical, chronological sequence for sending these messages is defined by the bank implementing and offering these services.

**Interbank clearing and settlement between debtor agent and creditor agent**

Depending on the interbank clearing and settlement method chosen, a number of messages may be exchanged between the agent parties in the payment chain.

**Account information from creditor agent to creditor**

Depending on the service level agreed, the creditor agent may provide the creditor with a BankToCustomerDebitCreditNotification ('notification') and/or BankToCustomerAccountReport/BankToCustomerStatement ('statement') once the payment has been posted to the creditor account. The logical, chronological sequence for sending these messages is defined by the bank implementing and offering these services.

The scenarios below illustrate the different customer roles that can be played on the initiating side of the credit transfer initiation, and on the receiving side of the cash transfer.

On the initiating side, up to three customer roles can be specified: the initiating party, that is, the party sending the message, the debtor, that is the debit account owner, and the ultimate debtor, that is, the party that owes the cash to the creditor as a result of receipt of goods or services.

These three roles can be played by one and the same actor, or they can be played by different actors.

The CustomerCreditTransferInitiation message allows inclusion of the three different roles on the initiating side.

On the receiving side, up to two customer roles can be specified: the creditor, that is, the credit account owner, and the creditor, that is, the party that is the ultimate beneficiary of the cash transfer. These two roles can be played by one and the same actor, or they can be played by different actors.

The CustomerCreditTransferInitiation message allows inclusion of the two different roles on the receiving side.

---

<!-- Page 23 -->

## 6.1.1 One Actor plays roles of Initiating Party, Debtor and Ultimate Debtor, Second actor plays roles of Creditor and Ultimate Creditor

| From | To | Message |
|---|---|---|
| Creditor | Debtor (initiating party) | Invoice & Document |
| Debtor (initiating party) | Debtor Agent | CustomerCreditTransferInitiation |
| Debtor Agent | Debtor (initiating party) | CustomerPaymentStatusReport |
| Debtor Agent | Creditor Agent | FitOfICustomerCreditTransfer |
| Debtor Agent | Debtor (initiating party) | Notification |
| Debtor Agent | Debtor (initiating party) | Statement |
| Creditor Agent | Creditor | Notification |
| Creditor Agent | Creditor | Statement |

The message is sent by an initiating party to the debtor agent. The actor playing the role of initiating party is the same as the actor playing the role of debtor and ultimate debtor. The actor playing the role of creditor is the same as the actor playing the role of creditor.

---

<!-- Page 24 -->

## 6.1.2 One actor plays roles of Initiating Party and Debtor, second actor plays role of Ultimate Debtor

| Creditor | Ultimate Debtor | Debtor (initiating party) | Debtor Agent | Creditor Agent |
|---|---|---|---|---|
| | Invoice → | | | |
| | | CustomerCreditTransferInitiation → | | |
| | | CustomerPaymentStatusReport ← | | |
| | | FitToFiCustomerCreditTransfer ← | | |
| | | Notification ← | | |
| | | Statement ← | | |
| | | Notification ← | | |
| | | Statement ← | | |

The message is sent by an initiating party to the debtor agent. The actor playing the role of initiating party is the same as the actor playing the role of debtor, but the role of the ultimate debtor is played by a different actor.

---

<!-- Page 25 -->

## 6.1.3 Three Different actors play the roles of Initiating Party, Debtor and Ultimate Debtor:

Creditor
Ultimate Debtor
Debtor
Initiating Party
Debtor Agent
Creditor Agent

Invoice
Invoice
Invoice
CustomerCreditTransferInitiation
CustomerPaymentStatusReport
FIToFICustomerCreditTransfer
Notification
Statement
Notification
Statement

The message is sent by an initiating party to the debtor agent. The actor playing the role of initiating party is different from the actor playing the role of debtor. The role of the ultimate debtor is played by yet another actor.

## 6.2 CustomerCreditTransferInitiation - Relay

The CustomerCreditTransferInitiation message is sent from the initiating party to the forwarding agent.

Depending on the service level agreed between the forwarding agent and the initiating party, the forwarding agent may send a CustomerPaymentStatusReport message to inform the initiating party of the status of the initiation.

After performing a series of checks, the forwarding agent will forward the CustomerCreditTransferInitiation message to the relevant debtor agent, that is, the agent that will debit the debtor account.

A relay scenario always requires service level agreements between all parties involved, in which obligations and responsibilities for each party are stipulated.

A number of additional message flows have been included to illustrate the complete end-to-end execution of the payment initiation. However, these messages are out of scope.

The below scenarios show the different customer roles that can be played on the initiating side of the credit transfer initiation, and on the receiving side of the cash transfer.

---

<!-- Page 26 -->

On the initiating side, up to three customer roles can be specified: the initiating party, that is, the party sending the message, the debtor, that is, the debit account owner, and the ultimate debtor, that is, the party that owes the cash to the creditor, as a result of receipt of goods or services.

These three roles can be played by one and the same actor, or they can be played by different actors. The CustomerCreditTransferInitiation message allows inclusion of the three different roles on the initiating side.

On the receiving side, up to two customer roles can be specified: the creditor, that is, the credit account owner, and the creditor, that is, the party that is the ultimate beneficiary of the cash transfer. These two roles can be played by one and the same actor, or they can be played by different actors. The CustomerCreditTransferInitiation message allows inclusion of the two different roles on the receiving side.

## 6.2.1 One actor plays roles of Initiating Party, Debtor and Ultimate Debtor

| Creditor | Debtor | Forwarding Agent | Debtor Agent | Creditor Agent |
|---|---|---|---|---|
| Invoice → | | | | |
| | CustomerCreditTransferInitiation | | | |
| | CustomerPaymentStatusReport | | | |
| | | CustomerCreditTransferInitiation | | |
| | | | | FIToFICustomerCreditTransfer |
| | CustomerPaymentStatusReport | CustomerPaymentStatusReport | | |
| | ← Notification | ← Notification | | |
| | ← Statement | ← Statement | | |
| | ← Notification | | | |
| | ← Statement | | | |

The message is sent by an initiating party to the forwarding agent. The actor playing the role of initiating party is the same as the actor playing the role of debtor and ultimate debtor. This illustrates the scenario

---

<!-- Page 27 -->

in which a company owns accounts abroad and uses a concentrator bank to initiate all its payments. The company plays the role of debtor, ultimate debtor and initiating party and asks the forwarding agent to request the execution of the payment at the debtor agent, that is, the account servicer of the debtor. After performing a series of checks, the forwarding agent will forward the message to the debtor agent.

## 6.2.2 One actor plays roles of Initiating Party and Debtor, Second Actor plays role of Ultimate Debtor

Actors: Creditor | Ultimate Debtor | Debtor (initiating party) | Forwarding Agent | Debtor Agent | Creditor Agent

Message sequence:

- Creditor → Ultimate Debtor: Invoice
- Ultimate Debtor → Debtor (initiating party): Invoice
- Debtor (initiating party) → Forwarding Agent: CustomerCredit TransferInitiation
- Forwarding Agent → Debtor (initiating party): CustomerPayment
- Debtor (initiating party) → Forwarding Agent: StatusReport
- Forwarding Agent → Debtor Agent: CustomerCredit TransferInitiation
- Debtor Agent → Forwarding Agent: CustomerPayment
- Forwarding Agent → Debtor (initiating party): StatusReport
- Creditor Agent → Debtor (initiating party): FitE/FICustomer CreditTransfer
- Debtor (initiating party) → Forwarding Agent: CustomerPayment
- Forwarding Agent → Debtor (initiating party): StatusReport
- Debtor (initiating party) → Forwarding Agent: Notification
- Forwarding Agent → Debtor Agent: Notification
- Debtor (initiating party) → Forwarding Agent: Statement
- Forwarding Agent → Debtor Agent: Statement
- Debtor (initiating party) → Creditor: Notification
- Debtor (initiating party) → Creditor: Statement

The message is sent by an initiating party to the forwarding agent. The actor playing the role of initiating party is the same as the actor playing the role of debtor, but the role of the ultimate debtor is played by a different actor. This illustrates the scenario in which, for example, a company's head office concentrates all payments from its subsidiaries. The head office plays the role of debtor and initiating party, whilst the subsidiaries play the role of originating parties, in this case ultimate debtor. After performing a series of checks, the forwarding agent will forward the message to the debtor agent.

---

<!-- Page 28 -->

## 6.2.3 One actor plays roles of Initiating Party and Ultimate Debtor, Second Actor plays role of Debtor

Creditor | Ultimate Debtor (initiating party) | Forwarding Agent | Debtor | Debtor Agent | Creditor Agent

- Invoice
- CustomerCreditTransferInitiation
- CustomerPaymentStatusReport
- CustomerCreditTransferInitiation
- CustomerPaymentStatusReport
- CustomerPaymentStatusReport
- FIToFICustomerCreditTransfer
- Notification
- Statement
- Notification
- Statement

The message is sent by an initiating party to the forwarding agent. The actor playing the role of initiating party is the same as the actor playing the role of ultimate debtor, but the role of the debtor is played by a different actor. This illustrates the scenario in which, for example, a head office initiates the payment, but has agreed with its subsidiary abroad to use the account of the subsidiary for certain payments. After performing a series of checks, the forwarding agent will forward the message to the debtor agent.

## 6.3 CustomerDirectDebitInitiation and FIToFICustomerDirectDebit

A Direct debit is a request for payment of an amount to be collected from a party bank account (the debtor) by an originator (the creditor). The amounts and dates of collections may vary.

Direct Debits result in cash transfers between debtors and creditors through infrastructures or correspondent banks. They may be exchanged as single instructions but are traditionally grouped following some common characteristics and, for convenience or efficiency reasons, exchanged in a batch mode.

Direct Debits are processed in different ways from country to country, especially regarding the handling of the mandate (when it exists) given by the debtor to the creditor.

The CustomerDirectDebitInitiation message is sent by the initiating party (creditor) to the forwarding agent or creditor agent. It is used to request single or bulk collection(s) of cash from one or various debtor account(s) to a creditor.

---

<!-- Page 29 -->

The FIToFICustomerDirectDebit message is sent by a financial institution to another financial institution, directly or through a clearing system. It is used to clear Direct Debit instructions, initiated by non-financial institution customers.

Only the messages that are part of the scope of the direct debit are illustrated in the diagram.

Creditor → Creditor Agent → Clearing and Settlement Agent → Debtor Agent → Debtor

CustomerDirectDebitInitiation

FIToFICustomerDirectDebit

FIToFICustomerDirectDebit

FIToFICustomerDirectDebit

To provide added value to its customer, a debtor agents may send the instruction (simplified version) to its customer, the debtor, for example, when pre-notifications are not used in a scheme.

The original mandate between the debtor and the creditor and the mandate management itself are identified as being out of scope and are therefore not included in the diagram. Some information on possible mandate management information flow is available below.

The mandate is the authorisation/expression of consent given by the debtor, allowing a specified creditor to originate direct debit instructions to debit a specified debtor account in accordance with the relevant direct debit Scheme Rules and, if applicable, the mandate details.

A valid/authorised mandate represents the debtor agreement to:

- authorise the creditor to issue direct debit instruction(s) to the debtor account
- instruct the debtor agent to act upon the creditor direct debit instruction

| Note | In some cases, the debtor agent is unaware of the mandate and simply acts upon the direct debit instruction. |
|---|---|

A mandate can be an electronic mandate or a mandate in paper form. In case of a paper mandate the creditor dematerialises the mandate upon the mandate presentation in paper form. Dematerialised mandate data are referred to as the Mandate Related Information (MRI) only and are not to be considered as the mandate document. The original mandate remains subject for archiving and reference for any legal matter.

Prior to the sending of a direct debit instruction, the creditor may notify the debtor of the amount and date on which the direct debit instruction will be presented to the debtor agent for debit. This notification may be sent together with or separately from other commercial documents (for example, an invoice).

There are two types of pre-notifications:

- Schedule of payments for a number of subsequent Direct Debits for an agreed period of time.
- Individual advises of a direct debit subject for collection on a specified value date only. In case of recurrent

---

<!-- Page 30 -->

Direct Debit requires an update for each individual recurrent direct debit prior to its collection.

The debtor will reconcile the pre-notification with the signed/authorised mandate and where relevant other records (such as account payable items, contract details or subscription agreement). The debtor ensures the account is covered with subject amount.

The creditor sends the CustomerDirectDebitInitiation message to its agent (the creditor agent), together with the Mandate Related Information when requested by the scheme.

The creditor agent sends an FIToFICustomerDirectDebit message to the clearing and settlement agent, in line with the clearing cycle. The Mandate Related Information (MRI) is also transported, when requested by the scheme.

The clearing and settlement agent sends the FIToFICustomerDirectDebit message, together with the Mandate Related Information (MRI), when requested by the scheme, to the debtor agent.

**Out of scope**

- Optionally, the debtor agent could forward the direct debit instruction (simplified version) to the debtor (for example, if pre-notifications are not used in a scheme).
- If the clearing and settlement agent are two parties the clearing agent prepares and sends the payment information for the settlement agent (in accordance with the agreed and published settlement cycle). The process includes the calculation of the settlement positions and transmission of the files to the Settlement Agent.

The information provided includes the net position to be debited, the party to be debited, the net position to be credited, the party to be credited and the value date.

The clearing agent prepares and sends the payment information for the settlement agent (in accordance with the agreed and published settlement cycle). The process includes the calculation of the settlement positions and transmission of the files to the settlement agent.

The information provided includes the net position to be debited, the party to be debited, the net position to be credited, the party to be credited and the value date.

The settlement is executed by the settlement agent, in accordance with the settlement cycle, based on the settlement report provided by the clearing agent. The settlement agent performs the transfer of funds from the debtor agent to the creditor agent.

Reporting (BankToCustomerDebitCreditNotification message ('notification') and/or BankToCustomerAccountReport/ BankToCustomerStatement message ('statement')) to the debtors and creditors is out of scope. Timing may vary depending on market practices and value added services provided by some agents, that is, before or after settlement.

## 6.4 Negative Customer and FIToFIPaymentStatusReport with Direct Debit

The negative CustomerPaymentStatusReport message (single or grouped) or FIToFIPaymentStatusReport message (single or grouped) is sent by the receiver of an instruction to inform the sender of the instruction about the negative processability of the instruction.

The negative CustomerPaymentStatusReport message FIToFIPaymentStatusReport message used to reject a direct debit instruction, is to be sent before settlement. After settlement, the correct message to be used is the PaymentReturn message.

### 6.4.1 Negative CustomerPaymentStatusReport - Creditor Agent

A negative CustomerPaymentStatusReport message is initiated by the creditor agent to reject a CustomerDirectDebitInitiation message. (Only the messages that are part of the scope of the direct debit are illustrated in the diagram):

---

<!-- Page 31 -->

Creditor
Creditor Agent
Clearing and Settlement Agent
Debtor Agent
Debtor

CustomerDirectDebitInitiation
CustomerPaymentStatusReport

The creditor sends the CustomerDirectDebitInitiation message to its Agent (the creditor agent).
The creditor agent sends a negative CustomerPaymentStatusReport message to the creditor to inform him about the non processability of the CustomerDirectDebitInitiation instruction, for instance due to missing information.

## 6.4.2 Negative CustomerPaymentStatusReport - Clearing And Settlement Agent

A negative FitOfiPaymentStatusReport message is initiated by the clearing and settlement agent to reject an FitOfiCustomerDirectDebit message (only the messages that are part of the scope of the direct debit are illustrated in the diagram):

Creditor
Creditor Agent
Clearing and Settlement Agent
Debtor Agent
Debtor

CustomerDirectDebitInitiation
CustomerPaymentStatusReport
FitOfiCustomerDirectDebit
FitOfiPaymentStatusReport
Information

Whenever possible, the creditor agent will correct or complement the instruction and re-submit. If this is the case, the creditor agent would not send a negative CustomerPaymentStatusReport to the creditor. However, depending on what has been agreed between the creditor and its agent, the creditor agent may inform its customer about the repair, for example, value date.

With respect to 'Information' above: If the creditor agent books after collection (that is cycle is 3 days) then the CustomerPaymentStatusReport message is to be used. If the creditor agent books immediately

---

<!-- Page 32 -->

and the instruction is rejected in the interbank leg, then the creditor needs to be informed of a payment return.

The creditor sends the CustomerDirectDebitInitiation message to its Agent (the creditor agent).

The creditor agent confirms the processability of the CustomerDirectDebitInitiation instruction by sending a positive CustomerPaymentStatusReport message to the creditor.

The creditor agent sends a FIToFICustomerDirectDebit message to the clearing and settlement agent, in line with the clearing cycle. The Mandate Related Information (MRI) is also transported, when applicable.

If information is missing and interbank settlement has not taken place yet, the clearing and settlement agent informs the creditor agent about the non processability of the FIToFICustomerDirectDebit instruction. The creditor agent may inform (but not necessarily) his customer, the creditor, about the negative processing of the CustomerDirectDebitInitiation instruction by using a negative CustomerPaymentStatusReport message, a BankToCustomerDebitCreditNotification message ('notification') or through a BankToCustomerAccountReport and/or BankToCustomerStatement message.


| Note | Before sending a negative CustomerPaymentStatusReport message to its customer, it is assumed that the creditor agent will try to correct the CustomerDirectDebitInitiation message information and re-submit an FIToFICustomerDirectDebit message to the clearing and settlement agent. In this case the creditor will not be involved. |
| :--- | :--- |

## 6.4.3 Negative FIToFIPaymentStatusReport - Debtor Agent

A negative FIToFIPaymentStatusReport message is initiated by the debtor agent to reject the FIToFICustomerDirectDebit message (only the messages that are part of the scope of the direct debit are illustrated in the diagram):

Creditor
Creditor Agent
Clearing and Settlement Agent
Debtor Agent
Debtor

CustomerDirectDebitInitiation
CustomerPaymentStatusReport
FIToFICustomerDirectDebit
FIToFIPaymentStatusReport
FIToFICustomerDirectDebit
FIToFIPaymentStatusReport
FIToFIPaymentStatusReport
Information

Whenever possible, the creditor agent will correct or complement the instruction and re-submit. If this is the case, the creditor agent would not send a negative CustomerPaymentStatusReport to the creditor.

---

<!-- Page 33 -->

However, depending on what has been agreed between the creditor and its agent, the creditor agent may inform its customer about the repair, for example, value date.

With respect to 'Information' above: if the creditor agent books after collection, for example, cycle is 3 days, then the CustomerPaymentStatusReport message is to be used. If the creditor agent books immediately and the instruction is rejected in the interbank leg, then the creditor needs to be informed of a payment return.

The creditor sends a CustomerDirectDebitInitiation message to its Agent (the creditor agent).

The creditor agent confirms the processability of the CustomerDirectDebitInitiation message by sending a positive

**6.4 CustomerPaymentStatusReport message to the Creditor**

The creditor agent sends a FitOfiCustomerDirectDebit message to the clearing and settlement agent, in line with the clearing cycle. The Mandate Related Information (MRI) is also transported, when applicable.

The clearing and settlement agent confirms the processability of the FitOfiCustomerDirectDebit message by sending a positive FitOfiPaymentStatusReport message to the creditor agent.

The clearing and settlement agent sends a FitOfiCustomerDirectDebit message, optionally with the Mandate Related Reference (MRI), to the debtor agent immediately for information purposes only.

If settlement has not yet taken place, the debtor agent may send a negative FitOfiPaymentStatusReport message to the clearing and settlement agent, to inform him about the rejection of the FitOfiCustomerDirectDebitInstruction. This negative FitOfiPaymentStatusReport message may subsequently be forwarded to the creditor agent. The creditor agent may inform (but not necessarily) his customer, the creditor, about the negative processing of the CustomerDirectDebitInitiation instruction by using a CustomerPaymentStatusReport message, a BankToCustomerDebitCreditNotification message ('notification') or through a BankToCustomerAccountReport and/or BankToCustomerStatement message ('statement').

**6.5 Positive Customer and FitOfiPaymentStatusReport with Direct Debit**

The positive CustomerPaymentStatusReport message (single or grouped) and FitOfiPaymentStatusReport message (single or grouped) is sent by the receiver of an instruction to inform the receiver that the instruction received is processable.

A positive CustomerPaymentStatusReport message or FitOfiPaymentStatusReport message can also be used to confirm the processability of a PaymentReversal message (in case of FitOfi) or a PaymentReversal message.

The positive CustomerPaymentStatusReport message and FitOfiPaymentStatusReport message are also meant to be generic to ensure re-usability with other Payments Instruments.

The CustomerPaymentStatusReport and FitOfiPaymentStatusReport messages are exchanged, point to point between two parties, optionally and as per bilateral agreements and may be complemented by a BankToCustomerDebitCreditNotification message ('notification') and/or BankToCustomerAccountReport/ BankToCustomerStatement message ('statement').

**6.5.1 Confirmation of Processability of CustomerDirectDebitInitiation**

This scenario shows the use of the CustomerPaymentStatusReport message and FitOfiPaymentStatusReport message to confirm the processability of a CustomerDirectDebitInitiation

---

<!-- Page 34 -->

instruction, followed by an FIToFICustomerDirectDebit message (only the messages that are part of the scope of the direct debit are illustrated in the diagram):

![](images/image_01.png)

The positive CustomerPaymentStatusReport and FIToFIPaymentStateReport messages are optional.

To provide added value to its creditor, a bank may send a CustomerPaymentStatusReport message with an updated status to inform the creditor about the status of the transaction. The status updates may be provided throughout the life-cycle of the transaction.

A 'mixed' CustomerPaymentStatusReport or FIToFIPaymentStatusReport message may be exchanged, that is, the status is 'partially accepted' at group level, indicating that the group contains a mix of accepted, pending or rejected transactions.

The creditor sends the CustomerDirectDebitInitiation message to its Agent (the creditor agent).

The creditor agent confirms the processability of the CustomerDirectDebitInitiation instruction by sending a positive CustomerPaymentStatusReport message to the creditor.

The creditor agent sends an FIToFICustomerDirectDebit message to the clearing and settlement agent, in line with the clearing cycle. The Mandate Related Information (MRI) is also transported, when applicable.

The clearing and settlement agent confirms the processability of the FIToFICustomerDirectDebit instruction by sending a positive FIToFIPaymentStatusReport message to the creditor agent.

The clearing and settlement agent sends an FIToFICustomerDirectDebit message, optionally with the Mandate Related Information (MRI) to the debtor agent immediately for information purposes only.

The debtor agent sends a positive FIToFIPaymentStatusReport message to the clearing and settlement agent. This positive status message may be subsequently be forwarded to the creditor agent.

## 6.6 PaymentReturn with Direct Debit

A PaymentReturn message is initiated by the debtor agent and sent to the previous party in the payment chain when a debit cannot be executed due to an administrative reason (such as non-existing/closed account) or due to a banking reason (such as insufficient funds). The PaymentReturn message is also the message to be used by the debtor agent following the receipt of a refund request by the debtor as it is assumed that the refund request will be done through a non-automated tool (such as phone/fax) and is

---

<!-- Page 35 -->

not part of the scope. In this case, the PaymentReturn message will contain a code to indicate that it is triggered by a request for refund by the debtor.

## 6.6.1 PaymentReturn Initiated by Debtor Agent

A PaymentReturn message is initiated by the debtor agent (only the messages that are part of the scope of the direct debit are illustrated in the diagram):

```
 Creditor        Creditor Agent      Clearing and Settlement   Debtor Agent        Debtor
    |                 |                     Agent                  |                 |
    | CustomerDirectDebitInitiation        |                 |                 |
    |------------------------------------>|                 |                 |
    | CustomerPaymentStatusReport          |                 |                 |
    |<------------------------------------|                 |                 |
    |                 | FitToFiCustomerDirectDebit          |                 |
    |                 |------------------------------------>|                 |
    |                 | FitToFiPaymentStatusReport          |                 |
    |                 |<------------------------------------|                 |
    |                 |                     | FitToFiCustomerDirectDebit      |
    |                 |                     |-------------------------------->|
    |                 |                     | FitToFiPaymentStatusReport      |
    |                 |                     |<--------------------------------|
    |                 |                     | PaymentReturn                   |
    |                 |                     |<--------------------------------|
    |                 |                     | FitToFiPaymentStatusReport      |
    |                 |                     |-------------------------------->|
    |                 |                     |                 | RefundRequest |
    |                 |                     |                 |<--------------|
    |                 | PaymentReturn       |                 |                 |
    |                 |<------------------------------------|                 |
    |                 | FitToFiPaymentStatusReport          |                 |
    |                 |<------------------------------------|                 |
```

With respect to the RefundRequest, the payment return process can be triggered by a RefundRequest by the debtor or initiated by the debtor agent.

If the booking of the original instruction on the creditor's account has already taken place, the return of the funds will be notified to the creditor through return information included in a BankToCustomerNotification message and/or a BankToCustomerAccountReport or a BankToCustomerStatement message.

The creditor sends the CustomerDirectDebitInitiation message to its Agent (the creditor agent).

The creditor agent confirms the processability of the CustomerDirectDebitInitiation instruction by sending a positive CustomerPaymentStatusReport to the creditor.

The creditor agent sends a FitToFiCustomerDirectDebit message to the clearing and settlement agent, in line with the clearing cycle. The Mandate Related Information (MRI) is also transported, when applicable.

The clearing and settlement agent confirms the processability of the FitToFiCustomerDirectDebit instruction by sending a positive FitToFiPaymentStatusReport message to the creditor agent.

The clearing and settlement agent sends a FitToFiCustomerDirectDebit message, optionally with the Mandate Related Reference (MRR) to the debtor agent immediately for information purposes only.

---

<!-- Page 36 -->

The debtor agent sends a positive FIToFIPaymentStatusReport message to the clearing and settlement agent.

If the debtor agent is unable to make the collection from the debtor Account for one or several reasons (for example, insufficient funds, customer deceased), the debtor agent will initiate a PaymentReturn message, and route it through the clearing and settlement agent to the creditor agent, giving the reason for the Return.

The clearing and settlement agent optionally confirms the receipt of the PaymentReturn message by sending a positive FIToFIPaymentStatusReport message to the debtor agent.

The clearing and settlement agent forwards the PaymentReturn message to the creditor agent.

If the clearing and settlement agent are two parties the Clearing Agent prepares the (returned) payment information for the Settlement Agent (the net position to be debited, the party to be debited, the net position to be credited, the party to be credited and the value date) in accordance with the agreed and published settlement cycle. The Settlement Agent performs the transfer of cash from the credit party to the debit party (in accordance with the agreed published settlement cycle). (Out of scope and not illustrated).

The creditor agent will optionally confirm receipt of the PaymentReturn message to the clearing and settlement agent. Depending on agreements between the creditor and the creditor agent, the creditor may be informed either through a negative CustomerPaymentStatusReport message, or through a CustomerToBankDebitCreditNotification message ('notification') or through a BankToCustomerAccountReport and/or BankToCustomerStatement message ('statement') about the funds return and thus the debit on his account.

### 6.6.2 Refund by the Debtor

This scenario is similar to the previous scenario, except that the PaymentReturn message by the debtor agent to the clearing and settlement agent is triggered by a Refund Request by the debtor to his agent, the debtor agent (in a non-automated manner). In this case, the PaymentReturn message will contain a code indicating that it was triggered by a request for refund by the debtor.

## 6.7 Customer Payment Reversal with Direct Debit

The creditor will initiate a CustomerPaymentReversal message, after settlement, when a paid direct debit should not have been processed.

The creditor agent will, in turn, initiate an FIToFIPaymentReversal message for the next agent in the payment chain. Consequently, the debtor will be credited.



| Note | The creditor agent may be the originator of a payment reversal - he will in this case initiate an FIToFIPaymentReversal message (only the potential messages that are part of the scope of the direct debit are illustrated in the diagram): |
| :--- | :--- |

---

<!-- Page 37 -->

Creditor | Creditor Agent | Clearing and Settlement Agent | Debtor Agent | Debtor

CustomerDirectDebit Initiation

CustomerPaymentStatus Report

FIToFICustomerDirectDebit

FIToFIPaymentStatusReport

FIToFICustomerDirectDebit

FIToFIPaymentStatusReport

Start of the reversal, for example, in the case of a duplicated direct debit instruction

CustomerPaymentReversal

CustomerPaymentStatus Report

FIToFIPaymentReversal

FIToFIPaymentStatusReport

FIToFIPaymentReversal

FIToFIPaymentStatusReport

The creditor sends a CustomerDirectDebitInitiation message to its agent (the creditor agent).

The creditor agent confirms the processability of the CustomerDirectDebitInitiation instruction by sending a positive CustomerPaymentStatusReport message to the creditor.

The creditor agent sends a FIToFICustomerDirectDebit message to the clearing and settlement agent, in line with the clearing cycle. The Mandate Related Information (MRI) is also transported, when applicable.

The clearing and settlement agent confirms the processability of the FIToFICustomerDirectDebit instruction by sending a positive FIToFIPaymentStatusReport message to the creditor agent.

The clearing and settlement agent sends an FIToFICustomerDirectDebit message, optionally with the Mandate Related Reference (MRR), to the debtor agent immediately for information purposes only.

The debtor agent sends a positive FIToFIPaymentStatusReport message to the clearing and settlement agent. The creditor realises this was a duplicated CustomerDirectDebitInitiation instruction. He now wants to send a CustomerPaymentReversal message. He identifies the original CustomerDirectDebitInitiation message (or a file of direct debit instructions) and generates an offsetting transaction in favour of the debtor, under the quotation of the reversal reasons. The creditor agent may confirm the receipt of the CustomerPaymentReversal message by sending a positive CustomerPaymentStatusReport message to the creditor.

An FIToFIPaymentReversal message is submitted by the creditor agent to the clearing and settlement agent for settlement, under quotation of the original direct debit reference and the reason for the reversal.

---

<!-- Page 38 -->

The Clearing Agent confirms the processability of the reversal by sending a positive FIToFIPaymentStatusReport message to the creditor agent.

The clearing and settlement agent forwards the FIToFIPaymentReversal message to the debtor agent immediately for information purposes only.

In case the clearing and settlement agent are two parties the Clearing Agent prepares the payment information for the Settlement Agent (in accordance with the agreed and published settlement cycle). That process includes the calculation of the settlement positions.

The information provided to the Settlement Agent is the net position to be debited, the party to be debited, the net position to the credited, the party to be credited and the value date (Out of Scope).

The Settlement Agent performs the transfer of funds from the Credit Party to the Debit Party (in accordance with the agreed and published settlement cycle) (Out of Scope).

A positive FIToFIPaymentStatusReport message can optionally be initiated by the debtor agent and sent to the clearing and settlement agent to confirm the processability of the reversal message.



| Note | It may exceptionally occur that a PaymentReturn message and a CustomerPaymentReversal message would cross each other, this could only be avoided through value-added monitoring services that could be offered by the scheme manager and/or this might provoke exceptions/investigation handling. |
|------|------|

---

<!-- Page 39 -->

# 7 Business Examples

## 7.1 CustomerCreditTransferInitiation pain.001.001.12

**Description**

ABC Corporation, New York has received three invoices:

**Invoice 1**

An invoice with number 4562, dated 08 September 2012 from DEF Electronics, London: 10 million JPY needs to be paid to DEF Electronics account 23683707094215 with AAAA Bank, London (AAAAGB2L). ABC Corporation assigns reference ABC/4562/2012-09-08 to the payment. Payment transaction charges are shared between ABC Corporation and DEF Electronics.

**Invoice 2**

An invoice with number ABC-13679, dated 15 September 2012 from GHI Semiconductors, Brussels: 500,000 EUR needs to be paid to GHI Semiconductors account BE30001216371411 with DDDD Bank, Belgium (DDDDBEBB). ABC Corporation assigns reference ABC/ABC-13679/2012-09-15 to the payment. The accounts receivable department of GHI Semiconductors needs to be advised when the funds have been credited on the account on telephone number +32/2/2222222. GHI Semiconductors will bear all payment transaction charges.

**Invoice 3**

An invoice with number 987-AC, dated 27 September 2012, from their branch ABC Corporation, California: 1 million USD needs to be paid to the branch account 4895623 with BBBB Bank, San Francisco (BBBBUS88). ABC assigns a reference ABC/987-AC/2012-09-27 to the payment. Payment transaction charges are shared.

ABC Corporation holds an account 00125574999 with BBBB Bank, New York (BBBBUS33) and instructs its bank to execute payment of the invoices with a CustomerCreditTransferInitiation message.

**Business Data**

CustomerCreditTransferInitiation from ABC Corporation, New York to BBBB Bank, New York:



<table>
  <tr>
    <th>Element</th>
    <th>&lt;XMLTag&gt;</th>
    <th>Content</th>
  </tr>
  <tr>
    <td>Group Header</td>
    <td>&lt;GrpHdr&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>MessageIdentification</td>
    <td>&lt;MsgId&gt;</td>
    <td>ABC/120928/CCT001</td>
  </tr>
  <tr>
    <td>CreationDateTime</td>
    <td>&lt;CreDtTm&gt;</td>
    <td>2012-09-28T14:07:00</td>
  </tr>
  <tr>
    <td>NumberOfTransactions</td>
    <td>&lt;NbOfTxs&gt;</td>
    <td>3</td>
  </tr>
  <tr>
    <td>Controlsum</td>
    <td>&lt;CtrlSum&gt;</td>
    <td>11500000</td>
  </tr>
  <tr>
    <td>InitiatingParty</td>
    <td>&lt;InitgPty&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>Name</td>
    <td>&lt;Nm&gt;</td>
    <td>ABC Corporation</td>
  </tr>
  <tr>
    <td>PostalAddress</td>
    <td>&lt;PstlAdr&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>StreetName</td>
    <td>&lt;StrtNm&gt;</td>
    <td>Times Square</td>
  </tr>
  <tr>
    <td>BuildingNumber</td>
    <td>&lt;BldgNb&gt;</td>
    <td>7</td>
  </tr>
  <tr>
    <td>PostCode</td>
    <td>&lt;PstCd&gt;</td>
    <td>NY 10036</td>
  </tr>
  <tr>
    <td>TownName</td>
    <td>&lt;TwnNm&gt;</td>
    <td>New York</td>
  </tr>
  <tr>
    <td>Country</td>
    <td>&lt;Ctry&gt;</td>
    <td>US</td>
  </tr>
  <tr>
    <td>PaymentInformation</td>
    <td>&lt;PmtInf&gt;</td>
    <td></td>
  </tr>
</table>

---

<!-- Page 40 -->

| Element | <XMLTag> | Content |
| :--- | :--- | :--- |
| PaymentInformationIdentification | <PmtInfId> | ABC/086 |
| PaymentMethod | <PmtMtd> | TRF |
| BatchBooking | <BtchBookg> | FALSE |
| RequestedExecutionDate | <ReqdExctnDt> | 2012-09-29 |
| Date | <Dt> | |
| Debtor | <Dbtr> | |
| Name | <Nm> | ABC Corporation |
| PostalAddress | <PstlAdr> | |
| StreetName | <StrNm> | Times Square |
| BuildingNumber | <BldgNb> | 7 |
| PostCode | <PstCd> | NY 10036 |
| TownName | <TwnNm> | New York |
| Country | <Ctry> | US |
| DebtorAccount | <DbtrAcct> | |
| Identification | <Id> | |
| Other | <Othr> | |
| Identification | <Id> | 00125574999 |
| DebtorAgent | <DbtrAgt> | |
| FinancialInstitutionIdentification | <FinInstlId> | |
| BICFI | <BICFI> | BBBUS33 |
| CreditTransferTransactionInformation | <CdtTrfTxInf> | |
| PaymentIdentification | <PmtId> | |
| InstructionIdentification | <InstrId> | ABC/120928/CCT001/1 |
| EndToEndIdentification | <EndToEndId> | ABC/4562/2012-09-08 |
| Amount | <Amt> | |
| InstructedAmount | <InstdAmt> | JPY 10000000 |
| ChargeBearer | <ChrgBr> | SHAR |
| CreditorAgent | <CdtorAgt> | |
| FinancialInstitutionIdentification | <FinInstlId> | |
| BICFI | <BICFI> | AAAAGB2L |
| Creditor | <Cdtor> | |
| Name | <Nm> | DEF Electronics |
| PostalAddress | <PstlAdr> | |
| AddressLine | <AdrLine> | Corn Exchange 5th Floor |
| AddressLine | <AdrLine> | Mark Lane 55 |
| AddressLine | <AdrLine> | EC3R7NE London |
| AddressLine | <AdrLine> | GB |
| CreditorAccount | <CdtorAcct> | |
| Identification | <Id> | |

---

<!-- Page 41 -->

| Element | <XMLTag> | Content |
| :--- | :--- | :--- |
| Other | <Othr> | |
| Identification | <Id> | 23683707994215 |
| Purpose | <Purp> | |
| Code | <Cd> | GDDS |
| RemittanceInformation | <RmtInf> | |
| Structured | <Strd> | |
| ReferredDocumentInformation | <RtrdDocInf> | |
| Type | <Type> | |
| CodeOrProprietary | <CdOrPrtry> | |
| Code | <Cd> | CINV |
| Number | <Nb> | 4562 |
| RelatedDate | <RltdDt> | |
| Type | <Tp> | |
| Code | <Cd> | INDA |
| Date | <Dt> | 2012-09-08 |
| CreditTransferTransactionInformation | <CdtTrfTxInf> | |
| PaymentIdentification | <PmtId> | |
| InstructionIdentification | <InstrId> | ABC/120928/CCT001/2 |
| EndToEndIdentification | <EndToEndId> | ABC/ABC-13679/2012-09-15 |
| Amount | <Amt> | |
| InstructedAmount | <InstdAmt> | EUR 500000 |
| ChargeBearer | <ChrgBr> | CRED |
| CreditorAgent | <CdtrAgt> | |
| FinancialInstitutionIdentification | <FinInstnId> | |
| BICFI | <BICFI> | DDDDBEBB |
| Creditor | <Cdtr> | |
| Name | <Nm> | GHI Semiconductors |
| PostalAddress | <PstlAdr> | |
| StreetName | <StrtNm> | Avenue Brugmann |
| BuildingNumber | <BldgNb> | 415 |
| PostCode | <PstCd> | 1180 |
| TownName | <TwnNm> | Brussels |
| Country | <Ctry> | BE |
| CreditorAccount | <CdtrAcct> | |
| Identification | <Id> | |
| IBAN | <IBAN> | BE30001216371411 |
| InstructionForCreditorAgent | <InstrForCdtrAgt> | |
| Code | <Cd> | PHOB |
| InstructionInformation | <InstrInf> | +32/2/2222222 |

---

<!-- Page 42 -->

| Element | <XMLTag> | Content |
| :--- | :--- | :--- |
| Purpose | <Purp> | |
| Code | <Cd> | GDDS |
| RemittanceInformation | <RmtInf> | |
| Structured | <Strd> | |
| ReferredDocumentInformation | <RtrdDocInf> | |
| Type | <RtrdDocType> | |
| CodeOrProprietary | <CdOrPrtry> | |
| Code | <Cd> | CINV |
| Number | <Nb> | ABC-13679 |
| RelatedDate | <RltdDt> | |
| Type | <Tp> | |
| Code | <Cd> | INDA |
| Date | <Dt> | 2012-09-15 |
| CreditTransferTransactionInformation | <CdtTrfTxInf> | |
| PaymentIdentification | <PmtId> | |
| InstructionIdentification | <InstrId> | ABC/120928/CCT001/3 |
| EndToEndIdentification | <EndToEndId> | ABC/987-AC/2012-09-27 |
| Amount | <Amt> | |
| InstructedAmount | <InstdAmt> | USD 1.000.000 |
| ChargeBearer | <ChrgBr> | SHAR |
| CreditorAgent | <CdtrAgnt> | |
| FinancialInstitutionIdentification | <FinInstnId> | |
| BICFI | <BICFI> | BBBBUS66 |
| Creditor | <Cdtor> | |
| Name | <Nm> | ABC Corporation |
| PostalAddress | <PstlAdr> | |
| Department | <Dpt> | Treasury department |
| StreetName | <StrtNm> | Bush Street |
| BuildingNumber | <BldgNb> | 13 |
| PostCode | <PstCd> | CA 94108 |
| TownName | <TwnNm> | San Francisco |
| Country | <Ctry> | US |
| CreditorAccount | <CdtrAcct> | |
| Identification | <Id> | |
| Other | <Othr> | |
| Identification | <Id> | 4895623 |
| Purpose | <Purp> | |
| Code | <Cd> | INTC |
| RemittanceInformation | <RmtInf> | |

---

<!-- Page 43 -->

| Element | <XMLTag> | Content |
| :--- | :--- | :--- |
| Structured | <Strd> | |
| ReferredDocumentInformation | <RtrdDocInf> | |
| Type | <Type> | |
| CodeOrProprietary | <CdOrPrtry> | |
| Code | <Cd> | CINV |
| Number | <Nb> | 987-AC |
| RelatedDate | <RltdDt> | |
| Type | <Tp> | |
| Code | <Cd> | INDA |
| Date | <Dt> | 2012-09-27 |

**Message Instance**

<CstmrCdtTrfInit>
    <GrpHdr>
        <MsgId>ABC/120928/CCT001</MsgId>
        <CreDtTm>2012-09-28T14:07:00</CreDtTm>
        <NbOfTxs>3</NbOfTxs>
        <CtrlSum>11500000</CtrlSum>
        <InitPty>
            <Nm>ABC Corporation</Nm>
            <PstlAdr>
                <StrtNm>Times Square</StrtNm>
                <BldgNb>7</BldgNb>
                <PstCd>NY 10036</PstCd>
                <TwnNm>New York</TwnNm>
                <Ctry>US</Ctry>
            </PstlAdr>
        </InitPty>
    </GrpHdr>
    <PmtInf>
        <PmtInfId>ABC/086</PmtInfId>
        <PmtMtd>TRF</PmtMtd>
        <BtchBookg>false</BtchBookg>
        <ReqdExctnDt>
            <Dt>2012-09-29</Dt>
        </ReqdExctnDt>
        <Dbtr>
            <Nm>ABC Corporation</Nm>

---

<!-- Page 44 -->

```xml
<PstlAdr>
<StrtNm>Times Square</StrtNm>
<BldgNb>7</BldgNb>
<PstCd>NY 10036</PstCd>
<TwnNm>New York</TwnNm>
<Ctry>US</Ctry>
</PstlAdr>
</Dbtr>
<DbtrAcct>
<Id>
<Othr>
<Id>00125574999</Id>
</Othr>
</Id>
</DbtrAcct>
<DbtrAgt>
<FinInstlId>
<BICFI>BBBBUS33</BICFI>
</FinInstlId>
</DbtrAgt>
<CdtTrfTxInf>
<RmtId>
<InstrId>ABC/120928/CCT001/01</InstrId>
<EndToEndId>ABC/4562/2012-09-08</EndToEndId>
</RmtId>
<Amt>
<InstdAmt Ccy="JPY">10000000</InstdAmt>
</Amt>
<ChrgBr>SHAR</ChrgBr>
<CdtrAgt>
<FinInstlId>
<BICFI>AAAAGB2L</BICFI>
</FinInstlId>
</CdtrAgt>
<Cdtr>
<Nm>DEF Electronics</Nm>
<PstlAdr>
<AdrLine>Corn Exchange 5th Floor</AdrLine>
<AdrLine>Mark Lane 55</AdrLine>
```

---

<!-- Page 45 -->

```
<AdrLine>EC3R7NE London</AdrLine>
<AdrLine>GB</AdrLine>
</PstlAdr>
</Cdtr>
<CdtrAcct>
<Id>
<Othr>
<Id>23683707994125</Id>
</Othr>
</Id>
</CdtrAcct>
<Purp>
<Cd>GDDS</Cd>
</Purp>
<RmtInf>
<Strd>
<RfrdDocInf>
<Tp>
<CdOrPrtry>
<Cd>CINV</Cd>
</CdOrPrtry>
</Tp>
<Nb>4562</Nb>
<RltdDt>
<Tp>
<Cd>INDA</Cd>
</Tp>
<Dt>2012-09-08</Dt>
</RltdDt>
</RfrdDocInf>
</Strd>
</RmtInf>
</CdtTrfTxInf>
<CdtTrfTxInf>
<PmtId>
<InstrId>ABC/120928/CCT001/2</InstrId>
<EndToEndId>ABC/ABC-13679/2012-09-15</EndToEndId>
</PmtId>
<Amt>
```

---

<!-- Page 46 -->

```
<InstdAmt Ccy="EUR">500000</InstdAmt>
</Amt>
<ChrgBr>CRED</ChrgBr>
<CdtrAgt>
  <FinInstnId>
    <BICFI>DDDDBEBB</BICFI>
  </FinInstnId>
</CdtrAgt>
<Cdtr>
  <Nm>GHI Semiconductors</Nm>
  <PstlAdr>
    <StrtNm>Avenue Brugmann</StrtNm>
    <BldgNb>415</BldgNb>
    <PstCd>1180</PstCd>
    <TwnNm>Brussels</TwnNm>
    <Ctry>BE</Ctry>
  </PstlAdr>
</Cdtr>
<CdtrAcct>
  <Id>
    <IBAN>BE30001216371411</IBAN>
  </Id>
</CdtrAcct>
<InstrForCdtrAgt>
  <Cd>PHOB</Cd>
  <InstrInf>+32/2/2222222</InstrInf>
</InstrForCdtrAgt>
<Purp>
  <Cd>GDDS</Cd>
</Purp>
<RmtInf>
  <Strd>
    <RfrdDocInf>
      <Tp>
        <CdOrPrtry>
          <Cd>CINV</Cd>
        </CdOrPrtry>
      </Tp>
      <Nb>ABC-13679</Nb>
```

---

<!-- Page 47 -->

```
<RltDt>
<Tp>
<Cd>INDA</Cd>
</Tp>
<Dt>2012-09-15</Dt>
</RltDt>
</RfrdDocInf>
</Strd>
</RmtrInf>
</CdtTrfXlIn>
<CdtTrfXlIn>
<PmtId>
<Instd>ABC/120928/CCT001/3</Instd>
<EndToEndId>ABC/987-AC/2012-09-27</EndToEndId>
</PmtId>
<Amt>
<InstdAmt Ccy="USD">1000000</InstdAmt>
</Amt>
<ChrgBr>SHAR</ChrgBr>
<CdtrAgt>
<FinInstnId>
<BICFI>BBBBUS66</BICFI>
</FinInstnId>
</CdtrAgt>
<Cdtr>
<Nm>ABC Corporation</Nm>
<PstlAdr>
<Dept>Treasury department</Dept>
<StrtNm>Bush Street</StrtNm>
<BldgNb>13</BldgNb>
<PstCd>CA 94108</PstCd>
<TwnNm>San Francisco</TwnNm>
<Ctry>US</Ctry>
</PstlAdr>
</Cdtr>
<CdtrAcct>
<Id>
<Othr>
<Id>4895623</Id>
```

---

<!-- Page 48 -->

</Othr>
</Id>
</CdtmAcct>
<Purp>
<Cd>INTC</Cd>
</Purp>
<RmtnInf>
<Strd>
<RfrdDocInf>
<Tp>
<CdOrPrtry>
<Cd>CINV</Cd>
</CdOrPrtry>
</Tp>
<Nb>987-AC</Nb>
<RltdDt>
<Tp>
<Cd>INDA</Cd>
</Tp>
<Dt>2012-09-27</Dt>
</RltdDt>
</RfrdDocInf>
</Strd>
</RmtnInf>
</CdtmTrfTxInf>
</PmtInf>
</CstmrCdtTrfInitn>

## 7.2 CustomerPaymentStatusReport pain.002.001.14 - 1

**Description**

As follow-up to the payment initiation by ABC Corporation, BBBBUS33 sends a CustomerPaymentStatusReport to acknowledge that the message passed technical validation and was accepted, based on the customer profile.

**Business Data**

CustomerPaymentStatusReport from BBBB Bank to ABC Corporation:



<table>
  <tr>
    <th>Element</th>
    <th>XML Tag</th>
    <th>Content</th>
  </tr>
  <tr>
    <td>Group Header</td>
    <td>&lt;GrpHdr&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>MessageIdentification</td>
    <td>&lt;MsgId&gt;</td>
    <td>BBBB/120928-PSR/001</td>
  </tr>
  <tr>
    <td>CreationDateTime</td>
    <td>&lt;CreDtTm&gt;</td>
    <td>2012-09-28T14:09:00</td>
  </tr>
</table>

---

<!-- Page 49 -->

| Element | XML Tag | Content |
| :--- | :--- | :--- |
| InitiatingParty | <InitgPty> | |
| Name | <Nm> | ABC Corporation |
| PostalAddress | <PstlAdr> | |
| StreetName | <StrtNm> | Times Square |
| BuildingNumber | <BldgNb> | 7 |
| PostCode | <PstCd> | NY 10036 |
| TownName | <TwnNm> | New York |
| Country | <Ctry> | US |
| DebtorAgent | <DbtrAgt> | |
| FinancialInstitutionIdentification | <FinInstlId> | |
| BICFI | <BICFI> | BBBBUS33 |
| OriginalGroupInformationAndStatus | <OrgnlGrpInfAndSts> | |
| OriginalMessageIdentification | <OrgnlMsgId> | ABC/120928/CCT001 |
| OriginalMessageNameIdentification | <OrgnlMsgNmId> | pain.001.001.12 |
| OriginalCreationDateTime | <OrgnlCreDtTm> | 2012-09-28T14:07:00 |
| OriginalNumberOfTransactions | <OrgnlNbOfTxs> | 3 |
| OriginalControlSum | <OrgnlCtrSum> | 1.500.000 |
| GroupStatus | <GrpSts> | ACCP |

**Message Instance**

```xml
<CstmrPmtStsRpt>
    <GrpHdr>
        <MsgId>BBB/120928-PSR/001</MsgId>
        <CreDtTm>2012-09-28T14:09:00</CreDtTm>
        <InitgPty>
            <Nm>ABC Corporation</Nm>
            <PstlAdr>
                <StrtNm>Times Square</StrtNm>
                <BldgNb>7</BldgNb>
                <PstCd>NY 10036</PstCd>
                <TwnNm>New York</TwnNm>
                <Ctry>US</Ctry>
            </PstlAdr>
        </InitgPty>
        <DbtrAgt>
            <FinInstlId>
                <BICFI>BBB BUS33</BICFI>
            </FinInstlId>
```

---

<!-- Page 50 -->

</DbtrAgt>
</GrpHdr>
<OrgnlGrpInfAndSts>
    <OrgnlMsgId>ABC/120928/CCT001</OrgnlMsgId>
    <OrgnlMsgNmId>pain.001.001.12</OrgnlMsgNmId>
    <OrgnlCredTm>2012-09-28T14:07:00</OrgnlCredTm>
    <OrgnlNbOfTx>3</OrgnlNbOfTx>
    <OrgnlCtrlSum>11500000</OrgnlCtrlSum>
    <GrpSts>ACCP</GrpSts>
</OrgnlGrpInfAndSts>
</CstmrPmtStsRpt>

## 7.3 CustomerPaymentStatusReport pain.002.001.14 - 2

### Description

AAA AUS29 received an FIToFIPaymentStatusReport from its correspondent, ABABUS23, containing reject information about a previously sent FIToFICustomerDirectDebit. As AAAAUS29 has not yet credited the account of the original initiating party (Virgay) of the direct debit, AAAAUS29 in its turn informs Virgay about the rejection of the CustomerDirectDebitInitiation sent on 28 June 2012.

### Business Description

CustomerPaymentStatusReport from AAAAUS29 to Virgay:



<table>
  <thead>
    <tr>
      <th>Element</th>
      <th>&lt;XMLTag&gt;</th>
      <th>Content</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Group Header</td>
      <td>&lt;GrpHdr&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>MessageIdentification</td>
      <td>&lt;MsgId&gt;</td>
      <td>AAAAUS29_5678c</td>
    </tr>
    <tr>
      <td>CreationDateTime</td>
      <td>&lt;CredTm&gt;</td>
      <td>2012-06-29T15:49:00</td>
    </tr>
    <tr>
      <td>InitiatingParty</td>
      <td>&lt;InitgPty&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>Name</td>
      <td>&lt;Nm&gt;</td>
      <td>Virgay</td>
    </tr>
    <tr>
      <td>PostalAddress</td>
      <td>&lt;PstlAdr&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>StreetName</td>
      <td>&lt;StrtNm&gt;</td>
      <td>Virginia Lane</td>
    </tr>
    <tr>
      <td>BuildingNumber</td>
      <td>&lt;BldgNb&gt;</td>
      <td>36</td>
    </tr>
    <tr>
      <td>PostCode</td>
      <td>&lt;PstCd&gt;</td>
      <td>NJ 07311</td>
    </tr>
    <tr>
      <td>TownName</td>
      <td>&lt;TwnNm&gt;</td>
      <td>Jersey City</td>
    </tr>
    <tr>
      <td>Country</td>
      <td>&lt;Ctry&gt;</td>
      <td>US</td>
    </tr>
    <tr>
      <td>CreditorAgent</td>
      <td>&lt;CdtAgnt&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>FinancialInstitutionIdentification</td>
      <td>&lt;FinInstlId&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>BICFI</td>
      <td>&lt;BICFI&gt;</td>
      <td>AAAAUS29</td>
    </tr>
    <tr>
      <td>OriginalGroupInformationAndStat us</td>
      <td>&lt;OrgnlGrpInfAndSts&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>OriginalMessageIdentification</td>
      <td>&lt;OrgnlMsgId&gt;</td>
      <td>CAVAY1234</td>
    </tr>
    <tr>
      <td>OriginalMessageName Identification</td>
      <td>&lt;OrgnlMsgNmId&gt;</td>
      <td>pain.008.001.11</td>
    </tr>
    <tr>
      <td>OriginalCreationDateTime</td>
      <td>&lt;OrgnlCredTm&gt;</td>
      <td>2012-06-28T14:25:00</td>
    </tr>
    <tr>
      <td>OriginalPaymentInformationAndSt</td>
      <td>&lt;OrgnlPmtInfSts&gt;</td>
      <td></td>
    </tr>
  </tbody>
</table>

---

<!-- Page 51 -->

| Element | <XMLTag> | Content |
| :--- | :--- | :--- |
| atus | | |
| OriginalPaymentInformationIdentification | <OrgnlPmtInfId> | JKL_774 |
| TransactionInformationAndStatus | <TxInfAndSts> | |
| StatusID | <StsId> | RJT2012_657B |
| OriginalEndToEndIdentification | <OrgnlEndToEndId> | VA100327/0123 |
| TransactionStatus | <TxSts> | RJCT |
| StatusReasonInformation | <StsRsnInf> | |
| Originator | <Orgtr> | |
| OrganisationIdentification | <OrgId> | |
| AnyBIC | <AnyBIC> | ABABUS23 |
| Reason | <StsRsn> | |
| Code | <Cd> | AM05 |
| OriginalTransactionReference | <OrgnlTxRef> | |
| Amount | <Amt> | |
| InstructedAmount | <InstdAmt> | USD 1025 |
| RequestedCollectionDate | <ReqdCollnDt> | 2012-07-02 |
| MandateRelatedInformation | <MndtRltdInf> | |
| DirectDebitMandate | <DrctDbtMndt> | |
| MandateIdentification | <MndtId> | VIRGAY123 |
| Debtor | <Dbtr> | |
| Name | <Name> | Jones |
| PostalAddress | <PstlAdr> | |
| StreetName | <StrtNm> | Hudson Street |
| BuildingNumber | <BldgNb> | 19 |
| PostCode | <PstCd> | NJ 07302 |
| TownName | <TwnNm> | Jersey City |
| Country | <Ctry> | US |
| Creditor | <Cdtr> | |
| Name | <Name> | Virgay |
| PostalAddress | <PstlAdr> | |
| StreetName | <StrtNm> | Virginia Lane |
| BuildingNumber | <BldgNb> | 36 |
| PostCode | <PstCd> | NJ 07311 |
| TownName | <TwnNm> | Jersey City |
| Country | <Ctry> | US |

**Message Instance**
<CstmrPmtStsRpt>
  <GrpHdr>
    <MsgId>AAAAUS29_5678</MsgId>

---

<!-- Page 52 -->

```
<CredtTm>2012-06-29T15:49:00</CredtTm>
<InitPty>
  <Nm>Virgay</Nm>
  <PstlAdr>
    <StrtNm>Virginia Lane</StrtNm>
    <BldgNb>36</BldgNb>
    <PstCd>NJ 07311</PstCd>
    <TwnNm>Jersey City</TwnNm>
    <Ctry>US</Ctry>
  </PstlAdr>
</InitPty>
</CdtrAg>
<FinInstnId>
  <BICFI>AAAAUS29</BICFI>
</FinInstnId>
</CdtrAg>
</GrpHdr>
<OrgnlGrpInfAndSts>
  <OrgnlMsgId>CAVAY1234</OrgnlMsgId>
  <OrgnlMsgNmId>pain.008.001.11</OrgnlMsgNmId>
  <OrgnlCredTm>2012-06-28T14:25:00</OrgnlCredTm>
</OrgnlGrpInfAndSts>
<OrgnlPmtInfAndSts>
  <OrgnlPmtInfId>JKL_774</OrgnlPmtInfId>
  <TxInfAndSts>
    <StsId>RIT2012 6578</StsId>
    <OrgnlEndToEndId>VA100327/0123</OrgnlEndToEndId>
    <TxSts>RJCT</TxSts>
    <StsRsnInf>
      <Orgtr>
        <Id>
          <OrgId>
            <AnyBIC>ABABUS23</AnyBIC>
          </OrgId>
        </Id>
      </Orgtr>
      <Rsn>
        <Cd>AM05</Cd>
      </Rsn>
```

---

<!-- Page 53 -->

```
</StsRsnInf>
<OrgnlTxRef>
    <Amt>
        <InstdAmt Ccy="USD">1025</InstdAmt>
    </Amt>
    <ReqdColltnDt>2012-07-02</ReqdColltnDt>
    <MndtRltdInf>
        <DrctDbtMndt>
            <MndtId>VIRGAY123</MndtId>
        </DrctDbtMndt>
    </MndtRltdInf>
</Dbtr>
    <Pty>
        <Nm>Jones</Nm>
        <PstlAdr>
            <StrtNm>Hudson Street</StrtNm>
            <BldgNb>19</BldgNb>
            <PstCd>NJ 07302</PstCd>
            <TwnNm>Jersey City</TwnNm>
            <Ctry>US</Ctry>
        </PstlAdr>
    </Pty>
</Dbtr>
<Cdtr>
    <Pty>
        <Nm>Virgay</Nm>
        <PstlAdr>
            <StrtNm>Virginia Lane</StrtNm>
            <BldgNb>36</BldgNb>
            <PstCd>NJ 07311</PstCd>
            <TwnNm>Jersey City</TwnNm>
            <Ctry>US</Ctry>
        </PstlAdr>
    </Pty>
</Cdtr>
</OrgnlTxRef>
</TxInfAndSts>
</OrgnlPmtInfAndSts>
</CstmrPmtStsRpt>
```

---

<!-- Page 54 -->

## 7.4 CustomerPaymentReversal pain.007.001.12

### Description

On 17 June 2012, date of the collection from debtor Schneider, Ritcom electricity company realises that the direct debit instruction sent on 9 June 2012 was a duplicated instruction. As settlement of the direct debit already took place, Ritcom electricity company initiates a CustomerPaymentReversal message and sends it to its account servicer AAAADEFF. Any potential charges relating to this reversal payment, paid by Schneider, will be deducted from the next invoice.

### Business Data

CustomerPaymentReversal from Ritcom to AAAADEFF :



<table><tr><td>Element</td><td>&lt;XMLTag&gt;</td><td>Content</td></tr><tr><td>Group Header</td><td>&lt;GrpHd&gt;</td><td></td></tr><tr><td>MessageIdentification</td><td>&lt;MsgId&gt;</td><td>RIT-REV-20120617-456f</td></tr><tr><td>CreationDateTime</td><td>&lt;CreDtTm&gt;</td><td>2012-06-17T15:38:00</td></tr><tr><td>NumberOfTransactions</td><td>&lt;NbOfTxs&gt;</td><td>1</td></tr><tr><td>InitiatingParty</td><td>&lt;InitgPty&gt;</td><td></td></tr><tr><td>Name</td><td>&lt;Nm&gt;</td><td>Ritcom</td></tr><tr><td>PostalAddress</td><td>&lt;PstlAdr&gt;</td><td></td></tr><tr><td>StreetName</td><td>&lt;StrNm&gt;</td><td>Schueman Strasse</td></tr><tr><td>BuildingNumber</td><td>&lt;BldgNb&gt;</td><td>18</td></tr><tr><td>PostCode</td><td>&lt;PstCd&gt;</td><td>60017</td></tr><tr><td>TownName</td><td>&lt;TwnNm&gt;</td><td>Frankfurt am Main</td></tr><tr><td>Country</td><td>&lt;Ctry&gt;</td><td>DE</td></tr><tr><td>DebtorAgent</td><td>&lt;DbtrAgt&gt;</td><td></td></tr><tr><td>FinancialInstitutionIdentification</td><td>&lt;FinInstlId&gt;</td><td></td></tr><tr><td>BICFI</td><td>&lt;BICFI&gt;</td><td>BBBBBDE33</td></tr><tr><td>CreditorAgent</td><td>&lt;CdtrAgt&gt;</td><td></td></tr><tr><td>FinancialInstitutionIdentification</td><td>&lt;FinInstlId&gt;</td><td></td></tr><tr><td>BICFI</td><td>&lt;BICFI&gt;</td><td>AAAAD EFF</td></tr><tr><td>OriginalGroupInformation</td><td>&lt;OrgnlGrpInf&gt;</td><td></td></tr><tr><td>OriginalMessageIdentification</td><td>&lt;OrgnlMsgId&gt;</td><td>RITCOM1234</td></tr><tr><td>OriginalMessageNameIdentification</td><td>&lt;OrgnlMsgNmId&gt;</td><td>pain.008.001.11</td></tr><tr><td>OriginalCreationDateTime</td><td>&lt;OrgnlCreDtTm&gt;</td><td>2012-06-09T09:18:00</td></tr><tr><td>OriginalPaymentInformationAndReversal</td><td>&lt;OrgnlPmtInfAndRvsl&gt;</td><td></td></tr><tr><td>OriginalPaymentInformationIdentification</td><td>&lt;OrgnlPmtInfId&gt;</td><td>RIT/0053</td></tr><tr><td>TransactionInformation</td><td>&lt;TxInf&gt;</td><td></td></tr><tr><td>ReversalIdentification</td><td>&lt;RvslId&gt;</td><td>RIT5467</td></tr><tr><td>OriginalEndToEndIdentification</td><td>&lt;OrgnlEndToEnd&gt;</td><td>RIT/012010-2562C26</td></tr><tr><td>OriginalInstructedAmount</td><td>&lt;OrgnlInstdAmt&gt;</td><td>EUR 286</td></tr><tr><td>ReversedInstructedAmount</td><td>&lt;RvslInstdAmt&gt;</td><td>EUR 286</td></tr></table>

---

<!-- Page 55 -->

| Element | <XMLTag> | Content |
| :--- | :--- | :--- |
| ReversalReasonInformation | <RvslRsnInf> | |
| Originator | <Orgtr> | |
| Name | <Nm> | Ritcom |
| PostalAddress | <PstlAdr> | |
| StreetName | <StrtNm> | Schueman Strasse |
| BuildingNumber | <BldgNb> | 18 |
| PostCode | <PstCd> | 60017 |
| TownName | <TwnNm> | Frankfurt am Main |
| Country | <Ctry> | DE |
| Reason | <Rsn> | |
| Code | <Cd> | AM05 |
| OriginalTransactionReference | <OrgnlTxRef> | |
| RequestedCollectionDate | <ReqdCollnDt> | 2012-06-16 |
| MandateRelatedInformation | <MndtRltdInf> | |
| DirectDebitMandate | <DrctDbtMndt> | |
| MandateIdentification | <MndtId> | RIT04/av002 |
| Debtor | <Dbtr> | |
| Name | <Nm> | Schneider |
| PostalAddress | <PstlAdr> | |
| StreetName | <StrtNm> | Kuertman Strasse |
| BuildingNumber | <BldgNb> | 45 |
| PostCode | <PstCd> | 50475 |
| TownName | <TwnNm> | Koin |
| Country | <Ctry> | DE |
| DebtorAccount | <DbtrAcct> | |
| Identification | <Id> | |
| IBAN | <IBAN> | DE89370400440332014000 |
| Creditor | <Cdtr> | |
| Name | <Nm> | Ritcom |
| PostalAddress | <PstlAdr> | |
| StreetName | <StrtNm> | Schueman Strasse |
| BuildingNumber | <BldgNb> | 18 |
| PostCode | <PstCd> | 60017 |
| TownName | <TwnNm> | Frankfurt am Main |
| Country | <Ctry> | DE |

**Message Instance**
<CstmrPmtRvsl>
   <GrpHdr>
      <MsgId>RIT-REV-20120617-456f</MsgId>

---

<!-- Page 56 -->

```xml
<CreDtTm>2012-06-17T15:38:00</CreDtTm>
<NbOfTxs>1</NbOfTxs>
<InitPty>
    <Nm>Ritcom</Nm>
    <PstlAdr>
        <StrtNm>Schueman Strasse</StrtNm>
        <BldgNb>18</BldgNb>
        <PstCd>60017</PstCd>
        <TwnNm>Frankfurt am Main</TwnNm>
        <Ctry>DE</Ctry>
    </PstlAdr>
</InitPty>
<DbtrAgt>
    <FinInstnId>
        <BICFI>BBBDEDE33</BICFI>
    </FinInstnId>
</DbtrAgt>
<CdtrAgt>
    <FinInstnId>
        <BICFI>AAAADEFF</BICFI>
    </FinInstnId>
</CdtrAgt>
</GrpHdr>
<OrgnlGrpInf>
    <OrgnlMsgId>RITCOM1234</OrgnlMsgId>
    <OrgnlMsgNmId>pain.008.001.11</OrgnlMsgNmId>
    <OrgnlCreDtTm>2012-06-09T09:18:00</OrgnlCreDtTm>
</OrgnlGrpInf>
<OrgnlPmtInfAndRvsl>
    <OrgnlPmtInfId>RIT/0053</OrgnlPmtInfId>
    <TxInf>
        <RvslId>RIT5467</RvslId>
        <OrgnlEndToEndId>RIT/012010-2562C26</OrgnlEndToEndId>
        <OrgnlInstdAmt Ccy="EUR">286</OrgnlInstdAmt>
        <RvslInstdAmt Ccy="EUR">286</RvslInstdAmt>
        <RvslRsnInf>
            <Orgtr>
                <Nm>Ritcom</Nm>
                <PstlAdr>
```

---

<!-- Page 57 -->

```
                    <StrtNm>Schueman Strasse</StrtNm>
                    <BldgNb>18</BldgNb>
                    <PstCd>60017</PstCd>
                    <TwnNm>Frankfurt am Main</TwnNm>
                    <Ctry>DE</Ctry>
                </PstlAdr>
            </Orgtr>
            <Rsn>
                <Cd>AM05</Cd>
            </Rsn>
        </RvslRsnInf>
        <OrgnTxRef>
            <ReqdColltnDt>2010-06-16</ReqdColltnDt>
            <MndtRltdInf>
                <DrctDbtMndt>
                    <MndtId>RIT04/av002</MndtId>
                </DrctDbtMndt>
            </MndtRltdInf>
            <Dbtr>
                <Pty>
                    <Nm>Schneider</Nm>
                    <PstlAdr>
                        <StrtNm>Kuertman Strasse</StrtNm>
                        <BldgNb>45</BldgNb>
                        <PstCd>50475</PstCd>
                        <TwnNm>Koeln</TwnNm>
                        <Ctry>DE</Ctry>
                    </PstlAdr>
                </Pty>
            </Dbtr>
            <DbtrAcct>
                <Id>
                    <IBAN>DE89370400440332014000</IBAN>
                </Id>
            </DbtrAcct>
        </OrgnTxRef>
        <Cdtr>
            <Pty>
                <Nm>Ritcom</Nm>
                <PstlAdr>
```

---

<!-- Page 58 -->

```xml
<StrtNm>Schueman Strasse</StrtNm>
<BldgNb>18</BldgNb>
<PstCd>60017</PstCd>
<TwnNm>Frankfurt am Main</TwnNm>
<Ctry>DE</Ctry>
</PstlAdr>
</Pty>
</Cdtr>
</OrgnlTxRef>
</TxInf>
</OrgnlPmtInfAndRvsl>
</CstmrPmtRvsl>
```

## 7.5 CustomerDirectDebitInitiation pain.008.001.11

**Narrative**

On 2 June 2012, Virgay insurance company sends a CustomerDirectDebitInitiation message to its account servicer, AAAAUS29. AAAAUS29 offers a special service to Virgay, under agreement VERPA-1.

The direct debit initiation message contains two collection instructions from two different debtors.

The first direct debit instruction is for 1025 USD to be collected from account 123456, owned by debtor Jones and serviced by agent BBBBUS39. The mandate reference is VIRGAY123 and was signed by Jones on 13 July 2008. The last collection is due to take place on 13 July 2015. The payment is for a yearly life insurance fee.

The second direct debit instruction is for 985 USD to be collected from account 789101, owned by debtor Lee and serviced by agent CCCCUS27. This is a one-off direct debit which was notified to Lee on 8 June 2012, with reference VIRGAY2439/2012. The payment is for a car insurance premium.

The requested collection date for both collections is 13 July 2012 and charges related to the handling of the instruction will be shared between Virgay insurance company and the debtors.

**Business Data**

CustomerDirectDebitInitiation from Virgay to AAAAUS29:

| Element | <XMLTag> | Content |
| :--- | :--- | :--- |
| Group Header | <GrpHdr> | |
| MessageIdentification | <MsgId> | CAVAY1234 |
| CreationDateTime | <CreDtTm> | 2012-06-02T14:25:00 |
| NumberOfTransactions | <NbOfTxs> | 2 |
| ControlSum | <CtrlSum> | 2010 |
| InitiatingParty | <InitgPty> | |
| Name | <Nm> | Virgay |
| PostalAddress | <PstlAdr> | |
| StreetName | <StrtNm> | Virginia Lane |
| BuildingNumber | <BldgNb> | 36 |

---

<!-- Page 59 -->

| Element | <XMLTag> | Content |
|---|---|---|
| PostCode | <PstCd> | NJ 07311 |
| TownName | <TwnNm> | Jersey City |
| Country | <Ctry> | US |
| ContactDetails | <CntctDtls> |  |
| Name | <Nm> | J. Thompson |
| EmailAddress | <EmailAdr> | Thompson@virgay.com |
| PaymentInformation | <PmtInf> |  |
| PaymentInformationIdentification | <PmtInfId> | CAVAY/88683 |
| PaymentMethod | <PmtMtd> | DD |
| BatchBooking | <BtchBookg> | FALSE |
| RequestedCollectionDate | <ReqColltnDt> | 2012-07-13 |
| Creditor | <Cdr> |  |
| Name | <Nm> | Virgay |
| PostalAddress | <PstlAdr> |  |
| StreetName | <StrtNm> | Virginia Lane |
| BuildingNumber | <BldgNb> | 36 |
| PostCode | <PstCd> | NJ 07311 |
| TownName | <TwnNm> | Jersey City |
| Country | <Ctry> | US |
| CreditorAccount | <CdrAcct> |  |
| Identification | <Id> |  |
| Other | <Othr> |  |
| Identification | <Id> | 789123 |
| CreditorAgent | <CdrAgnt> |  |
| FinancialInstitutionIdentification | <FinInstlId> |  |
| BICFI | <BICFI> | AAAAUS29 |
| DirectDebitTransactionInformation | <DrctDbtTxInf> |  |
| PaymentIdentification | <PmtId> |  |
| EndToEndIdentification | <EndToEndId> | VA060327/0123 |
| PaymentTypeInformation | <PmtTpInf> |  |
| InstructionPriority | <InstrPrty> | NORM |
| ServiceLevel | <SvcLvl> |  |
| Proprietary | <Prtry> | VERPA-1 |
| SequenceType | <SeqTp> | RCUR |
| InstructedAmount | <InstdAmt> | USD 1025 |
| ChargeBearer | <ChgBr> | SHAR |
| DirectDebitTransaction | <DrctDbtTx> |  |
| MandateRelatedInformation | <MndtRltdInf> |  |
| MandateIdentification | <MndtId> | VIRGAY123 |
| DateOfSignature | <DtOfSgntr> | 2008-07-13 |

---

<!-- Page 60 -->

| Element | <XMLTag> | Content |
| :--- | :--- | :--- |
| FinalCollectionDate | <FinCollnDt> | 2015-07-13 |
| Frequency | <Frcq><Tp> | YEAR |
| DebtorAgent | <DbtrAg> | |
| FinancialInstitutionIdentification | <FinInstnId> | |
| BICFI | <BICFI> | BBBBUS39 |
| Debtor | <Dbtr> | |
| Name | <Nm> | Jones |
| PostalAddress | <PstlAdr> | |
| StreetName | <StrtNm> | Hudson Street |
| BuildingNumber | <BldgNb> | 19 |
| PostCode | <PstCd> | NJ 07302 |
| TownName | <TwnNm> | Jersey City |
| Country | <Ctry> | US |
| DebtorAccount | <DbtrAcct> | |
| Identification | <Id> | |
| Other | <Othr> | |
| Identification | <Id> | 123456 |
| Purpose | <Purp> | |
| Code | <Cd> | LIFI |
| RemittanceInformation | <Rmtnf> | |
| Unstructured | <Ustrd> | LIFE INSURANCE PAYMENT/ JULY 2012 |
| DirectDebitTransactionInformation | <DrctDbtTxInf> | |
| PaymentIdentification | <PmtId> | |
| EndToEndIdentification | <EndToEndId> | AY090327456 |
| PaymentTypeInformation | <PmtTpInf> | |
| InstructionPriority | <InstrPrty> | NORM |
| ServiceLevel | <SvcLvl> | |
| Proprietary | <Prpry> | VERPA-1 |
| SequenceType | <SeqTp> | OFF |
| InstructedAmount | <InstdAmt> | USD 985 |
| ChargeBearer | <ChgBr> | SHAR |
| DirectDebitTransaction | <DrctDbtTx> | |
| PreNotificationIdentification | <PreNtfctnId> | VIRGAY2435/2012 |
| PreNotificationDate | <PreNtfctnDt> | 2012-06-08 |
| DebtorAgent | <DbtrAg> | |
| FinancialInstitutionIdentification | <FinInstnId> | |
| BICFI | <BICFI> | CCCCUS27 |
| Debtor | <Dbtr> | |
| Name | <Nm> | Lee |

---

<!-- Page 61 -->

| Element | <XMLTag> | Content |
| :--- | :--- | :--- |
| PostalAddress | <PstlAdr> | |
| StreetName | <StrtNm> | Cross Road |
| BuildingNumber | <BldgNb> | 45 |
| PostCode | <PstCd> | NJ 07399 |
| TownName | <TwnNm> | Jersey City |
| Country | <Ctry> | US |
| DebtorAccount | <DbtrAcct> | |
| Identification | <Id> | |
| Other | <Othr> | |
| Identification | <Id> | 789101 |
| RemittanceInformation | <RmtInf> | |
| Unstructured | <Ustrd> | CAR INSURANCE PREMIUM |

**Message Instance**

```
<CstmrDrctDbtInitn>
   <GrpHdr>
      <MsgId>CAVAY1234</MsgId>
      <CreDtTm>2012-06-02T14:25:00</CreDtTm>
      <NbOfTxs>2</NbOfTxs>
      <CtrlSum>2010</CtrlSum>
      <InitgPty>
         <Nm>Virgay</Nm>
         <PstlAdr>
            <StrtNm>Virginia Lane</StrtNm>
            <BldgNb>36</BldgNb>
            <PstCd>NJ 07311</PstCd>
            <TwnNm>Jersey City</TwnNm>
            <Ctry>US</Ctry>
         </PstlAdr>
      </InitgPty>
      <CtctDtls>
         <Nm>J. Thompson</Nm>
         <EmailAdr>Thompson@virgay.com</EmailAdr>
      </CtctDtls>
   </GrpHdr>
   <PmtInf>
      <PmtInfId>CAVAY/88683</PmtInfId>
```

---

<!-- Page 62 -->

```xml
<PmtMtd>DD</PmtMtd>
<BtchBookg>false</BtchBookg>
<ReqdColltnDt>2012-07-13</ReqdColltnDt>
<Cdtr>
    <Nm>Virgay</Nm>
    <PstlAdr>
        <StrtNm>Virginia Lane</StrtNm>
        <BldgNb>36</BldgNb>
        <PstCd>NJ 07311</PstCd>
        <TwnNm>Jersey City</TwnNm>
        <Ctry>US</Ctry>
    </PstlAdr>
</Cdtr>
<CdtrAcct>
    <Id>
        <Othr>
            <Id>789123</Id>
        </Othr>
    </Id>
</CdtrAcct>
<CdtrAgt>
    <FinInstnId>
        <BICFI>AAAAUS29</BICFI>
    </FinInstnId>
</CdtrAgt>
<DrcctDbtTxInf>
    <PmtId>
        <EndToEndId>VA060327/0123</EndToEndId>
    </PmtId>
    <PmtTpInf>
        <InstrPrty>NORM</InstrPrty>
        <SvcLvl>
            <Prtty>VERPA-1</Prtty>
        </SvcLvl>
        <SeqTp>RCUR</SeqTp>
    </PmtTpInf>
    <InstdAmt Ccy="USD">1025</InstdAmt>
    <ChrgBr>SHAR</ChrgBr>
    <DrcctDbtTx>
```

---

<!-- Page 63 -->

```
<MndtRltdInf>
    <MndtId>VIRGAY123</MndtId>
    <DtOfSgntr>2008-07-13</DtOfSgntr>
    <FnlColltnDt>2015-07-13</FnlColltnDt>
    <Frcy><Tp>YEAR</Tp></Frcy>
</MndtRltdInf>
</DrctDbtTx>
<DbtrAgt>
    <FinInstnId>
        <BICFI>BBBBUS539</BICFI>
    </FinInstnId>
</DbtrAgt>
<Dbtr>
    <Nm>Jones</Nm>
    <PstlAdr>
        <StrtNm>Hudson Street</StrtNm>
        <BldgNb>19</BldgNb>
        <PstCd>NJ 07302</PstCd>
        <TwnNm>Jersey City</TwnNm>
        <Ctry>US</Ctry>
    </PstlAdr>
</Dbtr>
<DbtrAcct>
    <Id>
        <Othr>
            <Id>123456</Id>
        </Othr>
    </Id>
</DbtrAcct>
<Purp>
    <Cd>LIF</Cd>
</Purp>
<RmtnInf>
    <Ustrd>LIFE INSURANCE PAYMENT/ JULY 2012</Ustrd>
</RmtnInf>
</DrctDbtTxInf>
<DrctDbtXInf>
    <PmtId>
        <EndToEndId>AY090327/456</EndToEndId>
```

---

<!-- Page 64 -->

```
</PmtId>
<PmtTpInf>
  <InstrPrty>NORM</InstrPrty>
  <SvcLvl>
    <Prtry>VERPA-1</Prtry>
  </SvcLvl>
  <SeqTp>OOFF</SeqTp>
</PmtTpInf>
<InstdAmt Ccy="USD">985</InstdAmt>
<ChrgBr>SHAR</ChrgBr>
<DrtctDbtTx>
  <PrvNfcctnlId>VIRGAY2435/2012</PrvNfcctnlId>
  <PrvNfcctnlDt>2012-06-08</PrvNfcctnlDt>
</DrtctDbtTx>
<DbtrAgt>
  <FinInstnId>
    <BICFI>CCCCUS27</BICFI>
  </FinInstnId>
</DbtrAgt>
<Dbtr>
  <Nm>Lee</Nm>
  <PstlAdr>
    <StrtNm>Cross Road</StrtNm>
    <BldgNb>45</BldgNb>
    <PstCd>NJ07399</PstCd>
    <TwnNm>Jersey City</TwnNm>
    <Ctry>US</Ctry>
  </PstlAdr>
</Dbtr>
<DbtrAcct>
  <Id>
    <Othr>
      <Id>789101</Id>
    </Othr>
  </Id>
</DbtrAcct>
<RmtnInf>
  <Ustrd>CAR INSURANCE PREMIUM</Ustrd>
</RmtnInf>
```

---

<!-- Page 65 -->

</DrctDbtTxInf>
    </PmtInf>
  </CstmrDrctDbtInitn>

---

<!-- Page 66 -->

Message Definition Report - Part 1                                                                 Revision Record

# 8 Revision Record

| Revision | Date | Author | Description | Sections affected |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 | December 2023 | SWIFT | Draft version for SEG review | All |
| 2.0 | March 2024 | ISO 20022 RA | Approved version | All |

**Disclaimer:**

Although the Registration Authority has used all reasonable efforts to ensure accuracy of the contents of the iso20022.org website and the information published thereon, the Registration Authority assumes no liability whatsoever for any inadvertent errors or omissions that may appear thereon. Moreover, the information is provided on an "as is" basis. The Registration Authority disclaims all warranties and conditions, either express or implied, including but not limited to implied warranties of merchantability, title, non-infringement and fitness for a particular purpose.

The Registration Authority shall not be liable for any direct, indirect, special or consequential damages arising out of the use of the information published on the iso20022.org website, even if the Registration Authority has been advised of the possibility of such damages.

**Intellectual Property Rights:**

The ISO 20022 MessageDefinitions described in this document were contributed by SWIFT, IFX, OAGI & TWIST as part of ISTH. The ISO 20022 IPR policy is available at www.ISO20022.org > About ISO 20022 > Intellectual Property Rights.