<!-- Page 1 -->

ISO 2022

## Payments Clearing and Settlement - Maintenance 2024 - 2025

# Message Definition Report Part 1

## Approved by the Payments SEG on 4 February 2025

This document provides information about the use of the messages for Payments Clearing and Settlement and includes, for example, business scenarios and messages flows.

February 2025

---

<!-- Page 2 -->

Message Definition Report Part 1                                                                                   Table of Contents

# Table of Contents

| | | |
|---|---|---|
| | Table of Contents.................................................................................................................... | 2 |
| **1** | **Introduction**.................................................................................................................... | **5** |
| 1.1 | Terms and Definitions.................................................................................................................... | 5 |
| 1.2 | Abbreviations and Acronyms.................................................................................................................... | 5 |
| 1.3 | Document Scope and Objectives.................................................................................................................... | 5 |
| 1.4 | References.................................................................................................................... | 6 |
| **2** | **Scope and Functionality**.................................................................................................................... | **7** |
| 2.1 | Background.................................................................................................................... | 7 |
| 2.2 | Scope.................................................................................................................... | 7 |
| 2.3 | Groups of MessageDefinitions and Functionality.................................................................................................................... | 7 |
| **3** | **BusinessRoles and Participants**.................................................................................................................... | **9** |
| 3.1 | Participants and BusinessRoles Definitions.................................................................................................................... | 9 |
| 3.2 | BusinessRoles and Participants Table.................................................................................................................... | 10 |
| **4** | **BusinessProcess Description**.................................................................................................................... | **11** |
| 4.1 | Credit Transfer.................................................................................................................... | 11 |
| 4.2 | Direct Debit.................................................................................................................... | 14 |
| **5** | **Description of BusinessActivities**.................................................................................................................... | **17** |
| 5.1 | Credit Transfer.................................................................................................................... | 17 |
| 5.2 | Direct Debit.................................................................................................................... | 19 |
| **6** | **BusinessTransactions**.................................................................................................................... | **24** |
| 6.1 | Credit Transfer.................................................................................................................... | 24 |
| 6.2 | Direct Debit.................................................................................................................... | 47 |
| **7** | **Business Examples**.................................................................................................................... | **63** |
| 7.1 | FIToFIPaymentStatusReport_pacs.002.001.15.................................................................................................................... | 63 |
| 7.2 | FIToFICustomerDirectDebit_pacs.003.001.11.................................................................................................................... | 66 |
| 7.3 | PaymentReturn_pacs.004.001.14 - 1.................................................................................................................... | 71 |
| 7.4 | PaymentReturn_pacs.004.001.14 - 2.................................................................................................................... | 77 |
| 7.5 | FIToFIPaymentReversal_pacs.007.001.13.................................................................................................................... | 85 |
| 7.6 | FIToFICustomerCreditTransfer_pacs.008.001.13 - 1.................................................................................................................... | 89 |
| 7.7 | FIToFICustomerCreditTransfer_pacs.008.001.13 - 2.................................................................................................................... | 113 |
| 7.8 | FinancialInstitutionCreditTransfer_pacs.009.001.12 - 1.................................................................................................................... | 123 |
| 7.9 | FinancialInstitutionCreditTransfer_pacs.009.001.12 - 2.................................................................................................................... | 130 |
| 7.10 | FinancialInstitutionDirectDebit_pacs.010.001.06.................................................................................................................... | 140 |
| 7.11 | FIToFIPaymentStatusRequest - pacs.028.001.06.................................................................................................................... | 143 |
| **8** | **Revision Record**.................................................................................................................... | **149** |

---

<!-- Page 3 -->

Message Definition Report Part 1                                                                                          Table of Contents

## Preliminary Note

The Message Definition Report (MDR) is made of three parts:

**MDR Part 1**

This describes the contextual background required to understand the functionality of the proposed message set. Part 1 is produced by the submitting organisation that developed or maintained the message set in line with an MDR Part 1 template provided by the ISO 20022 Registration Authority (RA) on www.iso20022.org.

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
| *BusinessRole* | Functional role played by a business actor in a particular *BusinessProcess* or *BusinessTransaction*. |
| *Participant* | Involvement of a *BusinessRole* in a *BusinessTransaction*. |
| *BusinessProcess* | Definition of the business activities undertaken by *BusinessRoles* within a *BusinessArea* whereby each *BusinessProcess* fulfils one type of business activity and whereby a *BusinessProcess* may include and extend other *BusinessProcesses*. |
| *BusinessTransaction* | Particular solution that meets the communication requirements and the interaction requirements of a particular *BusinessProcess* and *BusinessArea*. |
| *MessageDefinition* | Formal description of the structure of a message instance. |

## 1.2 Abbreviations and Acronyms

The following is a list of abbreviations and acronyms used in the document.

| Abbreviation/Acronyms | Definition |
|---|---|
| MDR | Message Definition Report |
| MCR | Maintenance change request |
| SEG | Standards Evaluation Group |
| FI | Financial Institution |
| XML | eXtensible Mark-up Language |
| IBAN | International Bank Account Number |
| BIC | Business Identifier Code |
| ACH | Automated Clearing House |
| DD | Direct Debit |
| RTGS | Real time gross settlement |
| MRI | Mandate Related Information |
| Ect. | Etcetera |

## 1.3 Document Scope and Objectives

This document is the first part of the Payments Clearing and Settlement Message Definition Report (MDR) that describes the BusinessTransactions and underlying message set. For the sake of completeness, the document may also describe BusinessActivities that are not in the scope of the business processes covered in this document.

This document describes the following:

---

<!-- Page 5 -->

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



<table>
  <tr>
    <th>Document</th>
    <th>Version</th>
    <th>Date</th>
    <th>Author</th>
  </tr>
  <tr>
    <td>ISO 20022 Business Justification #6 – (single) credit transfers</td>
    <td>2006</td>
    <td>09-09-2005</td>
    <td>SWIFT</td>
  </tr>
  <tr>
    <td>ISO 20022 Business Justification #5 - Direct Debits</td>
    <td>2006</td>
    <td>08-09-2006</td>
    <td>SWIFT</td>
  </tr>
  <tr>
    <td>ISO 20022 Business Justification #8 - (bulk) credit transfers</td>
    <td>2006</td>
    <td>08-09-2006</td>
    <td>SWIFT</td>
  </tr>
  <tr>
    <td>ISO 20022 Business Justification #85 - Financial Institution Direct Debit</td>
    <td>2014</td>
    <td>31-07-2014</td>
    <td>SWIFT</td>
  </tr>
  <tr>
    <td>ISO 20022 Business Justification #110 - Payment Status Request</td>
    <td>2016</td>
    <td>11-07-2016</td>
    <td>SWIFT</td>
  </tr>
  <tr>
    <td>ISO 20022 Maintenance Change Request (MCR #170) document (Payments Maintenance 2020/2021)</td>
    <td>2020</td>
    <td>31-08-2020</td>
    <td>SWIFT</td>
  </tr>
  <tr>
    <td>ISO 20022 Maintenance Change Request (MCR #208) document (Payments Maintenance 2022/2023)</td>
    <td>2022</td>
    <td>31-08-2022</td>
    <td>SWIFT</td>
  </tr>
  <tr>
    <td>ISO 20022 Maintenance Change Request (MCR #234) document (Payments Maintenance 2023/2024)</td>
    <td>2023</td>
    <td>31-08-2023</td>
    <td>SWIFT</td>
  </tr>
  <tr>
    <td>ISO 20022 Maintenance Change Request (MCR #252) document (Payments Maintenance 2024/2025)</td>
    <td>2024</td>
    <td>31-08-2024</td>
    <td>Swift</td>
  </tr>
</table>

---

<!-- Page 6 -->

# 2 Scope and Functionality

## 2.1 Background

This Message Definition Report covers a set of eight MessageDefinitions developed by SWIFT and approved by the ISO 20022 Payments Standards Evaluation Group (SEG) in February 2025.

These messages are specifically designed to support the clearing and settlement of credit transfers, direct debits and reversals directly between banks or across an automated clearing house (ACH) and real time gross settlement systems (RTGS).

In 2015, the FinancialInstitutionDirectDebit message was added as a result of reverse engineering the existing SWIFT FIN MT 204 Financial Markets Direct Debit Message in order to bridge the gap detected at the occasion of the migration of several market infrastructures worldwide from their SWIFT FIN portfolio of messages (MT 103, MT 103+, MT 202, MT 204, MT 900, MT 910) to ISO 20022.

In 2016, the FIToFIPaymentStatusRequest message was added to accommodate the need, initially identified for real time payments, to launch an investigation on a previously sent payment instruction, where an (expected) FIToFIPaymentStatusReport message is missing.

## 2.2 Scope

The scope is the set of messages used between financial institutions for the clearing and settlement of payment transactions.

## 2.3 Groups of MessageDefinitions and Functionality

### 2.3.1 Instruction Messages

The FIToFICustomerCreditTransfer message is used to move funds from a debtor account to a creditor.

The FIToFICustomerDirectDebit message is used to collect funds from a debtor account for a creditor.

The FinancialInstitutionCreditTransfer message is used to move funds from a debtor account to a creditor, where both debtor and creditor are financial institutions.

The FinancialInstitutionDirectDebit message is used to collect funds from a debtor account for a creditor, where both debtor and creditor are financial institutions.

| MessageDefinition | Message Identifier |
|---|---|
| FIToFICustomerCreditTransfer | pacs.008 |
| FIToFICustomerDirectDebit | pacs.003 |
| FinancialInstitutionCreditTransfer | pacs.009 |
| FinancialInstitutionDirectDebit | pacs.010 |

### 2.3.2 Related Messages

The FIToFIPaymentReversal message is used to reverse a payment previously executed.

The PaymentReturn message is used to undo a payment previously settled.

The FIToFIPaymentStatusReport message is used to inform on the positive or negative status of an instruction (either single or file) and to report on a pending instruction.

The FIToFIPaymentStatusRequest message is used to request a FIToFIPaymentStatusReport message containing information on the status of a previously sent instruction.

---

<!-- Page 7 -->

| MessageDefinition | Message Identifier |
| :--- | :--- |
| FIToFIPaymentReversal | pacs.007 |
| PaymentReturn | pacs.004 |
| FIToFIPaymentStatusReport | pacs.002 |
| FIToFIPaymentStatusRequest | pacs.028 |

---

<!-- Page 8 -->

# 3 BusinessRoles and Participants

A BusinessRole represents an entity (or a class of entities) of the real world, physical or legal, a person, a group of persons, a corporation. Examples of BusinessRoles: "Financial Institution", "Automated Clearing House", "Central Securities Depository".

A Participant is a functional role performed by a BusinessRole in a particular BusinessProcess or BusinessTransaction. Examples of Participants: the "user" of a system, "debtor", "creditor", "investor".

The relationship between BusinessRoles and Participants is many-to-many. One BusinessRole can be involved as different Participants at different moments in time or at the same time. Examples of BusinessRoles: "user", "debtor", "creditor", "investor". Different BusinessRoles can be involved as the same Participant.

In the context of Payments Clearing and Settlement the high-level BusinessRoles and typical Participants can be represented as follows:

## 3.1 Participants and BusinessRoles Definitions

**Participants**



<table>
  <tr>
    <th>Description</th>
    <th>Definition</th>
  </tr>
  <tr>
    <td>Debtor</td>
    <td>Party that owes an amount of money to the (ultimate) creditor. In the context of the payment model, the debtor is also the debit account owner.</td>
  </tr>
  <tr>
    <td>Creditor</td>
    <td>Party to which an amount of money is due. In the context of the payment model, the creditor is also the credit account owner.</td>
  </tr>
  <tr>
    <td>Ultimate Debtor</td>
    <td>Ultimate party that owes an amount of money to the (ultimate) creditor.</td>
  </tr>
  <tr>
    <td>Ultimate Creditor</td>
    <td>Ultimate party to which an amount of money is due.</td>
  </tr>
  <tr>
    <td>Debtor agent</td>
    <td>Financial institution servicing an account for the debtor.</td>
  </tr>
  <tr>
    <td>Creditor Agent</td>
    <td>Financial institution servicing an account for the creditor.</td>
  </tr>
  <tr>
    <td>Forwarding Agent</td>
    <td>Financial institution that receives the instruction from the initiating party and forwards it to the next agent in the payment chain for execution.</td>
  </tr>
  <tr>
    <td>Initiating Party</td>
    <td>Party initiating the payment to an agent. In the payment context, this can either be the debtor (in a credit transfer), the creditor (in a direct debit), or a party that initiates the payment on behalf of the debtor or creditor.</td>
  </tr>
  <tr>
    <td>Account Owner</td>
    <td>Party that legally owns the account.</td>
  </tr>
  <tr>
    <td>Account Servicer</td>
    <td>Party that manages the account on behalf of the account owner, that is manages the registration and booking of entries on the account, calculates balances on the account and provides information about the account.</td>
  </tr>
  <tr>
    <td>Payment Clearing Agent (Instructing Agent)</td>
    <td>Agent that instructs the next party in the payment chain to carry out the payment/instruction.</td>
  </tr>
  <tr>
    <td>Payment Settlement Agent (Instructed Agent)</td>
    <td>Agent that executes the instruction upon the request of the previous party in the chain (either an agreement party, or a clearing agent).</td>
  </tr>
  <tr>
    <td>Intermediary Agent</td>
    <td>Agent between the debtor's agent and the creditor's agent. There can be several intermediary agents specified for the execution of a payment.</td>
  </tr>
</table>

---

<!-- Page 9 -->

**BusinessRoles**

| Description | Definition |
| :--- | :--- |
| Financial Institution | Organisation established primarily to provide financial services. |
| Clearing System | Specifies the system which plays a role in the clearing process. |
| Party | Entity involved in a payment. |

## 3.2 BusinessRoles and Participants Table

| BusinessRole | Financial Institution | Clearing System | Party |
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

<!-- Page 10 -->

# 4 BusinessProcess Description

## 4.1 Credit Transfer

This diagram pictures the high level end-to-end payments BusinessProcesses for the credit transfer.

*   **Process end-to-end payment**
    *   Process customer-to-bank payment
    *   Process interbank payment
        *   Accept interbank payment
            *   Assess interbank Payment risk
            *   Validate interbank payment
            *   Authorise interbank payment
        *   Clear interbank payment
            *   Sort interbank payment
            *   Calculate the settlement positions
            *   Prepare onward interbank payment
                *   Generate regulatory reporting information
        *   Settle interbank payment
    *   Report

---

<!-- Page 11 -->

## Accept Inter-Bank Payment

| Item | Description |
|---|---|
| Definition | Payment acceptance includes the check of the validation of the payment and the payment risk assessment. |
| Trigger | Receipt of the payment order. |
| Pre-conditions | Clearing agent has received the payment order. |
| Post-conditions | Payment has been accepted or rejected. |
| Role | Financial Institution |

## Asses Interbank Payment Risk

| Item | Description |
|---|---|
| Definition | Settlement agent undertakes the necessary risk checks in order to process the payment further, for example, embargo, sufficient credit, cover received, system limits. |
| Trigger | Receipt of the payment order. |
| Pre-conditions | The settlement agent has received the payment order. |
| Post-conditions | Payment has been accepted or rejected. |
| Role | Financial Institution |

## Validate Interbank Payment

| Item | Description |
|---|---|
| Definition | Clearing agent undertakes the necessary content checks in order to process the payment further. For example, authenticate the remitting party, validate syntax, confirm the SLAs. |
| Trigger | Receipt of the payment order. |
| Pre-conditions | The clearing agent has received the payment order. |
| Post-conditions | Payment has been accepted or rejected. If accepted, the instructed payment is ready for the risk assessment or is executable. |
| Role | Financial Institution |

## Authorise Interbank Payment

| Item | Description |
|---|---|
| Definition | Authorisation of a payment order by the payment clearing agent. This is an extension of the sub-process of the Accept Interbank Payment process. An authorisation may be implicit if the system where the payment is generated has been approved to generate payments, as the preceding procedures are deemed satisfactory secure. The system will then generate a digital signature without manual intervention. An authorisation may be explicit, if procedures require human approval. |
| Trigger | A payment order has been created. |
| Pre-conditions | Accept payment process is completed and waits for authorisation if required by the payment clearing agent. |

---

<!-- Page 12 -->

| Item | Description |
|---|---|
| Post-conditions | Payment order is authorised. |
| Role | Financial Institution |

## Clear Interbank Payment

| Item | Description |
|---|---|
| Definition | Preparation of the payment information by the payment clearing agent for the next clearing agent in the interbank chain. This process of preparing payment information can be divided into the sub-processes 'Sort payment' and 'prepare onward interbank payment'. |
| Trigger | Payment execution date is reached. |
| Pre-conditions | Payment is accepted. |
| Post-conditions | Next clearing agent is determined. |
| Role | Clearing system or financial institution |

## Sort Interbank Payment

| Item | Description |
|---|---|
| Definition | Clearing agent determines the next clearing agent or creditor/debtor for the payment. The clearing agent identification is done by the previous party or selected by the current agent (tables). The last clearing agent is determined by the creditor/debtor's account service. |
| Trigger | • The payment must be instructed to the next party . |
| Pre-conditions | Payment is accepted. |
| Post-conditions | Next clearing agent is determined. |
| Role | Financial institution |

## Calculate the Settlement Positions

| Item | Description |
|---|---|
| Definition | Clearing agent applies the payment amount to the debit party and credit party's clearing positions. For multiple payments, it is equivalent to calculate the sub-settlement positions. The calculation may be done continuously or at certain times through bilateral netting. The settlement may be delegated to a third party. |
| Trigger | Payment has been accepted. |
| Pre-conditions | Payment is executable. |
| Post-conditions | Payment amount is applied to the debit and credit party. |
| Role | Financial institution |

## Prepare Onward Interbank Payment

| Item | Description |
|---|---|
| Definition | Clearing agent collects the information necessary to remit the payment to the next party (clearing and/or settlement agent). Then the clearing agent remits the payment to the party. |
| Trigger | Payment must be instructed to the next party. |

---

<!-- Page 13 -->

| Item | Description |
| :--- | :--- |
| Pre-conditions | Money has been received. |
| Post-conditions | The onward payment is ready. |
| Role | Financial institution |

## Settle Interbank Payment

| Item | Description |
| :--- | :--- |
| Definition | Settlement agent performs the transfer of cash between the debit party and the credit party. |
| Trigger | Payment execution date in the payment is reached. |
| Pre-conditions | Instructed payment is executable (all information is there to process the payment and the payment validity has been checked) and the settlement agent is identified by the clearing agent. |
| Post-conditions | Transfer of ownership is performed between the debit party and credit party. |
| Role | Financial institution |

## Generate Regulatory Reporting Information

| Item | Description |
| :--- | :--- |
| Definition | Forwarding party or debtor agent selects the information from the payment transaction necessary to meet regulatory reporting requirements, if necessary, for example, balance of payments reporting, reporting on money-laundering issues. |
| Trigger | Payment meets the regulatory reporting criteria. |
| Pre-conditions | There are regulatory reporting requirements. |
| Post-conditions | Information for the regulatory reporting has been extracted based on information in the payment. |
| Role | Financial institution |

# 4.2 Direct Debit

This diagram pictures the high level BusinessProcesses for the direct debit.

*   Process Direct Debit end-to-end
    *   Manage Direct Debit Mandate
        *   Process batch of Direct Debit
    *   Process customer-to-bank Direct Debit
        *   Process incoming Direct Debit
    *   Process interbank Direct Debit
        *   Process reversals
        *   Process return/mandate for refund
    *   Report
        *   Process report
        *   Process cancellation/Revocation

---

<!-- Page 14 -->

## Process direct debit

| Item | Description |
| :--- | :--- |
| Definition | The creditor's agent (or creditor if it is a financial institution direct debit) sends the message to the clearing system in line with the clearing cycle. The clearing system forwards the message to the debtor's agent immediately for information purposes only and processes the direct debit in accordance with the settlement cycle, to initiate the debit to the debtor's account. |
| Trigger | Release of direct debit instructions to the instructed agent. |
| Pre-conditions | Direct debit instructions received and successfully validated. |
| Post-conditions | Forwarded direct debit instructions. |
| Role | Financial institution / clearing system |

## Process Reject

| Item | Description |
| :--- | :--- |
| Definition | Reconciles reject with the original direct debit instructions and identifies the reason for rejection. If the reject results from a formatting error, correct the data and resubmit for processing. |
| Trigger | Reconciliation of the reject. |
| Pre-conditions | Reject received. |
| Post-conditions | Reconciled reject. |
| Role | Financial institution |

## Process Return/Request for Refund

| Item | Description |
| :--- | :--- |
| Definition | Returns are individual debits that have reached the debtor's agent and have been settled at the inter-bank level, but the debtor's agent is then unable to make the collection for one of a number of reasons, for example, account closed, no funds, customer dead, etc. The debtor has the unconditional right during "n" days after a debit to instruct its bank to revoke the debit. Following that instruction the debtor's account is credited by its bank and the debit is returned electronically through the clearing process to the creditor's agent. |
| Trigger | Return of a direct debit / request for refund. |
| Pre-conditions | Settled direct debit instruction subject for return / refund. |
| Post-conditions | Returned direct debit instruction / requested refund. |
| Role | Financial institution or party |

## Process Reversal

| Item | Description |
| :--- | :--- |
| Definition | The direct debit reversal will contain sufficient information which allows the debtor's agent to identify it as a "reversal" of a particular direct debit. The debtor's agent will credit debtor's account under quotation of the original direct debit reference and the reason for reversal. |
| Trigger | Accounting and reporting of the direct debit reversal instruction |

---

<!-- Page 15 -->

| Item | Description |
| :--- | :--- |
| Pre-conditions | Direct debit reversal received and successfully validated |
| Post-conditions | Reversed direct debit instruction |
| Role | Financial institution |

| Note | The process cancellation/revocation is out of scope. |
| :--- | :--- |

---

<!-- Page 16 -->

# 5 Description of BusinessActivities

This section presents the different BusinessActivities within each BusinessProcess. The BusinessActivities of a process are described with activity diagrams.

**Legend**

| Symbol | Name | Definition |
|---|---|---|
| ● | Start Point | Shows where the lifecycle of the business process commences. |
| ◉ | End Point | Shows where the lifecycle of the business process may ends. |
| ◇ | Lozenge (or diamond) | Indicates that a choice between several actions can be made. |
| — | Bar | Indicates that several actions are initiated in parallel. |

## 5.1 Credit Transfer

[Activity Diagram: Swimlanes — PaymentClearingAgent A | PaymentClearingAgent B | PaymentSettlementAgent]

- PaymentClearingAgent A: Start Point → Prepare payment (debtor payment) → Init payment → Create payment data → ◇ "Is it a bar transfer?" → [No] Receive payment order → [Yes] Prepare payment (creditor payment) → [SingleCreditTransferMessage]
- PaymentClearingAgent B: Receive payment order → Check payment validation → ◇ "Sufficient data for payment order?" → [No] Ask for payment validation → [Yes] ◇ "Is payment order valid?" → [Yes] End (creditor payment) / [No] ...
- PaymentSettlementAgent: Receive payment order → End (creditor payment) → Cancel payment (creditor payment) → Prepare payment (creditor payment) → End Point
- Cross-lane messages: [SingleCreditTransferMessage], [SettlementMessage], [SettlementResponse], [SettlementCancel], [SettlementCancelResponse]

The agents in this activity diagram are called PaymentClearingAgent and PaymentSettlementAgent in generic terms. In more concrete examples, these will be replaced by the most relevant agents, for example, debtor agent, creditor agent and intermediary agent.

---

<!-- Page 17 -->

| Step | Description | Initiator |
| :--- | :--- | :--- |
| Prepare onward interbank payment | The PaymentClearingAgent prepares the outgoing payment instruction and selects the next PaymentClearingAgent and/or the clearing channel through which the payment instruction will be cleared and/or settled. | PaymentClearingAgent A |
| Send payment | The PaymentClearingAgent sends out the payment instruction to the selected channel/PaymentClearingAgent. | PaymentClearingAgent A |
| Assess reject reason code | The PaymentClearingAgent assesses the reject reason code provided by the rejecting PaymentClearingAgent. | PaymentClearingAgent A |
| Repair payment order | The PaymentClearingAgent reformats/supplements the original payment order for re-submission to the appropriate clearing channel/PaymentClearingAgent. | PaymentClearingAgent A |
| Recycle payment order | The PaymentClearingAgent recycles the rejected payment order. Recycling can be by downgrading the STP level under which the payment order can be cleared and settled, or selecting another channel for clearing and settling the payment. | PaymentClearingAgent A |
| Receive payment order | The PaymentClearingAgent acknowledges receipt of the payment order (technical) and proceeds to next step. | PaymentClearingAgent B |
| Apply technical validation | The PaymentClearingAgent applies technical validation on the payment order. Technical validation may comprise syntactic validation (conformance of the payment order with its technical definition), semantic validation ( message, through to technical content consistency). | PaymentClearingAgent B |
| Apply business validation | | PaymentClearingAgent B |
| Reject payment order | The PaymentClearingAgent rejects the payment order to the preceding PaymentClearingAgent and appends a relevant reject reason code explaining the reason for the reject. | PaymentClearingAgent B |
| Sort interbank payment | | PaymentClearingAgent B |
| Calculate settlement positions | | PaymentClearingAgent B |
| Prepare onward interbank payment | The PaymentClearingAgent prepares the outgoing payment instruction and selects the next PaymentClearingAgent and/or the clearing channel through which the payment instruction will be cleared and/or settled. | PaymentClearingAgent B |
| Assess interbank payment risk | | PaymentSettlementAgent |
| Settle payment order | | PaymentSettlementAgent |
| Inform about settlement | | PaymentSettlementAgent |

---

<!-- Page 18 -->

## 5.2 Direct Debit

Some base definitions of direct debit terms:

- Direct Debit: Direct Debit(s) results in cash transfers between debtors and creditors through infrastructures or correspondent banks. They may be exchanged as single instructions but are traditionally grouped following some common characteristics and, for convenience or efficiency reasons, exchanged in a batch mode.

- Mandate: This is the authorisation / expression of consent given by the Debtor allowing a specified creditor to originate Direct Debit instructions for debiting the specified Debtor's account in accordance with the relevant Direct Debit scheme rules and, if applicable, the mandate details.

- Reject: Rejects are individual debits or files of debits that are rejected due to technical reasons, e.g. invalid format, wrong IBAN check digit. Rejects take place prior to interbank settlement if the creditor's agent, the debtor's agent or any other agent in the chain is not able to process the individual debit or files of debits.

- Request for Cancellation: A request by the creditor to cancel a Direct Debit instruction prior to the interbank settlement

- Revocation: A request by the creditor to revoke a Direct Debit Payment order prior to the acceptance by the creditor's Agent.

- Reversal: The creditor initiates a reversal instruction after settlement, when a paid Direct Debit should not have been processed. Consequently, the debtor will be credited back.

- Refusal by the Debtor: One of the Debtor's right to refuse either any Direct Debit transaction to be debited on its account, or one Direct Debit, once pre-noticed by a creditor.

- Return: Returns are individual debits that have reached the Debtor's Agent and have been settled at the interbank level, but the Debtor's Agent is then unable to make the collection for one of a number of reasons e.g. account closed, no funds, customer dead, account does not accept Direct Debit, etc.

- Refund: Refund is the process to claim for reimbursement of a Direct Debit for any reason after settlement and within a defined period ("n" days). A refund instruction is initiated by the Debtor.

---

<!-- Page 19 -->

## 5.2.1 Direct debit instruction

![Direct debit instruction flowchart](image)

| Step | Description | Initiator |
|---|---|---|
| Forward 1st/off Direct Debit | The creditor agent (or creditor for financial institution direct debits) sends the message to the clearing system in line with the clearing cycle. The clearing system forwards the message to the debtor agent and processes the direct debit in accordance with the settlement cycle, to initiate the debit to the Debtor's account. | Creditor Agent or Creditor |
| Reject Direct Debit instruction | Reject prior to interbank settlement by creditor agent or its processing agent. Rejections can happen for a number of reasons, some of which are defined by the scheme rules and some of which are due to specific controls defined by the creditor agent or any other agents in the chain. | Creditor Agent |
| Process B2B reject | The creditor agent reconciles the Direct Debit reject with the original Direct Debit instructions and assesses the reason causing the reject e.g. formatting error, value date incompatibility, invalid bank operation code, etc. | Creditor Agent |
| Correct and resubmit | In case of formatting issues the creditor agent corrects the data and resubmits it for processing. | Creditor Agent |
| Reject Direct Debit instruction | The debtor agent may reject the instruction due to a number of reasons (e.g. missing account for debtor, missing agreement with the debtor to accept Direct Debits. | Debtor Agent |
| Return Direct Debit | Returns are individual debits that have | Debtor Agent |

---

<!-- Page 20 -->

| Step | Description | Initiator |
| :--- | :--- | :--- |
| Instruction | reached the debtor agent and have been settled at the interbank level, but the debtor agent is then unable to make the collection for one of a number of reasons e.g. account closed, no funds available, etc. | |
| | Detailed Direct Debit Return activity diagram available below. | |
| Report Direct Debit Settlement Proceeds | Process that includes the calculation of the settlement positions and transmission of the settlement information to the settlement agent. | ACH |
| Request Refund | The debtor has the unconditional right during "n" days after a debit to instruct its bank to revoke the debit. Following that instruction, the debtor account is credited by his bank and the debit is returned electronically through the clearing process to the creditor agent. | Debtor |
| | Detailed request refund Direct Debit activity diagram available below. | |

## 5.2.2 Return Direct Debit

![Return Direct Debit activity diagram](image)

---

<!-- Page 21 -->

## 5.2.3 Request Refund Direct Debit

[Flowchart: Request Refund Direct Debit process involving Creditor, Creditor Agent, PSP, and Debtor with steps like Request Refund, Check Provisional Credit, Submit Refund, Refund Accepted/Rejected, Generate Credit Transfer Instruction, etc.]

## 5.2.4 Direct Debit Reversal

The creditor initiates a reversal instruction after settlement, when a paid Direct Debit should not have been processed. If the reversal instruction is accepted, consequently the Debtor will be credited back.

[Flowchart: Direct Debit Reversal process involving Creditor, Creditor Agent, PSP, and Debtor with steps like Request Reversal, Check Provisional Credit, Submit Reversal, Reversal Accepted/Rejected, Generate Credit Transfer Instruction, etc.]

| Step | Description | Initiator |
| :--- | :--- | :--- |
| Request reversal of the Direct Debit payment order | The creditor identifies the original direct debit instruction (or a file of direct debit instructions) and generates an offsetting transaction in favor of the debtor under quotation of the reversal reason. | Creditor |
| Process request for reversal and submit reversal to the clearing | The creditor agent identifies the original direct debit instruction and generates an offsetting clearing transaction in favor of the debtor. Subject transaction is submitted to the instructed agent for | Creditor Agent |

---

<!-- Page 22 -->

| Step | Description | Initiator |
| :--- | :--- | :--- |
| | settlement under quotation of the original direct debit reference and the reversal reason. | |
| Reject reversal | Rejects are individual transactions/messages or batches that are rejected prior to interbank settlement. | Instructed Agent/ACH |
| Process B2B rejected reversal | The creditor agent reconciles the reject with the original instruction and assesses the reason causing the reject e.g. formatting error, due date incompatibility or invalid bank operation code. | Creditor Agent |
| Clear Direct Debit Reversal | Preparation of the payment information for the next agent in the chain (in accordance with the agreed and published settlement cycle). The process includes the calculation of the settlement positions and transmission of the files to the next agent. | ACH |
| Return Direct Debit Reversal | The debtor may return the direct debit reversal based on a number of reasons (e.g. account number invalid). The debtor agent returns the transaction in line with the clearing rules and specifications via the Instructed Agent/ACH. | Debtor Agent |
| Settle Direct Debit Reversal Proceeds | The settlement agent performs the transfer of funds from the credit party to the debit party (in accordance with the agreed and published settlement cycle). | Settlement Agent |

---

<!-- Page 23 -->

# 6 BusinessTransactions

This section describes the message flows based on the activity diagrams documented above. It shows the typical exchanges of information in the context of a BusinessTransaction.

When relevant, messages from other business areas, which are necessary for a complete understanding of the transaction, are shown on the BusinessTransaction diagrams:

| Message | Number |
|---|---|
| CustomerDirectDebitInitiation | Pain.008 |

## 6.1 Credit Transfer

### 6.1.1 FIToFICustomerCreditTransfer

An FIToFICustomerCreditTransfer message is the inter-bank movement of an amount from a party bank account (the debtor account) to a beneficiary party (the creditor).

FIToFICustomerCreditTransfer messages result in one or more cash transfers between debtors and creditors through correspondent banks or infrastructures. They may be exchanged as single or grouped instructions following certain common characteristics and, for convenience or efficiency reasons, exchanged in a batch mode. The processing of credit transfers may differ from country to country and system to system.

Depending on the scenario, there might be an agent between the debtor agent and the creditor agent. This agent can be an intermediary agent or a reimbursement agent. The narrative will describe more in detail the agent role.

In scenarios where the receiving agent services an account for the sending agent, the scenario also includes the case where the sending agent has an account with a branch/head office of the receiving agent and will indicate that the receiving agent can reimburse itself at this institution. The sending agent has to be aware of an intra-group agreement allowing this.

A payment clearing and settlement system could occur between debtor agent and creditor agent (or between any other agents). The clearing process where the clearing agent after being informed on the transaction prepares and sends the payment information to the settlement agent (if different) is out of scope and will not be described. This process includes the calculation of the settlement positions and transmission of files to the settlement agent. The settlement agent transfers the funds from the debtor agent to the creditor agent in accordance with the settlement cycle and based on the settlement report provided by the clearing agent.

Only messages concerning the interbank credit transfer are illustrated in the sequence diagrams. The original contracts between the debtor and the creditor (for example order and invoice) and the CustomerCreditTransferInitiation message by the debtor are out of scope and are therefore not included in the diagram.

#### 6.1.1.1 Debtor Agent and Creditor Agent are Correspondents

The debtor agent and creditor agent are correspondents in the currency of the transaction.

---

<!-- Page 24 -->

Debtors
Debtor Agent
Intermediary Agent 1 or Instructed or Instructing Reimbursement Agent
Creditor Agent
Creditor

FitOfICustomerCreditTransfer
FitOfIPaymentStatusReport

The scenario caters for the debtor agent servicing an account for the creditor agent and vice versa. It also covers the case where debtor agent and creditor agent are linked directly across a payment clearing and settlement system.

The debtor agent sends the FitOfICustomerCreditTransfer message to the creditor agent.

The creditor agent optionally confirms the processability of the FitOfICustomerCreditTransfer instruction by sending a positive FitOfIPaymentStatusReport message to the debtor agent.

**Out of Scope**
- The 'On Us' scenario where the debtor agent is also the creditor agent
- Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement')) messages)

## 6.1.1.2 Debtor Agent and Creditor Agent are not Correspondents - 1

There is an intermediary agent between the debtor agent and creditor agent (the so-called 3-party serial payment).

Debtors
Debtor Agent
Intermediary Agent 1 or Instructed or Instructing Reimbursement Agent
Creditor Agent
Creditor

FitOfICustomerCreditTransfer
FitOfIPaymentStatusReport
FitOfICustomerCreditTransfer
FitOfIPaymentStatusReport

The scenario also covers the payment clearing system case where the agent between the debtor agent and the creditor agent is a clearing and/or settlement agent.

---

<!-- Page 25 -->

For sake of simplicity, the scenario is limited to one intermediary agent between the debtor agent and the creditor agent.

The debtor agent sends the FIToFICustomerCreditTransfer message to the intermediary agent.

The intermediary agent optionally confirms the processability of the FIToFICustomerCreditTransfer by sending a positive FIToFIPaymentStatusReport message to the debtor agent.

The intermediary agent forwards the FIToFICustomerCreditTransfer message to the creditor agent.

The creditor agent optionally confirms the processability of the FIToFICustomerCreditTransfer instruction by sending a positive FIToFIPaymentStatusReport message to the intermediary agent.

**Out of Scope**

- The intermediary agent may send a status update to the debtor agent.
- Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages)

## 6.1.1.3 Debtor Agent and Creditor Agent are not Correspondents - 2

The debtor agent and the creditor agent are not correspondents in the currency of the transaction. There is a reimbursement agent between them (so-called 3-party cover payment).

For the sake of simplicity, it is assumed that the debtor agent and the creditor agent have the same reimbursement agent. The FIToFICustomerCreditTransfer instruction will be covered through a separate FinancialInstitutionCreditTransfer message sent to the reimbursement agent (illustrated under the FinancialInstitutionCreditTransfer section).

The debtor agent sends the FIToFICustomerCreditTransfer message to the creditor agent.

The creditor agent optionally confirms the processability of the FIToFICustomerCreditTransfer instruction by sending a positive FIToFIPaymentStatusReport message to the debtor agent.

The debtor agent sends a FinancialInstitutionCreditTransfer message to the reimbursement agent.

The reimbursement agent optionally confirms the processability of the FinancialInstitutionCreditTransfer by sending a positive FIToFIPaymentStatusReport message to the debtor agent.

**Out of Scope**

- Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages)

---

<!-- Page 26 -->

## 6.1.2 Negative FIToFIPaymentStatusReport with FIToFICustomerCreditTransfer

The negative FIToFIPaymentStatusReport message is used, point to point between two parties, to report about the negative processability of an instruction, that is, to report about the rejection of the instruction, and is used to:

- Reject an FIToFICustomerCreditTransfer
- Reject a FinancialInstitutionCreditTransfer

The negative FIToFIPaymentStatusReport message is sent before settlement.

After settlement, the correct message to be used is the PaymentReturn message, the BankToCustomerDebitCreditNotification message ('notification') and/or the BankToCustomerAccountReport/ BankToCustomerStatement message ('statement'). Different options are illustrated in the sequence diagram.

### 6.1.2.1 Debtor Agent and Creditor Agent are Direct Correspondents

Negative FIToFIPaymentStatusReport messages are exchanged when rejecting an instruction.

Debtor | Debtor Agent | Intermediary Agent 1 or Instructed or Instructing Reimbursement Agent | Creditor Agent | Creditor

FIToFICustomerCreditTransfer →

← FIToFIPaymentStatusReport

This scenario covers the case where the creditor agent (or a branch/head office of the creditor agent) services an account for the debtor agent. In the cases where the debtor agent services an account for the creditor agent and in the case of clearing system payments, the creditor agent will inform about the non-processability by using a PaymentReturn message.

The debtor agent sends the FIToFICustomerCreditTransfer message to the creditor agent.

The creditor agent sends a negative FIToFIPaymentStatusReport message to inform the debtor agent about the non-processability of the FIToFICustomerCreditTransfer instruction (for example, due to missing or incorrect information).

**Note** Whenever possible, the debtor agent might try to repair and re-submit the instruction. Depending on what has been agreed with the debtor, the debtor agent may inform the debtor of the repair with an updated FIToFIPaymentStatusReport message.

### 6.1.2.2 Debtor Agent and Creditor Agent are not Correspondents - 1

There is an intermediary agent between the debtor agent and creditor agent (so-called 3-party Serial payment). Negative FIToFIPaymentStatusReport messages are exchanged when rejecting an instruction.

---

<!-- Page 27 -->

Debtor | Debtor Agent | Intermediary Agent 1 or Instructed or Instructing Reimbursement Agent | Creditor Agent | Creditor

- FitToFCustomerCreditTransfer
- FitToFPaymentStatusReport
- FitToFCustomerCreditTransfer
- FitToFPaymentStatusReport
- Case A: PaymentStatusReport
- Case B: PaymentReturn

The scenario covers the case where the creditor agent (or branch/head office of creditor agent) services an account for the intermediary agent. In the cases where the intermediary agent services an account for the creditor agent or they are linked through a payment clearing system, the creditor agent will inform about the non-processability by using a PaymentReturn message.

The debtor agent sends the FitToFCustomerCreditTransfer message to the intermediary agent.

The intermediary agent may optionally confirm the processability of the FitToFCustomerCreditTransfer instruction by sending a positive FitToFPaymentStatusReport message to the debtor agent.

The intermediary agent forwards the FitToFCustomerCreditTransfer message to the creditor agent.

The creditor agent sends a negative FitToFPaymentStatusReport message to inform the intermediary agent about the non-processability of the FitToFCustomerCreditTransfer instruction (for example due to missing/incorrect information).

| Note | The intermediary agent might try to repair and re-submit the instruction when possible and inform the debtor agent with an updated FitToFPaymentStatusReport accordingly. |
|---|---|

**Case A**

The intermediary agent has not yet booked the instruction on the account of the debtor agent.

The intermediary agent forwards the negative FitToFPaymentStatusReport message to inform the debtor agent about the non-processability of the FitToFCustomerCreditTransfer instruction.

**Case B**

The intermediary agent has booked the instruction on the account of the debtor agent.

The intermediary agent sends a PaymentReturn message including the Return reason to the debtor agent to inform the debtor agent about the non-processability of the FitToFCustomerCreditTransfer instruction.

---

<!-- Page 28 -->

## 6.1.2.3 Debtor Agent and Creditor Agent are not Correspondents - 2

The debtor agent and creditor agent are not correspondents in the currency of the transaction. There is a reimbursement agent between them (so-called 3-party cover payment). Negative FIToFIPaymentStatusReport messages are exchanged when rejecting an instruction.

```
Debtor        Debtor Agent        Intermediary Agent 1 or Instructed or Instructing Reimbursement Agent        Creditor Agent        Creditor
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |
   |               |                          |                                              |                     |

---

<!-- Page 29 -->

## 6.1.3.1 Debtor Agent and the Creditor Agent are Correspondents

A return is exchanged after settlement has taken place.

```
Debtor      Debtor Agent      Intermediary Agent 1 or Instructed or      Creditor Agent      Creditor
                |              Instructing Reimbursement Agent                |                 |
                |                     |                                       |                 |
                |                     |---- FIToFICustomerCreditTransfer ---->|                 |
                |                     |                                       |                 |
                |                     |<---- PaymentReturn ------------------|                 |
                |                     |                                       |                 |
                |                     |---- FIToFIPaymentStatusReport ------>|                 |
                |                     |                                       |                 |
```

The scenario covers the case where the debtor agent services an account for the creditor agent and the case where debtor agent and creditor agent are linked through a payment clearing system.

Where the creditor agent services an account for the debtor agent, the creditor agent will inform about the non- processability of the instruction by using a negative FIToFIPaymentStatusReport (status Reject) message.

The debtor agent sends the FIToFICustomerCreditTransfer message to the creditor agent.

The creditor agent sends a PaymentReturn message to inform the debtor agent about the non-processability of the FIToFICustomerCreditTransfer instruction including the return reason (for example due to missing/incorrect information/closed account…).

The debtor agent optionally confirms the processability of the PaymentReturn message by sending a positive FIToFIPaymentStatusReport message to the creditor agent.

| Note | Whenever possible, the debtor agent might try to repair and re-submit the instruction. Depending on what has been agreed it may inform the debtor about the repair with an updated FIToFIPaymentStatusReport message. |
|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

---

<!-- Page 30 -->

Debtor

Debtor Agent

Intermediary Agent 1 or Instructed or Instructing Reimbursement Agent

Creditor Agent

Credor

FitOfICustomerCreditTransfer

FitOfIPaymentStatusReport

FitOfICustomerCreditTransfer

PaymentStatusReport

FitOfIPaymentStatusReport

PaymentReturn

FitOfIPaymentStatusReport

The scenario covers the case where the intermediary agent services an account for the creditor agent or the case where the intermediary agent and the creditor agent are linked through a payment clearing system.

If the creditor agent services an account for the intermediary agent, the creditor agent will inform about the non-processability with a negative FitOfIPaymentStatusReport (status Reject) message.

Depending on whether settlement has taken place or not, the intermediary agent might report to the debtor agent with a negative FitOfIPaymentStatusReport or a PaymentReturn message.

The debtor agent sends the FitOfICustomerCreditTransfer message to the intermediary agent.

The intermediary agent optionally confirms the processability of the FitOfICustomerCreditTransfer by sending a positive FitOfIPaymentStatusReport message to the debtor agent.

The intermediary agent forwards the FitOfICustomerCreditTransfer message to the creditor agent.

The creditor agent sends a PaymentReturn message to inform the intermediary agent about the non-processability of the FitOfICustomerCreditTransfer (for example due to missing/incorrect information) including the return reason.

The intermediary agent optionally confirms the receipt of the PaymentReturn message by sending a positive FitOfIPaymentStatusReport message to the creditor agent.

| Note | The intermediary agent might try to repair and re-submit the instruction when possible and inform the debtor agent with an updated FitOfIPaymentStatusReport message accordingly. |
|---|---|

The intermediary agent forwards the PaymentReturn message including the return reason to the debtor agent to inform the debtor agent about the non-processability of the FitOfICustomerCreditTransfer instruction.

The debtor agent optionally confirms the receipt of the PaymentReturn message by sending a positive FitOfIPaymentStatusReport message to the intermediary agent.

---

<!-- Page 31 -->

**Note** The debtor agent might try to repair and re-submit the instruction when possible and inform the debtor with an updated FitOfiPaymentStatusReport message accordingly.

**Out of Scope**
- Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages)

## 6.1.3.3 Debtor Agent and Creditor Agent are not Correspondents - 2

The debtor agent and creditor agent are not correspondents in the currency of the transaction. There is an instructed reimbursement agent between them (so-called 3-party cover payment). A return is exchanged after settlement has take place.

```
Debtor      Debtor Agent      Intermediary Agent 1 or Instructed or Instructing Reimbursement Agent      Creditor Agent      Creditor
   |             |                          |                                                        |             |
   |             |----FitOfiCustomerCreditTransfer--------------------------------------------->|             |
   |             |----FinancialInstitutionCreditTransfer----->|                                 |             |
   |             |<----FitOfiPaymentStatusReport----|         |                                 |             |
   |             |<----PaymentReturn--------------------------------------------|             |
   |             |----FitOfiPaymentStatusReport--------------------------------------------->|             |
   |             |                          |----FinancialInstitutionCreditTransfer----->|             |
   |             |                          |<----FitOfiPaymentStatusReport----|         |             |
   |             |                          |                                                        |             |
```

For sake of simplicity, it is assumed that the debtor agent and the creditor agent have the same reimbursement agent.

The debtor agent sends the FitOfiCustomerCreditTransfer message to the creditor agent.

The debtor agent sends a FinancialInstitutionCreditTransfer message to the reimbursement agent.

The reimbursement agent optionally confirms the processability of the FinancialInstitutionCreditTransfer instruction by sending a positive FitOfiPaymentStatusReport message to the debtor agent.

The creditor agent cannot apply the payment instruction (for example creditor account closed) and sends a PaymentReturn message to inform the debtor agent about the non-processability of the FitOfiCustomerCreditTransfer instruction including the return reason.

**Note** This PaymentReturn message exceptionally will not move funds, but will inform about the movement of funds (as was the case with the original FitOfiCustomerCreditTransfer). The funds will be moved with the FinancialInstitutionCreditTransfer sent by the creditor agent as described below.

---

<!-- Page 32 -->

The debtor agent optionally confirms the receipt of the PaymentReturn message by sending a positive FitToFiPaymentStatusReport message to the creditor agent.

The creditor agent sends a FinancialInstitutionCreditTransfer message to the reimbursement agent.

The reimbursement agent optionally confirms the processability of the FinancialInstitutionCreditTransfer instruction by sending a positive FitToFiPaymentStatusReport message to the creditor agent.

| Note | If the creditor agent is not aware that inter-bank settlement has taken place, it might send a negative FitToFiPaymentStatusReport message to the debtor agent. It is assumed though, that once it finds out that settlement did take place (through BankToCustomerDebitCreditNotification ('notification') and/or BankToCustomerAccountReport/ BankToCustomerStatement message ('statement') from the reimbursement agent) the creditor agent will return the funds by sending a FinancialInstitutionCreditTransfer to the reimbursement agent. |
|---|---|

**Out of Scope**
- Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages)

---

<!-- Page 33 -->

## 6.1.4 Debtor Agent sends FIToFIPaymentStatusRequest

In the previous scenarios, the (optional) possibility of confirming the processability of the FIToFICustomerCreditTransfer via a FIToFIPaymentStatusReport was always mentioned/included. In some schemes, especially referring to real-time payments, the receipt of this FIToFIPaymentStatusReport is crucial within a certain timeframe. In the case the FIToFIPaymentStatusReport is not received within the required timeframe, a reminder shall be launched by sending an FIToFIPaymentStatusRequest. This message requests to receive a FIToFIPaymentStatusReport message. The reply message to the FIToFIPaymentStatusRequest shall be a FIToFIPaymentStatusReport referring to the original payment instruction.

| Debtor | Debtor Agent | Intermediary Agent 1 or Instructed or Instructing Reimbursement Agent | Creditor Agent | Creditor |
|---|---|---|---|---|
| | FIToFICustomerCreditTransfer | | | |
| | FIToFIPaymentStatusRequest | | | |
| | FIToFIPaymentStatusReport | | | |

| Note | Sending an FIToFIPaymentStatusRequest is possible in all FIToFICustomerCreditTransfer scenarios described before (section 6.1.1, 6.1.2 and 6.1.3), if no 'final' status is received yet in a FIToFIPaymentStatusReport message. |
|---|---|

## 6.1.5 FinancialInstitutionCreditTransfer

A FinancialInstitutionCreditTransfer message is the inter-bank movement of an amount from a party bank account (the debtor) to a beneficiary party (the creditor) where all parties are financial institutions.

FinancialInstitutionCreditTransfer messages result in cash transfers between debtors and creditors through correspondent banks or infrastructures. They may be exchanged as single instructions or grouped following certain common characteristics and, for convenience or efficiency reasons, exchanged in a batch mode. The processing of credit transfers may differ from country to country and system to system.

Depending on the scenario, there might be an agent between the debtor agent and the creditor agent. This agent can be an intermediary agent or a reimbursement agent. The narrative will describe more in detail the agent role.

In scenarios where the receiving agent services an account for the sending agent, the scenario also includes the case where the sending agent has an account with a branch/head office of the receiving agent and will indicate that the receiving agent can reimburse itself at this institution. The sending agent has to be aware of an intra-group agreement allowing this.

A payment clearing and settlement system could occur between debtor agent and creditor agent (or between any other agents). The clearing process where the clearing agent after being informed on the transaction prepares and sends the payment information to the settlement agent (if different) is out of scope and will not be described. This process includes the calculation of the settlement positions and transmission of files to the settlement agent. The settlement agent transfers the funds from the debtor

---

<!-- Page 34 -->

agent to the creditor agent in accordance with the settlement cycle and based on the settlement report provided by the clearing agent.

Only the messages in the scope of interbank credit transfer are illustrated in the BusinessTransactions (sequence diagrams). The original contracts between the debtor and the creditor, for example, forex, inter-bank loans, and securities transactions, are out of scope and are not included in the diagrams.

## 6.1.5.1 Debtor and Creditor are Correspondents

```
Debtor        Debtor Agent    Intermediary Agent 1 or Instructed or    Creditor Agent    Creditor
   |              |              Instructing Reimbursement Agent          |              |
   |              |                     |                                  |              |
   |              |                     |                                  |              |
   |--------------|---------------------|----------------------------------|------------>|
   |              |                     |         FinancialInstitutionCreditTransfer      |
   |              |                     |                                  |              |
   |<-------------|---------------------|----------------------------------|------------|
   |              |                     |              FitOfPaymentStatusReport           |
   |              |                     |                                  |              |
```

The scenario covers the case where the creditor services an account for the debtor, that is, the debtor agent. In scope: the debtor sends the FinancialInstitutionCreditTransfer message to the creditor.

The creditor optionally confirms the processability of the FinancialInstitutionCreditTransfer by sending a positive FitOfPaymentStatusReport message to the debtor.

**Out of Scope**

- Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages).
- If the debtor services an account for the creditor, that is, the creditor agent, then instead of sending a FinancialInstitutionCreditTransfer message, the debtor will send a BankToCustomerDebitCreditNotification message ('notification') and/or BankToCustomerAccountReport/BankToCustomerStatement message ('statement').

## 6.1.5.2 Debtor and Creditor Agent are Correspondents

```
Debtor        Debtor Agent    Intermediary Agent 1 or Instructed or    Creditor Agent    Creditor
   |              |              Instructing Reimbursement Agent          |              |
   |              |                     |                                  |              |
   |--------------|---------------------|----------------------------------|------------|
   |              |                     |         FinancialInstitutionCreditTransfer      |
   |              |                     |                                  |              |
   |<-------------|---------------------|----------------------------------|------------|
   |              |                     |              FitOfPaymentStatusReport           |
   |              |                     |                                  |              |
```

---

<!-- Page 35 -->

The scenario covers both cases where the debtor services an account for the creditor agent and where the creditor agent services an account for the debtor.

The debtor sends the FinancialInstitutionCreditTransfer message to the creditor agent.

The creditor agent optionally confirms the processability of the FinancialInstitutionCreditTransfer by sending a positive FitOfIPaymentStatusReport message to the debtor.

**Out of Scope**
- Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages).

## 6.1.5.3 Debtor Agent and Creditor are Correspondents

| Debtor | Debtor Agent | Intermediary Agent 1 or Instructed or Instructing Reimbursement Agent | Creditor Agent | Creditor |
|---|---|---|---|---|
| → FinancialInstitutionCreditTransfer | | | | |
| ← FitOfIPaymentStatusReport | | | | |
| | → FinancialInstitutionCreditTransfer | | | |
| | ← FitOfIPaymentStatusReport | | | |

The scenario covers the case where the creditor services an account for the debtor agent.

The debtor sends the FinancialInstitutionCreditTransfer message to the debtor agent.

The debtor agent optionally confirms the processability of the FinancialInstitutionCreditTransfer instruction by sending a positive FitOfIPaymentStatusReport message to the debtor.

The debtor agent forwards the FinancialInstitutionCreditTransfer message to the creditor.

The creditor optionally confirms the processability of the FinancialInstitutionCreditTransfer by sending a positive FitOfIPaymentStatusReport message to the debtor agent.

**Out of Scope**
- Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages)
- If the debtor agent services an account for the creditor, that is, the creditor agent, then instead of sending a FinancialInstitutionCreditTransfer message, the debtor agent will send a BankToCustomerDebitCreditNotification message ('notification') and/or BankToCustomerAccountReport/ BankToCustomerStatement message ('statement').

---

<!-- Page 36 -->

## 6.1.5.4 Debtor Agent and Creditor Agent are Correspondents

```
 Debtor        Debtor Agent    Intermediary Agent 1 or Instructed or    Creditor Agent      Credor
                 Instructing Reimbursement Agent
   |                |                  |                    |                |
   | FinancialInstitutionCreditTransfer |                    |                |
   |---------------------------------->|                    |                |
   |                |                  |                    |                |
   |<---------------| FIToFIPaymentStatusReport             |                |
   |                |                  |                    |                |
   |                | FinancialInstitutionCreditTransfer    |                |
   |                |-------------------------------------->|                |
   |                |                  |                    |                |
   |                |<-----------------| FIToFIPaymentStatusReport           |
   |                |                  |                    |                |
   |                |                  |                    |                |
```

The scenario includes both cases where the debtor agent services an account for the creditor agent and vice versa. In scope: The debtor sends the FinancialInstitutionCreditTransfer message to the debtor agent.

The debtor agent optionally confirms the processability of the FinancialInstitutionCreditTransfer instruction by sending a positive FIToFIPaymentStatusReport message to the debtor.

The debtor agent forwards the FinancialInstitutionCreditTransfer message to the creditor agent.

The creditor agent optionally confirms the processability of the FinancialInstitutionCreditTransfer instruction by sending a positive FIToFIPaymentStatusReport message to the debtor agent.

**Out of Scope**
- Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages).

## 6.1.5.5 Debtor Agent and Creditor Agent are Not Correspondents

There is an intermediary agent between the debtor agent and creditor agent.

---

<!-- Page 37 -->

Debtor

Debtor Agent

Intermediary Agent 1 or Instructed or Instructing Reimbursement Agent

Creditor Agent

Creditor

FinancialInstitutionCreditTransfer

FitOfIPaymentStatusReport

FinancialInstitutionCreditTransfer

FitOfIPaymentStatusReport

FinancialInstitutionCreditTransfer

FitOfIPaymentStatusReport

For sake of simplicity only one intermediary agent has been illustrated. The scenario also caters for clearing payments with direct communication with the Clearing and settlement agent.

The debtor sends the FinancialInstitutionCreditTransfer message to the debtor agent.

The debtor agent optionally confirms the processability of the FinancialInstitutionCreditTransfer instruction by sending a positive FitOfIPaymentStatusReport message to the debtor.

The debtor agent forwards the FinancialInstitutionCreditTransfer message to the intermediary agent.

The intermediary agent optionally confirms the processability of the FinancialInstitutionCreditTransfer instruction by sending a positive FitOfIPaymentStatusReport message to the debtor agent.

The intermediary agent forwards the FinancialInstitutionCreditTransfer message to the creditor agent.

The creditor agent optionally confirms the processability of the FinancialInstitutionCreditTransfer instruction by sending a positive FitOfIPaymentStatusReport message to the intermediary agent.

**Out of Scope**

- Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages)

## 6.1.6 Negative FitOfIPaymentStatusReport with FinancialInstitutionCreditTransfer

The negative FitOfIPaymentStatusReport message is used, point to point between two parties, to report about the negative processability of an instruction, that is, to report about the rejection of the instruction, and is used to:

- Reject a FitOfICustomerCreditTransfer

- Reject a FinancialInstitutionCreditTransfer

The negative FitOfIPaymentStatusReport message is sent before Settlement.

After Settlement, the correct message to be used is the PaymentReturn message, the BankToCustomerDebitCreditNotification message ('notification') and/or the BankToCustomerAccountReport/ BankToCustomerStatement message ('statement'). Different options are illustrated in the message flow.

---

<!-- Page 38 -->

## 6.1.6.1 Debtor and Creditor are Correspondents

Negative FIToFIPaymentStatusReport messages are exchanged when rejecting an instruction.

```
Debtors       Debtors Agent    Intermediary Agent 1 or Instructed or    Creditors Agent    Creditors
                Instructing Reimbursement Agent
   |                |                  |                   |                |
   |----------------|------------------|-------------------|----------------|-->
   |                |                  |  FinancialInstitutionCreditTransfer |                |
   |                |                  |                   |                |
   |<---------------|------------------|-------------------|----------------|
   |                |                  |  FitToFIPaymentStatusReport       |                |
   |                |                  |                   |                |
```

The scenario covers the case where the creditor services an account for the debtor, that is, the debtor agent.

For cases where the debtor services an account for the creditor, or the debtor and creditor are linked through a clearing and settlement system, the creditor will inform about the non-processability of the instruction, by using a PaymentReturn message.

The debtor sends the FinancialInstitutionCreditTransfer message to the creditor.

The creditor sends a negative FIToFIPaymentStatusReport message to inform the debtor about the non-processability of the FinancialInstitutionCreditTransfer instruction (for example due to missing/incorrect information).

## 6.1.6.2 Debtor and Creditor Agent are Correspondents

Negative FIToFIPaymentStatusReport messages are exchanged when rejecting an instruction.

```
Debtors       Debtors Agent    Intermediary Agent 1 or Instructed or    Creditors Agent    Creditors
                Instructing Reimbursement Agent
   |                |                  |                   |                |
   |                |------------------|-------------------|-->
   |                |  FinancialInstitutionCreditTransfer  |                |
   |                |                  |                   |                |
   |<---------------|------------------|-------------------|
   |                |  FitToFIPaymentStatusReport          |                |
   |                |                  |                   |                |
```

The scenario covers the case where the creditor agent services an account for the debtor.

In cases where the debtor services an account for the creditor agent, or debtor and creditor agent are linked through a clearing and settlement system, the creditor agent will inform about the non-processability of the instruction by using a PaymentReturn message.

---

<!-- Page 39 -->

The debtor sends the FinancialInstitutionCreditTransfer message to the creditor agent.

The creditor agent sends a negative FitOfIPaymentStatusReport message to inform the debtor about the non-processability of the FinancialInstitutionCreditTransfer instruction (for example due to missing/incorrect information).

## 6.1.6.3 Debtor Agent and Creditor are Correspondents

Negative FitOfIPaymentStatusReport messages are exchanged when rejecting an instruction.

Debtor | Debtor Agent | Intermediary Agent 1 or Instructed or Instructing Reimbursement Agent | Creditor Agent | Creditor

FinancialInstitutionCreditTransfer

FitOfIPaymentStatusReport

FinancialInstitutionCreditTransfer

FitOfIPaymentStatusReport

The scenario covers the case where the creditor services an account for the debtor agent.

In cases where the debtor agent services an account for the creditor, or debtor agent and creditor are linked through a clearing and settlement system, the creditor will inform about the non-processability of the instruction by using a PaymentReturn message.

The debtor sends the FinancialInstitutionCreditTransfer message to the debtor agent.

The debtor agent optionally confirms the processability of the FinancialInstitutionCreditTransfer instruction by sending a positive FitOfIPaymentStatusReport message to the debtor.

The debtor agent forwards the FinancialInstitutionCreditTransfer instruction to the creditor.

The creditor sends a negative FitOfIPaymentStatusReport message to inform the debtor agent about the non-processability of the FinancialInstitutionCreditTransfer instruction.

| Note | The debtor agent might try to correct and re-submit the instruction and inform the debtor about this correction with an updated FitOfIPaymentStatusReport message. If the status is now positive, no further action is required but the debtor might be informed on the positive outcome through a positive FitOfIPaymentStatusReport message. |
|---|---|

### Out of Scope

- Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages)

## 6.1.6.4 Debtor Agent and Creditor Agent are Correspondents

Negative FitOfIPaymentStatusReport messages are exchanged when rejecting an instruction.

---

<!-- Page 40 -->

| Debtor | Debtor Agent | Intermediary Agent 1 or Instructed or Instructing Reimbursement Agent | Creditor Agent | Creditor |
| :---: | :---: | :---: | :---: | :---: |
| FinancialInstitutionCreditTransfer | | | | |
| FitOfIPaymentStatusReport | | | | |
| | FinancialInstitutionCreditTransfer | | | |
| | FitOfIPaymentStatusReport | | | |

The scenario covers the case where the creditor agent services an account for the debtor agent.

In cases where the debtor agent services an account for the creditor agent, or debtor agent and creditor agent are linked through a clearing and settlement system, the creditor agent will inform on the non-processability of the instruction by using a PaymentReturn message.

The debtor sends the FinancialInstitutionCreditTransfer message to the debtor agent.

The debtor agent optionally confirms the processability of the FinancialInstitutionCreditTransfer instruction by sending a positive FitOfIPaymentStatusReport message to the debtor.

The debtor agent forwards the FinancialInstitutionCreditTransfer message to the creditor agent.

The creditor agent sends a negative FitOfIPaymentStatusReport message to inform the debtor agent about the non-processability of the FinancialInstitutionCreditTransfer instruction.

| Note | The debtor agent might try to correct and re-submit the instruction and inform the debtor about this correction with an updated FitOfIPaymentStatusReport message. If status is now positive no further action is required, but the debtor might be informed on the positive outcome through a positive FitOfIPaymentStatusReport message. |
| :--- | :--- |

**Out of Scope**
- Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages).

## 6.1.6.5 Debtor Agent and Creditor Agent Not Correspondents

Negative FitOfIPaymentStatusReport messages are exchanged when rejecting an instruction.

---

<!-- Page 41 -->

| Debtor | Debtor Agent | Intermediary Agent 1 or Instructed or Instructing Reimbursement Agent | Creditor Agent | Creditor |
|---|---|---|---|---|
| FinancialInstitutionCreditTransfer | | | | |
| FitOfIPaymentStatusReport | | | | |
| | FinancialInstitutionCreditTransfer | | | |
| | FitOfIPaymentStatusReport | | | |
| | | FinancialInstitutionCreditTransfer | | |
| | | FitOfIPaymentStatusReport | | |
| | PaymentReturn | | | |

For sake of simplicity only one intermediary agent has been added. The scenario covers the case where the creditor agent services an account for the intermediary agent.

In cases where the intermediary agent services an account for the creditor agent (including clearing payments where the intermediary agent is a central clearing and/or settlement agent), the creditor agent will inform about the non- processability of the instruction by using a PaymentReturn message.

The debtor sends the FinancialInstitutionCreditTransfer message to the debtor agent.

The debtor agent optionally confirms the processability of the FinancialInstitutionCreditTransfer instruction by sending a positive FitOfIPaymentStatusReport message to the debtor.

The debtor agent forwards the FinancialInstitutionCreditTransfer message to the intermediary agent.

The intermediary agent optionally confirms the processability of the FinancialInstitutionCreditTransfer instruction by sending a positive FitOfIPaymentStatusReport message to the debtor agent.

The intermediary agent forwards the FinancialInstitutionCreditTransfer message to the creditor agent.

The creditor agent sends a negative FitOfIPaymentStatusReport message to inform the intermediary agent about the non-processability of the FinancialInstitutionCreditTransfer instruction.

| Note | The intermediary agent might try to correct and re-submit the instruction and inform the debtor agent about this correction with an updated FitOfIPaymentStatusReport message. If Status is now positive, no further action is required, but the debtor agent might be informed on the positive outcome through a positive FitOfIPaymentStatusReport message. |
|---|---|

The intermediary agent sends a PaymentReturn message to the debtor agent.

| Note | The debtor agent might try to correct and re-submit the instruction and inform the debtor about this correction with an updated FitOfIPaymentStatusReport message. If Status is now positive, no further action is required, but the debtor might be informed on the positive outcome through a positive FitOfIPaymentStatusReport message. |
|---|---|

---

<!-- Page 42 -->

Out of Scope
- (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages)

## 6.1.7 PaymentReturn with FinancialInstitutionCreditTransfer

The PaymentReturn message is sent by an instructed agent to the previous party in the payment chain when a payment cannot be executed due to an administrative reason (for example, non existing/closed account) or banking reason (for example, insufficient funds).

### 6.1.7.1 Debtor and Creditor are direct Correspondents

A return is exchanged after settlement has taken place.

```
Debtor    Debtor Agent    Intermediary Agent 1 or Instructed or Instructing Reimbursement Agent    Creditor Agent    Creditor
   |           |                          |                          |               |
   |           |                          |                          |               |
   |           |                          |  FinancialInstitutionCreditTransfer      |
   |           |                          |-------------------------->               |
   |           |                          |                          |               |
   |           |                          |           PaymentReturn   |               |
   |           |                          |<--------------------------|               |
   |           |                          |                          |               |
   |           |                          |  FitToFIPaymentStatusReport              |
   |           |                          |-------------------------->               |
   |           |                          |                          |               |
```

The scenario covers the case where the debtor services an account for the creditor, that is, the creditor agent, and the case where the debtor and the creditor are linked through a payment clearing system.

For cases where the creditor services an account for the debtor, the creditor will inform about the non-processability of the instruction by using a negative FitToFIPaymentStatusReport (status Reject) message.

The debtor sends the FinancialInstitutionCreditTransfer message to the creditor.

The creditor sends a PaymentReturn message including the return reason to inform the debtor about the non-processability of the FinancialInstitutionCreditTransfer instruction (for example due to missing/incorrect information). In scope: The debtor optionally confirms the receipt of the PaymentReturn message by sending a positive FitToFIPaymentStatusReport message to the creditor.

**Out of Scope**
- Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages)

The case where the debtor and the creditor agent are correspondents is very similar. Therefore, it is not illustrated. The scenario would cover the case where the debtor services an account for the creditor agent and the case where the debtor and the creditor agent are linked through a clearing and settlement system.

If the creditor agent services an account for the debtor, the creditor agent will inform about the non-processability of the instruction by using a negative FitToFIPaymentStatusReport message to reject the instruction.

---

<!-- Page 43 -->

## 6.1.7.2 Debtor Agent and Creditor are Correspondents

The debtor agent and the creditor are correspondents. A return is exchanged after settlement has taken place.

| Debtor | Debtor Agent | Intermediary Agent 1 or Instructed or Instructing Reimbursement Agent | Creditor Agent | Creditor |
|---|---|---|---|---|
| FinancialInstitutionCreditTransfer → | | | | |
| ← FitOfIPaymentStatusReport | | | | |
| | FinancialInstitutionCreditTransfer → | | | |
| | ← PaymentReturn | | | |
| | FitOfIPaymentStatusReport → | | | |

The scenario covers the case where the debtor agent services an account for the creditor and where the debtor agent and the creditor are linked through a payment clearing system.

If the creditor services an account for the debtor agent, the creditor will inform about the non-processability of the instruction by using a negative FitOfIPaymentStatusReport (status Reject) message.

The debtor sends the FinancialInstitutionCreditTransfer message to the debtor agent.

The debtor agent optionally confirms the processability of the FinancialInstitutionCreditTransfer instruction by sending a positive FitOfIPaymentStatusReport message to the debtor.

The debtor agent forwards the FinancialInstitutionCreditTransfer message to the creditor.

If the debtor agent services an account for the creditor, that is, is the creditor agent, the debtor agent will send a BankToCustomerDebitCreditNotification ('notification') and/or BankToCustomerAccountReport/ BankToCustomerStatement ('statement') message instead of forwarding the FinancialInstitutionCreditTransfer message. In scope. The creditor sends a PaymentReturn message including the return reason to inform the debtor agent about the non-processability of the FinancialInstitutionCreditTransfer instruction (for example due to missing/incorrect information).

| Note | Whenever possible, the debtor agent might try to repair and re-submit the instruction. Depending on what has been agreed it may inform the debtor of the repair with an updated FitOfIPaymentStatusReport message. |
|---|---|

The debtor agent optionally confirms the receipt of the PaymentReturn message by sending a positive FitOfIPaymentStatusReport message to the creditor.

---

<!-- Page 44 -->

**Out of Scope**
- Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages)

### 6.1.7.3 Debtor Agent and Creditor Agent are Correspondents

A return is exchanged after settlement has taken place.

The scenario covers the case where the debtor agent services an account for the creditor agent and where the debtor agent and the creditor agent are linked through a payment clearing system.

If the creditor agent services an account for the debtor agent, the creditor agent will inform about the non-processability of the instruction by using a negative FitOfiPaymentStatusReport (status Reject) message.

The debtor sends the FinancialInstitutionCreditTransfer message to the debtor agent.

The debtor agent optionally confirms the processability of the FinancialInstitutionCreditTransfer instruction by sending a positive FitOfiPaymentStatusReport message to the creditor.

The debtor agent forwards the FinancialInstitutionCreditTransfer message to the creditor agent.

The creditor agent sends a PaymentReturn message to inform the debtor agent about the non-processability of the FinancialInstitutionCreditTransfer instruction (for example due to missing/incorrect information).

| Note | Whenever possible, the debtor agent might try to repair and re-submit the instruction. Depending on what has been agreed it may inform the debtor about the repair with an updated FitOfiPaymentStatusReport message. |
| :--- | :--- |

| **Out of Scope** | - Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages). |
| :--- | :--- |

### 6.1.7.4 Debtor Agent and Creditor Agent are Not Correspondents

A return is exchanged after settlement has taken place.

---

<!-- Page 45 -->

```markdown
Debtor | Debtor Agent | Intermediate Agent 1 or Instructed or Instructing Reimbursement Agent | Creditor Agent | Creditor

- FinancialInstitutionCreditTransfer
- FIToFIPaymentStatusReport
- FinancialInstitutionCreditTransfer
- FIToFIPaymentStatusReport
- FinancialInstitutionCreditTransfer
- PaymentReturn
- FIToFIPaymentStatusReport
- PaymentReturn
- FIToFIPaymentStatusReport

For sake of simplicity, only one intermediary agent has been added.

The scenario covers the case where the intermediary agent services an account for the creditor agent or the case where the intermediary agent and the creditor agent are linked through a payment clearing system.

If the creditor agent services an account for the intermediary agent, the creditor agent will inform about the non-processability of the instruction by using a negative FIToFIPaymentStatusReport (status Reject) message. In scope: The debtor sends the FinancialInstitutionCreditTransfer message to the debtor agent.

The debtor agent optionally confirms the processability of the FinancialInstitutionCreditTransfer instruction by sending a positive FIToFIPaymentStatusReport message to the debtor.

The debtor agent forwards the FinancialInstitutionCreditTransfer to the intermediary agent.

The intermediary agent optionally confirms the processability of the FinancialInstitutionCreditTransfer instruction by sending a positive FIToFIPaymentStatusReport message to the debtor agent.

The intermediary agent forwards the FinancialInstitutionCreditTransfer instruction to the creditor agent.

The creditor agent sends a PaymentReturn message including the return reason to inform the intermediary agent about the non-processability of the FinancialInstitutionCreditTransfer instruction (for example due to missing/ incorrect information).

| Note | Whenever possible, the intermediary agent might try to repair and re-submit the instruction. Depending on what has been agreed it may inform the debtor agent of the repair with an updated FIToFIPaymentStatusReport message. |
| :--- | :--- |

The intermediary agent optionally confirms the receipt of the PaymentReturn message by sending a positive FIToFIPaymentStatusReport message to the creditor agent.
```

---

<!-- Page 46 -->

The intermediary agent forwards the PaymentReturn message including the return reason to the debtor agent to inform the debtor agent about the non-processability of the FinancialInstitutionCreditTransfer instruction.



| Note | Whenever possible, the debtor agent might try to repair and re-submit the instruction. Depending on what has been agreed it may inform the debtor about the repair with an updated FIToFIPaymentStatusReport message. |
|---|---|

The debtor agent optionally confirms the receipt of the PaymentReturn message by sending a positive FIToFIPaymentStatusReport message to the intermediary agent.

**Out of Scope**
- Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages)

## 6.1.8 Debtor sends FIToFIPaymentStatusRequest

In the previous scenarios, the (optional) possibility of confirming the processability of the FinancialInstitutionCreditTransfer via a FIToFIPaymentStatusReport was always mentioned/included. In some schemes, especially referring to real-time payments, the receipt of this FIToFIPaymentStatusReport is crucial within a certain timeframe. In this case, if the FIToFIPaymentStatusReport is not received within the required timeframe, a reminder shall be launched by sending an FIToFIPaymentStatusRequest. The reply message to the FIToFIPaymentStatusRequest shall be a FIToFIPaymentStatusReport referring to the original payment instruction.

Debtor | Debtor Agent | Intermediary Agent 1 or Instructed or Instructing Reimbursement Agent | Creditor Agent | Creditor

FinancialInstitutionCreditTransfer

FIToFIPaymentStatusRequest

FIToFIPaymentStatusReport



| Note | Sending an FIToFIPaymentStatusRequest is possible in all FinancialInstitutionCreditTransfer scenarios described before (section 6.1.5, 6.1.6, 6.1.7), if no 'final' status is received yet in a FIToFIPaymentStatusReport message. |
|---|---|

## 6.2 Direct Debit

### 6.2.1 FIToFICustomerDirectDebit

A direct debit is a request for payment of an amount to be collected from a party bank account (the debtor account) by an originator (the creditor). The amounts and dates of collections may vary.

---

<!-- Page 47 -->

Direct debits result in cash transfers between debtor and creditor through infrastructures or correspondent banks. They may be exchanged as single instructions but are traditionally grouped following some common characteristics and, for convenience or efficiency reasons, exchanged in a batch mode.

Direct debits are processed in different ways from country to country, especially regarding the handling of the mandate (when it exists) given by the debtor to the creditor.

The CustomerDirectDebitInitiation message is sent by the initiating party (creditor) to the forwarding agent or creditor agent. It is used to request single or bulk collection(s) of cash from one or various debtor account(s) to a creditor. The CustomerDirectDebitInitiation is only shown in the diagram for information purpose. The focus of this document is on the interbank processing of the FitOfICustomerDirectDebit message.

The FitOfICustomerDirectDebit message is sent by a financial institution to another financial institution, directly or through a Clearing System. It is used to clear direct debit instructions, initiated by non-financial institution customers.

| Creditor | Creditor Agent | Clearing and Settlement Agent | Debtor Agent | Debtor |
|---|---|---|---|---|
| CustomerDirectDebitInitiation → | | | | |
| | FitOfICustomerDirectDebit → | | | |
| | | FitOfICustomerDirectDebit → | | |
| | | | FitOfICustomerDirectDebit → | |
| | | | (See note) | |

| Note | As added value to customers, some debtor agents send the instructions (simplified version) to their customers, the debtors, for example, if pre-notifications are not used in a scheme |
|---|---|

The original mandate between the debtor and the creditor and the mandate management itself are identified as being out of scope and are therefore not included in the diagram. Some information on possible mandate management information flow is available below.

The mandate is the authorisation/expression of consent given by the debtor, allowing a specified creditor to originate direct debit instructions to debit a specified debtor account in accordance with the relevant Direct Debit Scheme Rules and, if applicable, the mandate details.

A valid/authorised mandate represents the debtor agreement:

- to authorise the creditor to issue direct debit instruction(s) to the debtor account, and;

- to instruct the debtor agent to act upon the creditor direct debit instruction.

---

<!-- Page 48 -->

| Note | In some cases, the debtor agent is unaware of the Mandate and simply acts upon the direct debit instruction. A mandate can be an electronic mandate or a mandate in paper form. In case of a paper mandate the creditor dematerialises the mandate upon the mandate presentation in paper form. Dematerialised mandate data are referred to as the Mandate Related Information (MRI) only and are not to be considered as the mandate document. The original mandate remains subject for archiving and reference for any legal matter. |

Prior to the sending of a direct debit instruction, the creditor may notify the debtor of the amount and date on which the direct debit instruction will be presented to the debtor agent for debit. This notification may be sent together with or separately from other commercial documents (for example, an invoice).

There are two types of pre-notifications:

*   Schedule of payments for a number of subsequent direct debits for an agreed period of time.
*   Individual advices of a direct debit subject for collection on a specified value date only. In the case of a recurrent direct debit. This requires an update for each individual recurrent direct debit prior to its collection.

The debtor will reconcile the pre-notification with the signed/authorised mandate and where relevant other records (such as account payable items, contract details or subscription agreement). The debtor ensures the account is covered with subject amount.

The creditor sends the CustomerDirectDebitInitiation message to its agent (the creditor agent), together with the Mandate Related Information when requested by the scheme.

The creditor agent sends a FIToFICustomerDirectDebit message to the Clearing and settlement agent, in line with the clearing cycle. The Mandate Related Information (MRI) is also transported, when requested by the scheme.

The clearing and settlement agent send the FIToFICustomerDirectDebit message, together with the Mandate Related Information (MRI), when requested by the scheme, to the debtor agent.

The information provided includes the net position to be debited, the party to be debited, the net position to be credited, the party to be credited and the value date.

The settlement is executed by the settlement agent, in accordance with the settlement cycle, based on the settlement report provided by the clearing agent. The settlement agent performs the transfer of funds from the debtor agent to the creditor agent.

**Out of scope**

– The debtor agent could optionally forward the direct debit instruction (simplified version) to the debtor (for example, in case pre-notifications are not used in a Scheme).

– If clearing and settlement is carried out by two parties, the clearing agent prepares and sends the payment information for the settlement agent (in accordance with the agreed and published settlement cycle). The process includes the calculation of the settlement positions and transmission of the files to the settlement agent.

– Reporting (BankToCustomerDebitCreditNotification (notification) BankToCustomerAccountDebitReport and BankToCustomerStatement (statement) messages) to the debtor and creditors. Timing may vary depending on market practices and value added services provided by some agents that are before or after settlement.

## 6.2.2 FIToFIPaymentStatusReport with Direct Debit

The negative FIToFIPaymentStatusReport message is sent by the receiver of an instruction to inform the sender of the instruction about the negative processability of the instruction.

The negative FIToFIPaymentStatusReport message is to be sent before settlement. Indeed, after settlement, the correct message to be used is the PaymentReturn message.

---

<!-- Page 49 -->

## 6.2.2.1 CreditorNegative FIToFIPaymentStatusReport initiated by Clearing and Settlement Agent

A negative FIToFIPaymentStatusReport message is initiated by the clearing and settlement agent to reject an FIToFICustomerDirectDebit message.

Whenever possible the creditor agent will correct/complement the instruction and re-submit. Consequently he would not send a negative PaymentStatusReport to the creditor. However, depending on what has been agreed between the creditor and its agent, the creditor agent may inform its customer about the repair, for example, value date.

| Creditor | Creditor Agent | Clearing and Settlement Agent | Debtor Agent | Debtor |
|---|---|---|---|---|
| CustomerDirectDebitInitiation | | | | |
| CustomerPaymentStatusReport | | | | |
| | FIToFICustomerDirectDebit | | | |
| | FIToFIPaymentStatusReport | | | |
| Information* | | | | |

\* Information: If the creditor agent books after collection, for example, the cycle is 3 days, then the CustomerPaymentStatusReport message is to be used. If the creditor agent books immediately and the instruction is rejected in the interbank leg, then the creditor needs to be informed of a payment return

The creditor sends the CustomerDirectDebitInitiation message to its agent (the creditor agent).

The creditor agent confirms the processability of the CustomerDirectDebitInitiation instruction by sending a positive CustomerPaymentStatusReport message to the creditor.

The creditor agent sends an FIToFICustomerDirectDebit message to the clearing and settlement agent, in line with the clearing cycle. The Mandate Related Information (MRI) is also transported, when applicable.

If information is missing and inter-bank settlement has not taken place yet, the clearing and settlement agent informs the creditor agent about the non processability of the FIToFICustomerDirectDebit instruction. The creditor agent may inform its customer, the creditor, about the negative processing of the CustomerDirectDebitInitiation instruction by using a negative CustomerPaymentStatusReport message, a BankToCustomerDebitCreditNotification message ('notification') or through a BankToCustomerAccountReport/BankToCustomerStatement message ('statement').

| Note | Before sending a negative CustomerPaymentStatusReport message to its customer, it is assumed that the creditor agent will try to correct the CustomerDirectDebitInitiation message information and re-submit an FIToFICustomerDirectDebit message to the clearing and settlement agent. In this case the creditor will not be involved. |
|---|---|

---

<!-- Page 50 -->

## 6.2.2.2 Negative FiToFIPaymentStatusReport Initiated by Debtor Agent

A negative FiToFIPaymentStatusReport message is initiated by the debtor agent to reject the FiToFiCustomerDirectDebit message. (After settlement the correct message to be used by the debtor agent is the PaymentReturn message.

Whenever possible the creditor agent will correct/complement the instruction and re-submit. Consequently he would not send a negative CustomerPaymentStatusReport to the creditor. However, depending on what has been agreed between the creditor and its agent, the creditor agent may inform its customer about the repair, for example, value date.

| Creditor | Creditor Agent | Clearing and Settlement Agent | Debtor Agent | Debtor |
|---|---|---|---|---|
| CustomerDirectDebitInitiation → | | | | |
| ← CustomerPaymentStatusReport | | | | |
| | → FiToFiCustomerDirectDebit | | | |
| | ← FiToFIPaymentStatusReport | | | |
| | | → FiToFiCustomerDirectDebit | | |
| | | ← FiToFIPaymentStatusReport | | |
| | ← FiToFIPaymentStatusReport | | | |
| ← Information* | | | | |

\* Information: If the creditor agent books after collection, for example, the cycle is 3 days, then the CustomerPaymentStatusReport message is to be used. If the creditor agent books immediately and the instruction is rejected in the interbank leg, then the creditor needs to be informed of a payment return.

The creditor sends a CustomerDirectDebitInitiation message to its agent (the creditor agent).

The creditor agent confirms the processability of the CustomerDirectDebitInitiation instruction by sending a CustomerPaymentStatusReport message to the creditor.

The creditor agent sends an FiToFiCustomerDirectDebit message to the clearing and settlement agent, in line with the clearing cycle. The Mandate Related Information (MRI) is also transported, when applicable.

The clearing and settlement agent confirms the processability of the FiToFiCustomerDirectDebit instruction by sending an FiToFIPaymentStatusReport message to the creditor agent.

The clearing and settlement agent sends an FiToFiCustomerDirectDebit message, optionally with the Mandate Related Reference (MRI) to the debtor agent immediately for information purposes only.

---

<!-- Page 51 -->

If settlement has not yet taken place, the debtor agent may send a negative FIToFIPaymentStatusReport message to the clearing and settlement agent, to inform it about the rejection of the FIToFICustomerDirectDebit instruction. This negative FIToFIPaymentStatusReport message may subsequently be forwarded to the creditor agent. The creditor agent may inform its customer, the creditor, about the negative processing of the CustomerDirectDebitInitiation instruction by using a CustomerPaymentStatusReport message, a BankToCustomerDebitCreditNotification message ('notification') or through a BankToCustomerAccountReport/ BankToCustomerStatement message ('statement').

## 6.2.3 Positive FI To FI Payment Status Report with Direct Debit

The positive FIToFIPaymentStatusReport message is sent by the receiver of an instruction to inform the receiver that the instruction received (either single or grouped) is processable.

A positive FIToFIPaymentStatusReport message can also be used to confirm the processability of a PaymentReturn message or an FIToFIPaymentReversal message.

The positive FIToFIPaymentStatusReport message is also meant to be generic to ensure re-usability with other Payments Instruments.

The FIToFIPaymentStatusReport messages are exchanged, point to point between two parties, optionally and as per bilateral agreements and may be complemented by an BankToCustomerDebitCreditNotification message ('notification') and/or BankToCustomerAccountReport/BankToCustomerStatement message ('statement').

```
 Creditor       Creditor Agent    Clearing and Settlement Agent    Debtor Agent       Debtor
    |               |                     |                            |                |
    | CustomerDirectDebitInitiation       |                            |                |
    |------------------------------------>|                            |                |
    |               |                     |                            |                |
    | CustomerPaymentStatusReport         |                            |                |
    |<------------------------------------|                            |                |
    |               |                     |                            |                |
    |               | FIToFICustomerDirectDebit                        |                |
    |               |------------------------------------->|           |                |
    |               |                     |                            |                |
    |               | FIToFIPaymentStatusReport              |         |                |
    |               |<------------------------------------|           |                |
    |               |                     |                            |                |
    |               |                     | FIToFICustomerDirectDebit  |                |
    |               |                     |--------------------------->|                |
    |               |                     |                            |                |
    |               |                     | FIToFIPaymentStatusReport  |                |
    |               |                     |<---------------------------|                |
    |               |                     |                            |                |
    |               |                     |                            |                |
```

- The positive CustomerPaymentStatusReport and FIToFIPaymentStatusReport messages are optional.

- As added value service to creditors, some banks may update CustomerPaymentStatusReport messages to inform creditors about the status of transactions during their lifecycle.

- Mixed CustomerPaymentStatusReport and FIToFIPaymentStatusReport messages may be exchanged, that is, 'partially accepted' on group level, indicated that the group contains a mix of accepted, pending and/or rejected transactions.

---

<!-- Page 52 -->

## 6.2.3.1 **FitToFiPaymentStatusReport to confirm Processability of FitToFiCustomerDirectDebit instruction**

In this scenario, the FitToFiPaymentStatusReport message is used to confirm the processability of a FitToFiCustomerDirectDebit instruction.

The creditor agent sends an FitToFiCustomerDirectDebit message to the clearing and settlement agent, in line with the clearing cycle. The Mandate Related Information (MRI) is also transported, when applicable.

The clearing and settlement agent confirms the processability of the FitToFiCustomerDirectDebit instruction by sending a positive FitToFiPaymentStatusReport message to the creditor agent.

The clearing and settlement agent sends an FitToFiCustomerDirectDebit message, together with potentially the Mandate Related Information (MRI) to the debtor agent immediately for information purposes only.

The debtor agent sends a positive FitToFiPaymentStatusReport message to the clearing and settlement agent. This positive status message may subsequently be forwarded to the creditor agent.

## 6.2.4 **PaymentReturn with Direct Debit**

A PaymentReturn message is initiated by the debtor agent and sent to the previous party in the payment chain when a debit cannot be executed due to an administrative reason (for example non existing/closed account) or due to a banking reason (for example insufficient funds).

The PaymentReturn message is also the message to be used by the debtor agent following the receipt of a refund request by the debtor (out of scope) as it is assumed that the refund request will be done through a non-automated tool (for example phone/fax) and is not part of the scope.

In this case, the PaymentReturn message will contain a code to indicate that it is triggered by a request for refund by the debtor.

### 6.2.4.1 **PaymentReturn Initiated by Debtor Agent**

If booking of the original instruction on the creditor account has already taken place, the return of funds will be notified to the creditor through return information included in the BankToCustomerNotification message (notification) and/or the BankToCustomerAccountReport or the BankToCustomerStatement message (Statement).

---

<!-- Page 53 -->

# Creditor

# Creditor Agent

# Clearing and Settlement Agent

# Debtor Agent

# Debtor

CustomerDirectDebitInitiation

CustomerPaymentStatusReport

FitOfiCustomerDirectDebit

FitOfiPaymentStatusReport

FitOfiCustomerDirectDebit

FitOfiPaymentStatusReport

RefundRequest

PaymentReturn

FitOfiPaymentStatusReport

PaymentReturn

FitOfiPaymentStatusReport

The creditor initiates the direct debit (for example by sending) the CustomerDirectDebitInitiation message to its agent (the creditor agent).

The creditor agent confirms the processability of the instruction by sending for example a positive CustomerPaymentStatusReport to the creditor.

The creditor agent sends a FitOfiCustomerDirectDebit message to the clearing and settlement agent, in line with the clearing cycle. The Mandate Related Information (MRI) is also transported, when applicable.

The clearing and settlement agent confirms the processability of the FitOfiCustomerDirectDebit instruction by sending a positive FitOfiPaymentStatusReport message to the creditor agent.

The clearing and settlement agent sends an FitOfiCustomerDirectDebit message, together with potentially the Mandate Related Reference (MRI) to the debtor agent immediately for information purposes only.

The debtor agent sends a positive FitOfiPaymentStatusReport message to the clearing and settlement agent.

If the debtor agent is unable to make the collection from the debtor Account for one or several reasons (insufficient funds, customer deceased...), It will initiate a PaymentReturn message, and route it through the clearing and settlement agent to the creditor agent, giving the reason for the Return.

The clearing and settlement agent optionally confirms the receipt of the PaymentReturn message by sending a positive FitOfiPaymentStatusReport message to the debtor agent.

The clearing and settlement agent forwards the PaymentReturn message to the creditor agent.

---

<!-- Page 54 -->

If clearing and settlement is carried out by two parties, the clearing agent prepares the (returned) payment information for the settlement agent (the net position to be debited, the party to be debited, the net position to be credited, the party to be credited and the value date) in accordance with the agreed and published settlement cycle. The settlement agent performs the transfer of cash from the credit party to the debit party (in accordance with the agreed published settlement cycle). (Out of scope and not illustrated).

The creditor agent may, optionally, confirm receipt of the PaymentReturn message to the clearing agent. Depending on agreements between the creditor and the creditor agent, the creditor may be informed either through a negative CustomerPaymentStatusReport message, or through a BankToCustomerDebitCreditNotification message ('notification') and/or BankToCustomerAccountReport/BankToCustomerStatement message ('statement') about the funds return and thus the debit on its account.

## 6.2.4.2 Refund by the Debtor

(The PaymentReturn process can be triggered by refund request by the debtor or initiated by the debtor agent).

This scenario is similar to the previous scenario, except that the PaymentReturn instruction by the debtor agent to the clearing and settlement agent is triggered by a Refund Request by the debtor to its agent, the debtor agent (in a non-automated manner). In this case, the PaymentReturn message will contain a code indicating that it was triggered by a request for refund by the debtor.

## 6.2.5 FIToFIPaymentReversal with Direct Debit

The creditor can initiate a CustomerPaymentReversal message, after settlement, when a paid direct debit should not have been processed.

The creditor agent will, in turn, initiate a FIToFIPaymentReversal for the next agent in the payment chain. Consequently, the debtor will be credited.

| Note | The creditor agent may be the originator of a payment reversal - it will in this case initiate a FIToFIPaymentReversal message. |
|---|---|

The creditor sends (for example) a CustomerDirectDebitInitiation message to its agent (the creditor agent). (Only potential messages, part of the direct debit scope are illustrated in the sequence diagram).

---

<!-- Page 55 -->

Creditor | Creditor Agent | Clearing and Settlement Agent | Debtor Agent | Debtor
---|---|---|---|---
CustomerDirectDebitInitiation | | | |
CustomerPaymentStatusReport | | | |
| FitOfICustomerDirectDebit | | |
| FitOfPaymentStatusReport | | |
| | FitOfICustomerDirectDebit | |
| | FitOfPaymentStatusReport | |
CustomerPaymentReversal | | | |
CustomerPaymentStatusReport | | | |
| FitOfPaymentReversal | | |
| FitOfPaymentStatusReport | | |
| | FitOfPaymentReversal | |
| | FitOfPaymentStatusReport | |

The creditor agent can confirm the processability of the CustomerDirectDebitInitiation instruction by sending a positive CustomerPaymentStatusReport message to the creditor.

The creditor agent sends a FitOfICustomerDirectDebit message to the clearing and settlement agent, in line with the clearing cycle. The Mandate Related Information (MRI) is also transported, when applicable.

The clearing and settlement agent confirms the processability of the FitOfICustomerDirectDebit instruction by sending a positive FitOfIPaymentStatusReport message to the creditor agent.

The clearing and settlement agent sends an FitOfICustomerDirectDebit message, together with potentially the Mandate Related Information (MRI) to the debtor agent immediately for information purposes only.

The debtor agent sends a positive FitOfIPaymentStatusReport message to the clearing and settlement agent. The creditor realises this was a duplicated CustomerDirectDebitInitiation instruction. It now wants to send a CustomerPaymentReversal message. It identifies the original CustomerDirectDebitInitiation message (or a file of direct debit instructions) and generates an offsetting transaction in favour of the debtor, under the quotation of the reversal reasons. The creditor agent may confirm the receipt of the CustomerPaymentReversal message by sending a positive CustomerPaymentStatusReport message to the creditor.

An FitOfIPaymentReversal message is submitted by the creditor agent to the clearing and settlement agent for settlement, under quotation of the original direct debit reference and the reason for the reversal for example, in case of duplicated direct debit instruction.

---

<!-- Page 56 -->

The clearing agent confirms the processability of the reversal by sending a positive FIToFIPaymentStatusReport message to the creditor agent.

The clearing and settlement agent forwards the FIToFIPaymentReversal message to the debtor agent immediately for information purposes only.

If clearing and settlement is carried out by two parties, the clearing agent prepares the payment information for the settlement agent (in accordance with the agreed and published settlement cycle). That process includes the calculation of the settlement positions.

The information provided to the settlement agent is the net position to be debited, the party to be debited, the net position to the credited, the party to be credited and the value date (Out of Scope).

The settlement agent performs the transfer of funds from the credit party to the debit party (in accordance with the agreed and published settlement cycle) (out of scope).

A positive FIToFIPaymentStatusReport message can optionally be initiated by the debtor agent and sent to the clearing and settlement agent to confirm the processability of the reversal message.



| Note | It may exceptionally occur that a PaymentReturn message and an FIToFIPaymentReversal message would cross each other, but this could only be avoided through value-added monitoring services that could be offered by the scheme manager and/or might provoke exceptions/investigation handling. |
|---|---|

## 6.2.6 Creditor Agent sends FIToFIPaymentStatusRequest

In the previous scenarios, the (optional) possibility of confirming the processability of the FIToFICustomerDirectDebit via a FIToFIPaymentStatusReport was always mentioned/included. In some payment schemes, especially referring to real-time payments, the receipt of this FIToFIPaymentStatusReport is crucial within a certain timeframe. In this case, if the FIToFIPaymentStatusReport is not received within the required timeframe, a reminder shall be launched by sending an FIToFIPaymentStatusRequest. The reply message to the FIToFIPaymentStatusRequest shall be a FIToFIPaymentStatusReport referring to the original payment instruction.

| Creditor Agent | Clearing and Settlement Agent | Debtor Agent | Debtor |
|---|---|---|---|
| FIToFICustomerDirectDebit → | | | |
| FIToFIPaymentStatusRequest → | | | |

---

<!-- Page 57 -->

| **Note** | Sending an FIToFIPaymentStatusRequest is possible in all FinancialInstitutionCreditTransfer scenarios described before (section 6.2.2, 6.2.3, 6.2.4, 6.2.5), if no 'final' status is received yet in a FIToFIPaymentStatusReport message. |
|---|---|

## 6.2.7 FinancialInstitutionDirectDebit

A FinancialInstitutionDirectDebit message is the interbank instruction to collect an amount via direct debit from (one or more) party bank account(s) (the Debtor Account(s)) in favour of one or more beneficiary party(ies) (the creditor(s)) where all parties are financial institutions.

FinancialInstitutionDirectDebits result in cash transfers between Debtor(s) and creditor(s) in the books of the debtor agent or through correspondent banks.

If there are different transactions, they can be grouped per creditor in a CreditInstruction, but one message can potentially contain multiple credit instructions for different creditors.

This is represented in the message by putting the creditor and debtor details on a different level (CreditInstruction block can contain multiple DirectDebitTransactionInformation blocks). This makes the FinancialInstitutionDirectDebit message different from the other (pacs) messages in this business area, but is necessary to have the equivalent of the MT 204 (allowing for 1 beneficiary institution, but multiple debit institutions).

The FinancialInstitutionDirectDebit message is sent to the debtor agent. It is used to clear direct debit instructions, initiated by a financial institution creditor.

### 6.2.7.1 Creditor and Debtor Agent are correspondents

The scenario covers the case where the debtor agent services an account for the creditor and for the debtor(s). For sake of simplicity, only 1 Debtor is represented in the sequence diagram.

![Sequence diagram: Creditor Exchange or Clearing House, Creditor Agent, IntermediaryAgent, Debtor Agent, Debtor, with messages FinancialInstitutionDirectDebit and FIToFIPaymentStatusReport](image)

The creditor sends the FinancialInstitutionDirectDebit message to the debtor agent. Creditor and debtor agent are correspondents in the currency of the transaction and by sending the message the creditor requests to credit the amount on his account with the debtor agent.

The debtor agent (optionally) confirms the processability of the FinancialInstitutionDirectDebit by sending a positive FIToFIPaymentStatusReport.

**Out of Scope**

- Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages).
- Some debtor agents potentially send the instruction to the debtor(s) for information (and value added) services. (Pre)Notifications are not included.
- The mandate/agreements related to the direct debit flows are not taken into account for the purpose of this document.

---

<!-- Page 58 -->

If the FinancialInstitutionDirectDebit cannot be processed by the debtor agent, a negative FIToFIPaymentsStatusReport message is sent back to the creditor before settlement.

## 6.2.7.2 Creditor Agent and Debtor Agent are correspondents

The scenario covers the case where the creditor has the authority to request Direct Debits to the debtor agent in the currency of the transaction, but requests to move the funds to an account the creditor owns at another bank (the creditor agent).

The creditor requests with a FinancialInstitutionDirectDebit message to move the amount(s) to the account with the creditor agent. This creditor agent and the debtor agent are correspondents in the currency of the transaction(s).

The debtor agent (optionally) confirms the processability of the FinancialInstitutionDirectDebit by sending a positive FIToFIPaymentStatusReport.

The debtor agent sends the FinancialInstitutionCreditTransfer to the creditor agent to move the funds to the creditor.

The creditor agent (optionally) confirms the processability of the FinancialInstitutionCreditTransfer by sending a positive FIToFIPaymentStatusReport.

### Out of Scope

- Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages).
- Some debtor agents potentially send the instruction to the debtor(s) for information (and value added) services. (Pre)Notifications are not included.
- The mandate/agreements related to the direct debit flows are not taken into account for the purpose of this document.

If the FinancialInstitutionDirectDebit cannot be processed by the debtor agent, a negative FIToFIPaymentsStatusReport message is sent back to the creditor before settlement and no FinancialInstitutionCreditTransfer will be sent to the creditor agent.

## 6.2.7.3 Creditor Agent and Debtor Agent are not correspondents

The scenario covers the case where the creditor has the authority to request direct debits to the debtor agent in the currency of the transaction(s), but requests to move the funds to an account the creditor owns at another bank (the creditor agent). The debtor agent and the creditor agent are not correspondents in the currency of the transaction(s), but have a common correspondent (the intermediary agent).

---

<!-- Page 59 -->

Although the FinancialInstitutionDirectDebit allows for multiple intermediary agents, for sake of simplicity only one intermediary agent has been illustrated.

| Creditor Exchange or Clearing House | Creditor Agent | Intermediary Agent | Debtor Agent | Debtor |
|---|---|---|---|---|
| | | | FinancialInstitutionDirectDebit | |
| | | | FitOfPaymentStatusReport | |
| | | | FinancialInstitutionCreditTransfer | |
| | | | FitOfPaymentStatusReport | |
| | | FinancialInstitutionCreditTransfer | | |
| | | FitOfPaymentStatusReport | | |

The creditor sends the FinancialInstitutionDirectDebit message to the debtor agent to request the move of funds to his account with the creditor agent, through an intermediary agent.

The debtor agent (optionally) confirms the processability of the FinancialInstitutionDirectDebit by sending a positive FitOfPaymentStatusReport.

The debtor agent sends the FinancialInstitutionCreditTransfer to the intermediary agent to move the funds to the creditor.

The intermediary agent optionally confirms the processability of the FinancialInstitutionTransfer by sending a positive FitOfPaymentStatusReport message to the debtor agent.

The intermediary agent forwards the FinancialInstitutionCreditTransfer message to the creditor agent.

The creditor agent optionally confirms the processability of the FinancialInstitutionCreditTransfer instruction by sending a positive FitOfPaymentStatusReport message.

**Out of Scope**
- Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages).
- Some debtor agents potentially send the instruction to the debtor(s) for information (and value added) services. (Pre)Notifications are not included.
- The mandate/agreements related to the direct debit flows are not taken into account for the purpose of this document.

If the FinancialInstitutionDirectDebit cannot be processed by the debtor agent, a negative FitOfPaymentStatusReport message is sent back to the creditor before settlement and no FinancialInstitutionCreditTransfer will be sent to the intermediary agent.

### 6.2.7.4 Payment Return in a FinancialInstitutionDirectDebit scenario

The scenario covers the case where the creditor has the authority to request direct debits to the debtor agent in the currency of the transaction(s), but creditor (nor creditor agent) and debtor agent are not correspondents in the currency of the transaction(s). For sake of simplicity only one intermediary agent has been illustrated.

---

<!-- Page 60 -->

| Creditor Exchange or Clearing House | Creditor Agent | IntermediaryAgent | Debtor Agent | Debtor |
|---|---|---|---|---|
| | FinancialInstitutionDirectDebit | | | |
| | FitOfIPaymentStatusReport | | | |
| | | FinancialInstitutionCreditTransfer | | |
| | | FitOfIPaymentStatusReport | | |
| | FinancialInstitutionCreditTransfer | | | |
| | FitOfIPaymentStatusReport | | | |
| | | PaymentReturn | | |
| | | FitOfIPaymentStatusReport | | |
| | FitOfIPaymentStatusReport | | | |

The creditor sends the FinancialInstitutionDirectDebit message to the debtor agent to request the move of funds to his account with the creditor agent, through an intermediary agent.

The debtor agent (optionally) confirms the processability of the FinancialInstitutionDirectDebit by sending a positive FitOfIPaymentStatusReport.

The intermediary agent forwards the FinancialInstitutionCreditTransfer message to the creditor agent.

The creditor agent cannot process the FinancialInstitutionCreditTransfer and sends a negative FitOfIPaymentStatusReport message to the intermediary agent.

If the settlement had already taken place, the intermediary agent sends a PaymentReturn message to the debtor agent.

The debtor agent optionally confirms the processability of the PaymentReturn message by sending a positive FitOfIPaymentStatusReport message to the intermediary agent.

The debtor agent optionally informs the creditor with a negative FitOfIPaymentStatusReport message.

| Note | Whenever possible, the intermediary agent or debtor agent might try to repair and re-submit the instruction and may inform the creditor agent with an updated FitOfIPaymentStatusReport. |
|---|---|

## Out of Scope

- Reporting (BankToCustomerDebitCreditNotification ('notification'), BankToCustomerAccountReport and BankToCustomerStatement ('statement') messages).
- Some debtor agents potentially send the instruction to the debtor(s) for information (and value added) services. (Pre)Notifications are not included.
- The mandate/agreements related to the direct debit flows are not taken into account for the purpose of this document.

---

<!-- Page 61 -->

## 6.2.7.5 FitOfIPaymentReversal with Direct Debit

After the scenario described in 6.2.6.1, the creditor may realises (for example) that the FinancialInstitutionDirectDebit instruction was a duplicate.

| Creditor Exchange or Clearing House | Creditor Agent | IntermediaryAgent | Debtor Agent | Debtor |
|---|---|---|---|---|
| → FinancialInstitutionDirectDebit | | | | |
| ← FitOfIPaymentStatusReport | | | | |
| → FitOfIPaymentReversal | | | | |
| ← FitOfIPaymentStatusReport | | | | |

The creditor can initiate an FitOfIPaymentReversal message, after settlement, when a paid direct debit should not have been processed.

The debtor agent can confirm the processability of the FitOfIPaymentReversal by sending a positive FITFIPaymentsStatusReport to the creditor.

## 6.2.7.6 Creditor sends FitOfIPaymentStatusRequest

In the previous scenarios, the (optional) possibility of confirming the processability of the FinancialInstitutionDirectDebit via a FitOfIPaymentStatusReport was always mentioned/included. In some payment schemes, especially referring to real-time payments, the receipt of this FitOfIPaymentStatusReport is crucial within a certain timeframe. In this case, if the FitOfIPaymentStatusReport is not received within the required timeframe, a reminder shall be launched by sending an FitOfIPaymentStatusRequest. The reply message to the FitOfIPaymentStatusRequest shall be a FitOfIPaymentStatusReport referring to the original payment instruction.

| Creditor | Creditor Agent | Clearing and Settlement Agent | Debtor Agent | Debtor |
|---|---|---|---|---|
| → FinancialInstitutionDirectDebit | | | | |
| → FitOfIPaymentStatusRequest | | | | |

| Note | Sending an FitOfIPaymentStatusRequest is possible in all FinancialInstitutionCreditTransfer scenarios described before (section 6.2.7.2, 6.2.7.2, 6.2.7.3, 6.2.7.4), if no final status is received yet in a FitOfIPaymentStatusReport message. |
|---|---|

---

<!-- Page 62 -->

# 7 Business Examples

## 7.1 FIToFIPaymentStatusReport pacs.002.001.15

**Description**

On 28 June 2015, ABABUS23 received a FIToFICustomerDirectDebit message from AAAAUS29. On 29 June 2015, ABABUS23 rejects the FIToFICustomerDirectDebit message by sending a FIToFIPaymentStatusReport message to AAAAUS29, referring to the original instruction and indicating the reason for the rejection.

**Related Message Examples**

The FIToFICustomerDirectDebit instruction from AAAAUS29 to ABABUS23 is included in the business example section of the FIToFICustomerDirectDebit message.

As AAAAUS29 has not yet credited the account of its customer, Virgay, in turn, AAAAUS29 will send a CustomerPaymentStatusReport to inform Virgay of the rejection. This example is included in the business example section of the PaymentStatusReport message in the Payments Initiation Message Reference Guide.

**Business Data**

PaymentStatusReport from ABABUS23 to AAAAUS29:



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
      <td>ABABUS23-STATUS-456/04</td>
    </tr>
    <tr>
      <td>CreationDateTime</td>
      <td>&lt;CreDtTm&gt;</td>
      <td>2015-06-29T09:56:00</td>
    </tr>
    <tr>
      <td>InstructingAgent</td>
      <td>&lt;InstdAg&gt;</td>
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
      <td>ABABUS23</td>
    </tr>
    <tr>
      <td>InstructedAgent</td>
      <td>&lt;InstdAg&gt;</td>
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
      <td>OriginalGroupInformationAndStatus</td>
      <td>&lt;OrgnlGrpInfAndSts&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>OriginalMessageIdentification</td>
      <td>&lt;OrgnlMsgId&gt;</td>
      <td>AAAA100628-123v</td>
    </tr>
    <tr>
      <td>OriginalMessageNameIdentification</td>
      <td>&lt;OrgnlMsgNmId&gt;</td>
      <td>pacs.003.001.11</td>
    </tr>
    <tr>
      <td>OriginalCreationDateTime</td>
      <td>&lt;OrgnlCreDtTm&gt;</td>
      <td>2015-06-28T10:05:00</td>
    </tr>
    <tr>
      <td>TransactionInformationAndStatus</td>
      <td>&lt;TxInfAndSts&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>StatusIdentification</td>
      <td>&lt;StsId&gt;</td>
      <td>AB/8568</td>
    </tr>
    <tr>
      <td>OriginalEndToEndIdentification</td>
      <td>&lt;OrgnlEndToEndId&gt;</td>
      <td>VA060327/0123</td>
    </tr>
    <tr>
      <td>OriginalTransactionIdentification</td>
      <td>&lt;OrgnlTxId&gt;</td>
      <td>AAAAUS29/100628/ad458</td>
    </tr>
    <tr>
      <td>TransactionStatus</td>
      <td>&lt;TxSts&gt;</td>
      <td>RJCT</td>
    </tr>
    <tr>
      <td>StatusReasonInformation</td>
      <td>&lt;StsRsnInf&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>Originator</td>
      <td>&lt;Orgtr&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>Identification</td>
      <td>&lt;Id&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>OrganisationIdentification</td>
      <td>&lt;OrgId&gt;</td>
      <td></td>
    </tr>
  </tbody>
</table>

---

<!-- Page 63 -->

| Element | XMLTag | Content |
| :--- | :--- | :--- |
| AnyBIC | <AnyBIC> | ABABUS23 |
| Reason | <Rsn> | |
| Code | <Cd> | AM05 |
| OriginalTransactionReference | <OrgnlTxRef> | |
| InterbankSettlementAmount | <RtrdIntrBkSttlmAmt> | USD 1025 |
| InterbankSettlementDate | <IntrBkSttlmDt> | 2015-06-28 |
| RequestedCollectionDate | <ReqdColltnDt> | 2015-07-13 |
| MandateRelatedInformation | <MndtRltdInf> | |
| MandateIdentification | <MndtId> | VIRGAY123 |
| DirectDebitMandate | <DrctDbtMndt> | |
| Debtor | <Dbtr> | |
| Name | <Nm> | Jones |
| PostalAddress | <PstlAdr> | |
| StreetName | <StrtNm> | Hudson Street |
| BuildingNumber | <BldgNb> | 19 |
| PostCode | <PstCd> | NJ 07302 |
| TownName | <TwnNm> | Jersey City |
| Country | <Ctry> | US |
| Creditor | <Cdtor> | Virgay |
| Name | <Name> | |
| PostalAddress | <PstlAdr> | |
| StreetName | <StrtNm> | Virginia Lane |
| BuildingNumber | <BldgNb> | 36 |
| PostCode | <PstCd> | NJ 07311 |
| TownName | <TwnNm> | Jersey City |
| Country | <Ctry> | US |

## Message Instance

```xml
<FitpFIPmtStsRpt>
    <GrpHdr>
        <MsgId>ABABUS23-STATUS-456/04</MsgId>
        <CreDtTm>2015-06-29T09:56:00</CreDtTm>
        <InstgAgt>
            <FinInstnId>
                <BICFI>ABABUS23</BICFI>
            </FinInstnId>
        </InstgAgt>
        <InstdAgt>
            <FinInstnId>
                <BICFI>AAA AUS29</BICFI>
```

---

<!-- Page 64 -->

```xml
</FinInstmId>
</InstdAgt>
</GrpHdr>
<OrgnlGrpInfAndSts>
    <OrgnlMsgId>AAAA100628-123v</OrgnlMsgId>
    <OrgnlMsgNmId>pac.003.001.11</OrgnlMsgNmId>
    <OrgnlCredTm>2015-06-28T10:05:00</OrgnlCredTm>
</OrgnlGrpInfAndSts>
<TxInfAndSts>
    <StsId>AB/8568</StsId>
    <OrgnlEndToEndId>VA060327/0123</OrgnlEndToEndId>
    <OrgnlTxId>AAAAUS29/100628/ad458</OrgnlTxId>
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
    </StsRsnInf>
    <OrgnlTxRef>
        <IntrBkSttlmAmt Ccy="USD">1025</IntrBkSttlmAmt>
        <IntrBkSttlmDt>2015-06-28</IntrBkSttlmDt>
        <ReqdCollnDt>2015-07-13</ReqdCollnDt>
        <MndtRltdInf>
            <DrctDbtMndt>
                <MndId>VIRGAY123</MndId>
            </DrctDbtMndt>
        </MndtRltdInf>
        <Dbtr>
            <Pty>
                <Nm>Jonese</Nm>
                <PstlAdr>
                    <StrtNm>Hudson Street</StrtNm>
```

---

<!-- Page 65 -->

```xml
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
</FIFoFiPmtStsRpt>
```

## 7.2 FitOFI CustomerDirectDebit pacs.003.001.11

### Description

On 28 June 2015, following the receipt of a CustomerDirectDebitInitiation message from its customer Virgay, AAAAUS29 in its turn sends an FitOFICustomerDirectDebit message to ABABUS23, the common correspondent for AAAAUS29 and BBBBUS39, the agent of debtor Jones.

AAAAUS29 instructs ABABUS23, under Service Level CTRV - 356, to collect USD 1025 from account 123456, owned by Jones, the debtor, and serviced by BBBBUS39. The mandate related information is also provided: the mandate reference is VIRGAY123 and the mandate was signed by Jones on 13 July 2008. The last collection is due to take place on 13 July 2015. The payment is for life insurance. The requested collection date is 13 July 20102 and charges related to the handling of the instruction are shared between the creditor and the debtor.



| Note | The CustomerDirectDebitInitiation instruction sent by Virgay to AAAAUS29 is documented in the business example section of the CustomerDirectDebitInitiation message in the Payments Initiation Message Reference Guide. |
| :--- | :--- |

### Business Data

FitOFICustomerDirectDebit from AAAAUS29 to ABABUS23:

---

<!-- Page 66 -->

| Element | <XMLTag> | Content |
|---|---|---|
| Group Header | <GrpHdr> | |
| MessageIdentification | <MsgId> | AAAA100628-123v |
| CreationDateTime | <CreDtTm> | 2015-06-28T10:05:00 |
| NumberOfTransactions | <NbOfTxs> | 1 |
| InterbankSettlementDate | <IntrBkSttlmDt> | 2015-06-28 |
| Settlement Information | <SttlmInf> | |
| Settlement Method | <SttlmMtd> | INDA |
| PaymentTypeInformation | <PmtTpInf> | |
| InstructionPriority | <InstrPrty> | NORM |
| ServiceLevel | <SvcLvl> | |
| Proprietary | <Prtry> | CTRV-356 |
| SequenceType | <SeqTp> | RCUR |
| InstructingAgent | <InstgAgt> | |
| FinancialInstitutionIdentification | <FinInstnId> | |
| BICFI | <BICFI> | AAAAUS29 |
| InstructedAgent | <InstdAgt> | |
| FinancialInstitutionIdentification | <FinInstnId> | |
| BICFI | <BICFI> | ABABUS23 |
| DirectDebitTransactionInformation | <DrctDbtTxInf> | |
| Payment Identification | <PmtId> | |
| EndToEndIdentification | <EndToEndId> | VA060713/0123 |
| Transaction Identification | <TxId> | AAAAUS29/100628/ad458 |
| InterbankSettlementAmount | <IntrBkSttlmAmt> | USD 1025 |
| InstructedAmount | <InstdAmt> | USD 1025 |
| ChargeBearer | <ChrgBr> | SHAR |
| RequestedCollectionDate | <ReqdColltnDt> | 2015-07-13 |
| DirectDebitTransaction | <DrctDbtTx> | |
| MandateRelatedInformation | <MndtReltdInf> | |
| MandateIdentification | <MndtId> | VIRGAY123 |
| DateOfSignature | <DtOfSgntr> | 2008-07-13 |
| FinalCollectionDate | <FnlColltnDt> | 2015-07-13 |
| Frequency Type | <Frqcy><Tp> | YEAR |
| Creditor | <Cdr> | |
| Name | <Nm> | Virgay |
| PostalAddress | <PstlAdr> | |
| StreetName | <StrtNm> | Virginia Lane |
| BuildingNumber | <BldgNb> | 36 |
| PostCode | <PstCd> | NJ 07311 |
| TownName | <TwnNm> | Jersey City |
| Country | <Ctry> | US |

---

<!-- Page 67 -->

| Element | XMLTag | Content |
| :--- | :--- | :--- |
| CreditorAccount | <CdrAcct> | |
| Identification | <Id> | |
| Other | <Othr> | |
| Identification | <Id> | 789123 |
| CreditorAgent | <CdrAgtr> | |
| FinancialInstitutionIdentification | <FinInstlId> | |
| BICFI | <BICFI> | AAAAUS29 |
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
| DebtorAgent | <DbtrAgtr> | |
| FinancialInstitutionIdentification | <FinInstlId> | |
| BICFI | <BICFI> | BBBBUS39 |
| Purpose | <Purp> | |
| Code | <Cd> | LIFI |
| RemittanceInformation | <RmtnInf> | |
| Unstructured | <Ustrd> | LIFE INSURANCE PAYMENT7 JULY 2015 |

## Message Instance

```xml
<FIToFICstmrDrctDbt>
    <GrpHd>
        <MsgId>AAAA100628-123v</MsgId>
        <CreDtTm>2015-06-28T10:05:00</CreDtTm>
        <NbOfTxs>1</NbOfTxs>
        <IntrBkSttlmtDt>2015-06-28</IntrBkSttlmtDt>
        <SttlmInf>
            <SttlmMtd>INDA</SttlmMtd>
        </SttlmInf>
        <PmtTpInf>
            <InstrPrty>NORM</InstrPrty>
```

---

<!-- Page 68 -->

```xml
<SvcLvl>
    <Prtry>CTRLV-356</Prtry>
</SvcLvl>
<SeqTp>RCUR</SeqTp>
</PmtTpinf>
<InstgAgt>
    <FinInstnId>
        <BICFI>AAAAUS29</BICFI>
    </FinInstnId>
</InstgAgt>
<InstdAgt>
    <FinInstnId>
        <BICFI>ABABUS23</BICFI>
    </FinInstnId>
</InstdAgt>
</GrpHdr>
<DrcrDbtTxInf>
    <RmtId>
        <EndToEndId>VA060713/0123</EndToEndId>
        <TxId>AAAAUS29/100628/ad458</TxId>
    </RmtId>
    <IntrBkSttlmAmt Ccy="USD">1025</IntrBkSttlmAmt>
    <InstdAmt Ccy="USD">1025</InstdAmt>
    <ChrgBr>SHAR</ChrgBr>
    <ReqdColltnDt>2015-07-13</ReqdColltnDt>
    <DrcrDbtTx>
        <MndtRltdInf>
            <MndtId>VIRGAY123</MndtId>
            <DtOfSgntr>2008-07-13</DtOfSgntr>
            <FnColltnDt>2015-07-13</FnColltnDt>
            <Frqcy><Tp>YEAR</Tp></Frqcy>
        </MndtRltdInf>
    </DrcrDbtTx>
    <Cdtr>
        <Nm>Virgay</Nm>
        <PstlAdr>
            <StrtNm>Virginia Lane</StrtNm>
            <BldgNb>36</BldgNb>
            <PstCd>NJ 07311</PstCd>
```

---

<!-- Page 69 -->

```xml
<TwnNm>Jersey City</TwnNm>
<Ctry>US</Ctry>
</PstlAdr>
</Cdt>
<CdtrAcct>
  <Id>
    <Othr>
      <Id>789123</Id>
    </Othr>
  </Id>
</CdtrAcct>
<CdtrAg>
  <FinInstnId>
    <BICFI>AAAAUS29</BICFI>
  </FinInstnId>
</CdtrAg>
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
<DbtrAg>
  <FinInstnId>
    <BICFI>BBBBUS39</BICFI>
  </FinInstnId>
</DbtrAg>
<Purp>
```

---

<!-- Page 70 -->

</Cd>LIF</Cd>
</Purp>
<RmtInf>
<Ustrd>LIFE INSURANCE PAYMENT/JULY 2015</Ustrd>
</RmtInf>
</DrctDbtXfer>
</FitoFICstmrDrctDbt>

## 7.3 PaymentReturn pacs.004.001.14 - 1

This example covers two PaymentReturn messages. The first PaymentReturn message is sent by CCCC Bank to BBBB Bank. The second PaymentReturn message is sent by BBBB Bank to AAAA Bank.

### 7.3.1 First PaymentReturn

**Description**

On receipt of a FitToFIPaymentCancellationRequest message from BBBB Bank, CCCC Bank checks with Seed Inc. whether it is willing to return the credited funds. Seed Inc. accepts to return the amount credited onto its account (EUR 74850) without requesting compensation. CCCC Bank sends a PaymentReturn message to BBBB Bank.

**Business Data**

PaymentReturn from CCCC Bank to BBBB Bank:



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
    <td>CCCC/151122-PR007</td>
  </tr>
  <tr>
    <td>CreationDateTime</td>
    <td>&lt;CreDtTm&gt;</td>
    <td>2015-11-22T10:37:00</td>
  </tr>
  <tr>
    <td>NumberOfTransactions</td>
    <td>&lt;NbOfTxs&gt;</td>
    <td>1</td>
  </tr>
  <tr>
    <td>SettlementInformation</td>
    <td>&lt;SttlInf&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>SettlementMethod</td>
    <td>&lt;SttlMtd&gt;</td>
    <td>CLRG</td>
  </tr>
  <tr>
    <td>ClearingSystem</td>
    <td>&lt;ClrSys&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>Proprietary</td>
    <td>&lt;Prtry&gt;</td>
    <td>CBJ</td>
  </tr>
  <tr>
    <td>InstructingAgent</td>
    <td>&lt;InstdAg&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>FinancialInstitutionIdentification</td>
    <td>&lt;FinInstnId&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>BICFI</td>
    <td>&lt;BICFI&gt;</td>
    <td>CCCCIE2D</td>
  </tr>
  <tr>
    <td>InstructedAgent</td>
    <td>&lt;InstdAg&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>FinancialInstitutionIdentification</td>
    <td>&lt;FinInstnId&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>BICFI</td>
    <td>&lt;BICFI&gt;</td>
    <td>BBBBIE2D</td>
  </tr>
  <tr>
    <td>OriginalGroupInformation</td>
    <td>&lt;OrgnlGrpInf&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>OriginalMessageIdentification</td>
    <td>&lt;OrgnlMsgId&gt;</td>
    <td>BBBB/151109-CBJ056</td>
  </tr>
  <tr>
    <td>OriginalMessageNameIdentification</td>
    <td>&lt;OrgnlMsgNmId&gt;</td>
    <td>pacs.008.001.12</td>
  </tr>
  <tr>
    <td>OriginalCreationDateTime</td>
    <td>&lt;OrgnlCreDtTm&gt;</td>
    <td>2015-11-09T10:13:00</td>
  </tr>
  <tr>
    <td>TransactionInformation</td>
    <td>&lt;TxInf&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>ReturnIdentification</td>
    <td>&lt;RtrId&gt;</td>
    <td>CCCC/151122-</td>
  </tr>
</table>

---

<!-- Page 71 -->

| Element | <XMLTag> | Content |
| :--- | :--- | :--- |
| | | PR007/1 |
| OriginalInstructionIdentification | <OrgnlInstrId> | BBBB/151109-CBJ056/1 |
| OriginalEndToEndIdentification | <OrgnlEndToEndId> | CROPS/SX-25T/2015-10-13 |
| OriginalTransactionIdentification | <OrgnlTxId> | AAAA/151109-CCT/EUR443/1 |
| OriginalInterbankSettlementAmount | <OrgnlIntrBkSttlmAmt> | EUR 74900 |
| ReturnedInterbankSettlementAmount | <RtrdIntrBkSttlmAmt> | EUR 74750 |
| InterbankSettlementDate | <IntrBkSttlmDt> | 2015-11-22 |
| ReturnedInstructedAmount | <RtrdInstdAmt> | EUR 74850 |
| ChargeBearer | <ChrgBr> | CRED |
| ChargesInformation | <ChrgInf> | |
| Amount | <Amt> | EUR 100 |
| Agent | <Agt> | |
| FinancialInstitutionIdentification | <FinInstlId> | |
| BICFI | <BICFI> | CCCCIIE2D |
| ReturnReasonInformation | <RtrnRsnInf> | |
| Originator | <Orgtr> | |
| Name | <Nm> | Seed Inc. |
| Reason | <Rsn> | |
| Code | <Cd> | NARR |
| AdditionalInformation | <AddtlInf> | RETURN AFTER ACCEPTED PAYMENT CANCELLATION REQUEST |

## Message Instance

```
<PmtRtr>
   <GrpHdr>
      <MsgId>CCCC/151122-PR007</MsgId>
      <CreDtTm>2015-11-22T10:37:00</CreDtTm>
      <NbOfTxs>1</NbOfTxs>
      <SttlmInf>
         <SttlmMtd>CLRG</SttlmMtd>
         <ClrSys>
            <Prtry>CBJ</Prtry>
         </ClrSys>
      </SttlmInf>
      <InstdAgt>
         <FinInstlId>
```

---

<!-- Page 72 -->

```xml
<BICFI>CCCCIE2D</BICFI>
</FinInstnId>
</InstgAgt>
<InstdAgt>
<FinInstnId>
<BICFI>BBBBIE2D</BICFI>
</FinInstnId>
</InstdAgt>
</GrpHdr>
<OrgnlGrpInf>
<OrgnlMsgId>BBBB/151109-CBJ056</OrgnlMsgId>
<OrgnlMsgNmId>pacs.008.001.12</OrgnlMsgNmId>
<OrgnlCreDtTm>2015-11-09T10:13:00</OrgnlCreDtTm>
</OrgnlGrpInf>
<TxInf>
<RtrId>CCCC/151122-PR007</RtrId>
<OrgnlInstd>BBBB/151109-CBJ056/1</OrgnlInstd>
<OrgnlEndToEndId>CROPS/SX-25T/2015-10-13</OrgnlEndToEndId>
<OrgnlTxId>AAAA/151109-CCT/EUR443/1</OrgnlTxId>
<OrgnlIntrBkSttlmAmt Ccy="EUR">74900</OrgnlIntrBkSttlmAmt>
<RtrdIntrBkSttlmAmt Ccy="EUR">74750</RtrdIntrBkSttlmAmt>
<RtrdSttlmDt>2015-11-22</IntrBkSttlmDt>
<RtrdSttlmAmt Ccy="EUR">74850</RtrdSttlmAmt>
<ChrgBr>CRED</ChrgBr>
<ChrgsInf>
<Amt Ccy="EUR">100</Amt>
<Agt>
<FinInstnId>
<BICFI>CCCCIE2D</BICFI>
</FinInstnId>
</Agt>
</ChrgsInf>
<RtrRsnInf>
<Orgr>
<Nm>Seed Inc.</Nm>
</Orgr>
<Rsn>
<Cd>NARR</Cd>
</Rsn>
```

---

<!-- Page 73 -->

```xml
<AddtlInf>RETURN AFTER ACCEPTED PAYMENT CANCELLATION REQUEST</AddtlInf>
</RtrRsnInf>
</TxInf>
</PmtRtr>
```

## 7.3.2 Second PaymentReturn

### Description

On receipt of the payment return message from CCCC Bank, BBBB Bank deducts processing charges for the return message, credits the account of AAAA Bank and forwards the payment return message to AAAA Bank.

### Business Data

PaymentReturn from BBBB Bank to AAAA Bank:



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
      <td>BBBB/151122-PR05</td>
    </tr>
    <tr>
      <td>CreationDateTime</td>
      <td>&lt;CreDtTm&gt;</td>
      <td>2015-11-22T11:15:00</td>
    </tr>
    <tr>
      <td>NumberOfTransactions</td>
      <td>&lt;NbOfTxs&gt;</td>
      <td>1</td>
    </tr>
    <tr>
      <td>SettlementInformation</td>
      <td>&lt;SttlInf&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>SettlementMethod</td>
      <td>&lt;SttlMtd&gt;</td>
      <td>INGA</td>
    </tr>
    <tr>
      <td>InstructingAgent</td>
      <td>&lt;InstdAg&gt;</td>
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
      <td>BBBBIE2D</td>
    </tr>
    <tr>
      <td>InstructedAgent</td>
      <td>&lt;InstdAg&gt;</td>
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
      <td>AAAAGB2L</td>
    </tr>
    <tr>
      <td>OriginalGroupInformation</td>
      <td>&lt;OrgnlGrpInf&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>OriginalMessageIdentification</td>
      <td>&lt;OrgnlMsgId&gt;</td>
      <td>AAAA/151109-CCT/<br/>EUR443</td>
    </tr>
    <tr>
      <td>OriginalMessageNameIdentification</td>
      <td>&lt;OrgnlMsgNmId&gt;</td>
      <td>pacs.008.001.12</td>
    </tr>
    <tr>
      <td>OriginalCreationDateTime</td>
      <td>&lt;OrgnlCreDtTm&gt;</td>
      <td>2015-11-09T10:03:13</td>
    </tr>
    <tr>
      <td>TransactionInformation</td>
      <td>&lt;TxInf&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>ReturnIdentification</td>
      <td>&lt;RtrId&gt;</td>
      <td>BBBB/151122-PR05/1</td>
    </tr>
    <tr>
      <td>OriginalInstructionIdentification</td>
      <td>&lt;OrgnlInstdId&gt;</td>
      <td>AAAA/151109-CCT/<br/>EUR443/1</td>
    </tr>
    <tr>
      <td>OriginalEndToEndIdentification</td>
      <td>&lt;OrgnlEndToEnd&gt;</td>
      <td>CROPS/SX-257/2015-<br/>10-13</td>
    </tr>
    <tr>
      <td>OriginalTransactionIdentification</td>
      <td>&lt;OrgnlTxId&gt;</td>
      <td>AAAA/151109-CCT/<br/>EUR443/1</td>
    </tr>
    <tr>
      <td>OriginalInterbankSettlementAmount</td>
      <td>&lt;OrgnlIntrBkSttlmAmt&gt;</td>
      <td>EUR 75000</td>
    </tr>
    <tr>
      <td>ReturnedInterbankSettlementAmount</td>
      <td>&lt;RtrdIntrBkSttlmAmt&gt;</td>
      <td>EUR 74650</td>
    </tr>
    <tr>
      <td>InterbankSettlementDate</td>
      <td>&lt;IntrBkSttlmDt&gt;</td>
      <td>2015-11-22</td>
    </tr>
  </tbody>
</table>

---

<!-- Page 74 -->

| Element | XMLTag | Content |
| :--- | :--- | :--- |
| ReturnedInstructedAmount | <RtrdInstdAmt> | EUR 74850 |
| ChargeBearer | <ChrgBr> | CRED |
| ChargesInformation | <ChrgInf> | |
| Amount | <Amt> | EUR 100 |
| Agent | <Agt> | |
| FinancialInstitutionIdentification | <FinInstId> | |
| BICFI | <BICFI> | CCCCI E2D |
| ChargesInformation | <ChrgInf> | |
| Amount | <Amt> | EUR 100 |
| Agent | <Agt> | |
| FinancialInstitutionIdentification | <FinInstId> | |
| BICFI | <BICFI> | BBBBIE2D |
| ReturnReasonInformation | <RtrRsnInf> | |
| Originator | <Orgtr> | |
| Name | <Nm> | Seed Inc. |
| Reason | <Rsn> | |
| Code | <Cd> | NARR |
| AdditionalReturnReasonInformation | <AddtlRtrRsnInf> | RETURN AFTER ACCEPTED PAYMENT CANCELLATION REQUEST |

## Message Instance

```xml
<PmtRtr>
    <GrpHdr>
        <MsgId>BBB8/151122-PR05</MsgId>
        <CreDtTm>2015-11-22T11:15:00</CreDtTm>
        <NbOfTxs>1</NbOfTxs>
        <SttlmInf>
            <SttlmMtd>INGA</SttlmMtd>
        </SttlmInf>
        <InstdAgt>
            <FinInstId>
                <BICFI>BBBBIE2D</BICFI>
            </FinInstId>
        </InstdAgt>
        <InstdAgt>
            <FinInstId>
                <BICFI>AAABGB2L</BICFI>
```

---

<!-- Page 75 -->

```xml
</FinInstld>
        </InstdAgt>
    </GrpHdr>
    <OrgnlGrpInf>
        <OrgnlMsgId>AAAA/151109-CCT/EUR443</OrgnlMsgId>
        <OrgnlMsgNmId>pacs.008.001.12</OrgnlMsgNmId>
        <OrgnlCredTm>2015-11-09T10:03:13</OrgnlCredTm>
    </OrgnlGrpInf>
    <TxInf>
        <RtrId>BBBB/151122-PR05/1</RtrId>
        <OrgnlInstd>AAAA/151109-CCT/EUR443/1</OrgnlInstd>
        <OrgnlEndToEndId>CROPS/SX-25T/2015-10-13</OrgnlEndToEndId>
        <OrgnlTxId>AAAA/151109-CCT/EUR443/1</OrgnlTxId>
        <OrgnlIntrBkSttlmAmt Ccy="EUR">75000</OrgnlIntrBkSttlmAmt>
        <RtrdIntrBkSttlmAmt Ccy="EUR">74650</RtrdIntrBkSttlmAmt>
        <IntrBkSttlmDt>2015-11-22</IntrBkSttlmDt>
        <RtrdInstdAmt Ccy="EUR">74850</RtrdInstdAmt>
        <ChrgBr>CRED</ChrgBr>
        <ChrgsInf>
            <Amt Ccy="EUR">100</Amt>
            <Agt>
                <FinInstld>
                    <BICFI>CCCCIE2D</BICFI>
                </FinInstld>
            </Agt>
        </ChrgsInf>
        <ChrgsInf>
            <Amt Ccy="EUR">100</Amt>
            <Agt>
                <FinInstld>
                    <BICFI>BBBIE2D</BICFI>
                </FinInstld>
            </Agt>
        </ChrgsInf>
        <RtrRsnInf>
            <Orgr>
                <Nm>Seed Inc.</Nm>
            </Orgr>
            <Rsn>
```

---

<!-- Page 76 -->

</Cd>Narr</Cd>
</Rsn>
<AddtlInf>RETURN AFTER ACCEPTED PAYMENT CANCELLATION REQUEST</AddtlInf>
</RtrRsnInf>
</TxInf>
</PmtRtr>

## 7.4 PaymentReturn pacs.004.001.14 - 2

This example covers two PaymentReturn messages. The first PaymentReturn message is sent by BBBBUS39 to ABABUS23. The second PaymentReturn message is sent by ABABUS23 to AAAAUS29.

### 7.4.1 First PaymentReturn

**Description**

On 28 June 2015, upon receipt of a direct debit instruction received from ABABUS23 for the collection of USD 1025, and after having checked the instruction, BBBBUS39 realises that the account specified for debtor Jones does not allow direct debits. BBBBUS39 therefore decides to send a PaymentReturn message to ABABUS23, specifying the reason, and taking charges for USD 50.

**Business Data**

PaymentReturn from BBBBUS39 to ABABUS23:



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
      <td>BBBBUS39-RETURN-0213</td>
    </tr>
    <tr>
      <td>CreationDateTime</td>
      <td>&lt;CreDtTm&gt;</td>
      <td>2015-06-29T11:15:00</td>
    </tr>
    <tr>
      <td>NumberOfTransactions</td>
      <td>&lt;NbOfTxs&gt;</td>
      <td>1</td>
    </tr>
    <tr>
      <td>SettlementInformation</td>
      <td>&lt;SttlmInf&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>Settlement Method</td>
      <td>&lt;SttlmMtd&gt;</td>
      <td>INGA</td>
    </tr>
    <tr>
      <td>InstructingAgent</td>
      <td>&lt;InstdAg&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>FinancialInstitutionIdentification</td>
      <td>&lt;FinInstnId&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>BICFI</td>
      <td>&lt;BICFI&gt;</td>
      <td>BBBBUS39</td>
    </tr>
    <tr>
      <td>InstructedAgent</td>
      <td>&lt;InstdAg&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>FinancialInstitutionIdentification</td>
      <td>&lt;FinInstnId&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>BICFI</td>
      <td>&lt;BICFI&gt;</td>
      <td>ABABUS23</td>
    </tr>
    <tr>
      <td>OriginalGroupInformation</td>
      <td>&lt;OrgnlGrpInf&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>OriginalMessageIdentification</td>
      <td>&lt;OrgnlMsgId&gt;</td>
      <td>ABABUS23-589cd</td>
    </tr>
    <tr>
      <td>OriginalMessageName Identification</td>
      <td>&lt;OrgnlMsgNmId&gt;</td>
      <td>pacs.003.001.11</td>
    </tr>
    <tr>
      <td>OriginalCreationDateAndTime</td>
      <td>&lt;OrgnlCreDtTm&gt;</td>
      <td>2015-06-28T15:02:00</td>
    </tr>
    <tr>
      <td>TransactionInformation</td>
      <td>&lt;TxInf&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>ReturnIdentification</td>
      <td>&lt;RtrId&gt;</td>
      <td>AB/RETURN765</td>
    </tr>
    <tr>
      <td>OriginalEndToEndIdentification</td>
      <td>&lt;OrgnlEndToEnd&gt;</td>
      <td>VA060327/0123</td>
    </tr>
    <tr>
      <td>ReturnedInterbankSettlementAmount</td>
      <td>&lt;RtrdIntBkSttlmAmt&gt;</td>
      <td>USD 975</td>
    </tr>
  </tbody>
</table>

---

<!-- Page 77 -->

| Element | XMLTag | Content |
| :--- | :--- | :--- |
| InterbankSettlementDate | <IntrBkSttlmDt> | 2015-07-29 |
| ChargeBearer | <ChrgBr> | CRED |
| ChargesInformation | <ChrgInf> | |
| Amount | <Amt> | USD 50 |
| Agent | <Agtr> | |
| FinancialInstitutionIdentification | <FinInstnId> | |
| BICFI | <BICFI> | BBBBUS39 |
| ReturnReasonInformation | <RtrRsnInf> | |
| Originator | <Orgtr> | |
| Identification | <Id> | |
| OrganisationIdentification | <OrgId> | |
| AnyBIC | <AnyBIC> | BBBBUS39 |
| Reason | <RtrRsn> | |
| Code | <Cd> | AG01 |
| OriginalTransactionReference | <OrgnlTxRef> | |
| InterbankSettlementAmount | <IntrBkSttlmAmt> | USD 1025 |
| InterbankSettlementDate | <IntrBkSttlmDt> | 2015-06-28 |
| RequestedCollectionDate | <ReqdCollnDt> | 2015-07-13 |
| MandateRelatedInformation | <MndtRltdInf> | |
| DirectDebitMandate | <DrctDbtMndt> | |
| MandateIdentification | <MndtId> | VIRGAY123 |
| Debtor | <Dbtr> | |
| Name | <Nm> | Jones |
| PostalAddress | <PstlAdr> | |
| StreetName | <StrtNm> | Hudson Street |
| BuildingNumber | <BldgNb> | 19 |
| PostCode | <PstCd> | NJ 07302 |
| TownName | <TwnNm> | Jersey City |
| Country | <Ctry> | US |
| Creditor | <Cdtr> | |
| Name | <Nm> | Virgay |
| PostalAddress | <PstlAdr> | |
| StreetName | <StrtNm> | Virginia Lane |
| BuildingNumber | <BldgNb> | 36 |
| PostCode | <PstCd> | NJ 07311 |
| TownName | <TwnNm> | Jersey City |
| Country | <Ctry> | US |

**Message Instance**

<PmtRtr>

---

<!-- Page 78 -->

```xml
<GrpHdr>
  <MsgId>BBBBUS39-RETURN-0123</MsgId>
  <CreDtTm>2015-06-29T11:15:00</CreDtTm>
  <NbOfTxs>1</NbOfTxs>
  <SttlmInf>
    <SttlmMtd>INGA</SttlmMtd>
  </SttlmInf>
  <InstgAgt>
    <FinInstnId>
      <BICFI>BBBBUS39</BICFI>
    </FinInstnId>
  </InstgAgt>
  <InstdAgt>
    <FinInstnId>
      <BICFI>ABABUS23</BICFI>
    </FinInstnId>
  </InstdAgt>
</GrpHdr>
<OrgnlGrpInf>
  <OrgnlMsgId>ABABUS23-589cd</OrgnlMsgId>
  <OrgnlMsgNmId>pac.003.001.11</OrgnlMsgNmId>
  <OrgnlCreDtTm>2015-06-28T15:02:00</OrgnlCreDtTm>
</OrgnlGrpInf>
<TxInf>
  <RtrId>AB/RETURN765</RtrId>
  <OrgnlInstrId>VA060327/0123</OrgnlInstrId>
  <RtrdIntrBkSttlmAmt Ccy="USD">975</RtrdIntrBkSttlmAmt>
  <IntrBkSttlmDt>2015-07-29</IntrBkSttlmDt>
  <ChrgBr>CRED</ChrgBr>
  <ChrgsInf>
    <Amt Ccy="USD">50</Amt>
    <Agt>
      <FinInstnId>
        <BICFI>BBBBUS39</BICFI>
      </FinInstnId>
    </Agt>
  </ChrgsInf>
  <RtrRsnInf>
    <Orgtr>
```

---

<!-- Page 79 -->

```xml
</Id>
    <OrgId>
        <AnyBIC>BBBBUS39</AnyBIC>
    </OrgId>
</Id>
</Orgtr>
<Rsn>
    <Cd>AG01</Cd>
</Rsn>
</RtrRsnInf>
<OrgnlTxRef>
    <IntrBkSttlmAmt Ccy="USD">1025</IntrBkSttlmAmt>
    <IntrBkSttlmDt>2015-06-28</IntrBkSttlmDt>
    <ReqdColltnDt>2015-07-13</ReqdColltnDt>
    <MndtRltdInf>
        <DrctDbtMndt>
            <MndtId>VIRGAY123</MndtId>
        </DrctDbtMndt>
    </MndtRltdInf>
    <Dbtr>
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
```

---

<!-- Page 80 -->

```xml
<Ctry>US</Ctry>
</PstlAd>
</Pty>
</Cdtr>
</OrgnTxRef>
</TxInf>
/PmtRtr>
```

## 7.4.2 Second PaymentReturn

**Description**

On 29 June 2015, upon receipt of a PaymentReturn message from BBBBUS39, ABABUS23 forwards the PaymentReturn instruction to AAAAUS29, the account servicer for creditor Virga. It forwards the reason for the return and takes USD 35 for charges. Virga will be informed about the debit on its account through its statement.

**Business Data**

PaymentReturn from ABABUS23 to AAAAUS29:



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
      <td>ABABUS23RETURN-546</td>
    </tr>
    <tr>
      <td>CreationDateTime</td>
      <td>&lt;CreDtTm&gt;</td>
      <td>2015-06-29T13:28:00</td>
    </tr>
    <tr>
      <td>NumberOfTransactions</td>
      <td>&lt;NbOfTxs&gt;</td>
      <td>1</td>
    </tr>
    <tr>
      <td>SettlementInformation</td>
      <td>&lt;SttlInf&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>Settlement Method</td>
      <td>&lt;SttlMtd&gt;</td>
      <td>INGA</td>
    </tr>
    <tr>
      <td>InstructingAgent</td>
      <td>&lt;InstdAg&gt;</td>
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
      <td>ABABUS23</td>
    </tr>
    <tr>
      <td>InstructedAgent</td>
      <td>&lt;InstdAg&gt;</td>
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
      <td>OriginalGroupInformation</td>
      <td>&lt;OrgnlGrpInf&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>OriginalMessageIdentification</td>
      <td>&lt;OrgnlMsgId&gt;</td>
      <td>AAAA060327-123v</td>
    </tr>
    <tr>
      <td>OriginalMessageName Identification</td>
      <td>&lt;OrgnlMsgNmId&gt;</td>
      <td>pacs.003.001.11</td>
    </tr>
    <tr>
      <td>OriginalCreationDateAndTime</td>
      <td>&lt;OrgnlCreDtTm&gt;</td>
      <td>2015-06-28T10:05:00</td>
    </tr>
    <tr>
      <td>TransactionInformation</td>
      <td>&lt;TxInf&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>ReturnIdentification</td>
      <td>&lt;RtrId&gt;</td>
      <td>ABABUS23/RETURN765</td>
    </tr>
    <tr>
      <td>OriginalEndToEndIdentification</td>
      <td>&lt;OrgnlEndToEnd&gt;</td>
      <td>VA060327/0123</td>
    </tr>
    <tr>
      <td>ReturnedInterbankSettlementAmount</td>
      <td>&lt;RtrdInBkSttlmAmt&gt;</td>
      <td>USD 1110</td>
    </tr>
    <tr>
      <td>InterbankSettlementDate</td>
      <td>&lt;IntrBkSttlmDt&gt;</td>
      <td>2015-06-29</td>
    </tr>
    <tr>
      <td>ChargeBearer</td>
      <td>&lt;ChrgBr&gt;</td>
      <td>CRED</td>
    </tr>
    <tr>
      <td>ChargesInformation</td>
      <td>&lt;ChrgsInf&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>Amount</td>
      <td>&lt;Amt&gt;</td>
      <td>USD 50</td>
    </tr>
  </tbody>
</table>

---

<!-- Page 81 -->

| Element | <XMLTag> | Content |
| :--- | :--- | :--- |
| Agent | <Agt> | |
| FinancialInstitutionIdentification | <FinInstnId> | |
| BICFI | <BICFI> | BBBBUS39 |
| ChargesInformation | <ChrgsInf> | |
| Amount | <Amt> | USD 35 |
| Agent | <Agt> | |
| FinancialInstitutionIdentification | <FinInstnId> | |
| BICFI | <BICFI> | ABABUS23 |
| ReturnReasonInformation | <RtrRsnInf> | |
| Originator | <Orgtr> | |
| Identification | <Id> | |
| OrganisationIdentification | <OrgId> | |
| AnyBIC | <AnyBIC> | BBBBUS39 |
| Reason | <RtrRsn> | |
| Code | <Cd> | AG01 |
| OriginalTransactionReference | <OrgnlTxRef> | |
| InterbankSettlementAmount | <IntrBkSttlmAmt> | USD 1025 |
| InterbankSettlementDate | <IntrBkSttlmDt> | 2015-06-28 |
| RequestedCollectionDate | <ReqdColltnDt> | 2015-07-13 |
| MandateRelatedInformation | <MndtRltdInf> | |
| DirectDebitMandate | <DrctDbtMndt> | |
| MandateIdentification | <MndtId> | VIRGAY123 |
| Debtor | <Dbtr> | |
| Name | <Nm> | Jones |
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

---

<!-- Page 82 -->

## Message Instance

```xml
<PmtRtr>
    <GrpHdr>
        <MsgId>ABABUS23RETURN-546</MsgId>
        <CreDtTm>2015-06-29T13:28:00</CreDtTm>
        <NbOfTxs>1</NbOfTxs>
        <SttlmInf>
            <SttlmMtd>INGA</SttlmMtd>
        </SttlmInf>
        <InstgAgt>
            <FinInstnId>
                <BICFI>ABABUS23</BICFI>
            </FinInstnId>
        </InstgAgt>
        <InstdAgt>
            <FinInstnId>
                <BICFI>AAAAUS29</BICFI>
            </FinInstnId>
        </InstdAgt>
    </GrpHdr>
    <OrgnlGrpInf>
        <OrgnlMsgId>AAAA060327-123v</OrgnlMsgId>
        <OrgnlMsgNmId>pac.003.001.11</OrgnlMsgNmId>
        <OrgnlCreDtTm>2015-06-28T10:05:00</OrgnlCreDtTm>
    </OrgnlGrpInf>
    <TxInf>
        <RtrId>ABABUS23/RETURN765</RtrId>
        <RtrdIntrBkStlmAmt Ccy="USD">1110</RtrdIntrBkStlmAmt>
        <IntrBkStlmDt>2015-06-29</IntrBkStlmDt>
        <ChrgBr>CRED</ChrgBr>
        <ChrgInf>
            <Amt Ccy="USD">50</Amt>
            <Agt>
                <FinInstnId>
                    <BICFI>BBBBUS39</BICFI>
                </FinInstnId>
            </Agt>
        </ChrgInf>
        <ChrgInf>
```

---

<!-- Page 83 -->

```
            <Amt Ccy="USD">35</Amt>
            <Agt>
                <FinInstnId>
                    <BICFI>ABABUS23</BICFI>
                </FinInstnId>
            </Agt>
        </ChrgInf>
        <RtrRsnInf>
            <Orgtr>
                <Id>
                    <OrgId>
                        <AnyBIC>BBBBUS39</AnyBIC>
                    </OrgId>
                </Id>
            </Orgtr>
            <Rsn>
                <Cd>AG01</Cd>
            </Rsn>
        </RtrRsnInf>
        <OrgnlTxRef>
            <IntrBkSttlmAmt Ccy="USD">1025</IntrBkSttlmAmt>
            <IntrBkSttlmDt>2015-06-28</IntrBkSttlmDt>
            <ReqdColltnDt>2015-07-13</ReqdColltnDt>
            <MndtRltdInf>
                <DrctDbtMndt>
                    <MndtId>VIRGAY123</MndtId>
                </DrctDbtMndt>
            </MndtRltdInf>
            <Dbtr>
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
```

---

<!-- Page 84 -->

</Dbtr>
<Cdtr>
<Pty>
<Nm>Virgavs</Nm>
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
</TxInf>
</PmtRtr>

## 7.5 FIToFIPaymentReversal pacs.007.001.13

**Description**

On 6 July 2015, AAAAUS29 finds out that the FIToFICustomerDirectDebit message it sent to ABABUS23 on 28 June 2015, for the collection of USD 1025 from debtor Jones, was a duplicated payment instruction. As the requested collection date was 13 July, AAAAUS29 decides to send an FIToFIPaymentReversal message to its correspondent ABABUS23, giving the reason for the reversal.

Any potential charges related to the reversal will be settled outside of the message, that is as part of the monthly billing process.



| **Note** | The FIToFICustomerDirectDebit instruction from AAAAUS29 to ABABUS23 is included in the business example section of the FIToFICustomerDirectDebit message. |
|---|---|

**Business Data**

FIToFIPaymentReversal from AAAAUS29 to ABABUS23:

| Element | <XMLTag> | Content |
|---|---|---|
| Group Header | <GrpHdr> | |
| MessageIdentification | <MsgId> | AAAAUS29-REVERSAL/ 0012 |
| CreationDateTime | <CreDtTm> | 2015-07-06T10:35:00 |
| NumberOfTransactions | <NbOfTxs> | 1 |
| InterbankSettlementDate | <IntrBkSttlmDt> | 2015-07-06 |
| SettlementInformation | <SttlmInf> | |
| SettlementMethod | <SttlmMtd> | INDA |

---

<!-- Page 85 -->

| Element | <XMLTag> | Content |
|---|---|---|
| InstructingAgent | <InstgAgt> | |
| FinancialInstitutionIdentification | <FinInstnId> | |
| BICFI | <BICFI> | AAAAUS29 |
| InstructedAgent | <InstdAgt> | |
| FinancialInstitutionIdentification | <FinInstnId> | |
| BICFI | <BICFI> | ABABUS23 |
| OriginalGroupInformation | <OrgnlGrpInf> | |
| OriginalMessageIdentification | <OrgnlMsgId> | AAAA120628-123v |
| OriginalMessageNameIdentification | <OrgnlMsgNmId> | pacs.003.001.11 |
| OriginalCreationDateAndTime | <OrgnlCreDtTm> | 2015-06-28T10:05:00 |
| TransactionInformation | <TxInf> | |
| ReversalIdentification | <RvslId> | AAAAUS29_REV2563 |
| OriginalEndToEndIdentification | <OrgnlEndToEnd> | VA060327/0123 |
| OriginalTransactionIdentification | <OrgnlTxId> | AAAAUS29/150628/ad458 |
| ReversedInterbankSettlementAmount | <RvslIntrBkSttlmAmt> | USD 1025 |
| ReversedInstructedAmount | <RvslInstdAmt> | USD 1025 |
| ReversalReasonInformation | <RvslRsnInf> | |
| Originator | <Orgtr> | |
| Identification | <Id> | |
| OrganisationIdentification | <OrgId> | |
| AnyBIC | <AnyBIC> | AAAAUS29 |
| Reason | <Rsn> | |
| Code | <Cd> | AM05 |
| OriginalTransactionReference | <OrgnlTxRef> | |
| InterbankSettlementAmount | <IntrBkSttlmAmt> | USD 1025 |
| InterbankSettlementDate | <IntrBkSttlmDt> | 2015-06-28 |
| RequestedCollectionDate | <ReqdCollnDt> | 2015-07-13 |
| MandateRelatedInformation | <MndtReltdInf> | |
| DirectDebitMandate | <DrctDbtMndt> | |
| MandateIdentification | <MndtId> | VIRGAY123 |
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

---

<!-- Page 86 -->

| Element | XMLTag> | Content |
| :--- | :--- | :--- |
| Other | <Othr> | |
| Identification | <Id> | 123456 |
| DebtorAgent | <DbtrAgt> | |
| FinancialInstitutionIdentification | <FinInstnId> | |
| BICFI | <BICFI> | BBBBUS39 |
| Creditor | <Cdtr> | |
| Name | <Nm> | Virgay |
| PostalAddress | <PstlAdr> | |
| StreetName | <StrtNm> | Virginia Lane |
| BuildingNumber | <BldgNb> | 36 |
| PostCode | <PstCd> | NJ 07311 |
| TownName | <TwnNm> | Jersey City |
| Country | <Ctry> | US |

**Message Instance**

```xml
<FIToPmtRvsl>
    <GrpHdr>
        <MsgId>AAAAUS29-REVERSAL/0012</MsgId>
        <CredrTm>2015-07-06T10:35:00</CredrTm>
        <NbOfTxs>1</NbOfTxs>
        <IntrBkSttlmDt>2015-07-06</IntrBkSttlmDt>
        <SttlmInf>
            <SttlmMtd>INDA</SttlmMtd>
        </SttlmInf>
        <InstdAgt>
            <FinInstnId>
                <BICFI>AAAAUS29</BICFI>
            </FinInstnId>
        </InstdAgt>
        <InstdAgt>
            <FinInstnId>
                <BICFI>ABABUS23</BICFI>
            </FinInstnId>
        </InstdAgt>
    </GrpHdr>
    <OrgnlGrpInf>
        <OrgnlMsgId>AAAA120628-123v</OrgnlMsgId>
        <OrgnlMsgNmId>pacs.003.001.11</OrgnlMsgNmId>
        <OrgnlCredrTm>2015-06-28T10:05:00</OrgnlCredrTm>
```

---

<!-- Page 87 -->

```xml
</OrgnlGrpInf>
<TxInf>
    <RvsIId>AAAAUS29_REV2563</RvsIId>
    <OrgnlEndToEndId>VA060327/0123</OrgnlEndToEndId>
    <OrgnlTxId>AAAAUS29/150628/ad458</OrgnlTxId>
    <RvsdIntrBkSttlmAmt Ccy="USD">1025</RvsdIntrBkSttlmAmt>
    <RvsdInstdAmt Ccy="USD">1025</RvsdInstdAmt>
    <RvsIRsnInf>
        <Orgtr>
            <Id>
                <OrgId>
                    <AnyBIC>AAAAUS29</AnyBIC>
                </OrgId>
            </Id>
        </Orgtr>
        <Rsn>
            <Cd>AM05</Cd>
        </Rsn>
    </RvsIRsnInf>
    <OrgnlTxRef>
        <IntrBkSttlmAmt Ccy="USD">1025</IntrBkSttlmAmt>
        <IntrBkSttlmDt>2015-06-28</IntrBkSttlmDt>
        <ReqdCollnDt>2015-07-13</ReqdCollnDt>
        <MndtRltdInf>
            <DrctDbtMndt>
                <MndtId>VIRGAY123</MndtId>
            </DrctDbtMndt>
        </MndtRltdInf>
        <Dbtr>
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
```

---

<!-- Page 88 -->

```xml
</Dbtr>
<DbtrAcct>
    <Id>
        <Othr>
            <Id>123456</Id>
        </Othr>
    </Id>
</DbtrAcct>
<DbtrAgt>
    <FinInstnId>
        <BICFI>BBBBUS39</BICFI>
    </FinInstnId>
</DbtrAgt>
<Cdtr>
    <Pty>
        <Nm>Virgays</Nm>
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
</TxInf>
</FIToFIPmtRvsl>
```

## 7.6 FIToFICustomerCreditTransfer pacs.008.001.13 - 1

This example covers four FIToFICustomerCreditTransfer messages sent by BBBBUS33.

* The first FIToFICustomerCreditTransfer message is sent to AAAAGB2L.
* The second FIToFICustomerCreditTransfer message is sent to EEEEDEFF.
* The third FIToFICustomerCreditTransfer is sent to BBBUS66

A fourth FIToFICustomerCreditTransfer message, sent by EEEEDEFF to DDDDBEBB, is also shown.

**Description**

BBB Bank, New York, has received a payment initiation from its client ABC Corporation, New York, that holds an account 00125574999 with them for payment of the following invoices:

---

<!-- Page 89 -->

**Invoice 1**

An invoice with number 4562, dated 08 September 2015 from DEF Electronics, London: 10 million JPY (AAAGB2L) to be paid to DEF Electronics account 23683707994215 with AAAA Bank, London (AAAGB2L). ABC Corporation assigns reference ABC/4562/2015-09-08 to the payment. Payment transaction charges are shared between ABC Corporation and DEF Electronics.

**Invoice 2**

An invoice with number ABC-13679, dated 15 September 2015 from GHI Semiconductors, Brussels: 500,000 EUR needs to be paid to GHI Semiconductors account BE30001216371411 with DDDD Bank, Belgium (DDDDBEBB). ABC Corporation assigns reference ABC-13679/2015-09-15 to the payment. The accounts receivable department of GHI Semiconductors needs to be advised when the funds have been credited to the account on telephone number +32/2/2222222. GHI Semiconductors will bear all payment transaction charges.

**Invoice 3**

An invoice with number 987-AC, dated 27 September 2015 from their branch ABC Corporation, California: 1 million USD needs to be paid on the branch account 4895623 with BBBB Bank, San Francisco (BBBBUS66). ABC assigns reference ABC/987-AC/2015-09-27 to the payment. Payment transaction charges are shared.

**Related Message Examples**

ABC Corporation sent a CustomerCreditTransferInitiation message containing the 3 transactions to BBBB Bank. This is illustrated in the CustomerCreditTransferInitiation business example section of the Payments Initiation Message Reference Guide.

To process the three payment instructions, BBBB Bank sends three FIToFICustomerCreditTransfer messages:

1. A first message to AAAA Bank, London (AAAGB2L). As the banks do not have a JPY account relationship, the payment is processed using the cover method. The JPY correspondent of BBBB Bank is CCCC Bank, Tokyo (CCCCJPJT). The JPY correspondent of AAAA Bank, London is AAAA Bank, Tokyo (AAAAJPJT). For the reimbursement instruction sent by BBBB Bank to its JPY correspondent CCCC Bank, please refer to the FinancialInstitutionCreditTransfer business example 1.

2. A second message to its EUR correspondent EEEE Bank, Frankfurt (EEEEDEF) where BBBB Bank has multiple accounts, for payment to DDDDBEBB. BBBB Bank specifies that account 29314569847 should be used for reimbursement.

BBBB Bank has also received a payment order from their client Mr. Jones requesting to pay a 5 thousand EUR insurance premium by 30 September 2006 for contract ZZ/JO/14794 to ZZ Insurances, Frankfurt on their account DE89370400440532014000 with EEEEDeff. Charges will be shared between the parties. BBBB Bank decides to include the latter 2 transactions in one FIToFICustomerCreditTransfer message.

3. A third message is sent to its branch BBBB Bank, San Francisco and instructs its branch to credit the account of ABC Corporation California in their books, account number 4895623.

## 7.6.1 First FIToFICustomerCreditTransfer

**Business Data**

The first FIToFICustomerCreditTransfer message, from BBBBUS33 to AAAGB2L:



<table><tr><td>Element</td><td>&lt;XMLTag&gt;</td><td>Content</td></tr><tr><td>Group Header</td><td>&lt;GrpHdr&gt;</td><td>AAAA</td></tr><tr><td>MessageIdentification</td><td>&lt;MsgId&gt;</td><td>BBBB/150928-CCT/JPY/</td></tr></table>

---

<!-- Page 90 -->

| Element | XMLTag | Content |
| :--- | :--- | :--- |
| CreationDateTime | <CreDtTm> | 2015-09-28T16:00:00 |
| NumberOfTransactions | <NbOfTxs> | 1 |
| SettlementInformation | <SttlmInf> | |
| SettlementMethod | <StlmMtd> | COVE |
| InstructingReimbursementAgent | <InstdRmbrsmtAgtr> | |
| FinancialInstitutionIdentification | <FinInstlId> | |
| BICFI | <BICFI> | CCCCJPJT |
| InstructedReimbursementAgent | <InstdRmbrsmtAgtr> | |
| FinancialInstitutionIdentification | <FinInstlId> | |
| BICFI | <BICFI> | AAAAJPJT |
| InstructingAgent | <InstdAgtr> | |
| FinancialInstitutionIdentification | <FinInstlId> | |
| BICFI | <BICFI> | BBBBUS33 |
| InstructedAgent | <InstdAgtr> | |
| FinancialInstitutionIdentification | <FinInstlId> | |
| BICFI | <BICFI> | AAAAGB2L |
| CreditTransferTransactionInformation | <CdtTrfTxInf> | |
| PaymentIdentification | <PmtId> | |
| InstructionIdentification | <InstrId> | BBBB/150928-CCT/JPY/123/1 |
| EndToEndIdentification | <EndToEndId> | ABC/4562/2015-09-08 |
| Transaction Identification | <TxId> | BBBB/150928-CCT/JPY/123/1 |
| PaymentTypeInformation | <PmtTpInf> | |
| InstructionPriority | <InstrPrty> | NORM |
| InterbankSettlementAmount | <IntrBkSttlmAmt> | JPY 10000000 |
| InterbankSettlementDate | <IntrBkSttlmDt> | 2015-09-29 |
| AcceptanceDateTime | <AcctpCreDtTm> | 2015-09-28T15:45:00 |
| ChargeBearer | <ChrgBr> | SHAR |
| Debtor | <Dbtr> | |
| Name | <Nm> | ABC Corporation |
| PostalAddress | <PstlAdr> | |
| StreetName | <StrtNm> | Times Square |
| BuildingNumber | <BldgNb> | 7 |
| PostCode | <PstCd> | NY 10036 |
| TownName | <TwnNm> | New York |
| Country | <Ctry> | US |
| DebtorAccountIdentification | <DbtrAcctId> | |

---

<!-- Page 91 -->

| Element | XMLTag | Content |
| :--- | :--- | :--- |
| Other | <Othr> | |
| Identification | <Id> | 00125574999 |
| DebtorAgent | <DbtrAgt> | |
| FinancialInstitutionIdentification | <FinInstnId> | |
| BICFI | <BICFI> | BBBBUS33 |
| CreditorAgent | <CdrAgt> | |
| FinancialInstitutionIdentification | <FinInstnId> | |
| BICFI | <BICFI> | AAAAAGB2L |
| Creditor | <Cdr> | |
| Name | <Name> | DEF Electronics |
| PostalAddress | <PstlAdr> | |
| StreetName | <StrtNm> | Mark Lane |
| BuildingNumber | <BldgNb> | 55 |
| PostCode | <PstCd> | EC3R7NE |
| TownName | <TwnNm> | London |
| Country | <Ctry> | GB |
| AddressLine | <AdrLine> | Corn Exchange 5th Floor |
| CreditorAccount | <CdrAcct> | |
| Identification | <Id> | |
| Other | <Othr> | |
| Identification | <Id> | 23683707994215 |
| Purpose | <Purp> | |
| Code | <Cd> | GDDS |
| RemittanceInformation | <Rmtnf> | |
| Structured | <Strd> | |
| ReferredDocumentInformation | <RfrdDocInf> | |
| Type | <Type> | |
| CodeOrProprietary | <CdOrPrty> | |
| Code | <Cd> | CINV |
| Number | <Nb> | 4562 |
| RelatedDate | <RltdDt> | |
| Type | <Tp> | |
| Code | <Cd> | INDA |
| Date | <Dt> | 2015-09-08 |

## Message Instance

<FIToFICstmrCdtTrf>
    <GrpHdr>
        <MsgId>BBB8/150928-CCT/IPY/123</MsgId>
        <CredItTm>2015-09-28T16:00:00</CredItTm>

---

<!-- Page 92 -->

```xml
<NbOffTx>1</NbOffTx>
<SttlmInf>
  <SttlmMtd>COVE</SttlmMtd>
  <InstgRmbrsmntAg>
    <FinInstId>
      <BICFI>CCCCJPJT</BICFI>
    </FinInstId>
  </InstgRmbrsmntAg>
  <InstdRmbrsmntAg>
    <FinInstId>
      <BICFI>AAAAJPJT</BICFI>
    </FinInstId>
  </InstdRmbrsmntAg>
</SttlmInf>
<InstgAg>
  <FinInstId>
    <BICFI>BBBBSU33</BICFI>
  </FinInstId>
</InstgAg>
<InstdAg>
  <FinInstId>
    <BICFI>AAAAGB2L</BICFI>
  </FinInstId>
</InstdAg>
</GrpHdr>
<CdtTrfTxInf>
  <PmtId>
    <InstrId>BBBB/150928-CCT/JPY/123/1</InstrId>
    <EndToEndId>ABC/4562/2015-09-08</EndToEndId>
    <TxId>BBBB/150928-CCT/JPY/123/1</TxId>
  </PmtId>
  <PmtTpInf>
    <InstrPty>NORM</InstrPty>
  </PmtTpInf>
  <IntrBkSttlmAmt Ccy="JPY">10000000</IntrBkSttlmAmt>
  <IntrBkSttlmDt>2015-09-29</IntrBkSttlmDt>
  <ChrgBr>SHAR</ChrgBr>
  <Dbtr>
    <Nm>ABC Corporation</Nm>
```

---

<!-- Page 93 -->

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
<DbtrAg>
    <FinInstnId>
        <BICFI>BBBBUS33</BICFI>
    </FinInstnId>
</DbtrAg>
<CdtrAg>
    <FinInstnId>
        <BICFI>AAAAGB2L</BICFI>
    </FinInstnId>
</CdtrAg>
<Cdtr>
    <Nm>DEF Electronics</Nm>
    <PstlAdr>
        <StrtNm>Mark Lane</StrtNm>
        <BldgNb>55</BldgNb>
        <PstCd>EC3R7NE</PstCd>
        <TwnNm>London</TwnNm>
        <Ctry>GB</Ctry>
        <AdrLine>Corn Exchange 5th Floor</AdrLine>
    </PstlAdr>
</Cdtr>
<CdtrAcct>
    <Id>
        <Othr>
```

---

<!-- Page 94 -->

```xml
                <Id>23683707994215</Id>
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
                    <Dt>2015-09-08</Dt>
                </RltdDt>
            </RfrdDocInf>
        </Strd>
    </RmtInf>
</CdtTrfTxInf>
</FIToFICstmrCdtTrf>
```

### 7.6.2 Second FIToFICustomerCreditTransfer

**Business Data**

The second FIToFICustomerCreditTransfer, from BBBBUS33 to EEEEDEFF:

| Element | <XMLTag> | Content |
| :--- | :--- | :--- |
| Group Header | | |
| MessageIdentification | <MsgId> | BBBB/150928-CCT/EUR/912 |
| CreationDateTime | <CreDtTm> | 2015-09-28T16:01:00 |
| NumberOfTransactions | <NbOfTx> | 2 |
| TotalInterbankSettlementAmount | <TtlIntrBkSttlmAmt> | EUR 504.500 |
| InterbankSettlementDate | <IntrBkSttlmDt> | 2015-09-29 |

---

<!-- Page 95 -->

| Element | <XMLTag> | Content |
| :--- | :--- | :--- |
| SettlementInformation | <SttlmInf> | |
| SettlementMethod | <SttlmMtd> | INDA |
| SettlementAccount | <SttlmAcc> | |
| Identification | <Id> | |
| Other | <Othr> | |
| Identification | <Id> | 29314569847 |
| InstructingAgent | <InstdAg> | |
| FinancialInstitutionIdentification | <FinInstlId> | |
| BICF | <BICF> | BBBBUS33 |
| InstructedAgent | <InstdAg> | |
| FinancialInstitutionIdentification | <FinInstlId> | |
| BICF | <BICF> | EEEEDEFF |
| CreditTransferTransactionInformation | <CdtTrfTxInf> | |
| PaymentIdentification | <PmtId> | |
| InstructionIdentification | <InstdId> | BBBB/150928-CCT/EUR/912/1 |
| EndToEndIdentification | <EndToEndId> | ABC/ABC-13679/2015-09-15 |
| Transaction Identification | <TxId> | BBBB/150928-CCT/EUR/912/1 |
| PaymentTypeInformation | <PmtTpInf> | |
| InstructionPriority | <InstrPrty> | NORM |
| InterbankSettlementAmount | <IntrBkSttlmAmt> | EUR 499.500 |
| InstructedAmount | <InstdAmt> | EUR 500.000 |
| ChargeBearer | <ChrgBr> | CRED |
| ChargesInformation | <ChrgsInf> | |
| Amount | <Amt> | EUR 500 |
| Agent | <Ag> | |
| FinancialInstitutionIdentification | <FinInstlId> | |
| BICF | <BICF> | BBBBUS33 |
| Debtor | <Dbtr> | |
| Name | <Nm> | ABC Corporation |
| PostalAddress | <PstlAdr> | |
| StreetName | <StrtNm> | Times Square |
| BuildingNumber | <BldgNb> | 7 |
| PostCode | <PstCd> | NY 10036 |
| TownName | <TwnNm> | New York |
| Country | <Ctry> | US |
| DebtorAccount | <DbtrAcct> | |
| Identification | <Id> | |
| Other | <Othr> | |

---

<!-- Page 96 -->

| Element | <XMLTag> | Content |
| :--- | :--- | :--- |
| Identification | <Id> | 00125574999 |
| DebtorAgent | <DbtrAgnt> | |
| FinancialInstitutionIdentification | <FinInstId> | |
| BICFI | <BICFI> | BBBBUSB33 |
| CreditorAgent | <CdtrAgnt> | |
| FinancialInstitutionIdentification | <FinInstId> | |
| BICFI | <BICFI> | DDDDBEBB |
| Creditor | <Cdtr> | |
| Name | <Name> | GHI Semiconductors |
| PostalAddress | <PstlAdr> | |
| StreetName | <StrtNm> | Avenue Brugmann |
| BuildingNumber | <BldgNb> | 415 |
| PostCode | <PstCd> | 1180 |
| TownName | <TwnNm> | Brussels |
| Country | <Ctry> | BE |
| CreditorAccount | <CdtrAcct> | |
| Identification | <Id> | |
| IBAN | <IBAN> | BE30001216371411 |
| Purpose | <Purp> | |
| Code | <Cd> | GDDS |
| RemittanceInformation | <RmtInf> | |
| Structured | <Strd> | |
| ReferredDocumentInformation | <RfrdDocInf> | |
| Type | <RfrdDocTp> | |
| CodeOrProprietary | <CdOrPrtry> | |
| Code | <Cd> | CINV |
| Number | <Nb> | ABC-13679 |
| RelatedDate | <RltdDt> | |
| Type | <Tp> | |
| Code | <Cd> | INDA |
| Date | <Dt> | 2015-09-15 |
| CreditTransferTransactionInformation | <CdtTrfTxInf> | |
| PaymentIdentification | <PmtId> | |
| InstructionIdentification | <InstrId> | BBBB/150928-CCT/EUR/912/2 |
| EndToEndIdentification | <EndToEndId> | BBBB/150928-ZZ/OJ/164794 |
| TransactionIdentification | <TxId> | BBBB/150928-CCT/EUR/912/2 |
| PaymentTypeInformation | <PmtTpInf> | |

---

<!-- Page 97 -->

| Element | <XMLTag> | Content |
| :--- | :--- | :--- |
| InstructionPriority | <InstrPrty> | NORM |
| InterbankSettlementAmount | <IntrBkSttlmAmt> | EUR 5000 |
| ChargeBearer | <ChrgBr> | SHAR |
| Debtor | <Dbtr> | |
| Name | <Name> | Mr. Jones |
| PostalAddress | <PstlAdr> | |
| StreetName | <StrtNm> | 16th Street |
| BuildingNumber | <BldgNb> | 30 |
| PostCode | <PstCd> | NY 10023 |
| TownName | <TwnNm> | New York |
| Country | <Ctry> | US |
| DebtorAccount | <DbtrAcct> | |
| Identification | <Id> | |
| Other | <Othr> | |
| Identification | <Id> | 00125583145 |
| DebtorAgent | <DbtrAgt> | |
| FinancialInstitutionIdentification | <FinInstnId> | |
| BICFI | <BICFI> | BBBBUSB33 |
| CreditorAgent | <CdtrAgt> | |
| FinancialInstitutionIdentification | <FinInstnId> | |
| BICFI | <BICFI> | EEEEDEFF |
| Creditor | <Cdtr> | |
| Name | <Name> | ZZ Insurances |
| PostalAddress | <PstlAdr> | |
| StreetName | <StrtNm> | Friedrich-Ebert-Anlage |
| BuildingNumber | <BldgNb> | 2-14 |
| PostCode | <PstCd> | D-60 325 |
| TownName | <TwnNm> | Frankfurt am Main |
| Country | <Ctry> | DE |
| AddressLine | <AdrLine> | City Haus 1 10th Floor |
| CreditorAccount | <CdtrAcct> | |
| Identification | <Id> | |
| IBAN | <IBAN> | DE89370400440532014000 |
| RemittanceInformation | <RmtInf> | |
| Unstructured | <Ustrd> | Contract ZZ/JO/164794 |

## Message Instance

```
<FIToFICstmrCdtTrf>
   <GrpHdr>
      <MsgId>BBBB/150928-CT/EUR/912</MsgId>
```

---

<!-- Page 98 -->

```xml
<CreDtTm>2015-09-28T16:01:00</CreDtTm>
<NbOfTxs>2</NbOfTxs>
<TtlIntrBkSttlmAmt Ccy="EUR">504500</TtlIntrBkSttlmAmt>
<IntrBkSttlmDt>2015-09-29</IntrBkSttlmDt>
<SttlmInf>
  <SttlmMtd>INDA</SttlmMtd>
  <SttlmAcct>
    <Id>
      <Othr>
        <Id>29314569847</Id>
      </Othr>
    </Id>
  </SttlmAcct>
</SttlmInf>
<InstdAgt>
  <FinInstnId>
    <BICFI>BBBBUS33</BICFI>
  </FinInstnId>
</InstdAgt>
<InstdAgt>
  <FinInstnId>
    <BICFI>EEEEDEFF</BICFI>
  </FinInstnId>
</InstdAgt>
</GrpHdr>
<CdtTrfTxInf>
  <PmtId>
    <InstrId>BBBB/150928-CCT/EUR/912/1</InstrId>
    <EndToEndId>ABC/ABC-13679/2015-09-15</EndToEndId>
    <TxId>BBBB/150928-CCT/EUR/912/1</TxId>
  </PmtId>
  <PmtTpInf>
    <InstrPrty>NORM</InstrPrty>
  </PmtTpInf>
  <IntrBkSttlmAmt Ccy="EUR">499500</IntrBkSttlmAmt>
  <InstdAmt Ccy="EUR">500000</InstdAmt>
  <ChrgBr>CRED</ChrgBr>
  <ChrgsInf>
    <Amt Ccy="EUR">500</Amt>
```

---

<!-- Page 99 -->

```xml
<Agtr>
   <FinInstnId>
      <BICFI>BBB8BUS33</BICFI>
   </FinInstnId>
</Agtr>
</ChrgsInf>
<Dbtr>
   <Nm>ABC Corporation</Nm>
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
   <FinInstnId>
      <BICFI>BBB8BUS33</BICFI>
   </FinInstnId>
</DbtrAgt>
<CdtrAgt>
   <FinInstnId>
      <BICFI>DDDDDEBEB</BICFI>
   </FinInstnId>
</CdtrAgt>
<Cdtr>
   <Nm>GHI Semiconductors</Nm>
   <PstlAdr>
      <StrtNm>Avenue Brugmann</StrtNm>
      <BldgNb>415</BldgNb>
      <PstCd>1180</PstCd>
```

---

<!-- Page 100 -->

```xml
<TwnNm>Brussels</TwnNm>
<Ctry>BE</Ctry>
</PstlAdr>
</Cdtr>
<CdtrAcct>
<Id>
<IBAN>BE300001216371411</IBAN>
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
<Nb>ABC-13679</Nb>
<RltdDt>
<Tp>
<Cd>INDA</Cd>
</Tp>
<Dt>2015-09-15</Dt>
</RltdDt>
</RfrdDocInf>
</Strd>
</RmtInf>
<CdtTrfTxInf>
<CdtTrfTxInf>
<PmtId>
<InstdId>BBBB/150928-CCT/EUR/912/2</InstdId>
<EndToEndId>BBBB/150928-ZZ/J0/164794</EndToEndId>
<TxId>BBBB/150928-CCT/EUR/912/2</TxId>
</PmtId>
<PmtTpInf>
<InstrPrty>NORM</InstrPrty>
```

---

<!-- Page 101 -->

```
</PmtIdInf>
<IntrBkSttlmAmt Ccy="EUR">5000</IntrBkSttlmAmt>
<ChrgBr>SHAR</ChrgBr>
<Dbtr>
    <Nm>Mr. Jones</Nm>
    <PstlAdr>
        <StrtNm>16th Street</StrtNm>
        <BldgNb>30</BldgNb>
        <PstCd>NY10023</PstCd>
        <TwnNm>New York</TwnNm>
        <Ctry>US</Ctry>
    </PstlAdr>
</Dbtr>
<DbtrAcct>
    <Othr>
        <Id>00125583145</Id>
    </Othr>
</Id>
</DbtrAcct>
<DbtrAgt>
    <FinInstnId>
        <BICF>BBBBUS33</BICF>
    </FinInstnId>
</DbtrAgt>
<CdtrAgt>
    <FinInstnId>
        <BICF>EEEEDEFF</BICF>
    </FinInstnId>
</CdtrAgt>
<Cdtr>
    <Nm>ZZ Insurance</Nm>
    <PstlAdr>
        <StrtNm>Friedrich-Ebert-Anlage</StrtNm>
        <BldgNb>2-14</BldgNb>
        <PstCd>D-60 325</PstCd>
        <TwnNm>Frankfurt am Main</TwnNm>
        <Ctry>DE</Ctry>
        <AdrLine>City Haus 1 10th Floor</AdrLine>
```

---

<!-- Page 102 -->

```xml
</PstlAdr>
</Cdtr>
<CdtrAcct>
  <Id>
    <IBAN>DE89370400440532014000</IBAN>
  </Id>
</CdtrAcct>
<RmtInf>
  <Ustrd>Contract ZZ/JO/164794</Ustrd>
</RmtInf>
</CdtrTrfXml>
</FitOfICstmrCdtTrf>
```

## 7.6.3 Third FitOfICustomerCreditTransfer

**Business Data**

The third FitOfICustomerCreditTransfer, from BBBBUS33 to BBBBUS66:



<table border="1">
	<tr> <th> Element </th> <th> &lt;XMLTag&gt; </th> <th> Content </th> </tr>
	<tr> <td> Group Header </td> <td> &lt;GrpHdr&gt; </td> <td> </td> </tr>
	<tr> <td> MessageIdentification </td> <td> &lt;MsgId&gt; </td> <td> BBBB/150928-CCT/ USD/897 </td> </tr>
	<tr> <td> CreationDateTime </td> <td> &lt;CreDtTm&gt; </td> <td> 2015-09-28T16:02:00 </td> </tr>
	<tr> <td> NumberOfTransactions </td> <td> &lt;NbOfTx&gt; </td> <td> 1 </td> </tr>
	<tr> <td> TotalInterbankSettlementAmount </td> <td> &lt;TtlIntrBkSttlmAmt&gt; </td> <td> USD 1.000.000 </td> </tr>
	<tr> <td> InterbankSettlementDate </td> <td> &lt;IntrBkSttlmDt&gt; </td> <td> 2015-06-29 </td> </tr>
	<tr> <td> SettlementInformation </td> <td> &lt;SttlmInf&gt; </td> <td> </td> </tr>
	<tr> <td> SettlementMethod </td> <td> &lt;SttlmMtd&gt; </td> <td> INDA </td> </tr>
	<tr> <td> InstructingAgent </td> <td> &lt;InstdAg&gt; </td> <td> </td> </tr>
	<tr> <td> FinancialInstitutionIdentification </td> <td> &lt;FinInstlId&gt; </td> <td> </td> </tr>
	<tr> <td> BICFI </td> <td> &lt;BICFI&gt; </td> <td> BBBBUS33 </td> </tr>
	<tr> <td> InstructedAgent </td> <td> &lt;InstdAg&gt; </td> <td> </td> </tr>
	<tr> <td> FinancialInstitutionIdentification </td> <td> &lt;FinInstlId&gt; </td> <td> </td> </tr>
	<tr> <td> BICFI </td> <td> &lt;BICFI&gt; </td> <td> BBBBUS66 </td> </tr>
	<tr> <td> CreditTransferTransactionInformation </td> <td> &lt;CdtTrfTxInf&gt; </td> <td> </td> </tr>
	<tr> <td> PaymentIdentification </td> <td> &lt;PmtId&gt; </td> <td> </td> </tr>
	<tr> <td> InstructionIdentification </td> <td> &lt;InstdId&gt; </td> <td> ABC/150928/CCT001/3 </td> </tr>
	<tr> <td> EndToEndIdentification </td> <td> &lt;EndToEndId&gt; </td> <td> ABC/987-AC/2015-09-27 </td> </tr>
	<tr> <td> Transaction Identification </td> <td> &lt;TxId&gt; </td> <td> BBBB/150928-CCT/ USD/897 </td> </tr>
	<tr> <td> PaymentTypeInformation </td> <td> &lt;PmtTpInf&gt; </td> <td> </td> </tr>
	<tr> <td> InstructionPriority </td> <td> &lt;InstrPrty&gt; </td> <td> NORM </td> </tr>
	<tr> <td> InterbankSettlementAmount </td> <td> &lt;IntrBkSttlmAmt&gt; </td> <td> USD 1.000.000 </td> </tr>
</table>

---

<!-- Page 103 -->

| Element | <XMLTag> | Content |
|---|---|---|
| ChargeBearer | <ChrgBr> | SHAR |
| Debtor | <Dbtr> | |
| Name | <Nm> | ABC Corporation |
| PostalAddress | <PstlAdr> | |
| StreetName | <StrtNm> | Times Square |
| BuildingNumber | <BldgNb> | 7 |
| PostCode | <PstCd> | NY 10036 |
| TownName | <TwnNm> | New York |
| Country | <Ctry> | US |
| DebtorAccount | <DbtrAcct> | |
| Identification | <Id> | |
| Other | <Othr> | |
| Identification | <Id> | 00125574999 |
| DebtorAgent | <DbtrAgt> | |
| FinancialInstitutionIdentification | <FinInstnId> | |
| BICFI | <BICFI> | BBBBUS33 |
| CreditorAgent | <CdtrAgt> | |
| FinancialInstitutionIdentification | <FinInstnId> | |
| BICFI | <BICFI> | BBBBUS66 |
| Creditor | <Cdtr> | |
| Name | <Name> | ABC Corporation |
| Department | <Dept> | Treasury department |
| PostalAddress | <PstlAdr> | |
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
| Structured | <Strd> | |
| ReferredDocumentInformation | <RfrdDocInf> | |
| Type | <RfrdDocType> | |
| CodeOrProprietary | <CdOrPrtry> | |

---

<!-- Page 104 -->

| Element | XMLTag | Content |
| :--- | :--- | :--- |
| Code | <Cd> | CINV |
| Number | <Nb> | 987-AC |
| RelatedDate | <RltdDt> | |
| Type | <Tp> | |
| Code | <Cd> | INDA |
| Date | <Dt> | 2015-09-27 |

**Message Instance**

```xml
<FitOfICstmrCdtTrf>
    <GrpHdr>
        <MsgId>BBBB/150928-CCT/USD/897</MsgId>
        <CreDtTm>2015-09-28T16:02:00</CreDtTm>
        <NbOfTxs>1</NbOfTxs>
        <TtlIntrBkSttlmAmt Ccy="USD">1000000</TtlIntrBkSttlmAmt>
        <IntrBkSttlmDt>2015-06-29</IntrBkSttlmDt>
        <SttlmInf>
            <SttlmMtd>INDA</SttlmMtd>
        </SttlmInf>
        <InstdAgt>
            <FinInstnId>
                <BICFI>BBBBUS33</BICFI>
            </FinInstnId>
        </InstdAgt>
        <InstdAgt>
            <FinInstnId>
                <BICFI>BBBBUS66</BICFI>
            </FinInstnId>
        </InstdAgt>
    </GrpHdr>
    <CdtTrfTxInf>
        <PmtId>
            <InstdId>ABC/150928/CCT001/3</InstdId>
            <EndToEndId>ABC/987-AC/2015-09-27</EndToEndId>
            <TxId>BBBB/150928-CCT/USD/897</TxId>
        </PmtId>
        <PmtTpInf>
            <InstrPrty>NORM</InstrPrty>
        </PmtTpInf>
```

---

<!-- Page 105 -->

```xml
<IntrBkStlmAmt Ccy="USD">1000000</IntrBkStlmAmt>
<ChrgBr>SHAR</ChrgBr>
<Dbtr>
  <Nm>ABC Corporation</Nm>
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
  <FinInstnId>
    <BICFI>BBBBUS33</BICFI>
  </FinInstnId>
</DbtrAgt>
<CdtrAgt>
  <FinInstnId>
    <BICFI>BBBBUS56</BICFI>
  </FinInstnId>
</CdtrAgt>
<Cdtr>
  <Nm>ABC Corporation</Nm>
  <PstlAdr>
    <Dept>Treasury Department</Dept>
    <StrtNm>Bush Street</StrtNm>
    <BldgNb>13</BldgNb>
    <PstCd>CA 94108</PstCd>
    <TwnNm>San Francisco</TwnNm>
    <Ctry>US</Ctry>
  </PstlAdr>
```

---

<!-- Page 106 -->

</Cdt r>
<CdtrAcct>
  <Id>
    <Othr>
      <Id>4895623</Id>
    </Othr>
  </Id>
</CdtrAcct>
<Purp>
  <Cd>INTC</Cd>
</Purp>
<RmtInf>
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
        <Dt>2015-09-27</Dt>
      </RltdDt>
    </RfrdDocInf>
  </Strd>
</RmtInf>
</CdtTrfTxInf>
</FItOFICstmrCdtTrf>

### 7.6.4 Fourth FItOFICustomerCreditTransfer

**Description**

On receipt of the message of BBBB Bank, EEEE Bank debits the account of BBBB Bank and credits its customer ZZ Insurances as instructed in the second payment transaction. EEEE Bank creates a new FItOFICustomerCreditTransfer to execute the first payment transaction and sends it to creditor agent DDDDBEBB through the clearing system XYZ of which both banks are members.

**Business Data**

FItOFICustomerCreditTransfer from EEEEDEFF to DDDDBEBB:

---

<!-- Page 107 -->

| Element | XMLTag | Content |
| :--- | :--- | :--- |
| Group Header | <GrpHdr> | |
| MessageIdentification | <MsgId> | EEEE/150929-EUR/059 |
| CreationDateTime | <CreDtTm> | 12-09-29T09:00:00 |
| NumberOfTransactions | <NbOfTxs> | 1 |
| SettlementInformation | <SttlmInf> | |
| SettlementMethod | <SttlmMtd> | CLRG |
| ClearingSystem | <ClrSys> | |
| Proprietary | <Prtry> | XYZ |
| InstructingAgent | <InstdAgnt> | |
| FinancialInstitutionIdentification | <FinInstnId> | |
| BICFI | <BICFI> | EEEEDEFF |
| InstructedAgent | <InstdAgnt> | |
| FinancialInstitutionIdentification | <FinInstnId> | |
| BICFI | <BICFI> | DDDDBeBB |
| CreditTransferTransactionInformation | <CdtTrfTxInf> | |
| PaymentIdentification | <PmtId> | |
| InstructionIdentification | <InstdId> | EEEE/150929-EUR/059/1 |
| EndToEndIdentification | <EndToEndId> | ABC/ABC-13679/2015-09-15 |
| TransactionIdentification | <TxId> | BBBB/150928-CCT/EUR/912/1 |
| PaymentTypeInformation | <PmtTpInf> | |
| InstructionPriority | <InstrPrty> | NORM |
| InterbankSettlementAmount | <IntrBkSttlmAmt> | EUR 499.250 |
| InterbankSettlementDate | <IntrBkSttlmDt> | 2015-09-29 |
| InstructedAmount | <InstdAmt> | EUR 500.000 |
| ChargeBearer | <ChrgBr> | CRED |
| ChargesInformation | <ChrgsInf> | |
| Amount | <Amt> | EUR 500 |
| Agent | <Agt> | |
| FinancialInstitutionIdentification | <FinInstnId> | |
| BICFI | <BICFI> | BBBBUS33 |
| ChargesInformation | <ChrgsInf> | |
| Amount | <Amt> | EUR 250 |
| Agent | <Agt> | |
| FinancialInstitutionIdentification | <FinInstnId> | |
| BICFI | <BICFI> | EEEEDEFF |
| Debtor | <Dbtr> | |
| Name | <Nm> | ABC Corporation |
| PostalAddress | <PstlAdr> | |

---

<!-- Page 108 -->

| Element | <XMLTag> | Content |
| :--- | :--- | :--- |
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
| BICFI | <BICFI> | BBBBUS33 |
| CreditorAgent | <CdtrAgt> | |
| FinancialInstitutionIdentification | <FinInstlId> | |
| BICFI | <BICFI> | DDDDBEBB |
| Creditor | <Cdtr> | |
| Name | <Name> | GHI Semiconductors |
| PostalAddress | <PstlAdr> | |
| StreetName | <StrNm> | Avenue Brugmann |
| BuildingNumber | <BldgNb> | 415 |
| PostCode | <PstCd> | 1180 |
| TownName | <TwnNm> | Brussels |
| Country | <Ctry> | BE |
| CreditorAccount | <CdtrAcct> | |
| Identification | <Id> | |
| IBAN | <IBAN> | BE30001216371411 |
| Purpose | <Purp> | |
| Code | <Cd> | GDDS |
| RemittanceInformation | <RmtInf> | |
| Structured | <Strd> | |
| ReferredDocumentInformation | <RfrdDocInf> | |
| Type | <Type> | |
| CodeOrProprietary | <CdOrPrtry> | |
| Code | <Cd> | CINV |
| Number | <Nb> | ABC-13679 |
| RelatedDate | <RltdDt> | |
| Type | <Tp> | |
| Code | <Cd> | INDA |
| Date | <Dt> | 2015-09-15 |

---

<!-- Page 109 -->

**Message Instance**

```xml
<FIToFICstmrCdtTrf>
    <GrpHdr>
        <MsgId>EEEE/150929-EUR/059</MsgId>
        <CreDtTm>2015-09-29T09:00:00</CreDtTm>
        <NbOfTxs>1</NbOfTxs>
        <SttlmInf>
            <StlmMtd>CLRG</StlmMtd>
            <ClrSys>
                <Prtry>XYZ</Prtry>
            </ClrSys>
        </SttlmInf>
        <InstgAgt>
            <FinInstnId>
                <BICFI>EEEEDEFF</BICFI>
            </FinInstnId>
        </InstgAgt>
        <InstdAgt>
            <FinInstnId>
                <BICFI>DDDDBEBB</BICFI>
            </FinInstnId>
        </InstdAgt>
    </GrpHdr>
    <CdtTrfTxInf>
        <PmtId>
            <InstrId>EEEE/150929-EUR/059/1</InstrId>
            <EndToEndId>ABC/ABC-13679/2015-09-15</EndToEndId>
            <TxId>BBBB/150928-CCT/EUR/912</TxId>
        </PmtId>
        <PmtTpInf>
            <InstrPrty>NORM</InstrPrty>
        </PmtTpInf>
        <IntrBkSttlmAmt Ccy="EUR">499250</IntrBkSttlmAmt>
        <IntrBkSttlmDt>2015-09-29</IntrBkSttlmDt>
        <InstdAmt Ccy="EUR">500000</InstdAmt>
        <ChrgBr>CRED</ChrgBr>
        <ChrgInf>
            <Amt Ccy="EUR">500</Amt>
            <Agt>
```

---

<!-- Page 110 -->

```
                <FinInstnId>
                    <BICFI>BBB8BUS33</BICFI>
                </FinInstnId>
            </Agt>
        </ChrgsInf>
        <ChrgsInf>
            <Amt Ccy="EUR">250</Amt>
            <Agt>
                <FinInstnId>
                    <BICFI>EEEEDEEFF</BICFI>
                </FinInstnId>
            </Agt>
        </ChrgsInf>
        <Dbtr>
            <Nm>ABC Corporation</Nm>
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
            <FinInstnId>
                <BICFI>BBB8BUS33</BICFI>
            </FinInstnId>
        </DbtrAgt>
        <CdtrAgt>
            <FinInstnId>
                <BICFI>DDDDBEBEB</BICFI>
            </FinInstnId>
```

---

<!-- Page 111 -->

```
</CdrAgt>
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
            <RltdDt>
                <Tp>
                    <Cd>INDA</Cd>
                </Tp>
                <Dt>2015-09-15</Dt>
            </RltdDt>
        </RfrdDocInf>
    </Strd>
</RmtInf>
</CdtTrfTxInf>
</FtoFlCstmrCdtTrf>
```

---

<!-- Page 112 -->

### 7.7 FIToFICustomerCreditTransfer pacs.008.001.13 - 2

This example covers two FIToFICustomerCreditTransfer messages. The first FIToFICustomerCreditTransfer message is sent by AAAA Bank to BBBB Bank. The second FIToFICustomerCreditTransfer message is sent by BBBB Bank to CCCC Bank.

#### 7.7.1 First FIToFICustomerCreditTransfer

##### Description

Biogenetics-Crops, HQ, Glasgow, subsidiary of Biogenetics HQ, London, has received an invoice with number SX-25T, dated 13 October 2010 from Seed Inc., Dublin: 75 thousand EUR needs to be paid to the account of Seed Inc. IE29CCCC933115212345678 held at CCCC Bank, Dublin (CCCCIE2D). Transaction charges for the payment are shared between Biogenetics and Seed Inc.

The payment of all Biogenetics invoices is centralised at Biogenetics HQ. It assigns reference CROPS/SX-25T/

2015-10-13 to the payment order and passes it on to AAAA Bank (AAAAGB2L) where it holds the account

46373892034012. AAAA Bank sends the payment to its correspondent BBBB Bank in Dublin (BBBBIE2D).

##### Business Data

The first FIToFICustomerCreditTransfer, sent by AAAA Bank to BBBB Bank:

| Element | <XMLTag> | Content |
|---|---|---|
| Group Header | <GrpHdr> | |
| MessageIdentification | <MsgId> | AAAA/151109-CCT/EUR/443 |
| CreationDateTime | <CreDtTm> | 2015-11-09T10:09:13 |
| NumberOfTransactions | <NbOfTxs> | 1 |
| SettlementInformation | <SttlmInf> | |
| SettlementMethod | <SttlmMtd> | INDA |
| InstructingAgent | <InstdAg> | |
| FinancialInstitutionIdentification | <FinInstId> | |
| BICFI | <BICFI> | AAAAGB2L |
| InstructedAgent | <InstdAg> | |
| FinancialInstitutionIdentification | <FinInstId> | |
| BICFI | <BICFI> | BBBBIE2D |
| CreditTransferTransactionInformation | <CdtTrfTxInf> | |
| PaymentIdentification | <PmtId> | |
| InstructionIdentification | <Instd> | AAAA/151109-CCT/EUR/443/1 |
| EndToEndIdentification | <EndToEndId> | CROPS/SX-25T/2015-10-13 |
| Transaction Identification | <TxId> | AAAA/151109-CCT/EUR/443/1 |
| InterbankSettlementAmount | <IntrBkSttlmAmt> | EUR 75.000 |
| InterbankSettlementDate | <IntrBkSttlmDt> | 2015-11-09 |
| InstructedAmount | <InstdAmt> | EUR 75.000 |

---

<!-- Page 113 -->

| Element | XMLTag | Content |
|---|---|---|
| ChargeBearer | <ChrgBr> | SHAR |
| UltimateDebtor | <UltmDbtr> | |
| Name | <Nm> | Biogenetics - CROPS |
| PostalAddress | <PstlAdr> | |
| StreetName | <StrtNm> | Growth Street |
| BuildingNumber | <BldgNb> | 17 |
| PostCode | <PstCd> | G5 0TW |
| TownName | <TwnNm> | Glasgow |
| Country | <Ctry> | GB |
| Debtor | <Dbtr> | |
| Name | <Nm> | Biogenetics - HQ |
| PostalAddress | <PstlAdr> | |
| StreetName | <StrtNm> | Corn Street |
| BuildingNumber | <BldgNb> | 13 |
| PostCode | <PstCd> | W6 8DR |
| TownName | <TwnNm> | London |
| Country | <Ctry> | GB |
| DebtorAccount | <DbtrAcct> | |
| Identification | <Id> | |
| Other | <Othr> | |
| Identification | <Id> | 46373892034012 |
| DebtorAgent | <DbtrAgt> | |
| FinancialInstitutionIdentification | <FinInstlId> | |
| BICFI | <BICFI> | AAAAGB2L |
| CreditorAgent | <CdtrAgt> | |
| FinancialInstitutionIdentification | <FinInstlId> | |
| BICFI | <BICFI> | CCCCEIE2D |
| Creditor | <Cdtr> | |
| Name | <Name> | Seed Inc. |
| PostalAddress | <PstlAdr> | |
| StreetName | <StrtNm> | Grain Lane |
| BuildingNumber | <BldgNb> | 27 |
| TownName | <TwnNm> | Dublin |
| Country | <Ctry> | IE |
| CreditorAccount | <CdtrAcct> | |
| Identification | <Id> | |
| IBAN | <IBAN> | IE29CCCC93115212345678 |
| Purpose | <Purp> | |
| Code | <Cd> | GDDS |
| RemittanceInformation | <RmtnInf> | |

---

<!-- Page 114 -->

| Element | XMLTag | Content |
| :--- | :--- | :--- |
| Structured | <Strd> | |
| ReferredDocumentInformation | <RfrdDocInf> | |
| Type | <Type> | |
| Code | <Cd> | CINV |
| Number | <Nb> | SX-2ST |
| RelatedDate | <RltdDt> | |
| Type | <Tp> | |
| Code | <Cd> | INDA |
| Date | <Dt> | 2015-10-13 |

**Message Instance**

```xml
<FIToFICstmrCdtTrf>
    <GrpHdr>
        <MsgId>AAAA/151109-CCT/EUR/443</MsgId>
        <CreDtTm>2015-11-09T10:09:13</CreDtTm>
        <NbOfTxs>1</NbOfTxs>
        <SttlmInf>
            <SttlmMtd>INDA</SttlmMtd>
        </SttlmInf>
        <InstdAgt>
            <FinInstnId>
                <BICFI>AAAAGBZL/BICFI>
            </FinInstnId>
        </InstdAgt>
        <InstdAgt>
            <FinInstnId>
                <BICFI>BBBBIE2D</BICFI>
            </FinInstnId>
        </InstdAgt>
    </GrpHdr>
    <CdtTrfTxInf>
        <PmtId>
            <InstdId>AAAA/151109-CCT/EUR/443/1</InstdId>
            <EndToEndId>CROPS/SX-2ST/2015-10-13</EndToEndId>
            <TxId>AAAA/151109-CCT/EUR/443/1</TxId>
        </PmtId>
        <IntrBkSttlmAmt Ccy="EUR">750000</IntrBkSttlmAmt>
        <IntrBkSttlmDt>2015-11-09</IntrBkSttlmDt>
        <InstdAmt Ccy="EUR">75000</InstdAmt>
```

---

<!-- Page 115 -->

```
<ChrgBr>SHAR</ChrgBr>
<UltmltDbr>
    <Nm>Biogenetics - CROPS</Nm>
    <PstlAdr>
        <StrtNm>Growth Street</StrtNm>
        <BldgNb>17</BldgNb>
        <PstCd>G5 0TW</PstCd>
        <TwnNm>Glasgow</TwnNm>
        <Ctry>GB</Ctry>
    </PstlAdr>
</UltmltDbr>
<Dbr>
    <Nm>Biogenetics - HQ</Nm>
    <PstlAdr>
        <StrtNm>Corn Street</StrtNm>
        <BldgNb>13</BldgNb>
        <PstCd>W6 8DR</PstCd>
        <TwnNm>London</TwnNm>
        <Ctry>GB</Ctry>
    </PstlAdr>
</Dbr>
<DbrtrAcct>
    <Id>
        <Othr>
            <Id>46373892034012</Id>
        </Othr>
    </Id>
</DbrtrAcct>
<DbrtrAg>
    <FinInstnId>
        <BICFI>AAAAGB2L</BICFI>
    </FinInstnId>
</DbrtrAg>
<CdtrAg>
    <FinInstnId>
        <BICFI>CCCCIE2D</BICFI>
    </FinInstnId>
</CdtrAg>
<Cdtr>
```

---

<!-- Page 116 -->

```
                <Nm>Seed Inc.</Nm>
                <PstlAdr>
                    <StrtNm>Grain Lane</StrtNm>
                    <BldgNb>27</BldgNb>
                    <TwnNm>Dublin</TwnNm>
                    <Ctry>IE</Ctry>
                </PstlAdr>
            </Cdtr>
            <CdtrAcct>
                <Id>
                    <IBAN>IE29CCCC93115212345678</IBAN>
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
                        <Nb>SX-25T</Nb>
                        <RltdDt>
                            <Tp>
                                <Cd>INDA</Cd>
                            </Tp>
                            <Dt>2015-10-13</Dt>
                        </RltdDt>
                    </RfrdDocInf>
                </Strd>
            </RmtInf>
        </CdtTrfTxInf>
    </FitToFiCstrmCdtTrf>
```

---

<!-- Page 117 -->

## 7.7.2 Second FIToFICustomerCreditTransfer

### Description

On receipt of the payment instruction, BBBB Bank debits AAAA Bank account, deducts its processing charges and sends an FIToFICustomerCreditTransfer to CCCC Bank, Dublin across the Irish RTGS system.

### Business Data

The second FIToFICustomerCreditTransfer, sent by BBBB Bank to CCCC Bank:



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
    <td>BBBB/151109-CBJ056</td>
  </tr>
  <tr>
    <td>CreationDateTime</td>
    <td>&lt;CreDtTm&gt;</td>
    <td>2015-11-09T10:13:00</td>
  </tr>
  <tr>
    <td>NumberOfTransactions</td>
    <td>&lt;NbOfTxs&gt;</td>
    <td>1</td>
  </tr>
  <tr>
    <td>SettlementInformation</td>
    <td>&lt;StlmInf&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>SettlementMethod</td>
    <td>&lt;StlmMtd&gt;</td>
    <td>CLRG</td>
  </tr>
  <tr>
    <td>ClearingSystem</td>
    <td>&lt;ClrSys&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>Proprietary</td>
    <td>&lt;Prtry&gt;</td>
    <td>CBJ</td>
  </tr>
  <tr>
    <td>InstructingAgent</td>
    <td>&lt;InstdAgnt&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>FinancialInstitutionIdentification</td>
    <td>&lt;FinInstnId&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>BICFI</td>
    <td>&lt;BICFI&gt;</td>
    <td>BBBBIE2D</td>
  </tr>
  <tr>
    <td>InstructedAgent</td>
    <td>&lt;InstdAgnt&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>FinancialInstitutionIdentification</td>
    <td>&lt;FinInstnId&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>BICFI</td>
    <td>&lt;BICFI&gt;</td>
    <td>CCCCIE2D</td>
  </tr>
  <tr>
    <td>CreditTransferTransactionInformation</td>
    <td>&lt;CdtTrfTxInf&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>PaymentIdentification</td>
    <td>&lt;PmtId&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>InstructionIdentification</td>
    <td>&lt;InstrId&gt;</td>
    <td>BBBB/151109-CBJ056/1</td>
  </tr>
  <tr>
    <td>EndToEndIdentification</td>
    <td>&lt;EndToEndId&gt;</td>
    <td>CROPS/SX-25T/2015-10-13</td>
  </tr>
  <tr>
    <td>TransactionIdentification</td>
    <td>&lt;TxId&gt;</td>
    <td>AAAA/151109-CCT/EUR/443/1</td>
  </tr>
  <tr>
    <td>InterbankSettlementAmount</td>
    <td>&lt;IntrBkSttlmAmt&gt;</td>
    <td>EUR 74.900</td>
  </tr>
  <tr>
    <td>InterbankSettlementDate</td>
    <td>&lt;IntrBkSttlmDt&gt;</td>
    <td>2015-11-09</td>
  </tr>
  <tr>
    <td>InstructedAmount</td>
    <td>&lt;InstdAmt&gt;</td>
    <td>EUR 75.000</td>
  </tr>
  <tr>
    <td>ChargeBearer</td>
    <td>&lt;ChrgBr&gt;</td>
    <td>SHAR</td>
  </tr>
  <tr>
    <td>ChargesInformation</td>
    <td>&lt;ChrgsInf&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>Amount</td>
    <td>&lt;Amt&gt;</td>
    <td>EUR 100</td>
  </tr>
  <tr>
    <td>Agent</td>
    <td>&lt;Agnt&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>FinancialInstitutionIdentification</td>
    <td>&lt;FinInstnId&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>BICFI</td>
    <td>&lt;BICFI&gt;</td>
    <td>BBBBIE2D</td>
  </tr>
  <tr>
    <td>UltimateDebtor</td>
    <td>&lt;UltmtDbtr&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>Name</td>
    <td>&lt;Nm&gt;</td>
    <td>Biogenetics - CROPS</td>
  </tr>
  <tr>
    <td>PostalAddress</td>
    <td>&lt;PstlAdr&gt;</td>
    <td></td>
  </tr>
</table>

---

<!-- Page 118 -->

| Element | <XMLTag> | Content |
| :--- | :--- | :--- |
| StreetName | <StrtNm> | Growth Street |
| BuildingNumber | <BldgNb> | 17 |
| PostCode | <PstCd> | G5 0TW |
| TownName | <TwnNm> | Glasgow |
| Country | <Ctry> | GB |
| Debtor | <Dbtr> | |
| Name | <Nm> | Biogenetics - HQ |
| PostalAddress | <PstlAdr> | |
| StreetName | <StrtNm> | Corn Street |
| BuildingNumber | <BldgNb> | 13 |
| PostCode | <PstCd> | W6 8DR |
| TownName | <TwnNm> | London |
| Country | <Ctry> | GB |
| DebtorAccount | <DbtrAcct> | |
| Identification | <Id> | |
| Other | <Othr> | |
| Identification | <Id> | 46373892034012 |
| DebtorAgent | <DbtrAgt> | |
| FinancialInstitutionIdentification | <FinInstlId> | |
| BICFI | <BICFI> | AAAAGB2L |
| CreditorAgent | <CdtrAgt> | |
| FinancialInstitutionIdentification | <FinInstlId> | |
| BICFI | <BICFI> | CCCCIE2D |
| Creditor | <Cdtr> | |
| Name | <Name> | Seed Inc. |
| PostalAddress | <PstlAdr> | |
| StreetName | <StrtNm> | Grain Lane |
| BuildingNumber | <BldgNb> | 27 |
| TownName | <TwnNm> | Dublin |
| Country | <Ctry> | IE |
| CreditorAccount | <CdtrAcct> | |
| Identification | <Id> | |
| IBAN | <IBAN> | IE29CCCC93115212345678 |
| Purpose | <Purp> | |
| Code | <Cd> | GDDS |
| RemittanceInformation | <RmtInf> | |
| Structured | <Strd> | |
| ReferredDocumentInformation | <RfrdDocInf> | |
| Type | <Type> | |
| CodeOrProprietary | <CdOrPrtry> | |

---

<!-- Page 119 -->

| Element | <XMLTag> | Content |
| :--- | :--- | :--- |
| Code | <Cd> | CINV |
| Number | <Nb> | SX-25T |
| RelatedDate | <RltdDt> | |
| Type | <Tp> | |
| Code | <Cd> | INDA |
| Date | <Dt> | 2015-10-13 |

## Message Instance

```xml
<FitToFICstmtrCdtTrf>
   <GrpHdr>
      <MsgId>BBBB/151109-CBJO56</MsgId>
      <CreDtTm>2015-11-09T10:13:00</CreDtTm>
      <NbOfTxs>1</NbOfTxs>
      <SttlmInf>
         <SttlmMtd>CLRG</SttlmMtd>
         <ClrSys>
            <Prtry>CBJ</Prtry>
         </ClrSys>
      </SttlmInf>
      <InstgAg>
         <FinInstnId>
            <BICFI>BBBBIE2D</BICFI>
         </FinInstnId>
      </InstgAg>
      <InstdAg>
         <FinInstnId>
            <BICFI>CCCCIE2D</BICFI>
         </FinInstnId>
      </InstdAg>
   </GrpHdr>
   <CdtTrfTxInf>
      <PmtId>
         <InstrId>BBBB/151109-CBJO56/1</InstrId>
         <EndToEndId>CROPS/SX-25T/2015-10-13</EndToEndId>
         <TxId>AAAA/151109-CCT/EUR/443/1</TxId>
      </PmtId>
      <IntrBkSttlmAmt Ccy="EUR">74900</IntrBkSttlmAmt>
      <IntrBkSttlmDt>2015-11-09</IntrBkSttlmDt>
```

---

<!-- Page 120 -->

```xml
<InstdAmt Ccy="EUR">75000</InstdAmt>
<ChrgBr>SHAR</ChrgBr>
<ChrgInf>
    <Amt Ccy="EUR">100</Amt>
    <Agt>
        <FinInstnId>
            <BICFI>BBBBIE2D</BICFI>
        </FinInstnId>
    </Agt>
</ChrgInf>
<UltmtDbtr>
    <Nm>Biogenetics - CROPS</Nm>
    <PstlAdr>
        <StrtNm>Growth Street</StrtNm>
        <BldgNb>17</BldgNb>
        <PstCd>G5 0TW</PstCd>
        <TwnNm>Glasgow</TwnNm>
        <Ctry>GB</Ctry>
    </PstlAdr>
</UltmtDbtr>
<Dbtr>
    <Nm>Biogenetics - HQ</Nm>
    <PstlAdr>
        <StrtNm>Corn Street</StrtNm>
        <BldgNb>13</BldgNb>
        <PstCd>W6 8DR</PstCd>
        <TwnNm>London</TwnNm>
        <Ctry>GB</Ctry>
    </PstlAdr>
</Dbtr>
<DbtrAcct>
    <Id>
        <Othr>
            <Id>46373892034012</Id>
        </Othr>
    </Id>
</DbtrAcct>
<DbtrAgt>
    <FinInstnId>
```

---

<!-- Page 121 -->

```xml
<BICFI>AAAGB2L</BICFI>
</FinInstnId>
</DbtrAgt>
<CdtrAgt>
  <FinInstnId>
    <BICFI>CCCCIE2D</BICFI>
  </FinInstnId>
</CdtrAgt>
<Cdtr>
  <Nm>Seed Inc.</Nm>
  <PstlAdr>
    <StrtNm>Grain Lane</StrtNm>
    <BldgNb>27</BldgNb>
    <TwnNm>Dublin</TwnNm>
    <Ctry>E</Ctry>
  </PstlAdr>
</Cdtr>
<CdtrAcct>
  <Id>
    <IBAN>IE29CCCC93115212345678</IBAN>
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
      <Nb>SX-25T</Nb>
      <RltdDt>
        <Tp>
          <Cd>INDA</Cd>
        </Tp>
        <Dt>2015-10-13</Dt>
```

---

<!-- Page 122 -->

</RltdDt>
    </RfrdDocInf>
    </Strd>
    </RmtnInf>
    </CdtTrfTxInf>
    </FitOfICstmrCdtTrf>

## 7.8 FinancialInstitutionCreditTransfer pacs.009.001.12 - 1

This example covers two FinancialInstitutionCreditTransfer messages. The first FinancialInstitutionCreditTransfer message is sent by BBBB Bank to CCCC Bank. The second FinancialInstitutionCreditTransfer message is sent by CCCCJPJT to AAAAJPT.

### 7.8.1 First FinancialInstitutionCreditTransfer

**Description**

Under business example 1 of the FitOfICustomerCreditTransfer, BBBB Bank, New York (BBBBUS33) sent an FitOfICustomerCreditTransfer message to AAAA Bank (AAAAGB2L) using the cover method as BBBB Bank does not have a JPY account relationship with AAAA Bank. BBBB Bank uses CCCC Bank, Tokyo as its correspondent. AAAA Bank uses AAAA Bank, Tokyo (AAAAJPJT) as its JPY correspondent. Immediately after sending the FitOfICustomerCreditTransfer to AAAA Bank, BBBB Bank sends its correspondent CCCC Bank a FinancialInstitutionCreditTransfer message to cover the customer payment.

**Business Data**

FinancialInstitutionCreditTransfer from BBBB Bank to CCCC Bank:



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
      <td>BBBB/150928-FICT/JPY/430</td>
    </tr>
    <tr>
      <td>CreationDateTime</td>
      <td>&lt;CreDtTm&gt;</td>
      <td>2015-09-28T16:00:00</td>
    </tr>
    <tr>
      <td>NumberOfTransactions</td>
      <td>&lt;NbOfTxs&gt;</td>
      <td>1</td>
    </tr>
    <tr>
      <td>SettlementInformation</td>
      <td>&lt;SttlmInf&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>SettlementMethod</td>
      <td>&lt;SttlmMtd&gt;</td>
      <td>INDA</td>
    </tr>
    <tr>
      <td>InstructingAgent</td>
      <td>&lt;InstdAgnt&gt;</td>
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
      <td>BBBBUS33</td>
    </tr>
    <tr>
      <td>InstructedAgent</td>
      <td>&lt;InstdAgnt&gt;</td>
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
      <td>CCCCJPJT</td>
    </tr>
    <tr>
      <td>CreditTransferTransactionInformation</td>
      <td>&lt;CdtTrfTxInf&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>PaymentIdentification</td>
      <td>&lt;PmtId&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>InstructionIdentification</td>
      <td>&lt;InstrId&gt;</td>
      <td>BBBB/150928-FICT/JPY/430/1</td>
    </tr>
  </tbody>
</table>

---

<!-- Page 123 -->

| Element | <XMLTag> | Content |
| :--- | :--- | :--- |
| EndToEndIdentification | <EndToEndId> | ABC/4562/2015-09-08 |
| TransactionIdentification | <TxId> | BBB/150928-CCT/JPY/123/1 |
| InterbankSettlementAmount | <IntrBkSttlmAmt> | JPY 10000000 |
| InterbankSettlementDate | <IntrBkSttlmDt> | 2015-09-29 |
| Debtor | <Dbtr> | |
| FinancialInstitutionIdentification | <FinInstId> | |
| BICFI | <BICFI> | BBBBUS33 |
| CreditorAgent | <CdtrAgt> | |
| FinancialInstitutionIdentification | <FinInstId> | |
| BICFI | <BICFI> | AAAAJPT |
| Creditor | <Cdtr> | |
| FinancialInstitutionIdentification | <FinInstId> | |
| BICFI | <BICFI> | AAAAGB2L |
| UnderlyingCustomerCreditTransfer | <UndrlgCstmrCdtTrf> | |
| InitiatingParty | <InitgPty> | |
| Name | <Nm> | ABC Corporation |
| PostalAddress | <PstlAdr> | |
| Streetname | <StrtNm> | Times Square |
| BuildingNumber | <BldgNb> | 7 |
| Postcode | <PstCd> | NY 10036 |
| TownName | <TwnNm> | New York |
| Country | <Ctry> | US |
| Debtor | <Dbtr> | |
| Name | <Nm> | ABC Corporation |
| PostalAddress | <PstlAdr> | |
| Streetname | <StrtNm> | Times Square |
| BuildingNumber | <BldgNb> | 7 |
| Postcode | <PstCd> | NY 10036 |
| TownName | <TwnNm> | New York |
| Country | <Ctry> | US |
| DebtorAgent | <DbtrAgt> | |
| FinancialInstitutionIdentification | <FinInstId> | |
| BICFI | <BICFI> | BBBBUS33 |
| CreditorAgent | <CdtrAgt> | |
| FinancialInstitutionIdentification | <FinInstId> | |
| BICFI | <BICFI> | AAAAGB2L |
| Creditor | <Cdtr> | |
| Name | <Nm> | DEF Electronics |
| PostalAddress | <PstlAdr> | |

---

<!-- Page 124 -->

| Element | XMLTag | Content |
| :--- | :--- | :--- |
| StreetName | <StrtNm> | Mark Lane |
| BuildingNumber | <BldgNb> | 55 |
| Postcode | <PstCd> | EC3R7NE |
| TownName | <TwnNm> | London |
| Country | <Ctry> | GB |
| AddressLine | <AdrLine> | Corn Exchange 5th Floor |
| CreditorAccount | <CdrAcct> | |
| Identification | <Id> | |
| Other | <Othr> | |
| Identification | <Id> | 29683707994815 |
| RemittanceInformation | <RmtInf> | |
| Structured | <Strd> | |
| ReferredDocumentInformation | <RfrdDocInf> | |
| Type | <RfrdDocType> | |
| CodeOrProprietary | <CdOrPrtry> | |
| Code | <Cd> | CINV |
| Number | <RfrdDocNb> | 4562 |
| RelatedDate | <RltdDt> | |
| Type | <Tp> | |
| Code | <Cd> | INDA |
| Date | <Dt> | 2015-09-08 |

## Message Instance

```xml
<FICdtTrf>
    <GrpHdr>
        <MsgId>BBB8/150928-FICT/JPY/430</MsgId>
        <CreDtTm>2015-09-28T16:00:00</CreDtTm>
        <NbOfTxs>1</NbOfTxs>
        <SttlmInf>
            <SttlmMtd>INDA</SttlmMtd>
        </SttlmInf>
        <InstdAgt>
            <FinInstnId>
                <BICFI>BBBBUS33</BICFI>
            </FinInstnId>
        </InstdAgt>
        <InstdAgt>
            <FinInstnId>
                <BICFI>CCCCJPJT</BICFI>
```

---

<!-- Page 125 -->

```
</FinInstId>
</InstdAg>
</GrpHdr>
<CdtTrfTxInf>
    <PmtId>
        <InstrId>BBBB/150928-FICT/JPY/430/1</InstrId>
        <EndToEndId>ABC/4562/2015-09-08</EndToEndId>
        <TxId>BBBB/150928-CCT/123/1</TxId>
    </PmtId>
    <IntrBkSttlmAmt Ccy="JPY">10000000</IntrBkSttlmAmt>
    <IntrBkSttlmDt>2015-09-29</IntrBkSttlmDt>
    <Dbtr>
        <FinInstId>
            <BICFI>BBBBUS33</BICFI>
        </FinInstId>
    </Dbtr>
    <Cdt>
        <FinInstId>
            <BICFI>AAAJPJT</BICFI>
        </FinInstId>
    </Cdt>
    <Cdt>
        <FinInstId>
            <BICFI>AAAAGB2L</BICFI>
        </FinInstId>
    </Cdt>
    <UndrlygCstmrCdtTrf>
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
        <Dbtr>
            <Nm>ABC Corporation</Nm>
```

---

<!-- Page 126 -->

```
<PstlAdr>
   <StrtNm>Times Square</StrtNm>
   <BldgNb>7</BldgNb>
   <PstCd>NY 10036</PstCd>
   <TwnNm>New York</TwnNm>
   <Ctry>US</Ctry>
</PstlAdr>
</Dbtr>
<DbtrAgt>
   <FinInstnId>
      <BICFI>BBBBUS33</BICFI>
   </FinInstnId>
</DbtrAgt>
<CdtrAgt>
   <FinInstnId>
      <BICFI>AAAGGB21</BICFI>
   </FinInstnId>
</CdtrAgt>
<Cdtr>
   <Nm>DEF Electronics</Nm>
   <PstlAdr>
      <StrtNm>Mark Lane</StrtNm>
      <BldgNb>55</BldgNb>
      <PstCd>EC3R2NE</PstCd>
      <TwnNm>London</TwnNm>
      <Ctry>GB</Ctry>
      <AdrLine>Corn Exchange 5th Floor</AdrLine>
   </PstlAdr>
</Cdtr>
<CdtrAcct>
   <Id>
      <Othr>
         <Id>29683707994815</Id>
      </Othr>
   </Id>
</CdtrAcct>
<RmtInf>
   <Strd>
      <RfrdDocInf>
```

---

<!-- Page 127 -->

```xml
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
<Dt>2015-09-08</Dt>
</RltdDt>
</Strd>
</RmtInf>
</UndrlygCstmrCdtTrf>
<CdtTrfTxInf>
</FlcCdtTrf>
```

## 7.8.2 Second FinancialInstitutionCreditTransfer

**Description**

On receipt of the instruction of BBBB Bank, CCCC Bank forwards the FinancialInstitutionCreditTransfer to the creditor agent AAAAJPJT. CCCC Bank holds multiple accounts with AAAAJPJT, and specifies that account 3451571 has to be used for reimbursement.

**Business Data**

FinancialInstitutionCreditTransfer from CCCCJPJT to AAAAJPJT:

| Element | XMLTag> | Content |
| :--- | :--- | :--- |
| Group Header | <GrpHdr> | |
| MessageIdentification | <MsgId> | CCCC/150929-FICT/743 |
| CreationDateTime | <CreDtTm> | 2015-09-29T08:00:10 |
| NumberOfTransactions | <NbOfTxs> | 1 |
| SettlementInformation | <SttlmInf> | |
| SettlementMethod | <SttlmMtd> | INDA |
| SettlementAccount | <SttlmAcct> | |
| Identification | <Id> | |
| Other | <Othr> | |
| Identification | <Id> | 3451571 |
| InstructingAgent | <InstdAgnt> | |
| FinancialInstitutionIdentification | <FinInstnId> | |

---

<!-- Page 128 -->

| Element | <XMLTag> | Content |
| :--- | :--- | :--- |
| BICFI | <BICFI> | CCCCJPJT |
| InstructedAgent | <InstdAg> | |
| FinancialInstitutionIdentification | <FinInstlId> | |
| BICFI | <BICFI> | AAAAJPJT |
| CreditTransferTransactionInformation | <CdtTrfTxInf> | |
| PaymentIdentification | <PmtId> | |
| InstructionIdentification | <Instd> | CCCC/150929-FICT/743/1 |
| EndToEndIdentification | <EndToEndId> | ABC/4562/2015-09-08 |
| Transaction Identification | <TxId> | BBBB/150928-CCT/JPY/123/1 |
| InterbankSettlementAmount | <IntrBkSttlmAmt> | JPY 10000000 |
| InterbankSettlementDate | <IntrBkSttlmDt> | 2015-09-29 |
| Debtor | <Dbtr> | |
| FinancialInstitutionIdentification | <FinInstlId> | |
| BICFI | <BICFI> | BBBBUS33 |
| Creditor | <Cdtor> | |
| FinancialInstitutionIdentification | <FinInstlId> | |
| BICFI | <BICFI> | AAAAGB2L |

## Message Instance

```xml
<CdtTrf>
    <GrpHdr>
        <MsgId>CCCC/150929-FICT/743</MsgId>
        <CreDtTm>2015-09-29T08:00:10</CreDtTm>
        <NbOfTxs>1</NbOfTxs>
    </GrpHdr>
    <SttlmInf>
        <SttlmMtd>INDA</SttlmMtd>
        <SttlmAcct>
            <Id>
                <Othr>
                    <Id>3451571</Id>
                </Othr>
            </Id>
        </SttlmAcct>
    </SttlmInf>
    <InstdAg>
        <FinInstlId>
            <BICFI>CCCCJPJT</BICFI>
        </FinInstlId>
```

---

<!-- Page 129 -->

</InstgAgt>
<InstdAgt>
<FinInstnId>
<BICFI>AAAAJPJT</BICFI>
</FinInstnId>
</InstdAgt>
</GrpHdr>
<CdtTrfTxInf>
<PmtId>
<InstdId>CCCC/150929-FICT/743/1</InstdId>
<EndToEndId>ABC/4562/2015-09-08</EndToEndId>
<TxId>BBBBB/150928-CCT/JPY/123/1</TxId>
</PmtId>
<IntrBkSttlmAmt Ccy="JPY">10000000</IntrBkSttlmAmt>
<IntrBkSttlmDt>2015-09-29</IntrBkSttlmDt>
<Dbtr>
<FinInstnId>
<BICFI>BBBBB533</BICFI>
</FinInstnId>
</Dbtr>
<Cdtr>
<FinInstnId>
<BICFI>AAAAGB2L</BICFI>
</FinInstnId>
</Cdtr>
</CdtTrfTxInf>
</FICdtTrf>

## 7.9 FinancialInstitutionCreditTransfer pacs.009.001.12 - 2

This example covers three FinancialInstitutionCreditTransfer messages.

- The first FinancialInstitutionCreditTransfer message is sent by AAAAFRPP to CCCCSSESS.
- The second FinancialInstitutionCreditTransfer message is sent by CCCCSSESS to FFFFSSESS.
- The second FinancialInstitutionCreditTransfer message is sent by FFFFSSESS to DDDDDULL.

### 7.9.1 First FinancialInstitutionCreditTransfer

**Description**

On 20 October 2015, AAAAFRPP agrees on a foreign exchange deal with BBBBITTT: 100 million SEK is sold against 10,621,575.00 EUR (exchange rate 9.4148). The deal is confirmed with common reference BBBBTT4148AAAAAPP.

---

<!-- Page 130 -->

On the same day AAAAFRPP sends a FinancialInstitutionCreditTransfer message to its SEK correspondent CCCCSSE5. They instruct CCCCSSE5 to debit their account 123456789 with value date 22 October 2015 to pay 100 million SEK to BBBBITTT.

BBBBITTT has communicated the following settlement instructions: the SEK amount is to be credited to the SEK sub- account of their account 99556622876 with DDDDLULL. DDDDLULL owns a SEK account 24538877443 with FFFFSE5.

## Business Data

The first FinancialInstitutionCreditTransfer message, from AAAAFRPP to CCCCSSE5:



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
      <td>AAAA/151020-SEK/005</td>
    </tr>
    <tr>
      <td>CreationDateTime</td>
      <td>&lt;CreDtTm&gt;</td>
      <td>2015-10-20T11:03:00</td>
    </tr>
    <tr>
      <td>NumberOfTransactions</td>
      <td>&lt;NbOfTxs&gt;</td>
      <td>1</td>
    </tr>
    <tr>
      <td>SettlementInformation</td>
      <td>&lt;StlmInf&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>SettlementMethod</td>
      <td>&lt;StlmMtd&gt;</td>
      <td>INDA</td>
    </tr>
    <tr>
      <td>SettlementAccount</td>
      <td>&lt;StlmAcct&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>Identification</td>
      <td>&lt;Id&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>Other</td>
      <td>&lt;Othr&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>Identification</td>
      <td>&lt;Id&gt;</td>
      <td>123456789</td>
    </tr>
    <tr>
      <td>InstructingAgent</td>
      <td>&lt;InstdAg&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>FinancialInstitutionIdentification</td>
      <td>&lt;FinInstId&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>BICFI</td>
      <td>&lt;BICFI&gt;</td>
      <td>AAAAFRPP</td>
    </tr>
    <tr>
      <td>InstructedAgent</td>
      <td>&lt;InstdAg&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>FinancialInstitutionIdentification</td>
      <td>&lt;FinInstId&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>BICFI</td>
      <td>&lt;BICFI&gt;</td>
      <td>CCCCSSE5</td>
    </tr>
    <tr>
      <td>CreditTransferTransactionInformation</td>
      <td>&lt;CdtTrfTxInf&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>PaymentIdentification</td>
      <td>&lt;PmtId&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>InstructionIdentification</td>
      <td>&lt;InstrId&gt;</td>
      <td>AAAA/151020-SEK/005/1</td>
    </tr>
    <tr>
      <td>EndToEndIdentification</td>
      <td>&lt;EndToEndId&gt;</td>
      <td>BBBBTT4148AAAAPP</td>
    </tr>
    <tr>
      <td>Transaction Identification</td>
      <td>&lt;TxId&gt;</td>
      <td>AAAA/151020-SEK/005/1</td>
    </tr>
    <tr>
      <td>InterbankSettlementAmount</td>
      <td>&lt;IntrBkSttlmAmt&gt;</td>
      <td>SEK 100.000.000</td>
    </tr>
    <tr>
      <td>InterbankSettlementDate</td>
      <td>&lt;IntrBkSttlmDt&gt;</td>
      <td>2015-10-22</td>
    </tr>
    <tr>
      <td>IntermediaryAgent1</td>
      <td>&lt;IntrmyAg1&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>FinancialInstitutionIdentification</td>
      <td>&lt;FinInstId&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>BICFI</td>
      <td>&lt;BICFI&gt;</td>
      <td>FFFFSE5</td>
    </tr>
    <tr>
      <td>Debtor</td>
      <td>&lt;Dbtr&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>FinancialInstitutionIdentification</td>
      <td>&lt;FinInstId&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>BICFI</td>
      <td>&lt;BICFI&gt;</td>
      <td>AAAAFRPP</td>
    </tr>
    <tr>
      <td>CreditorAgent</td>
      <td>&lt;CdtrAg&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>FinancialInstitutionIdentification</td>
      <td>&lt;FinInstId&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>BICFI</td>
      <td>&lt;BIC&gt;</td>
      <td>DDDDLULL</td>
    </tr>
  </tbody>
</table>

---

<!-- Page 131 -->

| Element | XMLTag> | Content |
| :--- | :--- | :--- |
| CreditorAgentAccount | <CdtorAgmtAcc> | |
| Identification | <Id> | |
| Other | <Othr> | |
| Identification | <Id> | 24538877443 |
| Creditor | <Cdtor> | |
| FinancialInstitutionIdentification | <FinInstnId> | |
| BICFI | <BICFI> | BBBBITTT |
| CreditorAccount | <CdtorAcc> | |
| Identification | <Id> | |
| Other | <Othr> | |
| Identification | <Id> | 995566ZZ876 |
| Currency | <Ccy> | SEK |

**Message Instance**

```xml
<FICdtTrf>
    <GrpHdr>
        <MsgId>AAAA/151020-SEK/005</MsgId>
        <CreDtTm>2015-10-20T11:03:00</CreDtTm>
        <NbOfTxs>1</NbOfTxs>
        <SttlmInf>
            <SttlmMtd>INDA</SttlmMtd>
            <SttlmAcct>
                <Id>
                    <Othr>
                        <Id>123456789</Id>
                    </Othr>
                </Id>
            </SttlmAcct>
        </SttlmInf>
        <InstdAgt>
            <FinInstnId>
                <BICFI>AAAAFRPP</BICFI>
            </FinInstnId>
        </InstdAgt>
        <InstdAgt>
            <FinInstnId>
                <BICFI>CCCCSESS</BICFI>
            </FinInstnId>
        </InstdAgt>
```

---

<!-- Page 132 -->

```
</GrpHdr>
<CdtTrfTxInf>
  <PmtId>
    <InstrId>AAAA/151020-SEK/005/1</InstrId>
    <EndToEndId>BBBTTT4148AAAAAPP</EndToEndId>
    <TxId>AAAA/151020-SEK/005/1</TxId>
  </PmtId>
  <IntrBkSttlmAmt Ccy="SEK">100000000</IntrBkSttlmAmt>
  <IntrBkSttlmDt>2015-10-22</IntrBkSttlmDt>
  <IntrmyAgt1>
    <FinInstnId>
      <BICFI>FFFSESE5</BICFI>
    </FinInstnId>
  </IntrmyAgt1>
  <Dbtr>
    <FinInstnId>
      <BICFI>AAAAFRPP</BICFI>
    </FinInstnId>
  </Dbtr>
  <CdtrAgt>
    <FinInstnId>
      <BICFI>DDDDLULL</BICFI>
    </FinInstnId>
  </CdtrAgt>
  <CdtrAgtAcct>
    <Id>
      <Othr>
        <Id>24538877443</Id>
      </Othr>
    </Id>
  </CdtrAgtAcct>
  <Cdtr>
    <FinInstnId>
      <BICFI>BBBBITTT</BICFI>
    </FinInstnId>
  </Cdtr>
  <CdtrAcct>
    <Id>
      <Othr>
```

---

<!-- Page 133 -->

</Id>
</Othr>
</Id>
<Ccy>SEK</Ccy>
</CdtrAcct>
</CdtrTrfXtnfo>
</FIcdtTrf>

## 7.9.2 Second FinancialInstitutionCreditTransfer

**Description**

On 22 October 2015 CCCC forwards the FinancialInstitutionCreditTransfer to the next party in the chain FFFF through the Swedish RTGS system RIX.

**Business Data**

The second FinancialInstitutionCreditTransfer message, from CCCCSSESS to FFFFSESS:



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
      <td>CCCC/151022-SSK/075</td>
    </tr>
    <tr>
      <td>CreationDate Time</td>
      <td>&lt;CreDtTm&gt;</td>
      <td>2015-10-22T09:00:00</td>
    </tr>
    <tr>
      <td>NumberOfTransactions</td>
      <td>&lt;NbOfTxs&gt;</td>
      <td>1</td>
    </tr>
    <tr>
      <td>SettlementInformation</td>
      <td>&lt;SttlInf&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>SettlementMethod</td>
      <td>&lt;SttlMtd&gt;</td>
      <td>CLRG</td>
    </tr>
    <tr>
      <td>ClearingSystem</td>
      <td>&lt;ClrSys&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>Code</td>
      <td>&lt;Cd&gt;</td>
      <td>SSK</td>
    </tr>
    <tr>
      <td>InstructingAgent</td>
      <td>&lt;InstdAgnt&gt;</td>
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
      <td>CCCCSSESS</td>
    </tr>
    <tr>
      <td>InstructedAgent</td>
      <td>&lt;InstdAgnt&gt;</td>
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
      <td>FFFFSESS</td>
    </tr>
    <tr>
      <td>CreditTransferTransactionInformation</td>
      <td>&lt;CdtrTrfXtnfo&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>PaymentIdentification</td>
      <td>&lt;PmtId&gt;</td>
      <td></td>
    </tr>
    <tr>
      <td>InstructionIdentification</td>
      <td>&lt;InstdId&gt;</td>
      <td>CCCC/151022-SSK/075/1</td>
    </tr>
    <tr>
      <td>EndToEndIdentification</td>
      <td>&lt;EndToEndId&gt;</td>
      <td>BBB8TT14148AAAAPP</td>
    </tr>
    <tr>
      <td>Transaction Identification</td>
      <td>&lt;TxId&gt;</td>
      <td>AAAA/151020-SEK/005/1</td>
    </tr>
    <tr>
      <td>InterbankSettlementAmount</td>
      <td>&lt;IntrBkSttlmAmt&gt;</td>
      <td>SEK 100.000.000</td>
    </tr>
    <tr>
      <td>InterbankSettlementDate</td>
      <td>&lt;IntrBkSttlmDt&gt;</td>
      <td>2015-10-22</td>
    </tr>
    <tr>
      <td>Debtor</td>
      <td>&lt;Dbtr&gt;</td>
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
      <td>AAAAFRPP</td>
    </tr>
    <tr>
      <td>CreditorAgent</td>
      <td>&lt;CdtrAgnt&gt;</td>
      <td></td>
    </tr>
  </tbody>
</table>

---

<!-- Page 134 -->

| Element | <XMLTag> | Content |
| :--- | :--- | :--- |
| FinancialInstitutionIdentification | <FinInstId> | |
| BICFI | <BICFI> | DDDDLLULL |
| CreditorAgentAccount | <CdttrAgAcct> | |
| Identification | <Id> | |
| Other | <Othr> | |
| Identification | <Id> | 24538877443 |
| Creditor | <Cdttr> | |
| FinancialInstitutionIdentification | <FinInstId> | |
| BICFI | <BICFI> | BBBBITTT |
| CreditorAccount | <CdttrAcct> | |
| Identification | <Id> | |
| Other | <Othr> | |
| Identification | <Id> | 99566ZZ876 |
| Currency | <Ccy> | SEK |

## Message Instance

```
<FICdtTrf>
    <GrpHdr>
        <MsgId>CCCC/151022-SSK/075</MsgId>
        <CreDtTm>2015-10-22T09:00:00</CreDtTm>
        <NbOfTxs>1</NbOfTxs>
        <SttlmInf>
            <SttlmMtd>CLRG</SttlmMtd>
            <ClrSys>
                <Cd>SSK</Cd>
            </ClrSys>
        </SttlmInf>
        <InstgAgt>
            <FinInstId>
                <BICFI>CCCCSESS</BICFI>
            </FinInstId>
        </InstgAgt>
        <InstdAgt>
            <FinInstId>
                <BICFI>FFFFSESS</BICFI>
            </FinInstId>
        </InstdAgt>
    </GrpHdr>
    <CdtTrfTxInf>
```

---

<!-- Page 135 -->

```xml
</PmtId>
    <InstdId>CCCC/151022-SSK/075/1</InstdId>
    <EndToEndId>BBBTTT4148AAAAPP</EndToEndId>
    <TxId>AAAA/151020-SEK/005/1</TxId>
</PmtId>
<IntrBkSttlmAmt Ccy="SEK">100000000</IntrBkSttlmAmt>
<IntrBkSttlmDt>2015-10-22</IntrBkSttlmDt>
<Dbtr>
    <FinInstnId>
        <BICFI>AAAAFRPP</BICFI>
    </FinInstnId>
</Dbtr>
<CdtrAgt>
    <FinInstnId>
        <BICFI>DDDULLULL</BICFI>
    </FinInstnId>
</CdtrAgt>
<CdtrAgtAcct>
    <Id>
        <Othr>
            <Id>24538877443</Id>
        </Othr>
    </Id>
</CdtrAgtAcct>
<Cdtr>
    <FinInstnId>
        <BICFI>BBBBIITT</BICFI>
    </FinInstnId>
</Cdtr>
<CdtrAcct>
    <Id>
        <Othr>
            <Id>995566Z2876</Id>
        </Othr>
    </Id>
    <Ccy>SEK</Ccy>
</CdtrAcct>
</CdtrTrfTxInf>
</FIcdtTrf>
```

---

<!-- Page 136 -->

## 7.9.3 Third FinancialInstitutionCreditTransfer

### Description

FFFF sends a FinancialInstitutionCreditTransfer to the next party which is the creditor agent DDDD, Luxemburg, for whom they service a SEK account. On receipt, DDDD will credit the SEK account of its client BBBBITTT.

### Business Data

The third FinancialInstitutionCreditTransfer message, from FFFFSESS to DDDDLULL:



<table>
  <tr>
    <th>Element</th>
    <th>&lt;XMLtag&gt;</th>
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
    <td>FFFF/151022-SEK/110</td>
  </tr>
  <tr>
    <td>CreationDate Time</td>
    <td>&lt;CreDtTm&gt;</td>
    <td>2015-10-22T10:11:00</td>
  </tr>
  <tr>
    <td>NumberOfTransactions</td>
    <td>&lt;NbOfTxs&gt;</td>
    <td>1</td>
  </tr>
  <tr>
    <td>SettlementInformation</td>
    <td>&lt;SttlmInf&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>SettlementMethod</td>
    <td>&lt;SttlmMtd&gt;</td>
    <td>INGA</td>
  </tr>
  <tr>
    <td>SettlementAccount</td>
    <td>&lt;SttlmAcct&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>Identification</td>
    <td>&lt;Id&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>Other</td>
    <td>&lt;Othr&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>Identification</td>
    <td>&lt;Id&gt;</td>
    <td>24538877443</td>
  </tr>
  <tr>
    <td>InstructingAgent</td>
    <td>&lt;InstdAg&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>FinancialInstitutionIdentification</td>
    <td>&lt;FinInstId&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>BICFI</td>
    <td>&lt;BICFI&gt;</td>
    <td>FFFFSESS</td>
  </tr>
  <tr>
    <td>InstructedAgent</td>
    <td>&lt;InstdAg&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>FinancialInstitutionIdentification</td>
    <td>&lt;FinInstId&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>BICFI</td>
    <td>&lt;BICFI&gt;</td>
    <td>DDDDLULL</td>
  </tr>
  <tr>
    <td>CreditTransferTransactionInformation</td>
    <td>&lt;CdtTrfTxInf&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>PaymentIdentification</td>
    <td>&lt;PmtId&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>InstructionIdentification</td>
    <td>&lt;InstrId&gt;</td>
    <td>FFFF/151022-SEK/110/1</td>
  </tr>
  <tr>
    <td>EndToEndIdentification</td>
    <td>&lt;EndToEndId&gt;</td>
    <td>BBBBTTT4148AAAAAPP</td>
  </tr>
  <tr>
    <td>Transaction Identification</td>
    <td>&lt;TxId&gt;</td>
    <td>AAAA/151020-SEK/005/1</td>
  </tr>
  <tr>
    <td>IntraBankSettlementAmount</td>
    <td>&lt;IntrBkSttlmAmt&gt;</td>
    <td>SEK 100.000.000</td>
  </tr>
  <tr>
    <td>IntraBankSettlementDate</td>
    <td>&lt;IntrBkSttlmDt&gt;</td>
    <td>2015-10-22</td>
  </tr>
  <tr>
    <td>Debtor</td>
    <td>&lt;Dbtr&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>FinancialInstitutionIdentification</td>
    <td>&lt;FinInstId&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>BICFI</td>
    <td>&lt;BICFI&gt;</td>
    <td>AAAARFPP</td>
  </tr>
  <tr>
    <td>DebtorAgent</td>
    <td>&lt;DbtrAg&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>FinancialInstitutionIdentification</td>
    <td>&lt;FinInstId&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>BICFI</td>
    <td>&lt;BICFI&gt;</td>
    <td>CCCCSESS</td>
  </tr>
  <tr>
    <td>Creditor</td>
    <td>&lt;Cdtr&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>FinancialInstitutionIdentification</td>
    <td>&lt;FinInstId&gt;</td>
    <td></td>
  </tr>
</table>

---

<!-- Page 137 -->

| Element | XMLTag | Content |
| :--- | :--- | :--- |
| BICFI | <BICFI> | BBBBITTT |
| CreditorAccount | <Cdt rAcct> | |
| Identification | <Id> | |
| Other | <Othr> | |
| Identification | <Id> | 99556622876 |
| Currency | <Ccy> | SEK |

**Message Instance**

```xml
<FICdtTrf>
    <GrpHdr>
        <MsgId>FFFF/151022-SEK/110</MsgId>
        <CreDtTm>2015-10-22T10:11:00</CreDtTm>
        <NbOfTxs>1</NbOfTxs>
        <SttlmInf>
            <SttlmMtd>INGA</SttlmMtd>
            <SttlmAcct>
                <Id>
                    <Othr>
                        <Id>2453888877443</Id>
                    </Othr>
                </Id>
            </SttlmAcct>
        </SttlmInf>
        <InstdAgt>
            <FinInstnId>
                <BICFI>FFFFSESS</BICFI>
            </FinInstnId>
        </InstdAgt>
        <InstdAgt>
            <FinInstnId>
                <BICFI>DDDDULLL</BICFI>
            </FinInstnId>
        </InstdAgt>
    </GrpHdr>
    <CdtTrfTxInf>
        <PmtId>
            <InstrId>FFFF/151022-SEK/110/1</InstrId>
            <EndToEndId>BBB8TT4148AAAAPP</EndToEndId>
```

---

<!-- Page 138 -->

```xml
<TxId>AAAA/151020-SEK/005/1</TxId>
</PmtId>
<IntrBkSttlmAmt Ccy="SEK">100000000</IntrBkSttlmAmt>
<IntrBkSttlmDt>2015-10-22</IntrBkSttlmDt>
<Dbtr>
    <FinInstnId>
        <BICFI>AAAAFRPP</BICFI>
    </FinInstnId>
</Dbtr>
<DbtrAgt>
    <FinInstnId>
        <BICFI>CCCCSESS</BICFI>
    </FinInstnId>
</DbtrAgt>
<Cdtr>
    <FinInstnId>
        <BICFI>BBBBIITT</BICFI>
    </FinInstnId>
</Cdtr>
<CdtrAcct>
    <Id>
        <Othr>
            <Id>995566ZZ2876</Id>
        </Othr>
    </Id>
    <Ccy>SEK</Ccy>
</CdtrAcct>
</CdtTrfTxInf>
</FITcdtTrf>
```

---

<!-- Page 139 -->

## 7.10 FinancialInstitutionDirectDebit pacs.010.001.06

### Description

Bank MMMM instructs Bank NNNN to debit the account of Bank PPPP for 2500 EUR and Bank OOOO for 5000 EUR in favour of its account at Bank QQQQ with value date 21 November 2015.

### Business Data

The FinancialInstitutionDirectDebit message, from Bank MMMMBEBB to Bank NNNNDEFF:



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
    <td>MMMM/151121 PPPP_OOOO_EUR</td>
  </tr>
  <tr>
    <td>CreationDate Time</td>
    <td>&lt;CreDtTm&gt;</td>
    <td>2015-11-20T16:00:00</td>
  </tr>
  <tr>
    <td>NumberOfTransactions</td>
    <td>&lt;NbOfTxs&gt;</td>
    <td>2</td>
  </tr>
  <tr>
    <td>InstructingAgent</td>
    <td>&lt;InstgAgt&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>FinancialInstitutionIdentification</td>
    <td>&lt;FinInstnId&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>BICFI</td>
    <td>&lt;BICFI&gt;</td>
    <td>MMMMBE BB</td>
  </tr>
  <tr>
    <td>InstructedAgent</td>
    <td>&lt;InstdAgt&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>FinancialInstitutionIdentification</td>
    <td>&lt;FinInstnId&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>BICFI</td>
    <td>&lt;BICFI&gt;</td>
    <td>NNNNDEFF</td>
  </tr>
  <tr>
    <td>CreditInstruction</td>
    <td>&lt;CdtTrfTxInf&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>CreditIdentification</td>
    <td>&lt;CdtId&gt;</td>
    <td>MMMM/151121 PPPP_OOOO_EUR_7500</td>
  </tr>
  <tr>
    <td>BatchBooking</td>
    <td>&lt;BtchBookg&gt;</td>
    <td>true</td>
  </tr>
  <tr>
    <td>creditor agent</td>
    <td>&lt;CdtrAgt&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>FinancialInstitutionIdentification</td>
    <td>&lt;FinInstnId&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>BICFI</td>
    <td>&lt;BICFI&gt;</td>
    <td>QQQQFRPP</td>
  </tr>
  <tr>
    <td>creditor agentAccount Identification</td>
    <td>&lt;CdtrAgtAcct&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>Identification</td>
    <td>&lt;Id&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>IBAN</td>
    <td>&lt;IBAN&gt;</td>
    <td>DE89370400440532013000</td>
  </tr>
  <tr>
    <td>creditor</td>
    <td>&lt;Cdt&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>FinancialInstitutionIdentification</td>
    <td>&lt;FinInstnId&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>BICFI</td>
    <td>&lt;BICFI&gt;</td>
    <td>MMMMBE BB</td>
  </tr>
  <tr>
    <td>creditorAccount</td>
    <td>&lt;CdtrAcct&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>Identification</td>
    <td>&lt;Id&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>IBAN</td>
    <td>&lt;IBAN&gt;</td>
    <td>FR1420041010050500013M02606</td>
  </tr>
  <tr>
    <td>DirectDebitTransactionInformation</td>
    <td>&lt;DrctDbtTxInf&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>PaymentIdentification</td>
    <td>&lt;PmtId&gt;</td>
    <td></td>
  </tr>
  <tr>
    <td>InstructionIdentification</td>
    <td>&lt;InstrId&gt;</td>
    <td>MMMM/151121 PPPP_OOOO_EUR_2500</td>
  </tr>
  <tr>
    <td>EndToEndIdentification</td>
    <td>&lt;EndToEndId&gt;</td>
    <td>REFERENCE0001</td>
  </tr>
</table>

---

<!-- Page 140 -->

| Element | <XMLTag> | Content |
| :--- | :--- | :--- |
| Transaction Identification | <TxId> | PPPP_2500 |
| InterbankSettlementAmount | <IntrBkSttlmAmt> | EUR2500 |
| InterbankSettlementDate | <IntrBkSttlmDt> | 2015-11-21 |
| debtor | <Dbtr> | |
| FinancialInstitutionIdentification | <FinInstId> | |
| BICFI | <BICFI> | PPPPDKKK |
| debtor agent | <DbtrAgt> | |
| FinancialInstitutionIdentification | <FinInstId> | |
| BICFI | <BICFI> | NNNNDEFF |
| DirectDebitTransactionInformation | <DrctDbtTxInf> | |
| PaymentIdentification | <PmtId> | |
| InstructionIdentification | <InstrId> | MMMM/151121 PPPP_OOOO_EUR_5000 |
| EndToEndIdentification | <EndToEndId> | REFERENCE0002 |
| Transaction Identification | <TxId> | OOOO_5000 |
| InterbankSettlementAmount | <IntrBkSttlmAmt> | EUR5000 |
| InterbankSettlementDate | <IntrBkSttlmDt> | 2015-11-21 |
| debtor | <Dbtr> | |
| FinancialInstitutionIdentification | <FinInstId> | |
| BICFI | <BICFI> | OOOOATWW |
| debtor agent | <DbtrAgt> | |
| FinancialInstitutionIdentification | <FinInstId> | |
| BICFI | <BICFI> | NNNNDEFF |

## Message Instance

```xml
<FIDrctDbt>
    <GrpHd>
        <MsgId>MMMM/151121 PPPP_OOOO_EUR</MsgId>
        <CreDtTm>2015-11-20T16:00:00</CreDtTm>
        <NbOfTxs>2</NbOfTxs>
        <InstgAgt>
            <FinInstId>
                <BICFI>MMMMBEBA</BICFI>
            </FinInstId>
        </InstgAgt>
        <InstdAgt>
            <FinInstId>
                <BICFI>NNNNDEFF</BICFI>
            </FinInstId>
```

---

<!-- Page 141 -->

```
</InstdAgt>
</GrpHdr>
<CdtInstr>
    <CdtId>MMMM/151121 PPPP_OOOO_EUR_7500</CdtId>
    <BtchBookg>true</BtchBookg>
    <CdtTrAgt>
        <FinInstnId>
            <BICFI>QQQQFRPP</BICFI>
        </FinInstnId>
    </CdtTrAgt>
    <CdtTrAgtAcct>
        <Id>
            <IBAN>DE89370400440532013000</IBAN>
        </Id>
    </CdtTrAgtAcct>
    <CdtTr>
        <FinInstnId>
            <BICFI>MMMMMBEBB</BICFI>
        </FinInstnId>
    </CdtTr>
    <CdtTrAcct>
        <Id>
            <IBAN>FR1420041010050500013M02606</IBAN>
        </Id>
    </CdtTrAcct>
    <DrcctDbtTxInf>
        <RmtId>
            <InstdId>MMMM/151121 PPPP_OOOO_EUR_2500</InstdId>
            <EndToEndId>REFERENCE0001</EndToEndId>
            <TxId>PPPP_2500</TxId>
        </RmtId>
        <IntrBkSttlmAmt Ccy="EUR">2500</IntrBkSttlmAmt>
        <IntrBkSttlmDt>2015-11-21</IntrBkSttlmDt>
        <Dbtr>
            <FinInstnId>
                <BICFI>PPPPDKKK</BICFI>
            </FinInstnId>
        </Dbtr>
        <DbtrAgt>
```

---

<!-- Page 142 -->

```xml
</FinInstnId>
<BICFI>NNNNDEFF</BICFI>
</FinInstnId>
</DbtrAgt>
</DrctDbtTxInf>
<DrctDbtTxInf>
<PmtId>
<InstdId>MMMM/151121 PPPP_OOOO_EUR_5000</InstdId>
<EndToEndId>REFERENCE0002</EndToEndId>
<TxId>OOOO_5000</TxId>
</PmtId>
<IntrBkSttlmAmt Ccy="EUR">5000</IntrBkSttlmAmt>
<IntrBkSttlmDt>2015-11-21</IntrBkSttlmDt>
<Dbtr>
<FinInstnId>
<BICFI>OOOOATWW</BICFI>
</FinInstnId>
</Dbtr>
<DbtrAgt>
<FinInstnId>
<BICFI>NNNNDEFF</BICFI>
</FinInstnId>
</DbtrAgt>
</DrctDbtTxInf>
</CdtInstr>
</FIDrctDbt>
```

## 7.11 FIToFIPaymentStatusRequest - pacs.028.001.06

### Description

This example relates to the instruction message in section 7.6.1, a FIToFICustomerCreditTransfer message sent by BBBBU533 to AAAAGB2L. No FIToFIPaymentStatusReport message was received yet, but BBBBU533 wants to know the status of the instruction. BBBBU533 therefore sends a FIToFIPaymentStatusRequest message to request a FIToFIPaymentStatusReport.

### Business Data

The FIToFIPaymentStatusRequest message, from Bank BBBBU533 to Bank AAAAGB2L:



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
  </tbody>
</table>

---

<!-- Page 143 -->

| Element | XMLTag | Content |
| :--- | :--- | :--- |
| MessageIdentification | <MsgId> | BBBB/150928-CCT/JPY/456 |
| CreationDateTime | <CreDtTm> | 2015-09-28T16:06:00 |
| InstructingAgent | <InstdAg> | |
| FinancialInstitutionIdentification | <FinInstnId> | |
| BICFI | <BICF> | BBBBUS33 |
| InstructedAgent | <InstdAg> | |
| FinancialInstitutionIdentification | <FinInstnId> | |
| BICFI | <BICF> | AAAAGB2L |
| OriginalGroupInformation | <OrgnlGrpInf> | |
| OriginalMessageIdentification | <OrgnlMsgId> | BBBB/150928-CCT/JPY/123 |
| OriginalMessageNameIdentification | <OrgnlMsgNmId> | pacs.008.001.12 |
| OriginalCreationDateAndTime | <OrgnlCreDtTm> | 2015-09-28T16:00:00 |
| TransactionInformation | <TxInf> | |
| StatusRequestIdentification | <StsReqId> | BBBB/150928-CCT/JPY/456&Request |
| OriginalInstructionIdentification | <OrgnlInstrId> | BBBB/150928-CCT/JPY/123/1 |
| OriginalEndToEndIdentification | <OrgnlEndToEndId> | ABC/4562/2015-09-08 |
| OriginalTransactionIdentification | <OrgnlTxId> | BBBB/150928-CCT/JPY/123/1 |
| AcceptanceDateTime | <AccepDtTm> | 2015-09-28T15:45:00 |
| OriginalTransactionReference | <OrgnlTxRef> | |
| InterbankSettlementAmount | <IntrBkSttlmAmt> | JPY10000000 |
| InterbankSettlementDate | <IntrBkSttlmDt> | 2015-09-28 |
| PaymentTypeInformation | <PmtTpInf> | |
| InstructionPriority | <InstrPrty> | NORM |
| RemittanceInformation | <RmtInf> | |
| Structured | <Strd> | |
| ReferredDocumentInformation | <RfrdDocInf> | |
| Type | <Tp> | |
| CodeOrProprietary | <CdOrPrtry> | |
| Code | <Cd> | CINV |
| Number | <Nb> | 4562 |
| RelatedDate | <RltdDt> | |
| Type | <Tp> | |
| Code | <Cd> | INDA |
| Date | <Dt> | 2015-09-08 |
| Debtor | <Dbtr> | |
| Name | <Nm> | ABC Corporation |

---

<!-- Page 144 -->

| Element | XMLTag | Content |
|---|---|---|
| PostalAddress | <PstlAdr> | |
| StreetName | <StrtNm> | Times Square |
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
| BICFI | <BICF> | BBBBUS33 |
| CreditorAgent | <CdtrAgt> | |
| FinancialInstitutionIdentification | <FinInstlId> | |
| BICFI | <BICF> | AAAAGB2L |
| Creditor | <Cdtr> | |
| Name | <Name> | DEF Electronics |
| PostalAddress | <PstlAdr> | |
| StreetName | <StrtNm> | Mark Lane |
| BuildingNumber | <BldgNb> | 55 |
| PostCode | <PstCd> | EC3R7NE |
| TownName | <TwnNm> | London |
| Country | <Ctry> | GB |
| AddressLine | <AdrLine> | Corn Exchange 5th Floor |
| CreditorAccount | <CdtrAcct> | |
| Identification | <Id> | |
| Other | <Othr> | |
| Identification | <Id> | 23683707994215 |

## Message Instance

```xml
<FIToFIPmtStsReq>
    <GrpHd>
        <MsgId>BBB8/150929-CCT/JPY/456</MsgId>
        <CreDtTm>2015-09-28T16:06:00</CreDtTm>
        <InstgAgt>
            <FinInstlId>
                <BICF>BBBBUS33</BICF>
```

---

<!-- Page 145 -->

```
</FinInstnId>
</InstgAgt>
<InstdAgt>
  <FinInstnId>
    <BICFI>AAAAAGB2L</BICFI>
  </FinInstnId>
</InstdAgt>
</GrpHdr>
<OrgnlGrpInf>
  <OrgnlMsgId>BBBB/150928-CCT/JPY/123</OrgnlMsgId>
  <OrgnlMsgNmId>pac.008.001.12</OrgnlMsgNmId>
  <OrgnlCreDtTm>2015-09-28T16:00:00</OrgnlCreDtTm>
</OrgnlGrpInf>
<TxInf>
  <StsReqId>BBBB/150928-CCT/JPY/456Request</StsReqId>
  <OrgnlInstrId>BBBB/150928-CCT/JPY/123/1</OrgnlInstrId>
  <OrgnlEndToEndId>ABC/4562/2015-09-08</OrgnlEndToEndId>
  <OrgnlTxId>BBBB/150928-CCT/JPY/123/1</OrgnlTxId>
  <AcctpnctDtTm>2015-09-28T15:45:00</AcctpnctDtTm>
  <OrgnlTxRef>
    <IntrBkSttlmAmt Ccy="JPY">10000000</IntrBkSttlmAmt>
    <IntrBkSttlmDt>2015-09-28</IntrBkSttlmDt>
    <PmtTpInf>
      <InstrPrty>NORM</InstrPrty>
    </PmtTpInf>
    <RmtInf>
      <Strd>
        <RfrdDocInf>
          <Tp>
            <CdOrPrty>
              <Cd>CINV</Cd>
            </CdOrPrty>
          </Tp>
          <Nb>4562</Nb>
          <RltDt>
            <Tp>
              <Cd>INDA</Cd>
            </Tp>
            <Dt>2015-09-08</Dt>
```

---

<!-- Page 146 -->

```
</RltdDt>
</RfrdDocInf>
</Strd>
<RmtInf>
<Dbtr>
<Pty>
<Nm>ABC Corporation</Nm>
<PstlAdr>
<StrtNm>Times Square</StrtNm>
<BldgNb>7</BldgNb>
<PstCd>NY 10036</PstCd>
<TwnNm>New York</TwnNm>
<Ctry>US</Ctry>
</PstlAdr>
</Pty>
</Dbtr>
<DbtrAcct>
<Id>
<Othr>
<Id>00125574999</Id>
</Othr>
</Id>
</DbtrAcct>
<DbtrAgt>
<FinInstnId>
<BICFI>BBBEBUS33</BICFI>
</FinInstnId>
</DbtrAgt>
<CdtrAgt>
<FinInstnId>
<BICFI>AAAAGB2L</BICFI>
</FinInstnId>
</CdtrAgt>
<Cdtr>
<Pty>
<Nm>DEF Electronics</Nm>
<PstlAdr>
<StrtNm>Mark Lane</StrtNm>
<BldgNb>55</BldgNb>
```

---

<!-- Page 147 -->

<PstCd>EC3R7NE</PstCd>
<TwnNm>London</TwnNm>
<Ctry>GB</Ctry>
<AdrLine>Corn Exchange 5th Floor</AdrLine>
</PstAd>
</Pty>
</Cdtr>
<CdtrAcct>
<Id>
<Othr>
<Id>23683707994215</Id>
</Othr>
</Id>
</CdtrAcct>
</OrgnlTxRef>
</TxInf>
</FIToFIPmtStsReq>

---

<!-- Page 148 -->

Message Definition Report - Part 1                                                                 Revision Record

# 8 Revision Record

| Revision | Date | Author | Description | Sections affected |
| :--- | :--- | :--- | :--- | :--- |
| 1.0 | December 2024 | Swift | Draft version for SEG review | All |
| 2.0 | February 2025 | ISO 20022 RA | Approved version | All |

**Disclaimer:**

Although the Registration Authority has used all reasonable efforts to ensure accuracy of the contents of the iso20022.org website and the information published thereon, the Registration Authority assumes no liability whatsoever for any inadvertent errors or omissions that may appear thereon. Moreover, the information is provided on an "as is" basis. The Registration Authority disclaims all warranties and conditions, either express or implied, including but not limited to implied warranties of merchantability, title, non-infringement and fitness for a particular purpose.

The Registration Authority shall not be liable for any direct, indirect, special or consequential damages arising out of the use of the information published on the iso20022.org website, even if the Registration Authority has been advised of the possibility of such damages.

**Intellectual Property Rights:**

The ISO 20022 MessageDefinitions described in this document were contributed by SWIFT. The ISO 20022 IPR policy is available at www.ISO20022.org > About ISO 20022 > Intellectual Property Rights.