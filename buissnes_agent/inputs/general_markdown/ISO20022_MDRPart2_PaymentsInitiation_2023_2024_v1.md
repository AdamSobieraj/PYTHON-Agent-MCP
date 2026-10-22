<!-- Page 1 -->

ISO 20022

# Payments Initiation - Maintenance 2023 - 2024

# Message Definition Report - Part 2

**Approved by the Payments SEG on 08 January 2024**

This document provides details of the Message Definitions for Payments Initiation - Maintenance 2023 - 2024.

March 2024

---

<!-- Page 2 -->

# Table of Contents

**1** **Message Set Overview** .................................................................................................................... 3

1.1 List of MessageDefinitions .................................................................................................................... 3

**2** **pain.001.001.12 CustomerCreditTransferInitiationV12** .................................................................................................................... 4

2.1 MessageDefinition Functionality .................................................................................................................... 4

2.2 Structure .................................................................................................................... 6

2.3 Constraints .................................................................................................................... 10

2.4 Message Building Blocks .................................................................................................................... 14

**3** **pain.002.001.14 CustomerPaymentStatusReportV14** .................................................................................................................... 78

3.1 MessageDefinition Functionality .................................................................................................................... 78

3.2 Structure .................................................................................................................... 79

3.3 Constraints .................................................................................................................... 84

3.4 Message Building Blocks .................................................................................................................... 87

**4** **pain.007.001.12 CustomerPaymentReversalV12** .................................................................................................................... 163

4.1 MessageDefinition Functionality .................................................................................................................... 163

4.2 Structure .................................................................................................................... 164

4.3 Constraints .................................................................................................................... 168

4.4 Message Building Blocks .................................................................................................................... 171

**5** **pain.008.001.11 CustomerDirectDebitInitiationV11** .................................................................................................................... 239

5.1 MessageDefinition Functionality .................................................................................................................... 239

5.2 Structure .................................................................................................................... 240

5.3 Constraints .................................................................................................................... 244

5.4 Message Building Blocks .................................................................................................................... 246

**6** **Message Items Types** .................................................................................................................... 309

6.1 MessageComponents .................................................................................................................... 309

6.2 Message Datatypes .................................................................................................................... 407

---

<!-- Page 3 -->

# 1 Message Set Overview

## Introduction

This document describes the Payments Initiation message set. It includes the new version of the MessageDefinitions that have been added as part of the maintenance cycle 2023-2024 (See MCR #234) and approved by the Payments Standards Evaluation Group on 08 January 2024.

## 1.1 List of MessageDefinitions

The following table lists all MessageDefinitions described in this book.



<table>
  <thead>
    <tr>
      <th>MessageDefinition</th>
      <th>Definition</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>pain.001.001.12<br>CustomerCreditTransferInitiationV12</td>
      <td>The CustomerCreditTransferInitiation message is sent by the initiating party to the forwarding agent or debtor agent. It is used to request movement of funds from the debtor account to a Creditor.</td>
    </tr>
    <tr>
      <td>pain.002.001.14<br>CustomerPaymentStatusReportV14</td>
      <td>The CustomerPaymentStatusReport message is sent by an instructed agent to the previous party in the payment chain. It is used to inform this party about the positive or negative status of an instruction (either single or file). It is also used to report on a pending instruction.</td>
    </tr>
    <tr>
      <td>pain.007.001.12<br>CustomerPaymentReversalV12</td>
      <td>The CustomerPaymentReversal message is sent by the initiating party to the next party in the payment chain. It is used to reverse a payment previously executed.</td>
    </tr>
    <tr>
      <td>pain.008.001.11<br>CustomerDirectDebitInitiationV11</td>
      <td>The CustomerDirectDebitInitiation message is sent by the initiating party to the forwarding agent or creditor agent. It is used to request single or bulk collection(s) of funds from one or various debtor's account(s) for a creditor.</td>
    </tr>
  </tbody>
</table>

---

<!-- Page 4 -->

# 2 pain.001.001.12 CustomerCreditTransferInitiationV12

## 2.1 MessageDefinition Functionality

Scope

The CustomerCreditTransferInitiation message is sent by the initiating party to the forwarding agent or debtor agent. It is used to request movement of funds from the debtor account to a creditor.

Usage

The CustomerCreditTransferInitiation message can contain one or more customer credit transfer instructions.

The CustomerCreditTransferInitiation message is used to exchange:

- One or more instances of a credit transfer initiation;

- Payment transactions that result in book transfers at the debtor agent or payments to another financial institution;

- Payment transactions that result in an electronic cash transfer to the creditor account or in the emission of a cheque.

The message can be used in a direct or a relay scenario:

- In a direct scenario, the message is sent directly to the debtor agent. The debtor agent is the account servicer of the debtor.

- In a relay scenario, the message is sent to a forwarding agent. The forwarding agent acts as a concentrating financial institution. It will forward the CustomerCreditTransferInitiation message to the debtor agent.

The message can also be used by an initiating party that has authority to send the message on behalf of the debtor. This caters for example for the scenario of a payments factory initiating all payments on behalf of a large corporate.

The CustomerCreditTransferInitiation message can be used in domestic and cross-border scenarios.

The CustomerCreditTransferInitiation message must not be used by the debtor agent to execute the credit transfer instruction(s). The FitToFiCustomerCreditTransfer message must be used instead.

Outline

The CustomerCreditTransferInitiationV12 MessageDefinition is composed of 3 MessageBuildingBlocks:

A. GroupHeader

Set of characteristics shared by all individual transactions included in the message.

B. PaymentInformation

Set of characteristics that applies to the debit side of the payment transactions included in the credit transfer initiation.

---

<!-- Page 5 -->

C. Supplementary Data

Additional information that cannot be captured in the structured elements and/or any other specific block.

---

<!-- Page 6 -->

## 2.2 Structure



<table>
  <thead>
    <tr>
      <th>Or</th>
      <th>MessageElement/BuildingBlock/&lt;XML Tag&gt;</th>
      <th>Mult.</th>
      <th>Type</th>
      <th>Constr. No.</th>
      <th>Page</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td><i>Message root &lt;Document&gt; &lt;CstmrCdtTrfInit&gt;</i></td>
      <td>[1..1]</td>
      <td></td>
      <td>C32</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td><b>GroupHeader</b> &lt;GrpHdr&gt;</td>
      <td>[1..1]</td>
      <td></td>
      <td></td>
      <td>14</td>
    </tr>
    <tr>
      <td></td>
      <td><b>MessageIdentification</b> &lt;MsgId&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>14</td>
    </tr>
    <tr>
      <td></td>
      <td><b>CreationDateTime</b> &lt;CreDtTm&gt;</td>
      <td>[1..1]</td>
      <td>DateTime</td>
      <td></td>
      <td>14</td>
    </tr>
    <tr>
      <td></td>
      <td><b>Authorisation</b> &lt;AuthStrn&gt;</td>
      <td>[0..2]</td>
      <td>±</td>
      <td></td>
      <td>15</td>
    </tr>
    <tr>
      <td></td>
      <td><b>NumberOfTransactions</b> &lt;NbOfTxs&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>15</td>
    </tr>
    <tr>
      <td></td>
      <td><b>ControlSum</b> &lt;CtrlSum&gt;</td>
      <td>[0..1]</td>
      <td>Quantity</td>
      <td></td>
      <td>15</td>
    </tr>
    <tr>
      <td></td>
      <td><b>InitiatingParty</b> &lt;InitgPty&gt;</td>
      <td>[1..1]</td>
      <td>±</td>
      <td></td>
      <td>15</td>
    </tr>
    <tr>
      <td></td>
      <td><b>ForwardingAgent</b> &lt;FwdgAg&gt;</td>
      <td>[0..1]</td>
      <td>±</td>
      <td></td>
      <td>16</td>
    </tr>
    <tr>
      <td></td>
      <td><b>InitiationSource</b> &lt;InitnSrc&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>17</td>
    </tr>
    <tr>
      <td></td>
      <td><b>Name</b> &lt;Nm&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>17</td>
    </tr>
    <tr>
      <td></td>
      <td><b>Provider</b> &lt;Prvd&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>17</td>
    </tr>
    <tr>
      <td></td>
      <td><b>Version</b> &lt;Vrsn&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>18</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td><b>PaymentInformation</b> &lt;PmtInf&gt;</td>
      <td>[1..]</td>
      <td></td>
      <td>C4, C5, C6, C7, C8, C9, C14, C16, C23, C29, C30, C37, C10, C11, C12, C13, C35</td>
      <td>18</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td><b>PaymentInformationIdentification</b> &lt;PmtId&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>25</td>
    </tr>
    <tr>
      <td></td>
      <td><b>PaymentMethod</b> &lt;PmtMtd&gt;</td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td></td>
      <td>25</td>
    </tr>
    <tr>
      <td></td>
      <td><b>RequestedAdviceType</b> &lt;ReqdAdvcTp&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>26</td>
    </tr>
    <tr>
      <td></td>
      <td><b>CreditAdvice</b> &lt;CdtAdvc&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>26</td>
    </tr>
    <tr>
      <td>[Or</td>
      <td><b>Code</b> &lt;Cd&gt;</td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td></td>
      <td>26</td>
    </tr>
    <tr>
      <td>Or]</td>
      <td><b>Proprietary</b> &lt;Pry&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>27</td>
    </tr>
    <tr>
      <td></td>
      <td><b>DebitAdvice</b> &lt;DbtAdvc&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>27</td>
    </tr>
    <tr>
      <td>[Or</td>
      <td><b>Code</b> &lt;Cd&gt;</td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td></td>
      <td>27</td>
    </tr>
    <tr>
      <td>Or]</td>
      <td><b>Proprietary</b> &lt;Pry&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>27</td>
    </tr>
  </tbody>
</table>

---

<!-- Page 7 -->

| Or | MessageElement/BuildingBlock <XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | BatchBooking <BtchBkng> | [0..1] | Indicator | | 27 |
| | NumberOfTransactions <NbOfTxs> | [0..1] | Text | | 28 |
| | ControlSum <CtrlSum> | [0..1] | Quantity | | 28 |
| | PaymentTypeInformation <PmtTpInf> | [0..1] | ± | | 28 |
| | RequestedExecutionDate <ReqdExctnDt> | [1..1] | ± | | 28 |
| | PoolingAdjustmentDate <PoolgAdjstmntDt> | [0..1] | Date | | 29 |
| | Debtor <Dbtr> | [1..1] | ± | | 29 |
| | DebtorAccount <DbtrAcct> | [1..1] | ± | C21, C20 | 30 |
| | DebtorAgent <DbtrAgt> | [1..1] | ± | | 31 |
| | DebtorAgentAccount <DbtrAgtAcct> | [0..1] | ± | C21, C20 | 32 |
| | InstructionForDebtorAgent <InstrForDbtrAgt> | [0..1] | Text | | 33 |
| | UltimateDebtor <UltmtDbtr> | [0..1] | ± | | 33 |
| | ChargeBearer <ChrgBr> | [0..1] | CodeSet | | 34 |
| | ChargesAccount <ChrgsAcct> | [0..1] | ± | C21, C20 | 35 |
| | ChargesAccountAgent <ChrgsAcctAgt> | [0..1] | ± | | 36 |
| | CreditTransferTransactionInformation <CdtTrfTxInf> | [1..*] | | C22, C24, C25, C26, C27, C28, C34, C36 | 36 |
| | PaymentIdentification <PmtId> | [1..1] | ± | | 40 |
| | PaymentTypeInformation <PmtTpInf> | [0..1] | ± | | 41 |
| | Amount <Amt> | [1..1] | ± | | 41 |
| | ExchangeRateInformation <XchgRateInf> | [0..1] | | | 42 |
| | UnitCurrency <UnitCcy> | [0..1] | CodeSet | C1 | 42 |
| | ExchangeRate <XchgRate> | [0..1] | Rate | | 42 |
| | RateType <RateTp> | [0..1] | CodeSet | | 42 |
| | ContractIdentification <CtrctId> | [0..1] | Text | | 43 |
| | ChargeBearer <ChrgBr> | [0..1] | CodeSet | | 43 |
| | MandateRelatedInformation <MndtRltdInf> | [0..1] | ± | | 43 |
| | ChequeInstruction <ChqInstr> | [0..1] | | C15 | 44 |

---

<!-- Page 8 -->

| Or | MessageElement/BuildingBlock<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **ChequeType** <CheqTp> | [0..1] | CodeSet | | 45 |
| | **ChequeNumber** <CheqNb> | [0..1] | Text | | 46 |
| | **ChequeFrom** <CheqFr> | [0..1] | | | 46 |
| | **Name** <Nm> | [1..1] | Text | | 46 |
| | **Address** <Adr> | [1..1] | ± | | 47 |
| | **DeliveryMethod** <DlvryMtd> | [0..1] | | | 47 |
| (Or | **Code** <Cd> | [1..1] | CodeSet | | 48 |
| Or) | **Proprietary** <Prtry> | [1..1] | Text | | 48 |
| | **DeliverTo** <DlvryTo> | [0..1] | | | 48 |
| | **Name** <Nm> | [1..1] | Text | | 49 |
| | **Address** <Adr> | [1..1] | ± | | 49 |
| | **InstructionPriority** <InstrPrty> | [0..1] | CodeSet | | 49 |
| | **ChequeMaturityDate** <ChqMtrtyDt> | [0..1] | Date | | 50 |
| | **FormsCode** <FrmsCd> | [0..1] | Text | | 50 |
| | **MemoField** <MemoFld> | [0..2] | Text | | 50 |
| | **RegionalClearingZone** <RgnlClrZone> | [0..1] | Text | | 50 |
| | **PrintLocation** <PrntLocn> | [0..1] | Text | | 50 |
| | **Signature** <Sgntr> | [0..5] | Text | | 50 |
| | **UltimateDebtor** <UltmtDbtr> | [0..1] | ± | | 50 |
| | **IntermediaryAgent1** <IntrmyAgt1> | [0..1] | ± | | 51 |
| | **IntermediaryAgent1Account** <IntrmyAgt1Acct> | [0..1] | ± | C21, C20 | 52 |
| | **IntermediaryAgent2** <IntrmyAgt2> | [0..1] | ± | | 53 |
| | **IntermediaryAgent2Account** <IntrmyAgt2Acct> | [0..1] | ± | C21, C20 | 53 |
| | **IntermediaryAgent3** <IntrmyAgt3> | [0..1] | ± | | 54 |
| | **IntermediaryAgent3Account** <IntrmyAgt3Acct> | [0..1] | ± | C21, C20 | 55 |
| | **CreditorAgent** <CdtrAgt> | [0..1] | ± | | 56 |
| | **CreditorAgentAccount** <CdtrAgtAcct> | [0..1] | ± | C21, C20 | 56 |
| | **Creditor** <Cdtr> | [0..1] | ± | | 57 |
| | **CreditorAccount** <CdtrAcct> | [0..1] | ± | C21, C20 | 58 |

---

<!-- Page 9 -->

| Or | MessageElement/BuildingBlock=<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | UltimateCreditor <UltimiCditr> | [0..1] | ± | | 59 |
| | InstructionForCreditorAgent <InstrForCrditAgnt> | [0..*] | ± | | 60 |
| | InstructionForDebtorAgent <InstrForDbtrAgnt> | [0..1] | | | 61 |
| | Code <Cd> | [0..1] | CodeSet | | 61 |
| | InstructionInformation <InstrInf> | [0..1] | Text | | 61 |
| | Purpose <Purp> | [0..1] | ± | | 61 |
| | RegulatoryReporting <RgltryRptg> | [0..10] | ± | | 62 |
| | Tax <Tax> | [0..1] | | | 62 |
| | Creditor <Cditr> | [0..1] | ± | | 64 |
| | Debtor <Dbtr> | [0..1] | ± | | 64 |
| | UltimateDebtor <UltimiDbtr> | [0..1] | ± | | 64 |
| | AdministrationZone <AdminZone> | [0..1] | Text | | 65 |
| | ReferenceNumber <RefNbr> | [0..1] | Text | | 65 |
| | Method <Mtd> | [0..1] | Text | | 65 |
| | TotalTaxableBaseAmount <TtlTaxblBaseAmt> | [0..1] | Amount | C1, C18 | 65 |
| | TotalTaxAmount <TtlTaxAmt> | [0..1] | Amount | C1, C18 | 66 |
| | Date <Dt> | [0..1] | Date | | 66 |
| | SequenceNumber <SeqNbr> | [0..1] | Quantity | | 66 |
| | Record <Rcrd> | [0..*] | | | 66 |
| | Type <Tp> | [0..1] | Text | | 67 |
| | Category <Ctgy> | [0..1] | Text | | 67 |
| | CategoryDetails <CtgyDtls> | [0..1] | Text | | 67 |
| | DebtorStatus <DbtrSts> | [0..1] | Text | | 68 |
| | CertificateIdentification <CertId> | [0..1] | Text | | 68 |
| | FormsCode <FrmsCd> | [0..1] | Text | | 68 |
| | Period <Prd> | [0..1] | | | 68 |
| | Year <Yr> | [0..1] | Year | | 68 |
| | Type <Tp> | [0..1] | CodeSet | | 68 |
| | FromToDate <FrToDt> | [0..1] | ± | | 69 |
| | TaxAmount <TaxAmt> | [0..1] | | | 70 |
| | Rate <Rate> | [0..1] | Rate | | 70 |

---

<!-- Page 10 -->

| Or | MessageElement/BuildingBlock<XML Tag> | Mult. | Type | Constr. No. | Page |
| :--- | :--- | :--- | :--- | :--- | :--- |
| | **TaxableBaseAmount** `<TaxblBaseAmt>` | [0..1] | Amount | C1, C18 | 70 |
| | **TotalAmount** `<TtlAmt>` | [0..1] | Amount | C1, C18 | 70 |
| | **Details** `<Dtls>` | [0..*] | | | 71 |
| | **Period** `<Prd>` | [0..1] | | | 71 |
| | **Year** `<Yr>` | [0..1] | Year | | 71 |
| | **Type** `<Tp>` | [0..1] | CodeSet | | 72 |
| | **FromToDate** `<FrToDt>` | [0..1] | ± | | 72 |
| | **Amount** `<Amt>` | [1..1] | Amount | C1, C18 | 73 |
| | **AdditionalInformation** `<AddtlInf>` | [0..1] | Text | | 73 |
| | **RelatedRemittanceInformation** `<RltdRmtInf>` | [0..10] | | | 73 |
| | **RemittanceIdentification** `<RmtId>` | [0..1] | Text | | 74 |
| | **RemittanceLocationDetails** `<RmtLctnDtls>` | [0..*] | | | 74 |
| | **Method** `<Mtd>` | [1..1] | CodeSet | | 74 |
| | **ElectronicAddress** `<EltrncAdr>` | [0..1] | Text | | 75 |
| | **PostalAddress** `<PstlAdr>` | [0..1] | | | 75 |
| | **Name** `<Nm>` | [1..1] | Text | | 75 |
| | **Address** `<Adr>` | [1..1] | ± | | 75 |
| | **RemittanceInformation** `<RmtInf>` | [0..1] | ± | | 76 |
| | **SupplementaryData** `<SplmtryData>` | [0..*] | ± | C33 | 77 |
| | **SupplementaryData** `<SplmtryData>` | [0..*] | ± | C33 | 77 |

## 2.3 Constraints

**C1** **ActiveOrHistoricCurrency**

The Currency Code must be registered, or have already been registered. Valid active or historic currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and may be or not be withdrawn on the day the message containing the Currency is exchanged.

**C2** **AnyBIC**

Only a valid Business identifier code is allowed. Business identifier codes for financial or non-financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.

**C3** **BICFI**

Valid BICs for financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous characters.

---

<!-- Page 11 -->

C4 **ChargeBearerRule**

If ChargeBearer is present, then CreditTransferTransactionInformation/ChargeBearer is not allowed.

If CreditTransferTransactionInformation/ChargeBearer is present, then ChargeBearer is not allowed.

CreditTransferTransactionInformation/ChargeBearer and ChargeBearer may both be absent.

C5 **ChargesAccountAgentRule**

If ChargesAccountAgent is present, then it must contain a branch of the DebtorAgent. It must not contain a completely different agent.

C6 **ChargesAccountRule**

If ChargesAccountAgent is present, then ChargesAccount must be present.

C7 **ChequeAndCreditorAccountRule**

If PaymentMethod is CHK (Cheque), then CreditTransferTransactionInformation/CreditorAccount is not allowed.

C8 **ChequeDeliveryAndCreditorAgentRule**

If PaymentMethod is CHK (Cheque) and CreditTransferTransactionInformation/ChequeInstruction/DeliveryMethod/Code is present and is equal to MLFA (MailToFinalAgent), CRFA (CourierToFinalAgent), RGFA (RegisteredMailToFinalAgent) or PUFA (PickUpByFinalAgent), then CreditTransferTransactionInformation/CreditorAgent must be present.

C9 **ChequeDeliveryAndNoCreditorAgentRule**

If PaymentMethod is CHK (Cheque) and CreditTransferTransactionInformation/ChequeInstruction/DeliveryMethod/Code is present and different from MLFA (MailToFinalAgent), CRFA (CourierToFinalAgent), RGFA (RegisteredMailToFinalAgent) or PUFA (PickUpByFinalAgent), then CreditTransferTransactionInformation/CreditorAgent is not allowed.

C10 **ChequeFromGuideline**

CreditTransferTransactionInformation/ChequeInstruction/ChequeFrom may only be present if different from CreditTransferTransactionInformation/UltimateDebtor or Debtor.

C11 **ChequeInstructionDeliverToCreditorAgentGuideline**

If CreditTransferTransactionInformation/ChequeInstruction/DeliveryMethod is present and is ORFA (CourierToFinalAgent), MLFA (MailToFinalAgent), PUFA (PickUpByFinalAgent) or RGFA (RegisteredMailToFinalAgent), then CreditTransferTransactionInformation/ChequeInstruction/DeliverTo may only be present if different from CreditTransferTransactionInformation/Creditor.

C12 **ChequeInstructionDeliverToCreditorGuideline**

If PaymentInformation/CreditTransferTransactionInformation/ChequeInstruction/DeliveryMethod is present and is CRCD (CourierToCreditor), MLCD (MailToCreditor), PUCD (PickUpByCreditor) or RGCD (RegisteredMailToCreditor), then CreditTransferTransactionInformation/ChequeInstruction/DeliverTo may only be present if different from CreditTransferTransactionInformation/Creditor.

---

<!-- Page 12 -->

**C13** **ChequeInstructionDeliverToDebtorGuideline**

If CreditTransfer/TransactionInformation/ChequeInstruction/DeliveryMethod is present and if CreditTransfer/TransactionInformation/ChequeInstruction/DeliveryMethod/Code is CRDB (CourierToDebtor), MLDB (MailToDebtor), PUDb (PickUpByDebtor) or RGDB (RegisteredMailToDebtor), then CreditTransfer/TransactionInformation/ChequeInstruction/DeliverTo may only be present if different from Debtor.

**C14** **ChequeInstructionRule**

If PaymentMethod is different from CHK (Cheque), then CreditTransfer/TransactionInformation/ChequeInstruction is not allowed.

**C15** **ChequeMaturityDateRule**

If ChequeMaturityDate is present, then ChequeType must be present and equal to DRFT or ELDR.

**C16** **ChequeNoDeliveryAndNoCreditorAgentRule**

If PaymentMethod is CHK (Cheque) and CreditTransfer/TransactionInformation/ChequeInstruction/DeliveryMethod is not present, then CreditTransfer/TransactionInformation/CreditorAgent is not allowed.

**C17** **Country**

The code is checked against the list of country names obtained from the United Nations (ISO 3166, Alpha-2 code).

**C18** **CurrencyAmount**

The number of fractional digits (or minor unit of currency) must comply with ISO 4217.

Note: The decimal separator is a dot.

**C19** **IBAN**

A valid IBAN consists of all three of the following components: Country Code, check digits and BBAN.

**C20** **IdentificationAndProxyGuideline**

If the account identification is not defined through a conventional identification such as an email address or a mobile number, then the proxy element should be used for the identification of the account.

**C21** **IdentificationOrProxyPresenceRule**

Identification must be present or Proxy must be present. Both may be present.

**C22** **InstructionForCreditorAgentRule**

If InstructionForCreditorAgent/Code contains CHQB, then CreditorAccount is not allowed.

**C23** **InstructionForDebtorAgentRule**

If InstructionForDebtorAgent is present, then CreditTransfer/TransactionInformation/InstructionForDebtorAgent is not allowed.

If CreditTransfer/TransactionInformation/InstructionForDebtorAgent is present, then InstructionForDebtorAgent is not allowed.

CreditTransfer/TransactionInformation/InstructionForDebtorAgent and InstructionForDebtorAgent may both be absent.

---

<!-- Page 13 -->

| Code | Rule | Description |
| :--- | :--- | :--- |
| C24 | **IntermediaryAgent1AccountRule** | If IntermediaryAgent1Account is present, then IntermediaryAgent1 must be present. |
| C25 | **IntermediaryAgent2AccountRule** | If IntermediaryAgent2Account is present, then IntermediaryAgent2 must be present. |
| C26 | **IntermediaryAgent2Rule** | If IntermediaryAgent2 is present, then IntermediaryAgent1 must be present. |
| C27 | **IntermediaryAgent3AccountRule** | If IntermediaryAgent3Account is present, then IntermediaryAgent3 must be present. |
| C28 | **IntermediaryAgent3Rule** | If IntermediaryAgent3 is present, then IntermediaryAgent2 must be present. |
| C29 | **NonChequePaymentMethodRule** | If PaymentMethod is different from CHK (Cheque) and CreditTransferTransactionInformation/Creditor is not present, then CreditTransferTransactionInformation/CreditorAccount must be present. |
| C30 | **PaymentTypeInformationRule** | If PaymentTypeInformation is present, then CreditTransferTransactionInformation/PaymentTypeInformation is not allowed. |
| C31 | **RemittanceAmountAndTypeGuideline** | If Type/Code is equal to CREN, DUPA or REMI for RemittanceAmountAndType, RemittanceAmountAndType must not be repeated. |
| C32 | **SupplementaryDataRule** | The SupplementaryData building block at message level must not be used to provide additional information about a transaction. The SupplementaryData element at transaction level should be used for that purpose.<br>*This constraint is defined at the MessageDefinition level.* |
| C33 | **SupplementaryDataRule** | This component may not be used without the explicit approval of a SEG and submission to the RA of ISO 20022 compliant structure(s) to be used in the Envelope element. |
| C34 | **UltimateCreditorGuideline** | UltimateCreditor may only be present if different from Creditor. |
| C35 | **UltimateDebtorGuideline** | UltimateDebtor may only be present if different from Debtor. |
| C36 | **UltimateDebtorGuideline** | UltimateDebtor may only be present if different from Debtor. |
| C37 | **UltimateDebtorRule** | If UltimateDebtor is present, then CreditTransferTransactionInformation/UltimateDebtor is not allowed. |

---

<!-- Page 14 -->

If CreditTransferTransactionInformation/UltimateDebtor is present, then UltimateDebtor is not allowed.

CreditTransferTransactionInformation/UltimateDebtor and UltimateDebtor may both be absent.

## 2.4 Message Building Blocks

This chapter describes the MessageBuildingBlocks of this MessageDefinition.

### 2.4.1 GroupHeader <GrpHdr>

Presence: [1..1]

Definition: Set of characteristics shared by all individual transactions included in the message.

GroupHeader <GrpHdr> contains the following GroupHeader114 elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | **MessageIdentification** <MsgId> | [1..1] | Text | | 14 |
| | **CreationDateTime** <CreDtTm> | [1..1] | DateTime | | 14 |
| | **Authorisation** <Authstr> | [0..2] | ± | | 15 |
| | **NumberOfTransactions** <NbOfTxs> | [1..1] | Text | | 15 |
| | **ControlSum** <CtrlSum> | [0..1] | Quantity | | 15 |
| | **InitiatingParty** <InitgPty> | [1..1] | ± | | 15 |
| | **ForwardingAgent** <FwdgAgnt> | [0..1] | ± | | 16 |
| | **InitiationSource** <InitnSrc> | [0..1] | | | 17 |
| | **Name** <Nm> | [1..1] | Text | | 17 |
| | **Provider** <Prvd> | [0..1] | Text | | 17 |
| | **Version** <Vrsn> | [0..1] | Text | | 18 |

#### 2.4.1.1 MessageIdentification <MsgId>

Presence: [1..1]

Definition: Point to point reference, as assigned by the instructing party, and sent to the next party in the chain to unambiguously identify the message.

Usage: The instructing party has to make sure that MessageIdentification is unique per instructed party for a pre-agreed period.

Datatype: "Max35Text" on page 431

#### 2.4.1.2 CreationDateTime <CreDtTm>

Presence: [1..1]

Definition: Date and time at which the message was created.

Datatype: "ISODateTime" on page 425

---

<!-- Page 15 -->

## 2.4.1.3 Authorisation <Authn>

*Presence:* [0..2]

*Definition:* User identification or any user key to be used to check whether the initiating party is allowed to initiate transactions from the account specified in the message.

Usage: The content is not of a technical nature, but reflects the organisational structure at the initiating side.

The authorisation element can typically be used in relay scenarios, payment initiations, payment returns or payment reversals that are initiated on behalf of a party different from the initiating party.

**Authorisation <Authn>** contains one of the following elements (see “*Authorisation1Choice*” on page 336 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| (Or | Code <Cd> | [1..1] | CodeSet | | 336 |
| Or) | Proprietary <Ptry> | [1..1] | Text | | 336 |

## 2.4.1.4 NumberOfTransactions <NbOfTxs>

*Presence:* [1..1]

*Definition:* Number of individual transactions contained in the message.

*Datatype:* “*Max15NumericText*” on page 430

## 2.4.1.5 ControlSum <CtrlSum>

*Presence:* [0..1]

*Definition:* Total of all individual amounts included in the message, irrespective of currencies.

*Datatype:* “*DecimalNumber*” on page 427

## 2.4.1.6 InitiatingParty <InitgPty>

*Presence:* [1..1]

*Definition:* Party that initiates the payment.

Usage: This can either be the debtor or the party that initiates the credit transfer on behalf of the debtor.

---

<!-- Page 16 -->

InitiatingParty <InitgPty> contains the following elements (see "PartyIdentification27" on page 336 for details)



<table>
  <thead>
    <tr>
      <th>Or</th>
      <th>MessageElement&lt;XML Tag&gt;</th>
      <th>Mult.</th>
      <th>Type</th>
      <th>Constr. No.</th>
      <th>Page</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td>Name &lt;Nm&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>337</td>
    </tr>
    <tr>
      <td></td>
      <td>PostalAddress &lt;PstlAdr&gt;</td>
      <td>[0..1]</td>
      <td>±</td>
      <td></td>
      <td>338</td>
    </tr>
    <tr>
      <td></td>
      <td>Identification &lt;Id&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>338</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>OrganisationIdentification &lt;OrgId&gt;</td>
      <td>[1..1]</td>
      <td></td>
      <td></td>
      <td>339</td>
    </tr>
    <tr>
      <td></td>
      <td>AnyBIC &lt;AnyBIC&gt;</td>
      <td>[0..1]</td>
      <td>IdentifierSet</td>
      <td>C5</td>
      <td>340</td>
    </tr>
    <tr>
      <td></td>
      <td>LEI &lt;LEI&gt;</td>
      <td>[0..1]</td>
      <td>IdentifierSet</td>
      <td></td>
      <td>340</td>
    </tr>
    <tr>
      <td></td>
      <td>Other &lt;Othr&gt;</td>
      <td>[0..*]</td>
      <td></td>
      <td></td>
      <td>340</td>
    </tr>
    <tr>
      <td></td>
      <td>Identification &lt;Id&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td></td>
      <td>SchemeName &lt;SchmeNm&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Code &lt;Cd&gt;</td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Proprietary &lt;Ptry&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td></td>
      <td>Issuer &lt;Issr&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>PrivateIdentification &lt;PrvtId&gt;</td>
      <td>[1..1]</td>
      <td></td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td></td>
      <td>DateAndPlaceOfBirth &lt;DtAndPlcOfBirth&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>342</td>
    </tr>
    <tr>
      <td></td>
      <td>BirthDate &lt;BirthDt&gt;</td>
      <td>[1..1]</td>
      <td>Date</td>
      <td></td>
      <td>342</td>
    </tr>
    <tr>
      <td></td>
      <td>ProvinceOfBirth &lt;PrvcOfBirth&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>342</td>
    </tr>
    <tr>
      <td></td>
      <td>CityOfBirth &lt;CityOfBirth&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>CountryOfBirth &lt;CtryOfBirth&gt;</td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td>C7</td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>Other &lt;Othr&gt;</td>
      <td>[0..*]</td>
      <td></td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>Identification &lt;Id&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>SchemeName &lt;SchmeNm&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Code &lt;Cd&gt;</td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td></td>
      <td>344</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Proprietary &lt;Ptry&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>344</td>
    </tr>
    <tr>
      <td></td>
      <td>Issuer &lt;Issr&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>344</td>
    </tr>
    <tr>
      <td></td>
      <td>CountryOfResidence &lt;CtryOfRes&gt;</td>
      <td>[0..1]</td>
      <td>CodeSet</td>
      <td>C7</td>
      <td>344</td>
    </tr>
    <tr>
      <td></td>
      <td>ContactDetails &lt;CtctDtls&gt;</td>
      <td>[0..1]</td>
      <td>±</td>
      <td></td>
      <td>344</td>
    </tr>
  </tbody>
</table>

## 2.4.1.7 ForwardingAgent <FwdgAgt>

*Presence:* [0..1]

*Definition:* Financial institution that receives the instruction from the initiating party and forwards it to the next agent in the payment chain for execution.

---

<!-- Page 17 -->

ForwardingAgent <FwdgAgt> contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on page 320 for details)



| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | FinancialInstitutionIdentification <FinInstnId> | [1..1] |  |  | 321 |
| | BICFI <BICFI> | [0..1] | IdentifierSet | C6 | 321 |
| | ClearingSystemMemberIdentification <ClrSysMmbId> | [0..1] | ± |  | 322 |
| | LEI <LEI> | [0..1] | IdentifierSet |  | 322 |
| | Name <Nm> | [0..1] | Text |  | 322 |
| | PostalAddress <PstlAdr> | [0..1] | ± |  | 322 |
| | Other <Othr> | [0..1] | ± |  | 323 |
| | BranchIdentification <BrnchId> | [0..1] |  |  | 324 |
| | Identification <Id> | [0..1] | Text |  | 324 |
| | LEI <LEI> | [0..1] | IdentifierSet |  | 324 |
| | Name <Nm> | [0..1] | Text |  | 324 |
| | PostalAddress <PstlAdr> | [0..1] | ± |  | 324 |

## 2.4.1.8 InitiationSource <InitnSrc>

*Presence:* [0..1]

*Definition:* Source application or software used to initiate the payment.

**InitiationSource <InitnSrc>** contains the following **PaymentInitiationSource1** elements



| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Name <Nm> | [1..1] | Text |  | 17 |
| | Provider <Prvd> | [0..1] | Text |  | 17 |
| | Version <Vrsn> | [0..1] | Text |  | 18 |

### 2.4.1.8.1 Name <Nm>

*Presence:* [1..1]

*Definition:* Name of the application or software used to initiate the payment.

*Datatype:* "Max140Text" on page 429

### 2.4.1.8.2 Provider <Prvd>

*Presence:* [0..1]

*Definition:* Provider of the application or software used to initiate the payment.

*Datatype:* "Max35Text" on page 431

---

<!-- Page 18 -->

2.4.1.8.3 Version <Vrsn>

*Presence:* [0..1]

*Definition:* Version of the application or software used to initiate the payment.

*Datatype:* "Max35Text" on page 431

## 2.4.2 PaymentInformation <PmtInf>

*Presence:* [1..*]

*Definition:* Set of characteristics that applies to the debit side of the payment transactions included in the credit transfer initiation.

*Impacted by:* C4 "ChargeBearerRule", C5 "ChargesAccountAgentRule", C6 "ChargesAccountRule", C7 "ChequeAndCreditorAccountRule", C8 "ChequeDeliveryAndCreditorAgentRule", C9 "ChequeDeliveryAndNoCreditorAgentRule", C14 "ChequeInstructionRule", C16 "ChequeNoDeliveryAndNoCreditorAgentRule", C23 "InstructionForDebtorAgentRule", C29 "NonChequePaymentMethodRule", C30 "PaymentTypeInformationRule", C37 "UltimateDebtorRule", C10 "ChequeFromGuideline", C11 "ChequeInstructionDeliverToCreditorAgentGuideline", C12 "ChequeInstructionDeliverToCreditorGuideline", C13 "ChequeInstructionDeliverToDebtorGuideline", C35 "UltimateDebtorGuideline"

---

<!-- Page 19 -->

PaymentInformation <PmtInf> contains the following PaymentInstruction44 elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **PaymentInformationIdentification** <PmtId> | [1..1] | Text | | 25 |
| | **PaymentMethod** <PmtMtd> | [1..1] | CodeSet | | 25 |
| | **RequestedAdviceType** <ReqdAdvcTp> | [0..1] | | | 26 |
| | **CreditAdvice** <CdtAdvc> | [0..1] | | | 26 |
| Or | **Code** <Cd> | [1..1] | CodeSet | | 26 |
| Or | **Proprietary** <Ptry> | [1..1] | Text | | 27 |
| | **DebitAdvice** <DbtAdvc> | [0..1] | | | 27 |
| Or | **Code** <Cd> | [1..1] | CodeSet | | 27 |
| Or | **Proprietary** <Ptry> | [1..1] | Text | | 27 |
| | **BatchBooking** <BtchBkng> | [0..1] | Indicator | | 27 |
| | **NumberOfTransactions** <NbOfTxs> | [0..1] | Text | | 28 |
| | **ControlSum** <CtrlSum> | [0..1] | Quantity | | 28 |
| | **PaymentTypeInformation** <PmtTpInf> | [0..1] | ± | | 28 |
| | **RequestedExecutionDate** <ReqdExctnDt> | [1..1] | ± | | 28 |
| | **PoolingAdjustmentDate** <PoolgAdjstmtDt> | [0..1] | Date | | 29 |
| | **Debtor** <Dbtr> | [1..1] | ± | | 29 |
| | **DebtorAccount** <DbtrAcct> | [1..1] | ± | C21, C20 | 30 |
| | **DebtorAgent** <DbtrAgnt> | [1..1] | ± | | 31 |
| | **DebtorAgentAccount** <DbtrAgntAcct> | [0..1] | ± | C21, C20 | 32 |
| | **InstructionForDebtorAgent** <InstrForDbtrAgnt> | [0..1] | Text | | 33 |
| | **UltimateDebtor** <UltmtDbtr> | [0..1] | ± | | 33 |
| | **ChargeBearer** <ChrgBr> | [0..1] | CodeSet | | 34 |
| | **ChargesAccount** <ChrgsAcct> | [0..1] | ± | C21, C20 | 35 |
| | **ChargesAccountAgent** <ChrgsAcctAgnt> | [0..1] | ± | | 36 |
| | **CreditTransferTransactionInformation** <CdtTrfTxInf> | [1..*] | | C22, C24, C25, C26, C27, C28, C34, C36 | 36 |
| | **PaymentIdentification** <PmtId> | [1..1] | ± | | 40 |

---

<!-- Page 20 -->

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **PaymentTypeInformation** *<PmtTpInf>* | [0..1] | ± | | 41 |
| | **Amount** *<Amt>* | [1..1] | ± | | 41 |
| | **ExchangeRateInformation** *<XchgRateInf>* | [0..1] | | | 42 |
| | **UnitCurrency** *<UnitCcy>* | [0..1] | CodeSet | C1 | 42 |
| | **ExchangeRate** *<XchgRate>* | [0..1] | Rate | | 42 |
| | **RateType** *<RateTp>* | [0..1] | CodeSet | | 42 |
| | **ContractIdentification** *<CtrctId>* | [0..1] | Text | | 43 |
| | **ChargeBearer** *<ChrgBr>* | [0..1] | CodeSet | | 43 |
| | **MandateRelatedInformation** *<MndtReltdInf>* | [0..1] | ± | | 43 |
| | **ChequeInstruction** *<ChqInstr>* | [0..1] | | C15 | 44 |
| | **ChequeType** *<ChqTp>* | [0..1] | CodeSet | | 45 |
| | **ChequeNumber** *<ChqNb>* | [0..1] | Text | | 46 |
| | **ChequeFrom** *<ChqFr>* | [0..1] | | | 46 |
| | **Name** *<Nm>* | [1..1] | Text | | 46 |
| | **Address** *<Adr>* | [1..1] | ± | | 47 |
| | **DeliveryMethod** *<DlvyMtd>* | [0..1] | | | 47 |
| Or | **Code** *<Cd>* | [1..1] | CodeSet | | 48 |
| Or | **Proprietary** *<Prt>* | [1..1] | Text | | 48 |
| | **DeliverTo** *<DlvrTo>* | [0..1] | | | 48 |
| | **Name** *<Nm>* | [1..1] | Text | | 49 |
| | **Address** *<Adr>* | [1..1] | ± | | 49 |
| | **InstructionPriority** *<InstrPrty>* | [0..1] | CodeSet | | 49 |
| | **ChequeMaturityDate** *<ChqMtrtyDt>* | [0..1] | Date | | 50 |
| | **FormsCode** *<FrmsCd>* | [0..1] | Text | | 50 |
| | **MemoField** *<MemoFld>* | [0..2] | Text | | 50 |
| | **RegionalClearingZone** *<RgnlClrZone>* | [0..1] | Text | | 50 |
| | **PrintLocation** *<PrtLctn>* | [0..1] | Text | | 50 |
| | **Signature** *<Sgntr>* | [0..5] | Text | | 50 |
| | **UltimateDebtor** *<UltmtDbtr>* | [0..1] | ± | | 50 |
| | **IntermediateAgent1** *<IntmyAg1>* | [0..1] | ± | | 51 |
| | **IntermediateAgent1Account** *<IntmyAg1Acct>* | [0..1] | ± | C21, C20 | 52 |

---

<!-- Page 21 -->

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **IntermediateAgent2** *<IntrmyAgt2>* | [0..1] | ± | | 53 |
| | **IntermediateAgent2Account** *<IntrmyAgt2Acct>* | [0..1] | ± | C21, C20 | 53 |
| | **IntermediateAgent3** *<IntrmyAgt3>* | [0..1] | ± | | 54 |
| | **IntermediateAgent3Account** *<IntrmyAgt3Acct>* | [0..1] | ± | C21, C20 | 55 |
| | **CreditorAgent** *<CdtrAgt>* | [0..1] | ± | | 56 |
| | **CreditorAgentAccount** *<CdtrAgtAcct>* | [0..1] | ± | C21, C20 | 56 |
| | **Creditor** *<Cdtr>* | [0..1] | ± | | 57 |
| | **CreditorAccount** *<CdtrAcct>* | [0..1] | ± | C21, C20 | 58 |
| | **UltimateCreditor** *<UltmtCdtr>* | [0..1] | ± | | 59 |
| | **InstructionForCreditorAgent** *<InstrForCdtrAgt>* | [0..*] | ± | | 60 |
| | **InstructionForDebtorAgent** *<InstrForDbtrAgt>* | [0..1] | | | 61 |
| | **Code** *<Cd>* | [0..1] | CodeSet | | 61 |
| | **InstructionInformation** *<InstrInf>* | [0..1] | Text | | 61 |
| | **Purpose** *<Purp>* | [0..1] | ± | | 61 |
| | **RegulatoryReporting** *<RgltryRptg>* | [0..10] | ± | | 62 |
| | **Tax** *<Tax>* | [0..1] | | | 62 |
| | **Creditor** *<Cdtr>* | [0..1] | ± | | 64 |
| | **Debtor** *<Dbtr>* | [0..1] | ± | | 64 |
| | **UltimateDebtor** *<UltmtDbtr>* | [0..1] | ± | | 64 |
| | **AdministrationZone** *<AdminZone>* | [0..1] | Text | | 65 |
| | **ReferenceNumber** *<RefNb>* | [0..1] | Text | | 65 |
| | **Method** *<Mtd>* | [0..1] | Text | | 65 |
| | **TotalTaxableBaseAmount** *<TtlTaxblBaseAmt>* | [0..1] | Amount | C1, C18 | 65 |
| | **TotalTaxAmount** *<TtlTaxAmt>* | [0..1] | Amount | C1, C18 | 66 |
| | **Date** *<Dt>* | [0..1] | Date | | 66 |
| | **SequenceNumber** *<SeqNb>* | [0..1] | Quantity | | 66 |
| | **Record** *<Rcd>* | [0..*] | | | 66 |
| | **Type** *<Tp>* | [0..1] | Text | | 67 |
| | **Category** *<Ctgy>* | [0..1] | Text | | 67 |
| | **CategoryDetails** *<CtgyDtls>* | [0..1] | Text | | 67 |

---

<!-- Page 22 -->

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **DebtorStatus** <DbtrSts> | [0..1] | Text |  | 68 |
| | **CertificateIdentification** <Certs> | [0..1] | Text |  | 68 |
| | **FormsCode** <FrmsCd> | [0..1] | Text |  | 68 |
| | **Period** <Prd> | [0..1] |  |  | 68 |
| | **Year** <Yr> | [0..1] | Year |  | 68 |
| | **Type** <Tp> | [0..1] | CodeSet |  | 68 |
| | **FromToDate** <FrToDt> | [0..1] | ± |  | 69 |
| | **TaxAmount** <TaxAmt> | [0..1] |  |  | 70 |
| | **Rate** <Rate> | [0..1] | Rate |  | 70 |
| | **TaxableBaseAmount** <TaxblBaseAmt> | [0..1] | Amount | C1, C18 | 70 |
| | **TotalAmount** <TtlAmt> | [0..1] | Amount | C1, C18 | 70 |
| | **Details** <Dtls> | [0..*] |  |  | 71 |
| | **Period** <Prd> | [0..1] |  |  | 71 |
| | **Year** <Yr> | [0..1] | Year |  | 71 |
| | **Type** <Tp> | [0..1] | CodeSet |  | 72 |
| | **FromToDate** <FrToDt> | [0..1] | ± |  | 72 |
| | **Amount** <Amt> | [1..1] | Amount | C1, C18 | 73 |
| | **AdditionalInformation** <AddtlInf> | [0..1] | Text |  | 73 |
| | **RelatedRemittanceInformation** <RltdRmInf> | [0..10] |  |  | 73 |
| | **RemittanceIdentification** <RmId> | [0..1] | Text |  | 74 |
| | **RemittanceLocationDetails** <RmtLclnDtls> | [0..*] |  |  | 74 |
| | **Method** <Mtd> | [1..1] | CodeSet |  | 74 |
| | **ElectronicAddress** <ElctrncAdr> | [0..1] | Text |  | 75 |
| | **PostalAddress** <PstlAdr> | [0..1] |  |  | 75 |
| | **Name** <Nm> | [1..1] | Text |  | 75 |
| | **Address** <Adr> | [1..1] | ± |  | 75 |
| | **RemittanceInformation** <RmInf> | [0..1] | ± |  | 76 |
| | **SupplementaryData** <SplmtryData> | [0..*] | ± | C33 | 77 |

## Constraints

- **ChargeBearerRule**

  If ChargeBearer is present, then CreditTransferTransactionInformation/ChargeBearer is not allowed.

---

<!-- Page 23 -->

If CreditTransferTransactionInformation/ChargeBearer is present, then ChargeBearer is not allowed.

CreditTransferTransactionInformation/ChargeBearer and ChargeBearer may both be absent.
    Following Must be True
    /ChargeBearer Must be absent
    Or
    /CreditTransferTransactionInformation[*]/ChargeBearer Must be absent

* **ChargesAccountAgentRule**
If ChargesAccountAgent is present, then it must contain a branch of the DebtorAgent. It must not contain a completely different agent.
    On Condition
    /ChargesAccountAgent is present
    Following Must be True
    /ChargesAccountAgent/FinancialInstitutionIdentification/Name Must be equal to value 'Branch of DebtorAgent.'

* **ChargesAccountRule**
If ChargesAccountAgent is present, then ChargesAccount must be present.
    On Condition
    /ChargesAccountAgent is present
    Following Must be True
    /ChargesAccount Must be present

* **ChequeAndCreditorAccountRule**
If PaymentMethod is CHK (Cheque), then CreditTransferTransactionInformation/CreditorAccount is not allowed.
    On Condition
    /PaymentMethod is equal to value 'Cheque'
    Following Must be True
    /CreditTransferTransactionInformation[*]/CreditorAccount Must be absent

* **ChequeDeliveryAndCreditorAgentRule**
If PaymentMethod is CHK (Cheque) and CreditTransferTransactionInformation/ChequeInstruction/DeliveryMethod/Code is present and is equal to MLFA (MailToFinalAgent), CRFA (CourierToFinalAgent), RGFA (RegisteredMailToFinalAgent) or PUFA (PickUpByFinalAgent), then CreditTransferTransactionInformation/CreditorAgent must be present.
    On Condition
    /PaymentMethod is equal to value 'Cheque'
    And    /CreditTransferTransactionInformation[*]/ChequeInstruction is present
    And    /CreditTransferTransactionInformation[*]/ChequeInstruction/DeliveryMethod is present
    And    /CreditTransferTransactionInformation[*]/ChequeInstruction/DeliveryMethod/Code is present
    And    /CreditTransferTransactionInformation[*]/ChequeInstruction/DeliveryMethod/Code is within DataCode <Code> ChequeDeliveryCode
    Following Must be True
    /CreditTransferTransactionInformation[*]/CreditorAgent Must be present

* **ChequeDeliveryAndNoCreditorAgentRule**
If PaymentMethod is CHK (Cheque) and CreditTransferTransactionInformation/ChequeInstruction/DeliveryMethod/Code is present and different from MLFA (MailToFinalAgent), CRFA (CourierToFinalAgent), RGFA (RegisteredMailToFinalAgent) or PUFA (PickUpByFinalAgent), then CreditTransferTransactionInformation/CreditorAgent is not allowed.
    On Condition
    /PaymentMethod is equal to value 'Cheque'
    And    /CreditTransferTransactionInformation[*]/ChequeInstruction is present
    And    /CreditTransferTransactionInformation[*]/ChequeInstruction/DeliveryMethod

---

<!-- Page 24 -->

is present
    And    /CreditTransferTransactionInformation[*]/ChequeInstruction/DeliveryMethod/
    Code is present
    And    /CreditTransferTransactionInformation[*]/ChequeInstruction/DeliveryMethod/
    Code is not within DataType <Code> ChequeDelivery2Code
    Following Must be True
    /CreditTransferTransactionInformation[*]/CreditorAgent Must be absent

* **ChequeFromGuideline**

  CreditTransferTransactionInformation/ChequeInstruction/ChequeFrom may only be present if
  different from CreditTransferTransactionInformation/UltimateDebtor or Debtor.

* **ChequeInstructionDeliverToCreditorAgentGuideline**

  If CreditTransferTransactionInformation/ChequeInstruction/DeliveryMethod is present and is CRFA
  (CourierToFinalAgent), MLFA (MailToFinalAgent), PUFA (PickUpByFinalAgent) or RGFA
  (RegisteredMailToFinalAgent), then CreditTransferTransactionInformation/ChequeInstruction/
  DeliverTo may only be present if different from CreditTransferTransactionInformation/Creditor.

* **ChequeInstructionDeliverToCreditorGuideline**

  If PaymentInformation/CreditTransferTransactionInformation/ChequeInstruction/DeliveryMethod is
  present and is CRCD (CourierToCreditor), MLCD (MailToCreditor), PUCD (PickUpByCreditor) or
  RGCD (RegisteredMailToCreditor), then CreditTransferTransactionInformation/ChequeInstruction/
  DeliverTo may only be present if different from CreditTransferTransactionInformation/Creditor.

* **ChequeInstructionDeliverToDebtorGuideline**

  If CreditTransferTransactionInformation/ChequeInstruction/DeliveryMethod is present and if
  CreditTransferTransactionInformation/ChequeInstruction/DeliveryMethod/Code is CRDB
  (CourierToDebtor), MLDB (MailToDebtor), PUDB (PickUpByDebtor) or RGDB
  (RegisteredMailToDebtor), then CreditTransferTransactionInformation/ChequeInstruction/DeliverTo
  may only be present if different from Debtor.

* **ChequeInstructionRule**

  If PaymentMethod is different from CHK (Cheque), then CreditTransferTransactionInformation/
  ChequeInstruction is not allowed.

  On Condition
  /PaymentMethod is present
  And    /PaymentMethod is different from value 'Cheque'
  Following Must be True
  /CreditTransferTransactionInformation[*]/ChequeInstruction Must be absent

* **ChequeNoDeliveryAndNoCreditorAgentRule**

  If PaymentMethod is CHK (Cheque) and CreditTransferTransactionInformation/ChequeInstruction/
  DeliveryMethod is not present, then CreditTransferTransactionInformation/CreditorAgent is not
  allowed.

  On Condition
  /PaymentMethod is equal to value 'Cheque'
  And    /CreditTransferTransactionInformation[*]/ChequeInstruction is present
  And    /CreditTransferTransactionInformation[*]/ChequeInstruction/DeliveryMethod
  is absent
  Following Must be True
  /CreditTransferTransactionInformation[*]/CreditorAgent Must be absent

* **InstructionForDebtorAgentRule**

  If InstructionForDebtorAgent is present, then CreditTransferTransactionInformation/
  InstructionForDebtorAgent is not allowed.

---

<!-- Page 25 -->

If CreditTransferTransactionInformation/InstructionForDebtorAgent is present, then
InstructionForDebtorAgent is not allowed.

CreditTransferTransactionInformation/InstructionForDebtorAgent and InstructionForDebtorAgent
may both be absent.
    Following Must be True
    /InstructionForDebtorAgent Must be absent
    Or  /CreditTransferTransactionInformation[*]/InstructionForDebtorAgent Must be
    absent

* **NonChequePaymentMethodRule**

If PaymentMethod is different from CHK (Cheque) and CreditTransferTransactionInformation/
Creditor is not present, then CreditTransferTransactionInformation/CreditorAccount must be present.
    On Condition
    /PaymentMethod is different from value 'Cheque'
    And  /CreditTransferTransactionInformation[*]/Creditor is absent
    Following Must be True
    /CreditTransferTransactionInformation[*]/CreditorAccount Must be present

* **PaymentTypeInformationRule**

If PaymentTypeInformation is present, then CreditTransferTransactionInformation/
PaymentTypeInformation is not allowed.
    On Condition
    /PaymentTypeInformation is present
    Following Must be True
    /CreditTransferTransactionInformation[*]/PaymentTypeInformation Must be absent

* **UltimateDebtorGuideline**

UltimateDebtor may only be present if different from Debtor.

* **UltimateDebtorRule**

If UltimateDebtor is present, then CreditTransferTransactionInformation/UltimateDebtor is not
allowed.

If CreditTransferTransactionInformation/UltimateDebtor is present, then UltimateDebtor is not
allowed.

CreditTransferTransactionInformation/UltimateDebtor and UltimateDebtor may both be absent.
    Following Must be True
    /UltimateDebtor Must be absent
    Or  /CreditTransferTransactionInformation[*]/UltimateDebtor Must be absent

## 2.4.2.1 PaymentInformationIdentification <PmtInfId>

*Presence:* [1..1]

*Definition:* Unique identification, as assigned by a sending party, to unambiguously identify the payment
information group within the message.

*Datatype:* "Max35Text" on page 431

## 2.4.2.2 PaymentMethod <PmtMtd>

*Presence:* [1..1]

*Definition:* Specifies the means of payment that will be used to move the amount of money.

*Datatype:* "PaymentMethod3Code" on page 421

---

<!-- Page 26 -->

| CodeName | Name | Definition |
|---|---|---|
| CHK | Cheque | Written order to a bank to pay a certain amount of money from one person to another person. |
| TRF | CreditTransfer | Transfer of an amount of money in the books of the account service. |
| TRA | TransferAdvice | Transfer of an amount of money in the books of the account service. An advice should be sent back to the account owner. |

### 2.4.2.3 RequestedAdviceType <ReqdAdvcTp>

*Presence:* [0..1]

*Definition:* Type of advice details requested.

**RequestedAdviceType <ReqdAdvcTp>** contains the following **AdviceType1** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **CreditAdvice** <CdtAdvc> | [0..1] |  |  | 26 |
| {Or | **Code** <Cd> | [1..1] | CodeSet |  | 26 |
| Or} | **Proprietary** <Ptry> | [1..1] | Text |  | 27 |
| | **DebitAdvice** <DbtAdvc> | [0..1] |  |  | 27 |
| {Or | **Code** <Cd> | [1..1] | CodeSet |  | 27 |
| Or} | **Proprietary** <Ptry> | [1..1] | Text |  | 27 |

#### 2.4.2.3.1 CreditAdvice <CdtAdvc>

*Presence:* [0..1]

*Definition:* Type of credit advice requested.

**CreditAdvice <CdtAdvc>** contains one of the following **AdviceType1Choice** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| {Or | **Code** <Cd> | [1..1] | CodeSet |  | 26 |
| Or} | **Proprietary** <Ptry> | [1..1] | Text |  | 27 |

##### 2.4.2.3.1.1 Code <Cd>

*Presence:* [1..1]

*Definition:* Advice type, in a coded form.

*Datatype:* "AdviceType1Code" on page 409

| CodeName | Name | Definition |
|---|---|---|
| ADWD | AdviceWithDetails | Advice with transaction details is requested. |

---

<!-- Page 27 -->

| CodeName | Name | Definition |
|---|---|---|
| ADND | AdviceWithoutDetails | Advice without transaction details is requested. |

## 2.4.2.3.1.2 Proprietary <Ptry>

*Presence:* [1..1]

*Definition:* Advice type, in a proprietary form.

*Datatype:* "Max35Text" on page 431

## 2.4.2.3.2 DebitAdvice <DbtAdvc>

*Presence:* [0..1]

*Definition:* Type de debit advice requested.

DebitAdvice <DbtAdvc> contains one of the following AdviceType1Choice elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| (Or | Code <Cd> | [1..1] | CodeSet | | 27 |
| (Or) | Proprietary <Ptry> | [1..1] | Text | | 27 |

### 2.4.2.3.2.1 Code <Cd>

*Presence:* [1..1]

*Definition:* Advice type, in a coded form.

*Datatype:* "AdviceType1Code" on page 409

| CodeName | Name | Definition |
|---|---|---|
| ADWD | AdviceWithDetails | Advice with transaction details is requested. |
| ADND | AdviceWithoutDetails | Advice without transaction details is requested. |

### 2.4.2.3.2.2 Proprietary <Ptry>

*Presence:* [1..1]

*Definition:* Advice type, in a proprietary form.

*Datatype:* "Max35Text" on page 431

## 2.4.2.4 BatchBooking <BtchBook>

*Presence:* [0..1]

*Definition:* Identifies whether a single entry per individual transaction or a batch entry for the sum of the amounts of all transactions within the group of a message is requested.

Usage: Batch booking is used to request and not order a possible batch booking.

*Datatype:* One of the following values must be used (see "BatchBookingIndicator" on page 427):

---

<!-- Page 28 -->

• *Meaning When True:* Identifies that a batch entry for the sum of the amounts of all transactions in the batch or message is requested.

• *Meaning When False:* Identifies that a single entry for each of the transactions in the batch or message is requested.

## 2.4.2.5 NumberOfTransactions <NbOfTxs>

*Presence:* [0..1]

*Definition:* Number of individual transactions contained in the payment information group.

*Datatype:* "Max15NumericText" on page 430

## 2.4.2.6 ControlSum <CtrlSum>

*Presence:* [0..1]

*Definition:* Total of all individual amounts included in the group, irrespective of currencies.

*Datatype:* "DecimalNumber" on page 427

## 2.4.2.7 PaymentTypeInformation <PmtTpInf>

*Presence:* [0..1]

*Definition:* Set of elements used to further specify the type of transaction.

**PaymentTypeInformation <PmtTpInf>** contains the following elements (see "PaymentTypeInformation26" on page 346 for details)

| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | InstructionPriority <InstrPrty> | [0..1] | CodeSet | | 346 |
| | ServiceLevel <SvcLvl> | [0..*] | | | 346 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 347 |
| Or) | Proprietary <Prtry> | [1..1] | Text | | 347 |
| | LocalInstrument <LocInstrm> | [0..1] | | | 347 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 347 |
| Or) | Proprietary <Prtry> | [1..1] | Text | | 347 |
| | CategoryPurpose <CatgPurp> | [0..1] | | | 347 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 348 |
| Or) | Proprietary <Prtry> | [1..1] | Text | | 348 |

## 2.4.2.8 RequestedExecutionDate <ReqdExctnDt>

*Presence:* [1..1]

*Definition:* Date at which the initiating party requests the clearing agent to process the payment.

Usage: This is the date on which the debtor's account is to be debited. If payment by cheque, the date when the cheque must be generated by the bank.

---

<!-- Page 29 -->

RequestedExecutionDate <ReqdExctnDt> contains one of the following elements (see "DateAndDateTimeChoice" on page 316 for details)



| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| (Or | Date <Dt> | [1..1] | Date | | 317 |
| Or) | DateTime <DtTm> | [1..1] | DateTime | | 317 |

### 2.4.2.9 PoolingAdjustmentDate <PoolgAdjstmntDt>

*Presence:* [0..1]

*Definition:* Date used for the correction of the value date of a cash pool movement that has been posted with a different value date.

*Datatype:* "ISODate" on page 425

### 2.4.2.10 Debtor <Dbtr>

*Presence:* [1..1]

*Definition:* Party that owes an amount of money to the (ultimate) creditor.

---

<!-- Page 30 -->

Debtor <Dbtr> contains the following elements (see "PartyIdentification272" on page 336 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Const. No. | Page |
|---|---|---|---|---|---|
| | Name *<Nm>* | [0..1] | Text | | 337 |
| | PostalAddress *<PstlAdr>* | [0..1] | ± | | 338 |
| | Identification *<Id>* | [0..1] | | | 338 |
| (Or | OrganisationIdentification *<OrgId>* | [1..1] | | | 339 |
| | AnyBIC *<AnyBIC>* | [0..1] | IdentifierSet | C5 | 340 |
| | LEI *<LEI>* | [0..1] | IdentifierSet | | 340 |
| | Other *<Othr>* | [0.*] | | | 340 |
| | Identification *<Id>* | [1..1] | Text | | 341 |
| | SchemeName *<SchmeNm>* | [0..1] | | | 341 |
| (Or | Code *<Cd>* | [1..1] | CodeSet | | 341 |
| (Or) | Proprietary *<Prtry>* | [1..1] | Text | | 341 |
| | Issuer *<Issr>* | [0..1] | Text | | 341 |
| (Or) | PrivateIdentification *<PrvtId>* | [1..1] | | | 341 |
| | DateAndPlaceOfBirth *<DtAndPlcOfBirth>* | [0..1] | | | 342 |
| | BirthDate *<BirthDt>* | [1..1] | Date | | 342 |
| | ProvinceOfBirth *<PrvcOfBirth>* | [0..1] | Text | | 342 |
| | CityOfBirth *<CityOfBirth>* | [1..1] | Text | | 343 |
| | CountryOfBirth *<CtryOfBirth>* | [1..1] | CodeSet | C7 | 343 |
| | Other *<Othr>* | [0.*] | | | 343 |
| | Identification *<Id>* | [1..1] | Text | | 343 |
| | SchemeName *<SchmeNm>* | [0..1] | | | 343 |
| (Or) | Code *<Cd>* | [1..1] | CodeSet | | 344 |
| (Or) | Proprietary *<Prtry>* | [1..1] | Text | | 344 |
| | Issuer *<Issr>* | [0..1] | Text | | 344 |
| | CountryOfResidence *<CtryOfRes>* | [0..1] | CodeSet | C7 | 344 |
| | ContactDetails *<CtctDtls>* | [0..1] | ± | | 344 |

## 2.4.2.11 DebtorAccount <DbtrAcct>

Presence: [1..1]

Definition: Unambiguous identification of the account of the debtor to which a debit entry will be made as a result of the transaction.

Impacted by: C21 "IdentificationOrProxyPresenceRule", C20 "IdentificationAndProxyGuideline"

---

<!-- Page 31 -->

DebtorAccount <DbtrAcct> contains the following elements (see "CashAccount40" on page 309 for details)



<table><tr><td>Or</td><td>MessageElement&lt;XML Tag&gt;</td><td>Mult.</td><td>Type</td><td>Constr. No.</td><td>Page</td></tr><tr><td></td><td>Identification &lt;Ids&gt;</td><td>[0..1]</td><td>±</td><td></td><td>310</td></tr><tr><td></td><td>Type &lt;Tp&gt;</td><td>[0..1]</td><td>±</td><td></td><td>310</td></tr><tr><td></td><td>Currency &lt;Ccy&gt;</td><td>[0..1]</td><td>CodeSet</td><td>C2</td><td>310</td></tr><tr><td></td><td>Name &lt;Nm&gt;</td><td>[0..1]</td><td>Text</td><td></td><td>311</td></tr><tr><td></td><td>Proxy &lt;Prxy&gt;</td><td>[0..1]</td><td>±</td><td></td><td>311</td></tr></table>

## Constraints

- **IdentificationAndProxyGuideline**

If the account identification is not defined through a conventional identification such as an email address or a mobile number, then the proxy element should be used for the identification of the account.

- **IdentificationOrProxyPresenceRule**

Identification must be present or Proxy must be present. Both may be present.

```
Following Must be True
/Identification Must be present
Or
/Proxy Must be present
```

### 2.4.2.12 DebtorAgent <DbtrAgnt>

*Presence:* [1..1]

*Definition:* Financial institution servicing an account for the debtor.

---

<!-- Page 32 -->

DebtorAgent <DbtrAggt> contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on page 320 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | FinancialInstitutionIdentification <FinInstlId> | [1..1] | | | 321 |
| | BICFI <BICFI> | [0..1] | IdentifierSet | C6 | 321 |
| | ClearingSystemMemberIdentification <ClrSysMmbId> | [0..1] | ± | | 322 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 322 |
| | Name <Nm> | [0..1] | Text | | 322 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 322 |
| | Other <Othr> | [0..1] | ± | | 323 |
| | BranchIdentification <BrnchId> | [0..1] | | | 324 |
| | Identification <Id> | [0..1] | Text | | 324 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 324 |
| | Name <Nm> | [0..1] | Text | | 324 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 324 |

### 2.4.2.13 DebtorAgentAccount <DbtrAggtAcct>

Presence: [0..1]

Definition: Unambiguous identification of the account of the debtor agent at its servicing agent in the payment chain.

Impacted by: C21 "IdentificationOrProxyPresenceRule", C20 "IdentificationAndProxyGuideline"

DebtorAgentAccount <DbtrAggtAcct> contains the following elements (see "CashAccount40" on page 309 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Identification <Id> | [0..1] | ± | | 310 |
| | Type <Tp> | [0..1] | ± | | 310 |
| | Currency <Ccy> | [0..1] | CodeSet | C2 | 310 |
| | Name <Nm> | [0..1] | Text | | 311 |
| | Proxy <Prxy> | [0..1] | ± | | 311 |

---

<!-- Page 33 -->

Constraints

* **IdentificationAndProxyGuideline**

  If the account identification is not defined through a conventional identification such as an email address or a mobile number, then the proxy element should be used for the identification of the account.

* **IdentificationOrProxyPresenceRule**

  Identification must be present or Proxy must be present. Both may be present.

  ```
  Following Must be True
  /Identification Must be present
  Or    /Proxy Must be present
  ```

## 2.4.2.14 InstructionForDebtorAgent <InstrForDbtrAgt>

*Presence:* [0..1]

*Definition:* Further information related to the processing of the payment instruction, that may need to be acted upon by the debtor agent, depending on agreement between debtor and the debtor agent.

Usage: when present, then the instructions for the debtor agent apply for all credit transfer transaction information occurrences, present in the payment information.

*Datatype:* "Max140Text" on page 429

## 2.4.2.15 UltimateDebtor <UltmtDbtr>

*Presence:* [0..1]

*Definition:* Ultimate party that owes an amount of money to the (ultimate) creditor.

---

<!-- Page 34 -->

UltimateDebtor <UltmDbtr> contains the following elements (see *PartyIdentification272* on page 336 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Name <Nm> | [0..1] | Text | | 337 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 338 |
| | Identification <Id> | [0..1] | | | 338 |
| (Or | OrganisationIdentification <OrgId> | [1..1] | | | 339 |
| | AnyBIC <AnyBIC> | [0..1] | IdentifierSet | C5 | 340 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 340 |
| | Other <Othr> | [0..*] | | | 340 |
| | Identification <Id> | [1..1] | Text | | 341 |
| | SchemeName <SchmeNm> | [0..1] | | | 341 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 341 |
| Or) | Proprietary <Prtry> | [1..1] | Text | | 341 |
| | Issuer <Issr> | [0..1] | Text | | 341 |
| (Or) | PrivateIdentification <PrvtId> | [1..1] | | | 341 |
| | DateAndPlaceOfBirth <DtAndPlcOfBirth> | [0..1] | | | 342 |
| | BirthDate <BirthDt> | [1..1] | Date | | 342 |
| | ProvinceOfBirth <PrvcOfBirth> | [0..1] | Text | | 342 |
| | CityOfBirth <CityOfBirth> | [1..1] | Text | | 343 |
| | CountryOfBirth <CtryOfBirth> | [1..1] | CodeSet | C7 | 343 |
| | Other <Othr> | [0..*] | | | 343 |
| | Identification <Id> | [1..1] | Text | | 343 |
| | SchemeName <SchmeNm> | [0..1] | | | 343 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 344 |
| Or) | Proprietary <Prtry> | [1..1] | Text | | 344 |
| | Issuer <Issr> | [0..1] | Text | | 344 |
| | CountryOfResidence <CtryOfRes> | [0..1] | CodeSet | C7 | 344 |
| | ContactDetails <CtctDtls> | [0..1] | ± | | 344 |

## 2.4.2.16 ChargeBearer <ChrgBr>

*Presence:* [0..1]

*Definition:* Specifies which party/parties will bear the charges associated with the processing of the payment transaction.

---

<!-- Page 35 -->

Datatype: "ChargeBearerType1Code" on page 410



| CodeName | Name | Definition |
|---|---|---|
| DEBT | BorneByDebtor | All transaction charges are to be borne by the debtor. |
| CRED | BorneByCreditor | All transaction charges are to be borne by the creditor. |
| SHAR | Shared | In a credit transfer context, means that transaction charges on the sender side are to be borne by the debtor, transaction charges on the receiver side are to be borne by the creditor. In a direct debit context, means that transaction charges on the sender side are to be borne by the creditor, transaction charges on the receiver side are to be borne by the debtor. |
| SLEV | FollowingServiceLevel | Charges are to be applied following the rules agreed in the service level and/or scheme. |

## 2.4.2.17 ChargesAccount <ChrgsAcct>

*Presence:* [0..1]

*Definition:* Account used to process charges associated with a transaction.

Usage: Charges account should be used when charges have to be booked to an account different from the account identified in debtor's account.

*Impacted by:* C21 "IdentificationOrProxyPresenceRule", C20 "IdentificationAndProxyGuideline"

**ChargesAccount <ChrgsAcct>** contains the following elements (see "CashAccount40" on page 309 for details)



| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Identification <Id> | [0..1] | ± | | 310 |
| | Type <Tp> | [0..1] | ± | | 310 |
| | Currency <Ccy> | [0..1] | CodeSet | C2 | 310 |
| | Name <Nm> | [0..1] | Text | | 311 |
| | Proxy <Prxy> | [0..1] | ± | | 311 |

### Constraints

- **IdentificationAndProxyGuideline**

If the account identification is not defined through a conventional identification such as an email address or a mobile number, then the proxy element should be used for the identification of the account.

- **IdentificationOrProxyPresenceRule**

Identification must be present or Proxy must be present. Both may be present.

---

<!-- Page 36 -->

Following Must be True
/Identification Must be present
Or /Proxy Must be present

## 2.4.2.18 ChargesAccountAgent <ChrgsAcctAgtr>

Presence: [0..1]

Definition: Agent that services a charges account.

Usage: Charges account agent should only be used when the charges account agent is different from the debtor agent.

**ChargesAccountAgent <ChrgsAcctAgtr>** contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on page 320 for details)



| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | FinancialInstitutionIdentification <FinInstlId> | [1..1] |  |  | 321 |
| | BICFI <BICFI> | [0..1] | IdentifierSet | C6 |  |
| | ClearingSystemMemberIdentification <ClrSysMmbId> | [0..1] | ± |  | 322 |
| | LEI <LEI> | [0..1] | IdentifierSet |  | 322 |
| | Name <Nm> | [0..1] | Text |  | 322 |
| | PostalAddress <PstlAdr> | [0..1] | ± |  | 322 |
| | Other <Othr> | [0..1] | ± |  | 323 |
| | BranchIdentification <BrnchId> | [0..1] |  |  | 324 |
| | Identification <Id> | [0..1] | Text |  | 324 |
| | LEI <LEI> | [0..1] | IdentifierSet |  | 324 |
| | Name <Nm> | [0..1] | Text |  | 324 |
| | PostalAddress <PstlAdr> | [0..1] | ± |  | 324 |

## 2.4.2.19 CreditTransferTransactionInformation <CdtTrfTxInf>

Presence: [1..*]

Definition: Provides information on the individual transaction(s) included in the message.

Impacted by: C22 "InstructionForCreditorAgentRule", C24 "IntermediaryAgent1AccountRule", C25 "IntermediaryAgent2AccountRule", C26 "IntermediaryAgent2Rule", C27 "IntermediaryAgent3AccountRule", C28 "IntermediaryAgent3Rule", C34 "UltimateCreditorGuideline", C36 "UltimateDebtorGuideline"

---

<!-- Page 37 -->

CreditTransferTransactionInformation <CdTrfTxInf> contains the following CreditTransferTransaction61 elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **PaymentIdentification** <PmtId> | [1..1] | ± | | 40 |
| | **PaymentTypeInformation** <PmtTpInf> | [0..1] | ± | | 41 |
| | **Amount** <Amt> | [1..1] | ± | | 41 |
| | **ExchangeRateInformation** <XchgRateInf> | [0..1] | | | 42 |
| | **UnitCurrency** <UnitCcy> | [0..1] | CodeSet | C1 | 42 |
| | **ExchangeRate** <XchgRate> | [0..1] | Rate | | 42 |
| | **RateType** <RateTp> | [0..1] | CodeSet | | 42 |
| | **ContractIdentification** <CtrctId> | [0..1] | Text | | 43 |
| | **ChargeBearer** <ChgBr> | [0..1] | CodeSet | | 43 |
| | **MandateRelatedInformation** <MndtRltdInf> | [0..1] | ± | | 43 |
| | **ChequeInstruction** <ChqInstr> | [0..1] | | C15 | 44 |
| | **ChequeType** <ChqTp> | [0..1] | CodeSet | | 45 |
| | **ChequeNumber** <ChqNb> | [0..1] | Text | | 46 |
| | **ChequeFrom** <ChqFr> | [0..1] | | | 46 |
| | **Name** <Nm> | [1..1] | Text | | 46 |
| | **Address** <Adr> | [1..1] | ± | | 47 |
| | **DeliveryMethod** <DlvyMtd> | [0..1] | | | 47 |
| Or | **Code** <Cd> | [1..1] | CodeSet | | 48 |
| Or | **Proprietary** <Prtry> | [1..1] | Text | | 48 |
| | **DeliverTo** <DlvrTo> | [0..1] | | | 48 |
| | **Name** <Nm> | [1..1] | Text | | 49 |
| | **Address** <Adr> | [1..1] | ± | | 49 |
| | **InstructionPriority** <InstrPrty> | [0..1] | CodeSet | | 49 |
| | **ChequeMaturityDate** <ChqMtrtyDt> | [0..1] | Date | | 50 |
| | **FormsCode** <FrmsCd> | [0..1] | Text | | 50 |
| | **MemoField** <MemoFld> | [0..2] | Text | | 50 |
| | **RegionalClearingZone** <RgnlClrZone> | [0..1] | Text | | 50 |
| | **PrintLocation** <PrnLctn> | [0..1] | Text | | 50 |
| | **Signature** <Sgntr> | [0..5] | Text | | 50 |
| | **UltimateDebtor** <UltmtDbtr> | [0..1] | ± | | 50 |

---

<!-- Page 38 -->

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | IntermediaryAgent1 *<IntmyAg1>* | [0..1] | ± |  | 51 |
| | IntermediaryAgent1Account *<IntmyAg1Acct>* | [0..1] | ± | C21, C20 | 52 |
| | IntermediaryAgent2 *<IntmyAg2>* | [0..1] | ± |  | 53 |
| | IntermediaryAgent2Account *<IntmyAg2Acct>* | [0..1] | ± | C21, C20 | 53 |
| | IntermediaryAgent3 *<IntmyAg3>* | [0..1] | ± |  | 54 |
| | IntermediaryAgent3Account *<IntmyAg3Acct>* | [0..1] | ± | C21, C20 | 55 |
| | CreditorAgent *<CdttrAg1>* | [0..1] | ± |  | 56 |
| | CreditorAgentAccount *<CdttrAg1Acct>* | [0..1] | ± | C21, C20 | 56 |
| | Creditor *<Cdttr>* | [0..1] | ± |  | 57 |
| | CreditorAccount *<CdttrAcct>* | [0..1] | ± | C21, C20 | 58 |
| | UltimateCreditor *<UltmtCdttr>* | [0..1] | ± |  | 59 |
| | InstructionForCreditorAgent *<InstrForCdttrAg1>* | [0..*] | ± |  | 60 |
| | InstructionForDebtorAgent *<InstrForDbtrAg1>* | [0..1] |  |  | 61 |
| | Code *<Cd>* | [0..1] | CodeSet |  | 61 |
| | InstructionInformation *<InstrInf>* | [0..1] | Text |  | 61 |
| | Purpose *<Purp>* | [0..1] | ± |  | 61 |
| | RegulatoryReporting *<RgltryRptg>* | [0..10] | ± |  | 62 |
| | Tax *<Tax>* | [0..1] |  |  | 62 |
| | Creditor *<Cdttr>* | [0..1] | ± |  | 64 |
| | Debtor *<Dbtr>* | [0..1] | ± |  | 64 |
| | UltimateDebtor *<UltmtDbtr>* | [0..1] | ± |  | 64 |
| | AdministrationZone *<AdminZone>* | [0..1] | Text |  | 65 |
| | ReferenceNumber *<RefNb>* | [0..1] | Text |  | 65 |
| | Method *<Mtd>* | [0..1] | Text |  | 65 |
| | TotalTaxableBaseAmount *<TtlTaxblBaseAmt>* | [0..1] | Amount | C1, C18 | 65 |
| | TotalTaxAmount *<TtlTaxAmt>* | [0..1] | Amount | C1, C18 | 66 |
| | Date *<Dt>* | [0..1] | Date |  | 66 |
| | SequenceNumber *<SeqNb>* | [0..1] | Quantity |  | 66 |
| | Record *<Rcrd>* | [0..*] |  |  | 66 |

---

<!-- Page 39 -->

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **Type** `<Tp>` | [0..1] | Text | | 67 |
| | **Category** `<Ccy>` | [0..1] | Text | | 67 |
| | **CategoryDetails** `<CcyDtls>` | [0..1] | Text | | 67 |
| | **DebtorStatus** `<DbtrSts>` | [0..1] | Text | | 68 |
| | **CertificateIdentification** `<CertId>` | [0..1] | Text | | 68 |
| | **FormsCode** `<FrmsCd>` | [0..1] | Text | | 68 |
| | **Period** `<Prd>` | [0..1] | | | 68 |
| | **Year** `<Yr>` | [0..1] | Year | | 68 |
| | **Type** `<Tp>` | [0..1] | CodeSet | | 68 |
| | **FromToDate** `<FrToDt>` | [0..1] | ± | | 69 |
| | **TaxAmount** `<TaxAmt>` | [0..1] | | | 70 |
| | **Rate** `<Rate>` | [0..1] | Rate | | 70 |
| | **TaxableBaseAmount** `<TaxblBaseAmt>` | [0..1] | Amount | C1, C18 | 70 |
| | **TotalAmount** `<TtlAmt>` | [0..1] | Amount | C1, C18 | 70 |
| | **Details** `<Dtls>` | [0..*] | | | 71 |
| | **Period** `<Prd>` | [0..1] | | | 71 |
| | **Year** `<Yr>` | [0..1] | Year | | 71 |
| | **Type** `<Tp>` | [0..1] | CodeSet | | 72 |
| | **FromToDate** `<FrToDt>` | [0..1] | ± | | 72 |
| | **Amount** `<Amt>` | [1..1] | Amount | C1, C18 | 73 |
| | **AdditionalInformation** `<AddtlInf>` | [0..1] | Text | | 73 |
| | **RelatedRemittanceInformation** `<RltdRmInf>` | [0..10] | | | 73 |
| | **RemittanceIdentification** `<RmId>` | [0..1] | Text | | 74 |
| | **RemittanceLocationDetails** `<RmLctnDtls>` | [0..*] | | | 74 |
| | **Method** `<Mtd>` | [1..1] | CodeSet | | 74 |
| | **ElectronicAddress** `<ElctronicAdr>` | [0..1] | Text | | 75 |
| | **PostalAddress** `<PstlAdr>` | [0..1] | | | 75 |
| | **Name** `<Nm>` | [1..1] | Text | | 75 |
| | **Address** `<Adr>` | [1..1] | ± | | 75 |
| | **RemittanceInformation** `<RmInf>` | [0..1] | ± | | 76 |
| | **SupplementaryData** `<SplmtryData>` | [0..*] | ± | C33 | 77 |

---

<!-- Page 40 -->

## Constraints

* **InstructionForCreditorAgentRule**

  If InstructionForCreditorAgent/Code contains CHQB, then Creditor/Account is not allowed.

  On Condition
  /InstructionForCreditorAgent/*/Code is within DataType <<Code>>
  ValidationRulePayCreditorByCheque1Code
  Following Must be True
  /Creditor/Account Must be absent

* **IntermediaryAgent1AccountRule**

  If IntermediaryAgent1/Account is present, then IntermediaryAgent1 must be present.

  On Condition
  /IntermediaryAgent1 is absent
  Following Must be True
  /IntermediaryAgent1/Account Must be absent

* **IntermediaryAgent2AccountRule**

  If IntermediaryAgent2/Account is present, then IntermediaryAgent2 must be present.

  On Condition
  /IntermediaryAgent2 is absent
  Following Must be True
  /IntermediaryAgent2/Account Must be absent

* **IntermediaryAgent2Rule**

  If IntermediaryAgent2 is present, then IntermediaryAgent1 must be present.

  On Condition
  /IntermediaryAgent2 is present
  Following Must be True
  /IntermediaryAgent1 Must be present

* **IntermediaryAgent3AccountRule**

  If IntermediaryAgent3/Account is present, then IntermediaryAgent3 must be present.

  On Condition
  /IntermediaryAgent3 is absent
  Following Must be True
  /IntermediaryAgent3/Account Must be absent

* **IntermediaryAgent3Rule**

  If IntermediaryAgent3 is present, then IntermediaryAgent2 must be present.

  On Condition
  /IntermediaryAgent3 is present
  Following Must be True
  /IntermediaryAgent2 Must be present

* **UltimateCreditorGuideline**

  UltimateCreditor may only be present if different from Creditor.

* **UltimateDebtorGuideline**

  UltimateDebtor may only be present if different from Debtor.

### 2.4.2.19.1. PaymentIdentification <PmtId>

*Presence:* [1..1]

*Definition:* Set of elements used to reference a payment instruction.

---

<!-- Page 41 -->

PaymentIdentification <PmtId> contains the following elements (see "PaymentIdentification6" on page 330 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | InstructionIdentification <InstrId> | [0..1] | Text | | 330 |
| | EndToEndIdentification <EndToEndId> | [1..1] | Text | | 330 |
| | UETR <UETR> | [0..1] | IdentifierSet | | 330 |

## 2.4.2.19.2 PaymentTypeInformation <PmtTpInf>

*Presence: [0..1]*

*Definition: Set of elements used to further specify the type of transaction.*

PaymentTypeInformation <PmtTpInf> contains the following elements (see "PaymentTypeInformation26" on page 346 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | InstructionPriority <InstrPrty> | [0..1] | CodeSet | | 346 |
| | ServiceLevel <SvcLv> | [0..] | | | 346 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 347 |
| Or) | Proprietary <Prtry> | [1..1] | Text | | 347 |
| | LocalInstrument <LclInstrm> | [0..1] | | | 347 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 347 |
| Or) | Proprietary <Prtry> | [1..1] | Text | | 347 |
| | CategoryPurpose <CatgPurp> | [0..1] | | | 347 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 348 |
| Or) | Proprietary <Prtry> | [1..1] | Text | | 348 |

## 2.4.2.19.3 Amount <Amt>

*Presence: [1..1]*

*Definition: Amount of money to be moved between the debtor and creditor, before deduction of charges, expressed in the currency as ordered by the initiating party.*

Amount <Amt> contains one of the following elements (see "AmountType4Choice" on page 314 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| (Or | InstructedAmount <InstdAmt> | [1..1] | Amount | C2, C8 | 314 |
| Or) | EquivalentAmount <EqvtAmt> | [1..1] | | | 315 |
| | Amount <Amt> | [1..1] | Amount | C2, C8 | 315 |
| | CurrencyOfTransfer <CcyOfTrf> | [1..1] | CodeSet | C2 | 315 |

---

<!-- Page 42 -->

## 2.4.2.19.4 ExchangeRateInformation <XchgRateInf>

*Presence:* [0..1]

*Definition:* Provides details on the currency exchange rate and contract.

**ExchangeRateInformation** <XchgRateInf> contains the following **ExchangeRate1** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **UnitCurrency** <UnitCcy> | [0..1] | CodeSet | C1 | 42 |
| | **ExchangeRate** <XchgRate> | [0..1] | Rate | | 42 |
| | **RateType** <RateTp> | [0..1] | CodeSet | | 42 |
| | **ContractIdentification** <CtrId> | [0..1] | Text | | 43 |

## 2.4.2.19.4.1 UnitCurrency <UnitCcy>

*Presence:* [0..1]

*Definition:* Currency in which the rate of exchange is expressed in a currency exchange. In the example 1GBP = xxxCUR, the unit currency is GBP.

*Impacted by:* C1 "ActiveOrHistoricCurrency"

*Datatype:* "ActiveOrHistoricCurrencyCode" on page 409

**Constraints**

*   **ActiveOrHistoricCurrency**
    *   The Currency Code must be registered, or have already been registered. Valid active or historic currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and may be or not be withdrawn on the day the message containing the Currency is exchanged.

## 2.4.2.19.4.2 ExchangeRate <XchgRate>

*Presence:* [0..1]

*Definition:* The factor used for conversion of an amount from one currency to another. This reflects the price at which one currency was bought with another currency.

*Datatype:* "BaseOneRate" on page 428

## 2.4.2.19.4.3 RateType <RateTp>

*Presence:* [0..1]

*Definition:* Specifies the type used to complete the currency exchange.

*Datatype:* "ExchangeRateType1Code" on page 413

| CodeName | Name | Definition |
|---|---|---|
| SPOT | Spot | Exchange rate applied is the spot rate. |
| SALE | Sale | Exchange rate applied is the market rate at the time of the sale. |
| AGRD | Agreed | Exchange rate applied is the rate agreed between the parties. |

---

<!-- Page 43 -->

2.4.2.19.4.4 ContractIdentification <CtrctId>

*Presence:* [0..1]

*Definition:* Unique and unambiguous reference to the foreign exchange contract agreed between the initiating party/creditor and the debtor agent.

*Datatype:* "Max35Text" on page 431

## 2.4.2.19.5 ChargeBearer <ChrgBr>

*Presence:* [0..1]

*Definition:* Specifies which party/parties will bear the charges associated with the processing of the payment transaction.

*Datatype:* "ChargeBearerType1Code" on page 410



<table>
  <tr>
    <th>CodeName</th>
    <th>Name</th>
    <th>Definition</th>
  </tr>
  <tr>
    <td>DEBT</td>
    <td>BorneByDebtor</td>
    <td>All transaction charges are to be borne by the debtor.</td>
  </tr>
  <tr>
    <td>CRED</td>
    <td>BorneByCreditor</td>
    <td>All transaction charges are to be borne by the creditor.</td>
  </tr>
  <tr>
    <td>SHAR</td>
    <td>Shared</td>
    <td>In a credit transfer context, means that transaction charges on the sender side are to be borne by the debtor, transaction charges on the receiver side are to be borne by the creditor. In a direct debit context, means that transaction charges on the sender side are to be borne by the creditor, transaction charges on the receiver side are to be borne by the debtor.</td>
  </tr>
  <tr>
    <td>SLEV</td>
    <td>FollowingServiceLevel</td>
    <td>Charges are to be applied following the rules agreed in the service level and/or scheme.</td>
  </tr>
</table>

## 2.4.2.19.6 MandateRelatedInformation <MndtRltdInf>

*Presence:* [0..1]

*Definition:* Provides further details of the mandate signed between the creditor and the debtor.

---

<!-- Page 44 -->

MandateRelatedInformation <MndtRltdInf> contains the following elements (see "CreditTransferMandateData1" on page 317 for details)



<table>
  <tr>
    <th>Or</th>
    <th>MessageElement&lt;XML Tag&gt;</th>
    <th>Mult.</th>
    <th>Type</th>
    <th>Constr. No.</th>
    <th>Page</th>
  </tr>
  <tr>
    <td></td>
    <td>MandateIdentification &lt;MndtId&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>317</td>
  </tr>
  <tr>
    <td></td>
    <td>Type &lt;Tp&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>317</td>
  </tr>
  <tr>
    <td></td>
    <td>DateOfSignature &lt;DtOfSgntr&gt;</td>
    <td>[0..1]</td>
    <td>Date</td>
    <td></td>
    <td>318</td>
  </tr>
  <tr>
    <td></td>
    <td>DateOfVerification &lt;DtOfVrfctn&gt;</td>
    <td>[0..1]</td>
    <td>DateTime</td>
    <td></td>
    <td>318</td>
  </tr>
  <tr>
    <td></td>
    <td>ElectronicSignature &lt;ElctrncSgntr&gt;</td>
    <td>[0..1]</td>
    <td>Binary</td>
    <td></td>
    <td>318</td>
  </tr>
  <tr>
    <td></td>
    <td>FirstPaymentDate &lt;FrstPmtDt&gt;</td>
    <td>[0..1]</td>
    <td>Date</td>
    <td></td>
    <td>318</td>
  </tr>
  <tr>
    <td></td>
    <td>FinalPaymentDate &lt;FnlpmtDt&gt;</td>
    <td>[0..1]</td>
    <td>Date</td>
    <td></td>
    <td>318</td>
  </tr>
  <tr>
    <td></td>
    <td>Frequency &lt;Frqcy&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>319</td>
  </tr>
  <tr>
    <td></td>
    <td>Reason &lt;Rsn&gt;</td>
    <td>[0..1]</td>
    <td></td>
    <td></td>
    <td>319</td>
  </tr>
  <tr>
    <td>Or</td>
    <td>Code &lt;Cd&gt;</td>
    <td>[1..1]</td>
    <td>CodeSet</td>
    <td></td>
    <td>319</td>
  </tr>
  <tr>
    <td>Or</td>
    <td>Proprietary &lt;Ptry&gt;</td>
    <td>[1..1]</td>
    <td>Text</td>
    <td></td>
    <td>319</td>
  </tr>
</table>

### 2.4.2.19.7 ChequeInstruction <ChqInstr>

*Presence: [0..1]*

*Definition: Set of elements needed to issue a cheque.*

*Impacted by: C15 "ChequeMaturityDateRule"*

---

<!-- Page 45 -->

ChequeInstruction <ChqInstr> contains the following Cheque19 elements

| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | ChequeType <ChqTp> | [0..1] | CodeSet | | 45 |
| | ChequeNumber <ChqNb> | [0..1] | Text | | 46 |
| | ChequeFrom <ChqFr> | [0..1] | | | 46 |
| | Name <Nm> | [1..1] | Text | | 46 |
| | Address <Adr> | [1..1] | ± | | 47 |
| | DeliveryMethod <DlvyMtd> | [0..1] | | | 47 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 48 |
| Or) | Proprietary <Prtry> | [1..1] | Text | | 48 |
| | DeliverTo <DlvrTo> | [0..1] | | | 48 |
| | Name <Nm> | [1..1] | Text | | 49 |
| | Address <Adr> | [1..1] | ± | | 49 |
| | InstructionPriority <InstrPrty> | [0..1] | CodeSet | | 49 |
| | ChequeMaturityDate <ChqMtrtyDt> | [0..1] | Date | | 50 |
| | FormsCode <FrmsCd> | [0..1] | Text | | 50 |
| | MemoField <MemoFld> | [0..2] | Text | | 50 |
| | RegionalClearingZone <RgnlClrZone> | [0..1] | Text | | 50 |
| | PrintLocation <PrtLctn> | [0..1] | Text | | 50 |
| | Signature <Sgntr> | [0..5] | Text | | 50 |

## Constraints

- ChequeMaturityDateRule

  If ChequeMaturityDate is present, then ChequeType must be present and equal to DRFT or ELDR.

  ```
  On Condition
  /ChequeMaturityDate is present
  Following Must be True
  /ChequeType Must be present
  And     /ChequeType Must be within DataType <Code> ChequeType3Code
  ```

### 2.4.2.19.7.1 ChequeType <ChqTp>

*Presence:* [0..1]

*Definition:* Specifies the type of cheque to be issued.

*DataType:* "ChequeType2Code" on page 411

| CodeName | Name | Definition |
|---|---|---|
| CCHQ | CustomerCheque | Cheque drawn on the account of the debtor, and debited on the debtor's |

---

<!-- Page 46 -->

| CodeName | Name | Definition |
|---|---|---|
| | | account when the cheque is cashed. Synonym is 'corporate cheque'. |
| CCCH | CertifiedCustomerCheque | Cheque drawn on the account of the debtor, and debited on the debtor's account when the cheque is cashed. The financial institution prints and certifies the cheque, guaranteeing the payment. |
| BCHQ | BankCheque | Cheque drawn on the account of the debtor's financial institution, which is debited on the debtor's account when the cheque is issued. These cheques are printed by the debtor's financial institution and payment is guaranteed by the financial institution. Synonym is 'cashier's cheque'. |
| DRFT | Draft | A guaranteed bank cheque with a future value date (do not pay before), which in commercial terms is a 'negotiable instrument': the beneficiary can receive early payment from any bank under subtraction of a discount. The ordering customer's account is debited on value date. |
| ELDR | ElectronicDraft | An instrument with a future value date (do not pay before), which in commercial terms is a 'negotiable instrument': the beneficiary can receive early payment from any bank under subtraction of a discount. The ordering customer's account is debited on value date. |

## 2.4.2.19.7.2 ChequeNumber <ChqNb>

*Presence:* [0..1]

*Definition:* Unique and unambiguous identifier for a cheque as assigned by the agent.

*DataType:* "Max35Text" on page 431

## 2.4.2.19.7.3 ChequeFrom <ChqFr>

*Presence:* [0..1]

*Definition:* Identifies the party that ordered the issuance of the cheque.

**ChequeFrom <ChqFr>** contains the following **NameAndAddress18** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **Name** *<Nm>* | [1..1] | Text | | 46 |
| | **Address** *<Adr>* | [1..1] | ± | | 47 |

### 2.4.2.19.7.3.1 Name <Nm>

*Presence:* [1..1]

*Definition:* Name by which a party is known and is usually used to identify that party.

*DataType:* "Max140Text" on page 429

---

<!-- Page 47 -->

2.4.2.19.7.3.2 Address <Adr>

Presence: [1..1]

Definition: Postal address of a party.

Address <Adr> contains the following elements (see "PostalAddress27" on page 357 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | AddressType <AdrTp> | [0..1] | | | 357 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 358 |
| Or) | Proprietary <Ptry> | [1..1] | ± | | 358 |
| | CareOf <CareOf> | [0..1] | Text | | 358 |
| | Department <Dept> | [0..1] | Text | | 358 |
| | SubDepartment <SubDept> | [0..1] | Text | | 359 |
| | StreetName <StrtNm> | [0..1] | Text | | 359 |
| | BuildingNumber <BldgNb> | [0..1] | Text | | 359 |
| | BuildingName <BldgNm> | [0..1] | Text | | 359 |
| | Floor <Flr> | [0..1] | Text | | 359 |
| | UnitNumber <UnitNb> | [0..1] | Text | | 359 |
| | PostBox <PstBx> | [0..1] | Text | | 359 |
| | Room <Room> | [0..1] | Text | | 359 |
| | PostCode <PstCd> | [0..1] | Text | | 360 |
| | TownName <TwnNm> | [0..1] | Text | | 360 |
| | TownLocationName <TwnLctnNm> | [0..1] | Text | | 360 |
| | DistrictName <DstrctNm> | [0..1] | Text | | 360 |
| | CountrySubDivision <CtrySubDvsn> | [0..1] | Text | | 360 |
| | Country <Ctry> | [0..1] | CodeSet | C7 | 360 |
| | AddressLine <AdrLine> | [0..7] | Text | | 360 |

2.4.2.19.7.4 DeliveryMethod <DVryMtd>

Presence: [0..1]

Definition: Specifies the delivery method of the cheque by the debtor's agent.

DeliveryMethod <DVryMtd> contains one of the following ChequeDeliveryMethod1Choice elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| (Or | Code <Cd> | [1..1] | CodeSet | | 48 |
| Or) | Proprietary <Ptry> | [1..1] | Text | | 48 |

---

<!-- Page 48 -->

**2.4.2.19.7.4.1 Code <Cd>**

*Presence:* [1..1]

*Definition:* Specifies the delivery method of the cheque by the debtor's agent.

*Datatype:* "ChequeDelivery1Code" on page 411



| CodeName | Name | Definition |
| :--- | :--- | :--- |
| MLDB | MailToDebtor | Cheque is to be sent through mail services to debtor. |
| MLCD | MailToCreditor | Cheque is to be sent through mail services to creditor. |
| MLFA | MailToFinalAgent | Cheque is to be sent through mail services to creditor agent. |
| CRDB | CourierToDebtor | Cheque is to be sent through courier services to debtor. |
| CRCD | CourierToCreditor | Cheque is to be sent through courier services to creditor. |
| CRFA | CourierToFinalAgent | Cheque is to be sent through courier services to creditor agent. |
| PUDB | PickUpByDebtor | Cheque will be picked up by the debtor. |
| PUCD | PickUpByCreditor | Cheque will be picked up by the creditor. |
| PUFA | PickUpByFinalAgent | Cheque will be picked up by the creditor agent. |
| RGDB | RegisteredMailToDebtor | Cheque is to be sent through registered mail services to debtor. |
| RGCD | RegisteredMailToCreditor | Cheque is to be sent through registered mail services to creditor. |
| RGFA | RegisteredMailToFinalAgent | Cheque is to be sent through registered mail services to creditor agent. |

**2.4.2.19.7.4.2 Proprietary <Prtry>**

*Presence:* [1..1]

*Definition:* Specifies a proprietary delivery method of the cheque by the debtor's agent.

*Datatype:* "Max35Text" on page 431

**2.4.2.19.7.5 DeliverTo <DlvrTo>**

*Presence:* [0..1]

*Definition:* Party to whom the debtor's agent needs to send the cheque.

DeliverTo <DlvrTo> contains the following **NameAndAddress18** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
| :--- | :--- | :--- | :--- | :--- | :--- |
| | **Name** <Nm> | [1..1] | Text | | 49 |
| | **Address** <Adr> | [1..1] | ± | | 49 |

---

<!-- Page 49 -->

2.4.2.19.7.5.1 Name <Nm>

Presence: [1..1]

Definition: Name by which a party is known and is usually used to identify that party.

Datatype: "Max140Text" on page 429

2.4.2.19.7.5.2 Address <Adr>

Presence: [1..1]

Definition: Postal address of a party.

Address <Adr> contains the following elements (see "PostalAddress27" on page 357 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | AddressType <AdrTp> | [0..1] | | | 357 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 358 |
| Or) | Proprietary <Prtry> | [1..1] | ± | | 358 |
| | CareOf <CareOf> | [0..1] | Text | | 358 |
| | Department <Dept> | [0..1] | Text | | 358 |
| | SubDepartment <SubDept> | [0..1] | Text | | 359 |
| | StreetName <StrtNm> | [0..1] | Text | | 359 |
| | BuildingNumber <BldgNb> | [0..1] | Text | | 359 |
| | BuildingName <BldgNm> | [0..1] | Text | | 359 |
| | Floor <Flr> | [0..1] | Text | | 359 |
| | UnitNumber <UnitNb> | [0..1] | Text | | 359 |
| | PostBox <PstBx> | [0..1] | Text | | 359 |
| | Room <Room> | [0..1] | Text | | 359 |
| | PostCode <PstCd> | [0..1] | Text | | 360 |
| | TownName <TwnNm> | [0..1] | Text | | 360 |
| | TownLocationName <TwnLctnNm> | [0..1] | Text | | 360 |
| | DistrictName <DstrctNm> | [0..1] | Text | | 360 |
| | CountrySubDivision <CtrySubDvsn> | [0..1] | Text | | 360 |
| | Country <Ctry> | [0..1] | CodeSet | C7 | 360 |
| | AddressLine <AdrLine> | [0..7] | Text | | 360 |

2.4.2.19.7.6 InstructionPriority <InstrPrty>

Presence: [0..1]

Definition: Urgency or order of importance that the originator would like the recipient of the payment instruction to apply to the processing of the payment instruction.

Datatype: "Priority2Code" on page 422

---

<!-- Page 50 -->

| CodeName | Name | Definition |
| :--- | :--- | :--- |
| HIGH | High | Priority level is high. |
| NORM | Normal | Priority level is normal. |

**2.4.2.19.7.7 ChequeMaturityDate <ChqMtrtyDt>**

*Presence:* [0..1]

*Definition:* Date when the draft becomes payable and the debtor's account is debited.

*Datatype:* "ISODate" on page 425

**2.4.2.19.7.8 FormsCode <FrmsCd>**

*Presence:* [0..1]

*Definition:* Identifies, in a coded form, the cheque layout, company logo and digitised signature to be used to print the cheque, as agreed between the initiating party and the debtor's agent.

*Datatype:* "Max35Text" on page 431

**2.4.2.19.7.9 MemoField <MemoFld>**

*Presence:* [0..2]

*Definition:* Information that needs to be printed on a cheque, used by the payer to add miscellaneous information.

*Datatype:* "Max35Text" on page 431

**2.4.2.19.7.10 RegionalClearingZone <RgnlClrZone>**

*Presence:* [0..1]

*Definition:* Regional area in which the cheque can be cleared, when a country has no nation-wide cheque clearing organisation.

*Datatype:* "Max35Text" on page 431

**2.4.2.19.7.11 PrintLocation <PrntLctn>**

*Presence:* [0..1]

*Definition:* Specifies the print location of the cheque.

*Datatype:* "Max35Text" on page 431

**2.4.2.19.7.12 Signature <Sgntr>**

*Presence:* [0..5]

*Definition:* Signature to be used by the cheque servicer on a specific cheque to be printed.

*Datatype:* "Max70Text" on page 431

**2.4.2.19.8 UltimateDebtor <UltmtDbtr>**

*Presence:* [0..1]

*Definition:* Ultimate party that owes an amount of money to the (ultimate) creditor.

---

<!-- Page 51 -->

UltimateDebtor <UltmtdBtr> contains the following elements (see 'PartyIdentification27' on page 336 for details)



| Or | MessageElement<XML Tag> | Mult. | Type | Const. No. | Page |
|---|---|---|---|---|---|
| | Name <Nm> | [0..1] | Text | | 337 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 338 |
| | Identification <Id> | [0..1] | | | 338 |
| (Or | OrganisationIdentification <OrgId> | [1..1] | | | 339 |
| | AnyBIC <AnyBIC> | [0..1] | IdentifierSet | C5 | 340 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 340 |
| | Other <Othr> | [0..*] | | | 340 |
| | Identification <Id> | [1..1] | Text | | 341 |
| | SchemeName <SchmeNm> | [0..1] | | | 341 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 341 |
| Or | Proprietary <Prtry> | [1..1] | Text | | 341 |
| | Issuer <Issr> | [0..1] | Text | | 341 |
| (Or | PrivateIdentification <PrvtId> | [1..1] | | | 341 |
| | DateAndPlaceOfBirth <DtAndPlcOfBirth> | [0..1] | | | 342 |
| | BirthDate <BirthDt> | [1..1] | Date | | 342 |
| | ProvinceOfBirth <PrvcOfBirth> | [0..1] | Text | | 342 |
| | CityOfBirth <CityOfBirth> | [1..1] | Text | | 343 |
| | CountryOfBirth <CtryOfBirth> | [1..1] | CodeSet | C7 | 343 |
| | Other <Othr> | [0..*] | | | 343 |
| | Identification <Id> | [1..1] | Text | | 343 |
| | SchemeName <SchmeNm> | [0..1] | | | 343 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 344 |
| Or | Proprietary <Prtry> | [1..1] | Text | | 344 |
| | Issuer <Issr> | [0..1] | Text | | 344 |
| | CountryOfResidence <CtryOfRes> | [0..1] | CodeSet | C7 | 344 |
| | ContactDetails <CtctDtls> | [0..1] | ± | | 344 |

## 2.4.2.19.9 IntermediaryAgent1 <IntrmyAgt1>

*Presence:* [0..1]

*Definition:* Agent between the debtor's agent and the creditor's agent.

---

<!-- Page 52 -->

Usage: If more than one intermediary agent is present, then IntermediaryAgent1 identifies the agent between the Debtor Agent and the IntermediaryAgent2.

**IntermediaryAgent1** *<IntrmyAgt1>* contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on page 320 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | FinancialInstitutionIdentification *<FinInstlId>* | [0..1] |  |  | 321 |
| | BICFI *<BICFI>* | [0..1] | IdentifierSet | C6 | 321 |
| | ClearingSystemMemberIdentification *<ClrSysMmbId>* | [0..1] | ± |  | 322 |
| | LEI *<LEI>* | [0..1] | IdentifierSet |  | 322 |
| | Name *<Nm>* | [0..1] | Text |  | 322 |
| | PostalAddress *<PstlAdr>* | [0..1] | ± |  | 323 |
| | Other *<Othr>* | [0..1] | ± |  | 323 |
| | BranchIdentification *<BrnchId>* | [0..1] |  |  | 324 |
| | Identification *<Id>* | [0..1] | Text |  | 324 |
| | LEI *<LEI>* | [0..1] | IdentifierSet |  | 324 |
| | Name *<Nm>* | [0..1] | Text |  | 324 |
| | PostalAddress *<PstlAdr>* | [0..1] | ± |  | 324 |

## 2.4.2.19.10 IntermediaryAgent1Account *<IntrmyAgt1Acct>*

*Presence:* [0..1]

*Definition:* Unambiguous identification of the account of the intermediary agent 1 at its servicing agent in the payment chain.

*Impacted by:* C21 "IdentificationOrProxyPresenceRule", C20 "IdentificationAndProxyGuideline"

**IntermediaryAgent1Account** *<IntrmyAgt1Acct>* contains the following elements (see "CashAccount40" on page 309 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Identification *<Id>* | [0..1] | ± |  | 310 |
| | Type *<Tp>* | [0..1] | ± |  | 310 |
| | Currency *<Ccy>* | [0..1] | CodeSet | C2 | 310 |
| | Name *<Nm>* | [0..1] | Text |  | 311 |
| | Proxy *<Prxy>* | [0..1] | ± |  | 311 |

---

<!-- Page 53 -->

Constraints

* **IdentificationAndProxyGuideline**

If the account identification is not defined through a conventional identification such as an email address or a mobile number, then the proxy element should be used for the identification of the account.

* **IdentificationOrProxyPresenceRule**

Identification must be present or Proxy must be present. Both may be present.

```
Following Must be True
/Identification Must be present
Or
/Proxy Must be present
```

## 2.4.2.19.11 IntermediaryAgent2 <IntrmyAg2>

Presence: [0..1]

Definition: Agent between the debtor's agent and the creditor's agent.

Usage: If more than two intermediary agents are present, then IntermediaryAgent2 identifies the agent between the IntermediaryAgent1 and the IntermediaryAgent3.

IntermediaryAgent2 <IntrmyAg2> contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on page 320 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
| :--- | :--- | :--- | :--- | :--- | :--- |
| | FinancialInstitutionIdentification <FinInstlId> | [1..1] | | | 321 |
| | BICFI <BICFI/> | [0..1] | IdentifierSet | C6 | 321 |
| | ClearingSystemMemberIdentification <ClrSysMmbId> | [0..1] | ± | | 322 |
| | LEI <LEI/> | [0..1] | IdentifierSet | | 322 |
| | Name <Nm/> | [0..1] | Text | | 322 |
| | PostalAddress <PstlAdr/> | [0..1] | ± | | 322 |
| | Other <Othr/> | [0..1] | ± | | 323 |
| | BranchIdentification <BrnchId/> | [0..1] | | | 324 |
| | Identification <Id/> | [0..1] | Text | | 324 |
| | LEI <LEI/> | [0..1] | IdentifierSet | | 324 |
| | Name <Nm/> | [0..1] | Text | | 324 |
| | PostalAddress <PstlAdr/> | [0..1] | ± | | 324 |

## 2.4.2.19.12 IntermediaryAgent2Account <IntrmyAg2Acct>

Presence: [0..1]

Definition: Unambiguous identification of the account of the intermediary agent 2 at its servicing agent in the payment chain.

Impacted by: C21 "IdentificationOrProxyPresenceRule", C20 "IdentificationAndProxyGuideline"

---

<!-- Page 54 -->

IntermediaryAgent2Account <IntrmyAgt2Acct> contains the following elements (see "CashAccount40" on page 309 for details)



<table><tr><td>Or</td><td>MessageElement&lt;XML Tag&gt;</td><td>Mult.</td><td>Type</td><td>Constr. No.</td><td>Page</td></tr><tr><td></td><td>Identification &lt;Ids&gt;</td><td>[0..1]</td><td>±</td><td></td><td>310</td></tr><tr><td></td><td>Type &lt;Tp&gt;</td><td>[0..1]</td><td>±</td><td></td><td>310</td></tr><tr><td></td><td>Currency &lt;Ccy&gt;</td><td>[0..1]</td><td>CodeSet</td><td>C2</td><td>310</td></tr><tr><td></td><td>Name &lt;Nm&gt;</td><td>[0..1]</td><td>Text</td><td></td><td>311</td></tr><tr><td></td><td>Proxy &lt;Prxy&gt;</td><td>[0..1]</td><td>±</td><td></td><td>311</td></tr></table>

## Constraints

- **IdentificationAndProxyGuideline**

If the account identification is not defined through a conventional identification such as an email address or a mobile number, then the proxy element should be used for the identification of the account.

- **IdentificationOrProxyPresenceRule**

Identification must be present or Proxy must be present. Both may be present.

```
Following Must be True
/Identification Must be present
Or
/Proxy Must be present
```

### 2.4.2.19.13 IntermediaryAgent3 <IntrmyAgt3>

Presence: [0..1]

Definition: Agent between the debtor's agent and the creditor's agent.

Usage: If IntermediaryAgent3 is present, then it identifies the agent between the IntermediaryAgent 2 and the CreditorAgent.

---

<!-- Page 55 -->

IntermediaryAgent3 <IntrmyAgt3> contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on page 320 for details)



| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | FinancialInstitutionIdentification <FinInstId> | [0..1] |  |  | 321 |
| | BICFI <BICFI> | [0..1] | IdentifierSet | C6 | 321 |
| | ClearingSystemMemberIdentification <ClrSysMmbId> | [0..1] | ± |  | 322 |
| | LEI <LEI> | [0..1] | IdentifierSet |  | 322 |
| | Name <Nm> | [0..1] | Text |  | 322 |
| | PostalAddress <PstlAdr> | [0..1] | ± |  | 322 |
| | Other <Othr> | [0..1] | ± |  | 323 |
| | BranchIdentification <BrnchId> | [0..1] |  |  | 324 |
| | Identification <Id> | [0..1] | Text |  | 324 |
| | LEI <LEI> | [0..1] | IdentifierSet |  | 324 |
| | Name <Nm> | [0..1] | Text |  | 324 |
| | PostalAddress <PstlAdr> | [0..1] | ± |  | 324 |

## 2.4.2.19.14 IntermediaryAgent3Account <IntrmyAgt3Acct>

Presence: [0..1]

Definition: Unambiguous identification of the account of the intermediary agent 3 at its servicing agent in the payment chain.

Impacted by: C21 "IdentificationOrProxyPresenceRule", C20 "IdentificationAndProxyGuideline"

IntermediaryAgent3Account <IntrmyAgt3Acct> contains the following elements (see "CashAccount40" on page 309 for details)



| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Identification <Id> | [0..1] | ± |  | 310 |
| | Type <Tp> | [0..1] | ± |  | 310 |
| | Currency <Ccy> | [0..1] | CodeSet | C2 | 310 |
| | Name <Nm> | [0..1] | Text |  | 311 |
| | Proxy <Prxy> | [0..1] | ± |  | 311 |

---

<!-- Page 56 -->

Constraints

* **IdentificationAndProxyGuideline**

If the account identification is not defined through a conventional identification such as an email address or a mobile number, then the proxy element should be used for the identification of the account.

* **IdentificationOrProxyPresenceRule**

Identification must be present or Proxy must be present. Both may be present.

```
Following Must be True
/Identification Must be present
Or
/Proxy Must be present
```

## 2.4.2.19.15 CreditorAgent <CdtrAg>

Presence: [0..1]

Definition: Financial institution servicing an account for the creditor.

**CreditorAgent <CdtrAg>** contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on page 320 for details)



| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | FinancialInstitutionIdentification <FinInstlId> | [0..1] | | | 321 |
| | BICFI <BICFI> | [0..1] | IdentifierSet | C6 | 321 |
| | ClearingSystemMemberIdentification <ClrSysMmbId> | [0..1] | ± | | 322 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 322 |
| | Name <Nm> | [0..1] | Text | | 322 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 322 |
| | Other <Othr> | [0..1] | ± | | 323 |
| | BranchIdentification <BrnchId> | [0..1] | | | 324 |
| | Identification <Id> | [0..1] | Text | | 324 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 324 |
| | Name <Nm> | [0..1] | Text | | 324 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 324 |

## 2.4.2.19.16 CreditorAgentAccount <CdtrAgtAcct>

Presence: [0..1]

Definition: Unambiguous identification of the account of the creditor agent at its servicing agent to which a credit entry will be made as a result of the payment transaction.

Impacted by: C21 "IdentificationOrProxyPresenceRule", C20 "IdentificationAndProxyGuideline"

---

<!-- Page 57 -->

CreditorAgentAccount <CdtrAgtAcct> contains the following elements (see "CashAccount40" on page 309 for details)



| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Identification <Ids> | [0..1] | ± | | 310 |
| | Type <Tp> | [0..1] | ± | | 310 |
| | Currency <Ccy> | [0..1] | CodeSet | C2 | 310 |
| | Name <Nm> | [0..1] | Text | | 311 |
| | Proxy <Prxy> | [0..1] | ± | | 311 |

## Constraints

- **IdentificationAndProxyGuideline**

If the account identification is not defined through a conventional identification such as an email address or a mobile number, then the proxy element should be used for the identification of the account.

- **IdentificationOrProxyPresenceRule**

Identification must be present or Proxy must be present. Both may be present.

```
Following Must be True
/Identification Must be present
Or
/Proxy Must be present
```

### 2.4.2.19.17 Creditor <Cdt r>

*Presence: [0..1]*

*Definition: Party to which an amount of money is due.*

---

<!-- Page 58 -->

Creditor <Cdtr> contains the following elements (see "PartyIdentification22" on page 336 for details)



<table>
  <tr>
    <th>Or</th>
    <th>MessageElement<XML Tag></th>
    <th>Mult.</th>
    <th>Type</th>
    <th>Constr. No.</th>
    <th>Page</th>
  </tr>
  <tr>
    <td></td>
    <td>Name <Nm></td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>337</td>
  </tr>
  <tr>
    <td></td>
    <td>PostalAddress <PstlAdr></td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>338</td>
  </tr>
  <tr>
    <td></td>
    <td>Identification <Id></td>
    <td>[0..1]</td>
    <td></td>
    <td></td>
    <td>338</td>
  </tr>
  <tr>
    <td>Or</td>
    <td>OrganisationIdentification <OrgId></td>
    <td>[1..1]</td>
    <td></td>
    <td></td>
    <td>339</td>
  </tr>
  <tr>
    <td></td>
    <td>AnyBIC <AnyBIC></td>
    <td>[0..1]</td>
    <td>IdentifierSet</td>
    <td>C5</td>
    <td>340</td>
  </tr>
  <tr>
    <td></td>
    <td>LEI <LEI></td>
    <td>[0..1]</td>
    <td>IdentifierSet</td>
    <td></td>
    <td>340</td>
  </tr>
  <tr>
    <td></td>
    <td>Other <Othr></td>
    <td>[0..*]</td>
    <td></td>
    <td></td>
    <td>340</td>
  </tr>
  <tr>
    <td></td>
    <td>Identification <Id></td>
    <td>[1..1]</td>
    <td>Text</td>
    <td></td>
    <td>341</td>
  </tr>
  <tr>
    <td></td>
    <td>SchemeName <SchrmNm></td>
    <td>[0..1]</td>
    <td></td>
    <td></td>
    <td>341</td>
  </tr>
  <tr>
    <td>Or</td>
    <td>Code <Cd></td>
    <td>[1..1]</td>
    <td>CodeSet</td>
    <td></td>
    <td>341</td>
  </tr>
  <tr>
    <td>Or</td>
    <td>Proprietary <Prtry></td>
    <td>[1..1]</td>
    <td>Text</td>
    <td></td>
    <td>341</td>
  </tr>
  <tr>
    <td></td>
    <td>Issuer <Issr></td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>341</td>
  </tr>
  <tr>
    <td>Or</td>
    <td>PrivateIdentification <PrvtId></td>
    <td>[1..1]</td>
    <td></td>
    <td></td>
    <td>341</td>
  </tr>
  <tr>
    <td></td>
    <td>DateAndPlaceOfBirth <DtAndPlcOfBirth></td>
    <td>[0..1]</td>
    <td></td>
    <td></td>
    <td>342</td>
  </tr>
  <tr>
    <td></td>
    <td>BirthDate <BirthDt></td>
    <td>[1..1]</td>
    <td>Date</td>
    <td></td>
    <td>342</td>
  </tr>
  <tr>
    <td></td>
    <td>ProvinceOfBirth <PrvcOfBirth></td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>342</td>
  </tr>
  <tr>
    <td></td>
    <td>CityOfBirth <CityOfBirth></td>
    <td>[1..1]</td>
    <td>Text</td>
    <td></td>
    <td>343</td>
  </tr>
  <tr>
    <td></td>
    <td>CountryOfBirth <CtryOfBirth></td>
    <td>[1..1]</td>
    <td>CodeSet</td>
    <td>C7</td>
    <td>343</td>
  </tr>
  <tr>
    <td></td>
    <td>Other <Othr></td>
    <td>[0..*]</td>
    <td></td>
    <td></td>
    <td>343</td>
  </tr>
  <tr>
    <td></td>
    <td>Identification <Id></td>
    <td>[1..1]</td>
    <td>Text</td>
    <td></td>
    <td>343</td>
  </tr>
  <tr>
    <td></td>
    <td>SchemeName <SchrmNm></td>
    <td>[0..1]</td>
    <td></td>
    <td></td>
    <td>343</td>
  </tr>
  <tr>
    <td>Or</td>
    <td>Code <Cd></td>
    <td>[1..1]</td>
    <td>CodeSet</td>
    <td></td>
    <td>344</td>
  </tr>
  <tr>
    <td>Or</td>
    <td>Proprietary <Prtry></td>
    <td>[1..1]</td>
    <td>Text</td>
    <td></td>
    <td>344</td>
  </tr>
  <tr>
    <td></td>
    <td>Issuer <Issr></td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>344</td>
  </tr>
  <tr>
    <td></td>
    <td>CountryOfResidence <CtryOfRes></td>
    <td>[0..1]</td>
    <td>CodeSet</td>
    <td>C7</td>
    <td>344</td>
  </tr>
  <tr>
    <td></td>
    <td>ContactDetails <CtctDtls></td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>344</td>
  </tr>
</table>

## 2.4.2.19.18 CreditorAccount <CdtrAcct>

Presence: [0..1]

Definition: Unambiguous identification of the account of the creditor to which a credit entry will be posted as a result of the payment transaction.

Impacted by: C21 "IdentificationOrProxyPresenceRule", C20 "IdentificationAndProxyGuideline"

---

<!-- Page 59 -->

CreditorAccount <CdtrAcct> contains the following elements (see "CashAccount40" on page 309 for details)



<table>
  <tr>
    <th>Or</th>
    <th>MessageElement&lt;XML Tag&gt;</th>
    <th>Mult.</th>
    <th>Type</th>
    <th>Constr. No.</th>
    <th>Page</th>
  </tr>
  <tr>
    <td></td>
    <td>Identification &lt;Ids&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>310</td>
  </tr>
  <tr>
    <td></td>
    <td>Type &lt;Tp&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>310</td>
  </tr>
  <tr>
    <td></td>
    <td>Currency &lt;Ccy&gt;</td>
    <td>[0..1]</td>
    <td>CodeSet</td>
    <td>C2</td>
    <td>310</td>
  </tr>
  <tr>
    <td></td>
    <td>Name &lt;Nm&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>311</td>
  </tr>
  <tr>
    <td></td>
    <td>Proxy &lt;Prxy&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>311</td>
  </tr>
</table>

## Constraints

- **IdentificationAndProxyGuideline**

  If the account identification is not defined through a conventional identification such as an email address or a mobile number, then the proxy element should be used for the identification of the account.

- **IdentificationOrProxyPresenceRule**

  Identification must be present or Proxy must be present. Both may be present.

  ```
  Following Must be True
  /Identification Must be present
  Or      /Proxy Must be present
  ```

## 2.4.2.19.19 UltimateCreditor <UltmtCdr>

*Presence:* [0..1]

*Definition:* Ultimate party to which an amount of money is due.

---

<!-- Page 60 -->

UltimateCreditor <UltmtCdtor> contains the following elements (see "PartyIdentification272" on page 336 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Name <Nm> | [0..1] | Text | | 337 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 338 |
| | Identification <Id> | [0..1] | | | 338 |
| (Or | OrganisationIdentification <OrgId> | [1..1] | | | 339 |
| | AnyBIC <AnyBIC> | [0..1] | IdentifierSet | C5 | 340 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 340 |
| | Other <Othr> | [0..*] | | | 340 |
| | Identification <Id> | [1..1] | Text | | 341 |
| | SchemeName <SchmeNm> | [0..1] | | | 341 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 341 |
| Or) | Proprietary <Prtry> | [1..1] | Text | | 341 |
| | Issuer <Issr> | [0..1] | Text | | 341 |
| (Or) | PrivateIdentification <PrvtId> | [1..1] | | | 341 |
| | DateAndPlaceOfBirth <DtAndPlcOfBirth> | [0..1] | | | 342 |
| | BirthDate <BirthDt> | [1..1] | Date | | 342 |
| | ProvinceOfBirth <PrvcOfBirth> | [0..1] | Text | | 342 |
| | CityOfBirth <CityOfBirth> | [1..1] | Text | | 343 |
| | CountryOfBirth <CtryOfBirth> | [1..1] | CodeSet | C7 | 343 |
| | Other <Othr> | [0..*] | | | 343 |
| | Identification <Id> | [1..1] | Text | | 343 |
| | SchemeName <SchmeNm> | [0..1] | | | 343 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 344 |
| Or) | Proprietary <Prtry> | [1..1] | Text | | 344 |
| | Issuer <Issr> | [0..1] | Text | | 344 |
| | CountryOfResidence <CtryOfRes> | [0..1] | CodeSet | C7 | 344 |
| | ContactDetails <CtctDtls> | [0..1] | ± | | 344 |

**2.4.2.19.20 InstructionForCreditorAgent <InstrForCdtrAgt>**

*Presence:* [0..*]

*Definition:* Further information related to the processing of the payment instruction, provided by the initiating party, and intended for the creditor agent.

---

<!-- Page 61 -->

InstructionForCdrAgent <InstrForCdrAg> contains the following elements (see "InstructionForCdrAgent3" on page 345 for details)



<table>
  <tr>
    <th>Or</th>
    <th>MessageElement&lt;XML Tag&gt;</th>
    <th>Mult.</th>
    <th>Type</th>
    <th>Constr. No.</th>
    <th>Page</th>
  </tr>
  <tr>
    <td></td>
    <td>Code &lt;Cdr&gt;</td>
    <td>[0..1]</td>
    <td>CodeSet</td>
    <td></td>
    <td>345</td>
  </tr>
  <tr>
    <td></td>
    <td>InstructionInformation &lt;InstrInf&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>346</td>
  </tr>
</table>

## 2.4.2.19.21 InstructionForDbtrAgent <InstrForDbtrAg>

*Presence:* [0..1]

*Definition:* Further information related to the processing of the payment instruction, that may need to be acted upon by the debtor agent, depending on agreement between debtor and the debtor agent.

InstructionForDbtrAgent <InstrForDbtrAg> contains the following InstructionForDbtrAgent1 elements



<table>
  <tr>
    <th>Or</th>
    <th>MessageElement&lt;XML Tag&gt;</th>
    <th>Mult.</th>
    <th>Type</th>
    <th>Constr. No.</th>
    <th>Page</th>
  </tr>
  <tr>
    <td></td>
    <td>Code &lt;Cdr&gt;</td>
    <td>[0..1]</td>
    <td>CodeSet</td>
    <td></td>
    <td>61</td>
  </tr>
  <tr>
    <td></td>
    <td>InstructionInformation &lt;InstrInf&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>61</td>
  </tr>
</table>

### 2.4.2.19.21.1 Code <Cdr>

*Presence:* [0..1]

*Definition:* Coded information related to the processing of the payment instruction, provided by the initiating party, and intended for the creditor's agent.

*Datatype:* "ExternalDebtorAgentInstruction1Code" on page 415

### 2.4.2.19.21.2 InstructionInformation <InstrInf>

*Presence:* [0..1]

*Definition:* Further information complementing the coded instruction or instruction to the creditor's agent that is bilaterally agreed or specific to a user community.

*Datatype:* "Max140Text" on page 429

## 2.4.2.19.22 Purpose <Purp>

*Presence:* [0..1]

*Definition:* Underlying reason for the payment transaction.

Usage: Purpose is used by the end-customers, that is initiating party, (ultimate) debtor, (ultimate) creditor to provide information concerning the nature of the payment. Purpose is a content element, which is not used for processing by any of the agents involved in the payment chain.

Purpose <Purp> contains one of the following elements (see "Purpose2Choice" on page 334 for details)



<table>
  <tr>
    <th>Or</th>
    <th>MessageElement&lt;XML Tag&gt;</th>
    <th>Mult.</th>
    <th>Type</th>
    <th>Constr. No.</th>
    <th>Page</th>
  </tr>
  <tr>
    <td>Or</td>
    <td>Code &lt;Cdr&gt;</td>
    <td>[1..1]</td>
    <td>CodeSet</td>
    <td></td>
    <td>335</td>
  </tr>
  <tr>
    <td>Or</td>
    <td>Proprietary &lt;Prt&gt;</td>
    <td>[1..1]</td>
    <td>Text</td>
    <td></td>
    <td>335</td>
  </tr>
</table>

---

<!-- Page 62 -->

**2.4.2.19.23 RegulatoryReporting <RgltryRptg>**

*Presence:* [0..10]

*Definition:* Information needed due to regulatory and statutory requirements.

**RegulatoryReporting <RgltryRptg>** contains the following elements (see "RegulatoryReporting3" on page 361 for details)



<table>
  <thead>
    <tr>
      <th>Or</th>
      <th>MessageElement&lt;XML Tag&gt;</th>
      <th>Mult.</th>
      <th>Type</th>
      <th>Constr. No.</th>
      <th>Page</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td>DebitCreditReportingIndicator &lt;DbtCdtRptgInd&gt;</td>
      <td>[0..1]</td>
      <td>CodeSet</td>
      <td></td>
      <td>361</td>
    </tr>
    <tr>
      <td></td>
      <td>Authority &lt;Authrty&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>361</td>
    </tr>
    <tr>
      <td></td>
      <td>Name &lt;Nm&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>362</td>
    </tr>
    <tr>
      <td></td>
      <td>Country &lt;Ctry&gt;</td>
      <td>[0..1]</td>
      <td>CodeSet</td>
      <td>C7</td>
      <td>362</td>
    </tr>
    <tr>
      <td></td>
      <td>Details &lt;Dtls&gt;</td>
      <td>[0..*]</td>
      <td></td>
      <td></td>
      <td>362</td>
    </tr>
    <tr>
      <td></td>
      <td>Type &lt;Tp&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>362</td>
    </tr>
    <tr>
      <td></td>
      <td>Date &lt;Dt&gt;</td>
      <td>[0..1]</td>
      <td>Date</td>
      <td></td>
      <td>363</td>
    </tr>
    <tr>
      <td></td>
      <td>Country &lt;Ctry&gt;</td>
      <td>[0..1]</td>
      <td>CodeSet</td>
      <td>C7</td>
      <td>363</td>
    </tr>
    <tr>
      <td></td>
      <td>Code &lt;Cd&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>363</td>
    </tr>
    <tr>
      <td></td>
      <td>Amount &lt;Amt&gt;</td>
      <td>[0..1]</td>
      <td>Amount</td>
      <td>C2, C8</td>
      <td>363</td>
    </tr>
    <tr>
      <td></td>
      <td>Information &lt;Inf&gt;</td>
      <td>[0..*]</td>
      <td>Text</td>
      <td></td>
      <td>363</td>
    </tr>
  </tbody>
</table>

**2.4.2.19.24 Tax <Tax>**

*Presence:* [0..1]

*Definition:* Provides details on the tax.

---

<!-- Page 63 -->

Tax `<Tax>` contains the following `TaxData1` elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Creditor `<CdtIcr>` | [0..1] | ± | | 64 |
| | Debtor `<Dbtr>` | [0..1] | ± | | 64 |
| | UltimateDebtor `<UltmtDbtr>` | [0..1] | ± | | 64 |
| | AdministrationZone `<AdminstrZone>` | [0..1] | Text | | 65 |
| | ReferenceNumber `<RefNb>` | [0..1] | Text | | 65 |
| | Method `<Mtd>` | [0..1] | Text | | 65 |
| | TotalTaxableBaseAmount `<TtlTaxblBaseAmt>` | [0..1] | Amount | C1, C18 | 65 |
| | TotalTaxAmount `<TtlTaxAmt>` | [0..1] | Amount | C1, C18 | 66 |
| | Date `<Dt>` | [0..1] | Date | | 66 |
| | SequenceNumber `<SeqNb>` | [0..1] | Quantity | | 66 |
| | Record `<Rcrd>` | [0.*] | | | 66 |
| | Type `<Tp>` | [0..1] | Text | | 67 |
| | Category `<Ctgy>` | [0..1] | Text | | 67 |
| | CategoryDetails `<CtgyDtls>` | [0..1] | Text | | 67 |
| | DebtorStatus `<DbtrSts>` | [0..1] | Text | | 68 |
| | CertificateIdentification `<CertId>` | [0..1] | Text | | 68 |
| | FormsCode `<FrmsCde>` | [0..1] | Text | | 68 |
| | Period `<Prd>` | [0..1] | | | 68 |
| | Year `<Yr>` | [0..1] | Year | | 68 |
| | Type `<Tp>` | [0..1] | CodeSet | | 68 |
| | FromToDate `<FrToDt>` | [0..1] | ± | | 69 |
| | TaxAmount `<TaxAmt>` | [0..1] | | | 70 |
| | Rate `<Rate>` | [0..1] | Rate | | 70 |
| | TaxableBaseAmount `<TaxblBaseAmt>` | [0..1] | Amount | C1, C18 | 70 |
| | TotalAmount `<TtlAmt>` | [0..1] | Amount | C1, C18 | 70 |
| | Details `<Dtls>` | [0.*] | | | 71 |
| | Period `<Prd>` | [0..1] | | | 71 |
| | Year `<Yr>` | [0..1] | Year | | 71 |
| | Type `<Tp>` | [0..1] | CodeSet | | 72 |
| | FromToDate `<FrToDt>` | [0..1] | ± | | 72 |
| | Amount `<Amt>` | [1..1] | Amount | C1, C18 | 73 |

---

<!-- Page 64 -->

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | AdditionalInformation <AddtlInf> | [0..1] | Text | | 73 |

## 2.4.2.19.24.1 Creditor <Cdrtr>

*Presence:* [0..1]

*Definition:* Party on the credit side of the transaction to which the tax applies.

**Creditor <Cdrtr>** contains the following elements (see “TaxParty1” on page 405 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | TaxIdentification <TaxId> | [0..1] | Text | | 405 |
| | RegistrationIdentification <RegnId> | [0..1] | Text | | 405 |
| | TaxType <TaxTp> | [0..1] | Text | | 406 |

## 2.4.2.19.24.2 Debtor <Dbtr>

*Presence:* [0..1]

*Definition:* Party on the debit side of the transaction to which the tax applies.

**Debtor <Dbtr>** contains the following elements (see “TaxParty2” on page 406 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | TaxIdentification <TaxId> | [0..1] | Text | | 406 |
| | RegistrationIdentification <RegnId> | [0..1] | Text | | 406 |
| | TaxType <TaxTp> | [0..1] | Text | | 406 |
| | Authorisation <AuthStr> | [0..1] | | | 406 |
| | Title <Title> | [0..1] | Text | | 407 |
| | Name <Nm> | [0..1] | Text | | 407 |

## 2.4.2.19.24.3 UltimateDebtor <UltmtDbtr>

*Presence:* [0..1]

*Definition:* Ultimate party that owes an amount of money to the (ultimate) creditor, in this case, to the taxing authority.

---

<!-- Page 65 -->

UltimateDebtor <UltmtdBtr> contains the following elements (see "TaxParty2" on page 406 for details)



<table>
  <tr>
    <th>Or</th>
    <th>MessageElement &lt;XML Tag&gt;</th>
    <th>Mult.</th>
    <th>Type</th>
    <th>Const. No.</th>
    <th>Page</th>
  </tr>
  <tr>
    <td></td>
    <td>TaxIdentification &lt;TaxId&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>406</td>
  </tr>
  <tr>
    <td></td>
    <td>RegistrationIdentification &lt;RegnId&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>406</td>
  </tr>
  <tr>
    <td></td>
    <td>TaxType &lt;TaxTp&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>406</td>
  </tr>
  <tr>
    <td></td>
    <td>Authorisation &lt;AuthStrn&gt;</td>
    <td>[0..1]</td>
    <td></td>
    <td></td>
    <td>406</td>
  </tr>
  <tr>
    <td></td>
    <td>Title &lt;Title&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>407</td>
  </tr>
  <tr>
    <td></td>
    <td>Name &lt;Nm&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>407</td>
  </tr>
</table>

## 2.4.2.19.24.4 AdministrationZone <AdmstnZone>

*Presence:* [0..1]

*Definition:* Territorial part of a country to which the tax payment is related.

*Datatype:* "Max35Text" on page 431

## 2.4.2.19.24.5 ReferenceNumber <RefNbr>

*Presence:* [0..1]

*Definition:* Tax reference information that is specific to a taxing agency.

*Datatype:* "Max140Text" on page 429

## 2.4.2.19.24.6 Method <Mtd>

*Presence:* [0..1]

*Definition:* Method used to indicate the underlying business or how the tax is paid.

*Datatype:* "Max35Text" on page 431

## 2.4.2.19.24.7 TotalTaxableBaseAmount <TtlTaxblBaseAmt>

*Presence:* [0..1]

*Definition:* Total amount of money on which the tax is based.

*Impacted by:* C1 "ActiveOrHistoricCurrency", C18 "CurrencyAmount"

*Datatype:* "ActiveOrHistoricCurrencyAndAmount" on page 407

### Constraints

- **ActiveOrHistoricCurrency**

The Currency Code must be registered, or have already been registered. Valid active or historic currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and may be or not be withdrawn on the day the message containing the Currency is exchanged.

- **CurrencyAmount**

The number of fractional digits (or minor unit of currency) must comply with ISO 4217.

---

<!-- Page 66 -->

Note: The decimal separator is a dot.

**2.4.2.19.24.8 TotalTaxAmount <TlTaxAm>**

*Presence:* [0..1]

*Definition:* Total amount of money as result of the calculation of the tax.

*Impacted by:* C1 "ActiveOrHistoricCurrency", C18 "CurrencyAmount"

*Datatype:* "ActiveOrHistoricCurrencyAndAmount" on page 407

**Constraints**

- **ActiveOrHistoricCurrency**

  The Currency Code must be registered, or have already been registered. Valid active or historic currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and may be or not be withdrawn on the day the message containing the Currency is exchanged.

- **CurrencyAmount**

  The number of fractional digits (or minor unit of currency) must comply with ISO 4217.

  Note: The decimal separator is a dot.

**2.4.2.19.24.9 Date <Dt>**

*Presence:* [0..1]

*Definition:* Date by which tax is due.

*Datatype:* "ISODate" on page 425

**2.4.2.19.24.10 SequenceNumber <SeqNb>**

*Presence:* [0..1]

*Definition:* Sequential number of the tax report.

*Datatype:* "Number" on page 427

**2.4.2.19.24.11 Record <Rcrd>**

*Presence:* [0..*]

*Definition:* Record of tax details.

---

<!-- Page 67 -->

Record `<Rcrd>` contains the following **TaxRecord3** elements



<table><tr><td>Or</td><td>MessageElement&lt;XML Tag&gt;</td><td>Mult.</td><td>Type</td><td>Constr. No.</td><td>Page</td></tr><tr><td></td><td>Type &lt;Tp&gt;</td><td>[0..1]</td><td>Text</td><td></td><td>67</td></tr><tr><td></td><td>Category &lt;Ctgy&gt;</td><td>[0..1]</td><td>Text</td><td></td><td>67</td></tr><tr><td></td><td>CategoryDetails &lt;CtgyDtls&gt;</td><td>[0..1]</td><td>Text</td><td></td><td>67</td></tr><tr><td></td><td>DebtorStatus &lt;DbtrSts&gt;</td><td>[0..1]</td><td>Text</td><td></td><td>68</td></tr><tr><td></td><td>CertificateIdentification &lt;CertId&gt;</td><td>[0..1]</td><td>Text</td><td></td><td>68</td></tr><tr><td></td><td>FormsCode &lt;FrmsCd&gt;</td><td>[0..1]</td><td>Text</td><td></td><td>68</td></tr><tr><td></td><td>Period &lt;Prd&gt;</td><td>[0..1]</td><td></td><td></td><td>68</td></tr><tr><td></td><td>Year &lt;Yr&gt;</td><td>[0..1]</td><td>Year</td><td></td><td>68</td></tr><tr><td></td><td>Type &lt;Tp&gt;</td><td>[0..1]</td><td>CodeSet</td><td></td><td>68</td></tr><tr><td></td><td>FromToDate &lt;FrToDt&gt;</td><td>[0..1]</td><td>±</td><td></td><td>69</td></tr><tr><td></td><td>TaxAmount &lt;TaxAmt&gt;</td><td>[0..1]</td><td></td><td></td><td>70</td></tr><tr><td></td><td>Rate &lt;Rate&gt;</td><td>[0..1]</td><td>Rate</td><td></td><td>70</td></tr><tr><td></td><td>TaxableBaseAmount &lt;TaxblBaseAmt&gt;</td><td>[0..1]</td><td>Amount</td><td>C1, C18</td><td>70</td></tr><tr><td></td><td>TotalAmount &lt;TtlAmt&gt;</td><td>[0..1]</td><td>Amount</td><td>C1, C18</td><td>70</td></tr><tr><td></td><td>Details &lt;Dtls&gt;</td><td>[0..*]</td><td></td><td></td><td>71</td></tr><tr><td></td><td>Period &lt;Prd&gt;</td><td>[0..1]</td><td></td><td></td><td>71</td></tr><tr><td></td><td>Year &lt;Yr&gt;</td><td>[0..1]</td><td>Year</td><td></td><td>71</td></tr><tr><td></td><td>Type &lt;Tp&gt;</td><td>[0..1]</td><td>CodeSet</td><td></td><td>72</td></tr><tr><td></td><td>FromToDate &lt;FrToDt&gt;</td><td>[0..1]</td><td>±</td><td></td><td>72</td></tr><tr><td></td><td>Amount &lt;Amt&gt;</td><td>[1..1]</td><td>Amount</td><td>C1, C18</td><td>73</td></tr><tr><td></td><td>AdditionalInformation &lt;AddtlInf&gt;</td><td>[0..1]</td><td>Text</td><td></td><td>73</td></tr></table>

**2.4.2.19.24.11.1 Type &lt;Tp&gt;**

*Presence:* [0..1]

*Definition:* High level code to identify the type of tax details.

*Datatype:* "Max35Text" on page 431

**2.4.2.19.24.11.2 Category &lt;Ctgy&gt;**

*Presence:* [0..1]

*Definition:* Specifies the tax code as published by the tax authority.

*Datatype:* "Max35Text" on page 431

**2.4.2.19.24.11.3 CategoryDetails &lt;CtgyDtls&gt;**

*Presence:* [0..1]

---

<!-- Page 68 -->

Definition: Provides further details of the category tax code.
*Datatype:* "Max35Text" on page 431

**2.4.2.19.24.11.4 DebtorStatus <DbtrSts>**
*Presence:* [0..1]
*Definition:* Code provided by local authority to identify the status of the party that has drawn up the settlement document.
*Datatype:* "Max35Text" on page 431

**2.4.2.19.24.11.5 CertificateIdentification <CertId>**
*Presence:* [0..1]
*Definition:* Identification number of the tax report as assigned by the taxing authority.
*Datatype:* "Max35Text" on page 431

**2.4.2.19.24.11.6 FormsCode <FrmsCd>**
*Presence:* [0..1]
*Definition:* Identifies, in a coded form, on which template the tax report is to be provided.
*Datatype:* "Max35Text" on page 431

**2.4.2.19.24.11.7 Period <Prd>**
*Presence:* [0..1]
*Definition:* Set of elements used to provide details on the period of time related to the tax payment.
**Period <Prd>** contains the following **TaxPeriod3** elements

| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Year <Yr> | [0..1] | Year | | 68 |
| | Type <Tp> | [0..1] | CodeSet | | 68 |
| | FromToDate <FrToDt> | [0..1] | ± | | 69 |

**2.4.2.19.24.11.7.1 Year <Yr>**
*Presence:* [0..1]
*Definition:* Year related to the tax payment.
*Datatype:* "ISOYear" on page 432

**2.4.2.19.24.11.7.2 Type <Tp>**
*Presence:* [0..1]
*Definition:* Identification of the period related to the tax payment.
*Datatype:* "TaxRecordPeriod1Code" on page 424

| CodeName | Name | Definition |
|---|---|---|
| MM01 | FirstMonth | Tax is related to the second month of the period. |

---

<!-- Page 69 -->

| CodeName | Name | Definition |
|---|---|---|
| MM02 | SecondMonth | Tax is related to the first month of the period. |
| MM03 | ThirdMonth | Tax is related to the third month of the period. |
| MM04 | FourthMonth | Tax is related to the fourth month of the period. |
| MM05 | FifthMonth | Tax is related to the fifth month of the period. |
| MM06 | SixthMonth | Tax is related to the sixth month of the period. |
| MM07 | SeventhMonth | Tax is related to the seventh month of the period. |
| MM08 | EighthMonth | Tax is related to the eighth month of the period. |
| MM09 | NinthMonth | Tax is related to the ninth month of the period. |
| MM10 | TenthMonth | Tax is related to the tenth month of the period. |
| MM11 | EleventhMonth | Tax is related to the eleventh month of the period. |
| MM12 | TwelfthMonth | Tax is related to the twelfth month of the period. |
| QTR1 | FirstQuarter | Tax is related to the first quarter of the period. |
| QTR2 | SecondQuarter | Tax is related to the second quarter of the period. |
| QTR3 | ThirdQuarter | Tax is related to the third quarter of the period. |
| QTR4 | FourthQuarter | Tax is related to the forth quarter of the period. |
| HLF1 | FirstHalf | Tax is related to the first half of the period. |
| HLF2 | SecondHalf | Tax is related to the second half of the period. |

**2.4.2.19.24.11.7.3 FromToDate <FrToDt>**

*Presence:* [0..1]

*Definition:* Range of time between a start date and an end date for which the tax report is provided.

FromToDate <FrToDt> contains the following elements (see "DatePeriod2" on page 316 for details)

| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | FromDate <FrDt> | [1..1] | Date |  | 316 |
| | ToDate <ToDt> | [1..1] | Date |  | 316 |

---

<!-- Page 70 -->

2.4.2.19.24.11.8 TaxAmount <TaxAmt>
*Presence: [0..1]*
*Definition: Set of elements used to provide information on the amount of the tax record.*

TaxAmount <TaxAmt> contains the following TaxAmount3 elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
| :--- | :--- | :--- | :--- | :--- | :--- |
| | Rate <Rate> | [0..1] | Rate | | 70 |
| | TaxableBaseAmount <TaxblBaseAmt> | [0..1] | Amount | C1, C18 | 70 |
| | TotalAmount <TtlAmt> | [0..1] | Amount | C1, C18 | 70 |
| | Details <Dtls> | [0..*] | | | 71 |
| | Period <Prd> | [0..1] | | | 71 |
| | Year <Yr> | [0..1] | Year | | 71 |
| | Type <Tp> | [0..1] | CodeSet | | 72 |
| | FromToDate <FrToDt> | [0..1] | ± | | 72 |
| | Amount <Amt> | [1..1] | Amount | C1, C18 | 73 |

2.4.2.19.24.11.8.1 Rate <Rate>
*Presence: [0..1]*
*Definition: Rate used to calculate the tax.*
*Datatype: "PercentageRate" on page 428*

2.4.2.19.24.11.8.2 TaxableBaseAmount <TaxblBaseAmt>
*Presence: [0..1]*
*Definition: Amount of money on which the tax is based.*
*Impacted by: C1 "ActiveOrHistoricCurrency", C18 "CurrencyAmount"*
*Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 407*

Constraints

*   **ActiveOrHistoricCurrency**

    The Currency Code must be registered, or have already been registered. Valid active or historic currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and may be or not be withdrawn on the day the message containing the Currency is exchanged.

*   **CurrencyAmount**

    The number of fractional digits (or minor unit of currency) must comply with ISO 4217.

    Note: The decimal separator is a dot.

2.4.2.19.24.11.8.3 TotalAmount <TtlAmt>
*Presence: [0..1]*

---

<!-- Page 71 -->

*Definition:* Total amount that is the result of the calculation of the tax for the record.

*Impacted by:* C1 "ActiveOrHistoricCurrency", C18 "CurrencyAmount"

*Datatype:* "ActiveOrHistoricCurrencyAndAmount" on page 407

## Constraints

- **ActiveOrHistoricCurrency**

The Currency Code must be registered, or have already been registered. Valid active or historic currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and may be or not be withdrawn on the day the message containing the Currency is exchanged.

- **CurrencyAmount**

The number of fractional digits (or minor unit of currency) must comply with ISO 4217.

Note: The decimal separator is a dot.

## 2.4.2.19.24.11.8.4 Details <Dtls>

*Presence:* [0..*]

*Definition:* Set of elements used to provide details on the tax period and amount.

**Details <Dtls>** contains the following **TaxRecordDetails3** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **Period** <Prd> | [0..1] | | | 71 |
| | **Year** <Yr> | [0..1] | Year | | 71 |
| | **Type** <Tp> | [0..1] | CodeSet | | 72 |
| | **FromToDate** <FrToDt> | [0..1] | ± | | 72 |
| | **Amount** <Amt> | [1..1] | Amount | C1, C18 | 73 |

## 2.4.2.19.24.11.8.4.1 Period <Prd>

*Presence:* [0..1]

*Definition:* Set of elements used to provide details on the period of time related to the tax payment.

**Period <Prd>** contains the following **TaxPeriod3** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **Year** <Yr> | [0..1] | Year | | 71 |
| | **Type** <Tp> | [0..1] | CodeSet | | 72 |
| | **FromToDate** <FrToDt> | [0..1] | ± | | 72 |

## 2.4.2.19.24.11.8.4.1.1 Year <Yr>

*Presence:* [0..1]

*Definition:* Year related to the tax payment.

---

<!-- Page 72 -->

*Datatype:* *"ISOYear"* *on page 432*

**2.4.2.19.24.11.8.4.1.2 Type <Tp>**

*Presence:* *[0..1]*

*Definition:* *Identification of the period related to the tax payment.*

*Datatype:* *"TaxRecordPeriod1Code"* *on page 424*



| CodeName | Name | Definition |
| :--- | :--- | :--- |
| MM01 | FirstMonth | Tax is related to the second month of the period. |
| MM02 | SecondMonth | Tax is related to the first month of the period. |
| MM03 | ThirdMonth | Tax is related to the third month of the period. |
| MM04 | FourthMonth | Tax is related to the fourth month of the period. |
| MM05 | FifthMonth | Tax is related to the fifth month of the period. |
| MM06 | SixthMonth | Tax is related to the sixth month of the period. |
| MM07 | SeventhMonth | Tax is related to the seventh month of the period. |
| MM08 | EighthMonth | Tax is related to the eighth month of the period. |
| MM09 | NinthMonth | Tax is related to the ninth month of the period. |
| MM10 | TenthMonth | Tax is related to the tenth month of the period. |
| MM11 | EleventhMonth | Tax is related to the eleventh month of the period. |
| MM12 | TwelfthMonth | Tax is related to the twelfth month of the period. |
| QTR1 | FirstQuarter | Tax is related to the first quarter of the period. |
| QTR2 | SecondQuarter | Tax is related to the second quarter of the period. |
| QTR3 | ThirdQuarter | Tax is related to the third quarter of the period. |
| QTR4 | FourthQuarter | Tax is related to the forth quarter of the period. |
| HLF1 | FirstHalf | Tax is related to the first half of the period. |
| HLF2 | SecondHalf | Tax is related to the second half of the period. |

**2.4.2.19.24.11.8.4.1.3 FromToDate <FrToDt>**

*Presence:* *[0..1]*

---

<!-- Page 73 -->

*Definition:* Range of time between a start date and an end date for which the tax report is provided.

**FromToDate \<FrToDt\>** contains the following elements (see "DatePeriod2" on page 316 for details)



<table><tr><td>Or</td><td>MessageElement&lt;XML Tag&gt;</td><td>Mult.</td><td>Type</td><td>Constr. No.</td><td>Page</td></tr><tr><td></td><td>FromDate &lt;FrDt&gt;</td><td>[1..1]</td><td>Date</td><td></td><td>316</td></tr><tr><td></td><td>ToDate &lt;ToDt&gt;</td><td>[1..1]</td><td>Date</td><td></td><td>316</td></tr></table>

**2.4.2.19.24.11.8.4.2 Amount \<Amt\>**

*Presence:* [1..1]

*Definition:* Underlying tax amount related to the specified period.

*Impacted by:* C1 "ActiveOrHistoricCurrency", C18 "CurrencyAmount"

*Datatype:* "ActiveOrHistoricCurrencyAndAmount" on page 407

**Constraints**

- **ActiveOrHistoricCurrency**

The Currency Code must be registered, or have already been registered. Valid active or historic currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and may be or not be withdrawn on the day the message containing the Currency is exchanged.

- **CurrencyAmount**

The number of fractional digits (or minor unit of currency) must comply with ISO 4217.

Note: The decimal separator is a dot.

**2.4.2.19.24.11.9 AdditionalInformation \<AddtlInf\>**

*Presence:* [0..1]

*Definition:* Further details of the tax record.

*Datatype:* "Max140Text" on page 429

**2.4.2.19.25 RelatedRemittanceInformation \<RltdRmtInf\>**

*Presence:* [0..10]

*Definition:* Provides information related to the handling of the remittance information by any of the agents in the transaction processing chain.

---

<!-- Page 74 -->

RelatedRemittanceInformation <RltdRmInf> contains the following RemittanceLocation8 elements

| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | RemittanceIdentification <RmtId> | [0..1] | Text | | 74 |
| | RemittanceLocationDetails <RmtLctnDtls> | [0..*] | | | 74 |
| | Method <Mtd> | [1..1] | CodeSet | | 74 |
| | ElectronicAddress <ElctrncAdr> | [0..1] | Text | | 75 |
| | PostalAddress <PstlAdr> | [0..1] | | | 75 |
| | Name <Nm> | [1..1] | Text | | 75 |
| | Address <Adr> | [1..1] | ± | | 75 |

### 2.4.2.19.25.1 RemittanceIdentification <RmtId>

Presence: [0..1]

*Definition:* Unique identification, as assigned by the initiating party, to unambiguously identify the remittance information sent separately from the payment instruction, such as a remittance advice.

Datatype: "Max35Text" on page 431

### 2.4.2.19.25.2 RemittanceLocationDetails <RmtLctnDtls>

Presence: [0..*]

*Definition:* Set of elements used to provide information on the location and/or delivery of the remittance information.

RemittanceLocationDetails <RmtLctnDtls> contains the following RemittanceLocationData2 elements

| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Method <Mtd> | [1..1] | CodeSet | | 74 |
| | ElectronicAddress <ElctrncAdr> | [0..1] | Text | | 75 |
| | PostalAddress <PstlAdr> | [0..1] | | | 75 |
| | Name <Nm> | [1..1] | Text | | 75 |
| | Address <Adr> | [1..1] | ± | | 75 |

### 2.4.2.19.25.2.1 Method <Mtd>

Presence: [1..1]

*Definition:* Method used to deliver the remittance advice information.

Datatype: "RemittanceLocationMethod2Code" on page 422

| CodeName | Name | Definition |
|---|---|---|
| FAXI | Fax | Remittance advice information must be faxed. |

---

<!-- Page 75 -->

| CodeName | Name | Definition |
|---|---|---|
| EDIC | ElectronicDataInterchange | Remittance advice information must be sent through Electronic Data Interchange (EDI). |
| URID | UniformResourceIdentifier | Remittance advice information needs to be sent to a Uniform Resource Identifier (URI). URI is a compact string of characters that uniquely identify an abstract or physical resource. URI's are the super-set of identifiers, such as URLs, email addresses, ftp sites, etc, and as such, provide the syntax for all of the identification schemes. |
| EMAL | EMail | Remittance advice information must be sent through e-mail. |
| POST | Post | Remittance advice information must be sent through postal services. |
| SMSM | SMS | Remittance advice information must be sent through by phone as a short message service (SMS). |

## 2.4.2.19.25.2.2 ElectronicAddress <ElectrncAdr>

*Presence:* [0..1]

*Definition:* Electronic address to which an agent is to send the remittance information.

*Datatype:* "Max2048Text" on page 430

## 2.4.2.19.25.2.3 PostalAddress <PstlAdr>

*Presence:* [0..1]

*Definition:* Postal address to which an agent is to send the remittance information.

**PostalAddress <PstlAdr>** contains the following **NameAndAddress18** elements

| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
|  | **Name** <Nm> | [1..1] | Text |  | 75 |
|  | **Address** <Adr> | [1..1] | ± |  | 75 |

### 2.4.2.19.25.2.3.1 Name <Nm>

*Presence:* [1..1]

*Definition:* Name by which a party is known and is usually used to identify that party.

*Datatype:* "Max140Text" on page 429

### 2.4.2.19.25.2.3.2 Address <Adr>

*Presence:* [1..1]

*Definition:* Postal address of a party.

---

<!-- Page 76 -->

Address <Adr> contains the following elements (see "PostalAddress27" on page 357 for details)



| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | AddressType <AdrTp> | [0..1] |  |  | 357 |
| (Or | Code <Cd> | [1..1] | CodeSet |  | 358 |
| Or) | Proprietary <Pry> | [1..1] | ± |  | 358 |
| | CareOf <CareOf> | [0..1] | Text |  | 358 |
| | Department <Dept> | [0..1] | Text |  | 358 |
| | SubDepartment <SubDept> | [0..1] | Text |  | 359 |
| | StreetName <StrtNm> | [0..1] | Text |  | 359 |
| | BuildingNumber <BldgNb> | [0..1] | Text |  | 359 |
| | BuildingName <BldgNm> | [0..1] | Text |  | 359 |
| | Floor <Flr> | [0..1] | Text |  | 359 |
| | UnitNumber <UnitNb> | [0..1] | Text |  | 359 |
| | PostBox <PstBx> | [0..1] | Text |  | 359 |
| | Room <Room> | [0..1] | Text |  | 359 |
| | PostCode <PstCd> | [0..1] | Text |  | 360 |
| | TownName <TwnNm> | [0..1] | Text |  | 360 |
| | TownLocationName <TwnLctnNm> | [0..1] | Text |  | 360 |
| | DistrictName <DstrctNm> | [0..1] | Text |  | 360 |
| | CountrySubDivision <CtrySubDvsn> | [0..1] | Text |  | 360 |
| | Country <Ctry> | [0..1] | CodeSet | C7 | 360 |
| | AddressLine <AdrLine> | [0..7] | Text |  | 360 |

## 2.4.2.19.26 RemittanceInformation <RmtInf>

Presence: [0..1]

Definition: Information supplied to enable the matching of an entry with the items that the transfer is intended to settle, such as commercial invoices in an accounts' receivable system.

RemittanceInformation <RmtInf> contains the following elements (see "RemittanceInformation22" on page 364 for details)



| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Unstructured <Ustrd> | [0..*] | Text |  | 364 |
| | Structured <Strd> | [0..*] | ± |  | 364 |

---

<!-- Page 77 -->

2.4.2.19.27 SupplementaryData <SplmtryData>

Presence: [0..*]

Definition: Additional information that cannot be captured in the structured elements and/or any other specific block.

Impacted by: C33 "SupplementaryDataRule"

**SupplementaryData <SplmtryData>** contains the following elements (see "SupplementaryData1" on page 334 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | PlaceAndName <PlcAndNm> | [0..1] | Text | | 334 |
| | Envelope <Envlp> | [1..1] | (External Schema) | | 334 |

**Constraints**

* **SupplementaryDataRule**

This component may not be used without the explicit approval of a SEG and submission to the RA of ISO 20022 compliant structure(s) to be used in the Envelope element.

## 2.4.3 SupplementaryData <SplmtryData>

Presence: [0..*]

Definition: Additional information that cannot be captured in the structured elements and/or any other specific block.

Impacted by: C33 "SupplementaryDataRule"

**SupplementaryData <SplmtryData>** contains the following elements (see "SupplementaryData1" on page 334 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | PlaceAndName <PlcAndNm> | [0..1] | Text | | 334 |
| | Envelope <Envlp> | [1..1] | (External Schema) | | 334 |

**Constraints**

* **SupplementaryDataRule**

This component may not be used without the explicit approval of a SEG and submission to the RA of ISO 20022 compliant structure(s) to be used in the Envelope element.

---

<!-- Page 78 -->

# 3 pain.002.001.14 CustomerPaymentStatusReportV14

## 3.1 MessageDefinition Functionality

Scope

The CustomerPaymentStatusReport message is sent by an instructed agent to the previous party in the payment chain. It is used to inform this party about the positive or negative status of an instruction (either single or file). It is also used to report on a pending instruction.

Usage

The CustomerPaymentStatusReport message is exchanged between an agent and a non-financial institution customer to provide status information on instructions previously sent. Its usage will always be governed by a bilateral agreement between the agent and the non-financial institution customer.

The CustomerPaymentStatusReport message can be used to provide information about the status (for example a rejection, an acceptance) of the initiation of a credit transfer, a direct debit, as well as on the initiation of other customer instructions.

The CustomerPaymentStatusReport message refers to the original instruction(s) by means of references only or by means of references and a set of elements from the original instruction.

The CustomerPaymentStatusReport message can be used in domestic and cross-border scenarios.

The CustomerPaymentStatusReport may also be sent to the receiver of the payment in a real time payment scenario, as both sides of the transactions must be informed of the status of the transaction (that is either the beneficiary is credited, or the transaction is rejected).

Outline

The CustomerPaymentStatusReportV14 MessageDefinition is composed of 4 MessageBuildingBlocks:

A. GroupHeader

Set of characteristics shared by all individual transactions included in the status report message.

B. OriginalGroupInformationAndStatus

Original group information concerning the group of transactions, to which the status report message refers to.

C. OriginalPaymentInformationAndStatus

Information concerning the original payment information, to which the status report message refers.

D. SupplementaryData

Additional information that cannot be captured in the structured elements and/or any other specific block.

---

<!-- Page 79 -->

## 3.2 Structure



<table>
  <thead>
    <tr>
      <th>Or</th>
      <th>MessageElement/BuildingBlock &lt;XML Tag&gt;</th>
      <th>Mult.</th>
      <th>Type</th>
      <th>Constr. No.</th>
      <th>Page</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td><i>Message root &lt;Document&gt; &lt;CstmrPmtStsRpt&gt;</i></td>
      <td>[1..1]</td>
      <td></td>
      <td>C10, C11, C12, C13, C31</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td><b>GroupHeader</b> &lt;GrpHdr&gt;</td>
      <td>[1..1]</td>
      <td></td>
      <td></td>
      <td>87</td>
    </tr>
    <tr>
      <td></td>
      <td><b>MessageIdentification</b> &lt;MsgId&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>88</td>
    </tr>
    <tr>
      <td></td>
      <td><b>CreationDateTime</b> &lt;CreDtTm&gt;</td>
      <td>[1..1]</td>
      <td>DateTime</td>
      <td></td>
      <td>88</td>
    </tr>
    <tr>
      <td></td>
      <td><b>InitiatingParty</b> &lt;InitgPty&gt;</td>
      <td>[0..1]</td>
      <td>±</td>
      <td></td>
      <td>88</td>
    </tr>
    <tr>
      <td></td>
      <td><b>ForwardingAgent</b> &lt;FwdgAgt&gt;</td>
      <td>[0..1]</td>
      <td>±</td>
      <td></td>
      <td>89</td>
    </tr>
    <tr>
      <td></td>
      <td><b>DebtorAgent</b> &lt;DbtrAgt&gt;</td>
      <td>[0..1]</td>
      <td>±</td>
      <td></td>
      <td>90</td>
    </tr>
    <tr>
      <td></td>
      <td><b>CreditorAgent</b> &lt;CdtrAgt&gt;</td>
      <td>[0..1]</td>
      <td>±</td>
      <td></td>
      <td>91</td>
    </tr>
    <tr>
      <td></td>
      <td><b>OriginalGroupInformationAndStatus</b> &lt;OrgnlGrpInfAndSts&gt;</td>
      <td>[1..1]</td>
      <td></td>
      <td>C29, C19</td>
      <td>91</td>
    </tr>
    <tr>
      <td></td>
      <td><b>OriginalMessageIdentification</b> &lt;OrgnlMsgId&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>92</td>
    </tr>
    <tr>
      <td></td>
      <td><b>OriginalMessageNameIdentification</b> &lt;OrgnlMsgNmId&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>92</td>
    </tr>
    <tr>
      <td></td>
      <td><b>OriginalCreationDateTime</b> &lt;OrgnlCreDtTm&gt;</td>
      <td>[0..1]</td>
      <td>DateTime</td>
      <td></td>
      <td>93</td>
    </tr>
    <tr>
      <td></td>
      <td><b>OriginalNumberOfTransactions</b> &lt;OrgnlNbOfTxs&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>93</td>
    </tr>
    <tr>
      <td></td>
      <td><b>OriginalControlSum</b> &lt;OrgnlCtrlSum&gt;</td>
      <td>[0..1]</td>
      <td>Quantity</td>
      <td></td>
      <td>93</td>
    </tr>
    <tr>
      <td></td>
      <td><b>GroupStatus</b> &lt;GrpSts&gt;</td>
      <td>[0..1]</td>
      <td>CodeSet</td>
      <td></td>
      <td>93</td>
    </tr>
    <tr>
      <td></td>
      <td><b>StatusReasonInformation</b> &lt;StsRsnInf&gt;</td>
      <td>[0..*]</td>
      <td></td>
      <td>C30</td>
      <td>93</td>
    </tr>
    <tr>
      <td></td>
      <td><b>Originator</b> &lt;Orgtr&gt;</td>
      <td>[0..1]</td>
      <td>±</td>
      <td></td>
      <td>94</td>
    </tr>
    <tr>
      <td></td>
      <td><b>Reason</b> &lt;Rsn&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>95</td>
    </tr>
    <tr>
      <td>{Or</td>
      <td><b>Code</b> &lt;Cd&gt;</td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td></td>
      <td>96</td>
    </tr>
    <tr>
      <td>Or)</td>
      <td><b>Proprietary</b> &lt;Prtry&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>96</td>
    </tr>
    <tr>
      <td></td>
      <td><b>AdditionalInformation</b> &lt;AddtlInf&gt;</td>
      <td>[0..*]</td>
      <td>Text</td>
      <td></td>
      <td>96</td>
    </tr>
    <tr>
      <td></td>
      <td><b>NumberOfTransactionsPerStatus</b> &lt;NbOfTxsPerSts&gt;</td>
      <td>[0..*]</td>
      <td>±</td>
      <td></td>
      <td>96</td>
    </tr>
    <tr>
      <td></td>
      <td><b>OriginalPaymentInformationAndStatus</b> &lt;OrgnlPmtInfAndSts&gt;</td>
      <td>[0..*]</td>
      <td></td>
      <td>C20, C21, C22, C23</td>
      <td>96</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td><b>OriginalPaymentInformationIdentification</b> &lt;OrgnlPmtInfId&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>102</td>
    </tr>
    <tr>
      <td></td>
      <td><b>OriginalNumberOfTransactions</b> &lt;OrgnlNbOfTxs&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>103</td>
    </tr>
    <tr>
      <td></td>
      <td><b>OriginalControlSum</b> &lt;OrgnlCtrlSum&gt;</td>
      <td>[0..1]</td>
      <td>Quantity</td>
      <td></td>
      <td>103</td>
    </tr>
  </tbody>
</table>

---

<!-- Page 80 -->

| Or | MessageElement/BuildingBlock <XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **PaymentInformationStatus** <PmtInfSts> | [0..1] | CodeSet | | 103 |
| | **StatusReasonInformation** <StsRsnInf> | [0..*] | | C30 | 103 |
| | **Originator** <Orgtr> | [0..1] | ± | | 104 |
| | **Reason** <Rsn> | [0..1] | | | 105 |
| (Or | **Code** <Cd> | [1..1] | CodeSet | | 105 |
| Or) | **Proprietary** <Prtry> | [1..1] | Text | | 105 |
| | **AdditionalInformation** <AddtlInf> | [0..*] | Text | | 105 |
| | **NumberOfTransactionsPerStatus** <NbOfTxsPerSts> | [0..*] | ± | | 105 |
| | **TransactionInformationAndStatus** <TxInfAndSts> | [0..*] | | | 105 |
| | **StatusIdentification** <StsId> | [0..1] | Text | | 109 |
| | **OriginalInstructionIdentification** <OrgnlInstrId> | [0..1] | Text | | 109 |
| | **OriginalEndToEndIdentification** <OrgnlEndToEndId> | [0..1] | Text | | 109 |
| | **OriginalUETR** <OrgnlUETR> | [0..1] | IdentifierSet | | 110 |
| | **TransactionStatus** <TxSts> | [0..1] | CodeSet | | 110 |
| | **StatusReasonInformation** <StsRsnInf> | [0..*] | | C30 | 110 |
| | **Originator** <Orgtr> | [0..1] | ± | | 110 |
| | **Reason** <Rsn> | [0..1] | | | 111 |
| (Or | **Code** <Cd> | [1..1] | CodeSet | | 112 |
| Or) | **Proprietary** <Prtry> | [1..1] | Text | | 112 |
| | **AdditionalInformation** <AddtlInf> | [0..*] | Text | | 112 |
| | **ChargesInformation** <ChrgsInf> | [0..*] | | | 112 |
| | **Amount** <Amt> | [1..1] | Amount | C2, C8 | 112 |
| | **Agent** <Agtr> | [1..1] | ± | | 113 |
| | **Type** <Tp> | [0..1] | | | 113 |
| (Or | **Code** <Cd> | [1..1] | CodeSet | | 114 |
| Or) | **Proprietary** <Prtry> | [1..1] | ± | | 114 |
| | **TrackerData** <TrckrData> | [0..1] | | | 114 |
| | **ConfirmedDate** <ConfmDt> | [1..1] | ± | | 115 |
| | **ConfirmedAmount** <ConfdAmt> | [1..*] | Amount | C1, C9 | 115 |
| | **TrackerRecord** <TrckrRcd> | [1..*] | | | 115 |
| | **Agent** <Agtr> | [1..1] | ± | | 116 |

---

<!-- Page 81 -->

| Or | MessageElement/BuildingBlock/XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **ChargeBearer** `<ChrgBr>` | [0..1] | CodeSet | | 116 |
| | **ChargesAmount** `<ChrgsAmt>` | [0..1] | Amount | C1, C9 | 117 |
| | **ExchangeRateData** `<XchgRateData>` | [0..1] | | | 117 |
| | **SourceCurrency** `<SrcCcy>` | [1..1] | CodeSet | C1 | 118 |
| | **TargetCurrency** `<TrgtCcy>` | [1..1] | CodeSet | C1 | 118 |
| | **ExchangeRate** `<XchgRate>` | [1..1] | Rate | | 118 |
| | **UnitCurrency** `<UnitCcy>` | [0..1] | CodeSet | C1 | 118 |
| | **AcceptanceDateTime** `<AcctncDTm>` | [0..1] | DateTime | | 119 |
| | **AccountServicerReference** `<AccctSvcrRef>` | [0..1] | Text | | 119 |
| | **ClearingSystemReference** `<ClrSysRef>` | [0..1] | Text | | 119 |
| | **OriginalTransactionReference** `<OrgnlTxRef>` | [0..1] | | | 119 |
| | **InterbankSettlementAmount** `<IntrBkSttlmAmt>` | [0..1] | Amount | C2, C8 | 122 |
| | **Amount** `<Amt>` | [0..1] | ± | | 122 |
| | **InterbankSettlementDate** `<IntrBkSttlmDt>` | [0..1] | Date | | 123 |
| | **RequestedCollectionDate** `<ReqdColltnDt>` | [0..1] | Date | | 123 |
| | **RequestedExecutionDate** `<ReqdExctnDt>` | [0..1] | ± | | 123 |
| | **CreditorSchemeIdentification** `<CdrtrSchmeId>` | [0..1] | ± | | 123 |
| | **SettlementInformation** `<SttlmInf>` | [0..1] | | C17,<br>C18,<br>C25,<br>C26,<br>C27,<br>C28,<br>C33,<br>C34 | 124 |
| | **SettlementMethod** `<SttlmMtd>` | [1..1] | CodeSet | | 126 |
| | **SettlementAccount** `<SttlmAcct>` | [0..1] | ± | C16,<br>C15 | 127 |
| | **ClearingSystem** `<ClrSys>` | [0..1] | | | 127 |
| (Or | **Code** `<Cd>` | [1..1] | CodeSet | | 128 |
| Or) | **Proprietary** `<Prtry>` | [1..1] | Text | | 128 |
| | **InstructingReimbursementAgent** `<InstdRmbrmntAgtr>` | [0..1] | ± | | 128 |
| | **InstructingReimbursementAgentAccount** `<InstdRmbrmntAgtrAcct>` | [0..1] | ± | C16,<br>C15 | 129 |
| | **InstructedReimbursementAgent** `<InstdRmbrmntAgtr>` | [0..1] | ± | | 129 |
| | **InstructedReimbursementAgentAccount** `<InstdRmbrmntAgtrAcct>` | [0..1] | ± | C16,<br>C15 | 130 |

---

<!-- Page 82 -->

| Or | MessageElement/BuildingBlock<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **ThirdReimbursementAgent** <ThirdRmbrsmntAgnt> | [0..1] | † | | 131 |
| | **ThirdReimbursementAgentAccount** <ThirdRmbrsmntAgntAcct> | [0..1] | † | C16, C15 | 131 |
| | **PaymentTypeInformation** <PmtTpInf> | [0..1] | † | | 132 |
| | **PaymentMethod** <PmtMtd> | [0..1] | CodeSet | | 133 |
| | **MandateRelatedInformation** <MndtRltdInf> | [0..1] | | | 133 |
| (Or | **DirectDebitMandate** <DrtctDbtMndt> | [0..1] | | C3, C4 | 135 |
| | **MandateIdentification** <MndtId> | [0..1] | Text | | 137 |
| | **DateOfSignature** <DtOfSgntr> | [0..1] | Date | | 137 |
| | **AmendmentIndicator** <AmdmntInd> | [0..1] | Indicator | | 137 |
| | **AmendmentInformationDetails** <AmdmntInfDtls> | [0..1] | | | 137 |
| | **OriginalMandateIdentification** <OrgnlMndtId> | [0..1] | Text | | 138 |
| | **OriginalCreditorSchemeIdentification** <OrgnlCdrSchmeId> | [0..1] | † | | 138 |
| | **OriginalCreditorAgent** <OrgnlCddrAgnt> | [0..1] | † | | 139 |
| | **OriginalCreditorAgentAccount** <OrgnlCddrAgntAcct> | [0..1] | † | C16, C15 | 140 |
| | **OriginalDebtor** <OrgnlDbtr> | [0..1] | † | | 141 |
| | **OriginalDebtorAccount** <OrgnlDbtrAcct> | [0..1] | † | C16, C15 | 142 |
| | **OriginalDebtorAgent** <OrgnlDbtrAgnt> | [0..1] | † | | 143 |
| | **OriginalDebtorAgentAccount** <OrgnlDbtrAgntAcct> | [0..1] | † | C16, C15 | 144 |
| | **OriginalFinalCollectionDate** <OrgnlFnCltnDt> | [0..1] | Date | | 145 |
| | **OriginalFrequency** <OrgnlFrcy> | [0..1] | † | | 145 |
| | **OriginalReason** <OrgnlRsn> | [0..1] | | | 145 |
| (Or | **Code** <Cd> | [1..1] | CodeSet | | 145 |
| Or) | **Proprietary** <Prtry> | [1..1] | Text | | 145 |
| | **OriginalTrackingDays** <OrgnlTrckgDays> | [0..1] | Text | | 146 |
| | **ElectronicSignature** <ElctrncSgntr> | [0..1] | Text | | 146 |
| | **FirstCollectionDate** <FrstCollnDt> | [0..1] | Date | | 146 |
| | **FinalCollectionDate** <FnCltnDt> | [0..1] | Date | | 146 |
| | **Frequency** <Frcy> | [0..1] | † | | 146 |
| | **Reason** <Rsn> | [0..1] | | | 146 |

---

<!-- Page 83 -->

| Or | MessageElement/BuildingBlock/<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| [Or | **Code** *<Cd>* | [1..1] | CodeSet |  | 147 |
| Or] | **Proprietary** *<Ptry>* | [1..1] | Text |  | 147 |
|  | **TrackingDays** *<TrckgDays>* | [0..1] | Text |  | 147 |
| Or] | **CreditTransferMandate** *<CdtTrfMndt>* | [0..1] | † |  | 147 |
|  | **RemittanceInformation** *<RmtInf>* | [0..1] | † |  | 148 |
|  | **UltimateDebtor** *<UltmtDbtr>* | [0..1] |  |  | 148 |
| [Or | **Party** *<Pty>* | [1..1] | † |  | 148 |
| Or] | **Agent** *<Agt>* | [1..1] | † |  | 149 |
|  | **Debtor** *<Dbtr>* | [0..1] |  |  | 150 |
| [Or | **Party** *<Pty>* | [1..1] | † |  | 150 |
| Or] | **Agent** *<Agt>* | [1..1] | † |  | 151 |
|  | **DebtorAccount** *<DbtrAcct>* | [0..1] | † | C16, C15 | 152 |
|  | **DebtorAgent** *<DbtrAgt>* | [0..1] | † |  | 153 |
|  | **DebtorAgentAccount** *<DbtrAgtAcct>* | [0..1] | † | C16, C15 | 153 |
|  | **CreditorAgent** *<CdtrAgt>* | [0..1] | † |  | 154 |
|  | **CreditorAgentAccount** *<CdtrAgtAcct>* | [0..1] | † | C16, C15 | 155 |
|  | **Creditor** *<Cdtr>* | [0..1] |  |  | 156 |
| [Or | **Party** *<Pty>* | [1..1] | † |  | 156 |
| Or] | **Agent** *<Agt>* | [1..1] | † |  | 157 |
|  | **CreditorAccount** *<CdtrAcct>* | [0..1] | † | C16, C15 | 158 |
|  | **UltimateCreditor** *<UltmtCdtr>* | [0..1] |  |  | 159 |
| [Or | **Party** *<Pty>* | [1..1] | † |  | 159 |
| Or] | **Agent** *<Agt>* | [1..1] | † |  | 160 |
|  | **Purpose** *<Purp>* | [0..1] | † |  | 161 |
|  | **SupplementaryData** *<SplmtryData>* | [0..*] | † | C32 | 161 |
|  | **SupplementaryData** *<SplmtryData>* | [0..*] | † | C32 | 162 |

---

<!-- Page 84 -->

## 3.3 Constraints

**C1** **ActiveCurrency**

The currency code must be a valid active currency code, not yet withdrawn on the day the message containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day the message containing the Currency is exchanged.

**C2** **ActiveOrHistoricCurrency**

The Currency Code must be registered, or have already been registered. Valid active or historic currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and may be or not be withdrawn on the day the message containing the Currency is exchanged.

**C3** **AmendmentIndicatorFalseRule**

If AmendmentIndicator is false, then AmendmentInformationDetails is not allowed.

**C4** **AmendmentIndicatorTrueRule**

If AmendmentIndicator is true, then AmendmentInformationDetails must be present.

**C5** **AnyBIC**

Only a valid Business identifier code is allowed. Business identifier codes for financial or non-financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.

**C6** **BICFI**

Valid BICs for financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous characters.

**C7** **Country**

The code is checked against the list of country names obtained from the United Nations (ISO 3166, Alpha-2 code).

**C8** **CurrencyAmount**

The number of fractional digits (or minor unit of currency) must comply with ISO 4217.

Note: The decimal separator is a dot.

**C9** **CurrencyAmount**

The number of fractional digits (or minor unit of currency) must comply with ISO 4217.

Note: The decimal separator is a dot.

**C10** **GroupStatusAcceptedRule**

If OriginalGroupInformationAndStatus/GroupStatus is present and is equal to ACTC (AcceptedTechnicalValidation), ACCP (AcceptedCustomerProfile), ACSP (AcceptedSettlementProcess), ACSC (AcceptedSettlementCompleted) or ACWC (AcceptedWithChange), then OriginalPaymentInformationAndStatus/PaymentInformationStatus must be different from RJCT (Rejected).

On Condition

`/OriginalGroupInformationAndStatus/GroupStatus is present`

---

<!-- Page 85 -->

And /OriginalGroupInformationAndStatus/GroupStatus is within DataType
<<Code>> ValidationRuleStatusCode
And /OriginalPaymentInformationAndStatus[*]/PaymentInformationStatus is
present
Following Must be True
/OriginalPaymentInformationAndStatus[*]/PaymentInformationStatus Must not
be within DataType <<Code>> ValidationRuleRejectedCode
*This constraint is defined at the MessageDefinition level.*

**C11** **GroupStatusPendingRule**

If OriginalGroupInformationAndStatus/GroupStatus is present and is equal to PDNG (Pending),
then OriginalPaymentInformationAndStatus/PaymentInformationStatus must be different from
RJCT (Rejected).

On Condition
/OriginalGroupInformationAndStatus/GroupStatus is present
And /OriginalGroupInformationAndStatus/GroupStatus is within DataType
<<Code>> ValidationRulePendingCode
And /OriginalPaymentInformationAndStatus[*]/PaymentInformationStatus is
present
Following Must be True
/OriginalPaymentInformationAndStatus[*]/PaymentInformationStatus Must not
be within DataType <<Code>> ValidationRuleRejectedCode
*This constraint is defined at the MessageDefinition level.*

**C12** **GroupStatusReceivedRule**

If OriginalGroupInformationAndStatus/GroupStatus is present and is equal to RCVD
(Received), then OriginalPaymentInformationAndStatus/PaymentInformationStatus is not
allowed.

On Condition
/OriginalGroupInformationAndStatus/GroupStatus is present
And /OriginalGroupInformationAndStatus/GroupStatus is within DataType
<<Code>> ValidationRuleReceivedCode
And /OriginalPaymentInformationAndStatus[1] is present
Following Must be True
/OriginalPaymentInformationAndStatus[*]/PaymentInformationStatus Must be
absent.
*This constraint is defined at the MessageDefinition level.*

**C13** **GroupStatusRejectedRule**

If OriginalGroupInformationAndStatus/GroupStatus is present and is equal to RJCT (Rejected),
then OriginalPaymentInformationAndStatus/PaymentInformationStatus, if present, must be
equal to RJCT (Rejected).

On Condition
/OriginalGroupInformationAndStatus/GroupStatus is present
And /OriginalGroupInformationAndStatus/GroupStatus is within DataType
<<Code>> ValidationRuleRejectedCode
And /OriginalPaymentInformationAndStatus[*]/PaymentInformationStatus is
present
Following Must be True
/OriginalPaymentInformationAndStatus[*]/PaymentInformationStatus Must be
within DataType <<Code>> ValidationRuleRejectedCode
*This constraint is defined at the MessageDefinition level.*

**C14** **IBAN**

A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.

---

<!-- Page 86 -->

| ID | Rule | Description |
| :--- | :--- | :--- |
| C15 | **IdentificationAndProxyGuideline** | If the account identification is not defined through a conventional identification such as an email address or a mobile number, then the proxy element should be used for the identification of the account. |
| C16 | **IdentificationOrProxyPresenceRule** | Identification must be present or Proxy must be present. Both may be present. |
| C17 | **InstructedReimbursementAgentAccountRule** | If InstructedReimbursementAgentAccount is present, then InstructedReimbursementAgent must be present. |
| C18 | **InstructingReimbursementAgentAccountRule** | If InstructingReimbursementAgentAccount is present, then InstructingReimbursementAgent must be present. |
| C19 | **NumberOfTransactionsPerStatusGuideline** | OriginalGroupInformationAndStatus/NumberOfTransactionsPerStatus should only be present if GroupStatus equals 'PART'. |
| C20 | **PaymentInformationStatusAcceptedRule** | If PaymentInformationAndStatus/PaymentInformationStatus is present and is equal to ACTC (AcceptedTechnicalValidation), ACCP (AcceptedCustomerProfile), ACSP (AcceptedSettlementInProcess), ACSC (AcceptedSettlementCompleted) or ACWC (AcceptedWithChange), then TransactionInformationAndStatus/TransactionStatus must be different from RJCT (Rejected). |
| C21 | **PaymentInformationStatusPendingRule** | If OriginalPaymentInformationAndStatus/PaymentInformationStatus is present and is equal to PDNG (Pending), then TransactionInformationAndStatus/TransactionStatus must be different from RJCT (Rejected). |
| C22 | **PaymentInformationStatusReceivedRule** | If OriginalPaymentInformationAndStatus/PaymentInformationStatus is present and is equal to RCVD (Received), then TransactionInformationAndStatus/TransactionStatus is not allowed. |
| C23 | **PaymentInformationStatusRejectedRule** | If OriginalPaymentInformationAndStatus/PaymentInformationStatus is present and is equal to RJCT (Rejected), then TransactionInformationAndStatus/TransactionStatus, if present, must be equal to RJCT (Rejected). |
| C24 | **RemittanceAmountAndTypeGuideline** | If Type/Code is equal to CREN, DUPA or REMI for RemittanceAmountAndType, RemittanceAmountAndType must not be repeated. |
| C25 | **SettlementMethodAgentRule** | If SettlementMethod is equal to INDA or INGA, then ReimbursementAgent(s) and ClearingSystem are not allowed. |
| C26 | **SettlementMethodClearingRule** | If SettlementMethod is equal to CLRG, then SettlementAccount and ReimbursementAgent(s) are not allowed. |

---

<!-- Page 87 -->

| C27 | **SettlementMethodCoverAgentRule** |
|---|---|
| | If SettlementMethod is equal to COVE, then InstructedReimbursementAgent or InstructingReimbursementAgent must be present. |

| C28 | **SettlementMethodCoverRule** |
|---|---|
| | If SettlementMethod is equal to COVE, then SettlementAccount and ClearingSystem are not allowed. |

| C29 | **StatusReasonInformationRule** |
|---|---|
| | If GroupStatus is present and is different from RJCT or PDNG then StatusReasonInformation/AdditionalInformation must be absent. |

| C30 | **StatusReasonRule** |
|---|---|
| | If Reason/Code is equal to NARR, then AdditionalInformation must be present. |

| C31 | **SupplementaryDataRule** |
|---|---|
| | The SupplementaryData building block at message level must not be used to provide additional information about a transaction. The SupplementaryData element at transaction level should be used for that purpose. |
| | *This constraint is defined at the MessageDefinition level.* |

| C32 | **SupplementaryDataRule** |
|---|---|
| | This component may not be used without the explicit approval of a SEG and submission to the RA of ISO 20022 compliant structure(s) to be used in the Envelope element. |

| C33 | **ThirdReimbursementAgentAccountRule** |
|---|---|
| | If ThirdReimbursementAgentAccount is present, then ThirdReimbursementAgent must be present. |

| C34 | **ThirdReimbursementAgentRule** |
|---|---|
| | If ThirdReimbursementAgent is present, then InstructingReimbursementAgent and InstructedReimbursementAgent must both be present. |

## 3.4 Message Building Blocks

This chapter describes the MessageBuildingBlocks of this MessageDefinition.

### 3.4.1 GroupHeader <GrpHdr>

*Presence:* [1..1]

*Definition:* Set of characteristics shared by all individual transactions included in the status report message.

---

<!-- Page 88 -->

GroupHeader <GrpHdr> contains the following GroupHeader128 elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | **MessageIdentification** <MsgId> | [1..1] | Text | | 88 |
| | **CreationDateTime** <CreDtTm> | [1..1] | DateTime | | 88 |
| | **InitiatingParty** <InitPty> | [0..1] | ± | | 88 |
| | **ForwardingAgent** <FwdgAgt> | [0..1] | ± | | 89 |
| | **DebtorAgent** <DbtrAgt> | [0..1] | ± | | 90 |
| | **CreditorAgent** <CdtrAgt> | [0..1] | ± | | 91 |

## 3.4.1.1 MessageIdentification <MsgId>

*Presence:* [1..1]

*Definition:* Point to point reference, as assigned by the instructing party, and sent to the next party in the chain to unambiguously identify the message.

Usage: The instructing party has to make sure that 'MessageIdentification' is unique per instructed party for a pre-agreed period.

*Datatype:* "Max35Text" on page 431

## 3.4.1.2 CreationDateTime <CreDtTm>

*Presence:* [1..1]

*Definition:* Date and time at which the message was created.

*Datatype:* "ISODateTime" on page 425

## 3.4.1.3 InitiatingParty <InitPty>

*Presence:* [0..1]

*Definition:* Party that initiates the status message.

---

<!-- Page 89 -->

InitiatingParty <InitgPty> contains the following elements (see "PartyIdentification27" on page 336 for details)



| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | Name <Nm> | [0..1] | Text | | 337 |
| | PostalAddress <PstlAdr> | [0..1] | † | | 338 |
| | Identification <Id> | [0..1] | | | 338 |
| Or | OrganisationIdentification <OrgId> | [1..1] | | | 339 |
| | AnyBIC <AnyBIC> | [0..1] | IdentifierSet | C5 | 340 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 340 |
| | Other <Othr> | [0..*] | | | 340 |
| | Identification <Id> | [1..1] | Text | | 341 |
| | SchemeName <SchmeNm> | [0..1] | | | 341 |
| Or | Code <Cd> | [1..1] | CodeSet | | 341 |
| Or | Proprietary <Prtry> | [1..1] | Text | | 341 |
| | Issuer <Issr> | [0..1] | Text | | 341 |
| Or | PrivateIdentification <PrvtId> | [1..1] | | | 341 |
| | DateAndPlaceOfBirth <DtAndPlcOfBirth> | [0..1] | | | 342 |
| | BirthDate <BirthDt> | [1..1] | Date | | 342 |
| | ProvinceOfBirth <PrvcOfBirth> | [0..1] | Text | | 342 |
| | CityOfBirth <CityOfBirth> | [1..1] | Text | | 343 |
| | CountryOfBirth <CtryOfBirth> | [1..1] | CodeSet | C7 | 343 |
| | Other <Othr> | [0..*] | | | 343 |
| | Identification <Id> | [1..1] | Text | | 343 |
| | SchemeName <SchmeNm> | [0..1] | | | 343 |
| Or | Code <Cd> | [1..1] | CodeSet | | 344 |
| Or | Proprietary <Prtry> | [1..1] | Text | | 344 |
| | Issuer <Issr> | [0..1] | Text | | 344 |
| | CountryOfResidence <CtryOfRes> | [0..1] | CodeSet | C7 | 344 |
| | ContactDetails <CtctDtls> | [0..1] | † | | 344 |

### 3.4.1.4 ForwardingAgent <FwdgAgt>

*Presence:* [0..1]

*Definition:* Financial institution that receives the instruction from the initiating party and forwards it to the next agent in the payment chain.

---

<!-- Page 90 -->

ForwardingAgent <FwdgAgt> contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on page 320 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | FinancialInstitutionIdentification <FinInstId> | [0..1] | | | 321 |
| | BICFI <BICFI> | [0..1] | IdentifierSet | C6 | 321 |
| | ClearingSystemMemberIdentification <ClrSysMmbId> | [0..1] | ± | | 322 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 322 |
| | Name <Nm> | [0..1] | Text | | 322 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 322 |
| | Other <Othr> | [0..1] | ± | | 323 |
| | BranchIdentification <BrnchId> | [0..1] | | | 324 |
| | Identification <Id> | [0..1] | Text | | 324 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 324 |
| | Name <Nm> | [0..1] | Text | | 324 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 324 |

## 3.4.1.5 DebtorAgent <DbtrAgt>

Presence: [0..1]

Definition: Financial institution servicing an account for the debtor.

DebtorAgent <DbtrAgt> contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on page 320 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | FinancialInstitutionIdentification <FinInstId> | [1..1] | | | 321 |
| | BICFI <BICFI> | [0..1] | IdentifierSet | C6 | 321 |
| | ClearingSystemMemberIdentification <ClrSysMmbId> | [0..1] | ± | | 322 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 322 |
| | Name <Nm> | [0..1] | Text | | 322 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 322 |
| | Other <Othr> | [0..1] | ± | | 323 |
| | BranchIdentification <BrnchId> | [0..1] | | | 324 |
| | Identification <Id> | [0..1] | Text | | 324 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 324 |
| | Name <Nm> | [0..1] | Text | | 324 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 324 |

---

<!-- Page 91 -->

### 3.4.1.6 CreditorAgent <Cdt rAgtr>

*Presence:* [0..1]

*Definition:* Financial institution servicing an account for the creditor.

**CreditorAgent <Cdt rAgtr>** contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on page 320 for details)

| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | FinancialInstitutionIdentification <FinInstnId> | [1..1] | | | 321 |
| | BICFI <BICFI> | [0..1] | IdentifierSet | C6 | 321 |
| | ClearingSystemMemberIdentification <ClrSysMmbId> | [0..1] | ± | | 322 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 322 |
| | Name <Nm> | [0..1] | Text | | 322 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 322 |
| | Other <Othr> | [0..1] | ± | | 323 |
| | BranchIdentification <BrchId> | [0..1] | | | 324 |
| | Identification <Id> | [0..1] | Text | | 324 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 324 |
| | Name <Nm> | [0..1] | Text | | 324 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 324 |

## 3.4.2 OriginalGroupInformationAndStatus <OrgnlGrpInfAndSts>

*Presence:* [1..1]

*Definition:* Original group information concerning the group of transactions, to which the status report message refers to.

*Impacted by:* C29 "StatusReasonInformationRule", C19 "NumberOfTransactionPerStatusGuideline"

---

<!-- Page 92 -->

OriginalGroupInformationAndStatus <OrgnlGrpInfAndSts> contains the following OriginalGroupHeader22 elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | **OriginalMessageIdentification** *<OrgnlMsgId>* | [1..1] | Text | | 92 |
| | **OriginalMessageNameIdentification** *<OrgnlMsgNmId>* | [1..1] | Text | | 92 |
| | **OriginalCreationDateTime** *<OrgnlCdtTm>* | [0..1] | DateTime | | 93 |
| | **OriginalNumberOfTransactions** *<OrgnlNbOfTxs>* | [0..1] | Text | | 93 |
| | **OriginalControlSum** *<OrgnlCtrlSum>* | [0..1] | Quantity | | 93 |
| | **GroupStatus** *<GrpSts>* | [0..1] | CodeSet | | 93 |
| | **StatusReasonInformation** *<StsRsnInf>* | [0..*] | | C30 | 93 |
| | **Originator** *<Orgtr>* | [0..1] | ± | | 94 |
| | **Reason** *<Rsn>* | [0..1] | | | 95 |
| Or | **Code** *<Cd>* | [1..1] | CodeSet | | 96 |
| Or | **Proprietary** *<Prtry>* | [1..1] | Text | | 96 |
| | **AdditionalInformation** *<AddtlInf>* | [0..*] | Text | | 96 |
| | **NumberOfTransactionsPerStatus** *<NbOfTxsPerSts>* | [0..*] | ± | | 96 |

## Constraints

*   **NumberOfTransactionPerStatusGuideline**

    OriginalGroupInformationAndStatus/NumberOfTransactionsPerStatus should only be present if GroupStatus equals 'PART'.

*   **StatusReasonInformationRule**

    If GroupStatus is present and is different from RJCT or PDNG then StatusReasonInformation/AdditionalInformation must be absent.

    On Condition

    /GroupStatus is present

    And /GroupStatus is not within DataType *<Code>*

    ValidationRuleFailingAndRejectedCode

    Following Must be True

    /StatusReasonInformation[*]/AdditionalInformation[*] Must be absent

### 3.4.2.1 OriginalMessageIdentification <OrgnlMsgId>

*Presence:* [1..1]

*Definition:* Point to point reference, as assigned by the original instructing party, to unambiguously identify the original message.

*Datatype:* 'Max35Text' on page 431

### 3.4.2.2 OriginalMessageNameIdentification <OrgnlMsgNmId>

*Presence:* [1..1]

*Definition:* Specifies the original message name identifier to which the message refers.

---

<!-- Page 93 -->

Datatype: "Max35Text" on page 431

### 3.4.2.3 OriginalCreationDateTime <OrgnlCreDtTm>

Presence: [0..1]

Definition: Date and time at which the original message was created.

Datatype: "ISODateTime" on page 425

### 3.4.2.4 OriginalNumberOfTransactions <OrgnlNbOfTxs>

Presence: [0..1]

Definition: Number of individual transactions contained in the original message.

Datatype: "Max15NumericText" on page 430

### 3.4.2.5 OriginalControlSum <OrgnlCtrlSum>

Presence: [0..1]

Definition: Total of all individual amounts included in the original message, irrespective of currencies.

Datatype: "DecimalNumber" on page 427

### 3.4.2.6 GroupStatus <GrpSts>

Presence: [0..1]

Definition: Specifies the status of a group of transactions.

Datatype: "ExternalPaymentGroupStatus1Code" on page 417

### 3.4.2.7 StatusReasonInformation <StsRsnInf>

Presence: [0..*]

Definition: Provides detailed information on the status reason.

Impacted by: C30 "StatusReasonRule"

StatusReasonInformation <StsRsnInf> contains the following StatusReasonInformation14 elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **Originator** <Orgtr> | [0..1] | ± | | 94 |
| | **Reason** <Rsn> | [0..1] | | | 95 |
| [Or | **Code** <Cd> | [1..1] | CodeSet | | 96 |
| Or] | **Proprietary** <Prtry> | [1..1] | Text | | 96 |
| | **AdditionalInformation** <AddtlInf> | [0..*] | Text | | 96 |

**Constraints**

*   **StatusReasonRule**

    If Reason/Code is equal to NARR, then AdditionalInformation must be present.

---

<!-- Page 94 -->

On Condition
/Reason/Code is within DataType &lt;&lt;Code&gt;&gt; ValidationRuleNarrative1Code
And    /Reason is present
And    /Reason/Code is present
Following Must be True
/AdditionalInformation[1] Must be present

**3.4.2.7.1 Originator &lt;Orgtr&gt;**

*Presence:* [0..1]

*Definition:* Party that issues the status.

---

<!-- Page 95 -->

Originator <Orgrt> contains the following elements (see "PartyIdentification272" on page 336 for details)



| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | Name <Nm> | [0..1] | Text | | 337 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 338 |
| | Identification <Id> | [0..1] | | | 338 |
| (Or | OrganisationIdentification <OrgId> | [1..1] | | | 339 |
| | AnyBIC <AnyBIC> | [0..1] | IdentifierSet | C5 | 340 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 340 |
| | Other <Othr> | [0..*] | | | 340 |
| | Identification <Id> | [1..1] | Text | | 341 |
| | SchemeName <SchmeNm> | [0..1] | | | 341 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 341 |
| Or | Proprietary <Prtry> | [1..1] | Text | | 341 |
| | Issuer <Issr> | [0..1] | Text | | 341 |
| (Or) | PrivateIdentification <PrvtId> | [1..1] | | | 341 |
| | DateAndPlaceOfBirth <DtAndPlcOfBirth> | [0..1] | | | 342 |
| | BirthDate <BirthDt> | [1..1] | Date | | 342 |
| | ProvinceOfBirth <PrvcOfBirth> | [0..1] | Text | | 342 |
| | CityOfBirth <CityOfBirth> | [1..1] | Text | | 343 |
| | CountryOfBirth <CtryOfBirth> | [1..1] | CodeSet | C7 | 343 |
| | Other <Othr> | [0..*] | | | 343 |
| | Identification <Id> | [1..1] | Text | | 343 |
| | SchemeName <SchmeNm> | [0..1] | | | 343 |
| (Or) | Code <Cd> | [1..1] | CodeSet | | 344 |
| Or) | Proprietary <Prtry> | [1..1] | Text | | 344 |
| | Issuer <Issr> | [0..1] | Text | | 344 |
| | CountryOfResidence <CtryOfRes> | [0..1] | CodeSet | C7 | 344 |
| | ContactDetails <CtctDtls> | [0..1] | ± | | 344 |

### 3.4.2.7.2 Reason <Rsn>

*Presence:* [0..1]

*Definition:* Specifies the reason for the status report.

---

<!-- Page 96 -->

Reason <Rsn> contains one of the following StatusReason6Choice elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| (Or | Code <Cd> | [1..1] | CodeSet | | 96 |
| Or) | Proprietary <Pry> | [1..1] | Text | | 96 |

### 3.4.2.7.2.1 Code <Cd>

*Presence:* [1..1]

*Definition:* Reason for the status, as published in an external reason code list.

*Datatype:* "ExternalStatusReason1Code" on page 419

### 3.4.2.7.2.2 Proprietary <Pry>

*Presence:* [1..1]

*Definition:* Reason for the status, in a proprietary form.

*Datatype:* "Max35Text" on page 431

### 3.4.2.7.3 AdditionalInformation <AddtlInf>

*Presence:* [0..*]

*Definition:* Further details on the status reason.

Usage: Additional information can be used for several purposes such as the reporting of repaired information.

*Datatype:* "Max105Text" on page 429

## 3.4.2.8 NumberOfTransactionsPerStatus <NbOfTxsPerSts>

*Presence:* [0..*]

*Definition:* Detailed information on the number of transactions for each identical transaction status.

NumberOfTransactionsPerStatus <NbOfTxsPerSts> contains the following elements (see "NumberOfTransactionsPerStatus" on page 335 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | DetailedNumberOfTransactions <DtldNbOfTxs> | [1..1] | Text | | 335 |
| | DetailedStatus <DtldSts> | [1..1] | CodeSet | | 335 |
| | DetailedControlSum <DtldCtrlSum> | [0..1] | Quantity | | 335 |

## 3.4.3 OriginalPaymentInformationAndStatus <OrgnlPmtInfAndSts>

*Presence:* [0..*]

*Definition:* Information concerning the original payment information, to which the status report message refers.

---

<!-- Page 97 -->

*Impacted by:* C20 "PaymentInformationStatusAcceptedRule", C21
"PaymentInformationStatusPendingRule", C22 "PaymentInformationStatusReceivedRule", C23
"PaymentInformationStatusRejectedRule"

---

<!-- Page 98 -->

OriginalPaymentInformationAndStatus <OrgnlPmtInfAndSts> contains the following OriginalPaymentInstruction51 elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | OriginalPaymentInformationIdentification <OrgnlPmtInfId> | [1..1] | Text | | 102 |
| | OriginalNumberOfTransactions <OrgnlNbOfTxs> | [0..1] | Text | | 103 |
| | OriginalControlSum <OrgnlCtrlSum> | [0..1] | Quantity | | 103 |
| | PaymentInformationStatus <PmtInfSts> | [0..1] | CodeSet | | 103 |
| | StatusReasonInformation <StsRsnInf> | [0..*] | | C30 | 103 |
| | Originator <Orgtr> | [0..1] | ± | | 104 |
| | Reason <Rsn> | [0..1] | | | 105 |
| Or | Code <Cd> | [1..1] | CodeSet | | 105 |
| Or | Proprietary <Prtry> | [1..1] | Text | | 105 |
| | AdditionalInformation <AddtlInf> | [0..*] | Text | | 105 |
| | NumberOfTransactionsPerStatus <NbOfTxsPerSts> | [0..*] | ± | | 105 |
| | TransactionInformationAndStatus <TxInfAndSts> | [0..*] | | | 105 |
| | StatusIdentification <StsId> | [0..1] | Text | | 109 |
| | OriginalInstructionIdentification <OrgnlInstrId> | [0..1] | Text | | 109 |
| | OriginalEndToEndIdentification <OrgnlEndToEndId> | [0..1] | Text | | 109 |
| | OriginalUETR <OrgnlUETR> | [0..1] | IdentifierSet | | 110 |
| | TransactionStatus <TxSts> | [0..1] | CodeSet | | 110 |
| | StatusReasonInformation <StsRsnInf> | [0..*] | | C30 | 110 |
| | Originator <Orgtr> | [0..1] | ± | | 110 |
| | Reason <Rsn> | [0..1] | | | 111 |
| Or | Code <Cd> | [1..1] | CodeSet | | 112 |
| Or | Proprietary <Prtry> | [1..1] | Text | | 112 |
| | AdditionalInformation <AddtlInf> | [0..*] | Text | | 112 |
| | ChargesInformation <ChrgInf> | [0..*] | | | 112 |
| | Amount <Amt> | [1..1] | Amount | C2, C8 | 112 |
| | Agent <Agt> | [1..1] | ± | | 113 |
| | Type <Tp> | [0..1] | | | 113 |
| Or | Code <Cd> | [1..1] | CodeSet | | 114 |
| Or | Proprietary <Prtry> | [1..1] | ± | | 114 |
| | TrackerData <TrckrData> | [0..1] | | | 114 |

---

<!-- Page 99 -->

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **ConfirmedDate** `<ConfdDt>` | [1..1] | ± | | 115 |
| | **ConfirmedAmount** `<ConfdAmt>` | [1..1] | Amount | C1, C9 | 115 |
| | **TrackerRecord** `<TrckrRcrd>` | [1..*] | | | 115 |
| | **Agent** `<Agnt>` | [1..1] | ± | | 116 |
| | **ChargeBearer** `<ChrgBr>` | [0..1] | CodeSet | | 116 |
| | **ChargesAmount** `<ChrgsAmt>` | [0..1] | Amount | C1, C9 | 117 |
| | **ExchangeRateData** `<XchgRateData>` | [0..1] | | | 117 |
| | **SourceCurrency** `<SrcCcy>` | [1..1] | CodeSet | C1 | 118 |
| | **TargetCurrency** `<TgtCcy>` | [1..1] | CodeSet | C1 | 118 |
| | **ExchangeRate** `<XchgRate>` | [1..1] | Rate | | 118 |
| | **UnitCurrency** `<UnitCcy>` | [0..1] | CodeSet | C1 | 118 |
| | **AcceptanceDateTime** `<AcctpnctDtTm>` | [0..1] | Date Time | | 119 |
| | **AccountServicerReference** `<AcctSvcrRef>` | [0..1] | Text | | 119 |
| | **ClearingSystemReference** `<ClrSysRef>` | [0..1] | Text | | 119 |
| | **OriginalTransactionReference** `<OrgnlTxRef>` | [0..1] | | | 119 |
| | **InterbankSettlementAmount** `<IntrBkSttlmAmt>` | [0..1] | Amount | C2, C8 | 122 |
| | **Amount** `<Amt>` | [0..1] | ± | | 122 |
| | **InterbankSettlementDate** `<IntrBkSttlmDt>` | [0..1] | Date | | 123 |
| | **RequestedCollectionDate** `<ReqdCollnDt>` | [0..1] | Date | | 123 |
| | **RequestedExecutionDate** `<ReqdExctnDt>` | [0..1] | ± | | 123 |
| | **CreditorSchemeIdentification** `<CdtiSchmeId>` | [0..1] | ± | | 123 |
| | **SettlementInformation** `<SttlmInf>` | [0..1] | | C17, C18, C25, C26, C27, C28, C33, C34 | 124 |
| | **SettlementMethod** `<SttlmMtd>` | [1..1] | CodeSet | | 126 |
| | **SettlementAccount** `<SttlmAcc>` | [0..1] | ± | C16, C15 | 127 |
| | **ClearingSystem** `<ClrSys>` | [0..1] | | | 127 |
| Or | **Code** `<Cd>` | [1..1] | CodeSet | | 128 |
| Or | **Proprietary** `<Prtry>` | [1..1] | Text | | 128 |

---

<!-- Page 100 -->

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **InstructingReimbursementAgent** *<InstrgRmbrsmtAgnt>* | [0..1] | ± | | 128 |
| | **InstructingReimbursementAgentAccount** *<InstrgRmbrsmtAgntAcct>* | [0..1] | ± | C16, C15 | 129 |
| | **InstructedReimbursementAgent** *<InstdRmbrsmtAgnt>* | [0..1] | ± | | 129 |
| | **InstructedReimbursementAgentAccount** *<InstdRmbrsmtAgntAcct>* | [0..1] | ± | C16, C15 | 130 |
| | **ThirdReimbursementAgent** *<ThirdRmbrsmtAgnt>* | [0..1] | ± | | 131 |
| | **ThirdReimbursementAgentAccount** *<ThirdRmbrsmtAgntAcct>* | [0..1] | ± | C16, C15 | 131 |
| | **PaymentTypeInformation** *<PmtTpInf>* | [0..1] | ± | | 132 |
| | **PaymentMethod** *<PmtMtd>* | [0..1] | CodeSet | | 133 |
| | **MandateRelatedInformation** *<MndtReltdInf>* | [0..1] | | | 133 |
| (Or | **DirectDebitMandate** *<DrctDbtMndt>* | [0..1] | | C3, C4 | 135 |
| | **MandateIdentification** *<MndtId>* | [0..1] | Text | | 137 |
| | **DateOfSignature** *<DtOfSgntr>* | [0..1] | Date | | 137 |
| | **AmendmentIndicator** *<AmdmntInd>* | [0..1] | Indicator | | 137 |
| | **AmendmentInformationDetails** *<AmdmntInfDtls>* | [0..1] | | | 137 |
| | **OriginalMandateIdentification** *<OrgnlMndtId>* | [0..1] | Text | | 138 |
| | **OriginalCreditorSchemeIdentification** *<OrgnlCddtrSchemId>* | [0..1] | ± | | 138 |
| | **OriginalCreditorAgent** *<OrgnlCddtrAgnt>* | [0..1] | ± | | 139 |
| | **OriginalCreditorAgentAccount** *<OrgnlCddtrAgntAcct>* | [0..1] | ± | C16, C15 | 140 |
| | **OriginalDebtor** *<OrgnlDbtr>* | [0..1] | ± | | 141 |
| | **OriginalDebtorAccount** *<OrgnlDbtrAcct>* | [0..1] | ± | C16, C15 | 142 |
| | **OriginalDebtorAgent** *<OrgnlDbtrAgnt>* | [0..1] | ± | | 143 |
| | **OriginalDebtorAgentAccount** *<OrgnlDbtrAgntAcct>* | [0..1] | ± | C16, C15 | 144 |
| | **OriginalFinalCollectionDate** *<OrgnlFnClctnDt>* | [0..1] | Date | | 145 |
| | **OriginalFrequency** *<OrgnlFrqcy>* | [0..1] | ± | | 145 |
| | **OriginalReason** *<OrgnlRsn>* | [0..1] | | | 145 |
| (Or | **Code** *<Cd>* | [1..1] | CodeSet | | 145 |
| Or) | **Proprietary** *<Prtry>* | [1..1] | Text | | 145 |
| | **OriginalTrackingDays** *<OrgnlTrckgDays>* | [0..1] | Text | | 146 |

---

<!-- Page 101 -->

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **ElectronicSignature** <ElectmcSgntr> | [0..1] | Text | | 146 |
| | **FirstCollectionDate** <FrstColltnDt> | [0..1] | Date | | 146 |
| | **FinalCollectionDate** <FnIColltnDt> | [0..1] | Date | | 146 |
| | **Frequency** <Frqcy> | [0..1] | ± | | 146 |
| | **Reason** <Rsn> | [0..1] | | | 146 |
| (Or | **Code** <Cd> | [1..1] | CodeSet | | 147 |
| Or) | **Proprietary** <Prtry> | [1..1] | Text | | 147 |
| | **TrackingDays** <TrckgDays> | [0..1] | Text | | 147 |
| Or | **CreditTransferMandate** <CdtTrfMndt> | [0..1] | ± | | 147 |
| | **RemittanceInformation** <RmInf> | [0..1] | ± | | 148 |
| | **UltimateDebtor** <UltmDbtr> | [0..1] | | | 148 |
| (Or | **Party** <Pty> | [1..1] | ± | | 148 |
| Or) | **Agent** <Agt> | [1..1] | ± | | 149 |
| | **Debtor** <Dbtr> | [0..1] | | | 150 |
| (Or | **Party** <Pty> | [1..1] | ± | | 150 |
| Or) | **Agent** <Agt> | [1..1] | ± | | 151 |
| | **DebtorAccount** <DbtrAcct> | [0..1] | ± | C16, C15 | 152 |
| | **DebtorAgent** <DbtrAgt> | [0..1] | ± | | 153 |
| | **DebtorAgentAccount** <DbtrAgtAcct> | [0..1] | ± | C16, C15 | 153 |
| | **CreditorAgent** <CdtrAgt> | [0..1] | ± | | 154 |
| | **CreditorAgentAccount** <CdtrAgtAcct> | [0..1] | ± | C16, C15 | 155 |
| | **Creditor** <Cdtr> | [0..1] | | | 156 |
| (Or | **Party** <Pty> | [1..1] | ± | | 156 |
| Or) | **Agent** <Agt> | [1..1] | ± | | 157 |
| | **CreditorAccount** <CdtrAcct> | [0..1] | ± | C16, C15 | 158 |
| | **UltimateCreditor** <UltmtCdtr> | [0..1] | | | 159 |
| (Or | **Party** <Pty> | [1..1] | ± | | 159 |
| Or) | **Agent** <Agt> | [1..1] | ± | | 160 |
| | **Purpose** <Purp> | [0..1] | ± | | 161 |
| | **SupplementaryData** <SplmtryData> | [0..*] | ± | C32 | 161 |

---

<!-- Page 102 -->

Constraints

*   **PaymentInformationStatusAcceptedRule**

    If PaymentInformationStatus is present and is equal to ACTC (AcceptedTechnicalValidation), ACCP (AcceptedCustomerProfile), ACSP (AcceptedSettlementInProcess), ACSC (AcceptedSettlementCompleted) or ACWC (AcceptedWithChange), then TransactionInformationAndStatus/TransactionStatus must be different from RJCT (Rejected).
    On Condition
    /PaymentInformationStatus is present
    And /PaymentInformationStatus is within DataType <Code>
    ValidationRuleStatus1Code
    And /TransactionInformationAndStatus[*]/TransactionStatus is present
    Following Must be True
    /TransactionInformationAndStatus[*]/TransactionStatus Must not be within DataType <Code> ValidationRuleRejectedCode

*   **PaymentInformationStatusPendingRule**

    If OriginalPaymentInformationAndStatus/PaymentInformationStatus is present and is equal to PDNG (Pending), then TransactionInformationAndStatus/TransactionStatus must be different from RJCT (Rejected).
    On Condition
    /PaymentInformationStatus is present
    And /PaymentInformationStatus is within DataType <Code>
    ValidationRulePendingCode
    And /TransactionInformationAndStatus[*]/TransactionStatus is present
    Following Must be True
    /TransactionInformationAndStatus[*]/TransactionStatus Must not be within DataType <Code> ValidationRuleRejectedCode

*   **PaymentInformationStatusReceivedRule**

    If OriginalPaymentInformationAndStatus/PaymentInformationStatus is present and is equal to RCVD (Received), then TransactionInformationAndStatus/TransactionStatus is not allowed.
    On Condition
    /PaymentInformationStatus is present
    And /PaymentInformationStatus is within DataType <Code>
    ValidationRuleReceivedCode
    And /TransactionInformationAndStatus[1] is present
    Following Must be True
    /TransactionInformationAndStatus[*]/TransactionStatus Must be absent

*   **PaymentInformationStatusRejectedRule**

    If OriginalPaymentInformationAndStatus/PaymentInformationStatus is present and is equal to RJCT (Rejected), then TransactionInformationAndStatus/TransactionStatus, if present, must be equal to RJCT (Rejected).
    On Condition
    /PaymentInformationStatus is present
    And /PaymentInformationStatus is within DataType <Code>
    ValidationRuleRejectedCode
    And /TransactionInformationAndStatus[*]/TransactionStatus is present
    Following Must be True
    /TransactionInformationAndStatus[*]/TransactionStatus Must be within DataType <Code> ValidationRuleRejectedCode

### 3.4.3.1 OriginalPaymentInformationIdentification <OrgnlPmtInflId>

*Presence: [1..1]*

*Definition: Unique identification, as assigned by the original sending party, to unambiguously identify the original payment information group.*

---

<!-- Page 103 -->

Datatype: "Max35Text" on page 431

### 3.4.3.2 OriginalNumberOfTransactions <OrgnlNbOfTxs>

Presence: [0..1]

Definition: Number of individual transactions contained in the original payment information group.

Datatype: "Max15NumericText" on page 430

### 3.4.3.3 OriginalControlSum <OrgnlCtrlSum>

Presence: [0..1]

Definition: Total of all individual amounts included in the original payment information group, irrespective of currencies.

Datatype: "DecimalNumber" on page 427

### 3.4.3.4 PaymentInformationStatus <PmtInfSts>

Presence: [0..1]

Definition: Specifies the status of the payment information group.

Datatype: "ExternalPaymentGroupStatus1Code" on page 417

### 3.4.3.5 StatusReasonInformation <StsRsnInf>

Presence: [0..*]

Definition: Provides detailed information on the status reason.

Impacted by: C30 "StatusReasonRule"

StatusReasonInformation <StsRsnInf> contains the following StatusReasonInformation14 elements

| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | **Originator** <Orgtr> | [0..1] | ± | | 104 |
| | **Reason** <Rsn> | [0..1] | | | 105 |
| Or | **Code** <Cd> | [1..1] | CodeSet | | 105 |
| Or | **Proprietary** <Prt> | [1..1] | Text | | 105 |
| | **AdditionalInformation** <AddtlInf> | [0..*] | Text | | 105 |

## Constraints

*   **StatusReasonRule**

    If Reason/Code is equal to NARR, then AdditionalInformation must be present.

    On Condition
    /Reason/Code is within DataType <Code> ValidationRuleNarrative1Code
    And /Reason is present
    And /Reason/Code is present

---

<!-- Page 104 -->

Following Must be True
/AdditionalInformation[1] Must be present

### 3.4.3.5.1 Originator <Orgtr>

Presence: [0..1]

Definition: Party that issues the status.

**Originator <Orgtr>** contains the following elements (see "**PartyIdentification272**" on page 336 for details)



| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Name <Nm> | [0..1] | Text | | 337 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 338 |
| | Identification <Id> | [0..1] | | | 338 |
| (Or | OrganisationIdentification <OrgId> | [1..1] | | | 339 |
| | AnyBIC <AnyBIC> | [0..1] | IdentifierSet | C5 | 340 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 340 |
| | Other <Othr> | [0..*] | | | 340 |
| | Identification <Id> | [1..1] | Text | | 341 |
| | SchemeName <SchmeNm> | [0..1] | | | 341 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 341 |
| Or | Proprietary <Ptry> | [1..1] | Text | | 341 |
| | Issuer <Issr> | [0..1] | Text | | 341 |
| Or | PrivateIdentification <PrvtId> | [1..1] | | | 341 |
| | DateAndPlaceOfBirth<DtAndPlcOfBirth> | [0..1] | | | 342 |
| | BirthDate <BirthDt> | [1..1] | Date | | 342 |
| | ProvinceOfBirth <PrvcOfBirth> | [0..1] | Text | | 342 |
| | CityOfBirth <CityOfBirth> | [1..1] | Text | | 343 |
| | CountryOfBirth <CtryOfBirth> | [1..1] | CodeSet | C7 | 343 |
| | Other <Othr> | [0..*] | | | 343 |
| | Identification <Id> | [1..1] | Text | | 343 |
| | SchemeName <SchmeNm> | [0..1] | | | 343 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 344 |
| Or | Proprietary <Ptry> | [1..1] | Text | | 344 |
| | Issuer <Issr> | [0..1] | Text | | 344 |
| | CountryOfResidence <CtryOfRes> | [0..1] | CodeSet | C7 | 344 |
| | ContactDetails <CntctDtls> | [0..1] | ± | | 344 |

---

<!-- Page 105 -->

### 3.4.3.5.2 Reason <Rsn>

*Presence:* [0..1]

*Definition:* Specifies the reason for the status report.

**Reason <Rsn>** contains one of the following **StatusReason6Choice** elements



| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| (Or | **Code** <Cd> | [1..1] | CodeSet | | 105 |
| (Or) | **Proprietary** <Prtry> | [1..1] | Text | | 105 |

#### 3.4.3.5.2.1 Code <Cd>

*Presence:* [1..1]

*Definition:* Reason for the status, as published in an external reason code list.

*Datatype:* "ExternalStatusReason1Code" on page 419

#### 3.4.3.5.2.2 Proprietary <Prtry>

*Presence:* [1..1]

*Definition:* Reason for the status, in a proprietary form.

*Datatype:* "Max35Text" on page 431

### 3.4.3.5.3 AdditionalInformation <AddtlIno>

*Presence:* [0..*]

*Definition:* Further details on the status reason.

Usage: Additional information can be used for several purposes such as the reporting of repaired information.

*Datatype:* "Max105Text" on page 429

### 3.4.3.6 NumberOfTransactionsPerStatus <NbOfTxsPerSts>

*Presence:* [0..*]

*Definition:* Detailed information on the number of transactions for each identical transaction status.

**NumberOfTransactionsPerStatus <NbOfTxsPerSts>** contains the following elements (see "NumberOfTransactionsPerStatus5" on page 335 for details)



| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | DetailedNumberOfTransactions <DtldNbOfTxs> | [1..1] | Text | | 335 |
| | DetailedStatus <DtldSts> | [1..1] | CodeSet | | 335 |
| | DetailedControlSum <DtldCtrlSum> | [0..1] | Quantity | | 335 |

### 3.4.3.7 TransactionInformationAndStatus <TxInfAndSts>

*Presence:* [0..*]

*Definition:* Provides information on the original transactions to which the status report message refers.

---

<!-- Page 106 -->

TransactionInformationAndStatus <TxInfAndSts> contains the following PaymentTransaction160 elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **StatusIdentification** <StsId> | [0..1] | Text | | 109 |
| | **OriginalInstructionIdentification** <OrgnlInstrId> | [0..1] | Text | | 109 |
| | **OriginalEndToEndIdentification** <OrgnlEndToEndId> | [0..1] | Text | | 109 |
| | **OriginalUIETR** <OrgnlUIETR> | [0..1] | IdentifierSet | | 110 |
| | **TransactionStatus** <TxSts> | [0..1] | CodeSet | | 110 |
| | **StatusReasonInformation** <StsRsnInf> | [0..*] | | C30 | 110 |
| | **Originator** <Orgtr> | [0..1] | ± | | 110 |
| | **Reason** <Rsn> | [0..1] | | | 111 |
| (Or | **Code** <Cd> | [1..1] | CodeSet | | 112 |
| Or) | **Proprietary** <Prtty> | [1..1] | Text | | 112 |
| | **AdditionalInformation** <AddtlInf> | [0..*] | Text | | 112 |
| | **ChargesInformation** <ChrgsInf> | [0..*] | | | 112 |
| | **Amount** <Amt> | [1..1] | Amount | C2, C8 | 112 |
| | **Agent** <Agtr> | [1..1] | ± | | 113 |
| | **Type** <Tp> | [0..1] | | | 113 |
| (Or | **Code** <Cd> | [1..1] | CodeSet | | 114 |
| Or) | **Proprietary** <Prtty> | [1..1] | ± | | 114 |
| | **TrackerData** <TrckrData> | [0..1] | | | 114 |
| | **ConfirmedDate** <ConfmtdDt> | [1..1] | ± | | 115 |
| | **ConfirmedAmount** <ConfmtdAmt> | [1..1] | Amount | C1, C9 | 115 |
| | **TrackerRecord** <TrckrRcrd> | [0..*] | | | 115 |
| | **Agent** <Agtr> | [1..1] | ± | | 116 |
| | **ChargeBearer** <ChrgBr> | [0..1] | CodeSet | | 116 |
| | **ChargesAmount** <ChrgsAmt> | [0..1] | Amount | C1, C9 | 117 |
| | **ExchangeRateData** <XchgRateData> | [0..1] | | | 117 |
| | **SourceCurrency** <SrcCcy> | [1..1] | CodeSet | C1 | 118 |
| | **TargetCurrency** <TgtCcy> | [1..1] | CodeSet | C1 | 118 |
| | **ExchangeRate** <XchgRate> | [1..1] | Rate | | 118 |
| | **UnitCurrency** <UnitCcy> | [0..1] | CodeSet | C1 | 118 |
| | **AcceptanceDateTime** <AcceptncDtTm> | [0..1] | DateTime | | 119 |

---

<!-- Page 107 -->

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **AccountServicerReference** `<AcctSvcrRef>` | [0..1] | Text | | 119 |
| | **ClearingSystemReference** `<ClrSysRef>` | [0..1] | Text | | 119 |
| | **OriginalTransactionReference** `<OrgnlTxRef>` | [0..1] | | | 119 |
| | **InterbankSettlementAmount** `<IntrBkSttlmAmt>` | [0..1] | Amount | C2, C8 | 122 |
| | **Amount** `<Amt>` | [0..1] | ± | | 122 |
| | **InterbankSettlementDate** `<IntrBkSttlmDt>` | [0..1] | Date | | 123 |
| | **RequestedCollectionDate** `<ReqdColltnDt>` | [0..1] | Date | | 123 |
| | **RequestedExecutionDate** `<ReqdExctnDt>` | [0..1] | ± | | 123 |
| | **CreditorSchemeIdentification** `<CdrSchmeId>` | [0..1] | ± | | 123 |
| | **SettlementInformation** `<SttlmInf>` | [0..1] | | C17, C18, C25, C26, C27, C28, C33, C34 | 124 |
| | **SettlementMethod** `<SttlmMtd>` | [1..1] | CodeSet | | 126 |
| | **SettlementAccount** `<SttlmAcct>` | [0..1] | ± | C16, C15 | 127 |
| | **ClearingSystem** `<ClrSys>` | [0..1] | | | 127 |
| Or | **Code** `<Cd>` | [1..1] | CodeSet | | 128 |
| Or | **Proprietary** `<Prtry>` | [1..1] | Text | | 128 |
| | **InstructingReimbursementAgent** `<InstrRmbrsmntAgnt>` | [0..1] | ± | | 128 |
| | **InstructingReimbursementAgentAccount** `<InstrRmbrsmntAggtAcct>` | [0..1] | ± | C16, C15 | 129 |
| | **InstructedReimbursementAgent** `<InstdRmbrsmntAggt>` | [0..1] | ± | | 129 |
| | **InstructedReimbursementAgentAccount** `<InstdRmbrsmntAggtAcct>` | [0..1] | ± | C16, C15 | 130 |
| | **ThirdReimbursementAgent** `<ThirdRmbrsmntAggt>` | [0..1] | ± | | 131 |
| | **ThirdReimbursementAgentAccount** `<ThirdRmbrsmntAggtAcct>` | [0..1] | ± | C16, C15 | 131 |
| | **PaymentTypeInformation** `<PmtTpInf>` | [0..1] | ± | | 132 |
| | **PaymentMethod** `<PmtMtd>` | [0..1] | CodeSet | | 133 |
| | **MandateRelatedInformation** `<MndtRltdInf>` | [0..1] | | | 133 |
| Or | **DirectDebitMandate** `<DrctDbtMndt>` | [0..1] | | C3, C4 | 135 |
| | **MandateIdentification** `<MndtId>` | [0..1] | Text | | 137 |

---

<!-- Page 108 -->

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **DateOfSignature** `<DlOfSgntr>` | [0..1] | Date | | 137 |
| | **AmendmentIndicator** `<AmdmntInd>` | [0..1] | Indicator | | 137 |
| | **AmendmentInformationDetails** `<AmdmntInfDtls>` | [0..1] | | | 137 |
| | **OriginalMandateIdentification** `<OrgnlMndtId>` | [0..1] | Text | | 138 |
| | **OriginalCreditorSchemeIdentification** `<OrgnlCdrtrSchmeId>` | [0..1] | ± | | 138 |
| | **OriginalCreditorAgent** `<OrgnlCdrtrAgnt>` | [0..1] | ± | | 139 |
| | **OriginalCreditorAgentAccount** `<OrgnlCdrtrAgtAcct>` | [0..1] | ± | C16, C15 | 140 |
| | **OriginalDebtor** `<OrgnlDbtr>` | [0..1] | ± | | 141 |
| | **OriginalDebtorAccount** `<OrgnlDbtrAcct>` | [0..1] | ± | C16, C15 | 142 |
| | **OriginalDebtorAgent** `<OrgnlDbtrAgnt>` | [0..1] | ± | | 143 |
| | **OriginalDebtorAgentAccount** `<OrgnlDbtrAgntAcct>` | [0..1] | ± | C16, C15 | 144 |
| | **OriginalFinalCollectionDate** `<OrgnlFnClctnDt>` | [0..1] | Date | | 145 |
| | **OriginalFrequency** `<OrgnlFrqcy>` | [0..1] | ± | | 145 |
| | **OriginalReason** `<OrgnlRsn>` | [0..1] | | | 145 |
| Or | **Code** `<Cd>` | [1..1] | CodeSet | | 145 |
| Or | **Proprietary** `<Prtry>` | [1..1] | Text | | 145 |
| | **OriginalTrackingDays** `<OrgnlTrckgDays>` | [0..1] | Text | | 146 |
| | **ElectronicSignature** `<ElctrncSgntr>` | [0..1] | Text | | 146 |
| | **FirstCollectionDate** `<FrstClctnDt>` | [0..1] | Date | | 146 |
| | **FinalCollectionDate** `<FnClctnDt>` | [0..1] | Date | | 146 |
| | **Frequency** `<Frqcy>` | [0..1] | ± | | 146 |
| | **Reason** `<Rsn>` | [0..1] | | | 146 |
| Or | **Code** `<Cd>` | [1..1] | CodeSet | | 147 |
| Or | **Proprietary** `<Prtry>` | [1..1] | Text | | 147 |
| | **TrackingDays** `<TrckgDays>` | [0..1] | Text | | 147 |
| Or | **CreditTransferMandate** `<CdtTrfMndt>` | [0..1] | ± | | 147 |
| | **RemittanceInformation** `<RmtInf>` | [0..1] | ± | | 148 |
| | **UltimateDebtor** `<UltmtDbtr>` | [0..1] | | | 148 |
| Or | **Party** `<Pty>` | [1..1] | ± | | 148 |
| Or | **Agent** `<Agnt>` | [1..1] | ± | | 149 |

---

<!-- Page 109 -->

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **Debitor** `<Dbtr>` | [0..1] | | | 150 |
| (Or | **Party** `<Pty>` | [1..1] | ± | | 150 |
| Or) | **Agent** `<Agt>` | [1..1] | ± | | 151 |
| | **DebitorAccount** `<DbtrAcct>` | [0..1] | ± | C16, C15 | 152 |
| | **DebitorAgent** `<DbtrAgt>` | [0..1] | ± | | 153 |
| | **DebitorAgentAccount** `<DbtrAgtAcct>` | [0..1] | ± | C16, C15 | 153 |
| | **CreditorAgent** `<CdtrAgt>` | [0..1] | ± | | 154 |
| | **CreditorAgentAccount** `<CdtrAgtAcct>` | [0..1] | ± | C16, C15 | 155 |
| | **Creditor** `<Cdtr>` | [0..1] | | | 156 |
| (Or | **Party** `<Pty>` | [1..1] | ± | | 156 |
| Or) | **Agent** `<Agt>` | [1..1] | ± | | 157 |
| | **CreditorAccount** `<CdtrAcct>` | [0..1] | ± | C16, C15 | 158 |
| | **UltimateCreditor** `<UltmCdtr>` | [0..1] | | | 159 |
| (Or | **Party** `<Pty>` | [1..1] | ± | | 159 |
| Or) | **Agent** `<Agt>` | [1..1] | ± | | 160 |
| | **Purpose** `<Purp>` | [0..1] | ± | | 161 |
| | **SupplementaryData** `<SplmtryData>` | [0..*] | ± | C32 | 161 |

### 3.4.3.7.1 StatusIdentification <StsId>

*Presence: [0..1]*

*Definition: Unique identification, as assigned by an instructing party for an instructed party, to unambiguously identify the reported status.*

Usage: The instructing party is the party sending the status message and not the party that sent the original instruction that is being reported on.

*Datatype: "Max35Text" on page 431*

### 3.4.3.7.2 OriginalInstructionIdentification <OrgnlInstrId>

*Presence: [0..1]*

*Definition: Unique identification, as assigned by the original instructing party for the original instructed party, to unambiguously identify the original instruction.*

*Datatype: "Max35Text" on page 431*

### 3.4.3.7.3 OriginalEndToEndIdentification <OrgnlEndToEndId>

*Presence: [0..1]*

---

<!-- Page 110 -->

*Definition:* Unique identification, as assigned by the original initiating party, to unambiguously identify the original transaction.

*Datatype:* "Max35Text" on page 431

### 3.4.3.7.4 OriginalUETR <OrgnUETR>

*Presence:* [0..1]

*Definition:* Universally unique identifier to provide the original end-to-end reference of a payment transaction.

*Datatype:* "UUIDv4Identifier" on page 427

### 3.4.3.7.5 TransactionStatus <TxSts>

*Presence:* [0..1]

*Definition:* Specifies the status of a transaction, as published in an external payment transaction status code list.

*Datatype:* "ExternalPaymentTransactionStatus1Code" on page 418

### 3.4.3.7.6 StatusReasonInformation <StsRsnInf>

*Presence:* [0..*]

*Definition:* Provides detailed information on the status reason.

*Impacted by:* C30 "StatusReasonRule"

StatusReasonInformation <StsRsnInf> contains the following StatusReasonInformation14 elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Originator <Orgtr> | [0..1] | ± | | 110 |
| | Reason <Rsn> | [0..1] | | | 111 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 112 |
| Or) | Proprietary <Prtty> | [1..1] | Text | | 112 |
| | AdditionalInformation <AddtlInf> | [0..*] | Text | | 112 |

**Constraints**

- **StatusReasonRule**

If Reason/Code is equal to NARR, then AdditionalInformation must be present.

On Condition
/Reason/Code is within DataType <<Code>> ValidationRuleNarrative1Code
And /Reason is present
And /Reason/Code is present
Following Must be True
/AdditionalInformation[1] Must be present

#### 3.4.3.7.6.1 Originator <Orgtr>

*Presence:* [0..1]

*Definition:* Party that issues the status.

---

<!-- Page 111 -->

Originator <Orgrt> contains the following elements (see "PartyIdentification272" on page 336 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Name <Nm> | [0..1] | Text | | 337 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 338 |
| | Identification <Id> | [0..1] | | | 338 |
| (Or) | OrganisationIdentification <OrgId> | [1..1] | | | 339 |
| | AnyBIC <AnyBIC> | [0..1] | IdentifierSet | C5 | 340 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 340 |
| | Other <Othr> | [0..*] | | | 340 |
| | Identification <Id> | [1..1] | Text | | 341 |
| | SchemeName <SchmeNm> | [0..1] | | | 341 |
| (Or) | Code <Cd> | [1..1] | CodeSet | | 341 |
| Or | Proprietary <Prtry> | [1..1] | Text | | 341 |
| | Issuer <Issr> | [0..1] | Text | | 341 |
| (Or) | PrivateIdentification <PrvtId> | [1..1] | | | 341 |
| | DateAndPlaceOfBirth <DtAndPlcOfBirth> | [0..1] | | | 342 |
| | BirthDate <BirthDt> | [1..1] | Date | | 342 |
| | ProvinceOfBirth <PrvcOfBirth> | [0..1] | Text | | 342 |
| | CityOfBirth <CityOfBirth> | [1..1] | Text | | 343 |
| | CountryOfBirth <CtryOfBirth> | [1..1] | CodeSet | C7 | 343 |
| | Other <Othr> | [0..*] | | | 343 |
| | Identification <Id> | [1..1] | Text | | 343 |
| | SchemeName <SchmeNm> | [0..1] | | | 343 |
| (Or) | Code <Cd> | [1..1] | CodeSet | | 344 |
| Or | Proprietary <Prtry> | [1..1] | Text | | 344 |
| | Issuer <Issr> | [0..1] | Text | | 344 |
| | CountryOfResidence <CtryOfRes> | [0..1] | CodeSet | C7 | 344 |
| | ContactDetails <CtctDtls> | [0..1] | ± | | 344 |

**3.4.3.7.6.2 Reason <Rsn>**
*Presence:* [0..1]
*Definition:* Specifies the reason for the status report.

---

<!-- Page 112 -->

Reason <Rsn> contains one of the following StatusReason6Choice elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| (Or | Code <Cd> | [1..1] | CodeSet | | 112 |
| Or) | Proprietary <Ptry> | [1..1] | Text | | 112 |

### 3.4.3.7.6.2.1 Code <Cd>

*Presence:* [1..1]

*Definition:* Reason for the status, as published in an external reason code list.

*Datatype:* "ExternalStatusReason1Code" on page 419

### 3.4.3.7.6.2.2 Proprietary <Ptry>

*Presence:* [1..1]

*Definition:* Reason for the status, in a proprietary form.

*Datatype:* "Max35Text" on page 431

### 3.4.3.7.6.3 AdditionalInformation <AddtlInf>

*Presence:* [0..*]

*Definition:* Further details on the status reason.

Usage: Additional information can be used for several purposes such as the reporting of repaired information.

*Datatype:* "Max105Text" on page 429

### 3.4.3.7.7 ChargesInformation <ChrgsInf>

*Presence:* [0..*]

*Definition:* Provides information on the charges related to the processing of the rejection of the instruction.

Usage: This is passed on for information purposes only. Settlement of the charges will be done separately.

ChargesInformation <ChrgsInf> contains the following Charges16 elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Amount <Amt> | [1..1] | Amount | C2, C8 | 112 |
| | Agent <Agt> | [1..1] | ± | | 113 |
| | Type <Tp> | [0..1] | | | 113 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 114 |
| Or) | Proprietary <Ptry> | [1..1] | ± | | 114 |

### 3.4.3.7.7.1 Amount <Amt>

*Presence:* [1..1]

---

<!-- Page 113 -->

*Definition: Transaction charges to be paid by the charge bearer.*
*Impacted by: C2 "ActiveOrHistoricCurrency", C6 "CurrencyAmount"*
*DataType: "ActiveOrHistoricCurrencyAndAmount" on page 407*

## Constraints

- **ActiveOrHistoricCurrency**
  The Currency Code must be registered, or have already been registered. Valid active or historic currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and may be or not be withdrawn on the day the message containing the Currency is exchanged.

- **CurrencyAmount**
  The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
  Note: The decimal separator is a dot.

### 3.4.3.7.7.2 Agent <Agt>

*Presence: [1..1]*
*Definition: Agent that takes the transaction charges or to which the transaction charges are due.*
**Agent <Agt>** contains the following elements (see "BranchAndFinancialInstitutionIdentification6" on page 320 for details)

| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | FinancialInstitutionIdentification <FinInstId> | [1..1] |  |  | 321 |
| | BICFI <BICFI> | [0..1] | IdentifierSet | C6 | 321 |
| | ClearingSystemMemberIdentification <ClrSysMmbId> | [0..1] | ± |  | 322 |
| | LEI <LEI> | [0..1] | IdentifierSet |  | 322 |
| | Name <Nm> | [0..1] | Text |  | 322 |
| | PostalAddress <PstlAdr> | [0..1] | ± |  | 322 |
| | Other <Othr> | [0..1] | ± |  | 323 |
| | BranchIdentification <BrnchId> | [0..1] |  |  | 324 |
| | Identification <Id> | [0..1] | Text |  | 324 |
| | LEI <LEI> | [0..1] | IdentifierSet |  | 324 |
| | Name <Nm> | [0..1] | Text |  | 324 |
| | PostalAddress <PstlAdr> | [0..1] | ± |  | 324 |

### 3.4.3.7.7.3 Type <Tp>

*Presence: [0..1]*
*Definition: Defines the type of charges.*

---

<!-- Page 114 -->

Type <Tp> contains one of the following ChargeType3Choice elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| (Or | Code <Cd> | [1..1] | CodeSet | | 114 |
| Or) | Proprietary <Ptry> | [1..1] | ± | | 114 |

### 3.4.3.7.3.1 Code <Cd>

*Presence:* [1..1]

*Definition:* Charge type, in a coded form.

*DataType:* "ExternalChargeType1Code" on page 414

### 3.4.3.7.3.2 Proprietary <Ptry>

*Presence:* [1..1]

*Definition:* Type of charge in a proprietary form, as defined by the issuer.

Proprietary <Ptry> contains the following elements (see "GenericIdentification3" on page 329 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Identification <Id> | [1..1] | Text | | 329 |
| | Issuer <Issr> | [0..1] | Text | | 329 |

### 3.4.3.7.8 TrackerData <TrckrData>

*Presence:* [0..1]

*Definition:* Provides information on the tracking of the interbank transaction related to the payment.

TrackerData <TrckrData> contains the following TrackerData7 elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | ConfirmedDate <ConfmD> | [1..1] | ± | | 115 |
| | ConfirmedAmount <ConfmAmt> | [1..1] | Amount | C1, C9 | 115 |
| | TrackerRecord <TrckrRcrd> | [1..1] | | | 115 |
| | Agent <Agnt> | [1..1] | ± | | 116 |
| | ChargeBearer <ChrgBr> | [0..1] | CodeSet | | 116 |
| | ChargesAmount <ChrgsAmt> | [0..1] | Amount | C1, C9 | 117 |
| | ExchangeRateData <XchgRateData> | [0..1] | | | 117 |
| | SourceCurrency <SrcCcy> | [1..1] | CodeSet | C1 | 118 |
| | TargetCurrency <TgtCcy> | [1..1] | CodeSet | C1 | 118 |
| | ExchangeRate <XchgRate> | [1..1] | Rate | | 118 |
| | UnitCurrency <UnitCcy> | [0..1] | CodeSet | C1 | 118 |

---

<!-- Page 115 -->

### 3.4.3.7.8.1 ConfirmedDate <ConfDtd>

*Presence:* [1..1]

*Definition:* Point in time when an update to the tracking system has been confirmed.

Usage:

This date can be the point in time when an agent provides a pending status update to the tracking system or when the creditor has been credited and can use the amount of money (as confirmed to the tracking system by the creditor agent).

**ConfirmedDate <ConfDtd>** contains one of the following elements (see *DateAndDateTime2Choice* on page 316 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| (Or | Date <Dt> | [1..1] | Date | | 317 |
| Or) | DateTime <DtTm> | [1..1] | DateTime | | 317 |

### 3.4.3.7.8.2 ConfirmedAmount <ConfdAmt>

*Presence:* [1..1]

*Definition:* Amount of money confirmed to the tracking system by the agent.

*Impacted by:* C1 "ActiveCurrency", C9 "CurrencyAmount"

*Datatype:* "ActiveCurrencyAndAmount" on page 407

**Constraints**

* **ActiveCurrency**

  The currency code must be a valid active currency code, not yet withdrawn, on the day the message containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day the message containing the Currency is exchanged.

* **CurrencyAmount**

  The number of fractional digits (or minor unit of currency) must comply with ISO 4217.

  Note: The decimal separator is a dot.

### 3.4.3.7.8.3 TrackerRecord <TrkrRcrd>

*Presence:* [1..*]

*Definition:* Provides tracker transaction information for a specific agent involved in the transaction chain.

---

<!-- Page 116 -->

TrackerRecord <TrkrRcrd> contains the following TrackerRecord5 elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **Agent** <Agtr> | [1..1] | ± | | 116 |
| | **ChargeBearer** <ChrgBr> | [0..1] | CodeSet | | 116 |
| | **ChargesAmount** <ChrgsAmt> | [0..1] | Amount | C1, C9 | 117 |
| | **ExchangeRateData** <XchgRateData> | [0..1] | | | 117 |
| | **SourceCurrency** <SrcCcy> | [1..1] | CodeSet | C1 | 118 |
| | **TargetCurrency** <TrgtCcy> | [1..1] | CodeSet | C1 | 118 |
| | **ExchangeRate** <XchgRate> | [1..1] | Rate | | 118 |
| | **UnitCurrency** <UnitCcy> | [0..1] | CodeSet | C1 | 118 |

### 3.4.3.7.8.3.1 Agent <Agtr>

*Presence: [1..1]*

*Definition: Identification of an agent in the tracker.*

**Agent <Agtr>** contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on page 320 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | FinancialInstitutionIdentification <FinInstlId> | [1..1] | | | 321 |
| | BICFI <BICFI> | [0..1] | IdentifierSet | C6 | 321 |
| | ClearingSystemMemberIdentification <ClrSysMmbId> | [0..1] | ± | | 322 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 322 |
| | Name <Nm> | [0..1] | Text | | 322 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 322 |
| | Other <Othr> | [0..1] | ± | | 323 |
| | BranchIdentification <BrnchId> | [0..1] | | | 324 |
| | Identification <Id> | [0..1] | Text | | 324 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 324 |
| | Name <Nm> | [0..1] | Text | | 324 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 324 |

### 3.4.3.7.8.3.2 ChargeBearer <ChrgBr>

*Presence: [0..1]*

*Definition: Specifies which party/parties will bear the charges associated with the processing of the payment transaction.*

*Datatype: "ChargeBearerType1Code" on page 410*

---

<!-- Page 117 -->

| CodeName | Name | Definition |
| :--- | :--- | :--- |
| DEBT | BorneByDebtor | All transaction charges are to be borne by the debtor. |
| CRED | BorneByCreditor | All transaction charges are to be borne by the creditor. |
| SHAR | Shared | In a credit transfer context, means that transaction charges on the sender side are to be borne by the debtor, transaction charges on the receiver side are to be borne by the creditor. In a direct debit context, means that transaction charges on the sender side are to be borne by the creditor, transaction charges on the receiver side are to be borne by the debtor. |
| SLEV | FollowingServiceLevel | Charges are to be applied following the rules agreed in the service level and/or scheme. |

### 3.4.3.7.8.3.3 ChargesAmount <ChrgAmt>

*Presence:* [0..1]

*Definition:* Transaction charges to be paid by the charge bearer.

*Impacted by:* C1 "ActiveCurrency", C9 "CurrencyAmount"

*Datatype:* "ActiveCurrencyAndAmount" on page 407

**Constraints**

- **ActiveCurrency**

The currency code must be a valid active currency code, not yet withdrawn on the day the message containing the currency is exchanged. Valid active currency codes are registered on the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day the message containing the Currency is exchanged.

- **CurrencyAmount**

The number of fractional digits (or minor unit of currency) must comply with ISO 4217.

Note: The decimal separator is a dot.

### 3.4.3.7.8.3.4 ExchangeRateData <XchgRateData>

*Presence:* [0..1]

*Definition:* Provides details of the rate and the currencies used in the foreign exchange.

---

<!-- Page 118 -->

ExchangeRateData <XchgRateData> contains the following **CurrencyExchange13** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | **SourceCurrency** <SrcCcy> | [1..1] | CodeSet | C1 | 118 |
| | **TargetCurrency** <TrgtCcy> | [1..1] | CodeSet | C1 | 118 |
| | **ExchangeRate** <XchgRate> | [1..1] | Rate | | 118 |
| | **UnitCurrency** <UnitCcy> | [0..1] | CodeSet | C1 | 118 |

### 3.4.3.7.8.3.4.1 SourceCurrency <SrcCcy>

*Presence:* [1..1]

*Definition:* Currency from which an amount is to be converted in a currency conversion.

*Impacted by:* C1 "ActiveCurrency"

*Datatype:* "ActiveCurrencyCode" on page 408

**Constraints**

- **ActiveCurrency**

The currency code must be a valid active currency code, not yet withdrawn on the day the message containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day the message containing the Currency is exchanged.

### 3.4.3.7.8.3.4.2 TargetCurrency <TrgtCcy>

*Presence:* [1..1]

*Definition:* Currency into which an amount is to be converted in a currency conversion.

*Impacted by:* C1 "ActiveCurrency"

*Datatype:* "ActiveCurrencyCode" on page 408

**Constraints**

- **ActiveCurrency**

The currency code must be a valid active currency code, not yet withdrawn on the day the message containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day the message containing the Currency is exchanged.

### 3.4.3.7.8.3.4.3 ExchangeRate <XchgRate>

*Presence:* [1..1]

*Definition:* Factor used to convert an amount from one currency into another. This reflects the price at which one currency was bought with another currency.

*Datatype:* "BaseOneRate" on page 428

### 3.4.3.7.8.3.4.4 UnitCurrency <UnitCcy>

*Presence:* [0..1]

---

<!-- Page 119 -->

*Definition:* Currency in which the rate of exchange is expressed in a currency exchange. In the example 1GBP = xxxCUR, the unit currency is GBP.

*Impacted by:* C1 "ActiveCurrency"

*Datatype:* "ActiveCurrencyCode" on page 408

**Constraints**

* **ActiveCurrency**

The currency code must be a valid active currency code, not yet withdrawn on the day the message containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day the message containing the Currency is exchanged.

### 3.4.3.7.9 AcceptanceDateTime <AcceptncDtTm>

*Presence:* [0..1]

*Definition:* Point in time when the payment order from the initiating party meets the processing conditions of the account servicing agent. This means that the account servicing agent has received the payment order and has applied checks such as authorisation, availability of funds.

*Datatype:* "ISODateTime" on page 425

### 3.4.3.7.10 AccountServicerReference <AcctSvcrRef>

*Presence:* [0..1]

*Definition:* Unique reference, as assigned by the account servicing institution, to unambiguously identify the instruction.

*Datatype:* "Max35Text" on page 431

### 3.4.3.7.11 ClearingSystemReference <ClrSysRef>

*Presence:* [0..1]

*Definition:* Unique reference, as assigned by a clearing system, to unambiguously identify the instruction.

*Datatype:* "Max35Text" on page 431

### 3.4.3.7.12 OriginalTransactionReference <OrgnlTxRef>

*Presence:* [0..1]

*Definition:* Key elements used to identify the original transaction that is being referred to.

---

<!-- Page 120 -->

OriginalTransactionReference <OrgnlTxRef> contains the following
OriginalTransactionReference42 elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | InterbankSettlementAmount <IntkBkSttlmAmt> | [0..1] | Amount | C2, C8 | 122 |
| | Amount <Amt> | [0..1] | ± | | 122 |
| | InterbankSettlementDate <IntkBkSttlmDt> | [0..1] | Date | | 123 |
| | RequestedCollectionDate <ReqdColltnDt> | [0..1] | Date | | 123 |
| | RequestedExecutionDate <ReqdExctnDt> | [0..1] | ± | | 123 |
| | CreditorScheduleIdentification <CdtrSchmeId> | [0..1] | ± | | 123 |
| | SettlementInformation <SttlmInf> | [0..1] | | C17, C18, C25, C26, C27, C28, C33, C34 | 124 |
| | SettlementMethod <SttlmMtd> | [1..1] | CodeSet | | 126 |
| | SettlementAccount <SttlmAcc> | [0..1] | ± | C16, C15 | 127 |
| | ClearingSystem <ClrSys> | [0..1] | | | 127 |
| Or | Code <Cd> | [1..1] | CodeSet | | 128 |
| Or | Proprietary <Prtry> | [1..1] | Text | | 128 |
| | InstructingReimbursementAgent <InstdRmbrmntAg> | [0..1] | ± | | 128 |
| | InstructingReimbursementAgentAccount <InstdRmbrmntAgAcct> | [0..1] | ± | C16, C15 | 129 |
| | InstructedReimbursementAgent <InstdRmbrmntAg> | [0..1] | ± | | 129 |
| | InstructedReimbursementAgentAccount <InstdRmbrmntAgAcct> | [0..1] | ± | C16, C15 | 130 |
| | ThirdReimbursementAgent <ThrdRmbrmntAg> | [0..1] | ± | | 131 |
| | ThirdReimbursementAgentAccount <ThrdRmbrmntAgAcct> | [0..1] | ± | C16, C15 | 131 |
| | PaymentTypeInformation <PmtTpInf> | [0..1] | ± | | 132 |
| | PaymentMethod <PmtMtd> | [0..1] | CodeSet | | 133 |
| | MandateRelatedInformation <MndtRltdInf> | [0..1] | | | 133 |
| Or | DirectDebitMandate <DrctDbtMndt> | [0..1] | | C3, C4 | 135 |
| | MandateIdentification <MndtId> | [0..1] | Text | | 137 |
| | DateOfSignature <DtOfSgntr> | [0..1] | Date | | 137 |
| | AmendmentIndicator <AmdmntInd> | [0..1] | Indicator | | 137 |

---

<!-- Page 121 -->

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **AmendmentInformationDetails** <AmndmntInfDtls> | [0..1] | | | 137 |
| | **OriginalMandateIdentification** <OrgnlMndtdId> | [0..1] | Text | | 138 |
| | **OriginalCreditorSchemeIdentification** <OrgnlCddtrSchmeId> | [0..1] | ± | | 138 |
| | **OriginalCreditorAgent** <OrgnlCddtrAgnt> | [0..1] | ± | | 139 |
| | **OriginalCreditorAgentAccount** <OrgnlCddtrAgntAcct> | [0..1] | ± | C16, C15 | 140 |
| | **OriginalDebtor** <OrgnlDbtr> | [0..1] | ± | | 141 |
| | **OriginalDebtorAccount** <OrgnlDbtrAcct> | [0..1] | ± | C16, C15 | 142 |
| | **OriginalDebtorAgent** <OrgnlDbtrAgnt> | [0..1] | ± | | 143 |
| | **OriginalDebtorAgentAccount** <OrgnlDbtrAgntAcct> | [0..1] | ± | C16, C15 | 144 |
| | **OriginalFinalCollectionDate** <OrgnlFinlColltnDt> | [0..1] | Date | | 145 |
| | **OriginalFrequency** <OrgnlFrcqcy> | [0..1] | ± | | 145 |
| | **OriginalReason** <OrgnlRsn> | [0..1] | | | 145 |
| (Or | **Code** <Cd> | [1..1] | CodeSet | | 145 |
| Or) | **Proprietary** <Prtry> | [1..1] | Text | | 145 |
| | **OriginalTrackingDays** <OrgnlTrckgDays> | [0..1] | Text | | 146 |
| | **ElectronicSignature** <ElctrncSgntr> | [0..1] | Text | | 146 |
| | **FirstCollectionDate** <FrstColltnDt> | [0..1] | Date | | 146 |
| | **FinalCollectionDate** <FinlColltnDt> | [0..1] | Date | | 146 |
| | **Frequency** <Frcqcy> | [0..1] | ± | | 146 |
| | **Reason** <Rsn> | [0..1] | | | 146 |
| (Or | **Code** <Cd> | [1..1] | CodeSet | | 147 |
| Or) | **Proprietary** <Prtry> | [1..1] | Text | | 147 |
| | **TrackingDays** <TrckgDays> | [0..1] | Text | | 147 |
| Or | **CreditTransferMandate** <CdtTrfMndt> | [0..1] | ± | | 147 |
| | **RemittanceInformation** <RmtdInf> | [0..1] | ± | | 148 |
| | **UltimateDebtor** <UltmtDbtr> | [0..1] | | | 148 |
| (Or | **Party** <Pty> | [1..1] | ± | | 148 |
| Or) | **Agent** <Agnt> | [1..1] | ± | | 149 |
| | **Debtor** <Dbtr> | [0..1] | | | 150 |
| (Or | **Party** <Pty> | [1..1] | ± | | 150 |

---

<!-- Page 122 -->

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| Or | **Agent** `<Agtr>` | [1..1] | ± | | 151 |
| | DebtorAccount `<DbtrAcct>` | [0..1] | ± | C16, C15 | 152 |
| | DebtorAgent `<DbtrAgtr>` | [0..1] | ± | | 153 |
| | DebtorAgentAccount `<DbtrAgtrAcct>` | [0..1] | ± | C16, C15 | 153 |
| | CreditorAgent `<CdtrAgtr>` | [0..1] | ± | | 154 |
| | CreditorAgentAccount `<CdtrAgtrAcct>` | [0..1] | ± | C16, C15 | 155 |
| | Creditor `<Cdtr>` | [0..1] | | | 156 |
| (Or | **Party** `<Pty>` | [1..1] | ± | | 156 |
| Or) | **Agent** `<Agtr>` | [1..1] | ± | | 157 |
| | CreditorAccount `<CdtrAcct>` | [0..1] | ± | C16, C15 | 158 |
| | UltimateCreditor `<UltmCdtr>` | [0..1] | | | 159 |
| (Or | **Party** `<Pty>` | [1..1] | ± | | 159 |
| Or) | **Agent** `<Agtr>` | [1..1] | ± | | 160 |
| | Purpose `<Purp>` | [0..1] | ± | | 161 |

### 3.4.3.7.12.1 InterbankSettlementAmount <IntrBkSttlmAmt>

*Presence: [0..1]*

*Definition: Amount of money moved between the instructing agent and the instructed agent.*

*Impacted by: C2 "ActiveOrHistoricCurrency", C8 "CurrencyAmount"*

*Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 407*

**Constraints**

*   **ActiveOrHistoricCurrency**

    The Currency Code must be registered, or have already been registered. Valid active or historic currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and may be or not be withdrawn on the day the message containing the Currency is exchanged.

*   **CurrencyAmount**

    The number of fractional digits (or minor unit of currency) must comply with ISO 4217.

Note: The decimal separator is a dot.

### 3.4.3.7.12.2 Amount <Amt>

*Presence: [0..1]*

---

<!-- Page 123 -->

Definition: Amount of money to be moved between the debtor and creditor, before deduction of charges, expressed in the currency as ordered by the initiating party.

**Amount** `<Amt>` contains one of the following elements (see "AmountType4Choice" on page 314 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| (Or | InstructedAmount `<InstdAmt>` | [1..1] | Amount | C2, C8 | 314 |
| Or) | EquivalentAmount `<EqvIAmt>` | [1..1] | | | 315 |
| | Amount `<Amt>` | [1..1] | Amount | C2, C8 | 315 |
| | CurrencyOfTransfer `<CcyOfTrf>` | [1..1] | CodeSet | C2 | 315 |

### 3.4.3.7.12.3 InterbankSettlementDate `<IntrBkSttlmDt>`

Presence: [0..1]

Definition: Date on which the amount of money ceases to be available to the agent that owes it and when the amount of money becomes available to the agent to which it is due.

Datatype: "ISODate" on page 425

### 3.4.3.7.12.4 RequestedCollectionDate `<ReqdColltnDt>`

Presence: [0..1]

Definition: Date and time at which the creditor requests that the amount of money is to be collected from the debtor.

Datatype: "ISODate" on page 425

### 3.4.3.7.12.5 RequestedExecutionDate `<ReqdExctnDt>`

Presence: [0..1]

Definition: Date at which the initiating party requests the clearing agent to process the payment.

Usage: This is the date on which the debtor's account is to be debited. If payment by cheque, the date when the cheque must be generated by the bank.

**RequestedExecutionDate** `<ReqdExctnDt>` contains one of the following elements (see "DateAndDateTime2Choice" on page 316 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| (Or | Date `<Dt>` | [1..1] | Date | | 317 |
| Or) | DateTime `<DtTm>` | [1..1] | DateTime | | 317 |

### 3.4.3.7.12.6 CreditorSchemeIdentification `<CdtrSchmeId>`

Presence: [0..1]

Definition: Credit party that signs the mandate.

---

<!-- Page 124 -->

**CreditorSchemeIdentification** `<CddrSchmd>` contains the following elements (see *PartyIdentification27* on page 336 for details)



| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Name `<Nm>` | [0..1] | Text | | 337 |
| | PostalAddress `<PstlAdr>` | [0..1] | ± | | 338 |
| | Identification `<Id>` | [0..1] | | | 338 |
| (Or | OrganisationIdentification `<OrgId>` | [1..1] | | | 339 |
| | AnyBIC `<AnyBIC>` | [0..1] | IdentifierSet | C5 | 340 |
| | LEI `<LEI>` | [0..1] | IdentifierSet | | 340 |
| | Other `<Othr>` | [0..*] | | | 340 |
| | Identification `<Id>` | [1..1] | Text | | 341 |
| | SchemeName `<SchmeNm>` | [0..1] | | | 341 |
| (Or | Code `<Cd>` | [1..1] | CodeSet | | 341 |
| Or | Proprietary `<Prtry>` | [1..1] | Text | | 341 |
| | Issuer `<Issr>` | [0..1] | Text | | 341 |
| (Or | PrivateIdentification `<PrvtId>` | [1..1] | | | 341 |
| | DateAndPlaceOfBirth `<DtAndPlcOfBirth>` | [0..1] | | | 342 |
| | BirthDate `<BirthDt>` | [1..1] | Date | | 342 |
| | ProvinceOfBirth `<PrvcOfBirth>` | [0..1] | Text | | 342 |
| | CityOfBirth `<CityOfBirth>` | [1..1] | Text | | 343 |
| | CountryOfBirth `<CtryOfBirth>` | [1..1] | CodeSet | C7 | 343 |
| | Other `<Othr>` | [0..*] | | | 343 |
| | Identification `<Id>` | [1..1] | Text | | 343 |
| | SchemeName `<SchmeNm>` | [0..1] | | | 343 |
| (Or | Code `<Cd>` | [1..1] | CodeSet | | 344 |
| Or | Proprietary `<Prtry>` | [1..1] | Text | | 344 |
| | Issuer `<Issr>` | [0..1] | Text | | 344 |
| | CountryOfResidence `<CtryOfRes>` | [0..1] | CodeSet | C7 | 344 |
| | ContactDetails `<CtctDtls>` | [0..1] | ± | | 344 |

### 3.4.3.7.12.7 SettlementInformation <SttlmInf>

Presence: [0..1]

*Definition:* Specifies the details on how the settlement of the original transaction(s) between the instructing agent and the instructed agent was completed.

---

<!-- Page 125 -->

Impacted by: C17 "InstructedReimbursementAgentAccountRule", C18
"InstructingReimbursementAgentAccountRule", C25 "SettlementMethodAgentRule", C26
"SettlementMethodClearingRule", C27 "SettlementMethodCoverAgentRule", C28
"SettlementMethodCoverRule", C33 "ThirdReimbursementAgentAccountRule", C34
"ThirdReimbursementAgentRule"

SettlementInformation <SttlmInf> contains the following SettlementInstruction15 elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | **SettlementMethod** *<SttlmMtd>* | [1..1] | CodeSet | | 126 |
| | **SettlementAccount** *<SttlmAcct>* | ± | | C16, C15 | 127 |
| | **ClearingSystem** *<ClrSys>* | [0..1] | | | 127 |
| <span style="color:red">Or</span> | **Code** *<Cd>* | [1..1] | CodeSet | | 128 |
| <span style="color:red">Or</span> | **Proprietary** *<Prtry>* | [1..1] | Text | | 128 |
| | **InstructingReimbursementAgent** *<InstrgRmbrsmtAgg>* | [0..1] | ± | | 128 |
| | **InstructingReimbursementAgentAccount** *<InstrgRmbrsmtAggAcct>* | [0..1] | ± | C16, C15 | 129 |
| | **InstructedReimbursementAgent** *<InstdRmbrsmtAgg>* | [0..1] | ± | | 129 |
| | **InstructedReimbursementAgentAccount** *<InstdRmbrsmtAggAcct>* | [0..1] | ± | C16, C15 | 130 |
| | **ThirdReimbursementAgent** *<ThirdRmbrsmtAgg>* | [0..1] | ± | | 131 |
| | **ThirdReimbursementAgentAccount** *<ThirdRmbrsmtAggAcct>* | [0..1] | ± | C16, C15 | 131 |

## Constraints

*   **InstructedReimbursementAgentAccountRule**

    If InstructedReimbursementAgentAccount is present, then InstructedReimbursementAgent must be present.

    ```text
    On Condition
    /InstructedReimbursementAgent Is absent
    Following Must be True
    /InstructedReimbursementAgentAccount Must be absent
    ```

*   **InstructingReimbursementAgentAccountRule**

    If InstructingReimbursementAgentAccount is present, then InstructingReimbursementAgent must be present.

    ```text
    On Condition
    /InstructingReimbursementAgent Is absent
    Following Must be True
    /InstructingReimbursementAgentAccount Must be absent
    ```

*   **SettlementMethodAgentRule**

    If SettlementMethod is equal to INDA or INGA, then ReimbursementAgent(s) and ClearingSystem are not allowed.

    ```text
    On Condition
    /SettlementMethod Is equal to value 'InstructingAgent'
    Or    /SettlementMethod Is equal to value 'InstructedAgent'
    ```

---

<!-- Page 126 -->

Following Must be True
/ClearingSystem Must be absent
And /InstructingReimbursementAgent Must be absent
And /InstructedReimbursementAgent Must be absent
And /ThirdReimbursementAgent Must be absent

* **SettlementMethodClearingRule**

If SettlementMethod is equal to CLRG, then SettlementAccount and ReimbursementAgent(s) are not allowed.

On Condition
/SettlementMethod is equal to value 'ClearingSystem'
Following Must be True
/SettlementAccount Must be absent
And /InstructingReimbursementAgent Must be absent
And /InstructedReimbursementAgent Must be absent
And /ThirdReimbursementAgent Must be absent

* **SettlementMethodCoverAgentRule**

If SettlementMethod is equal to COVE, then InstructedReimbursementAgent or InstructingReimbursementAgent must be present.

On Condition
/SettlementMethod is equal to value 'CoverMethod'
Following Must be True
/InstructingReimbursementAgent Must be present
Or /InstructedReimbursementAgent Must be present

* **SettlementMethodCoverRule**

If SettlementMethod is equal to COVE, then SettlementAccount and ClearingSystem are not allowed.

On Condition
/SettlementMethod is equal to value 'CoverMethod'
Following Must be True
/SettlementAccount Must be absent
And /ClearingSystem Must be absent

* **ThirdReimbursementAgentAccountRule**

If ThirdReimbursementAgentAccount is present, then ThirdReimbursementAgent must be present.

On Condition
/ThirdReimbursementAgent is absent
Following Must be True
/ThirdReimbursementAgentAccount Must be absent

* **ThirdReimbursementAgentRule**

If ThirdReimbursementAgent is present, then InstructingReimbursementAgent and InstructedReimbursementAgent must both be present.

On Condition
/ThirdReimbursementAgent is present
Following Must be True
/InstructingReimbursementAgent Must be present
And /InstructedReimbursementAgent Must be present

**3.4.3.7.12.7.1 SettlementMethod <SttlmMtd>**

*Presence:* [1..1]

*Definition:* Method used to settle the (batch of) payment instructions.

*Datatype:* "SettlementMethod1Code" on page 423

---

<!-- Page 127 -->

| CodeName | Name | Definition |
|---|---|---|
| INDA | InstructedAgent | Settlement is done by the agent instructed to execute a payment instruction. |
| INGA | InstructingAgent | Settlement is done by the agent instructing and forwarding the payment to the next party in the payment chain. |
| COVE | CoverMethod | Settlement is done through a cover payment. |
| CLRG | ClearingSystem | Settlement is done through a payment clearing system. |

## 3.4.3.7.12.7.2 SettlementAccount <SttlmAcc>

*Presence:* [0..1]

*Definition:* A specific purpose account used to post debit and credit entries as a result of the transaction.

*Impacted by:* C16 "IdentificationOrProxyPresenceRule", C15 "IdentificationAndProxyGuideline"

**SettlementAccount <SttlmAcc>** contains the following elements (see "CashAccount40" on page 309 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Identification <Id> | [0..1] | ± | | 310 |
| | Type <Tp> | [0..1] | ± | | 310 |
| | Currency <Ccy> | [0..1] | CodeSet | C2 | 310 |
| | Name <Nm> | [0..1] | Text | | 311 |
| | Proxy <Prxy> | [0..1] | ± | | 311 |

### Constraints

- **IdentificationAndProxyGuideline**

  If the account identification is not defined through a conventional identification such as an email address or a mobile number, then the proxy element should be used for the identification of the account.

- **IdentificationOrProxyPresenceRule**

  Identification must be present or Proxy must be present. Both may be present.

  ```
  Following Must be True
  /Identification Must be present
  Or    /Proxy Must be present
  ```

## 3.4.3.7.12.7.3 ClearingSystem <ClrSys>

*Presence:* [0..1]

*Definition:* Specification of a pre-agreed offering between clearing agents or the channel through which the payment instruction is processed.

---

<!-- Page 128 -->

ClearingSystem <ClrSys> contains one of the following ClearingSystemIdentification3Choice elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| (Or | Code <Cd> | [1..1] | CodeSet | | 128 |
| Or) | Proprietary <Prtry> | [1..1] | Text | | 128 |

### 3.4.3.7.12.7.3.1 Code <Cd>

*Presence:* [1..1]

*Definition:* Infrastructure through which the payment instruction is processed, as published in an external clearing system identification code list.

*Datatype:* "ExternalCashClearingSystem1Code" on page 414

### 3.4.3.7.12.7.3.2 Proprietary <Prtry>

*Presence:* [1..1]

*Definition:* Clearing system identification in a proprietary form.

*Datatype:* "Max35Text" on page 431

### 3.4.3.7.12.7.4 InstructingReimbursementAgent <InstrgRmbrmntAg>

*Presence:* [0..1]

*Definition:* Agent through which the instructing agent will reimburse the instructed agent.

Usage: If InstructingAgent and InstructedAgent have the same reimbursement agent, then only InstructingReimbursementAgent must be used.

**InstructingReimbursementAgent <InstrgRmbrmntAg>** contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on page 320 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | FinancialInstitutionIdentification <FinInstlId> | [1..1] | | | 321 |
| | BICFI <BICFI> | [0..1] | IdentifierSet | C6 | 321 |
| | ClearingSystemMemberIdentification <ClrSysMmbId> | [0..1] | ± | | 322 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 322 |
| | Name <Nm> | [0..1] | Text | | 322 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 322 |
| | Other <Othr> | [0..1] | ± | | 323 |
| | BranchIdentification <BrnchId> | [0..1] | | | 324 |
| | Identification <Id> | [0..1] | Text | | 324 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 324 |
| | Name <Nm> | [0..1] | Text | | 324 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 324 |

---

<!-- Page 129 -->

### 3.4.3.7.12.7.5 InstructingReimbursementAgentAccount <InstrgRmbrsmntAgtAcct>

Presence: [0..1]

*Definition: Unambiguous identification of the account of the instructing reimbursement agent account at its servicing agent in the payment chain.*

*Impacted by: C16 "IdentificationOrProxyPresenceRule", C15 "IdentificationAndProxyGuideline"*

**InstructingReimbursementAgentAccount <InstrgRmbrsmntAgtAcct>** contains the following elements (see "CashAccount40" on page 309 for details)



| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | Identification <Ids> | [0..1] | ± | | 310 |
| | Type <Tp> | [0..1] | ± | | 310 |
| | Currency <Ccy> | [0..1] | CodeSet | C2 | 310 |
| | Name <Nm> | [0..1] | Text | | 311 |
| | Proxy <Prxy> | [0..1] | ± | | 311 |

**Constraints**

- **IdentificationAndProxyGuideline**

  If the account identification is not defined through a conventional identification such as an email address or a mobile number, then the proxy element should be used for the identification of the account.

- **IdentificationOrProxyPresenceRule**

  Identification must be present or Proxy must be present. Both may be present.

  ```
  Following Must be True
  /Identification Must be present
  Or
  /Proxy Must be present
  ```

### 3.4.3.7.12.7.6 InstructedReimbursementAgent <InstdRmbrsmntAgt>

Presence: [0..1]

*Definition: Agent at which the instructed agent will be reimbursed.*

Usage: If InstructedReimbursementAgent contains a branch of the InstructedAgent, then the party in InstructedAgent will claim reimbursement from that branch/will be paid by that branch.

Usage: If InstructingAgent and InstructedAgent have the same reimbursement agent, then only InstructingReimbursementAgent must be used.

---

<!-- Page 130 -->

InstructedReimbursementAgent <InstdRmbrmntAg> contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on page 320 for details)



<table>
  <tr>
    <th>Or</th>
    <th>MessageElement&lt;XML Tag&gt;</th>
    <th>Mult.</th>
    <th>Type</th>
    <th>Constr. No.</th>
    <th>Page</th>
  </tr>
  <tr>
    <td></td>
    <td>FinancialInstitutionIdentification &lt;FinInstlId&gt;</td>
    <td>[1..1]</td>
    <td></td>
    <td></td>
    <td>321</td>
  </tr>
  <tr>
    <td></td>
    <td>BICFI &lt;BICFI&gt;</td>
    <td>[0..1]</td>
    <td>IdentifierSet</td>
    <td>C6</td>
    <td>321</td>
  </tr>
  <tr>
    <td></td>
    <td>ClearingSystemMemberIdentification &lt;ClrSysMmbId&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>322</td>
  </tr>
  <tr>
    <td></td>
    <td>LEI &lt;LEI&gt;</td>
    <td>[0..1]</td>
    <td>IdentifierSet</td>
    <td></td>
    <td>322</td>
  </tr>
  <tr>
    <td></td>
    <td>Name &lt;Nm&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>322</td>
  </tr>
  <tr>
    <td></td>
    <td>PostalAddress &lt;PstlAdr&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>322</td>
  </tr>
  <tr>
    <td></td>
    <td>Other &lt;Othr&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>323</td>
  </tr>
  <tr>
    <td></td>
    <td>BranchIdentification &lt;BrnchId&gt;</td>
    <td>[0..1]</td>
    <td></td>
    <td></td>
    <td>324</td>
  </tr>
  <tr>
    <td></td>
    <td>Identification &lt;Id&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>324</td>
  </tr>
  <tr>
    <td></td>
    <td>LEI &lt;LEI&gt;</td>
    <td>[0..1]</td>
    <td>IdentifierSet</td>
    <td></td>
    <td>324</td>
  </tr>
  <tr>
    <td></td>
    <td>Name &lt;Nm&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>324</td>
  </tr>
  <tr>
    <td></td>
    <td>PostalAddress &lt;PstlAdr&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>324</td>
  </tr>
</table>

### 3.4.3.7.12.7 InstructedReimbursementAgentAccount <InstdRmbrmntAgtAcct>

Presence: [0..1]

Definition: Unambiguous identification of the account of the instructed reimbursement agent account at its servicing agent in the payment chain.

Impacted by: C16 "IdentificationOrProxyPresenceRule", C15 "IdentificationAndProxyGuideline"

InstructedReimbursementAgentAccount <InstdRmbrmntAgAcct> contains the following elements (see "CashAccount40" on page 309 for details)



<table>
  <tr>
    <th>Or</th>
    <th>MessageElement&lt;XML Tag&gt;</th>
    <th>Mult.</th>
    <th>Type</th>
    <th>Constr. No.</th>
    <th>Page</th>
  </tr>
  <tr>
    <td></td>
    <td>Identification &lt;Id&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>310</td>
  </tr>
  <tr>
    <td></td>
    <td>Type &lt;Tp&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>310</td>
  </tr>
  <tr>
    <td></td>
    <td>Currency &lt;Ccy&gt;</td>
    <td>[0..1]</td>
    <td>CodeSet</td>
    <td>C2</td>
    <td>310</td>
  </tr>
  <tr>
    <td></td>
    <td>Name &lt;Nm&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>311</td>
  </tr>
  <tr>
    <td></td>
    <td>Proxy &lt;Prxy&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>311</td>
  </tr>
</table>

---

<!-- Page 131 -->

Constraints

*   **IdentificationAndProxyGuideline**

    If the account identification is not defined through a conventional identification such as an email address or a mobile number, then the proxy element should be used for the identification of the account.

*   **IdentificationOrProxyPresenceRule**

    Identification must be present or Proxy must be present. Both may be present.

    ```text
    Following Must be True
    Or /Identification Must be present
    /Proxy Must be present
    ```

### 3.4.3.7.12.7.8 ThirdReimbursementAgent <ThrdRmbrsmntAg>

*Presence:* [0..1]

*Definition:* Agent at which the instructed agent will be reimbursed.

*Usage:* If ThirdReimbursementAgent contains a branch of the InstructedAgent, then the party in InstructedAgent will claim reimbursement from that branch/will be paid by that branch.

**ThirdReimbursementAgent <ThrdRmbrsmntAg>** contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on page 320 for details)



| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | FinancialInstitutionIdentification <FinInstnId> | [1..1] | | | 321 |
| | BICFI <BICFI> | [0..1] | IdentifierSet | C6 | 321 |
| | ClearingSystemMemberIdentification <ClrSysMmbId> | [0..1] | ± | | 322 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 322 |
| | Name <Nm> | [0..1] | Text | | 322 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 322 |
| | Other <Othr> | [0..1] | ± | | 323 |
| | BranchIdentification <BrnchId> | [0..1] | | | 324 |
| | Identification <Id> | [0..1] | Text | | 324 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 324 |
| | Name <Nm> | [0..1] | Text | | 324 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 324 |

### 3.4.3.7.12.7.9 ThirdReimbursementAgentAccount <ThrdRmbrsmntAg tAcct>

*Presence:* [0..1]

*Definition:* Unambiguous identification of the account of the third reimbursement agent account at its servicing agent in the payment chain.

*Impacted by:* C16 "IdentificationOrProxyPresenceRule", C15 "IdentificationAndProxyGuideline"

---

<!-- Page 132 -->

ThirdReimbursementAgentAccount <ThrdRmbrmntAgtAcc> contains the following elements (see "CashAccount40" on page 309 for details)



<table>
  <tr>
    <th>Or</th>
    <th>MessageElement&lt;XML Tag&gt;</th>
    <th>Mult.</th>
    <th>Type</th>
    <th>Constr. No.</th>
    <th>Page</th>
  </tr>
  <tr>
    <td></td>
    <td>Identification &lt;Id&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>310</td>
  </tr>
  <tr>
    <td></td>
    <td>Type &lt;Tp&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>310</td>
  </tr>
  <tr>
    <td></td>
    <td>Currency &lt;Ccy&gt;</td>
    <td>[0..1]</td>
    <td>CodeSet</td>
    <td>C2</td>
    <td>310</td>
  </tr>
  <tr>
    <td></td>
    <td>Name &lt;Nm&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>311</td>
  </tr>
  <tr>
    <td></td>
    <td>Proxy &lt;Prxy&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>311</td>
  </tr>
</table>

## Constraints

- **IdentificationAndProxyGuideline**

  If the account identification is not defined through a conventional identification such as an email address or a mobile number, then the proxy element should be used for the identification of the account.

- **IdentificationOrProxyPresenceRule**

  Identification must be present or Proxy must be present. Both may be present.

  ```
  Following Must be True
  /Identification Must be present
  Or
  /Proxy Must be present
  ```

### 3.4.3.7.12.8 PaymentTypeInfo <PmtTpinf>

*Presence:* [0..1]

*Definition:* Set of elements used to further specify the type of transaction.

---

<!-- Page 133 -->

PaymentTypeInformation <PmtTpInf> contains the following elements (see "PaymentTypeInformation27" on page 351 for details)



<table>
  <tr>
    <th>Or</th>
    <th>MessageElement&lt;XML Tag&gt;</th>
    <th>Mult.</th>
    <th>Type</th>
    <th>Constr. No.</th>
    <th>Page</th>
  </tr>
  <tr>
    <td></td>
    <td>InstructionPriority &lt;InstrPrty&gt;</td>
    <td>[0..1]</td>
    <td>CodeSet</td>
    <td></td>
    <td>351</td>
  </tr>
  <tr>
    <td></td>
    <td>ClearingChannel &lt;ClrChanl&gt;</td>
    <td>[0..1]</td>
    <td>CodeSet</td>
    <td></td>
    <td>351</td>
  </tr>
  <tr>
    <td></td>
    <td>ServiceLevel &lt;SvcLvl&gt;</td>
    <td>[0..*]</td>
    <td></td>
    <td></td>
    <td>352</td>
  </tr>
  <tr>
    <td>Or</td>
    <td>Code &lt;Cd&gt;</td>
    <td>[1..1]</td>
    <td>CodeSet</td>
    <td></td>
    <td>352</td>
  </tr>
  <tr>
    <td>Or</td>
    <td>Proprietary &lt;Ptry&gt;</td>
    <td>[1..1]</td>
    <td>Text</td>
    <td></td>
    <td>352</td>
  </tr>
  <tr>
    <td></td>
    <td>LocalInstrument &lt;LclInstrm&gt;</td>
    <td>[0..1]</td>
    <td></td>
    <td></td>
    <td>352</td>
  </tr>
  <tr>
    <td>Or</td>
    <td>Code &lt;Cd&gt;</td>
    <td>[1..1]</td>
    <td>CodeSet</td>
    <td></td>
    <td>352</td>
  </tr>
  <tr>
    <td>Or</td>
    <td>Proprietary &lt;Ptry&gt;</td>
    <td>[1..1]</td>
    <td>Text</td>
    <td></td>
    <td>353</td>
  </tr>
  <tr>
    <td></td>
    <td>SequenceType &lt;SeqTp&gt;</td>
    <td>[0..1]</td>
    <td>CodeSet</td>
    <td></td>
    <td>353</td>
  </tr>
  <tr>
    <td></td>
    <td>CategoryPurpose &lt;CtgyPurp&gt;</td>
    <td>[0..1]</td>
    <td></td>
    <td></td>
    <td>353</td>
  </tr>
  <tr>
    <td>Or</td>
    <td>Code &lt;Cd&gt;</td>
    <td>[1..1]</td>
    <td>CodeSet</td>
    <td></td>
    <td>353</td>
  </tr>
  <tr>
    <td>Or</td>
    <td>Proprietary &lt;Ptry&gt;</td>
    <td>[1..1]</td>
    <td>Text</td>
    <td></td>
    <td>353</td>
  </tr>
</table>

### 3.4.3.7.12.9 PaymentMethod<PmtMtd>

Presence: [0..1]

Definition: Specifies the means of payment that will be used to move the amount of money.

DataType: "PaymentMethod4Code" on page 421



<table>
  <tr>
    <th>CodeName</th>
    <th>Name</th>
    <th>Definition</th>
  </tr>
  <tr>
    <td>CHK</td>
    <td>Cheque</td>
    <td>Written order to a bank to pay a certain amount of money from one person to another person.</td>
  </tr>
  <tr>
    <td>TRF</td>
    <td>CreditTransfer</td>
    <td>Transfer of an amount of money in the books of the account servicer.</td>
  </tr>
  <tr>
    <td>DD</td>
    <td>DirectDebit</td>
    <td>Collection of an amount of money from the debtor's bank account by the creditor. The amount of money and dates of collections may vary.</td>
  </tr>
  <tr>
    <td>TRA</td>
    <td>TransferAdvice</td>
    <td>Transfer of an amount of money in the books of the account servicer. An advice should be sent back to the account owner.</td>
  </tr>
</table>

### 3.4.3.7.12.10 MandateRelatedInformation<MndtRltdInf>

Presence: [0..1]

Definition: Provides further details of the mandate signed between the creditor and the debtor.

---

<!-- Page 134 -->

MandateRelatedInformation <MndtRltdInf> contains one of the following MandateRelatedData3Choice elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| (Or | **DirectDebitMandate** <DtrctDbtMndt> | [0..1] | | C3, C4 | 135 |
| | **MandateIdentification** <MndtId> | [0..1] | Text | | 137 |
| | **DateOfSignature** <DtOfSgntr> | [0..1] | Date | | 137 |
| | **AmendmentIndicator** <AmdmntInd> | [0..1] | Indicator | | 137 |
| | **AmendmentInformationDetails** <AmdmntInfDtls> | [0..1] | | | 137 |
| | **OriginalMandateIdentification** <OrgnlMndtId> | [0..1] | Text | | 138 |
| | **OriginalCreditorSchemeIdentification** <OrgnlCddrSchemId> | [0..1] | ± | | 138 |
| | **OriginalCreditorAgent** <OrgnlCddrAgt> | [0..1] | ± | | 139 |
| | **OriginalCreditorAgentAccount** <OrgnlCddrAgtAcct> | [0..1] | ± | C16, C15 | 140 |
| | **OriginalDebtor** <OrgnlDbtr> | [0..1] | ± | | 141 |
| | **OriginalDebtorAccount** <OrgnlDbtrAcct> | [0..1] | ± | C16, C15 | 142 |
| | **OriginalDebtorAgent** <OrgnlDbtrAgt> | [0..1] | ± | | 143 |
| | **OriginalDebtorAgentAccount** <OrgnlDbtrAgtAcct> | [0..1] | ± | C16, C15 | 144 |
| | **OriginalFinalCollectionDate** <OrgnlFnCltnDt> | [0..1] | Date | | 145 |
| | **OriginalFrequency** <OrgnlFrqcy> | [0..1] | ± | | 145 |
| | **OriginalReason** <OrgnlRsn> | [0..1] | | | 145 |
| (Or | **Code** <Cd> | [1..1] | CodeSet | | 145 |
| Or) | **Proprietary** <Prtty> | [1..1] | Text | | 145 |
| | **OriginalTrackingDays** <OrgnlTrckgDays> | [0..1] | Text | | 146 |
| | **ElectronicSignature** <ElctrncSgntr> | [0..1] | Text | | 146 |
| | **FirstCollectionDate** <FirstCollnDt> | [0..1] | Date | | 146 |
| | **FinalCollectionDate** <FnCltnDt> | [0..1] | Date | | 146 |
| | **Frequency** <Frqcy> | [0..1] | ± | | 146 |
| | **Reason** <Rsn> | [0..1] | | | 146 |
| (Or | **Code** <Cd> | [1..1] | CodeSet | | 147 |
| Or) | **Proprietary** <Prtty> | [1..1] | Text | | 147 |
| | **TrackingDays** <TrckgDays> | [0..1] | Text | | 147 |
| Or) | **CreditTransferMandate** <CdtTrfMndt> | [0..1] | ± | | 147 |

---

<!-- Page 135 -->

**3.4.3.7.12.10.1 DirectDebitMandate &lt;DrctDbtMndt&gt;**

*Presence:* [0..1]

*Definition:* Specific direct debit mandate data.

*Impacted by:* C3 "AmendmentIndicatorFalseRule", C4 "AmendmentIndicatorTrueRule"

---

<!-- Page 136 -->

DirectDebitMandate `<DrctDbtMndt>` contains the following **MandateRelatedInformation16** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **MandateIdentification** `<MndId>` | [0..1] | Text | | 137 |
| | **DateOfSignature** `<DtOfSgntr>` | [0..1] | Date | | 137 |
| | **AmendmentIndicator** `<AmdmntInd>` | [0..1] | Indicator | | 137 |
| | **AmendmentInformationDetails** `<AmdmntInfDtls>` | [0..1] | | | 137 |
| | **OriginalMandateIdentification** `<OrgnlMndId>` | [0..1] | Text | | 138 |
| | **OriginalCreditorSchemeIdentification** `<OrgnCddrSchemId>` | [0..1] | ± | | 138 |
| | **OriginalCreditorAgent** `<OrgnCddrAgt>` | [0..1] | ± | | 139 |
| | **OriginalCreditorAgentAccount** `<OrgnCddrAgtAcct>` | [0..1] | ± | C16, C15 | 140 |
| | **OriginalDebtor** `<OrgnlDbtr>` | [0..1] | ± | | 141 |
| | **OriginalDebtorAccount** `<OrgnlDbtrAcct>` | [0..1] | ± | C16, C15 | 142 |
| | **OriginalDebtorAgent** `<OrgnlDbtrAgt>` | [0..1] | ± | | 143 |
| | **OriginalDebtorAgentAccount** `<OrgnlDbtrAgtAcct>` | [0..1] | ± | C16, C15 | 144 |
| | **OriginalFinalCollectionDate** `<OrgnlFnClctnDt>` | [0..1] | Date | | 145 |
| | **OriginalFrequency** `<OrgnlFrqcy>` | [0..1] | ± | | 145 |
| | **OriginalReason** `<OrgnlRsn>` | [0..1] | | | 145 |
| Or | **Code** `<Cd>` | [1..1] | CodeSet | | 145 |
| Or | **Proprietary** `<Prtty>` | [1..1] | Text | | 145 |
| | **OriginalTrackingDays** `<OrgnlTrckgDays>` | [0..1] | Text | | 146 |
| | **ElectronicSignature** `<ElctrncSgntr>` | [0..1] | Text | | 146 |
| | **FirstCollectionDate** `<FrstClctnDt>` | [0..1] | Date | | 146 |
| | **FinalCollectionDate** `<FnClctnDt>` | [0..1] | Date | | 146 |
| | **Frequency** `<Frqcy>` | [0..1] | ± | | 146 |
| | **Reason** `<Rsn>` | [0..1] | | | 146 |
| Or | **Code** `<Cd>` | [1..1] | CodeSet | | 147 |
| Or | **Proprietary** `<Prtty>` | [1..1] | Text | | 147 |
| | **TrackingDays** `<TrckgDays>` | [0..1] | Text | | 147 |

## Constraints

- **AmendmentIndicatorFalseRule**
  If AmendmentIndicator is false, then AmendmentInformationDetails is not allowed.

---

<!-- Page 137 -->

On Condition
/AmendmentIndicator is equal to value 'false'
Following Must be True
/AmendmentInformationDetails Must be absent

* **AmendmentIndicatorTrueRule**
  If AmendmentIndicator is true, then AmendmentInformationDetails must be present.
  On Condition
  /AmendmentIndicator is equal to value 'true'
  Following Must be True
  /AmendmentInformationDetails Must be present

**3.4.3.7.12.10.1.1 MandateIdentification <MndId>**
*Presence:* [0..1]
*Definition:* Unique identification, as assigned by the creditor, to unambiguously identify the mandate.
*Datatype:* "Max35Text" on page 431

**3.4.3.7.12.10.1.2 DateOfSignature <DtOfSgntr>**
*Presence:* [0..1]
*Definition:* Date on which the direct debit mandate has been signed by the debtor.
*Datatype:* "ISODate" on page 425

**3.4.3.7.12.10.1.3 AmendmentIndicator <AmdmInd>**
*Presence:* [0..1]
*Definition:* Indicator notifying whether the underlying mandate is amended or not.
*Datatype:* One of the following values must be used (see "**TrueFalseIndicator**" on page 427):
* Meaning When True: True
* Meaning When False: False

**3.4.3.7.12.10.1.4 AmendmentInformationDetails <AmdmntInfDtls>**
*Presence:* [0..1]
*Definition:* List of mandate elements that have been modified.

---

<!-- Page 138 -->

AmendmentInformationDetails <AmdmInfDtls> contains the following
AmendmentInformationDetails15 elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **OriginalMandateIdentification** <OrgnlMndtd> | [0..1] | Text | | 138 |
| | **OriginalCreditorSchemeIdentification** <OrgnlCddrSchmeId> | [0..1] | ± | | 138 |
| | **OriginalCreditorAgent** <OrgnlCddrAgt> | [0..1] | ± | | 139 |
| | **OriginalCreditorAgentAccount** <OrgnlCddrAgtAcct> | [0..1] | ± | C16, C15 | 140 |
| | **OriginalDebtor** <OrgnlDbtr> | [0..1] | ± | | 141 |
| | **OriginalDebtorAccount** <OrgnlDbtrAcct> | [0..1] | ± | C16, C15 | 142 |
| | **OriginalDebtorAgent** <OrgnlDbtrAgt> | [0..1] | ± | | 143 |
| | **OriginalDebtorAgentAccount** <OrgnlDbtrAgtAcct> | [0..1] | ± | C16, C15 | 144 |
| | **OriginalFinalCollectionDate** <OrgnlFinCollnDt> | [0..1] | Date | | 145 |
| | **OriginalFrequency** <OrgnlFrqcy> | [0..1] | ± | | 145 |
| | **OriginalReason** <OrgnlRsn> | [0..1] | | | 145 |
| Or | **Code** <Cd> | [1..1] | CodeSet | | 145 |
| Or | **Proprietary** <Prtry> | [1..1] | Text | | 145 |
| | **OriginalTrackingDays** <OrgnlTrckgDays> | [0..1] | Text | | 146 |

**3.4.3.7.12.10.1.4.1 OriginalMandateIdentification <OrgnlMndtd>**
*Presence:* [0..1]
*Definition:* Unique identification, as assigned by the creditor, to unambiguously identify the original mandate.
*Datatype:* "Max35Text" on page 431

**3.4.3.7.12.10.1.4.2 OriginalCreditorSchemeIdentification <OrgnlCddrSchmeId>**
*Presence:* [0..1]
*Definition:* Original creditor scheme identification that has been modified.

---

<!-- Page 139 -->

OriginalCdrSchemeldentification <OrgnlCdrSchemId> contains the following elements (see "PartyIdentification22" on page 336 for details)



<table>
  <thead>
    <tr>
      <th>Or</th>
      <th>MessageElement&lt;XML Tag&gt;</th>
      <th>Mult.</th>
      <th>Type</th>
      <th>Constr. No.</th>
      <th>Page</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td>Name &lt;Nm&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>337</td>
    </tr>
    <tr>
      <td></td>
      <td>PostalAddress &lt;PstlAdr&gt;</td>
      <td>[0..1]</td>
      <td>±</td>
      <td></td>
      <td>338</td>
    </tr>
    <tr>
      <td></td>
      <td>Identification &lt;Id&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>338</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>OrganisationIdentification &lt;OrgId&gt;</td>
      <td>[1..1]</td>
      <td></td>
      <td></td>
      <td>339</td>
    </tr>
    <tr>
      <td></td>
      <td>AnyBIC &lt;AnyBIC&gt;</td>
      <td>[0..1]</td>
      <td>IdentifierSet</td>
      <td>C5</td>
      <td>340</td>
    </tr>
    <tr>
      <td></td>
      <td>LEI &lt;LEI&gt;</td>
      <td>[0..1]</td>
      <td>IdentifierSet</td>
      <td></td>
      <td>340</td>
    </tr>
    <tr>
      <td></td>
      <td>Other &lt;Othr&gt;</td>
      <td>[0..*]</td>
      <td></td>
      <td></td>
      <td>340</td>
    </tr>
    <tr>
      <td></td>
      <td>Identification &lt;Id&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td></td>
      <td>SchemaName &lt;SchmeNm&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Code &lt;Cd&gt;</td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Proprietary &lt;Ptry&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td></td>
      <td>Issuer &lt;Issr&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>PrivateIdentification &lt;PrvtId&gt;</td>
      <td>[1..1]</td>
      <td></td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td></td>
      <td>DateAndPlaceOfBirth &lt;DtAndPlcOfBirth&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>342</td>
    </tr>
    <tr>
      <td></td>
      <td>BirthDate &lt;BirthDt&gt;</td>
      <td>[1..1]</td>
      <td>Date</td>
      <td></td>
      <td>342</td>
    </tr>
    <tr>
      <td></td>
      <td>ProvinceOfBirth &lt;PrvcOfBirth&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>342</td>
    </tr>
    <tr>
      <td></td>
      <td>CityOfBirth &lt;CityOfBirth&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>CountryOfBirth &lt;CtryOfBirth&gt;</td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td>C7</td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>Other &lt;Othr&gt;</td>
      <td>[0..*]</td>
      <td></td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>Identification &lt;Id&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>SchemaName &lt;SchmeNm&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Code &lt;Cd&gt;</td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td></td>
      <td>344</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Proprietary &lt;Ptry&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>344</td>
    </tr>
    <tr>
      <td></td>
      <td>Issuer &lt;Issr&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>344</td>
    </tr>
    <tr>
      <td></td>
      <td>CountryOfResidence &lt;CtryOfRes&gt;</td>
      <td>[0..1]</td>
      <td>CodeSet</td>
      <td>C7</td>
      <td>344</td>
    </tr>
    <tr>
      <td></td>
      <td>ContactDetails &lt;CtctDtls&gt;</td>
      <td>[0..1]</td>
      <td>±</td>
      <td></td>
      <td>344</td>
    </tr>
  </tbody>
</table>

**3.4.3.7.12.10.1.4.3 OriginalCreditorAgent <OrgnlCdrAg>**

*Presence:* [0..1]

*Definition:* Original creditor agent that has been modified.

---

<!-- Page 140 -->

OriginalCreditorAgent <OrgnlCddtrAgt> contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on page 320 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | FinancialInstitutionIdentification <FinInstlId> | [1..1] | | | 321 |
| | BICFI <BICFI> | [0..1] | IdentifierSet | C6 | 321 |
| | ClearingSystemMemberIdentification <ClrSysMmbId> | [0..1] | ± | | 322 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 322 |
| | Name <Nm> | [0..1] | Text | | 322 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 322 |
| | Other <Othr> | [0..1] | ± | | 323 |
| | BranchIdentification <BrnchId> | [0..1] | | | 324 |
| | Identification <Id> | [0..1] | Text | | 324 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 324 |
| | Name <Nm> | [0..1] | Text | | 324 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 324 |

**3.4.3.7.12.10.1.4.4 OriginalCreditorAgentAccount <OrgnlCddtrAgtAcct>**

*Presence:* [0..1]

*Definition:* Original creditor agent account that has been modified.

*Impacted by:* C16 "IdentificationOrProxyPresenceRule", C15 "IdentificationAndProxyGuideline"

OriginalCreditorAgentAccount <OrgnlCddtrAgtAcct> contains the following elements (see "CashAccount40" on page 309 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | Identification <Id> | [0..1] | ± | | 310 |
| | Type <Tp> | [0..1] | ± | | 310 |
| | Currency <Ccy> | [0..1] | CodeSet | C2 | 310 |
| | Name <Nm> | [0..1] | Text | | 311 |
| | Proxy <Prxy> | [0..1] | ± | | 311 |

## Constraints

*   **IdentificationAndProxyGuideline**
    If the account identification is not defined through a conventional identification such as an email address or a mobile number, then the proxy element should be used for the identification of the account.

*   **IdentificationOrProxyPresenceRule**
    Identification must be present or Proxy must be present. Both may be present.

---

<!-- Page 141 -->

Following Must be True
/Identification Must be present
Or /Proxy Must be present

**3.4.3.7.12.10.1.4.5 OriginalDebtor <OrgnlDbtr>**

*Presence*:[0..1]

*Definition*: Original debtor that has been modified.

---

<!-- Page 142 -->

OriginalDebtor <OrgnlDbtr> contains the following elements (see "PartyIdentification27" on page 336 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | Name *<Nm>* | [0..1] | Text | | 337 |
| | PostalAddress *<PstlAdr>* | | ± | | 338 |
| | Identification *<Id>* | [0..1] | | | 338 |
| (Or) | OrganisationIdentification *<OrgId>* | [1..1] | | | 339 |
| | AnyBIC *<AnyBIC>* | [0..1] | IdentifierSet | C5 | 340 |
| | LEI *<LEI>* | [0..1] | IdentifierSet | | 340 |
| | Other *<Othr>* | [0..*] | | | 340 |
| | Identification *<Id>* | [1..1] | Text | | 341 |
| | SchemeName *<SchmeNm>* | [0..1] | | | 341 |
| (Or) | Code *<Cd>* | [1..1] | CodeSet | | 341 |
| Or | Proprietary *<Prtry>* | [1..1] | Text | | 341 |
| | Issuer *<Issr>* | [0..1] | Text | | 341 |
| (Or) | PrivateIdentification *<PrvtId>* | [1..1] | | | 341 |
| | DateAndPlaceOfBirth *<DtAndPlcOfBirth>* | [0..1] | | | 342 |
| | BirthDate *<BirthDt>* | [1..1] | Date | | 342 |
| | ProvinceOfBirth *<PrvcOfBirth>* | [0..1] | Text | | 342 |
| | CityOfBirth *<CityOfBirth>* | [1..1] | Text | | 343 |
| | CountryOfBirth *<CtryOfBirth>* | [1..1] | CodeSet | C7 | 343 |
| | Other *<Othr>* | [0..*] | | | 343 |
| | Identification *<Id>* | [1..1] | Text | | 343 |
| | SchemeName *<SchmeNm>* | [0..1] | | | 343 |
| (Or) | Code *<Cd>* | [1..1] | CodeSet | | 344 |
| Or | Proprietary *<Prtry>* | [1..1] | Text | | 344 |
| | Issuer *<Issr>* | [0..1] | Text | | 344 |
| | CountryOfResidence *<CtryOfRes>* | [0..1] | CodeSet | C7 | 344 |
| | ContactDetails *<CtctDtls>* | [0..1] | ± | | 344 |

**3.4.3.7.12.10.1.4.6 OriginalDebtorAccount <OrgnlDbtrAcct>**
*Presence:* [0..1]
*Definition:* Original debtor account that has been modified.
*Impacted by:* C16 "IdentificationOrProxyPresenceRule", C15 "IdentificationAndProxyGuideline"

---

<!-- Page 143 -->

OriginalDebtorAccount <OrgnlDbtrAcct> contains the following elements (see "CashAccount40" on page 309 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Identification <Ids> | [0..1] | ± | | 310 |
| | Type <Tp> | [0..1] | ± | | 310 |
| | Currency <Ccy> | [0..1] | CodeSet | C2 | 310 |
| | Name <Nm> | [0..1] | Text | | 311 |
| | Proxy <Prxy> | [0..1] | ± | | 311 |

## Constraints

- **IdentificationAndProxyGuideline**

  If the account identification is not defined through a conventional identification such as an email address or a mobile number, then the proxy element should be used for the identification of the account.

- **IdentificationOrProxyPresenceRule**

  Identification must be present or Proxy must be present. Both may be present.

  ```
  Following Must be True
  /Identification Must be present
  Or
  /Proxy Must be present
  ```

**3.4.3.7.12.10.4.7 OriginalDebtorAgent <OrgnlDbtrAgent>**

*Presence:* [0..1]

*Definition:* Original debtor agent that has been modified.

---

<!-- Page 144 -->

OriginalDebtorAgent <OrgnlDbtrAgt> contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on page 320 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | FinancialInstitutionIdentification <FinInstId> | [0..1] | | | 321 |
| | BICFI <BICFI> | [0..1] | IdentifierSet | C6 | 321 |
| | ClearingSystemMemberIdentification <ClrSysMmbId> | [0..1] | ± | | 322 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 322 |
| | Name <Nm> | [0..1] | Text | | 322 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 322 |
| | Other <Othr> | [0..1] | ± | | 323 |
| | BranchIdentification <BrnchId> | [0..1] | | | 324 |
| | Identification <Id> | [0..1] | Text | | 324 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 324 |
| | Name <Nm> | [0..1] | Text | | 324 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 324 |

### 3.4.3.7.12.10.1.4.8 OriginalDebtorAgentAccount <OrgnlDbtrAgtAcc>

Presence: [0..1]

Definition: Original debtor agent account that has been modified.

Impacted by: C16 "IdentificationOrProxyPresenceRule", C15 "IdentificationAndProxyGuideline"

OriginalDebtorAgentAccount <OrgnlDbtrAgtAcc> contains the following elements (see "CashAccount40" on page 309 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | Identification <Id> | [0..1] | ± | | 310 |
| | Type <Tp> | [0..1] | ± | | 310 |
| | Currency <Ccy> | [0..1] | CodeSet | C2 | 310 |
| | Name <Nm> | [0..1] | Text | | 311 |
| | Proxy <Prxy> | [0..1] | ± | | 311 |

## Constraints

*   **IdentificationAndProxyGuideline**
    If the account identification is not defined through a conventional identification such as an email address or a mobile number, then the proxy element should be used for the identification of the account.

*   **IdentificationOrProxyPresenceRule**
    Identification must be present or Proxy must be present. Both may be present.

---

<!-- Page 145 -->

Following Must be True
/Identification Must be present
Or /Proxy Must be present

**3.4.3.7.12.10.1.4.9 OriginalFinalCollectionDate <OrgnlFnlColltnDt>**

*Presence:* [0..1]

*Definition:* Original final collection date that has been modified.

*DataType:* "ISODate" on page 425

**3.4.3.7.12.10.1.4.10 OriginalFrequency <OrgnlFrcq>**

*Presence:* [0..1]

*Definition:* Original frequency that has been modified.

**OriginalFrequency <OrgnlFrcq>** contains one of the following elements (see "Frequency36Choice" on page 326 for details)



<table>
  <thead>
    <tr>
      <th>Or</th>
      <th>MessageElement&lt;XML Tag&gt;</th>
      <th>Mult.</th>
      <th>Type</th>
      <th>Constr. No.</th>
      <th>Page</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Or</td>
      <td>Type &lt;Tp&gt;</td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td></td>
      <td>327</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Period &lt;Prd&gt;</td>
      <td>[1..1]</td>
      <td></td>
      <td></td>
      <td>327</td>
    </tr>
    <tr>
      <td></td>
      <td>Type &lt;Tp&gt;</td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td></td>
      <td>328</td>
    </tr>
    <tr>
      <td></td>
      <td>CountPerPeriod &lt;CntPerPrd&gt;</td>
      <td>[1..1]</td>
      <td>Quantity</td>
      <td></td>
      <td>328</td>
    </tr>
    <tr>
      <td>Or)</td>
      <td>PointInTime &lt;PntInTm&gt;</td>
      <td>[1..1]</td>
      <td></td>
      <td></td>
      <td>328</td>
    </tr>
    <tr>
      <td></td>
      <td>Type &lt;Tp&gt;</td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td></td>
      <td>328</td>
    </tr>
    <tr>
      <td></td>
      <td>PointInTime &lt;PntInTm&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>329</td>
    </tr>
  </tbody>
</table>

**3.4.3.7.12.10.1.4.11 OriginalReason <OrgnlRsn>**

*Presence:* [0..1]

*Definition:* Original reason for the mandate to allow the user to distinguish between different mandates for the same creditor.

**OriginalReason <OrgnlRsn>** contains one of the following **MandateSetupReason1Choice** elements



<table>
  <thead>
    <tr>
      <th>Or</th>
      <th>MessageElement&lt;XML Tag&gt;</th>
      <th>Mult.</th>
      <th>Type</th>
      <th>Constr. No.</th>
      <th>Page</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>Or</td>
      <td>Code &lt;Cd&gt;</td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td></td>
      <td>145</td>
    </tr>
    <tr>
      <td>Or)</td>
      <td>Proprietary &lt;Prtry&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>145</td>
    </tr>
  </tbody>
</table>

**3.4.3.7.12.10.1.4.11.1 Code <Cd>**

*Presence:* [1..1]

*Definition:* Reason for the mandate setup, as published in an external reason code list.

*DataType:* "ExternalMandateSetupReason1Code" on page 417

**3.4.3.7.12.10.1.4.11.2 Proprietary <Prtry>**

*Presence:* [1..1]

---

<!-- Page 146 -->

*Definition: Reason for the mandate setup, in a proprietary form.*
*Datatype: "Max70Text" on page 431*

**3.4.3.7.12.10.1.4.12 OriginalTrackingDays <OrgnlTrckgDays>**
*Presence: [0..1]*
*Definition: Original number of tracking days that has been modified.*
*Datatype: "Exact2NumericText" on page 428*

**3.4.3.7.12.10.1.5 ElectronicSignature <ElctrncSgntr>**
*Presence: [0..1]*
*Definition: Additional security provisions, such as a digital signature, as provided by the debtor.*
*Datatype: "Max1025Text" on page 429*

**3.4.3.7.12.10.1.6 FirstCollectionDate <FrstColltnDt>**
*Presence: [0..1]*
*Definition: Date of the first collection of a direct debit as per the mandate.*
*Datatype: "ISODate" on page 425*

**3.4.3.7.12.10.1.7 FinalCollectionDate <FnlColltnDt>**
*Presence: [0..1]*
*Definition: Date of the final collection of a direct debit as per the mandate.*
*Datatype: "ISODate" on page 425*

**3.4.3.7.12.10.1.8 Frequency <Frcy>**
*Presence: [0..1]*
*Definition: Regularity with which direct debit instructions are to be created and processed.*
**Frequency <Frcy>** contains one of the following elements (see "Frequency36Choice" on page 326 for details)



| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| Or | Type <Tp> | [1..1] | CodeSet | | 327 |
| Or | Period <Prd> | [1..1] | | | 327 |
| | Type <Tp> | [1..1] | CodeSet | | 328 |
| | CountPerPeriod <CntPerPrd> | [1..1] | Quantity | | 328 |
| Or | PointInTime <Ptlntm> | [1..1] | | | 328 |
| | Type <Tp> | [1..1] | CodeSet | | 328 |
| | PointInTime <Ptlntm> | [1..1] | Text | | 329 |

**3.4.3.7.12.10.1.9 Reason <Rsn>**
*Presence: [0..1]*

---

<!-- Page 147 -->

*Definition:* Reason for the direct debit mandate to allow the user to distinguish between different mandates for the same creditor.

**Reason** <Rsn> contains one of the following **MandateSetupReason1Choice** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| (Or | **Code** <Cd> | [1..1] | CodeSet | | 147 |
| Or) | **Proprietary** <Prtry> | [1..1] | Text | | 147 |

**3.4.3.7.12.10.1.9.1 Code <Cd>**

*Presence:* [1..1]

*Definition:* Reason for the mandate setup, as published in an external reason code list.

*Datatype:* "ExternalMandateSetupReason1Code" on page 417

**3.4.3.7.12.10.1.9.2 Proprietary <Prtry>**

*Presence:* [1..1]

*Definition:* Reason for the mandate setup, in a proprietary form.

*Datatype:* "Max70Text" on page 431

**3.4.3.7.12.10.1.10 TrackingDays <TrckgDays>**

*Presence:* [0..1]

*Definition:* Specifies the number of days the direct debit instruction must be tracked.

*Datatype:* "Exact2NumericText" on page 428

**3.4.3.7.12.10.2 CreditTransferMandate <CdtTrfMndt>**

*Presence:* [0..1]

*Definition:* Specific credit transfer mandate data.

---

<!-- Page 148 -->

CreditTransferMandate <CdtTrfMndt> contains the following elements (see "CreditTransferMandateData1" on page 317 for details)



<table>
  <tr>
    <th>Or</th>
    <th>MessageElement&lt;XML Tag&gt;</th>
    <th>Mult.</th>
    <th>Type</th>
    <th>Constr. No.</th>
    <th>Page</th>
  </tr>
  <tr>
    <td></td>
    <td>MandateIdentification &lt;MndtId&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>317</td>
  </tr>
  <tr>
    <td></td>
    <td>Type &lt;Tp&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>317</td>
  </tr>
  <tr>
    <td></td>
    <td>DateOfSignature &lt;DtOfSgntr&gt;</td>
    <td>[0..1]</td>
    <td>Date</td>
    <td></td>
    <td>318</td>
  </tr>
  <tr>
    <td></td>
    <td>DateOfVerification &lt;DtOfVrfctn&gt;</td>
    <td>[0..1]</td>
    <td>DateTime</td>
    <td></td>
    <td>318</td>
  </tr>
  <tr>
    <td></td>
    <td>ElectronicSignature &lt;ElctrncSgntr&gt;</td>
    <td>[0..1]</td>
    <td>Binary</td>
    <td></td>
    <td>318</td>
  </tr>
  <tr>
    <td></td>
    <td>FirstPaymentDate &lt;FrstPmtDt&gt;</td>
    <td>[0..1]</td>
    <td>Date</td>
    <td></td>
    <td>318</td>
  </tr>
  <tr>
    <td></td>
    <td>FinalPaymentDate &lt;FnlpmtDt&gt;</td>
    <td>[0..1]</td>
    <td>Date</td>
    <td></td>
    <td>318</td>
  </tr>
  <tr>
    <td></td>
    <td>Frequency &lt;Frqcy&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>319</td>
  </tr>
  <tr>
    <td></td>
    <td>Reason &lt;Rsn&gt;</td>
    <td>[0..1]</td>
    <td></td>
    <td></td>
    <td>319</td>
  </tr>
  <tr>
    <td>Or</td>
    <td>Code &lt;Cd&gt;</td>
    <td>[1..1]</td>
    <td>CodeSet</td>
    <td></td>
    <td>319</td>
  </tr>
  <tr>
    <td>Or</td>
    <td>Proprietary &lt;Ptry&gt;</td>
    <td>[1..1]</td>
    <td>Text</td>
    <td></td>
    <td>319</td>
  </tr>
</table>

### 3.4.3.7.12.11 RemittanceInformation <RmtInf>

Presence: [0..1]

Definition: Information supplied to enable the matching of an entry with the items that the transfer is intended to settle, such as commercial invoices in an accounts' receivable system.

RemittanceInformation <RmtInf> contains the following elements (see "RemittanceInformation22" on page 364 for details)



<table>
  <tr>
    <th>Or</th>
    <th>MessageElement&lt;XML Tag&gt;</th>
    <th>Mult.</th>
    <th>Type</th>
    <th>Constr. No.</th>
    <th>Page</th>
  </tr>
  <tr>
    <td></td>
    <td>Unstructured &lt;Ustrd&gt;</td>
    <td>[0..*]</td>
    <td>Text</td>
    <td></td>
    <td>364</td>
  </tr>
  <tr>
    <td></td>
    <td>Structured &lt;Strd&gt;</td>
    <td>[0..*]</td>
    <td>±</td>
    <td></td>
    <td>364</td>
  </tr>
</table>

### 3.4.3.7.12.12 UltimateDebtor <UltmtDbtr>

Presence: [0..1]

Definition: Ultimate party that owes an amount of money to the (ultimate) creditor.

UltimateDebtor <UltmtDbtr> contains one of the following Party50Choice elements



<table>
  <tr>
    <th>Or</th>
    <th>MessageElement&lt;XML Tag&gt;</th>
    <th>Mult.</th>
    <th>Type</th>
    <th>Constr. No.</th>
    <th>Page</th>
  </tr>
  <tr>
    <td>Or</td>
    <td><b>Party</b> &lt;Pty&gt;</td>
    <td>[1..1]</td>
    <td>±</td>
    <td></td>
    <td>148</td>
  </tr>
  <tr>
    <td>Or</td>
    <td><b>Agent</b> &lt;Agt&gt;</td>
    <td>[1..1]</td>
    <td>±</td>
    <td></td>
    <td>149</td>
  </tr>
</table>

#### 3.4.3.7.12.12.1 Party <Pty>

Presence: [1..1]

Definition: Identification of a person or an organisation.

---

<!-- Page 149 -->

Party <Pty> contains the following elements (see "PartyIdentification27" on page 336 for details)



<table>
  <thead>
    <tr>
      <th>Or</th>
      <th>MessageElement &lt;XML Tag&gt;</th>
      <th>Mult.</th>
      <th>Type</th>
      <th>Constr. No.</th>
      <th>Page</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td>Name &lt;Nm&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>337</td>
    </tr>
    <tr>
      <td></td>
      <td>PostalAddress &lt;PstlAdr&gt;</td>
      <td>[0..1]</td>
      <td>±</td>
      <td></td>
      <td>338</td>
    </tr>
    <tr>
      <td></td>
      <td>Identification &lt;Id&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>338</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>OrganisationIdentification &lt;OrgId&gt;</td>
      <td>[1..1]</td>
      <td></td>
      <td></td>
      <td>339</td>
    </tr>
    <tr>
      <td></td>
      <td>AnyBIC &lt;AnyBIC&gt;</td>
      <td>[0..1]</td>
      <td>IdentifierSet</td>
      <td>C5</td>
      <td>340</td>
    </tr>
    <tr>
      <td></td>
      <td>LEI &lt;LEI&gt;</td>
      <td>[0..1]</td>
      <td>IdentifierSet</td>
      <td></td>
      <td>340</td>
    </tr>
    <tr>
      <td></td>
      <td>Other &lt;Othr&gt;</td>
      <td>[0..*]</td>
      <td></td>
      <td></td>
      <td>340</td>
    </tr>
    <tr>
      <td></td>
      <td>Identification &lt;Id&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td></td>
      <td>SchemeName &lt;SchmeNm&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Code &lt;Cd&gt;</td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Proprietary &lt;Prtry&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td></td>
      <td>Issuer &lt;Issr&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>PrivateIdentification &lt;PrvtId&gt;</td>
      <td>[1..1]</td>
      <td></td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td></td>
      <td>DateAndPlaceOfBirth &lt;DtAndPlcOfBrth&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>342</td>
    </tr>
    <tr>
      <td></td>
      <td>BirthDate &lt;BirthDt&gt;</td>
      <td>[1..1]</td>
      <td>Date</td>
      <td></td>
      <td>342</td>
    </tr>
    <tr>
      <td></td>
      <td>ProvinceOfBirth &lt;PrvcOfBrth&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>342</td>
    </tr>
    <tr>
      <td></td>
      <td>CityOfBirth &lt;CityOfBrth&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>CountryOfBirth &lt;CtryOfBrth&gt;</td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td>C7</td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>Other &lt;Othr&gt;</td>
      <td>[0..*]</td>
      <td></td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>Identification &lt;Id&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>SchemeName &lt;SchmeNm&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Code &lt;Cd&gt;</td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td></td>
      <td>344</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Proprietary &lt;Prtry&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>344</td>
    </tr>
    <tr>
      <td></td>
      <td>Issuer &lt;Issr&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>344</td>
    </tr>
    <tr>
      <td></td>
      <td>CountryOfResidence &lt;CtryOfRes&gt;</td>
      <td>[0..1]</td>
      <td>CodeSet</td>
      <td>C7</td>
      <td>344</td>
    </tr>
    <tr>
      <td></td>
      <td>ContactDetails &lt;CtctDtls&gt;</td>
      <td>[0..1]</td>
      <td>±</td>
      <td></td>
      <td>344</td>
    </tr>
  </tbody>
</table>

### 3.4.3.7.12.12.2 Agent <Ag>

Presence: [1..1]

Definition: Identification of a financial institution.

---

<!-- Page 150 -->

Agent <Agt> contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on page 320 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Const. No. | Page |
|---|---|---|---|---|---|
| | FinancialInstitutionIdentification <FinInstlId> | [1..1] | | | 321 |
| | BICFI <BICFI> | [0..1] | IdentifierSet | C6 | 321 |
| | ClearingSystemMemberIdentification <ClrSysMmbId> | [0..1] | ± | | 322 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 322 |
| | Name <Nm> | [0..1] | Text | | 322 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 322 |
| | Other <Othr> | [0..1] | ± | | 323 |
| | BranchIdentification <BrnchId> | [0..1] | | | 324 |
| | Identification <Id> | [0..1] | Text | | 324 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 324 |
| | Name <Nm> | [0..1] | Text | | 324 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 324 |

### 3.4.3.7.12.13 Debtor <Dbtr>

*Presence: [0..1]*

*Definition: Party that owes an amount of money to the (ultimate) creditor.*

Debtor <Dbtr> contains one of the following **Party50Choice** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Const. No. | Page |
|---|---|---|---|---|---|
| (Or | Party <Pty> | [1..1] | ± | | 150 |
| (Or) | Agent <Agt> | [1..1] | ± | | 151 |

### 3.4.3.7.12.13.1 Party <Pty>

*Presence: [1..1]*

*Definition: Identification of a person or an organisation.*

---

<!-- Page 151 -->

Party <Pty> contains the following elements (see "PartyIdentification272" on page 336 for details)



<table>
  <thead>
    <tr>
      <th>Or</th>
      <th>MessageElement&lt;XML Tag&gt;</th>
      <th>Mult.</th>
      <th>Type</th>
      <th>Constr. No.</th>
      <th>Page</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td>Name &lt;Nm&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>337</td>
    </tr>
    <tr>
      <td></td>
      <td>PostalAddress &lt;PstlAdr&gt;</td>
      <td>[0..1]</td>
      <td>±</td>
      <td></td>
      <td>338</td>
    </tr>
    <tr>
      <td></td>
      <td>Identification &lt;Id&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>338</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>OrganisationIdentification &lt;OrgId&gt;</td>
      <td>[1..1]</td>
      <td></td>
      <td></td>
      <td>339</td>
    </tr>
    <tr>
      <td></td>
      <td>AnyBIC &lt;AnyBIC&gt;</td>
      <td>[0..1]</td>
      <td>IdentifierSet</td>
      <td>C5</td>
      <td>340</td>
    </tr>
    <tr>
      <td></td>
      <td>LEI &lt;LEI&gt;</td>
      <td>[0..1]</td>
      <td>IdentifierSet</td>
      <td></td>
      <td>340</td>
    </tr>
    <tr>
      <td></td>
      <td>Other &lt;Othr&gt;</td>
      <td>[0..*]</td>
      <td></td>
      <td></td>
      <td>340</td>
    </tr>
    <tr>
      <td></td>
      <td>Identification &lt;Id&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td></td>
      <td>SchemeName &lt;SchmeNm&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Code &lt;Cd&gt;</td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Proprietary &lt;Prtry&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td></td>
      <td>Issuer &lt;Issr&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>PrivateIdentification &lt;PrvtId&gt;</td>
      <td>[1..1]</td>
      <td></td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td></td>
      <td>DateAndPlaceOfBirth &lt;DtAndPlcOfBrth&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>342</td>
    </tr>
    <tr>
      <td></td>
      <td>BirthDate &lt;BirthDt&gt;</td>
      <td>[1..1]</td>
      <td>Date</td>
      <td></td>
      <td>342</td>
    </tr>
    <tr>
      <td></td>
      <td>ProvinceOfBirth &lt;PvcOfBrth&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>342</td>
    </tr>
    <tr>
      <td></td>
      <td>CityOfBirth &lt;CityOfBrth&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>CountryOfBirth &lt;CtryOfBrth&gt;</td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td>C7</td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>Other &lt;Othr&gt;</td>
      <td>[0..*]</td>
      <td></td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>Identification &lt;Id&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>SchemeName &lt;SchmeNm&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Code &lt;Cd&gt;</td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td></td>
      <td>344</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Proprietary &lt;Prtry&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>344</td>
    </tr>
    <tr>
      <td></td>
      <td>Issuer &lt;Issr&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>344</td>
    </tr>
    <tr>
      <td></td>
      <td>CountryOfResidence &lt;CtryOfRes&gt;</td>
      <td>[0..1]</td>
      <td>CodeSet</td>
      <td>C7</td>
      <td>344</td>
    </tr>
    <tr>
      <td></td>
      <td>ContactDetails &lt;CtctDtls&gt;</td>
      <td>[0..1]</td>
      <td>±</td>
      <td></td>
      <td>344</td>
    </tr>
  </tbody>
</table>

### 3.4.3.7.12.13.2 Agent <Ag>

Presence: [1..1]

Definition: Identification of a financial institution.

---

<!-- Page 152 -->

Agent < *Agt* > contains the following elements (see " *BranchAndFinancialInstitutionIdentification8* " on page 320 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | FinancialInstitutionIdentification < *FinInstlId* > | [1..1] |  |  | 321 |
| | BICFI < *BICFI* > | [0..1] | IdentifierSet | C6 | 321 |
| | ClearingSystemMemberIdentification < *ClrSysMmbId* > | [0..1] | ± |  | 322 |
| | LEI < *LEI* > | [0..1] | IdentifierSet |  | 322 |
| | Name < *Nm* > | [0..1] | Text |  | 322 |
| | PostalAddress < *PstlAdr* > | [0..1] | ± |  | 322 |
| | Other < *Othr* > | [0..1] | ± |  | 323 |
| | BranchIdentification < *BrnchId* > | [0..1] |  |  | 324 |
| | Identification < *Id* > | [0..1] | Text |  | 324 |
| | LEI < *LEI* > | [0..1] | IdentifierSet |  | 324 |
| | Name < *Nm* > | [0..1] | Text |  | 324 |
| | PostalAddress < *PstlAdr* > | [0..1] | ± |  | 324 |

### 3.4.3.7.12.14 DebtorAccount < *DbtrAcc* >

Presence: [0..1]

Definition: Unambiguous identification of the account of the debtor to which a debit entry will be made as a result of the transaction.

Impacted by: C16 "IdentificationOrProxyPresenceRule", C15 "IdentificationAndProxyGuideline"

DebtorAccount < *DbtrAcc* > contains the following elements (see " *CashAccount40* " on page 309 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Identification < *Id* > | [0..1] | ± |  | 310 |
| | Type < *Tp* > | [0..1] | ± |  | 310 |
| | Currency < *Ccy* > | [0..1] | CodeSet | C2 | 310 |
| | Name < *Nm* > | [0..1] | Text |  | 311 |
| | Proxy < *Prxy* > | [0..1] | ± |  | 311 |

---

<!-- Page 153 -->

Constraints

*   **IdentificationAndProxyGuideline**

    If the account identification is not defined through a conventional identification such as an email address or a mobile number, then the proxy element should be used for the identification of the account.

*   **IdentificationOrProxyPresenceRule**

    Identification must be present or Proxy must be present. Both may be present.

    ```
    Following Must be True
    /Identification Must be present
    Or
    /Proxy Must be present
    ```

### 3.4.3.7.12.15 DebtorAgent <DbtrAgt>

*Presence:* [0..1]

*Definition:* Financial institution servicing an account for the debtor.

**DebtorAgent <DbtrAgt>** contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on page 320 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
| :--- | :--- | :--- | :--- | :--- | :--- |
| | FinancialInstitutionIdentification <FinInstlId> | [1..1] | | | 321 |
| | BICFI <BICFI> | [0..1] | Identifier/Set | C6 | 321 |
| | ClearingSystemMemberIdentification <ClrSysMmbId> | [0..1] | ± | | 322 |
| | LEI <LEI> | [0..1] | Identifier/Set | | 322 |
| | Name <Nm> | [0..1] | Text | | 322 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 322 |
| | Other <Othr> | [0..1] | ± | | 323 |
| | BranchIdentification <BrnchId> | [0..1] | | | 324 |
| | Identification <Id> | [0..1] | Text | | 324 |
| | LEI <LEI> | [0..1] | Identifier/Set | | 324 |
| | Name <Nm> | [0..1] | Text | | 324 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 324 |

### 3.4.3.7.12.16 DebtorAgentAccount <DbtrAgtAcct>

*Presence:* [0..1]

*Definition:* Unambiguous identification of the account of the debtor agent at its servicing agent in the payment chain.

*Impacted by:* C16 "IdentificationOrProxyPresenceRule", C15 "IdentificationAndProxyGuideline"

---

<!-- Page 154 -->

DebtorAgentAccount <DbtrAgmtAcct> contains the following elements (see "CashAccount40" on page 309 for details)



| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Identification <Ids> | [0..1] | ± | | 310 |
| | Type <Tp> | [0..1] | ± | | 310 |
| | Currency <Ccy> | [0..1] | CodeSet | C2 | 310 |
| | Name <Nm> | [0..1] | Text | | 311 |
| | Proxy <Prxy> | [0..1] | ± | | 311 |

## Constraints

- **IdentificationAndProxyGuideline**

  If the account identification is not defined through a conventional identification such as an email address or a mobile number, then the proxy element should be used for the identification of the account.

- **IdentificationOrProxyPresenceRule**

  Identification must be present or Proxy must be present. Both may be present.

  ```
  Following Must be True
  /Identification Must be present
  Or
  /Proxy Must be present
  ```

### 3.4.3.7.12.17 CreditorAgent <CdtrAggt>

*Presence:* [0..1]

*Definition:* Financial institution servicing an account for the creditor.

---

<!-- Page 155 -->

**CreditorAgent** *<CdrAgnt>* contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on page 320 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | FinancialInstitutionIdentification *<FinInstId>* | [1..1] | | | 321 |
| | BICFI *<BICFI>* | [0..1] | IdentifierSet | C6 | 321 |
| | ClearingSystemMemberIdentification *<ClrSysMmbId>* | [0..1] | ± | | 322 |
| | LEI *<LEI>* | [0..1] | IdentifierSet | | 322 |
| | Name *<Nm>* | [0..1] | Text | | 322 |
| | PostalAddress *<PstlAdr>* | [0..1] | ± | | 322 |
| | Other *<Othr>* | [0..1] | ± | | 323 |
| | BranchIdentification *<BrnchId>* | [0..1] | | | 324 |
| | Identification *<Id>* | [0..1] | Text | | 324 |
| | LEI *<LEI>* | [0..1] | IdentifierSet | | 324 |
| | Name *<Nm>* | [0..1] | Text | | 324 |
| | PostalAddress *<PstlAdr>* | [0..1] | ± | | 324 |

### 3.4.3.7.12.18 CreditorAgentAccount <CdrAgntAcct>

Presence: [0..1]

*Definition:* Unambiguous identification of the account of the creditor agent at its servicing agent to which a credit entry will be made as a result of the payment transaction.

*Impacted by:* C16 "IdentificationOrProxyPresenceRule", C15 "IdentificationAndProxyGuideline"

**CreditorAgentAccount** *<CdrAgntAcct>* contains the following elements (see "CashAccount40" on page 309 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | Identification *<Id>* | [0..1] | ± | | 310 |
| | Type *<Tp>* | [0..1] | ± | | 310 |
| | Currency *<Ccy>* | [0..1] | CodeSet | C2 | 310 |
| | Name *<Nm>* | [0..1] | Text | | 311 |
| | Proxy *<Prxy>* | [0..1] | ± | | 311 |

---

<!-- Page 156 -->

Constraints

- **IdentificationAndProxyGuideline**

  If the account identification is not defined through a conventional identification such as an email address or a mobile number, then the proxy element should be used for the identification of the account.

- **IdentificationOrProxyPresenceRule**

  Identification must be present or Proxy must be present. Both may be present.

```
Following Must be True
/Identification Must be present
Or      /Proxy Must be present
```

### 3.4.3.7.12.19 Creditor <Cdr>

*Presence:* [0..1]

*Definition:* Party to which an amount of money is due.

**Creditor <Cdr>** contains one of the following **Party50Choice** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| (Or | **Party** <Pty> | [1..1] | ± | | 156 |
| Or) | **Agent** <Agt> | [1..1] | ± | | 157 |

### 3.4.3.7.12.19.1 Party <Pty>

*Presence:* [1..1]

*Definition:* Identification of a person or an organisation.

---

<!-- Page 157 -->

Party <Pty> contains the following elements (see "PartyIdentification272" on page 336 for details)



<table>
  <thead>
    <tr>
      <th>Or</th>
      <th>MessageElement&lt;XML Tag&gt;</th>
      <th>Mult.</th>
      <th>Type</th>
      <th>Constr. No.</th>
      <th>Page</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td>Name &lt;Nm&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>337</td>
    </tr>
    <tr>
      <td></td>
      <td>PostalAddress &lt;PstlAdr&gt;</td>
      <td>[0..1]</td>
      <td>±</td>
      <td></td>
      <td>338</td>
    </tr>
    <tr>
      <td></td>
      <td>Identification &lt;Id&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>338</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>OrganisationIdentification &lt;OrgId&gt;</td>
      <td>[1..1]</td>
      <td></td>
      <td></td>
      <td>339</td>
    </tr>
    <tr>
      <td></td>
      <td>AnyBIC &lt;AnyBIC&gt;</td>
      <td>[0..1]</td>
      <td>IdentifierSet</td>
      <td>C5</td>
      <td>340</td>
    </tr>
    <tr>
      <td></td>
      <td>LEI &lt;LEI&gt;</td>
      <td>[0..1]</td>
      <td>IdentifierSet</td>
      <td></td>
      <td>340</td>
    </tr>
    <tr>
      <td></td>
      <td>Other &lt;Othr&gt;</td>
      <td>[0..*]</td>
      <td></td>
      <td></td>
      <td>340</td>
    </tr>
    <tr>
      <td></td>
      <td>Identification &lt;Id&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td></td>
      <td>SchemeName &lt;SchmeNm&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Code &lt;Cd&gt;</td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Proprietary &lt;Prtry&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td></td>
      <td>Issuer &lt;Issr&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>PrivateIdentification &lt;PrvtId&gt;</td>
      <td>[1..1]</td>
      <td></td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td></td>
      <td>DateAndPlaceOfBirth &lt;DtAndPlcOfBrth&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>342</td>
    </tr>
    <tr>
      <td></td>
      <td>BirthDate &lt;BirthDt&gt;</td>
      <td>[1..1]</td>
      <td>Date</td>
      <td></td>
      <td>342</td>
    </tr>
    <tr>
      <td></td>
      <td>ProvinceOfBirth &lt;PvcOfBrth&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>342</td>
    </tr>
    <tr>
      <td></td>
      <td>CityOfBirth &lt;CityOfBrth&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>CountryOfBirth &lt;CtryOfBrth&gt;</td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td>C7</td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>Other &lt;Othr&gt;</td>
      <td>[0..*]</td>
      <td></td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>Identification &lt;Id&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>SchemeName &lt;SchmeNm&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Code &lt;Cd&gt;</td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td></td>
      <td>344</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Proprietary &lt;Prtry&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>344</td>
    </tr>
    <tr>
      <td></td>
      <td>Issuer &lt;Issr&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>344</td>
    </tr>
    <tr>
      <td></td>
      <td>CountryOfResidence &lt;CtryOfRes&gt;</td>
      <td>[0..1]</td>
      <td>CodeSet</td>
      <td>C7</td>
      <td>344</td>
    </tr>
    <tr>
      <td></td>
      <td>ContactDetails &lt;CtctDtls&gt;</td>
      <td>[0..1]</td>
      <td>±</td>
      <td></td>
      <td>344</td>
    </tr>
  </tbody>
</table>

### 3.4.3.7.12.19.2 Agent <Ag>

Presence: [1..1]

Definition: Identification of a financial institution.

---

<!-- Page 158 -->

Agent <Agt> contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on page 320 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | FinancialInstitutionIdentification <FinInstlD> | [1..1] | | | 321 |
| | BICFI <BICFI> | [0..1] | IdentifierSet | C6 | 321 |
| | ClearingSystemMemberIdentification <ClrSysMmbId> | [0..1] | ± | | 322 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 322 |
| | Name <Nm> | [0..1] | Text | | 322 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 322 |
| | Other <Othr> | [0..1] | ± | | 323 |
| | BranchIdentification <BrnchId> | [0..1] | | | 324 |
| | Identification <Id> | [0..1] | Text | | 324 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 324 |
| | Name <Nm> | [0..1] | Text | | 324 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 324 |

### 3.4.3.7.12.20 CreditorAccount <CdtrAcct>

*Presence:* [0..1]

*Definition:* Unambiguous identification of the account of the creditor to which a credit entry will be posted as a result of the payment transaction.

*Impacted by:* C16 "IdentificationOrProxyPresenceRule", C15 "IdentificationAndProxyGuideline"

CreditorAccount <CdtrAcct> contains the following elements (see "CashAccount40" on page 309 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Identification <Id> | [0..1] | ± | | 310 |
| | Type <Tp> | [0..1] | ± | | 310 |
| | Currency <Ccy> | [0..1] | CodeSet | C2 | 310 |
| | Name <Nm> | [0..1] | Text | | 311 |
| | Proxy <Prxy> | [0..1] | ± | | 311 |

---

<!-- Page 159 -->

Constraints

- **IdentificationAndProxyGuideline**

  If the account identification is not defined through a conventional identification such as an email address or a mobile number, then the proxy element should be used for the identification of the account.

- **IdentificationOrProxyPresenceRule**

  Identification must be present or Proxy must be present. Both may be present.

  ```
  Following Must be True
  /Identification Must be present
  Or      /Proxy Must be present
  ```

### 3.4.3.7.12.21 UltimateCreditor <UltmtCdr>

*Presence:* [0..1]

*Definition:* Ultimate party to which an amount of money is due.

**UltimateCreditor <UltmtCdr>** contains one of the following **Party50Choice** elements



| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| (Or | **Party** <Pty> | [1..1] | † |  | 159 |
| Or) | **Agent** <Agt> | [1..1] | † |  | 160 |

### 3.4.3.7.12.21.1 Party <Pty>

*Presence:* [1..1]

*Definition:* Identification of a person or an organisation.

---

<!-- Page 160 -->

Party <Pty> contains the following elements (see "PartyIdentification27" on page 336 for details)



<table>
  <thead>
    <tr>
      <th>Or</th>
      <th>MessageElement&lt;XML Tag&gt;</th>
      <th>Mult.</th>
      <th>Type</th>
      <th>Constr. No.</th>
      <th>Page</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td>Name &lt;Nm&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>337</td>
    </tr>
    <tr>
      <td></td>
      <td>PostalAddress &lt;PstlAdr&gt;</td>
      <td>[0..1]</td>
      <td>±</td>
      <td></td>
      <td>338</td>
    </tr>
    <tr>
      <td></td>
      <td>Identification &lt;Id&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>338</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>OrganisationIdentification &lt;OrgId&gt;</td>
      <td>[1..1]</td>
      <td></td>
      <td></td>
      <td>339</td>
    </tr>
    <tr>
      <td></td>
      <td>AnyBIC &lt;AnyBIC&gt;</td>
      <td>[0..1]</td>
      <td>IdentifierSet</td>
      <td>C5</td>
      <td>340</td>
    </tr>
    <tr>
      <td></td>
      <td>LEI &lt;LEI&gt;</td>
      <td>[0..1]</td>
      <td>IdentifierSet</td>
      <td></td>
      <td>340</td>
    </tr>
    <tr>
      <td></td>
      <td>Other &lt;Othr&gt;</td>
      <td>[0..*]</td>
      <td></td>
      <td></td>
      <td>340</td>
    </tr>
    <tr>
      <td></td>
      <td>Identification &lt;Id&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td></td>
      <td>SchemaName &lt;SchmeNm&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Code &lt;Cd&gt;</td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Proprietary &lt;Prtry&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td></td>
      <td>Issuer &lt;Issr&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>PrivateIdentification &lt;PrvtId&gt;</td>
      <td>[1..1]</td>
      <td></td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td></td>
      <td>DateAndPlaceOfBirth &lt;DtAndPlcOfBrth&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>342</td>
    </tr>
    <tr>
      <td></td>
      <td>BirthDate &lt;BirthDt&gt;</td>
      <td>[1..1]</td>
      <td>Date</td>
      <td></td>
      <td>342</td>
    </tr>
    <tr>
      <td></td>
      <td>ProvinceOfBirth &lt;PvcOfBrth&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>342</td>
    </tr>
    <tr>
      <td></td>
      <td>CityOfBirth &lt;CityOfBrth&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>CountryOfBirth &lt;CtryOfBrth&gt;</td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td>C7</td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>Other &lt;Othr&gt;</td>
      <td>[0..*]</td>
      <td></td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>Identification &lt;Id&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>SchemaName &lt;SchmeNm&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Code &lt;Cd&gt;</td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td></td>
      <td>344</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Proprietary &lt;Prtry&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>344</td>
    </tr>
    <tr>
      <td></td>
      <td>Issuer &lt;Issr&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>344</td>
    </tr>
    <tr>
      <td></td>
      <td>CountryOfResidence &lt;CtryOfRes&gt;</td>
      <td>[0..1]</td>
      <td>CodeSet</td>
      <td>C7</td>
      <td>344</td>
    </tr>
    <tr>
      <td></td>
      <td>ContactDetails &lt;CtctDtls&gt;</td>
      <td>[0..1]</td>
      <td>±</td>
      <td></td>
      <td>344</td>
    </tr>
  </tbody>
</table>

### 3.4.3.7.12.21.2 Agent <Agt>

*Presence:* [1..1]

*Definition:* Identification of a financial institution.

---

<!-- Page 161 -->

Agent **<Agt>** contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on page 320 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | FinancialInstitutionIdentification <FinInstnId> | [1..1] | | | 321 |
| | BICFI <BICFI> | [0..1] | IdentifierSet | C6 | 321 |
| | ClearingSystemMemberIdentification <ClrSysMmbId> | [0..1] | ± | | 322 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 322 |
| | Name <Nm> | [0..1] | Text | | 322 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 322 |
| | Other <Othr> | [0..1] | ± | | 323 |
| | BranchIdentification <BrnchId> | [0..1] | | | 324 |
| | Identification <Id> | [0..1] | Text | | 324 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 324 |
| | Name <Nm> | [0..1] | Text | | 324 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 324 |

### 3.4.3.7.12.22 Purpose <Purp>

*Presence:* [0..1]

*Definition:* Underlying reason for the payment transaction.

Usage:

Purpose is used by the end customers, that is initiating party, (ultimate) debtor, (ultimate) creditor to provide information concerning the nature of the payment. Purpose is a content element, which is not used for processing by any of the agents involved in the payment chain.

**Purpose <Purp>** contains one of the following elements (see "Purpose2Choice" on page 334 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| (Or | Code <Cd> | [1..1] | CodeSet | | 335 |
| (Or) | Proprietary <Prtry> | [1..1] | Text | | 335 |

### 3.4.3.7.13 Supplementary Data <SplmtryData>

*Presence:* [0..*]

*Definition:* Additional information that cannot be captured in the structured elements and/or any other specific block.

*Impacted by:* C32 "SupplementaryDataRule"

---

<!-- Page 162 -->

SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on page 334 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | PlaceAndName <PlcAndNm> | [0..1] | Text | | 334 |
| | Envelope <Envlp> | [1..1] | (External Schema) | | 334 |

**Constraints**

* **SupplementaryDataRule**

This component may not be used without the explicit approval of a SEG and submission to the RA of ISO 20022 compliant structure(s) to be used in the Envelope element.

## 3.4.4 SupplementaryData <SplmtryData>

*Presence: [0..]*

*Definition: Additional information that cannot be captured in the structured elements and/or any other specific block.*

*Impacted by: C32 "SupplementaryDataRule"*

SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on page 334 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | PlaceAndName <PlcAndNm> | [0..1] | Text | | 334 |
| | Envelope <Envlp> | [1..1] | (External Schema) | | 334 |

**Constraints**

* **SupplementaryDataRule**

This component may not be used without the explicit approval of a SEG and submission to the RA of ISO 20022 compliant structure(s) to be used in the Envelope element.

---

<!-- Page 163 -->

# 4 pain.007.001.12 CustomerPaymentReversalV12

## 4.1 MessageDefinition Functionality

Scope

The CustomerPaymentReversal message is sent by the initiating party to the next party in the payment chain. It is used to reverse a payment previously executed.

Usage

The CustomerPaymentReversal message is exchanged between a non-financial institution customer and an agent to reverse a CustomerDirectDebitInitiation message that has been settled. The result will be a credit on the debtor account.

The CustomerPaymentReversal message refers to the original CustomerDirectDebitInitiation message by means of references only or by means of references and a set of elements from the original instruction.

The CustomerPaymentReversal message can be used in domestic and cross-border scenarios.

Outline

The CustomerPaymentReversalV12 MessageDefinition is composed of 4 MessageBuildingBlocks:

A. GroupHeader

Set of characteristics shared by all individual transactions included in the message.

B. OriginalGroupInformation

Information concerning the original group of transactions, to which the message refers.

C. OriginalPaymentInformationAndReversal

Information concerning the original payment information, to which the reversal message refers.

D. SupplementaryData

Additional information that cannot be captured in the structured elements and/or any other specific block.

---

<!-- Page 164 -->

## 4.2 Structure



<table>
  <thead>
    <tr>
      <th>Or</th>
      <th>MessageElement\BuildingBlock&lt;XML Tag&gt;</th>
      <th>Mult.</th>
      <th>Type</th>
      <th>Constr. No.</th>
      <th>Page</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td><i>Message root &lt;Document&gt; &lt;CstmrPmtRvsl&gt;</i></td>
      <td>[1..1]</td>
      <td></td>
      <td>C11, C12, C13, C27, C9</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td><b>GroupHeader</b> <i>&lt;GrpHdr&gt;</i></td>
      <td>[1..1]</td>
      <td></td>
      <td>C6, C10</td>
      <td>171</td>
    </tr>
    <tr>
      <td></td>
      <td><b>MessageIdentification</b> <i>&lt;MsgId&gt;</i></td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>171</td>
    </tr>
    <tr>
      <td></td>
      <td><b>CreationDateTime</b> <i>&lt;CreDtTm&gt;</i></td>
      <td>[1..1]</td>
      <td>Date Time</td>
      <td></td>
      <td>172</td>
    </tr>
    <tr>
      <td></td>
      <td><b>Authorisation</b> <i>&lt;Authstrn&gt;</i></td>
      <td>[0..2]</td>
      <td>±</td>
      <td></td>
      <td>172</td>
    </tr>
    <tr>
      <td></td>
      <td><b>NumberOfTransactions</b> <i>&lt;NbOfTxs&gt;</i></td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>172</td>
    </tr>
    <tr>
      <td></td>
      <td><b>ControlSum</b> <i>&lt;CtrlSum&gt;</i></td>
      <td>[0..1]</td>
      <td>Quantity</td>
      <td></td>
      <td>172</td>
    </tr>
    <tr>
      <td></td>
      <td><b>GroupReversal</b> <i>&lt;GrpRvsl&gt;</i></td>
      <td>[0..1]</td>
      <td>Indicator</td>
      <td></td>
      <td>172</td>
    </tr>
    <tr>
      <td></td>
      <td><b>InitiatingParty</b> <i>&lt;InitgPty&gt;</i></td>
      <td>[0..1]</td>
      <td>±</td>
      <td></td>
      <td>173</td>
    </tr>
    <tr>
      <td></td>
      <td><b>ForwardingAgent</b> <i>&lt;FwdgAgt&gt;</i></td>
      <td>[0..1]</td>
      <td>±</td>
      <td></td>
      <td>174</td>
    </tr>
    <tr>
      <td></td>
      <td><b>DebtorAgent</b> <i>&lt;DbtrAgt&gt;</i></td>
      <td>[0..1]</td>
      <td>±</td>
      <td></td>
      <td>175</td>
    </tr>
    <tr>
      <td></td>
      <td><b>CreditorAgent</b> <i>&lt;CdtrAgt&gt;</i></td>
      <td>[0..1]</td>
      <td>±</td>
      <td></td>
      <td>176</td>
    </tr>
    <tr>
      <td></td>
      <td><b>OriginalGroupInformation</b> <i>&lt;OrgnlGrpInf&gt;</i></td>
      <td>[1..1]</td>
      <td></td>
      <td></td>
      <td>176</td>
    </tr>
    <tr>
      <td></td>
      <td><b>OriginalMessageIdentification</b> <i>&lt;OrgnlMsgId&gt;</i></td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>177</td>
    </tr>
    <tr>
      <td></td>
      <td><b>OriginalMessageNameIdentification</b> <i>&lt;OrgnlMsgNmId&gt;</i></td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>177</td>
    </tr>
    <tr>
      <td></td>
      <td><b>OriginalCreationDateTime</b> <i>&lt;OrgnlCreDtTm&gt;</i></td>
      <td>[0..1]</td>
      <td>Date Time</td>
      <td></td>
      <td>177</td>
    </tr>
    <tr>
      <td></td>
      <td><b>ReversalReasonInformation</b> <i>&lt;RvslRsnInf&gt;</i></td>
      <td>[0..*]</td>
      <td></td>
      <td></td>
      <td>177</td>
    </tr>
    <tr>
      <td></td>
      <td><b>Originator</b> <i>&lt;Orgtr&gt;</i></td>
      <td>[0..1]</td>
      <td>±</td>
      <td></td>
      <td>177</td>
    </tr>
    <tr>
      <td></td>
      <td><b>Reason</b> <i>&lt;Rsn&gt;</i></td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>178</td>
    </tr>
    <tr>
      <td>Or</td>
      <td><b>Code</b> <i>&lt;Cd&gt;</i></td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td></td>
      <td>179</td>
    </tr>
    <tr>
      <td>Or)</td>
      <td><b>Proprietary</b> <i>&lt;Pry&gt;</i></td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>179</td>
    </tr>
    <tr>
      <td></td>
      <td><b>AdditionalInformation</b> <i>&lt;AddtlInf&gt;</i></td>
      <td>[0..*]</td>
      <td>Text</td>
      <td></td>
      <td>179</td>
    </tr>
    <tr>
      <td></td>
      <td><b>OriginalPaymentInformationAndReversal</b> <i>&lt;OrgnlPmtInfAndRvsl&gt;</i></td>
      <td>[0..*]</td>
      <td></td>
      <td>C19, C20, C21</td>
      <td>179</td>
    </tr>
    <tr>
      <td></td>
      <td><b>ReversalPaymentInformationIdentification</b> <i>&lt;RvslPmtInfId&gt;</i></td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>184</td>
    </tr>
    <tr>
      <td></td>
      <td><b>OriginalPaymentInformationIdentification</b> <i>&lt;OrgnlPmtInfId&gt;</i></td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>184</td>
    </tr>
    <tr>
      <td></td>
      <td><b>OriginalNumberOfTransactions</b> <i>&lt;OrgnlNbOfTxs&gt;</i></td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>184</td>
    </tr>
    <tr>
      <td></td>
      <td><b>OriginalControlSum</b> <i>&lt;OrgnlCtrlSum&gt;</i></td>
      <td>[0..1]</td>
      <td>Quantity</td>
      <td></td>
      <td>184</td>
    </tr>
  </tbody>
</table>

---

<!-- Page 165 -->

| Or | MessageElement/BuildingBlock<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **BatchBooking** <BtchBookg> | [0..1] | Indicator | | 184 |
| | **PaymentInformationReversal** <PmtInfRvsl> | [0..1] | Indicator | | 184 |
| | **ReversalReasonInformation** <RvslRsnInf> | [0..*] | | | 185 |
| | **Originator** <Orgtr> | [0..1] | ± | | 185 |
| | **Reason** <Rsn> | [0..1] | | | 186 |
| (Or | **Code** <Cd> | [1..1] | CodeSet | | 187 |
| Or) | **Proprietary** <Prtry> | [1..1] | Text | | 187 |
| | **AdditionalInformation** <AddtlInf> | [0..*] | Text | | 187 |
| | **TransactionInformation** <TxInf> | [0..*] | | | 187 |
| | **ReversalIdentification** <RvslId> | [0..1] | Text | | 191 |
| | **OriginalInstructionIdentification** <OrgnlInstrId> | [0..1] | Text | | 191 |
| | **OriginalEndToEndIdentification** <OrgnlEndToEndId> | [0..1] | Text | | 191 |
| | **OriginalUETR** <OrgnlUETR> | [0..1] | IdentifierSet | | 191 |
| | **OriginalInstructedAmount** <OrgnlInstdAmt> | [0..1] | Amount | C1, C8 | 191 |
| | **ReversedInstructedAmount** <RvslInstdAmt> | [0..1] | Amount | C1, C8 | 192 |
| | **ChargeBearer** <ChrgBr> | [0..1] | CodeSet | | 192 |
| | **ReversalReasonInformation** <RvslRsnInf> | [0..*] | | | 193 |
| | **Originator** <Orgtr> | [0..1] | ± | | 193 |
| | **Reason** <Rsn> | [0..1] | | | 194 |
| (Or | **Code** <Cd> | [1..1] | CodeSet | | 195 |
| Or) | **Proprietary** <Prtry> | [1..1] | Text | | 195 |
| | **AdditionalInformation** <AddtlInf> | [0..*] | Text | | 195 |
| | **OriginalTransactionReference** <OrgnlTxRef> | [0..1] | | | 195 |
| | **InterbankSettlementAmount** <IntrBkSttlmAmt> | [0..1] | Amount | C1, C8 | 198 |
| | **Amount** <Amt> | [0..1] | ± | | 198 |
| | **InterbankSettlementDate** <IntrBkSttlmDt> | [0..1] | Date | | 199 |
| | **RequestedCollectionDate** <ReqdColltnDt> | [0..1] | Date | | 199 |
| | **RequestedExecutionDate** <ReqdExctnDt> | [0..1] | ± | | 199 |
| | **CreditorScheduleIdentification** <CdrSchedId> | [0..1] | ± | | 199 |
| | **SettlementInformation** <SttlmInf> | [0..1] | | C17, C18, C23, C24, C25, | 200 |

---

<!-- Page 166 -->

| Or | MessageElement/BuildingBlock<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | | | | C26, C29, C30 | |
| | **SettlementMethod** <i>&lt;SttlMtd&gt;</i> | [1..1] | CodeSet | | 202 |
| | **SettlementAccount** <i>&lt;SttlAcct&gt;</i> | [0..1] | ± | C16, C15 | 203 |
| | **ClearingSystem** <i>&lt;ClrSys&gt;</i> | [0..1] | | | 203 |
| [Or | **Code** <i>&lt;Cd&gt;</i> | [1..1] | CodeSet | | 204 |
| Or] | **Proprietary** <i>&lt;Pry&gt;</i> | [1..1] | Text | | 204 |
| | **InstructingReimbursementAgent** <i>&lt;InstrgRmbrmntAgnt&gt;</i> | [0..1] | ± | | 204 |
| | **InstructingReimbursementAgentAccount** <i>&lt;InstrgRmbrmntAgntAcct&gt;</i> | [0..1] | ± | C16, C15 | 205 |
| | **InstructedReimbursementAgent** <i>&lt;InstdRmbrmntAgnt&gt;</i> | [0..1] | ± | | 205 |
| | **InstructedReimbursementAgentAccount** <i>&lt;InstdRmbrmntAgntAcct&gt;</i> | [0..1] | ± | C16, C15 | 206 |
| | **ThirdReimbursementAgent** <i>&lt;ThrdRmbrmntAgnt&gt;</i> | [0..1] | ± | | 207 |
| | **ThirdReimbursementAgentAccount** <i>&lt;ThrdRmbrmntAgntAcct&gt;</i> | [0..1] | ± | C16, C15 | 207 |
| | **PaymentTypeInformation** <i>&lt;PmtTpinf&gt;</i> | [0..1] | ± | | 208 |
| | **PaymentMethod** <i>&lt;PmtMtd&gt;</i> | [0..1] | CodeSet | | 209 |
| | **MandateRelatedInformation** <i>&lt;MndtRltdInf&gt;</i> | [0..1] | | | 209 |
| [Or | **DirectDebitMandate** <i>&lt;DirectDbtMndt&gt;</i> | [0..1] | | C2, C3 | 211 |
| | **MandateIdentification** <i>&lt;MndtId&gt;</i> | [0..1] | Text | | 213 |
| | **DateOfSignature** <i>&lt;DtOfSgntr&gt;</i> | [0..1] | Date | | 213 |
| | **AmendmentIndicator** <i>&lt;AmdmntInd&gt;</i> | [0..1] | Indicator | | 213 |
| | **AmendmentInformationDetails** <i>&lt;AmdmntInfDtls&gt;</i> | [0..1] | | | 213 |
| | **OriginalMandateIdentification** <i>&lt;OrgnlMndtId&gt;</i> | [0..1] | Text | | 214 |
| | **OriginalCreditorSchemeIdentification** <i>&lt;OrgnlCdrSchemId&gt;</i> | [0..1] | ± | | 214 |
| | **OriginalCreditorAgent** <i>&lt;OrgnlCddrAgnt&gt;</i> | [0..1] | ± | | 215 |
| | **OriginalCreditorAgentAccount** <i>&lt;OrgnlCddrAgntAcct&gt;</i> | [0..1] | ± | C16, C15 | 216 |
| | **OriginalDebtor** <i>&lt;OrgnlDbtr&gt;</i> | [0..1] | ± | | 217 |
| | **OriginalDebtorAccount** <i>&lt;OrgnlDbtrAcct&gt;</i> | [0..1] | ± | C16, C15 | 218 |
| | **OriginalDebtorAgent** <i>&lt;OrgnlDbtrAgnt&gt;</i> | [0..1] | ± | | 219 |
| | **OriginalDebtorAgentAccount** <i>&lt;OrgnlDbtrAgntAcct&gt;</i> | [0..1] | ± | C16, C15 | 220 |

---

<!-- Page 167 -->

| Or | MessageElement/BuildingBlock/<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **OriginalFinalCollectionDate** `<OrgnlFinColltnDt>` | [0..1] | Date | | 221 |
| | **OriginalFrequency** `<OrgnlFrqcy>` | [0..1] | ± | | 221 |
| | **OriginalReason** `<OrgnlRsn>` | [0..1] | | | 221 |
| {Or | **Code** `<Cd>` | [1..1] | CodeSet | | 221 |
| Or] | **Proprietary** `<Ptry>` | [1..1] | Text | | 221 |
| | **OriginalTrackingDays** `<OrgnlTrckgDays>` | [0..1] | Text | | 222 |
| | **ElectronicSignature** `<ElctrncSgntr>` | [0..1] | Text | | 222 |
| | **FirstCollectionDate** `<FirstColltnDt>` | [0..1] | Date | | 222 |
| | **FinalCollectionDate** `<FinlColltnDt>` | [0..1] | Date | | 222 |
| | **Frequency** `<Frqcy>` | [0..1] | ± | | 222 |
| | **Reason** `<Rsn>` | [0..1] | | | 222 |
| {Or | **Code** `<Cd>` | [1..1] | CodeSet | | 223 |
| Or] | **Proprietary** `<Ptry>` | [1..1] | Text | | 223 |
| | **TrackingDays** `<TrckgDays>` | [0..1] | Text | | 223 |
| Or] | **CreditTransferMandate** `<CdtTrfMndt>` | [0..1] | ± | | 223 |
| | **RemittanceInformation** `<RmtnInf>` | [0..1] | ± | | 224 |
| | **UltimateDebtor** `<UltmtDbtr>` | [0..1] | | | 224 |
| {Or | **Party** `<Pty>` | [1..1] | ± | | 224 |
| Or] | **Agent** `<Agt>` | [1..1] | ± | | 225 |
| | **Debtor** `<Dbtr>` | [0..1] | | | 226 |
| {Or | **Party** `<Pty>` | [1..1] | ± | | 226 |
| Or] | **Agent** `<Agt>` | [1..1] | ± | | 227 |
| | **DebtorAccount** `<DbtrAcct>` | [0..1] | ± | C16, C15 | 228 |
| | **DebtorAgent** `<DbtrAgt>` | [0..1] | ± | | 229 |
| | **DebtorAgentAccount** `<DbtrAgtAcct>` | [0..1] | ± | C16, C15 | 229 |
| | **CreditorAgent** `<CdtrAgt>` | [0..1] | ± | | 230 |
| | **CreditorAgentAccount** `<CdtrAgtAcct>` | [0..1] | ± | C16, C15 | 231 |
| | **Creditor** `<Cdtr>` | [0..1] | | | 232 |
| {Or | **Party** `<Pty>` | [1..1] | ± | | 232 |
| Or] | **Agent** `<Agt>` | [1..1] | ± | | 233 |

---

<!-- Page 168 -->

| Or | MessageElement/BuildingBlock<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **CreditorAccount** *<CdtrAcct>* | [0..1] | ± | C16, C15 | 234 |
| | **UltimateCreditor** *<UltmtCdr>* | [0..1] | | | 235 |
| (Or | **Party** *<Pty>* | [1..1] | ± | | 235 |
| Or) | **Agent** *<Agnt>* | [1..1] | ± | | 236 |
| | **Purpose** *<Purp>* | [0..1] | ± | | 237 |
| | **SupplementaryData** *<SplmtryData>* | [0..*] | ± | C28 | 237 |
| | **SupplementaryData** *<SplmtryData>* | [0..*] | ± | C28 | 238 |

## 4.3 Constraints

**C1** **ActiveOrHistoricCurrency**

The Currency Code must be registered, or have already been registered. Valid active or historic currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and may be or not be withdrawn on the day the message containing the Currency is exchanged.

**C2** **AmendmentIndicatorFalseRule**

If AmendmentIndicator is false, then AmendmentInformationDetails is not allowed.

**C3** **AmendmentIndicatorTrueRule**

If AmendmentIndicator is true, then AmendmentInformationDetails must be present.

**C4** **AnyBIC**

Only a valid Business identifier code is allowed. Business identifier codes for financial or non-financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.

**C5** **BICFI**

Valid BICs for financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous characters.

**C6** **ControlSumAndGroupReversalRule**

If GroupReversal is true, then ControlSum is not allowed.

**C7** **Country**

The code is checked against the list of country names obtained from the United Nations (ISO 3166, Alpha-2 code).

**C8** **CurrencyAmount**

The number of fractional digits (or minor unit of currency) must comply with ISO 4217.

Note: The decimal separator is a dot.

---

<!-- Page 169 -->

| | |
|---|---|
| C9 | **GroupReversalAndNumberOfTransactionsGuideline**<br>If GroupHeader/GroupReversal is false and OriginalPaymentInformationAndReversal[*]/ PaymentInformationReversal is false, then NumberOfTransactions must equal the number of occurrences of OriginalPaymentInformationAndReversal[*]/TransactionInformation.<br>*This constraint is defined at the MessageDefinition level.* |
| C10 | **GroupReversalAndNumberOfTransactionsGuideline**<br>If GroupReversal is true, then NumberOfTransactions equals the number of transactions in the original message. |
| C11 | **GroupReversalAndPaymentInformationNotPresentRule**<br>If GroupHeader/GroupReversal is true, then OriginalPaymentInformationAndReversal is not allowed.<br>On Condition<br>/GroupHeader/GroupReversal is present<br>And /GroupHeader/GroupReversal is equal to value 'true'<br>Following Must be True<br>/OriginalPaymentInformationAndReversal[*] Must be absent<br>*This constraint is defined at the MessageDefinition level.* |
| C12 | **GroupReversalAndPaymentInformationPresentRule**<br>If GroupHeader/GroupReversal is false, then at least one occurrence of OriginalPaymentInformationAndReversal must be present.<br>On Condition<br>/GroupHeader/GroupReversal is present<br>And /GroupHeader/GroupReversal is equal to value 'false'<br>Following Must be True<br>/OriginalPaymentInformationAndReversal[1] Must be present<br>*This constraint is defined at the MessageDefinition level.* |
| C13 | **GroupReversalAndReasonRule**<br>If GroupHeader/GroupReversal is true, then OriginalGroupInformation/ ReversalReasonInformation/Reason must be present.<br>On Condition<br>/GroupHeader/GroupReversal is present<br>And /GroupHeader/GroupReversal is equal to value 'true'<br>Following Must be True<br>/OriginalGroupInformation/ReversalReasonInformation[*]/Reason Must be present<br>*This constraint is defined at the MessageDefinition level.* |
| C14 | **IBAN**<br>A valid IBAN consists of all three of the following components: Country Code, check digits and BBAN. |
| C15 | **IdentificationAndProxyGuideline**<br>If the account identification is not defined through a conventional identification such as an email address or a mobile number, then the proxy element should be used for the identification of the account. |
| C16 | **IdentificationOrProxyPresenceRule**<br>Identification must be present or Proxy must be present. Both may be present. |

---

<!-- Page 170 -->

| Code | Rule | Description |
| :--- | :--- | :--- |
| C17 | **InstructedReimbursementAgentAccountRule** | If InstructedReimbursementAgentAccount is present, then InstructedReimbursementAgent must be present. |
| C18 | **InstructingReimbursementAgentAccountRule** | If InstructingReimbursementAgentAccount is present, then InstructingReimbursementAgent must be present. |
| C19 | **PaymentInformationReversalAndReasonRule** | If PaymentInformationReversal is true, then ReversalReasonInformation/ReversalReason must present. |
| C20 | **PaymentInformationReversalAndTransactionInformationNotPresentRule** | If PaymentInformationReversal is true, then TransactionInformation is not allowed. |
| C21 | **PaymentInformationReversalAndTransactionInformationPresentRule** | If PaymentInformationReversal is false, then at least one occurrence of TransactionInformation must be present. |
| C22 | **RemittanceAmountAndTypeGuideline** | If Type/Code is equal to CREN, DUPA or REMI for RemittanceAmountAndType, RemittanceAmountAndType must not be repeated. |
| C23 | **SettlementMethodAgentRule** | If SettlementMethod is equal to INDA or INGA, then ReimbursementAgent(s) and ClearingSystem are not allowed. |
| C24 | **SettlementMethodClearingRule** | If SettlementMethod is equal to CLRG, then SettlementAccount and ReimbursementAgent(s) are not allowed. |
| C25 | **SettlementMethodCoverAgentRule** | If SettlementMethod is equal to COVE, then InstructedReimbursementAgent or InstructingReimbursementAgent must be present. |
| C26 | **SettlementMethodCoverRule** | If SettlementMethod is equal to COVE, then SettlementAccount and ClearingSystem are not allowed. |
| C27 | **SupplementaryDataRule** | The SupplementaryData building block at message level must not be used to provide additional information about a transaction. The SupplementaryData element at transaction level should be used for that purpose.<br>*This constraint is defined at the MessageDefinition level.* |
| C28 | **SupplementaryDataRule** | This component may not be used without the explicit approval of a SEG and submission to the RA of ISO 20022 compliant structure(s) to be used in the Envelope element. |
| C29 | **ThirdReimbursementAgentAccountRule** | If ThirdReimbursementAgentAccount is present, then ThirdReimbursementAgent must be present. |

---

<!-- Page 171 -->

C30 | **ThirdReimbursementAgentRule**
---|---
| If ThirdReimbursementAgent is present, then InstructingReimbursementAgent and InstructedReimbursementAgent must both be present.

## 4.4 Message Building Blocks

This chapter describes the MessageBuildingBlocks of this MessageDefinition.

## 4.4.1 GroupHeader <GrpHdr>

*Presence: [1..1]*

*Definition: Set of characteristics shared by all individual transactions included in the message.*

*Impacted by: C6 "ControlSumAndGroupReversalRule"; C10 "GroupReversalAndNumberOfTransactionsGuideline"*

**GroupHeader <GrpHdr>** contains the following **GroupHeader124** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | **MessageIdentification** <MsgId> | [1..1] | Text | | 171 |
| | **CreationDateTime** <CreDtTm> | [1..1] | DateTime | | 172 |
| | **Authorisation** <Authstr> | [0..2] | ± | | 172 |
| | **NumberOfTransactions** <NbOfTxs> | [1..1] | Text | | 172 |
| | **ControlSum** <CtrlSum> | [0..1] | Quantity | | 172 |
| | **GroupReversal** <GrpRvsl> | [0..1] | Indicator | | 172 |
| | **InitiatingParty** <InstdPty> | [0..1] | ± | | 173 |
| | **ForwardingAgent** <FwdgAgt> | [0..1] | ± | | 174 |
| | **DebtorAgent** <DbtrAgt> | [0..1] | ± | | 175 |
| | **CreditorAgent** <CdtrAgt> | [0..1] | ± | | 176 |

### Constraints

*   **ControlSumAndGroupReversalRule**

    If GroupReversal is true, then ControlSum is not allowed.

    On Condition
    /GroupReversal is present
    And /GroupReversal is equal to value 'true'
    Following Must be True
    /ControlSum Must be absent

*   **GroupReversalAndNumberOfTransactionsGuideline**

    If GroupReversal is true, then NumberOfTransactions equals the number of transactions in the original message.

### 4.4.1.1 MessageIdentification <MsgId>

*Presence: [1..1]*

---

<!-- Page 172 -->

*Definition: Point to point reference, as assigned by the instructing party, and sent to the next party in the chain to unambiguously identify the message.*

*Usage: The instructing party has to make sure that MessageIdentification is unique per instructed party for a pre-agreed period.*

*Datatype: "Max35Text" on page 431*

## 4.4.1.2 CreationDateTime <CreDtTm>

*Presence: [1..1]*

*Definition: Date and time at which the message was created.*

*Datatype: "ISODateTime" on page 425*

## 4.4.1.3 Authorisation <Authn>

*Presence: [0..2]*

*Definition: User identification or any user key to be used to check whether the initiating party is allowed to initiate transactions from the account specified in the message.*

*Usage: The content is not of a technical nature, but reflects the organisational structure at the initiating side.*

The authorisation element can typically be used in relay scenarios, payment initiations, payment returns or payment reversals that are initiated on behalf of a party different from the initiating party.

**Authorisation <Authn>** contains one of the following elements (see "**Authorisation1Choice**" on page 336 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| (Or | Code <Cd> | [1..1] | CodeSet | | 336 |
| Or) | Proprietary <Ptry> | [1..1] | Text | | 336 |

## 4.4.1.4 NumberOfTransactions <NbOfTxs>

*Presence: [1..1]*

*Definition: Number of individual transactions contained in the message.*

*Datatype: "Max15NumericText" on page 430*

## 4.4.1.5 ControlSum <CtrlSum>

*Presence: [0..1]*

*Definition: Total of all individual amounts included in the message, irrespective of currencies.*

*Datatype: "DecimalNumber" on page 427*

## 4.4.1.6 GroupReversal <GrpRvsl>

*Presence: [0..1]*

*Definition: Indicates whether the reversal applies to the whole group of transactions or to individual transactions within the original group.*

*Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 427):*

---

<!-- Page 173 -->

- *Meaning When True:* True
- *Meaning When False:* False

**4.4.1.7 InitiatingParty** \<InitgPty\>

*Presence:* [0..1]

*Definition:* Party that initiates the reversal message.

Usage: This can be either the creditor or a party that initiates the reversal of the direct debit on behalf of the creditor.

---

<!-- Page 174 -->

InitiatingParty <InitgPty> contains the following elements (see "PartyIdentification27" on page 336 for details)



| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | Name <Nm> | [0..1] | Text | | 337 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 338 |
| | Identification <Id> | [0..1] | | | 338 |
| (Or | OrganisationIdentification <OrgId> | [1..1] | | | 339 |
| | AnyBIC <AnyBIC> | [0..1] | IdentifierSet | C5 | 340 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 340 |
| | Other <Othr> | [0..*] | | | 340 |
| | Identification <Id> | [1..1] | Text | | 341 |
| | SchemeName <SchmeNm> | [0..1] | | | 341 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 341 |
| Or) | Proprietary <Prtry> | [1..1] | Text | | 341 |
| | Issuer <Issr> | [0..1] | Text | | 341 |
| (Or) | PrivateIdentification <PrvtId> | [1..1] | | | 341 |
| | DateAndPlaceOfBirth <DtAndPlcOfBirth> | [0..1] | | | 342 |
| | BirthDate <BirthDt> | [1..1] | Date | | 342 |
| | ProvinceOfBirth <PrvcOfBirth> | [0..1] | Text | | 342 |
| | CityOfBirth <CityOfBirth> | [1..1] | Text | | 343 |
| | CountryOfBirth <CtryOfBirth> | [1..1] | CodeSet | C7 | 343 |
| | Other <Othr> | [0..*] | | | 343 |
| | Identification <Id> | [1..1] | Text | | 343 |
| | SchemeName <SchmeNm> | [0..1] | | | 343 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 344 |
| Or) | Proprietary <Prtry> | [1..1] | Text | | 344 |
| | Issuer <Issr> | [0..1] | Text | | 344 |
| | CountryOfResidence <CtryOfRes> | [0..1] | CodeSet | C7 | 344 |
| | ContactDetails <CtctDtls> | [0..1] | ± | | 344 |

### 4.4.1.8 ForwardingAgent <FwdgAgt>

*Presence: [0..1]*

*Definition: Financial institution that receives the instruction from the initiating party and forwards it to the next agent in the payment chain.*

---

<!-- Page 175 -->

**ForwardingAgent** *<FwdgAgt>* contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on page 320 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | FinancialInstitutionIdentification *<FinInstId>* | [1..1] | | | 321 |
| | BICFI *<BICFI>* | [0..1] | IdentifierSet | C6 | 321 |
| | ClearingSystemMemberIdentification *<ClrSysMmbId>* | [0..1] | ± | | 322 |
| | LEI *<LEI>* | [0..1] | IdentifierSet | | 322 |
| | Name *<Nm>* | [0..1] | Text | | 322 |
| | PostalAddress *<PstlAdr>* | [0..1] | ± | | 322 |
| | Other *<Othr>* | [0..1] | ± | | 323 |
| | BranchIdentification *<BrnchId>* | [0..1] | | | 324 |
| | Identification *<Id>* | [0..1] | Text | | 324 |
| | LEI *<LEI>* | [0..1] | IdentifierSet | | 324 |
| | Name *<Nm>* | [0..1] | Text | | 324 |
| | PostalAddress *<PstlAdr>* | [0..1] | ± | | 324 |

## 4.4.1.9 DebtorAgent <DbtrAgt>

Presence: [0..1]

Definition: Financial institution servicing an account for the debtor.

**DebtorAgent** *<DbtrAgt>* contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on page 320 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | FinancialInstitutionIdentification *<FinInstId>* | [1..1] | | | 321 |
| | BICFI *<BICFI>* | [0..1] | IdentifierSet | C6 | 321 |
| | ClearingSystemMemberIdentification *<ClrSysMmbId>* | [0..1] | ± | | 322 |
| | LEI *<LEI>* | [0..1] | IdentifierSet | | 322 |
| | Name *<Nm>* | [0..1] | Text | | 322 |
| | PostalAddress *<PstlAdr>* | [0..1] | ± | | 322 |
| | Other *<Othr>* | [0..1] | ± | | 323 |
| | BranchIdentification *<BrnchId>* | [0..1] | | | 324 |
| | Identification *<Id>* | [0..1] | Text | | 324 |
| | LEI *<LEI>* | [0..1] | IdentifierSet | | 324 |
| | Name *<Nm>* | [0..1] | Text | | 324 |
| | PostalAddress *<PstlAdr>* | [0..1] | ± | | 324 |

---

<!-- Page 176 -->

### 4.4.1.10 CreditorAgent <Cdt rAg>

*Presence: [0..1]*

*Definition: Financial institution servicing an account for the creditor.*

**CreditorAgent <Cdt rAg>** contains the following elements (see "BranchAndFinanciallnstitutionIdentification8" on page 320 for details)

| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | FinanciallnstitutionIdentification <FinInstlId> | [1..1] | | | 321 |
| | BICFI <BICFI> | [0..1] | IdentifierSet | C6 | |
| | ClearingSystemMemberIdentification <ClrSysMmbId> | [0..1] | ± | | 322 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 322 |
| | Name <Nm> | [0..1] | Text | | 322 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 322 |
| | Other <Othr> | [0..1] | ± | | 323 |
| | BranchIdentification <BrnchId> | [0..1] | | | 324 |
| | Identification <Id> | [0..1] | Text | | 324 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 324 |
| | Name <Nm> | [0..1] | Text | | 324 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 324 |

## 4.4.2 OriginalGroupInformation <OrgnlGrpInf>

*Presence: [1..1]*

*Definition: Information concerning the original group of transactions, to which the message refers.*

**OriginalGroupInformation <OrgnlGrpInf>** contains the following **OriginalGroupHeader20** elements

| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | **OriginalMessageIdentification** <OrgnlMsgId> | [1..1] | Text | | 177 |
| | **OriginalMessageNameIdentification** <OrgnlMsgNmId> | [1..1] | Text | | 177 |
| | **OriginalCreationDateTime** <OrgnlCreDtTm> | [0..1] | Date Time | | 177 |
| | **ReversalReasonInformation** <RvslRsnInf> | [0..*] | | | 177 |
| | **Originator** <Orgtr> | [0..1] | ± | | 177 |
| | **Reason** <Rsn> | [0..1] | | | 178 |
| Or | **Code** <Cd> | [1..1] | CodeSet | | 179 |
| Or | **Proprietary** <Prtty> | [1..1] | Text | | 179 |
| | **AdditionalInformation** <AddtlInf> | [0..*] | Text | | 179 |

---

<!-- Page 177 -->

### 4.4.2.1 OriginalMessageIdentification <OrgnlMsgId>

*Presence:* [1..1]

*Definition:* Point to point reference, as assigned by the original instructing party, to unambiguously identify the original message.

*Datatype:* "Max35Text" on page 431

### 4.4.2.2 OriginalMessageNameIdentification <OrgnlMsgNmId>

*Presence:* [1..1]

*Definition:* Specifies the original message name identifier to which the message refers.

*Datatype:* "Max35Text" on page 431

### 4.4.2.3 OriginalCreationDateTime <OrgnlCreDtTm>

*Presence:* [0..1]

*Definition:* Date and time at which the original message was created.

*Datatype:* "ISODateTime" on page 425

### 4.4.2.4 ReversalReasonInformation <RvslRsnInf>

*Presence:* [0..*]

*Definition:* Provides detailed information on the reversal reason.

ReversalReasonInformation <RvslRsnInf> contains the following **PaymentReversalReason10** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **Originator** <Orgtr> | [0..1] | ± | | 177 |
| | **Reason** <Rsn> | [0..1] | | | 178 |
| (Or | **Code** <Cd> | [1..1] | CodeSet | | 179 |
| Or) | **Proprietary** <Prtry> | [1..1] | Text | | 179 |
| | **AdditionalInformation** <AddtlInf> | [0..*] | Text | | 179 |

#### 4.4.2.4.1 Originator <Orgtr>

*Presence:* [0..1]

*Definition:* Party that issues the reversal.

---

<!-- Page 178 -->

Originator <Orgrt> contains the following elements (see "PartyIdentification27" on page 336 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
| :--- | :--- | :--- | :--- | :--- | :--- |
| | Name <Nm> | [0..1] | Text | | 337 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 338 |
| | Identification <Id> | [0..1] | | | 338 |
| (Or | OrganisationIdentification <OrgId> | [1..1] | | | 339 |
| | AnyBIC <AnyBIC> | [0..1] | IdentifierSet | C5 | 340 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 340 |
| | Other <Othr> | [0..*] | | | 340 |
| | Identification <Id> | [1..1] | Text | | 341 |
| | SchemeName <SchmeNm> | [0..1] | | | 341 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 341 |
| Or) | Proprietary <Prtry> | [1..1] | Text | | 341 |
| | Issuer <Issr> | [0..1] | Text | | 341 |
| (Or) | PrivateIdentification <PrvtId> | [1..1] | | | 341 |
| | DateAndPlaceOfBirth <DtAndPlcOfBirth> | [0..1] | | | 342 |
| | BirthDate <BirthDt> | [1..1] | Date | | 342 |
| | ProvinceOfBirth <PrvcOfBirth> | [0..1] | Text | | 342 |
| | CityOfBirth <CityOfBirth> | [1..1] | Text | | 343 |
| | CountryOfBirth <CtryOfBirth> | [1..1] | CodeSet | C7 | 343 |
| | Other <Othr> | [0..*] | | | 343 |
| | Identification <Id> | [1..1] | Text | | 343 |
| | SchemeName <SchmeNm> | [0..1] | | | 343 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 344 |
| Or) | Proprietary <Prtry> | [1..1] | Text | | 344 |
| | Issuer <Issr> | [0..1] | Text | | 344 |
| | CountryOfResidence <CtryOfRes> | [0..1] | CodeSet | C7 | 344 |
| | ContactDetails <CtctDtls> | [0..1] | ± | | 344 |

### 4.4.2.4.2 Reason <Rsn>

*Presence:* [0..1]

*Definition:* Specifies the reason for the reversal.

---

<!-- Page 179 -->

Reason <Rsn> contains one of the following ReversalReason4Choice elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| (Or | **Code** <Cd> | [1..1] | CodeSet | | 179 |
| Or) | **Proprietary** <Prt y> | [1..1] | Text | | 179 |

**4.4.2.4.2.1 Code <Cd>**

*Presence:* [1..1]

*Definition:* Reason for the reversal, as published in an external reason code list.

*Datatype:* "ExternalReversalReason1Code" on page 419

**4.4.2.4.2.2 Proprietary <Prty>**

*Presence:* [1..1]

*Definition:* Reason for the reversal, in a proprietary form.

*Datatype:* "Max35Text" on page 431

**4.4.2.4.3 AdditionalInformation <AddtlInf>**

*Presence:* [0..*]

*Definition:* Further details on the reversal reason.

*Datatype:* "Max105Text" on page 429

## 4.4.3 OriginalPaymentInformationAndReversal <OrgnlPmtInfAndRvsl>

*Presence:* [0..*]

*Definition:* Information concerning the original payment information, to which the reversal message refers.

*Impacted by:* C19 "PaymentInformationReversalAndReasonRule", C20 "PaymentInformationReversalAndTransactionInformationNotPresentRule", C21 "PaymentInformationReversalAndTransactionInformationPresentRule"

---

<!-- Page 180 -->

OriginalPaymentInformationAndReversal <OrgnlPmtInfAndRvsl> contains the following OriginalPaymentInstruction50 elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **ReversalPaymentInformationIdentification** <RvslPmtInfId> | [0..1] | Text | | 184 |
| | **OriginalPaymentInformationIdentification** <OrgnlPmtInfId> | [1..1] | Text | | 184 |
| | **OriginalNumberOfTransactions** <OrgnlNbOfTxs> | [0..1] | Text | | 184 |
| | **OriginalControlSum** <OrgnlCtrlSum> | [0..1] | Quantity | | 184 |
| | **BatchBooking** <BtchBookg> | [0..1] | Indicator | | 184 |
| | **PaymentInformationReversal** <PmtInfRvsl> | [0..1] | Indicator | | 184 |
| | **ReversalReasonInformation** <RvslRsnInf> | [0..*] | | | 185 |
| | **Originator** <Orgtr> | [0..1] | ± | | 185 |
| | **Reason** <Rsn> | [0..1] | | | 186 |
| {Or | **Code** <Cd> | [1..1] | CodeSet | | 187 |
| Or} | **Proprietary** <Prtry> | [1..1] | Text | | 187 |
| | **AdditionalInformation** <AddtlInf> | [0..1] | Text | | 187 |
| | **TransactionInformation** <TxInf> | [0..*] | | | 187 |
| | **ReversalIdentification** <RvslId> | [0..1] | Text | | 191 |
| | **OriginalInstructionIdentification** <OrgnlInstrId> | [0..1] | Text | | 191 |
| | **OriginalEndToEndIdentification** <OrgnlEndToEndId> | [0..1] | Text | | 191 |
| | **OriginalUETR** <OrgnlUETR> | [0..1] | IdentifierSet | | 191 |
| | **OriginalInstructedAmount** <OrgnlInstdAmt> | [0..1] | Amount | C1, C8 | 191 |
| | **ReversedInstructedAmount** <RvsdInstdAmt> | [0..1] | Amount | C1, C8 | 192 |
| | **ChargeBearer** <ChrgBr> | [0..1] | CodeSet | | 192 |
| | **ReversalReasonInformation** <RvslRsnInf> | [0..*] | | | 193 |
| | **Originator** <Orgtr> | [0..1] | ± | | 193 |
| | **Reason** <Rsn> | [0..1] | | | 194 |
| {Or | **Code** <Cd> | [1..1] | CodeSet | | 195 |
| Or} | **Proprietary** <Prtry> | [1..1] | Text | | 195 |
| | **AdditionalInformation** <AddtlInf> | [0..*] | Text | | 195 |
| | **OriginalTransactionReference** <OrgnlTxRef> | [0..1] | | | 195 |
| | **InterbankSettlementAmount** <IntrBkSttlmAmt> | [0..1] | Amount | C1, C8 | 198 |
| | **Amount** <Amt> | [0..1] | ± | | 198 |

---

<!-- Page 181 -->

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **InterbankSettlementDate** *<IntrBkSttlmDt>* | [0..1] | Date | | 199 |
| | **RequestedCollectionDate** *<ReqdCollnDt>* | [0..1] | Date | | 199 |
| | **RequestedExecutionDate** *<ReqdExctnDt>* | [0..1] | ± | | 199 |
| | **CreditorSchemeIdentification** *<CdtrSchemId>* | [0..1] | ± | | 199 |
| | **SettlementInformation** *<SttlmInf>* | [0..1] | | C17, C18, C23, C24, C25, C26, C29, C30 | 200 |
| | **SettlementMethod** *<SttlmMtd>* | [1..1] | CodeSet | | 202 |
| | **SettlementAccount** *<SttlmAcct>* | [0..1] | ± | C16, C15 | 203 |
| | **ClearingSystem** *<ClrSys>* | [0..1] | | | 203 |
| {Or | **Code** *<Cd>* | [1..1] | CodeSet | | 204 |
| Or | **Proprietary** *<PrtY>* | [1..1] | Text | | 204 |
| | **InstructingReimbursementAgent** *<InstdRmbrsmtAgnt>* | [0..1] | ± | | 204 |
| | **InstructingReimbursementAgentAccount** *<InstdRmbrsmtAgntAcct>* | [0..1] | ± | C16, C15 | 205 |
| | **InstructedReimbursementAgent** *<InstdRmbrsmtAgnt>* | [0..1] | ± | | 205 |
| | **InstructedReimbursementAgentAccount** *<InstdRmbrsmtAgntAcct>* | [0..1] | ± | C16, C15 | 206 |
| | **ThirdReimbursementAgent** *<ThirdRmbrsmtAgnt>* | [0..1] | ± | | 207 |
| | **ThirdReimbursementAgentAccount** *<ThirdRmbrsmtAgntAcct>* | [0..1] | ± | C16, C15 | 207 |
| | **PaymentTypeInformation** *<PmtTpInf>* | [0..1] | ± | | 208 |
| | **PaymentMethod** *<PmtMtd>* | [0..1] | CodeSet | | 209 |
| | **MandateRelatedInformation** *<MndtReltdInf>* | [0..1] | | | 209 |
| {Or | **DirectDebitMandate** *<DrctDbtMndt>* | [0..1] | | C2, C3 | 211 |
| | **MandateIdentification** *<MndtId>* | [0..1] | Text | | 213 |
| | **DateOfSignature** *<DtOfSgntr>* | [0..1] | Date | | 213 |
| | **AmendmentIndicator** *<AmdmntInd>* | [0..1] | Indicator | | 213 |
| | **AmendmentInformationDetails** *<AmdmntInfDtls>* | [0..1] | | | 213 |
| | **OriginalMandateIdentification** *<OrgnlMndtId>* | [0..1] | Text | | 214 |

---

<!-- Page 182 -->

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **OriginalCreditorSchemeIdentification** *<OrgnlCdrtSchmId>* | [0..1] | ± | | 214 |
| | **OriginalCreditorAgent** *<OrgnlCdrtAgt>* | [0..1] | ± | | 215 |
| | **OriginalCreditorAgentAccount** *<OrgnlCdrtAgtAcc>* | [0..1] | ± | C16, C15 | 216 |
| | **OriginalDebtor** *<OrgnlDbtr>* | [0..1] | ± | | 217 |
| | **OriginalDebtorAccount** *<OrgnlDbtrAcc>* | [0..1] | ± | C16, C15 | 218 |
| | **OriginalDebtorAgent** *<OrgnlDbtrAgt>* | [0..1] | ± | | 219 |
| | **OriginalDebtorAgentAccount** *<OrgnlDbtrAgtAcc>* | [0..1] | ± | C16, C15 | 220 |
| | **OriginalFinalCollectionDate** *<OrgnlFinlCollnDt>* | [0..1] | Date | | 221 |
| | **OriginalFrequency** *<OrgnlFrqcy>* | [0..1] | ± | | 221 |
| | **OriginalReason** *<OrgnlRsn>* | [0..1] | | | 221 |
| Or | **Code** *<Cd>* | [1..1] | CodeSet | | 221 |
| Or | **Proprietary** *<Prtry>* | [1..1] | Text | | 221 |
| | **OriginalTrackingDays** *<OrgnlTrckgDays>* | [0..1] | Text | | 222 |
| | **ElectronicSignature** *<ElctrncSgntr>* | [0..1] | Text | | 222 |
| | **FirstCollectionDate** *<FrstCollnDt>* | [0..1] | Date | | 222 |
| | **FinalCollectionDate** *<FinlCollnDt>* | [0..1] | Date | | 222 |
| | **Frequency** *<Frqcy>* | [0..1] | ± | | 222 |
| | **Reason** *<Rsn>* | [0..1] | | | 222 |
| Or | **Code** *<Cd>* | [1..1] | CodeSet | | 223 |
| Or | **Proprietary** *<Prtry>* | [1..1] | Text | | 223 |
| | **TrackingDays** *<TrckgDays>* | [0..1] | Text | | 223 |
| Or | **CreditTransferMandate** *<CdtTrfMndt>* | [0..1] | ± | | 223 |
| | **RemittanceInformation** *<RmInf>* | [0..1] | ± | | 224 |
| | **UltimateDebtor** *<UltmtDbtr>* | [0..1] | | | 224 |
| Or | **Party** *<Pty>* | [1..1] | ± | | 224 |
| Or | **Agent** *<Agt>* | [1..1] | ± | | 225 |
| | **Debtor** *<Dbtr>* | [0..1] | | | 226 |
| Or | **Party** *<Pty>* | [1..1] | ± | | 226 |
| Or | **Agent** *<Agt>* | [1..1] | ± | | 227 |

---

<!-- Page 183 -->

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **DebtorAccount** `<DbtrAcct>` | [0..1] | ± | C16, C15 | 228 |
| | **DebtorAgent** `<DbtrAgt>` | [0..1] | ± | | 229 |
| | **DebtorAgentAccount** `<DbtrAgtAcct>` | [0..1] | ± | C16, C15 | 229 |
| | **CreditorAgent** `<CdtrAgt>` | [0..1] | ± | | 230 |
| | **CreditorAgentAccount** `<CdtrAgtAcct>` | [0..1] | ± | C16, C15 | 231 |
| | **Creditor** `<Cdtr>` | [0..1] | | | 232 |
| (Or | **Party** `<Pty>` | [1..1] | ± | | 232 |
| Or) | **Agent** `<Agt>` | [1..1] | ± | | 233 |
| | **CreditorAccount** `<CdtrAcct>` | [0..1] | ± | C16, C15 | 234 |
| | **UltimateCreditor** `<UltmtCdtr>` | [0..1] | | | 235 |
| (Or | **Party** `<Pty>` | [1..1] | ± | | 235 |
| Or) | **Agent** `<Agt>` | [1..1] | ± | | 236 |
| | **Purpose** `<Purp>` | [0..1] | ± | | 237 |
| | **SupplementaryData** `<SplmtryData>` | [0..*] | ± | C28 | 237 |

## Constraints

- **PaymentInformationReversalAndReasonRule**

  If PaymentInformationReversal is true, then ReversalReasonInformation/ReversalReason must be present.

  ```
  On Condition
  /PaymentInformationReversal is present
  And /PaymentInformationReversal is equal to value 'true'
  Following Must be True
  /ReversalReasonInformation[*]/Reason Must be present
  ```

- **PaymentInformationReversalAndTransactionInformationNotPresentRule**

  If PaymentInformationReversal is true, then TransactionInformation is not allowed.

  ```
  On Condition
  /PaymentInformationReversal is present
  And /PaymentInformationReversal is equal to value 'true'
  Following Must be True
  /TransactionInformation[*] Must be absent
  ```

- **PaymentInformationReversalAndTransactionInformationPresentRule**

  If PaymentInformationReversal is false, then at least one occurrence of TransactionInformation must be present.

  ```
  On Condition
  /PaymentInformationReversal is present
  And /PaymentInformationReversal is equal to value 'false'
  ```

---

<!-- Page 184 -->

Following Must be True
/TransactionInformation[*] Must be present

## 4.4.3.1 ReversalPaymentInformationIdentification <RvslPmtInflId>

*Presence:* [0..1]

*Definition:* Unique identification, as assigned by an instructing party for an instructed party, to unambiguously identify the reversed payment information group.

Usage: The instructing party is the party sending the reversal message and not the party that sent the original instruction that is being reversed.

*Datatype:* "Max35Text" on page 431

## 4.4.3.2 OriginalPaymentInformationIdentification <OrgnlPmtInflId>

*Presence:* [1..1]

*Definition:* Unique identification, as assigned by the original sending party, to unambiguously identify the original payment information group.

*Datatype:* "Max35Text" on page 431

## 4.4.3.3 OriginalNumberOfTransactions <OrgnlNbOfTxs>

*Presence:* [0..1]

*Definition:* Number of individual transactions contained in the original payment information group.

*Datatype:* "Max15NumericText" on page 430

## 4.4.3.4 OriginalControlSum <OrgnlCtrlSum>

*Presence:* [0..1]

*Definition:* Total of all individual amounts included in the original payment information group, irrespective of currencies.

*Datatype:* "DecimalNumber" on page 427

## 4.4.3.5 BatchBooking <BtchBookg>

*Presence:* [0..1]

*Definition:* Identifies whether a single entry per individual transaction or a batch entry for the sum of the amounts of all transactions within the group of a message is requested.

Usage: Batch booking is used to request and not order a possible batch booking.

*Datatype:* One of the following values must be used (see "BatchBookingIndicator" on page 427):

- *Meaning When True:* Identifies that a batch entry for the sum of the amounts of all transactions in the batch or message is requested.

- *Meaning When False:* Identifies that a single entry for each of the transactions in the batch or message is requested.

## 4.4.3.6 PaymentInformationReversal <PmtInfRvsl>

*Presence:* [0..1]

---

<!-- Page 185 -->

Definition: Indicates whether or not the reversal applies to the complete original payment information group or to individual transactions within that group.

Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 427):

- Meaning When True: True
- Meaning When False: False

### 4.4.3.7 ReversalReasonInformation <RvslRsnInf>

Presence: [0..*]

Definition: Provides detailed information on the reversal reason.

**ReversalReasonInformation <RvslRsnInf>** contains the following **PaymentReversalReason10** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **Originator** <Orgtr> | [0..1] | ± | | 185 |
| | **Reason** <Rsn> | [0..1] | | | 186 |
| (Or | **Code** <Cd> | [1..1] | CodeSet | | 187 |
| Or) | **Proprietary** <Prt> | [1..1] | Text | | 187 |
| | **AdditionalInformation** <AddtlInf> | [0..*] | Text | | 187 |

#### 4.4.3.7.1 Originator <Orgtr>

Presence: [0..1]

Definition: Party that issues the reversal.

---

<!-- Page 186 -->

Originator <Orgrt> contains the following elements (see "PartyIdentification272" on page 336 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
| :--- | :--- | :--- | :--- | :--- | :--- |
| | Name <Nm> | [0..1] | Text | | 337 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 338 |
| | Identification <Id> | [0..1] | | | 338 |
| (Or) | OrganisationIdentification <OrgId> | [1..1] | | | 339 |
| | AnyBIC <AnyBIC> | [0..1] | IdentifierSet | C5 | 340 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 340 |
| | Other <Othr> | [0..*] | | | 340 |
| | Identification <Id> | [1..1] | Text | | 341 |
| | SchemeName <SchmeNm> | [0..1] | | | 341 |
| (Or) | Code <Cd> | [1..1] | CodeSet | | 341 |
| Or | Proprietary <Prtry> | [1..1] | Text | | 341 |
| | Issuer <Issr> | [0..1] | Text | | 341 |
| (Or) | PrivateIdentification <PrvtId> | [1..1] | | | 341 |
| | DateAndPlaceOfBirth <DtAndPlcOfBirth> | [0..1] | | | 342 |
| | BirthDate <BirthDt> | [1..1] | Date | | 342 |
| | ProvinceOfBirth <PrvcOfBirth> | [0..1] | Text | | 342 |
| | CityOfBirth <CityOfBirth> | [1..1] | Text | | 343 |
| | CountryOfBirth <CtryOfBirth> | [1..1] | CodeSet | C7 | 343 |
| | Other <Othr> | [0..*] | | | 343 |
| | Identification <Id> | [1..1] | Text | | 343 |
| | SchemeName <SchmeNm> | [0..1] | | | 343 |
| (Or) | Code <Cd> | [1..1] | CodeSet | | 344 |
| Or | Proprietary <Prtry> | [1..1] | Text | | 344 |
| | Issuer <Issr> | [0..1] | Text | | 344 |
| | CountryOfResidence <CtryOfRes> | [0..1] | CodeSet | C7 | 344 |
| | ContactDetails <CtctDtls> | [0..1] | ± | | 344 |

### 4.4.3.7.2 Reason <Rsn>

*Presence:* [0..1]

*Definition:* Specifies the reason for the reversal.

---

<!-- Page 187 -->

Reason <Rsn> contains one of the following ReversalReason4Choice elements



<table>
  <tr>
    <th>Or</th>
    <th>MessageElement&lt;XML Tag&gt;</th>
    <th>Mult.</th>
    <th>Type</th>
    <th>Constr. No.</th>
    <th>Page</th>
  </tr>
  <tr>
    <td>(Or</td>
    <td>Code &lt;Cd&gt;</td>
    <td>[1..1]</td>
    <td>CodeSet</td>
    <td></td>
    <td>187</td>
  </tr>
  <tr>
    <td>Or)</td>
    <td>Proprietary &lt;Prtry&gt;</td>
    <td>[1..1]</td>
    <td>Text</td>
    <td></td>
    <td>187</td>
  </tr>
</table>

**4.4.3.7.2.1 Code <Cd>**

*Presence:* [1..1]

*Definition:* Reason for the reversal, as published in an external reason code list.

*Datatype:* "ExternalReversalReason1Code" on page 419

**4.4.3.7.2.2 Proprietary <Prtry>**

*Presence:* [1..1]

*Definition:* Reason for the reversal, in a proprietary form.

*Datatype:* "Max35Text" on page 431

**4.4.3.7.3 AdditionalInformation <AddtlInf>**

*Presence:* [0..*]

*Definition:* Further details on the reversal reason.

*Datatype:* "Max105Text" on page 429

**4.4.3.8 TransactionInformation <TxInf>**

*Presence:* [0..*]

*Definition:* Provides information on the original transactions to which the reversal message refers.

---

<!-- Page 188 -->

TransactionInformation <TxInf> contains the following PaymentTransaction156 elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **ReversalIdentification** *<RvslId>* | [0..1] | Text | | 191 |
| | **OriginalInstructionIdentification** *<OrgnlInstrId>* | [0..1] | Text | | 191 |
| | **OriginalEndToEndIdentification** *<OrgnlEndToEndId>* | [0..1] | Text | | 191 |
| | **OriginalUETR** *<OrgnlUETR>* | [0..1] | IdentifierSet | | 191 |
| | **OriginalInstructedAmount** *<OrgnlInstdAmt>* | [0..1] | Amount | C1, C8 | 191 |
| | **ReversedInstructedAmount** *<RvslInstdAmt>* | [0..1] | Amount | C1, C8 | 192 |
| | **ChargeBearer** *<ChgBr>* | [0..1] | CodeSet | | 192 |
| | **ReversalReasonInformation** *<RvslRsnInf>* | [0..*] | | | 193 |
| | **Originator** *<Orgtr>* | [0..1] | ± | | 193 |
| | **Reason** *<Rsn>* | [0..1] | | | 194 |
| (Or | **Code** *<Cd>* | [1..1] | CodeSet | | 195 |
| Or) | **Proprietary** *<Prtry>* | [1..1] | Text | | 195 |
| | **AdditionalInformation** *<AddtlInf>* | [0..*] | Text | | 195 |
| | **OriginalTransactionReference** *<OrgnlTxRef>* | [0..1] | | | 195 |
| | **InterbankSettlementAmount** *<IntrBkSttlmAmt>* | [0..1] | Amount | C1, C8 | 198 |
| | **Amount** *<Amt>* | [0..1] | ± | | 198 |
| | **InterbankSettlementDate** *<IntrBkSttlmDt>* | [0..1] | Date | | 199 |
| | **RequestedCollectionDate** *<ReqdColltnDt>* | [0..1] | Date | | 199 |
| | **RequestedExecutionDate** *<ReqdExctnDt>* | [0..1] | ± | | 199 |
| | **CreditorScheduleIdentification** *<CdtrSchedId>* | [0..1] | ± | | 199 |
| | **SettlementInformation** *<SttlmInf>* | [0..1] | | C17, C18, C23, C24, C25, C26, C29, C30 | 200 |
| | **SettlementMethod** *<SttlmMtd>* | [1..1] | CodeSet | | 202 |
| | **SettlementAccount** *<SttlmAcct>* | [0..1] | ± | C16, C15 | 203 |
| | **ClearingSystem** *<ClrSys>* | [0..1] | | | 203 |
| (Or | **Code** *<Cd>* | [1..1] | CodeSet | | 204 |
| Or) | **Proprietary** *<Prtry>* | [1..1] | Text | | 204 |

---

<!-- Page 189 -->

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **InstructingReimbursementAgent** <InstrRmbrsmtAgtr> | [0..1] | ± | | 204 |
| | **InstructingReimbursementAgentAccount** <InstrRmbrsmtAgtrAcct> | [0..1] | ± | C16, C15 | 205 |
| | **InstructedReimbursementAgent** <InstdRmbrsmtAgtr> | [0..1] | ± | | 205 |
| | **InstructedReimbursementAgentAccount** <InstdRmbrsmtAgtrAcct> | [0..1] | ± | C16, C15 | 206 |
| | **ThirdReimbursementAgent** <ThirdRmbrsmtAgtr> | [0..1] | ± | | 207 |
| | **ThirdReimbursementAgentAccount** <ThirdRmbrsmtAgtrAcct> | [0..1] | ± | C16, C15 | 207 |
| | **PaymentTypeInformation** <PmtTpInf> | [0..1] | ± | | 208 |
| | **PaymentMethod** <PmtMtd> | [0..1] | CodeSet | | 209 |
| | **MandateRelatedInformation** <MndtRltdInf> | [0..1] | | | 209 |
| (Or | **DirectDebitMandate** <DrctDbtMndt> | [0..1] | | C2, C3 | 211 |
| | **MandateIdentification** <MndtId> | [0..1] | Text | | 213 |
| | **DateOfSignature** <DtOfSgntr> | [0..1] | Date | | 213 |
| | **AmendmentIndicator** <AmdmntInd> | [0..1] | Indicator | | 213 |
| | **AmendmentInformationDetails** <AmdmntInfDtls> | [0..1] | | | 213 |
| | **OriginalMandateIdentification** <OrgnlMndtId> | [0..1] | Text | | 214 |
| | **OriginalCreditorSchemeIdentification** <OrgnlCdrSchmeId> | [0..1] | ± | | 214 |
| | **OriginalCreditorAgent** <OrgnlCdrAgtr> | [0..1] | ± | | 215 |
| | **OriginalCreditorAgentAccount** <OrgnlCdrAgtrAcct> | [0..1] | ± | C16, C15 | 216 |
| | **OriginalDebtor** <OrgnlDbtr> | [0..1] | ± | | 217 |
| | **OriginalDebtorAccount** <OrgnlDbtrAcct> | [0..1] | ± | C16, C15 | 218 |
| | **OriginalDebtorAgent** <OrgnlDbtrAgtr> | [0..1] | ± | | 219 |
| | **OriginalDebtorAgentAccount** <OrgnlDbtrAgtrAcct> | [0..1] | ± | C16, C15 | 220 |
| | **OriginalFinalCollectionDate** <OrgnlFnClctnDt> | [0..1] | Date | | 221 |
| | **OriginalFrequency** <OrgnlFrqcy> | [0..1] | ± | | 221 |
| | **OriginalReason** <OrgnlRsn> | [0..1] | | | 221 |
| (Or | **Code** <Cd> | [1..1] | CodeSet | | 221 |
| Or) | **Proprietary** <Prtry> | [1..1] | Text | | 221 |
| | **OriginalTrackingDays** <OrgnlTrckgDays> | [0..1] | Text | | 222 |

---

<!-- Page 190 -->

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **ElectronicSignature** <ElectronicSgntr> | [0..1] | Text | | 222 |
| | **FirstCollectionDate** <FirstCollnDt> | [0..1] | Date | | 222 |
| | **FinalCollectionDate** <FinlCollnDt> | [0..1] | Date | | 222 |
| | **Frequency** <Frcqy> | [0..1] | ± | | 222 |
| | **Reason** <Rsn> | [0..1] | | | 222 |
| (Or | **Code** <Cd> | [1..1] | CodeSet | | 223 |
| Or) | **Proprietary** <Prtcy> | [1..1] | Text | | 223 |
| | **TrackingDays** <TrckgDays> | [0..1] | Text | | 223 |
| Or | **CreditTransferMandate** <CdtTrfMndt> | [0..1] | ± | | 223 |
| | **RemittanceInformation** <RmInf> | [0..1] | ± | | 224 |
| | **UltimateDebtor** <UltmtDbtr> | [0..1] | | | 224 |
| (Or | **Party** <Pty> | [1..1] | ± | | 224 |
| Or) | **Agent** <Agt> | [1..1] | ± | | 225 |
| | **Debtor** <Dbtr> | [0..1] | | | 226 |
| (Or | **Party** <Pty> | [1..1] | ± | | 226 |
| Or) | **Agent** <Agt> | [1..1] | ± | | 227 |
| | **DebtorAccount** <DbtrAcct> | [0..1] | ± | C16, C15 | 228 |
| | **DebtorAgent** <DbtrAgt> | [0..1] | ± | | 229 |
| | **DebtorAgentAccount** <DbtrAgtAcct> | [0..1] | ± | C16, C15 | 229 |
| | **CreditorAgent** <CdtrAgt> | [0..1] | ± | | 230 |
| | **CreditorAgentAccount** <CdtrAgtAcct> | [0..1] | ± | C16, C15 | 231 |
| | **Creditor** <Cdtr> | [0..1] | | | 232 |
| (Or | **Party** <Pty> | [1..1] | ± | | 232 |
| Or) | **Agent** <Agt> | [1..1] | ± | | 233 |
| | **CreditorAccount** <CdtrAcct> | [0..1] | ± | C16, C15 | 234 |
| | **UltimateCreditor** <UltmtCdtr> | [0..1] | | | 235 |
| (Or | **Party** <Pty> | [1..1] | ± | | 235 |
| Or) | **Agent** <Agt> | [1..1] | ± | | 236 |
| | **Purpose** <Purp> | [0..1] | ± | | 237 |
| | **SupplementaryData** <SplmtryData> | [0..*] | ± | C28 | 237 |

---

<!-- Page 191 -->

## 4.4.3.8.1 ReversalIdentification <RvslId>

*Presence:* [0..1]

*Definition:* Unique identification, as assigned by an instructing party for an instructed party, to unambiguously identify the reversed transaction.

Usage: The instructing party is the party sending the reversal message and not the party that sent the original instruction that is being reversed.

*Datatype:* "Max35Text" on page 431

## 4.4.3.8.2 OriginalInstructionIdentification <OrgnlInstd>

*Presence:* [0..1]

*Definition:* Unique identification, as assigned by the original instructing party for the original instructed party, to unambiguously identify the original instruction.

*Datatype:* "Max35Text" on page 431

## 4.4.3.8.3 OriginalEndToEndIdentification <OrgnlEndToEndId>

*Presence:* [0..1]

*Definition:* Unique identification, as assigned by the original initiating party, to unambiguously identify the original transaction.

*Datatype:* "Max35Text" on page 431

## 4.4.3.8.4 OriginalUETR <OrgnlUETR>

*Presence:* [0..1]

*Definition:* Universally unique identifier to provide the original end-to-end reference of a payment transaction.

*Datatype:* "UUIDv4Identifier" on page 427

## 4.4.3.8.5 OriginalInstructedAmount <OrgnlInstdAmt>

*Presence:* [0..1]

*Definition:* Amount of money, as provided in the original transaction, to be moved between the debtor and the creditor, before deduction of charges, expressed in the currency, as ordered by the original initiating party.

Usage: This amount has to be transported unchanged through the transaction chain.

*Impacted by:* C1 "ActiveOrHistoricCurrency", C8 "CurrencyAmount"

*Datatype:* "ActiveOrHistoricCurrencyAndAmount" on page 407

**Constraints**

- **ActiveOrHistoricCurrency**

The Currency Code must be registered, or have already been registered. Valid active or historic currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)

---

<!-- Page 192 -->

contiguous letters, and may be or not be withdrawn on the day the message containing the Currency is exchanged.
* **CurrencyAmount**
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.

## 4.4.3.8.6 ReversedInstructedAmount <RvslInstdAmt>
*Presence:* [0..1]
*Definition:* Amount of money to be moved between the debtor and the creditor, before deduction of charges, in the reversed transaction.

Usage: This amount has to be transported unchanged through the transaction chain.
*Impacted by:* C1 "ActiveOrHistoricCurrency", C8 "CurrencyAmount"
*Datatype:* "ActiveOrHistoricCurrencyAndAmount" on page 407

**Constraints**
* **ActiveOrHistoricCurrency**
The Currency Code must be registered, or have already been registered. Valid active or historic currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and may be or not be withdrawn on the day the message containing the Currency is exchanged.
* **CurrencyAmount**
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.

## 4.4.3.8.7 ChargeBearer <ChrgBr>
*Presence:* [0..1]
*Definition:* Specifies if the creditor and/or debtor will bear the charges associated with the processing of the payment transaction.

Usage: The ChargeBearer applies to the reversal message, not to the original instruction.
*Datatype:* "ChargeBearerType1Code" on page 410



| CodeName | Name | Definition |
| :--- | :--- | :--- |
| DEBT | BorneByDebtor | All transaction charges are to be borne by the debtor. |
| CRED | BorneByCreditor | All transaction charges are to be borne by the creditor. |
| SHAR | Shared | In a credit transfer context, means that transaction charges on the sender side are to be borne by the debtor, transaction charges on the receiver side are to be borne by the creditor. In a direct debit context, means that transaction charges on the sender side are to be borne by the creditor, |

---

<!-- Page 193 -->

| CodeName | Name | Definition |
|---|---|---|
| | | transaction charges on the receiver side are to be borne by the debtor. |
| SLEV | FollowingServiceLevel | Charges are to be applied following the rules agreed in the service level and/or scheme. |

### 4.4.3.8.8 ReversalReasonInformation <RvslRsnInf>

*Presence:* [0..*]

*Definition:* Provides detailed information on the reversal reason.

**ReversalReasonInformation <RvslRsnInf>** contains the following **PaymentReversalReason10** elements

| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **Originator** <Orgtr> | [0..1] | ± | | 193 |
| | **Reason** <Rsn> | [0..1] | | | 194 |
| (Or | **Code** <Cd> | [1..1] | CodeSet | | 195 |
| Or) | **Proprietary** <Prtry> | [1..1] | Text | | 195 |
| | **AdditionalInformation** <AddtlInf> | [0..*] | Text | | 195 |

#### 4.4.3.8.8.1 Originator <Orgtr>

*Presence:* [0..1]

*Definition:* Party that issues the reversal.

---

<!-- Page 194 -->

Originator <Orgrt> contains the following elements (see "PartyIdentification272" on page 336 for details)



| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | Name <Nm> | [0..1] | Text | | 337 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 338 |
| | Identification <Id> | [0..1] | | | 338 |
| (Or | OrganisationIdentification <OrgId> | [1..1] | | | 339 |
| | AnyBIC <AnyBIC> | [0..1] | IdentifierSet | C5 | 340 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 340 |
| | Other <Othr> | [0..*] | | | 340 |
| | Identification <Id> | [1..1] | Text | | 341 |
| | SchemeName <SchmeNm> | [0..1] | | | 341 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 341 |
| Or) | Proprietary <Prtry> | [1..1] | Text | | 341 |
| | Issuer <Issr> | [0..1] | Text | | 341 |
| (Or) | PrivateIdentification <PrvtId> | [1..1] | | | 341 |
| | DateAndPlaceOfBirth <DtAndPlcOfBirth> | [0..1] | | | 342 |
| | BirthDate <BirthDt> | [1..1] | Date | | 342 |
| | ProvinceOfBirth <PrvcOfBirth> | [0..1] | Text | | 342 |
| | CityOfBirth <CityOfBirth> | [1..1] | Text | | 343 |
| | CountryOfBirth <CtryOfBirth> | [1..1] | CodeSet | C7 | 343 |
| | Other <Othr> | [0..*] | | | 343 |
| | Identification <Id> | [1..1] | Text | | 343 |
| | SchemeName <SchmeNm> | [0..1] | | | 343 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 344 |
| Or) | Proprietary <Prtry> | [1..1] | Text | | 344 |
| | Issuer <Issr> | [0..1] | Text | | 344 |
| | CountryOfResidence <CtryOfRes> | [0..1] | CodeSet | C7 | 344 |
| | ContactDetails <CtctDtls> | [0..1] | ± | | 344 |

**4.4.3.8.8.2 Reason <Rsn>**

*Presence:* [0..1]

*Definition:* Specifies the reason for the reversal.

---

<!-- Page 195 -->

Reason <Rsn> contains one of the following ReversalReason4Choice elements



<table>
  <tr>
    <th>Or</th>
    <th>MessageElement&lt;XML Tag&gt;</th>
    <th>Mult.</th>
    <th>Type</th>
    <th>Constr. No.</th>
    <th>Page</th>
  </tr>
  <tr>
    <td>(Or)</td>
    <td><b>Code</b> &lt;Cd&gt;</td>
    <td>[1..1]</td>
    <td>CodeSet</td>
    <td></td>
    <td>195</td>
  </tr>
  <tr>
    <td>Or)</td>
    <td><b>Proprietary</b> &lt;Ptry&gt;</td>
    <td>[1..1]</td>
    <td>Text</td>
    <td></td>
    <td>195</td>
  </tr>
</table>

**4.4.3.8.8.2.1 Code <Cd>**

*Presence:* [1..1]

*Definition:* Reason for the reversal, as published in an external reason code list.

*Datatype:* "ExternalReversalReason1Code" on page 419

**4.4.3.8.8.2.2 Proprietary <Ptry>**

*Presence:* [1..1]

*Definition:* Reason for the reversal, in a proprietary form.

*Datatype:* "Max35Text" on page 431

**4.4.3.8.8.3 AdditionalInformation <AddtlInf>**

*Presence:* [0..*]

*Definition:* Further details on the reversal reason.

*Datatype:* "Max105Text" on page 429

**4.4.3.8.9 OriginalTransactionReference <OrgnlTxRef>**

*Presence:* [0..1]

*Definition:* Key elements used to identify the original transaction that is being referred to.

---

<!-- Page 196 -->

OriginalTransactionReference <OrgnlTxRef> contains the following
OriginalTransactionReference42 elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | InterbankSettlementAmount <IntkBkSttlmAmt> | [0..1] | Amount | C1, C8 | 198 |
| | Amount <Amt> | [0..1] | ± | | 198 |
| | InterbankSettlementDate <IntkBkSttlmDt> | [0..1] | Date | | 199 |
| | RequestedCollectionDate <ReqdColltnDt> | [0..1] | Date | | 199 |
| | RequestedExecutionDate <ReqdExctnDt> | [0..1] | ± | | 199 |
| | CreditorScheduleIdentification <CdtrSchmeId> | [0..1] | ± | | 199 |
| | SettlementInformation <SttlmInf> | [0..1] | | C17, C18, C23, C24, C25, C26, C29, C30 | 200 |
| | SettlementMethod <SttlmMtd> | [1..1] | CodeSet | | 202 |
| | SettlementAccount <SttlmAcc> | [0..1] | ± | C16, C15 | 203 |
| | ClearingSystem <ClrSys> | [0..1] | | | 203 |
| {Or | Code <Cd> | [1..1] | CodeSet | | 204 |
| Or} | Proprietary <Prtry> | [1..1] | Text | | 204 |
| | InstructingReimbursementAgent <InsgRmbrsmntAg> | [0..1] | ± | | 204 |
| | InstructingReimbursementAgentAccount <InsgRmbrsmntAgAcct> | [0..1] | ± | C16, C15 | 205 |
| | InstructedReimbursementAgent <InstdRmbrsmntAg> | [0..1] | ± | | 205 |
| | InstructedReimbursementAgentAccount <InstdRmbrsmntAgAcct> | [0..1] | ± | C16, C15 | 206 |
| | ThirdReimbursementAgent <ThrdRmbrsmntAg> | [0..1] | ± | | 207 |
| | ThirdReimbursementAgentAccount <ThrdRmbrsmntAgAcct> | [0..1] | ± | C16, C15 | 207 |
| | PaymentTypeInformation <PmtTpInf> | [0..1] | ± | | 208 |
| | PaymentMethod <PmtMtd> | [0..1] | CodeSet | | 209 |
| | MandateRelatedInformation <MndtRltdInf> | [0..1] | | | 209 |
| {Or | DirectDebitMandate <DrctDbtMndt> | [0..1] | | C2, C3 | 211 |
| | MandateIdentification <MndtId> | [0..1] | Text | | 213 |
| | DateOfSignature <DtOfSgntr> | [0..1] | Date | | 213 |
| | AmendmentIndicator <AmdmntInd> | [0..1] | Indicator | | 213 |

---

<!-- Page 197 -->

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **AmendmentInformationDetails** <AmndmntInfDtls> | [0..1] |  |  | 213 |
| | **OriginalMandateIdentification** <OrgnlMndtd> | [0..1] | Text |  | 214 |
| | **OriginalCreditorSchemeIdentification** <OrgnlCddtrSchemId> | [0..1] | ± |  | 214 |
| | **OriginalCreditorAgent** <OrgnlCddtrAgnt> | [0..1] | ± |  | 215 |
| | **OriginalCreditorAgentAccount** <OrgnlCddtrAgntAcct> | [0..1] | ± | C16, C15 | 216 |
| | **OriginalDebtor** <OrgnlDbtr> | [0..1] | ± |  | 217 |
| | **OriginalDebtorAccount** <OrgnlDbtrAcct> | [0..1] | ± | C16, C15 | 218 |
| | **OriginalDebtorAgent** <OrgnlDbtrAgnt> | [0..1] | ± |  | 219 |
| | **OriginalDebtorAgentAccount** <OrgnlDbtrAgntAcct> | [0..1] | ± | C16, C15 | 220 |
| | **OriginalFinalCollectionDate** <OrgnlFinlColltnDt> | [0..1] | Date |  | 221 |
| | **OriginalFrequency** <OrgnlFrcq> | [0..1] | ± |  | 221 |
| | **OriginalReason** <OrgnlRsn> | [0..1] |  |  | 221 |
| (Or | **Code** <Cd> | [1..1] | CodeSet |  | 221 |
| Or) | **Proprietary** <Prtry> | [1..1] | Text |  | 221 |
| | **OriginalTrackingDays** <OrgnlTrckgDays> | [0..1] | Text |  | 222 |
| | **ElectronicSignature** <ElctrcSgntr> | [0..1] | Text |  | 222 |
| | **FirstCollectionDate** <FrstColltnDt> | [0..1] | Date |  | 222 |
| | **FinalCollectionDate** <FinlColltnDt> | [0..1] | Date |  | 222 |
| | **Frequency** <Frcq> | [0..1] | ± |  | 222 |
| | **Reason** <Rsn> | [0..1] |  |  | 222 |
| (Or | **Code** <Cd> | [1..1] | CodeSet |  | 223 |
| Or) | **Proprietary** <Prtry> | [1..1] | Text |  | 223 |
| | **TrackingDays** <TrckgDays> | [0..1] | Text |  | 223 |
| Or | **CreditTransferMandate** <CdtTrfMndt> | [0..1] | ± |  | 223 |
| | **RemittanceInformation** <RmtdInf> | [0..1] | ± |  | 224 |
| | **UltimateDebtor** <UltmtDbtr> | [0..1] |  |  | 224 |
| (Or | **Party** <Pty> | [1..1] | ± |  | 224 |
| Or) | **Agent** <Agnt> | [1..1] | ± |  | 225 |
| | **Debtor** <Dbtr> | [0..1] |  |  | 226 |
| (Or | **Party** <Pty> | [1..1] | ± |  | 226 |

---

<!-- Page 198 -->

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| Or | **Agent** `<Agtr>` | [1..1] | ± | | 227 |
| | **DebtorAccount** `<DbtrAcct>` | [0..1] | ± | C16, C15 | 228 |
| | **DebtorAgent** `<DbtrAgtr>` | [0..1] | ± | | 229 |
| | **DebtorAgentAccount** `<DbtrAgtrAcct>` | [0..1] | ± | C16, C15 | 229 |
| | **CreditorAgent** `<CdtrAgtr>` | [0..1] | ± | | 230 |
| | **CreditorAgentAccount** `<CdtrAgtrAcct>` | [0..1] | ± | C16, C15 | 231 |
| | **Creditor** `<Cdtr>` | [0..1] | | | 232 |
| Or | **Party** `<Pty>` | [1..1] | ± | | 232 |
| Or | **Agent** `<Agtr>` | [1..1] | ± | | 233 |
| | **CreditorAccount** `<CdtrAcct>` | [0..1] | ± | C16, C15 | 234 |
| | **UltimateCreditor** `<UltmtCdtr>` | [0..1] | | | 235 |
| Or | **Party** `<Pty>` | [1..1] | ± | | 235 |
| Or | **Agent** `<Agtr>` | [1..1] | ± | | 236 |
| | **Purpose** `<Purp>` | [0..1] | ± | | 237 |

**4.4.3.8.9.1 IntranBankSettlementAmount `<IntrBkSttlmAmt>`**

*Presence:* [0..1]

*Definition:* Amount of money moved between the instructing agent and the instructed agent.

*Impacted by:* C1 "ActiveOrHistoricCurrency", C8 "CurrencyAmount"

*Datatype:* "ActiveOrHistoricCurrencyAndAmount" on page 407

**Constraints**

*   **ActiveOrHistoricCurrency**

    The Currency Code must be registered, or have already been registered. Valid active or historic currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and may be or not be withdrawn on the day the message containing the Currency is exchanged.

*   **CurrencyAmount**

    The number of fractional digits (or minor unit of currency) must comply with ISO 4217.

    Note: The decimal separator is a dot.

**4.4.3.8.9.2 Amount `<Amt>`**

*Presence:* [0..1]

---

<!-- Page 199 -->

Definition: Amount of money to be moved between the debtor and creditor, before deduction of charges, expressed in the currency as ordered by the initiating party.

**Amount** `<Amt>` contains one of the following elements (see "AmountType4Choice" on page 314 for details)


| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| (Or | InstructedAmount `<InstdAmt>` | [1..1] | Amount | C2, C8 | 314 |
| Or) | EquivalentAmount `<EqvAmt>` | [1..1] | | | 315 |
| | Amount `<Amt>` | [1..1] | Amount | C2, C8 | 315 |
| | CurrencyOfTransfer `<CcyOfTrf>` | [1..1] | CodeSet | C2 | 315 |

### 4.4.3.8.9.3 InterbankSettlementDate `<IntrBkSttlmDt>`

*Presence:* [0..1]

*Definition:* Date on which the amount of money ceases to be available to the agent that owes it and when the amount of money becomes available to the agent to which it is due.

*Datatype:* "ISODate" on page 425

### 4.4.3.8.9.4 RequestedCollectionDate `<ReqdCollnDt>`

*Presence:* [0..1]

*Definition:* Date and time at which the creditor requests that the amount of money is to be collected from the debtor.

*Datatype:* "ISODate" on page 425

### 4.4.3.8.9.5 RequestedExecutionDate `<ReqdExctnDt>`

*Presence:* [0..1]

*Definition:* Date at which the initiating party requests the clearing agent to process the payment.

Usage: This is the date on which the debtor's account is to be debited. If payment by cheque, the date when the cheque must be generated by the bank.

**RequestedExecutionDate** `<ReqdExctnDt>` contains one of the following elements (see "DateAndDateTime2Choice" on page 316 for details)


| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| (Or | Date `<Dt>` | [1..1] | Date | | 317 |
| Or) | DateTime `<DtTm>` | [1..1] | DateTime | | 317 |

### 4.4.3.8.9.6 CreditorSchemeIdentification `<CdtrSchmId>`

*Presence:* [0..1]

*Definition:* Credit party that signs the mandate.

---

<!-- Page 200 -->

**CreditorSchemeIdentification** `<CddrSchmdId>` contains the following elements (see *PartyIdentification27* on page 336 for details)



<table>
  <thead>
    <tr>
      <th>Or</th>
      <th>MessageElement &lt;XML Tag&gt;</th>
      <th>Mult.</th>
      <th>Type</th>
      <th>Constr. No.</th>
      <th>Page</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td>Name &lt;Nm&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>337</td>
    </tr>
    <tr>
      <td></td>
      <td>PostalAddress &lt;PstlAdr&gt;</td>
      <td>[0..1]</td>
      <td>±</td>
      <td></td>
      <td>338</td>
    </tr>
    <tr>
      <td></td>
      <td>Identification &lt;Id&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>338</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>OrganisationIdentification &lt;OrgId&gt;</td>
      <td>[1..1]</td>
      <td></td>
      <td></td>
      <td>339</td>
    </tr>
    <tr>
      <td></td>
      <td>AnyBIC &lt;AnyBIC&gt;</td>
      <td>[0..1]</td>
      <td>IdentifierSet</td>
      <td>C5</td>
      <td>340</td>
    </tr>
    <tr>
      <td></td>
      <td>LEI &lt;LEI&gt;</td>
      <td>[0..1]</td>
      <td>IdentifierSet</td>
      <td></td>
      <td>340</td>
    </tr>
    <tr>
      <td></td>
      <td>Other &lt;Othr&gt;</td>
      <td>[0..*]</td>
      <td></td>
      <td></td>
      <td>340</td>
    </tr>
    <tr>
      <td></td>
      <td>Identification &lt;Id&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td></td>
      <td>SchemeName &lt;SchmeNm&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Code &lt;Cd&gt;</td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Proprietary &lt;Ptry&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td></td>
      <td>Issuer &lt;Issr&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>PrivateIdentification &lt;PrvtId&gt;</td>
      <td>[1..1]</td>
      <td></td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td></td>
      <td>DateAndPlaceOfBirth &lt;DtAndPlcOfBirth&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>342</td>
    </tr>
    <tr>
      <td></td>
      <td>BirthDate &lt;BirthDt&gt;</td>
      <td>[1..1]</td>
      <td>Date</td>
      <td></td>
      <td>342</td>
    </tr>
    <tr>
      <td></td>
      <td>ProvinceOfBirth &lt;PrvcOfBirth&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>342</td>
    </tr>
    <tr>
      <td></td>
      <td>CityOfBirth &lt;CityOfBirth&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>CountryOfBirth &lt;CtryOfBirth&gt;</td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td>C7</td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>Other &lt;Othr&gt;</td>
      <td>[0..*]</td>
      <td></td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>Identification &lt;Id&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>SchemeName &lt;SchmeNm&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Code &lt;Cd&gt;</td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td></td>
      <td>344</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Proprietary &lt;Ptry&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>344</td>
    </tr>
    <tr>
      <td></td>
      <td>Issuer &lt;Issr&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>344</td>
    </tr>
    <tr>
      <td></td>
      <td>CountryOfResidence &lt;CtryOfRes&gt;</td>
      <td>[0..1]</td>
      <td>CodeSet</td>
      <td>C7</td>
      <td>344</td>
    </tr>
    <tr>
      <td></td>
      <td>ContactDetails &lt;CtctDtls&gt;</td>
      <td>[0..1]</td>
      <td>±</td>
      <td></td>
      <td>344</td>
    </tr>
  </tbody>
</table>

### 4.4.3.8.9.7 SettlementInformation <SttlmInf>

Presence: [0..1]

*Definition: Specifies the details on how the settlement of the original transaction(s) between the instructing agent and the instructed agent was completed.*

---

<!-- Page 201 -->

Impacted by: C17 "InstructedReimbursementAgentAccountRule", C18 "InstructingReimbursementAgentAccountRule", C23 "SettlementMethodAgentRule", C24 "SettlementMethodClearingRule", C25 "SettlementMethodCoverAgentRule", C26 "SettlementMethodCoverRule", C29 "ThirdReimbursementAgentAccountRule", C30 "ThirdReimbursementAgentRule"

SettlementInformation <SttlmInf> contains the following SettlementInstruction15 elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **SettlementMethod** <StlmMtd> | [1..1] | CodeSet | | 202 |
| | **SettlementAccount** <SttlmAgt> | ± | ± | C16, C15 | 203 |
| | **ClearingSystem** <ClrSys> | [0..1] | | | 203 |
| (Or | **Code** <Cd> | [1..1] | CodeSet | | 204 |
| Or) | **Proprietary** <Prtry> | [1..1] | Text | | 204 |
| | **InstructingReimbursementAgent** <InsgRmbrsmtAgt> | [0..1] | ± | | 204 |
| | **InstructingReimbursementAgentAccount** <InsgRmbrsmtAgtAcct> | [0..1] | ± | C16, C15 | 205 |
| | **InstructedReimbursementAgent** <InstdRmbrsmtAgt> | [0..1] | ± | | 205 |
| | **InstructedReimbursementAgentAccount** <InstdRmbrsmtAgtAcct> | [0..1] | ± | C16, C15 | 206 |
| | **ThirdReimbursementAgent** <ThirdRmbrsmtAgt> | [0..1] | ± | | 207 |
| | **ThirdReimbursementAgentAccount** <ThirdRmbrsmtAgtAcct> | [0..1] | ± | C16, C15 | 207 |

## Constraints

- **InstructedReimbursementAgentAccountRule**

  If InstructedReimbursementAgentAccount is present, then InstructedReimbursementAgent must be present.

  On Condition
  /InstructedReimbursementAgent is absent
  Following Must be True
  /InstructedReimbursementAgentAccount Must be absent

- **InstructingReimbursementAgentAccountRule**

  If InstructingReimbursementAgentAccount is present, then InstructingReimbursementAgent must be present.

  On Condition
  /InstructingReimbursementAgent is absent
  Following Must be True
  /InstructingReimbursementAgentAccount Must be absent

- **SettlementMethodAgentRule**

  If SettlementMethod is equal to INDA or INGA, then ReimbursementAgent(s) and ClearingSystem are not allowed.

  On Condition
  /SettlementMethod is equal to value 'InstructingAgent'
  Or /SettlementMethod is equal to value 'InstructedAgent'

---

<!-- Page 202 -->

Following Must be True
    /ClearingSystem Must be absent
    And    /InstructingReimbursementAgent Must be absent
    And    /InstructedReimbursementAgent Must be absent
    And    /ThirdReimbursementAgent Must be absent

*   **SettlementMethodClearingRule**

    If SettlementMethod is equal to CLRG, then SettlementAccount and ReimbursementAgent(s) are not allowed.

    On Condition
    /SettlementMethod is equal to value 'ClearingSystem'
    Following Must be True
    /SettlementAccount Must be absent
    And    /InstructingReimbursementAgent Must be absent
    And    /InstructedReimbursementAgent Must be absent
    And    /ThirdReimbursementAgent Must be absent

*   **SettlementMethodCoverAgentRule**

    If SettlementMethod is equal to COVE, then InstructedReimbursementAgent or InstructingReimbursementAgent must be present.

    On Condition
    /SettlementMethod is equal to value 'CoverMethod'
    Following Must be True
    /InstructingReimbursementAgent Must be present
    Or    /InstructedReimbursementAgent Must be present

*   **SettlementMethodCoverRule**

    If SettlementMethod is equal to COVE, then SettlementAccount and ClearingSystem are not allowed.

    On Condition
    /SettlementMethod is equal to value 'CoverMethod'
    Following Must be True
    /SettlementAccount Must be absent
    And    /ClearingSystem Must be absent

*   **ThirdReimbursementAgentAccountRule**

    If ThirdReimbursementAgentAccount is present, then ThirdReimbursementAgent must be present.

    On Condition
    /ThirdReimbursementAgent is absent
    Following Must be True
    /ThirdReimbursementAgentAccount Must be absent

*   **ThirdReimbursementAgentRule**

    If ThirdReimbursementAgent is present, then InstructingReimbursementAgent and InstructedReimbursementAgent must both be present.

    On Condition
    /ThirdReimbursementAgent is present
    Following Must be True
    /InstructingReimbursementAgent Must be present
    And    /InstructedReimbursementAgent Must be present

4.4.3.8.9.7.1 SettlementMethod <SttlmMtd>

*Presence:* [1..1]

*Definition:* Method used to settle the (batch of) payment instructions.

*Datatype:* "SettlementMethod1Code" on page 423

---

<!-- Page 203 -->

| CodeName | Name | Definition |
|---|---|---|
| INDA | InstructedAgent | Settlement is done by the agent instructed to execute a payment instruction. |
| INGA | InstructingAgent | Settlement is done by the agent instructing and forwarding the payment to the next party in the payment chain. |
| COVE | CoverMethod | Settlement is done through a cover payment. |
| CLRG | ClearingSystem | Settlement is done through a payment clearing system. |

## 4.4.3.8.9.7.2 SettlementAccount <SttlmAcct>

*Presence:* [0..1]

*Definition:* A specific purpose account used to post debit and credit entries as a result of the transaction.

*Impacted by:* C16 "IdentificationOrProxyPresenceRule", C15 "IdentificationAndProxyGuideline"

**SettlementAccount <SttlmAcct>** contains the following elements (see "CashAccount40" on page 309 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Identification <Id> | [0..1] | ± | | 310 |
| | Type <Tp> | [0..1] | ± | | 310 |
| | Currency <Ccy> | [0..1] | CodeSet | C2 | 310 |
| | Name <Nm> | [0..1] | Text | | 311 |
| | Proxy <Prxy> | [0..1] | ± | | 311 |

### Constraints

- **IdentificationAndProxyGuideline**

  If the account identification is not defined through a conventional identification such as an email address or a mobile number, then the proxy element should be used for the identification of the account.

- **IdentificationOrProxyPresenceRule**

  Identification must be present or Proxy must be present. Both may be present.

  ```
  Following Must be True
  /Identification Must be present
  or   /Proxy Must be present
  ```

## 4.4.3.8.9.7.3 ClearingSystem <ClrSys>

*Presence:* [0..1]

*Definition:* Specification of a pre-agreed offering between clearing agents or the channel through which the payment instruction is processed.

---

<!-- Page 204 -->

ClearingSystem <ClrSys> contains one of the following ClearingSystemIdentification3Choice elements

| Or | MessageElement <XML Tag> | Mult. | Type | Const. No. | Page |
|:---|:---|:---|:---|:---|:---|
| (Or | **Code** *<Cd>* | [1..1] | CodeSet | | 204 |
| Or) | **Proprietary** *<Prtry>* | [1..1] | Text | | 204 |

### 4.4.3.8.9.7.3.1 Code <Cd>

*Presence:* [1..1]

*Definition:* Infrastructure through which the payment instruction is processed, as published in an external clearing system identification code list.

*Datatype:* "ExternalCashClearingSystem1Code" on page 414

### 4.4.3.8.9.7.3.2 Proprietary <Prtry>

*Presence:* [1..1]

*Definition:* Clearing system identification in a proprietary form.

*Datatype:* "Max35Text" on page 431

### 4.4.3.8.9.7.4 InstructingReimbursementAgent <InstrgRmbrsmtAgent>

*Presence:* [0..1]

*Definition:* Agent through which the instructing agent will reimburse the instructed agent.

Usage: If InstructingAgent and InstructedAgent have the same reimbursement agent, then only InstructingReimbursementAgent must be used.

**InstructingReimbursementAgent <InstrgRmbrsmtAgent>** contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on page 320 for details)

| Or | MessageElement <XML Tag> | Mult. | Type | Const. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | FinancialInstitutionIdentification *<FinInstlId>* | [1..1] | | | 321 |
| | BICFI *<BICFI>* | [0..1] | IdentifierSet | C6 | 321 |
| | ClearingSystemMemberIdentification *<ClrSysMmbId>* | [0..1] | ± | | 322 |
| | LEI *<LEI>* | [0..1] | IdentifierSet | | 322 |
| | Name *<Nm>* | [0..1] | Text | | 322 |
| | PostalAddress *<PstlAdr>* | [0..1] | ± | | 322 |
| | Other *<Othr>* | [0..1] | ± | | 323 |
| | BranchIdentification *<BrnchId>* | [0..1] | | | 324 |
| | Identification *<Id>* | [0..1] | Text | | 324 |
| | LEI *<LEI>* | [0..1] | IdentifierSet | | 324 |
| | Name *<Nm>* | [0..1] | Text | | 324 |
| | PostalAddress *<PstlAdr>* | [0..1] | ± | | 324 |

---

<!-- Page 205 -->

4.4.3.8.9.7.5 InstructingReimbursementAgentAccount <InstrgRmbrsmntAggtAcct>

Presence: [0..1]

*Definition: Unambiguous identification of the account of the instructing reimbursement agent account at its servicing agent in the payment chain.*

*Impacted by: C16 "IdentificationOrProxyPresenceRule", C15 "IdentificationAndProxyGuideline"*

**InstructingReimbursementAgentAccount** <InstrgRmbrsmntAggtAcct> contains the following elements (see "CashAccount40" on page 309 for details)



| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | Identification <Id> | [0..1] | ± | | 310 |
| | Type <Tp> | [0..1] | ± | | 310 |
| | Currency <Ccy> | [0..1] | CodeSet | C2 | 310 |
| | Name <Nm> | [0..1] | Text | | 311 |
| | Proxy <Prxy> | [0..1] | ± | | 311 |

## Constraints

- **IdentificationAndProxyGuideline**

  If the account identification is not defined through a conventional identification such as an email address or a mobile number, then the proxy element should be used for the identification of the account.

- **IdentificationOrProxyPresenceRule**

  Identification must be present or Proxy must be present. Both may be present.

  ```
  Following Must be True
  /Identification Must be present
  Or
  /Proxy Must be present
  ```

4.4.3.8.9.7.6 InstructedReimbursementAgent <InstdRmbrsmntAggt>

Presence: [0..1]

*Definition: Agent at which the instructed agent will be reimbursed.*

Usage: If InstructedReimbursementAgent contains a branch of the InstructedAgent, then the party in InstructedAgent will claim reimbursement from that branch/will be paid by that branch.

Usage: If InstructingAgent and InstructedAgent have the same reimbursement agent, then only InstructingReimbursementAgent must be used.

---

<!-- Page 206 -->

InstructedReimbursementAgent <InstdRmbrsmtAgnt> contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on page 320 for details)



| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | FinancialInstitutionIdentification <FinInstlId> | [1..1] | | | 321 |
| | BICFI <BICFI> | [0..1] | IdentifierSet | C6 | 321 |
| | ClearingSystemMemberIdentification <ClrSysMmbId> | [0..1] | ± | | 322 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 322 |
| | Name <Nm> | [0..1] | Text | | 322 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 322 |
| | Other <Othr> | [0..1] | ± | | 323 |
| | BranchIdentification <BrnchId> | [0..1] | | | 324 |
| | Identification <Id> | [0..1] | Text | | 324 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 324 |
| | Name <Nm> | [0..1] | Text | | 324 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 324 |

## 4.4.3.8.9.7.7 InstructedReimbursementAgentAccount <InstdRmbrsmtAgntAcct>

Presence: [0..1]

Definition: Unambiguous identification of the account of the instructed reimbursement agent account at its servicing agent in the payment chain.

Impacted by: C16 "IdentificationOrProxyPresenceRule", C15 "IdentificationAndProxyGuideline"

InstructedReimbursementAgentAccount <InstdRmbrsmtAgntAcct> contains the following elements (see "CashAccount40" on page 309 for details)



| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | Identification <Id> | [0..1] | ± | | 310 |
| | Type <Tp> | [0..1] | ± | | 310 |
| | Currency <Ccy> | [0..1] | CodeSet | C2 | 310 |
| | Name <Nm> | [0..1] | Text | | 311 |
| | Proxy <Prxy> | [0..1] | ± | | 311 |

---

<!-- Page 207 -->

## Constraints

- **IdentificationAndProxyGuideline**

  If the account identification is not defined through a conventional identification such as an email address or a mobile number, then the proxy element should be used for the identification of the account.

- **IdentificationOrProxyPresenceRule**

  Identification must be present or Proxy must be present. Both may be present.

  ```
  Following Must be True
  /Identification Must be present
  Or
  /Proxy Must be present
  ```

### 4.4.3.8.9.7.8 ThirdReimbursementAgent <ThrdRmbrsmntAg>

*Presence:* [0..1]

*Definition:* Agent at which the instructed agent will be reimbursed.

*Usage:* If ThirdReimbursementAgent contains a branch of the InstructedAgent, then the party in InstructedAgent will claim reimbursement from that branch/will be paid by that branch.

**ThirdReimbursementAgent <ThrdRmbrsmntAg>** contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on page 320 for details)



| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | FinancialInstitutionIdentification <FinInstnId> | [1..1] |  |  | 321 |
| | BICFI <BICFI> | [0..1] | IdentifierSet | C6 | 321 |
| | ClearingSystemMemberIdentification <ClrSysMmbId> | [0..1] | ± |  | 322 |
| | LEI <LEI> | [0..1] | IdentifierSet |  | 322 |
| | Name <Nm> | [0..1] | Text |  | 322 |
| | PostalAddress <PstlAdr> | [0..1] | ± |  | 322 |
| | Other <Othr> | [0..1] | ± |  | 323 |
| | BranchIdentification <BrnchId> | [0..1] |  |  | 324 |
| | Identification <Id> | [0..1] | Text |  | 324 |
| | LEI <LEI> | [0..1] | IdentifierSet |  | 324 |
| | Name <Nm> | [0..1] | Text |  | 324 |
| | PostalAddress <PstlAdr> | [0..1] | ± |  | 324 |

### 4.4.3.8.9.7.9 ThirdReimbursementAgentAccount <ThrdRmbrsmntAg>Acct>

*Presence:* [0..1]

*Definition:* Unambiguous identification of the account of the third reimbursement agent account at its servicing agent in the payment chain.

*Impacted by:* C16 "IdentificationOrProxyPresenceRule", C15 "IdentificationAndProxyGuideline"

---

<!-- Page 208 -->

ThirdReimbursementAgentAccount <ThrdRmbrmntAgtAcc> contains the following elements (see "CashAccount40" on page 309 for details)



<table>
  <tr>
    <th>Or</th>
    <th>MessageElement&lt;XML Tag&gt;</th>
    <th>Mult.</th>
    <th>Type</th>
    <th>Constr. No.</th>
    <th>Page</th>
  </tr>
  <tr>
    <td></td>
    <td>Identification &lt;Id&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>310</td>
  </tr>
  <tr>
    <td></td>
    <td>Type &lt;Tp&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>310</td>
  </tr>
  <tr>
    <td></td>
    <td>Currency &lt;Ccy&gt;</td>
    <td>[0..1]</td>
    <td>CodeSet</td>
    <td>C2</td>
    <td>310</td>
  </tr>
  <tr>
    <td></td>
    <td>Name &lt;Nm&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>311</td>
  </tr>
  <tr>
    <td></td>
    <td>Proxy &lt;Prxy&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>311</td>
  </tr>
</table>

## Constraints

- **IdentificationAndProxyGuideline**

  If the account identification is not defined through a conventional identification such as an email address or a mobile number, then the proxy element should be used for the identification of the account.

- **IdentificationOrProxyPresenceRule**

  Identification must be present or Proxy must be present. Both may be present.

  ```
  Following Must be True
  /Identification Must be present
  Or
  /Proxy Must be present
  ```

## 4.4.3.8.9.8 PaymentTypeInformation <PmtTpInf>

*Presence:* [0..1]

*Definition:* Set of elements used to further specify the type of transaction.

---

<!-- Page 209 -->

PaymentTypeInfo <PmtTplnf> contains the following elements (see "PaymentTypeInfo27" on page 351 for details)



<table>
  <tr>
    <th>Or</th>
    <th>MessageElement &lt;XML Tag&gt;</th>
    <th>Mult.</th>
    <th>Type</th>
    <th>Constr. No.</th>
    <th>Page</th>
  </tr>
  <tr>
    <td></td>
    <td>InstructionPriority &lt;InstrPrty&gt;</td>
    <td>[0..1]</td>
    <td>CodeSet</td>
    <td></td>
    <td>351</td>
  </tr>
  <tr>
    <td></td>
    <td>ClearingChannel &lt;ClrChanl&gt;</td>
    <td>[0..1]</td>
    <td>CodeSet</td>
    <td></td>
    <td>351</td>
  </tr>
  <tr>
    <td></td>
    <td>ServiceLevel &lt;SvcLvl&gt;</td>
    <td>[0..*]</td>
    <td></td>
    <td></td>
    <td>352</td>
  </tr>
  <tr>
    <td>Or</td>
    <td>Code &lt;Cd&gt;</td>
    <td>[1..1]</td>
    <td>CodeSet</td>
    <td></td>
    <td>352</td>
  </tr>
  <tr>
    <td>Or</td>
    <td>Proprietary &lt;Ptry&gt;</td>
    <td>[1..1]</td>
    <td>Text</td>
    <td></td>
    <td>352</td>
  </tr>
  <tr>
    <td></td>
    <td>LocalInstrument &lt;LclInstrm&gt;</td>
    <td>[0..1]</td>
    <td></td>
    <td></td>
    <td>352</td>
  </tr>
  <tr>
    <td>Or</td>
    <td>Code &lt;Cd&gt;</td>
    <td>[1..1]</td>
    <td>CodeSet</td>
    <td></td>
    <td>352</td>
  </tr>
  <tr>
    <td>Or</td>
    <td>Proprietary &lt;Ptry&gt;</td>
    <td>[1..1]</td>
    <td>Text</td>
    <td></td>
    <td>353</td>
  </tr>
  <tr>
    <td></td>
    <td>SequenceType &lt;SeqTp&gt;</td>
    <td>[0..1]</td>
    <td>CodeSet</td>
    <td></td>
    <td>353</td>
  </tr>
  <tr>
    <td></td>
    <td>CategoryPurpose &lt;CtgyPurp&gt;</td>
    <td>[0..1]</td>
    <td></td>
    <td></td>
    <td>353</td>
  </tr>
  <tr>
    <td>Or</td>
    <td>Code &lt;Cd&gt;</td>
    <td>[1..1]</td>
    <td>CodeSet</td>
    <td></td>
    <td>353</td>
  </tr>
  <tr>
    <td>Or</td>
    <td>Proprietary &lt;Ptry&gt;</td>
    <td>[1..1]</td>
    <td>Text</td>
    <td></td>
    <td>353</td>
  </tr>
</table>

## 4.4.3.8.9.9 PaymentMethod <PmtMtd>

*Presence:* [0..1]

*Definition:* Specifies the means of payment that will be used to move the amount of money.

*DataType:* "PaymentMethod4Code" on page 421



<table>
  <tr>
    <th>CodeName</th>
    <th>Name</th>
    <th>Definition</th>
  </tr>
  <tr>
    <td>CHK</td>
    <td>Cheque</td>
    <td>Written order to a bank to pay a certain amount of money from one person to another person.</td>
  </tr>
  <tr>
    <td>TRF</td>
    <td>CreditTransfer</td>
    <td>Transfer of an amount of money in the books of the account servicer.</td>
  </tr>
  <tr>
    <td>DD</td>
    <td>DirectDebit</td>
    <td>Collection of an amount of money from the debtor's bank account by the creditor. The amount of money and dates of collections may vary.</td>
  </tr>
  <tr>
    <td>TRA</td>
    <td>TransferAdvice</td>
    <td>Transfer of an amount of money in the books of the account servicer. An advice should be sent back to the account owner.</td>
  </tr>
</table>

## 4.4.3.8.9.10 MandateRelatedInformation <MndtRltdInf>

*Presence:* [0..1]

*Definition:* Provides further details of the mandate signed between the creditor and the debtor.

---

<!-- Page 210 -->

MandateRelatedInformation <MndtRltdInf> contains one of the following MandateRelatedData3Choice elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| (Or | **DirectDebitMandate** <DtrctDbtMndt> | [0..1] | | C2, C3 | 211 |
| | **MandateIdentification** <MndtId> | [0..1] | Text | | 213 |
| | **DateOfSignature** <DtOfSgntr> | [0..1] | Date | | 213 |
| | **AmendmentIndicator** <AmdmntInd> | [0..1] | Indicator | | 213 |
| | **AmendmentInformationDetails** <AmdmntInfDtls> | [0..1] | | | 213 |
| | **OriginalMandateIdentification** <OrgnlMndtId> | [0..1] | Text | | 214 |
| | **OriginalCreditorSchemeIdentification** <OrgnlCdtrSchemId> | [0..1] | ± | | 214 |
| | **OriginalCreditorAgent** <OrgnlCdtrAgt> | [0..1] | ± | | 215 |
| | **OriginalCreditorAgentAccount** <OrgnlCdtrAgtAcct> | [0..1] | ± | C16, C15 | 216 |
| | **OriginalDebtor** <OrgnlDbtr> | [0..1] | ± | | 217 |
| | **OriginalDebtorAccount** <OrgnlDbtrAcct> | [0..1] | ± | C16, C15 | 218 |
| | **OriginalDebtorAgent** <OrgnlDbtrAgt> | [0..1] | ± | | 219 |
| | **OriginalDebtorAgentAccount** <OrgnlDbtrAgtAcct> | [0..1] | ± | C16, C15 | 220 |
| | **OriginalFinalCollectionDate** <OrgnlFnlCollnDt> | [0..1] | Date | | 221 |
| | **OriginalFrequency** <OrgnlFrqcy> | [0..1] | ± | | 221 |
| | **OriginalReason** <OrgnlRsn> | [0..1] | | | 221 |
| (Or | **Code** <Cd> | [1..1] | CodeSet | | 221 |
| Or) | **Proprietary** <Ptry> | [1..1] | Text | | 221 |
| | **OriginalTrackingDays** <OrgnlTrckgDays> | [0..1] | Text | | 222 |
| | **ElectronicSignature** <ElctrncSgntr> | [0..1] | Text | | 222 |
| | **FirstCollectionDate** <FirstCollnDt> | [0..1] | Date | | 222 |
| | **FinalCollectionDate** <FnllCollnDt> | [0..1] | Date | | 222 |
| | **Frequency** <Frqcy> | [0..1] | ± | | 222 |
| | **Reason** <Rsn> | [0..1] | | | 222 |
| (Or | **Code** <Cd> | [1..1] | CodeSet | | 223 |
| Or) | **Proprietary** <Ptry> | [1..1] | Text | | 223 |
| | **TrackingDays** <TrckgDays> | [0..1] | Text | | 223 |
| Or) | **CreditTransferMandate** <CdtTrfMndt> | [0..1] | ± | | 223 |

---

<!-- Page 211 -->

**4.4.3.8.9.10.1 DirectDebitMandate &lt;DrctDbtMndt&gt;**

*Presence:* [0..1]

*Definition:* Specific direct debit mandate data.

*Impacted by:* C2 "AmendmentIndicatorFalseRule", C3 "AmendmentIndicatorTrueRule"

---

<!-- Page 212 -->

DirectDebitMandate `<DrctDbtMndt>` contains the following **MandateRelatedInformation16** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **MandateIdentification** `<MndId>` | [0..1] | Text | | 213 |
| | **DateOfSignature** `<DtOfSgntr>` | [0..1] | Date | | 213 |
| | **AmendmentIndicator** `<AmdmntInd>` | [0..1] | Indicator | | 213 |
| | **AmendmentInformationDetails** `<AmdmntInfDtls>` | [0..1] | | | 213 |
| | **OriginalMandateIdentification** `<OrgnlMndId>` | [0..1] | Text | | 214 |
| | **OriginalCreditorSchemeIdentification** `<OrgnCddrSchemId>` | [0..1] | ± | | 214 |
| | **OriginalCreditorAgent** `<OrgnCddrAgt>` | [0..1] | ± | | 215 |
| | **OriginalCreditorAgentAccount** `<OrgnCddrAgtAcct>` | [0..1] | ± | C16, C15 | 216 |
| | **OriginalDebtor** `<OrgnlDbtr>` | [0..1] | ± | | 217 |
| | **OriginalDebtorAccount** `<OrgnlDbtrAcct>` | [0..1] | ± | C16, C15 | 218 |
| | **OriginalDebtorAgent** `<OrgnlDbtrAgt>` | [0..1] | ± | | 219 |
| | **OriginalDebtorAgentAccount** `<OrgnlDbtrAgtAcct>` | [0..1] | ± | C16, C15 | 220 |
| | **OriginalFinalCollectionDate** `<OrgnlFnClctnDt>` | [0..1] | Date | | 221 |
| | **OriginalFrequency** `<OrgnlFrqcy>` | [0..1] | ± | | 221 |
| | **OriginalReason** `<OrgnlRsn>` | [0..1] | | | 221 |
| [Or | **Code** `<Cd>` | [1..1] | CodeSet | | 221 |
| Or] | **Proprietary** `<Prtty>` | [1..1] | Text | | 221 |
| | **OriginalTrackingDays** `<OrgnlTrckgDays>` | [0..1] | Text | | 222 |
| | **ElectronicSignature** `<ElctrncSgntr>` | [0..1] | Text | | 222 |
| | **FirstCollectionDate** `<FrstColltnDt>` | [0..1] | Date | | 222 |
| | **FinalCollectionDate** `<FnColltnDt>` | [0..1] | Date | | 222 |
| | **Frequency** `<Frqcy>` | [0..1] | ± | | 222 |
| | **Reason** `<Rsn>` | [0..1] | | | 222 |
| [Or | **Code** `<Cd>` | [1..1] | CodeSet | | 223 |
| Or] | **Proprietary** `<Prtty>` | [1..1] | Text | | 223 |
| | **TrackingDays** `<TrckgDays>` | [0..1] | Text | | 223 |

## Constraints

- **AmendmentIndicatorFalseRule**
  If AmendmentIndicator is false, then AmendmentInformationDetails is not allowed.

---

<!-- Page 213 -->

On Condition
/AmendmentIndicator is equal to value 'false'
Following Must be True
/AmendmentInformationDetails Must be absent

* **AmendmentIndicatorTrueRule**
  If AmendmentIndicator is true, then AmendmentInformationDetails must be present.
  On Condition
  /AmendmentIndicator is equal to value 'true'
  Following Must be True
  /AmendmentInformationDetails Must be present

**4.4.3.8.9.10.1.1 MandateIdentification <MndId>**

*Presence:* [0..1]

*Definition:* Unique identification, as assigned by the creditor, to unambiguously identify the mandate.

*Datatype:* "Max35Text" on page 431

**4.4.3.8.9.10.1.2 DateOfSignature <DtOfSgntr>**

*Presence:* [0..1]

*Definition:* Date on which the direct debit mandate has been signed by the debtor.

*Datatype:* "ISODate" on page 425

**4.4.3.8.9.10.1.3 AmendmentIndicator <AmdmntInd>**

*Presence:* [0..1]

*Definition:* Indicator notifying whether the underlying mandate is amended or not.

*Datatype:* One of the following values must be used (see "TrueFalseIndicator" on page 427):

* Meaning When True: True

* Meaning When False: False

**4.4.3.8.9.10.1.4 AmendmentInformationDetails <AmdmntInfDtls>**

*Presence:* [0..1]

*Definition:* List of mandate elements that have been modified.

---

<!-- Page 214 -->

AmendmentInformationDetails <AmdmInfDtls> contains the following AmendmentInformationDetails15 elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **OriginalMandateIdentification** <OrgnlMndtd> | [0..1] | Text | | 214 |
| | **OriginalCreditorSchemeIdentification** <OrgnlCdrtrSchmeId> | [0..1] | ± | | 214 |
| | **OriginalCreditorAgent** <OrgnlCdrtrAgt> | [0..1] | ± | | 215 |
| | **OriginalCreditorAgentAccount** <OrgnlCdrtrAgtAcct> | [0..1] | ± | C16, C15 | 216 |
| | **OriginalDebtor** <OrgnlDbtr> | [0..1] | ± | | 217 |
| | **OriginalDebtorAccount** <OrgnlDbtrAcct> | [0..1] | ± | C16, C15 | 218 |
| | **OriginalDebtorAgent** <OrgnlDbtrAgt> | [0..1] | ± | | 219 |
| | **OriginalDebtorAgentAccount** <OrgnlDbtrAgtAcct> | [0..1] | ± | C16, C15 | 220 |
| | **OriginalFinalCollectionDate** <OrgnlFinlColltnDt> | [0..1] | Date | | 221 |
| | **OriginalFrequency** <OrgnlFrqcy> | [0..1] | ± | | 221 |
| | **OriginalReason** <OrgnlRsn> | [0..1] | | | 221 |
| Or | **Code** <Cd> | [1..1] | CodeSet | | 221 |
| Or | **Proprietary** <Prtry> | [1..1] | Text | | 221 |
| | **OriginalTrackingDays** <OrgnlTrckgDays> | [0..1] | Text | | 222 |

**4.4.3.8.9.10.1.4.1 OriginalMandateIdentification <OrgnlMndtd>**

*Presence:* [0..1]

*Definition:* Unique identification, as assigned by the creditor, to unambiguously identify the original mandate.

*Datatype:* "Max35Text" on page 431

**4.4.3.8.9.10.1.4.2 OriginalCreditorSchemeIdentification <OrgnlCdrtrSchmeId>**

*Presence:* [0..1]

*Definition:* Original creditor scheme identification that has been modified.

---

<!-- Page 215 -->

OriginalCreditorSchemeIdentification <OrgnlCdrSchmeId> contains the following elements (see "PartyIdentification22" on page 336 for details)



<table>
  <thead>
    <tr>
      <th>Or</th>
      <th>MessageElement&lt;XML Tag&gt;</th>
      <th>Mult.</th>
      <th>Type</th>
      <th>Constr. No.</th>
      <th>Page</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td>Name &lt;Nm&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>337</td>
    </tr>
    <tr>
      <td></td>
      <td>PostalAddress &lt;PstlAdr&gt;</td>
      <td></td>
      <td>±</td>
      <td></td>
      <td>338</td>
    </tr>
    <tr>
      <td></td>
      <td>Identification &lt;Id&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>338</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>OrganisationIdentification &lt;OrgId&gt;</td>
      <td>[1..1]</td>
      <td></td>
      <td></td>
      <td>339</td>
    </tr>
    <tr>
      <td></td>
      <td>AnyBIC &lt;AnyBIC&gt;</td>
      <td>[0..1]</td>
      <td>IdentifierSet</td>
      <td>C5</td>
      <td>340</td>
    </tr>
    <tr>
      <td></td>
      <td>LEI &lt;LEI&gt;</td>
      <td>[0..1]</td>
      <td>IdentifierSet</td>
      <td></td>
      <td>340</td>
    </tr>
    <tr>
      <td></td>
      <td>Other &lt;Othr&gt;</td>
      <td>[0..*]</td>
      <td></td>
      <td></td>
      <td>340</td>
    </tr>
    <tr>
      <td></td>
      <td>Identification &lt;Id&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td></td>
      <td>SchemeName &lt;SchmeNm&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Code &lt;Cd&gt;</td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Proprietary &lt;Ptry&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td></td>
      <td>Issuer &lt;Issr&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>PrivateIdentification &lt;PrvtId&gt;</td>
      <td>[1..1]</td>
      <td></td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td></td>
      <td>DateAndPlaceOfBirth &lt;DtAndPlcOfBirth&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>342</td>
    </tr>
    <tr>
      <td></td>
      <td>BirthDate &lt;BirthDt&gt;</td>
      <td>[1..1]</td>
      <td>Date</td>
      <td></td>
      <td>342</td>
    </tr>
    <tr>
      <td></td>
      <td>ProvinceOfBirth &lt;PrvcOfBirth&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>342</td>
    </tr>
    <tr>
      <td></td>
      <td>CityOfBirth &lt;CityOfBirth&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>CountryOfBirth &lt;CtryOfBirth&gt;</td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td>C7</td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>Other &lt;Othr&gt;</td>
      <td>[0..*]</td>
      <td></td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>Identification &lt;Id&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>SchemeName &lt;SchmeNm&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Code &lt;Cd&gt;</td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td></td>
      <td>344</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Proprietary &lt;Ptry&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>344</td>
    </tr>
    <tr>
      <td></td>
      <td>Issuer &lt;Issr&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>344</td>
    </tr>
    <tr>
      <td></td>
      <td>CountryOfResidence &lt;CtryOfRes&gt;</td>
      <td>[0..1]</td>
      <td>CodeSet</td>
      <td>C7</td>
      <td>344</td>
    </tr>
    <tr>
      <td></td>
      <td>ContactDetails &lt;CtctDtls&gt;</td>
      <td>[0..1]</td>
      <td>±</td>
      <td></td>
      <td>344</td>
    </tr>
  </tbody>
</table>

**4.4.3.8.9.10.1.4.3 OriginalCreditorAgent <OrgnlCdrAgt>**

*Presence:* [0..1]

*Definition:* Original creditor agent that has been modified.

---

<!-- Page 216 -->

OriginalCreditorAgent <OrgnlCddtrAgt> contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on page 320 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | FinancialInstitutionIdentification <FinInstlId> | [0..1] | | | 321 |
| | BICFI <BICFI> | | IdentifierSet | C6 | 321 |
| | ClearingSystemMemberIdentification <ClrSysMmbId> | [0..1] | ± | | 322 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 322 |
| | Name <Nm> | [0..1] | Text | | 322 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 322 |
| | Other <Othr> | [0..1] | ± | | 323 |
| | BranchIdentification <BrnchId> | [0..1] | | | 324 |
| | Identification <Id> | [0..1] | Text | | 324 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 324 |
| | Name <Nm> | [0..1] | Text | | 324 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 324 |

### 4.4.3.8.9.10.1.4.4 OriginalCreditorAgentAccount <OrgnlCddtrAgtAcc>

Presence: [0..1]

Definition: Original creditor agent account that has been modified.

Impacted by: C16 "IdentificationOrProxyPresenceRule", C15 "IdentificationAndProxyGuideline"

OriginalCreditorAgentAccount <OrgnlCddtrAgtAcc> contains the following elements (see "CashAccount40" on page 309 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | Identification <Id> | [0..1] | ± | | 310 |
| | Type <Tp> | [0..1] | ± | | 310 |
| | Currency <Ccy> | [0..1] | CodeSet | C2 | 310 |
| | Name <Nm> | [0..1] | Text | | 311 |
| | Proxy <Prxy> | [0..1] | ± | | 311 |

## Constraints

- **IdentificationAndProxyGuideline**
  If the account identification is not defined through a conventional identification such as an email address or a mobile number, then the proxy element should be used for the identification of the account.

- **IdentificationOrProxyPresenceRule**
  Identification must be present or Proxy must be present. Both may be present.

---

<!-- Page 217 -->

```
Following Must be True
  /Identification Must be present
  Or    /Proxy Must be present
```

**4.4.3.8.9.10.1.4.5 OriginalDebtor <OrgnlDbtr>**

*Presence:* [0..1]

*Definition:* Original debtor that has been modified.

---

<!-- Page 218 -->

OriginalDebtor <OrgnlDbtr> contains the following elements (see "PartyIdentification27" on page 336 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | Name <Nm> | [0..1] | Text | | 337 |
| | PostalAddress <PstlAdr> | | ± | | 338 |
| | Identification <Id> | [0..1] | | | 338 |
| (Or | OrganisationIdentification <OrgId> | [1..1] | | | 339 |
| | AnyBIC <AnyBIC> | [0..1] | IdentifierSet | C5 | 340 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 340 |
| | Other <Othr> | [0..*] | | | 340 |
| | Identification <Id> | [1..1] | Text | | 341 |
| | SchemeName <SchmeNm> | [0..1] | | | 341 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 341 |
| Or | Proprietary <Prtry> | [1..1] | Text | | 341 |
| | Issuer <Issr> | [0..1] | Text | | 341 |
| (Or | PrivateIdentification <PrvtId> | [1..1] | | | 341 |
| | DateAndPlaceOfBirth <DtAndPlcOfBirth> | [0..1] | | | 342 |
| | BirthDate <BirthDt> | [1..1] | Date | | 342 |
| | ProvinceOfBirth <PrvcOfBirth> | [0..1] | Text | | 342 |
| | CityOfBirth <CityOfBirth> | [1..1] | Text | | 343 |
| | CountryOfBirth <CtryOfBirth> | [1..1] | CodeSet | C7 | 343 |
| | Other <Othr> | [0..*] | | | 343 |
| | Identification <Id> | [1..1] | Text | | 343 |
| | SchemeName <SchmeNm> | [0..1] | | | 343 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 344 |
| Or | Proprietary <Prtry> | [1..1] | Text | | 344 |
| | Issuer <Issr> | [0..1] | Text | | 344 |
| | CountryOfResidence <CtryOfRes> | [0..1] | CodeSet | C7 | 344 |
| | ContactDetails <CtctDtls> | [0..1] | ± | | 344 |

**4.4.3.8.9.10.1.4.6 OriginalDebtorAccount <OrgnlDbtrAcct>**
*Presence:* [0..1]
*Definition:* Original debtor account that has been modified.
*Impacted by:* C16 "IdentificationOrProxyPresenceRule", C15 "IdentificationAndProxyGuideline"

---

<!-- Page 219 -->

OriginalDebtorAccount <OrgnlDbtrAct> contains the following elements (see "CashAccount40" on page 309 for details)



<table>
  <thead>
    <tr>
      <th>Or</th>
      <th>MessageElement&lt;XML Tag&gt;</th>
      <th>Mult.</th>
      <th>Type</th>
      <th>Constr. No.</th>
      <th>Page</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td>Identification &lt;Id&gt;</td>
      <td>[0..1]</td>
      <td>±</td>
      <td></td>
      <td>310</td>
    </tr>
    <tr>
      <td></td>
      <td>Type &lt;Tp&gt;</td>
      <td>[0..1]</td>
      <td>±</td>
      <td></td>
      <td>310</td>
    </tr>
    <tr>
      <td></td>
      <td>Currency &lt;Ccy&gt;</td>
      <td>[0..1]</td>
      <td>CodeSet</td>
      <td>C2</td>
      <td>310</td>
    </tr>
    <tr>
      <td></td>
      <td>Name &lt;Nm&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>311</td>
    </tr>
    <tr>
      <td></td>
      <td>Proxy &lt;Prxy&gt;</td>
      <td>[0..1]</td>
      <td>±</td>
      <td></td>
      <td>311</td>
    </tr>
  </tbody>
</table>

## Constraints

- **IdentificationAndProxyGuideline**

  If the account identification is not defined through a conventional identification such as an email address or a mobile number, then the proxy element should be used for the identification of the account.

- **IdentificationOrProxyPresenceRule**

  Identification must be present or Proxy must be present. Both may be present.

  ```
  Following Must be True
  /Identification Must be present
  Or
  /Proxy Must be present
  ```

### 4.4.3.8.9.10.1.4.7 OriginalDebtorAgent <OrgnlDbtrAgt>

*Presence:* [0..1]

*Definition:* Original debtor agent that has been modified.

---

<!-- Page 220 -->

OriginalDebtorAgent <OrgnlDbtrAgt> contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on page 320 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | FinancialInstitutionIdentification <FinInstlId> | [1..1] | | | 321 |
| | BICFI <BICFI> | [0..1] | IdentifierSet | C6 | 321 |
| | ClearingSystemMemberIdentification <ClrSysMmbId> | [0..1] | ± | | 322 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 322 |
| | Name <Nm> | [0..1] | Text | | 322 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 322 |
| | Other <Othr> | [0..1] | ± | | 323 |
| | BranchIdentification <BrnchId> | [0..1] | | | 324 |
| | Identification <Id> | [0..1] | Text | | 324 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 324 |
| | Name <Nm> | [0..1] | Text | | 324 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 324 |

**4.4.3.8.9.10.1.4.8 OriginalDebtorAgentAccount <OrgnlDbtrAgtAcct>**

Presence: [0..1]

Definition: Original debtor agent account that has been modified.

Impacted by: C16 "IdentificationOrProxyPresenceRule", C15 "IdentificationAndProxyGuideline"

OriginalDebtorAgentAccount <OrgnlDbtrAgtAcct> contains the following elements (see "CashAccount40" on page 309 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | Identification <Id> | [0..1] | ± | | 310 |
| | Type <Tp> | [0..1] | ± | | 310 |
| | Currency <Ccy> | [0..1] | CodeSet | C2 | 310 |
| | Name <Nm> | [0..1] | Text | | 311 |
| | Proxy <Prxy> | [0..1] | ± | | 311 |

## Constraints

*   **IdentificationAndProxyGuideline**

    If the account identification is not defined through a conventional identification such as an email address or a mobile number, then the proxy element should be used for the identification of the account.

*   **IdentificationOrProxyPresenceRule**

    Identification must be present or Proxy must be present. Both may be present.

---

<!-- Page 221 -->

Following Must be True
/Identification Must be present
Or /Proxy Must be present

**4.4.3.8.9.10.1.4.9 OriginalFinalCollectionDate <OrgnlFrnlColltnDt>**

*Presence:* [0..1]

*Definition:* Original final collection date that has been modified.

*DataType:* "ISODate" on page 425

**4.4.3.8.9.10.1.4.10 OriginalFrequency <OrgnlFrqcy>**

*Presence:* [0..1]

*Definition:* Original frequency that has been modified.

**OriginalFrequency <OrgnlFrqcy>** contains one of the following elements (see "Frequency36Choice" on page 326 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| Or | **Type** *<Tp>* | [1..1] | CodeSet | | 327 |
| Or | **Period** *<Prd>* | [1..1] | | | 327 |
| | **Type** *<Tp>* | [1..1] | CodeSet | | 328 |
| | **CountPerPeriod** *<CntPerPrd>* | [1..1] | Quantity | | 328 |
| Or) | **PointInTime** *<PtInTm>* | [1..1] | | | 328 |
| | **Type** *<Tp>* | [1..1] | CodeSet | | 328 |
| | **PointInTime** *<PtInTm>* | [1..1] | Text | | 329 |

**4.4.3.8.9.10.1.4.11 OriginalReason <OrgnlRsn>**

*Presence:* [0..1]

*Definition:* Original reason for the mandate to allow the user to distinguish between different mandates for the same creditor.

**OriginalReason <OrgnlRsn>** contains one of the following MandateSetupReason1Choice elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| Or | **Code** *<Cd>* | [1..1] | CodeSet | | 221 |
| Or) | **Proprietary** *<Prtry>* | [1..1] | Text | | 221 |

**4.4.3.8.9.10.1.4.11.1 Code <Cd>**

*Presence:* [1..1]

*Definition:* Reason for the mandate setup, as published in an external reason code list.

*DataType:* "ExternalMandateSetupReason1Code" on page 417

**4.4.3.8.9.10.1.4.11.2 Proprietary <Prtry>**

*Presence:* [1..1]

---

<!-- Page 222 -->

Definition: Reason for the mandate setup, in a proprietary form.
Datatype: "Max70Text" on page 431

## 4.4.3.8.9.10.1.4.12 OriginalTrackingDays <OrgnlTrckgDays>

*Presence:* [0..1]

*Definition:* Original number of tracking days that has been modified.

*Datatype:* "Exact2NumericText" on page 428

## 4.4.3.8.9.10.1.5 ElectronicSignature <ElctrncSgntr>

*Presence:* [0..1]

*Definition:* Additional security provisions, such as a digital signature, as provided by the debtor.

*Datatype:* "Max1025Text" on page 429

## 4.4.3.8.9.10.1.6 FirstCollectionDate <FrstColltnDt>

*Presence:* [0..1]

*Definition:* Date of the first collection of a direct debit as per the mandate.

*Datatype:* "ISODate" on page 425

## 4.4.3.8.9.10.1.7 FinalCollectionDate <FnllColltnDt>

*Presence:* [0..1]

*Definition:* Date of the final collection of a direct debit as per the mandate.

*Datatype:* "ISODate" on page 425

## 4.4.3.8.9.10.1.8 Frequency <Frcy>

*Presence:* [0..1]

*Definition:* Regularity with which direct debit instructions are to be created and processed.

**Frequency <Frcy>** contains one of the following elements (see "Frequency36Choice" on page 326 for details)

| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| (Or | Type <Tp> | [1..1] | CodeSet | | 327 |
| Or | Period <Prd> | [1..1] | | | 327 |
| | Type <Tp> | [1..1] | CodeSet | | 328 |
| | CountPerPeriod <CntPerPrd> | [1..1] | Quantity | | 328 |
| Or) | PointInTime <Ptlntm> | [1..1] | | | 328 |
| | Type <Tp> | [1..1] | CodeSet | | 328 |
| | PointInTime <Ptlntm> | [1..1] | Text | | 329 |

## 4.4.3.8.9.10.1.9 Reason <Rsn>

*Presence:* [0..1]

---

<!-- Page 223 -->

*Definition:* Reason for the direct debit mandate to allow the user to distinguish between different mandates for the same creditor.

**Reason** <Rsn> contains one of the following **MandateSetupReason1Choice** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| (Or | **Code** <Cd> | [1..1] | CodeSet | | 223 |
| Or) | **Proprietary** <Prtry> | [1..1] | Text | | 223 |

**4.4.3.8.9.10.1.9.1 Code <Cd>**

*Presence:* [1..1]

*Definition:* Reason for the mandate setup, as published in an external reason code list.

*Datatype:* "ExternalMandateSetupReason1Code" on page 417

**4.4.3.8.9.10.1.9.2 Proprietary <Prtry>**

*Presence:* [1..1]

*Definition:* Reason for the mandate setup, in a proprietary form.

*Datatype:* "Max70Text" on page 431

**4.4.3.8.9.10.1.10 TrackingDays <TrckgDays>**

*Presence:* [0..1]

*Definition:* Specifies the number of days the direct debit instruction must be tracked.

*Datatype:* "Exact2NumericText" on page 428

**4.4.3.8.9.10.2 CreditTransferMandate <CdtTrfMndt>**

*Presence:* [0..1]

*Definition:* Specific credit transfer mandate data.

---

<!-- Page 224 -->

**CreditTransferMandate <CdtTrfMndt>** contains the following elements (see "CreditTransferMandateData1" on page 317 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | MandateIdentification <MndId> | [0..1] | Text | | 317 |
| | Type <Tp> | [0..1] | ± | | 317 |
| | DateOfSignature <DtOfSgntr> | [0..1] | Date | | 318 |
| | DateOfVerification <DtOfVrfctn> | [0..1] | DateTime | | 318 |
| | ElectronicSignature <ElctrncSgntr> | [0..1] | Binary | | 318 |
| | FirstPaymentDate <FrstPmtDt> | [0..1] | Date | | 318 |
| | FinalPaymentDate <FnlpmtDt> | [0..1] | Date | | 318 |
| | Frequency <Frqcy> | [0..1] | ± | | 319 |
| | Reason <Rsn> | [0..1] | | | 319 |
| Or | Code <Cd> | [1..1] | CodeSet | | 319 |
| Or | Proprietary <Pry> | [1..1] | Text | | 319 |

### 4.4.3.8.9.11 RemittanceInformation <RmtInf>

*Presence: [0..1]*

*Definition: Information supplied to enable the matching of an entry with the items that the transfer is intended to settle, such as commercial invoices in an accounts' receivable system.*

**RemittanceInformation <RmtInf>** contains the following elements (see "RemittanceInformation22" on page 364 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | Unstructured <Ustrd> | [0..*] | Text | | 364 |
| | Structured <Strd> | [0..*] | ± | | 364 |

### 4.4.3.8.9.12 UltimateDebtor <UltmtDbtr>

*Presence: [0..1]*

*Definition: Ultimate party that owes an amount of money to the (ultimate) creditor.*

**UltimateDebtor <UltmtDbtr>** contains one of the following **Party50Choice** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| Or | **Party** <Pty> | [1..1] | ± | | 224 |
| Or | **Agent** <Agt> | [1..1] | ± | | 225 |

### 4.4.3.8.9.12.1 Party <Pty>

*Presence: [1..1]*

*Definition: Identification of a person or an organisation.*

---

<!-- Page 225 -->

Party `<Pty>` contains the following elements (see "PartyIdentification272" on page 336 for details)



<table>
  <thead>
    <tr>
      <th>Or</th>
      <th>MessageElement&lt;XML Tag&gt;</th>
      <th>Mult.</th>
      <th>Type</th>
      <th>Constr. No.</th>
      <th>Page</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td>Name &lt;Nm&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>337</td>
    </tr>
    <tr>
      <td></td>
      <td>PostalAddress &lt;PstlAdr&gt;</td>
      <td>[0..1]</td>
      <td>±</td>
      <td></td>
      <td>338</td>
    </tr>
    <tr>
      <td></td>
      <td>Identification &lt;Id&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>338</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>OrganisationIdentification &lt;OrgId&gt;</td>
      <td>[1..1]</td>
      <td></td>
      <td></td>
      <td>339</td>
    </tr>
    <tr>
      <td></td>
      <td>AnyBIC &lt;AnyBIC&gt;</td>
      <td>[0..1]</td>
      <td>IdentifierSet</td>
      <td>C5</td>
      <td>340</td>
    </tr>
    <tr>
      <td></td>
      <td>LEI &lt;LEI&gt;</td>
      <td>[0..1]</td>
      <td>IdentifierSet</td>
      <td></td>
      <td>340</td>
    </tr>
    <tr>
      <td></td>
      <td>Other &lt;Othr&gt;</td>
      <td>[0..*]</td>
      <td></td>
      <td></td>
      <td>340</td>
    </tr>
    <tr>
      <td></td>
      <td>Identification &lt;Id&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td></td>
      <td>SchemeName &lt;SchmeNm&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Code &lt;Cd&gt;</td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Proprietary &lt;Prtry&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td></td>
      <td>Issuer &lt;Issr&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>PrivateIdentification &lt;PrvtId&gt;</td>
      <td>[1..1]</td>
      <td></td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td></td>
      <td>DateAndPlaceOfBirth &lt;DtAndPlcOfBrth&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>342</td>
    </tr>
    <tr>
      <td></td>
      <td>BirthDate &lt;BirthDt&gt;</td>
      <td>[1..1]</td>
      <td>Date</td>
      <td></td>
      <td>342</td>
    </tr>
    <tr>
      <td></td>
      <td>ProvinceOfBirth &lt;PvcOfBrth&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>342</td>
    </tr>
    <tr>
      <td></td>
      <td>CityOfBirth &lt;CityOfBrth&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>CountryOfBirth &lt;CtryOfBrth&gt;</td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td>C7</td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>Other &lt;Othr&gt;</td>
      <td>[0..*]</td>
      <td></td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>Identification &lt;Id&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>SchemeName &lt;SchmeNm&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Code &lt;Cd&gt;</td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td></td>
      <td>344</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Proprietary &lt;Prtry&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>344</td>
    </tr>
    <tr>
      <td></td>
      <td>Issuer &lt;Issr&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>344</td>
    </tr>
    <tr>
      <td></td>
      <td>CountryOfResidence &lt;CtryOfRes&gt;</td>
      <td>[0..1]</td>
      <td>CodeSet</td>
      <td>C7</td>
      <td>344</td>
    </tr>
    <tr>
      <td></td>
      <td>ContactDetails &lt;CtctDtls&gt;</td>
      <td>[0..1]</td>
      <td>±</td>
      <td></td>
      <td>344</td>
    </tr>
  </tbody>
</table>

### 4.4.3.8.9.12.2 Agent <Ag>

Presence: [1..1]

Definition: Identification of a financial institution.

---

<!-- Page 226 -->

Agent <Agt> contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on page 320 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | FinancialInstitutionIdentification <FinInstlId> | [1..1] | | | 321 |
| | BICFI <BICFI> | [0..1] | IdentifierSet | C6 | 321 |
| | ClearingSystemMemberIdentification <ClrSysMmbId> | [0..1] | ± | | 322 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 322 |
| | Name <Nm> | [0..1] | Text | | 322 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 322 |
| | Other <Othr> | [0..1] | ± | | 323 |
| | BranchIdentification <BrnchId> | [0..1] | | | 324 |
| | Identification <Id> | [0..1] | Text | | 324 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 324 |
| | Name <Nm> | [0..1] | Text | | 324 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 324 |

### 4.4.3.8.9.13 Debtor <Dbtr>

*Presence:* [0..1]

*Definition:* Party that owes an amount of money to the (ultimate) creditor.

**Debtor <Dbtr>** contains one of the following **Party50Choice** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| (Or | Party <Pty> | [1..1] | ± | | 226 |
| Or) | Agent <Agt> | [1..1] | ± | | 227 |

### 4.4.3.8.9.13.1 Party <Pty>

*Presence:* [1..1]

*Definition:* Identification of a person or an organisation.

---

<!-- Page 227 -->

Party <Pty> contains the following elements (see "PartyIdentification27" on page 336 for details)



<table>
  <tr>
    <th>Or</th>
    <th>MessageElement &lt;XML Tag&gt;</th>
    <th>Mult.</th>
    <th>Type</th>
    <th>Constr. No.</th>
    <th>Page</th>
  </tr>
  <tr>
    <td></td>
    <td>Name &lt;Nm&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>337</td>
  </tr>
  <tr>
    <td></td>
    <td>PostalAddress &lt;PstlAdr&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>338</td>
  </tr>
  <tr>
    <td></td>
    <td>Identification &lt;Id&gt;</td>
    <td>[0..1]</td>
    <td></td>
    <td></td>
    <td>338</td>
  </tr>
  <tr>
    <td>Or</td>
    <td>OrganisationIdentification &lt;OrgId&gt;</td>
    <td>[1..1]</td>
    <td></td>
    <td></td>
    <td>339</td>
  </tr>
  <tr>
    <td></td>
    <td>AnyBIC &lt;AnyBIC&gt;</td>
    <td>[0..1]</td>
    <td>IdentifierSet</td>
    <td>C5</td>
    <td>340</td>
  </tr>
  <tr>
    <td></td>
    <td>LEI &lt;LEI&gt;</td>
    <td>[0..1]</td>
    <td>IdentifierSet</td>
    <td></td>
    <td>340</td>
  </tr>
  <tr>
    <td></td>
    <td>Other &lt;Othr&gt;</td>
    <td>[0..*]</td>
    <td></td>
    <td></td>
    <td>340</td>
  </tr>
  <tr>
    <td></td>
    <td>Identification &lt;Id&gt;</td>
    <td>[1..1]</td>
    <td>Text</td>
    <td></td>
    <td>341</td>
  </tr>
  <tr>
    <td></td>
    <td>SchemeName &lt;SchmeNm&gt;</td>
    <td>[0..1]</td>
    <td></td>
    <td></td>
    <td>341</td>
  </tr>
  <tr>
    <td>Or</td>
    <td>Code &lt;Cd&gt;</td>
    <td>[1..1]</td>
    <td>CodeSet</td>
    <td></td>
    <td>341</td>
  </tr>
  <tr>
    <td>Or</td>
    <td>Proprietary &lt;Prtry&gt;</td>
    <td>[1..1]</td>
    <td>Text</td>
    <td></td>
    <td>341</td>
  </tr>
  <tr>
    <td></td>
    <td>Issuer &lt;Issr&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>341</td>
  </tr>
  <tr>
    <td>Or</td>
    <td>PrivateIdentification &lt;PrvtId&gt;</td>
    <td>[1..1]</td>
    <td></td>
    <td></td>
    <td>341</td>
  </tr>
  <tr>
    <td></td>
    <td>DateAndPlaceOfBirth &lt;DtAndPlcOfBrth&gt;</td>
    <td>[0..1]</td>
    <td></td>
    <td></td>
    <td>342</td>
  </tr>
  <tr>
    <td></td>
    <td>BirthDate &lt;BirthDt&gt;</td>
    <td>[1..1]</td>
    <td>Date</td>
    <td></td>
    <td>342</td>
  </tr>
  <tr>
    <td></td>
    <td>ProvinceOfBirth &lt;PvcOfBrth&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>342</td>
  </tr>
  <tr>
    <td></td>
    <td>CityOfBirth &lt;CityOfBrth&gt;</td>
    <td>[1..1]</td>
    <td>Text</td>
    <td></td>
    <td>343</td>
  </tr>
  <tr>
    <td></td>
    <td>CountryOfBirth &lt;CtryOfBrth&gt;</td>
    <td>[1..1]</td>
    <td>CodeSet</td>
    <td>C7</td>
    <td>343</td>
  </tr>
  <tr>
    <td></td>
    <td>Other &lt;Othr&gt;</td>
    <td>[0..*]</td>
    <td></td>
    <td></td>
    <td>343</td>
  </tr>
  <tr>
    <td></td>
    <td>Identification &lt;Id&gt;</td>
    <td>[1..1]</td>
    <td>Text</td>
    <td></td>
    <td>343</td>
  </tr>
  <tr>
    <td></td>
    <td>SchemeName &lt;SchmeNm&gt;</td>
    <td>[0..1]</td>
    <td></td>
    <td></td>
    <td>343</td>
  </tr>
  <tr>
    <td>Or</td>
    <td>Code &lt;Cd&gt;</td>
    <td>[1..1]</td>
    <td>CodeSet</td>
    <td></td>
    <td>344</td>
  </tr>
  <tr>
    <td>Or</td>
    <td>Proprietary &lt;Prtry&gt;</td>
    <td>[1..1]</td>
    <td>Text</td>
    <td></td>
    <td>344</td>
  </tr>
  <tr>
    <td></td>
    <td>Issuer &lt;Issr&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>344</td>
  </tr>
  <tr>
    <td></td>
    <td>CountryOfResidence &lt;CtryOfRes&gt;</td>
    <td>[0..1]</td>
    <td>CodeSet</td>
    <td>C7</td>
    <td>344</td>
  </tr>
  <tr>
    <td></td>
    <td>ContactDetails &lt;CtctDtls&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>344</td>
  </tr>
</table>

### 4.4.3.8.9.13.2 Agent <Ag>

Presence: [1..1]

Definition: Identification of a financial institution.

---

<!-- Page 228 -->

Agent <Agt> contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on page 320 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | FinancialInstitutionIdentification <FinInstlD> | [1..1] | | | 321 |
| | BICFI <BICFI> | [0..1] | IdentifierSet | C6 | 321 |
| | ClearingSystemMemberIdentification <ClrSysMmbId> | [0..1] | ± | | 322 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 322 |
| | Name <Nm> | [0..1] | Text | | 322 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 322 |
| | Other <Othr> | [0..1] | ± | | 323 |
| | BranchIdentification <BrnchId> | [0..1] | | | 324 |
| | Identification <Id> | [0..1] | Text | | 324 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 324 |
| | Name <Nm> | [0..1] | Text | | 324 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 324 |

## 4.4.3.8.9.14 DebtorAccount <DbtrAcct>

*Presence:* [0..1]

*Definition:* Unambiguous identification of the account of the debtor to which a debit entry will be made as a result of the transaction.

*Impacted by:* C16 "IdentificationOrProxyPresenceRule", C15 "IdentificationAndProxyGuideline"

**DebtorAccount <DbtrAcct>** contains the following elements (see "CashAccount40" on page 309 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Identification <Id> | [0..1] | ± | | 310 |
| | Type <Tp> | [0..1] | ± | | 310 |
| | Currency <Ccy> | [0..1] | CodeSet | C2 | 310 |
| | Name <Nm> | [0..1] | Text | | 311 |
| | Proxy <Prxy> | [0..1] | ± | | 311 |

---

<!-- Page 229 -->

Constraints

* **IdentificationAndProxyGuideline**

If the account identification is not defined through a conventional identification such as an email address or a mobile number, then the proxy element should be used for the identification of the account.

* **IdentificationOrProxyPresenceRule**

Identification must be present or Proxy must be present. Both may be present.

```
Following Must be True
/Identification Must be present
or /Proxy Must be present
```

## 4.4.3.8.9.15 DebtorAgent <DbtrAgnt>

Presence: [0..1]

Definition: Financial institution servicing an account for the debtor.

**DebtorAgent <DbtrAgnt>** contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on page 320 for details)



| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | FinancialInstitutionIdentification <FinInstId> | [1..1] | | | 321 |
| | BICFI <BICFI> | [0..1] | Identifier/Set | C6 | 321 |
| | ClearingSystemMemberIdentification <ClrSysMmbId> | [0..1] | ± | | 322 |
| | LEI <LEI> | [0..1] | Identifier/Set | | 322 |
| | Name <Nm> | [0..1] | Text | | 322 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 322 |
| | Other <Othr> | [0..1] | ± | | 323 |
| | BranchIdentification <BrnchId> | [0..1] | | | 324 |
| | Identification <Id> | [0..1] | Text | | 324 |
| | LEI <LEI> | [0..1] | Identifier/Set | | 324 |
| | Name <Nm> | [0..1] | Text | | 324 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 324 |

## 4.4.3.8.9.16 DebtorAgentAccount <DbtrAgctAcct>

Presence: [0..1]

Definition: Unambiguous identification of the account of the debtor agent at its servicing agent in the payment chain.

Impacted by: C16 "IdentificationOrProxyPresenceRule", C15 "IdentificationAndProxyGuideline"

---

<!-- Page 230 -->

DebtorAgentAccount <DbtrAgmtAcct> contains the following elements (see "CashAccount40" on page 309 for details)



| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Identification <Ids> | [0..1] | ± | | 310 |
| | Type <Tp> | [0..1] | ± | | 310 |
| | Currency <Ccy> | [0..1] | CodeSet | C2 | 310 |
| | Name <Nm> | [0..1] | Text | | 311 |
| | Proxy <Prxy> | [0..1] | ± | | 311 |

## Constraints

- **IdentificationAndProxyGuideline**

If the account identification is not defined through a conventional identification such as an email address or a mobile number, then the proxy element should be used for the identification of the account.

- **IdentificationOrProxyPresenceRule**

Identification must be present or Proxy must be present. Both may be present.

```
Following Must be True
/Identification Must be present
Or
/Proxy Must be present
```

### 4.4.3.8.9.17 CreditorAgent <CdtrAg>

*Presence:* [0..1]

*Definition:* Financial institution servicing an account for the creditor.

---

<!-- Page 231 -->

`CreditorAgent <CdrAggt>` contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on page 320 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | FinancialInstitutionIdentification <FinInstlId> | [0..1] | | | 321 |
| | BICFI <BICFI> | [0..1] | IdentifierSet | C6 | 321 |
| | ClearingSystemMemberIdentification <ClrSysMmbId> | [0..1] | ± | | 322 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 322 |
| | Name <Nm> | [0..1] | Text | | 322 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 322 |
| | Other <Othr> | [0..1] | ± | | 323 |
| | BranchIdentification <BrnchId> | [0..1] | | | 324 |
| | Identification <Id> | [0..1] | Text | | 324 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 324 |
| | Name <Nm> | [0..1] | Text | | 324 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 324 |

### 4.4.3.8.9.18 CreditorAgentAccount <CdrAggtAcct>

Presence: [0..1]

Definition: Unambiguous identification of the account of the creditor agent at its servicing agent to which a credit entry will be made as a result of the payment transaction.

Impacted by: C16 "IdentificationOrProxyPresenceRule", C15 "IdentificationAndProxyGuideline"

`CreditorAgentAccount <CdrAggtAcct>` contains the following elements (see "CashAccount40" on page 309 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Identification <Id> | [0..1] | ± | | 310 |
| | Type <Tp> | [0..1] | ± | | 310 |
| | Currency <Ccy> | [0..1] | CodeSet | C2 | 310 |
| | Name <Nm> | [0..1] | Text | | 311 |
| | Proxy <Prxy> | [0..1] | ± | | 311 |

---

<!-- Page 232 -->

Constraints

- **IdentificationAndProxyGuideline**

  If the account identification is not defined through a conventional identification such as an email address or a mobile number, then the proxy element should be used for the identification of the account.

- **IdentificationOrProxyPresenceRule**

  Identification must be present or Proxy must be present. Both may be present.

  ```
  Following Must be True
  /Identification Must be present
  Or      /Proxy Must be present
  ```

**4.4.3.8.9.19 Creditor <Cdt>**

*Presence:* [0..1]

*Definition:* Party to which an amount of money is due.

**Creditor <Cdt>** contains one of the following **Party50Choice** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| (Or | **Party** <Pty> | [1..1] | ± | | 232 |
| Or) | **Agent** <Agt> | [1..1] | ± | | 233 |

**4.4.3.8.9.19.1 Party <Pty>**

*Presence:* [1..1]

*Definition:* Identification of a person or an organisation.

---

<!-- Page 233 -->

Party <Pty> contains the following elements (see "PartyIdentification27" on page 336 for details)



<table>
  <tr>
    <th>Or</th>
    <th>MessageElement&lt;XML Tag&gt;</th>
    <th>Mult.</th>
    <th>Type</th>
    <th>Constr. No.</th>
    <th>Page</th>
  </tr>
  <tr>
    <td></td>
    <td>Name &lt;Nm&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>337</td>
  </tr>
  <tr>
    <td></td>
    <td>PostalAddress &lt;PstlAdr&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>338</td>
  </tr>
  <tr>
    <td></td>
    <td>Identification &lt;Id&gt;</td>
    <td>[0..1]</td>
    <td></td>
    <td></td>
    <td>338</td>
  </tr>
  <tr>
    <td>Or</td>
    <td>OrganisationIdentification &lt;OrgId&gt;</td>
    <td>[1..1]</td>
    <td></td>
    <td></td>
    <td>339</td>
  </tr>
  <tr>
    <td></td>
    <td>AnyBIC &lt;AnyBIC&gt;</td>
    <td>[0..1]</td>
    <td>IdentifierSet</td>
    <td>C5</td>
    <td>340</td>
  </tr>
  <tr>
    <td></td>
    <td>LEI &lt;LEI&gt;</td>
    <td>[0..1]</td>
    <td>IdentifierSet</td>
    <td></td>
    <td>340</td>
  </tr>
  <tr>
    <td></td>
    <td>Other &lt;Othr&gt;</td>
    <td>[0..*]</td>
    <td></td>
    <td></td>
    <td>340</td>
  </tr>
  <tr>
    <td></td>
    <td>Identification &lt;Id&gt;</td>
    <td>[1..1]</td>
    <td>Text</td>
    <td></td>
    <td>341</td>
  </tr>
  <tr>
    <td></td>
    <td>SchemeName &lt;SchmeNm&gt;</td>
    <td>[0..1]</td>
    <td></td>
    <td></td>
    <td>341</td>
  </tr>
  <tr>
    <td>Or</td>
    <td>Code &lt;Cd&gt;</td>
    <td>[1..1]</td>
    <td>CodeSet</td>
    <td></td>
    <td>341</td>
  </tr>
  <tr>
    <td>Or</td>
    <td>Proprietary &lt;Prtry&gt;</td>
    <td>[1..1]</td>
    <td>Text</td>
    <td></td>
    <td>341</td>
  </tr>
  <tr>
    <td></td>
    <td>Issuer &lt;Issr&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>341</td>
  </tr>
  <tr>
    <td>Or</td>
    <td>PrivateIdentification &lt;PrvtId&gt;</td>
    <td>[1..1]</td>
    <td></td>
    <td></td>
    <td>341</td>
  </tr>
  <tr>
    <td></td>
    <td>DateAndPlaceOfBirth &lt;DtAndPlcOfBrth&gt;</td>
    <td>[0..1]</td>
    <td></td>
    <td></td>
    <td>342</td>
  </tr>
  <tr>
    <td></td>
    <td>BirthDate &lt;BirthDt&gt;</td>
    <td>[1..1]</td>
    <td>Date</td>
    <td></td>
    <td>342</td>
  </tr>
  <tr>
    <td></td>
    <td>ProvinceOfBirth &lt;PvcOfBrth&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>342</td>
  </tr>
  <tr>
    <td></td>
    <td>CityOfBirth &lt;CityOfBrth&gt;</td>
    <td>[1..1]</td>
    <td>Text</td>
    <td></td>
    <td>343</td>
  </tr>
  <tr>
    <td></td>
    <td>CountryOfBirth &lt;CtryOfBrth&gt;</td>
    <td>[1..1]</td>
    <td>CodeSet</td>
    <td>C7</td>
    <td>343</td>
  </tr>
  <tr>
    <td></td>
    <td>Other &lt;Othr&gt;</td>
    <td>[0..*]</td>
    <td></td>
    <td></td>
    <td>343</td>
  </tr>
  <tr>
    <td></td>
    <td>Identification &lt;Id&gt;</td>
    <td>[1..1]</td>
    <td>Text</td>
    <td></td>
    <td>343</td>
  </tr>
  <tr>
    <td></td>
    <td>SchemeName &lt;SchmeNm&gt;</td>
    <td>[0..1]</td>
    <td></td>
    <td></td>
    <td>343</td>
  </tr>
  <tr>
    <td>Or</td>
    <td>Code &lt;Cd&gt;</td>
    <td>[1..1]</td>
    <td>CodeSet</td>
    <td></td>
    <td>344</td>
  </tr>
  <tr>
    <td>Or</td>
    <td>Proprietary &lt;Prtry&gt;</td>
    <td>[1..1]</td>
    <td>Text</td>
    <td></td>
    <td>344</td>
  </tr>
  <tr>
    <td></td>
    <td>Issuer &lt;Issr&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>344</td>
  </tr>
  <tr>
    <td></td>
    <td>CountryOfResidence &lt;CtryOfRes&gt;</td>
    <td>[0..1]</td>
    <td>CodeSet</td>
    <td>C7</td>
    <td>344</td>
  </tr>
  <tr>
    <td></td>
    <td>ContactDetails &lt;CtctDtls&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>344</td>
  </tr>
</table>

### 4.4.3.8.9.19.2 Agent <Ag>

*Presence:* [1..1]

*Definition:* Identification of a financial institution.

---

<!-- Page 234 -->

Agent <Agt> contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on page 320 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | FinancialInstitutionIdentification <FinInstlD> | [1..1] |  |  | 321 |
| | BICFI <BICFI> | [0..1] | IdentifierSet | C6 | 321 |
| | ClearingSystemMemberIdentification <ClrSysMmbId> | [0..1] | ± |  | 322 |
| | LEI <LEI> | [0..1] | IdentifierSet |  | 322 |
| | Name <Nm> | [0..1] | Text |  | 322 |
| | PostalAddress <PstlAdr> | [0..1] | ± |  | 322 |
| | Other <Othr> | [0..1] | ± |  | 323 |
| | BranchIdentification <BrnchId> | [0..1] |  |  | 324 |
| | Identification <Id> | [0..1] | Text |  | 324 |
| | LEI <LEI> | [0..1] | IdentifierSet |  | 324 |
| | Name <Nm> | [0..1] | Text |  | 324 |
| | PostalAddress <PstlAdr> | [0..1] | ± |  | 324 |

### 4.4.3.8.9.20 CreditorAccount <CdtrAcct>

*Presence:* [0..1]

*Definition:* Unambiguous identification of the account of the creditor to which a credit entry will be posted as a result of the payment transaction.

*Impacted by:* C16 "IdentificationOrProxyPresenceRule", C15 "IdentificationAndProxyGuideline"

CreditorAccount <CdtrAcct> contains the following elements (see "CashAccount40" on page 309 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Identification <Id> | [0..1] | ± |  | 310 |
| | Type <Tp> | [0..1] | ± |  | 310 |
| | Currency <Ccy> | [0..1] | CodeSet | C2 | 310 |
| | Name <Nm> | [0..1] | Text |  | 311 |
| | Proxy <Prxy> | [0..1] | ± |  | 311 |

---

<!-- Page 235 -->

Constraints

* **IdentificationAndProxyGuideline**

If the account identification is not defined through a conventional identification such as an email address or a mobile number, then the proxy element should be used for the identification of the account.

* **IdentificationOrProxyPresenceRule**

Identification must be present or Proxy must be present. Both may be present.

```
Following Must be True
/Identification Must be present
Or    /Proxy Must be present
```

**4.4.3.8.9.21 UltimateCreditor <UltmtCdtor>**

*Presence:* [0..1]

*Definition:* Ultimate party to which an amount of money is due.

**UltimateCreditor <UltmtCdtor>** contains one of the following **Party50Choice** elements



<table>
  <tr>
    <th>Or</th>
    <th>MessageElement&lt;XML Tag&gt;</th>
    <th>Mult.</th>
    <th>Type</th>
    <th>Constr. No.</th>
    <th>Page</th>
  </tr>
  <tr>
    <td>(Or)</td>
    <td><b>Party</b> &lt;Pty&gt;</td>
    <td>[1..1]</td>
    <td>±</td>
    <td></td>
    <td>235</td>
  </tr>
  <tr>
    <td>Or)</td>
    <td><b>Agent</b> &lt;Agt&gt;</td>
    <td>[1..1]</td>
    <td>±</td>
    <td></td>
    <td>236</td>
  </tr>
</table>

**4.4.3.8.9.21.1 Party <Pty>**

*Presence:* [1..1]

*Definition:* Identification of a person or an organisation.

---

<!-- Page 236 -->

Party <Pty> contains the following elements (see "PartyIdentification27" on page 336 for details)



<table>
  <thead>
    <tr>
      <th>Or</th>
      <th>MessageElement&lt;XML Tag&gt;</th>
      <th>Mult.</th>
      <th>Type</th>
      <th>Constr. No.</th>
      <th>Page</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td>Name &lt;Nm&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>337</td>
    </tr>
    <tr>
      <td></td>
      <td>PostalAddress &lt;PstlAdr&gt;</td>
      <td>[0..1]</td>
      <td>±</td>
      <td></td>
      <td>338</td>
    </tr>
    <tr>
      <td></td>
      <td>Identification &lt;Id&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>338</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>OrganisationIdentification &lt;OrgId&gt;</td>
      <td>[1..1]</td>
      <td></td>
      <td></td>
      <td>339</td>
    </tr>
    <tr>
      <td></td>
      <td>AnyBIC &lt;AnyBIC&gt;</td>
      <td>[0..1]</td>
      <td>IdentifierSet</td>
      <td>C5</td>
      <td>340</td>
    </tr>
    <tr>
      <td></td>
      <td>LEI &lt;LEI&gt;</td>
      <td>[0..1]</td>
      <td>IdentifierSet</td>
      <td></td>
      <td>340</td>
    </tr>
    <tr>
      <td></td>
      <td>Other &lt;Othr&gt;</td>
      <td>[0..*]</td>
      <td></td>
      <td></td>
      <td>340</td>
    </tr>
    <tr>
      <td></td>
      <td>Identification &lt;Id&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td></td>
      <td>SchemeName &lt;SchmeNm&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Code &lt;Cd&gt;</td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Proprietary &lt;Prtry&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td></td>
      <td>Issuer &lt;Issr&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>PrivateIdentification &lt;PrvtId&gt;</td>
      <td>[1..1]</td>
      <td></td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td></td>
      <td>DateAndPlaceOfBirth &lt;DtAndPlcOfBrth&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>342</td>
    </tr>
    <tr>
      <td></td>
      <td>BirthDate &lt;BirthDt&gt;</td>
      <td>[1..1]</td>
      <td>Date</td>
      <td></td>
      <td>342</td>
    </tr>
    <tr>
      <td></td>
      <td>ProvinceOfBirth &lt;PvcOfBrth&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>342</td>
    </tr>
    <tr>
      <td></td>
      <td>CityOfBirth &lt;CityOfBrth&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>CountryOfBirth &lt;CtryOfBrth&gt;</td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td>C7</td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>Other &lt;Othr&gt;</td>
      <td>[0..*]</td>
      <td></td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>Identification &lt;Id&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>SchemeName &lt;SchmeNm&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Code &lt;Cd&gt;</td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td></td>
      <td>344</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Proprietary &lt;Prtry&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>344</td>
    </tr>
    <tr>
      <td></td>
      <td>Issuer &lt;Issr&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>344</td>
    </tr>
    <tr>
      <td></td>
      <td>CountryOfResidence &lt;CtryOfRes&gt;</td>
      <td>[0..1]</td>
      <td>CodeSet</td>
      <td>C7</td>
      <td>344</td>
    </tr>
    <tr>
      <td></td>
      <td>ContactDetails &lt;CtctDtls&gt;</td>
      <td>[0..1]</td>
      <td>±</td>
      <td></td>
      <td>344</td>
    </tr>
  </tbody>
</table>

### 4.4.3.8.9.21.2 Agent <Ag>

*Presence:* [1..1]

*Definition:* Identification of a financial institution.

---

<!-- Page 237 -->

Agent <Agt> contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on page 320 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | FinancialInstitutionIdentification <FinInstnId> | [1..1] | | | 321 |
| | BICFI <BICFI> | [0..1] | IdentifierSet | C6 | 321 |
| | ClearingSystemMemberIdentification <ClrSysMmbId> | [0..1] | ± | | 322 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 322 |
| | Name <Nm> | [0..1] | Text | | 322 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 322 |
| | Other <Othr> | [0..1] | ± | | 323 |
| | BranchIdentification <BrnchId> | [0..1] | | | 324 |
| | Identification <Id> | [0..1] | Text | | 324 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 324 |
| | Name <Nm> | [0..1] | Text | | 324 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 324 |

## 4.4.3.8.9.22 Purpose <Purp>

*Presence:* [0..1]

*Definition:* Underlying reason for the payment transaction.

Usage:

Purpose is used by the end customers, that is initiating party, (ultimate) debtor, (ultimate) creditor to provide information concerning the nature of the payment. Purpose is a content element, which is not used for processing by any of the agents involved in the payment chain.

Purpose <Purp> contains one of the following elements (see "Purpose2Choice" on page 334 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| (Or | Code <Cd> | [1..1] | CodeSet | | 335 |
| (Or) | Proprietary <Prtry> | [1..1] | Text | | 335 |

## 4.4.3.8.10 Supplementary Data <SplmtryData>

*Presence:* [0..*]

*Definition:* Additional information that cannot be captured in the structured elements and/or any other specific block.

*Impacted by:* C28 "SupplementaryDataRule"

---

<!-- Page 238 -->

**SupplementaryData** *<SplmtryData>* contains the following elements (see "SupplementaryData1" on page 334 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | PlaceAndName *<PlcAndNm>* | [0..1] | Text | | 334 |
| | Envelope *<Envlp>* | [1..1] | (External Schema) | | 334 |

## Constraints

- **SupplementaryDataRule**

This component may not be used without the explicit approval of a SEG and submission to the RA of ISO 20022 compliant structure(s) to be used in the Envelope element.

# 4.4.4 SupplementaryData *<SplmtryData>*

*Presence:* [0..*]

*Definition:* Additional information that cannot be captured in the structured elements and/or any other specific block.

*Impacted by:* C28 "SupplementaryDataRule"

**SupplementaryData** *<SplmtryData>* contains the following elements (see "SupplementaryData1" on page 334 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | PlaceAndName *<PlcAndNm>* | [0..1] | Text | | 334 |
| | Envelope *<Envlp>* | [1..1] | (External Schema) | | 334 |

## Constraints

- **SupplementaryDataRule**

This component may not be used without the explicit approval of a SEG and submission to the RA of ISO 20022 compliant structure(s) to be used in the Envelope element.

---

<!-- Page 239 -->

# 5 pain.008.001.11 CustomerDirectDebitInitiationV11

## 5.1 MessageDefinition Functionality

Scope

The CustomerDirectDebitInitiation message is sent by the initiating party to the forwarding agent or creditor agent. It is used to request single or bulk collection(s) of funds from one or various debtor's account(s) for a creditor.

Usage

The CustomerDirectDebitInitiation message can contain one or more direct debit instructions.

The message can be used in a direct or a relay scenario:

- In a direct scenario, the message is sent directly to the creditor agent. The creditor agent is the account servicer of the creditor.

- In a relay scenario, the message is sent to a forwarding agent. The forwarding agent acts as a concentrating financial institution. It will forward the CustomerDirectDebitInitiation message to the creditor agent.

The message can also be used by an initiating party that has authority to send the message on behalf of the creditor. This caters for example for the scenario of a payments factory initiating all payments on behalf of a large corporate.

The CustomerDirectDebitInitiation message can be used in domestic and cross-border scenarios.

The CustomerDirectDebitInitiation may or may not contain mandate related information, i.e. extracts from a mandate, such as MandateIdentification or DateOfSignature. The CustomerDirectDebitInitiation message must not be considered as a mandate.

The CustomerDirectDebitInitiation message must not be used by the creditor agent to execute the direct debit instruction(s). The FIToFICustomerDirectDebit message must be used instead.

Outline

The CustomerDirectDebitInitiationV11 MessageDefinition is composed of 3 MessageBuildingBlocks:

A. GroupHeader

Set of characteristics shared by all individual transactions included in the message.

B. PaymentInformation

Set of characteristics that apply to the credit side of the payment transactions included in the direct debit transaction initiation.

C. SupplementaryData

Additional information that cannot be captured in the structured elements and/or any other specific block.

---

<!-- Page 240 -->

## 5.2 Structure



<table>
  <thead>
    <tr>
      <th>Or</th>
      <th>MessageElement/BuildingBlock &lt;XML Tag&gt;</th>
      <th>Mult.</th>
      <th>Type</th>
      <th>Constr. No.</th>
      <th>Page</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td><i>Message root &lt;Document&gt; &lt;CstmrDrctDbtInitn&gt;</i></td>
      <td>[1..1]</td>
      <td></td>
      <td>C17</td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td><b>GroupHeader</b> <i>&lt;GrpHdr&gt;</i></td>
      <td>[1..1]</td>
      <td></td>
      <td></td>
      <td>246</td>
    </tr>
    <tr>
      <td></td>
      <td><b>MessageIdentification</b> <i>&lt;MsgId&gt;</i></td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>246</td>
    </tr>
    <tr>
      <td></td>
      <td><b>CreationDateTime</b> <i>&lt;CreDtTm&gt;</i></td>
      <td>[1..1]</td>
      <td>DateTime</td>
      <td></td>
      <td>247</td>
    </tr>
    <tr>
      <td></td>
      <td><b>Authorisation</b> <i>&lt;AuthStrn&gt;</i></td>
      <td>[0..2]</td>
      <td>±</td>
      <td></td>
      <td>247</td>
    </tr>
    <tr>
      <td></td>
      <td><b>NumberOfTransactions</b> <i>&lt;NbOfTxs&gt;</i></td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>247</td>
    </tr>
    <tr>
      <td></td>
      <td><b>ControlSum</b> <i>&lt;CtrlSum&gt;</i></td>
      <td>[0..1]</td>
      <td>Quantity</td>
      <td></td>
      <td>247</td>
    </tr>
    <tr>
      <td></td>
      <td><b>InitiatingParty</b> <i>&lt;InitgPty&gt;</i></td>
      <td>[1..1]</td>
      <td>±</td>
      <td></td>
      <td>247</td>
    </tr>
    <tr>
      <td></td>
      <td><b>ForwardingAgent</b> <i>&lt;FwdgAgt&gt;</i></td>
      <td>[0..1]</td>
      <td>±</td>
      <td></td>
      <td>248</td>
    </tr>
    <tr>
      <td></td>
      <td><b>PaymentInformation</b> <i>&lt;PmtInf&gt;</i></td>
      <td>[1..*]</td>
      <td></td>
      <td>C6, C7, C8, C10, C15, C21, C19</td>
      <td>249</td>
    </tr>
    <tr>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
      <td></td>
    </tr>
    <tr>
      <td></td>
      <td><b>PaymentInformationIdentification</b> <i>&lt;PmtInfId&gt;</i></td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>254</td>
    </tr>
    <tr>
      <td></td>
      <td><b>PaymentMethod</b> <i>&lt;PmtMtd&gt;</i></td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td></td>
      <td>255</td>
    </tr>
    <tr>
      <td></td>
      <td><b>RequestedAdviceType</b> <i>&lt;ReqdAdvcTp&gt;</i></td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>255</td>
    </tr>
    <tr>
      <td></td>
      <td><b>CreditAdvice</b> <i>&lt;CdtAdvc&gt;</i></td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>255</td>
    </tr>
    <tr>
      <td>Or</td>
      <td><b>Code</b> <i>&lt;Cd&gt;</i></td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td></td>
      <td>255</td>
    </tr>
    <tr>
      <td>Or)</td>
      <td><b>Proprietary</b> <i>&lt;Pry&gt;</i></td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>256</td>
    </tr>
    <tr>
      <td></td>
      <td><b>DebitAdvice</b> <i>&lt;DbtAdvc&gt;</i></td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>256</td>
    </tr>
    <tr>
      <td>Or</td>
      <td><b>Code</b> <i>&lt;Cd&gt;</i></td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td></td>
      <td>256</td>
    </tr>
    <tr>
      <td>Or)</td>
      <td><b>Proprietary</b> <i>&lt;Pry&gt;</i></td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>256</td>
    </tr>
    <tr>
      <td></td>
      <td><b>BatchBooking</b> <i>&lt;BtchBookg&gt;</i></td>
      <td>[0..1]</td>
      <td>Indicator</td>
      <td></td>
      <td>256</td>
    </tr>
    <tr>
      <td></td>
      <td><b>NumberOfTransactions</b> <i>&lt;NbOfTxs&gt;</i></td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>257</td>
    </tr>
    <tr>
      <td></td>
      <td><b>ControlSum</b> <i>&lt;CtrlSum&gt;</i></td>
      <td>[0..1]</td>
      <td>Quantity</td>
      <td></td>
      <td>257</td>
    </tr>
    <tr>
      <td></td>
      <td><b>PaymentTypeInformation</b> <i>&lt;PmtTpInf&gt;</i></td>
      <td>[0..1]</td>
      <td>±</td>
      <td></td>
      <td>257</td>
    </tr>
    <tr>
      <td></td>
      <td><b>RequestedCollectionDate</b> <i>&lt;ReqdColltnDt&gt;</i></td>
      <td>[1..1]</td>
      <td>Date</td>
      <td></td>
      <td>257</td>
    </tr>
    <tr>
      <td></td>
      <td><b>Creditor</b> <i>&lt;Cdtr&gt;</i></td>
      <td>[1..1]</td>
      <td>±</td>
      <td></td>
      <td>258</td>
    </tr>
    <tr>
      <td></td>
      <td><b>CreditorAccount</b> <i>&lt;CdtrAcct&gt;</i></td>
      <td>[1..1]</td>
      <td>±</td>
      <td>C14, C13</td>
      <td>259</td>
    </tr>
    <tr>
      <td></td>
      <td><b>CreditorAgent</b> <i>&lt;CdtrAgt&gt;</i></td>
      <td>[1..1]</td>
      <td>±</td>
      <td></td>
      <td>259</td>
    </tr>
  </tbody>
</table>

---

<!-- Page 241 -->

| Or | MessageElement/BuildingBlock <XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **CreditorAgentAccount** `<CdtrAggtAcct>` | [0..1] | ± | C14, C13 | 260 |
| | **UltimateCreditor** `<UltmtCdr>` | [0..1] | ± | | 261 |
| | **ChargeBearer** `<ChrgBr>` | [0..1] | CodeSet | | 262 |
| | **ChargesAccount** `<ChrgsAcct>` | [0..1] | ± | C14, C13 | 263 |
| | **ChargesAccountAgent** `<ChrgsAcctAgtr>` | [0..1] | ± | | 264 |
| | **CreditorSchemeIdentification** `<CdtrSchemId>` | [0..1] | ± | | 264 |
| | **DirectDebitTransactionInformation** `<DrctDbtTxInf>` | [1..*] | | C20, C22 | 265 |
| | **PaymentIdentification** `<PmtId>` | [1..1] | ± | | 269 |
| | **PaymentTypeInformation** `<PmtTpInf>` | [1..1] | ± | | 269 |
| | **InstructedAmount** `<InstdAmt>` | [1..1] | Amount | C1, C11 | 269 |
| | **ChargeBearer** `<ChrgBr>` | [0..1] | CodeSet | | 270 |
| | **DirectDebitTransaction** `<DrctDbtTx>` | [0..1] | | | 270 |
| | **MandateRelatedInformation** `<MndtRltdInf>` | [0..1] | | C2, C3 | 272 |
| | **MandateIdentification** `<MndtId>` | [0..1] | Text | | 274 |
| | **DateOfSignature** `<DtOfSgntr>` | [0..1] | Date | | 274 |
| | **AmendmentIndicator** `<AmdmntInd>` | [0..1] | Indicator | | 274 |
| | **AmendmentInformationDetails** `<AmdmntInfDtls>` | [0..1] | | | 274 |
| | **OriginalMandateIdentification** `<OrgnlMndtId>` | [0..1] | Text | | 275 |
| | **OriginalCreditorSchemeIdentification** `<OrgnlCdtrSchemId>` | [0..1] | ± | | 275 |
| | **OriginalCreditorAgent** `<OrgnlCdtrAgtr>` | [0..1] | ± | | 276 |
| | **OriginalCreditorAgentAccount** `<OrgnlCdtrAggtAcct>` | [0..1] | ± | C14, C13 | 277 |
| | **OriginalDebtor** `<OrgnlDbtr>` | [0..1] | ± | | 278 |
| | **OriginalDebtorAccount** `<OrgnlDbtrAcct>` | [0..1] | ± | C14, C13 | 279 |
| | **OriginalDebtorAgent** `<OrgnlDbtrAgtr>` | [0..1] | ± | | 280 |
| | **OriginalDebtorAgentAccount** `<OrgnlDbtrAggtAcct>` | [0..1] | ± | C14, C13 | 281 |
| | **OriginalFinalCollectionDate** `<OrgnlFnclCollnDt>` | [0..1] | Date | | 282 |
| | **OriginalFrequency** `<OrgnlFrcq>` | [0..1] | ± | | 282 |
| | **OriginalReason** `<OrgnlRsn>` | [0..1] | | | 282 |
| Or | **Code** `<Cd>` | [1..1] | CodeSet | | 282 |

---

<!-- Page 242 -->

| Or | MessageElement/BuildingBlock <XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| Or | **Proprietary** <Ptry> | [1..1] | Text |  | 282 |
|  | **OriginalTrackingDays** <OrgnlTrckgDays> | [0..1] | Text |  | 283 |
|  | **ElectronicSignature** <ElctrncSgntr> | [0..1] | Text |  | 283 |
|  | **FirstCollectionDate** <FirstColltnDt> | [0..1] | Date |  | 283 |
|  | **FinalCollectionDate** <FinlColltnDt> | [0..1] | Date |  | 283 |
|  | **Frequency** <Frqcy> | [0..1] | ± |  | 283 |
|  | **Reason** <Rsn> | [0..1] |  |  | 283 |
| [Or | **Code** <Cd> | [1..1] | CodeSet |  | 284 |
| Or] | **Proprietary** <Ptry> | [1..1] | Text |  | 284 |
|  | **TrackingDays** <TrckgDays> | [0..1] | Text |  | 284 |
|  | **CreditorSchemeIdentification** <CdtrSchemId> | [0..1] | ± |  | 284 |
|  | **PreNotificationIdentification** <PrfNtfctnId> | [0..1] | Text |  | 285 |
|  | **PreNotificationDate** <PrfNtfctnDt> | [0..1] | Date |  | 286 |
|  | **UltimateCreditor** <UltmtCdtr> | [0..1] | ± |  | 286 |
|  | **DebtorAgent** <DbtrAgnt> | [1..1] | ± |  | 287 |
|  | **DebtorAgentAccount** <DbtrAgntAcct> | [0..1] | ± | C14, C13 | 288 |
|  | **Debtor** <Dbtr> | [1..1] | ± |  | 289 |
|  | **DebtorAccount** <DbtrAcct> | [1..1] | ± | C14, C13 | 290 |
|  | **UltimateDebtor** <UltmtDbtr> | [0..1] | ± |  | 291 |
|  | **InstructionForCreditorAgent** <InstrForCdtrAgnt> | [0..1] | Text |  | 292 |
|  | **Purpose** <Purp> | [0..1] | ± |  | 293 |
|  | **RegulatoryReporting** <RgltryRptg> | [0..10] | ± |  | 293 |
|  | **Tax** <Tax> | [0..1] |  |  | 293 |
|  | **Creditor** <Cdtr> | [0..1] | ± |  | 295 |
|  | **Debtor** <Dbtr> | [0..1] | ± |  | 295 |
|  | **UltimateDebtor** <UltmtDbtr> | [0..1] | ± |  | 295 |
|  | **AdministrationZone** <AdminZone> | [0..1] | Text |  | 296 |
|  | **ReferenceNumber** <RefNb> | [0..1] | Text |  | 296 |
|  | **Method** <Mtd> | [0..1] | Text |  | 296 |
|  | **TotalTaxableBaseAmount** <TotTaxblBaseAmt> | [0..1] | Amount | C1, C11 | 296 |
|  | **TotalTaxAmount** <TotTaxAmt> | [0..1] | Amount | C1, C11 | 297 |

---

<!-- Page 243 -->

| Or | MessageElement/BuildingBlock/<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **Date** *<Dt>* | [0..1] | Date |  | 297 |
| | **SequenceNumber** *<SeqNb>* | [0..1] | Quantity |  | 297 |
| | **Record** *<Rcrd>* | [0..*] |  |  | 297 |
| | **Type** *<Tp>* | [0..1] | Text |  | 298 |
| | **Category** *<Ctgy>* | [0..1] | Text |  | 298 |
| | **CategoryDetails** *<CtgyDtls>* | [0..1] | Text |  | 298 |
| | **DebtorStatus** *<DbtrSts>* | [0..1] | Text |  | 299 |
| | **CertificateIdentification** *<CertId>* | [0..1] | Text |  | 299 |
| | **FormsCode** *<FrmsCd>* | [0..1] | Text |  | 299 |
| | **Period** *<Prd>* | [0..1] |  |  | 299 |
| | **Year** *<Yr>* | [0..1] | Year |  | 299 |
| | **Type** *<Tp>* | [0..1] | CodeSet |  | 299 |
| | **FromToDate** *<FrToDt>* | [0..1] | ± |  | 300 |
| | **TaxAmount** *<TaxAmt>* | [0..1] |  |  | 301 |
| | **Rate** *<Rate>* | [0..1] | Rate |  | 301 |
| | **TaxableBaseAmount** *<TaxblBaseAmt>* | [0..1] | Amount | C1, C11 | 301 |
| | **TotalAmount** *<TtlAmt>* | [0..1] | Amount | C1, C11 | 301 |
| | **Details** *<Dtls>* | [0..*] |  |  | 302 |
| | **Period** *<Prd>* | [0..1] |  |  | 302 |
| | **Year** *<Yr>* | [0..1] | Year |  | 302 |
| | **Type** *<Tp>* | [0..1] | CodeSet |  | 303 |
| | **FromToDate** *<FrToDt>* | [0..1] | ± |  | 303 |
| | **Amount** *<Amt>* | [1..1] | Amount | C1, C11 | 304 |
| | **AdditionalInformation** *<AddtlInf>* | [0..1] | Text |  | 304 |
| | **RelatedRemittanceInformation** *<RltdRmInf>* | [0..10] |  |  | 304 |
| | **RemittanceIdentification** *<RmtdId>* | [0..1] | Text |  | 305 |
| | **RemittanceLocationDetails** *<RmLtctnDtls>* | [0..*] |  |  | 305 |
| | **Method** *<Mtd>* | [1..1] | CodeSet |  | 305 |
| | **ElectronicAddress** *<ElctrncAdr>* | [0..1] | Text |  | 306 |
| | **PostalAddress** *<PstlAdr>* | [0..1] |  |  | 306 |
| | **Name** *<Nm>* | [1..1] | Text |  | 306 |

---

<!-- Page 244 -->

| Or | MessageElement/BuildingBlock<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---:|:---|:---:|:---:|:---:|:---:|
| | **Address** `<Adr>` | [1..] | ± | | 306 |
| | **RemittanceInformation** `<RmtInf>` | [0..1] | ± | | 307 |
| | **SupplementaryData** `<SplmtryData>` | [0..*] | ± | C18 | 308 |
| | **SupplementaryData** `<SplmtryData>` | [0..*] | ± | C18 | 308 |

## 5.3 Constraints

**C1** **ActiveOrHistoricCurrency**

The Currency Code must be registered, or have already been registered. Valid active or historic currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and may be or not be withdrawn on the day the message containing the Currency is exchanged.

**C2** **AmendmentIndicatorFalseRule**

If AmendmentIndicator is false, then AmendmentInformationDetails is not allowed.

**C3** **AmendmentIndicatorTrueRule**

If AmendmentIndicator is true, then AmendmentInformationDetails must be present.

**C4** **AnyBIC**

Only a valid Business identifier code is allowed. Business identifier codes for financial or non-financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.

**C5** **BICFI**

Valid BICs for financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous characters.

**C6** **ChargeBearerRule**

If ChargeBearer is present, then DirectDebitTransactionInformation/ChargeBearer is not allowed.

If DirectDebitTransactionInformation/ChargeBearer is present, then ChargeBearer is not allowed.

DirectDebitTransactionInformation/ChargeBearer and ChargeBearer may both be absent.

**C7** **ChargesAccountAgentRule**

If ChargesAccountAgent is present, then it must contain a branch of the CreditorAgent. It must not contain a completely different agent.

**C8** **ChargesAccountRule**

If ChargesAccountAgent is present, then ChargesAccount must be present.

---

<!-- Page 245 -->

| C9 | **Country**<br>The code is checked against the list of country names obtained from the United Nations (ISO 3166, Alpha-2 code). |
| :--- | :--- |
| C10 | **CreditorSchemeIdentificationRule**<br>If CreditorSchemeIdentification is present, then DirectDebitTransactionInformation/CreditorSchemeIdentification is not allowed.<br><br>If DirectDebitTransactionInformation/CreditorSchemeIdentification is present, then CreditorSchemeIdentification is not allowed.<br><br>DirectDebitTransactionInformation/CreditorSchemeIdentification and CreditorSchemeIdentification may both be absent. |
| C11 | **CurrencyAmount**<br>The number of fractional digits (or minor unit of currency) must comply with ISO 4217.<br><br>Note: The decimal separator is a dot. |
| C12 | **IBAN**<br>A valid IBAN consists of all three of the following components: Country Code, check digits and BBAN. |
| C13 | **IdentificationAndProxyGuideline**<br>If the account identification is not defined through a conventional identification such as an email address or a mobile number, then the proxy element should be used for the identification of the account. |
| C14 | **IdentificationOrProxyPresenceRule**<br>Identification must be present or Proxy must be present. Both may be present. |
| C15 | **PaymentTypeInformationRule**<br>If PaymentTypeInformation is present, then DirectDebitTransactionInformation/PaymentTypeInformation is not allowed. |
| C16 | **RemittanceAmountAndTypeGuideline**<br>If Type/Code is equal to CREN, DUPA or REMI for RemittanceAmountAndType, RemittanceAmountAndType must not be repeated. |
| C17 | **SupplementaryDataRule**<br>The SupplementaryData building block at message level must not be used to provide additional information about a transaction. The SupplementaryData element at transaction level should be used for that purpose.<br><br>*This constraint is defined at the MessageDefinition level.* |
| C18 | **SupplementaryDataRule**<br>This component may not be used without the explicit approval of a SEG and submission to the RA of ISO 20022 compliant structure(s) to be used in the Envelope element. |
| C19 | **UltimateCreditorGuideline**<br>UltimateCreditor may only be present if different from Creditor. |

---

<!-- Page 246 -->

C20 **UltimateCreditorGuideline**
UltimateCreditor may only be present if different from Creditor.

C21 **UltimateCreditorRule**
If UltimateCreditor is present, then DirectDebitTransactionInformation/UltimateCreditor is not allowed.

If DirectDebitTransactionInformation/UltimateCreditor is present, then UltimateCreditor is not allowed.

DirectDebitTransactionInformation/UltimateCreditor and UltimateCreditor may both be absent.

C22 **UltimateDebtorGuideline**
UltimateDebtor may only be present if different from Debtor.

## 5.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.

## 5.4.1 GroupHeader <GrpHdr>
*Presence: [1..1]*
*Definition: Set of characteristics shared by all individual transactions included in the message.*
**GroupHeader <GrpHdr>** contains the following **GroupHeader118** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---:|:---|:---|:---|:---:|:---:|
| | **MessageIdentification** <MsgId> | [1..1] | Text | | 246 |
| | **CreationDateTime** <CreDtTm> | [1..1] | DateTime | | 247 |
| | **Authorisation** <Authstr> | [0..2] | ± | | 247 |
| | **NumberOfTransactions** <NbOfTxs> | [1..1] | Text | | 247 |
| | **ControlSum** <CtrlSum> | [0..1] | Quantity | | 247 |
| | **InitiatingParty** <InstdPty> | [1..1] | ± | | 247 |
| | **ForwardingAgent** <FwdgAgnt> | [0..1] | ± | | 248 |

### 5.4.1.1 MessageIdentification <MsgId>
*Presence: [1..1]*
*Definition: Point to point reference, assigned by the instructing party and sent to the next party in the chain, to unambiguously identify the message.*

Usage: The instructing party has to make sure that MessageIdentification is unique per instructed party for a pre-agreed period.

*Datatype: "Max35Text" on page 431*

---

<!-- Page 247 -->

### 5.4.1.2 CreationDateTime <CreDtTm>

*Presence:* [1..1]

*Definition:* Date and time at which the message was created.

*Datatype:* "ISODateTime" on page 425

### 5.4.1.3 Authorisation <Authstn>

*Presence:* [0..2]

*Definition:* User identification or any user key that allows to check if the initiating party is allowed to initiate transactions from the account specified in the initiation.

Usage: The content is not of a technical nature, but reflects the organisational structure at the initiating side. The authorisation element can typically be used in relay scenarios, payment initiations, payment returns or payment reversals that are initiated on behalf of a different party than the initiating party.

**Authorisation <Authstn>** contains one of the following elements (see "Authorisation1Choice" on page 336 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| Or | Code <Cd> | [1..1] | CodeSet |  | 336 |
| Or | Proprietary <Ptry> | [1..1] | Text |  | 336 |

### 5.4.1.4 NumberOfTransactions <NbOfTxs>

*Presence:* [1..1]

*Definition:* Number of individual transactions contained in the message.

*Datatype:* "Max15NumericText" on page 430

### 5.4.1.5 ControlSum <CtrlSum>

*Presence:* [0..1]

*Definition:* Total of all individual amounts included in the message, irrespective of currencies.

*Datatype:* "DecimalNumber" on page 427

### 5.4.1.6 InitiatingParty <InitgPty>

*Presence:* [1..1]

*Definition:* Party that initiates the payment.

Usage: This can either be the creditor or a party that initiates the direct debit on behalf of the creditor.

---

<!-- Page 248 -->

InitiatingParty <InitgPty> contains the following elements (see "PartyIdentification27" on page 336 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
| :--- | :--- | :--- | :--- | :--- | :--- |
| | Name *<Nm>* | [0..1] | Text | | 337 |
| | PostalAddress *<PstlAdr>* | [0..1] | ± | | 338 |
| | Identification *<Id>* | [0..1] | | | 338 |
| (Or | OrganisationIdentification *<OrgId>* | [1..1] | | | 339 |
| | AnyBIC *<AnyBIC>* | [0..1] | IdentifierSet | C5 | 340 |
| | LEI *<LEI>* | [0..1] | IdentifierSet | | 340 |
| | Other *<Othr>* | [0..*] | | | 340 |
| | Identification *<Id>* | [1..1] | Text | | 341 |
| | SchemeName *<SchmeNm>* | [0..1] | | | 341 |
| (Or | Code *<Cd>* | [1..1] | CodeSet | | 341 |
| Or) | Proprietary *<Prtry>* | [1..1] | Text | | 341 |
| | Issuer *<Issr>* | [0..1] | Text | | 341 |
| (Or) | PrivateIdentification *<PrvtId>* | [1..1] | | | 341 |
| | DateAndPlaceOfBirth *<DtAndPlcOfBirth>* | [0..1] | | | 342 |
| | BirthDate *<BirthDt>* | [1..1] | Date | | 342 |
| | ProvinceOfBirth *<PrvcOfBirth>* | [0..1] | Text | | 342 |
| | CityOfBirth *<CityOfBirth>* | [1..1] | Text | | 343 |
| | CountryOfBirth *<CtryOfBirth>* | [1..1] | CodeSet | C7 | 343 |
| | Other *<Othr>* | [0..*] | | | 343 |
| | Identification *<Id>* | [1..1] | Text | | 343 |
| | SchemeName *<SchmeNm>* | [0..1] | | | 343 |
| (Or) | Code *<Cd>* | [1..1] | CodeSet | | 344 |
| Or) | Proprietary *<Prtry>* | [1..1] | Text | | 344 |
| | Issuer *<Issr>* | [0..1] | Text | | 344 |
| | CountryOfResidence *<CtryOfRes>* | [0..1] | CodeSet | C7 | 344 |
| | ContactDetails *<CtctDtls>* | [0..1] | ± | | 344 |

### 5.4.1.7 ForwardingAgent <FwdgAgt>

*Presence:* [0..1]

*Definition:* Financial institution that receives the instruction from the initiating party and forwards it to the next agent in the payment chain for execution.

---

<!-- Page 249 -->

ForwardingAgent <FwdgAgt> contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on page 320 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | FinancialInstitutionIdentification <FinInstnId> | [1..1] |  |  | 321 |
| | BICFI <BICFI> | [0..1] | IdentifierSet | C6 | 321 |
| | ClearingSystemMemberIdentification <ClrSysMmbId> | [0..1] | ± |  | 322 |
| | LEI <LEI> | [0..1] | IdentifierSet |  | 322 |
| | Name <Nm> | [0..1] | Text |  | 322 |
| | PostalAddress <PstlAdr> | [0..1] | ± |  | 322 |
| | Other <Othr> | [0..1] | ± |  | 323 |
| | BranchIdentification <BrnchId> | [0..1] |  |  | 324 |
| | Identification <Id> | [0..1] | Text |  | 324 |
| | LEI <LEI> | [0..1] | IdentifierSet |  | 324 |
| | Name <Nm> | [0..1] | Text |  | 324 |
| | PostalAddress <PstlAdr> | [0..1] | ± |  | 324 |

## 5.4.2 PaymentInformation <PmtInf>

Presence: [1..*]

Definition: Set of characteristics that apply to the credit side of the payment transactions included in the direct debit transaction initiation.

Impacted by: C6 "ChargeBearerRule", C7 "ChargesAccountAgentRule", C8 "ChargesAccountRule", C10 "CreditorSchemeIdentificationRule", C15 "PaymentTypeInformationRule", C21 "UltimateCreditorRule", C19 "UltimateCreditorGuideline"

---

<!-- Page 250 -->

PaymentInformation `<PmtInf>` contains the following PaymentInstruction45 elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **PaymentInformationIdentification** `<PmtId>` | [1..1] | Text | | 254 |
| | **PaymentMethod** `<PmtMtd>` | [1..1] | CodeSet | | 255 |
| | **RequestedAdviceType** `<ReqdAdvTp>` | [0..1] | | | 255 |
| | **CreditAdvice** `<CdtAdvc>` | [0..1] | | | 255 |
| Or | **Code** `<Cd>` | [1..1] | CodeSet | | 255 |
| Or | **Proprietary** `<Ptry>` | [1..1] | Text | | 256 |
| | **DebitAdvice** `<DbtAdvc>` | [0..1] | | | 256 |
| Or | **Code** `<Cd>` | [1..1] | CodeSet | | 256 |
| Or | **Proprietary** `<Ptry>` | [1..1] | Text | | 256 |
| | **BatchBooking** `<BtchBkng>` | [0..1] | Indicator | | 256 |
| | **NumberOfTransactions** `<NbOfTxs>` | [0..1] | Text | | 257 |
| | **ControlSum** `<CtrlSum>` | [0..1] | Quantity | | 257 |
| | **PaymentTypeInformation** `<PmtTpInf>` | [0..1] | ± | | 257 |
| | **RequestedCollectionDate** `<ReqdCollnDt>` | [1..1] | Date | | 257 |
| | **Creditor** `<Cdtr>` | [1..1] | ± | | 258 |
| | **CreditorAccount** `<CdtrAcct>` | [1..1] | ± | C14, C13 | 259 |
| | **CreditorAgent** `<CdtrAgt>` | [1..1] | ± | | 259 |
| | **CreditorAgentAccount** `<CdtrAgtAcct>` | [0..1] | ± | C14, C13 | 260 |
| | **UltimateCreditor** `<UltmCdtr>` | [0..1] | ± | | 261 |
| | **ChargeBearer** `<ChrgBr>` | [0..1] | CodeSet | | 262 |
| | **ChargesAccount** `<ChrgsAcct>` | [0..1] | ± | C14, C13 | 263 |
| | **ChargesAccountAgent** `<ChrgsAcctAgt>` | [0..1] | ± | | 264 |
| | **CreditorSchemeIdentification** `<CdtrSchmeId>` | [0..1] | ± | | 264 |
| | **DirectDebitTransactionInformation** `<DrctDbtTxInf>` | [1..*] | | C20, C22 | 265 |
| | **PaymentIdentification** `<PmtId>` | [1..1] | ± | | 269 |
| | **PaymentTypeInformation** `<PmtTpInf>` | [0..1] | ± | | 269 |
| | **InstructedAmount** `<InstdAmt>` | [1..1] | Amount | C1, C11 | 269 |
| | **ChargeBearer** `<ChrgBr>` | [0..1] | CodeSet | | 270 |
| | **DirectDebitTransaction** `<DrctDbtTx>` | [0..1] | | | 270 |

---

<!-- Page 251 -->

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **MandateRelatedInformation** <i><MndtRltdInf></i> | [0..1] | | C2, C3 | 272 |
| | **MandateIdentification** <i><MndtId></i> | [0..1] | Text | | 274 |
| | **DateOfSignature** <i><DtOfSgntr></i> | [0..1] | Date | | 274 |
| | **AmendmentIndicator** <i><AmdmntInd></i> | [0..1] | Indicator | | 274 |
| | **AmendmentInformationDetails** <i><AmdmntInfDtls></i> | [0..1] | | | 274 |
| | **OriginalMandateIdentification** <i><OrgnlMndtId></i> | [0..1] | Text | | 275 |
| | **OriginalCreditorSchemeIdentification** <i><OrgnlCdrSchmeId></i> | [0..1] | ± | | 275 |
| | **OriginalCreditorAgent** <i><OrgnlCdrAgtr></i> | [0..1] | ± | | 276 |
| | **OriginalCreditorAgentAccount** <i><OrgnlCdrAgtrAcct></i> | [0..1] | ± | C14, C13 | 277 |
| | **OriginalDebtor** <i><OrgnlDbtr></i> | [0..1] | ± | | 278 |
| | **OriginalDebtorAccount** <i><OrgnlDbtrAcct></i> | [0..1] | ± | | 279 |
| | **OriginalDebtorAgent** <i><OrgnlDbtrAgtr></i> | [0..1] | ± | | 280 |
| | **OriginalDebtorAgentAccount** <i><OrgnlDbtrAgtrAcct></i> | [0..1] | ± | C14, C13 | 281 |
| | **OriginalFinalCollectionDate** <i><OrgnlFnCltnDt></i> | [0..1] | Date | | 282 |
| | **OriginalFrequency** <i><OrgnlFrqcy></i> | [0..1] | ± | | 282 |
| | **OriginalReason** <i><OrgnlRsn></i> | [0..1] | | | 282 |
| (Or | **Code** <i><Cd></i> | [1..1] | CodeSet | | 282 |
| Or) | **Proprietary** <i><Prtry></i> | [1..1] | Text | | 282 |
| | **OriginalTrackingDays** <i><OrgnlTrckgDays></i> | [0..1] | Text | | 283 |
| | **ElectronicSignature** <i><ElctrncSgntr></i> | [0..1] | Text | | 283 |
| | **FirstCollectionDate** <i><FrstColltnDt></i> | [0..1] | Date | | 283 |
| | **FinalCollectionDate** <i><FnCltnDt></i> | [0..1] | Date | | 283 |
| | **Frequency** <i><Frqcy></i> | [0..1] | ± | | 283 |
| | **Reason** <i><Rsn></i> | [0..1] | | | 283 |
| (Or | **Code** <i><Cd></i> | [1..1] | CodeSet | | 284 |
| Or) | **Proprietary** <i><Prtry></i> | [1..1] | Text | | 284 |
| | **TrackingDays** <i><TrckgDays></i> | [0..1] | Text | | 284 |
| | **CreditorSchemeIdentification** <i><CdrSchmeId></i> | [0..1] | ± | | 284 |
| | **PreNotificationIdentification** <i><PrNtfctnId></i> | [0..1] | Text | | 285 |
| | **PreNotificationDate** <i><PrNtfctnDt></i> | [0..1] | Date | | 286 |

---

<!-- Page 252 -->

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **UltimateCreditor** *<UltmtCddtr>* | [0..1] | ± | | 286 |
| | **DebtorAgent** *<DbtrAgt>* | [1..1] | ± | | 287 |
| | **DebtorAgentAccount** *<DbtrAgtAcct>* | [0..1] | ± | C14, C13 | 288 |
| | **Debtor** *<Dbtr>* | [1..1] | ± | | 289 |
| | **DebtorAccount** *<DbtrAcct>* | [1..1] | ± | C14, C13 | 290 |
| | **UltimateDebtor** *<UltmtDbtr>* | [0..1] | ± | | 291 |
| | **InstructionForCreditorAgent** *<InstrForCddtrAgt>* | [0..1] | Text | | 292 |
| | **Purpose** *<Purp>* | [0..1] | ± | | 293 |
| | **RegulatoryReporting** *<RgltryRptg>* | [0..10] | ± | | 293 |
| | **Tax** *<Tax>* | [0..1] | | | 293 |
| | **Creditor** *<Cddtr>* | [0..1] | ± | | 295 |
| | **Debtor** *<Dbtr>* | [0..1] | ± | | 295 |
| | **UltimateDebtor** *<UltmtDbtr>* | [0..1] | ± | | 295 |
| | **AdministrationZone** *<AdminZone>* | [0..1] | Text | | 296 |
| | **ReferenceNumber** *<RefNb>* | [0..1] | Text | | 296 |
| | **Method** *<Mtd>* | [0..1] | Text | | 296 |
| | **TotalTaxableBaseAmount** *<TtlTaxblBaseAmt>* | [0..1] | Amount | C1, C11 | 296 |
| | **TotalTaxAmount** *<TtlTaxAmt>* | [0..1] | Amount | C1, C11 | 297 |
| | **Date** *<Dt>* | [0..1] | Date | | 297 |
| | **SequenceNumber** *<SeqNb>* | [0..1] | Quantity | | 297 |
| | **Record** *<Rcrd>* | [0..*] | | | 297 |
| | **Type** *<Tp>* | [0..1] | Text | | 298 |
| | **Category** *<Ctgy>* | [0..1] | Text | | 298 |
| | **CategoryDetails** *<CtgyDtls>* | [0..1] | Text | | 298 |
| | **DebtorStatus** *<DbtrSts>* | [0..1] | Text | | 299 |
| | **CertificateIdentification** *<CertId>* | [0..1] | Text | | 299 |
| | **FormsCode** *<FrmsCd>* | [0..1] | Text | | 299 |
| | **Period** *<Prd>* | [0..1] | | | 299 |
| | **Year** *<Yr>* | [0..1] | Year | | 299 |
| | **Type** *<Tp>* | [0..1] | CodeSet | | 299 |
| | **FromToDate** *<FrToDt>* | [0..1] | ± | | 300 |

---

<!-- Page 253 -->

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **TaxAmount** `<TaxAmt>` | [0..1] |  |  | 301 |
| | **Rate** `<Rate>` | [0..1] | Rate |  | 301 |
| | **TaxableBaseAmount** `<TaxBlBaseAmt>` | [0..1] | Amount | C1, C11 | 301 |
| | **TotalAmount** `<TtlAmt>` | [0..1] | Amount | C1, C11 | 301 |
| | **Details** `<Dtls>` | [0..*] |  |  | 302 |
| | **Period** `<Prd>` | [0..1] |  |  | 302 |
| | **Year** `<Yr>` | [0..1] | Year |  | 302 |
| | **Type** `<Tp>` | [0..1] | CodeSet |  | 303 |
| | **FromToDate** `<FrToDt>` | [0..1] | ± |  | 303 |
| | **Amount** `<Amt>` | [1..1] | Amount | C1, C11 | 304 |
| | **AdditionalInformation** `<AddtlInf>` | [0..1] | Text |  | 304 |
| | **RelatedRemittanceInformation** `<RltdRmInf>` | [0..10] |  |  | 304 |
| | **RemittanceIdentification** `<RmId>` | [0..1] | Text |  | 305 |
| | **RemittanceLocationDetails** `<RmtLctnDtls>` | [0..*] |  |  | 305 |
| | **Method** `<Mtd>` | [1..1] | CodeSet |  | 305 |
| | **ElectronicAddress** `<ElctrncAdr>` | [0..1] | Text |  | 306 |
| | **PostalAddress** `<PstlAdr>` | [0..1] |  |  | 306 |
| | **Name** `<Nm>` | [1..1] | Text |  | 306 |
| | **Address** `<Adr>` | [1..1] | ± |  | 306 |
| | **RemittanceInformation** `<RmInf>` | [0..1] | ± |  | 307 |
| | **SupplementaryData** `<SplmtryData>` | [0..*] | ± | C18 | 308 |

## Constraints

- **ChargeBearerRule**

  If ChargeBearer is present, then DirectDebitTransactionInformation/ChargeBearer is not allowed.

  If DirectDebitTransactionInformation/ChargeBearer is present, then ChargeBearer is not allowed.

  DirectDebitTransactionInformation/ChargeBearer and ChargeBearer may both be absent.

  Following Must be True

  /ChargeBearer Must be absent

  Or /DirectDebitTransactionInformation[\*]/ChargeBearer Must be absent

- **ChargesAccountAgentRule**

  If ChargesAccountAgent is present, then it must contain a branch of the CreditorAgent. It must not contain a completely different agent.

---

<!-- Page 254 -->

On Condition
`/ChargesAccountAgent is present`
Following Must be True
`/ChargesAccountAgent/FinancialInstitutionIdentification/Name Must be equal to value 'Branch of DebtorAgent'`

*   **ChargesAccountRule**

    If **ChargesAccountAgent** is present, then **ChargesAccount** must be present.

    On Condition
    `/ChargesAccountAgent is present`
    Following Must be True
    `/ChargesAccount Must be present`

*   **CreditorSchemeIdentificationRule**

    If **CreditorSchemeIdentification** is present, then **DirectDebitTransactionInformation/CreditorSchemeIdentification** is not allowed.

    If **DirectDebitTransactionInformation/CreditorSchemeIdentification** is present, then **CreditorSchemeIdentification** is not allowed.

    **DirectDebitTransactionInformation/CreditorSchemeIdentification** and **CreditorSchemeIdentification** may both be absent.
    Following Must be True
    `/CreditorSchemeIdentification Must be absent`
    Or `/DirectDebitTransactionInformation[*]/DirectDebitTransaction/CreditorSchemeIdentification Must be absent`

*   **PaymentTypeInformationRule**

    If **PaymentTypeInformation** is present, then **DirectDebitTransactionInformation/PaymentTypeInformation** is not allowed.

    On Condition
    `/PaymentTypeInformation is present`
    Following Must be True
    `/DirectDebitTransactionInformation[*]/PaymentTypeInformation Must be absent`

*   **UltimateCreditorGuideline**

    **UltimateCreditor** may only be present if different from **Creditor**.

*   **UltimateCreditorRule**

    If **UltimateCreditor** is present, then **DirectDebitTransactionInformation/UltimateCreditor** is not allowed.

    If **DirectDebitTransactionInformation/UltimateCreditor** is present, then **UltimateCreditor** is not allowed.

    **DirectDebitTransactionInformation/UltimateCreditor** and **UltimateCreditor** may both be absent.
    Following Must be True
    `/UltimateCreditor Must be absent`
    Or `/DirectDebitTransactionInformation[*]/UltimateCreditor Must be absent`

### 5.4.2.1 PaymentInformationIdentification <PmtInfId>

*Presence: [1..1]*

*Definition: Unique identification, as assigned by a sending party, to unambiguously identify the payment information group within the message.*

---

<!-- Page 255 -->

Datatype: "Max35Text" on page 431

## 5.4.2.2 PaymentMethod <PmtId>

Presence: [1..1]

Definition: Specifies the means of payment that will be used to move the amount of money.

Datatype: "PaymentMethod2Code" on page 421



| CodeName | Name | Definition |
|---|---|---|
| DD | DirectDebit | Collection of an amount of money from the debtor's bank account by the creditor. The amount of money and dates of collections may vary. |

## 5.4.2.3 RequestedAdviceType <ReqdAdvTp>

Presence: [0..1]

Definition: Type of advice details requested.

**RequestedAdviceType <ReqdAdvTp>** contains the following **AdviceType1** elements



| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **CreditAdvice** <CdtAdv> | [0..1] | | | 255 |
| (Or | **Code** <Cd> | [1..1] | CodeSet | | 255 |
| Or) | **Proprietary** <Prt> | [1..1] | Text | | 256 |
| | **DebitAdvice** <DbtAdv> | [0..1] | | | 256 |
| (Or | **Code** <Cd> | [1..1] | CodeSet | | 256 |
| Or) | **Proprietary** <Prt> | [1..1] | Text | | 256 |

### 5.4.2.3.1 CreditAdvice <CdtAdv>

Presence: [0..1]

Definition: Type of credit advice requested.

**CreditAdvice <CdtAdv>** contains one of the following **AdviceType1Choice** elements



| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| (Or | **Code** <Cd> | [1..1] | CodeSet | | 255 |
| Or) | **Proprietary** <Prt> | [1..1] | Text | | 256 |

#### 5.4.2.3.1.1 Code <Cd>

Presence: [1..1]

Definition: Advice type, in a coded form.

Datatype: "AdviceType1Code" on page 409

---

<!-- Page 256 -->

| CodeName | Name | Definition |
|---|---|---|
| ADWD | AdviceWithDetails | Advice with transaction details is requested. |
| ADND | AdviceWithoutDetails | Advice without transaction details is requested. |

## 5.4.2.3.1.2 Proprietary <Ptry>

*Presence:* [1..1]

*Definition:* Advice type, in a proprietary form.

*Datatype:* "Max35Text" on page 431

## 5.4.2.3.2 DebitAdvice <DbtAdvc>

*Presence:* [0..1]

*Definition:* Type de debit advice requested.

DebitAdvice <DbtAdvc> contains one of the following AdviceType1Choice elements

| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| (Or | Code <Cd> | [1..1] | CodeSet | | 256 |
| (Or) | Proprietary <Ptry> | [1..1] | Text | | 256 |

### 5.4.2.3.2.1 Code <Cd>

*Presence:* [1..1]

*Definition:* Advice type, in a coded form.

*Datatype:* "AdviceType1Code" on page 409

| CodeName | Name | Definition |
|---|---|---|
| ADWD | AdviceWithDetails | Advice with transaction details is requested. |
| ADND | AdviceWithoutDetails | Advice without transaction details is requested. |

### 5.4.2.3.2.2 Proprietary <Ptry>

*Presence:* [1..1]

*Definition:* Advice type, in a proprietary form.

*Datatype:* "Max35Text" on page 431

## 5.4.4 BatchBooking <BtchBook>

*Presence:* [0..1]

*Definition:* Identifies whether a single entry per individual transaction or a batch entry for the sum of the amounts of all transactions within the group of a message is requested.

Usage: Batch booking is used to request and not order a possible batch booking.

*Datatype:* One of the following values must be used (see "BatchBookingIndicator" on page 427):

---

<!-- Page 257 -->

• *Meaning When True:* Identifies that a batch entry for the sum of the amounts of all transactions in the batch or message is requested.

• *Meaning When False:* Identifies that a single entry for each of the transactions in the batch or message is requested.

### 5.4.2.5 NumberOfTransactions <NbOfTxs>

*Presence:* [0..1]

*Definition:* Number of individual transactions contained in the payment information group.

*Datatype:* "Max15NumericText" on page 430

### 5.4.2.6 ControlSum <CtrlSum>

*Presence:* [0..1]

*Definition:* Total of all individual amounts included in the group, irrespective of currencies.

*Datatype:* "DecimalNumber" on page 427

### 5.4.2.7 PaymentTypeInformation <PmtTpInf>

*Presence:* [0..1]

*Definition:* Set of elements used to further specify the type of transaction.

**PaymentTypeInformation <PmtTpInf>** contains the following elements (see "PaymentTypeInformation29" on page 348 for details)



| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
| :--- | :--- | :--- | :--- | :--- | :--- |
| | InstructionPriority <InstrPrty> | [0..1] | CodeSet | | 348 |
| | ServiceLevel <SvcLvl> | [0..] | | | 349 |
| {Or | Code <Cd> | [1..1] | CodeSet | | 349 |
| Or} | Proprietary <Prtry> | [0..1] | Text | | 349 |
| | LocalInstrument <LocInstrm> | [0..1] | | | 349 |
| {Or | Code <Cd> | [1..1] | CodeSet | | 349 |
| Or} | Proprietary <Prtry> | [1..1] | Text | | 350 |
| | SequenceType <SeqTp> | [0..1] | CodeSet | | 350 |
| | CategoryPurpose <CatgPurp> | [0..1] | | | 350 |
| {Or | Code <Cd> | [1..1] | CodeSet | | 350 |
| Or} | Proprietary <Prtry> | [1..1] | Text | | 350 |

### 5.4.2.8 RequestedCollectionDate <ReqdCollDt>

*Presence:* [1..1]

*Definition:* Date and time at which the creditor requests that the amount of money is to be collected from the debtor.

*Datatype:* "ISODate" on page 425

---

<!-- Page 258 -->

## 5.4.2.9 Creditor <Cdr>

*Presence:* [1..1]

*Definition:* Party to which an amount of money is due.

**Creditor <Cdr>** contains the following elements (see "PartyIdentification272" on page 336 for details)



| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Name <Nm> | [0..1] | Text | | 337 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 338 |
| | Identification <Id> | [0..1] | | | 338 |
| {Or | OrganisationIdentification <OrgId> | [1..1] | | | 339 |
| | AnyBIC <AnyBIC> | [0..1] | IdentifierSet | C5 | 340 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 340 |
| | Other <Othr> | [0..*] | | | 340 |
| | Identification <Id> | [1..1] | Text | | 341 |
| | SchemeName <SchmeNm> | [0..1] | | | 341 |
| {Or | Code <Cd> | [1..1] | CodeSet | | 341 |
| Or} | Proprietary <Prtry> | [1..1] | Text | | 341 |
| | Issuer <Issr> | [0..1] | Text | | 341 |
| Or} | PrivateIdentification <PrvtId> | [1..1] | | | 341 |
| | DateAndPlaceOfBirth <DtAndPlcOfBirth> | [0..1] | | | 342 |
| | BirthDate <BirthDt> | [1..1] | Date | | 342 |
| | ProvinceOfBirth <PrvcOfBirth> | [1..1] | Text | | 342 |
| | CityOfBirth <CityOfBirth> | [1..1] | Text | | 343 |
| | CountryOfBirth <CtryOfBirth> | [1..1] | CodeSet | C7 | 343 |
| | Other <Othr> | [0..*] | | | 343 |
| | Identification <Id> | [1..1] | Text | | 343 |
| | SchemeName <SchmeNm> | [0..1] | | | 343 |
| {Or | Code <Cd> | [1..1] | CodeSet | | 344 |
| Or} | Proprietary <Prtry> | [1..1] | Text | | 344 |
| | Issuer <Issr> | [0..1] | Text | | 344 |
| | CountryOfResidence <CtryOfRes> | [0..1] | CodeSet | C7 | 344 |
| | ContactDetails <CtctDtls> | [0..1] | ± | | 344 |

---

<!-- Page 259 -->

## 5.4.2.10 CreditorAccount <CddrAcct>

*Presence:* [1..1]

*Definition:* Unambiguous identification of the account of the creditor to which a credit entry will be posted as a result of the payment transaction.

*Impacted by:* C14 "IdentificationOrProxyPresenceRule", C13 "IdentificationAndProxyGuideline"

**CreditorAccount <CddrAcct>** contains the following elements (see "CashAccount40" on page 309 for details)



| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | Identification <Id> | [0..1] | ± | | 310 |
| | Type <Tp> | [0..1] | ± | | 310 |
| | Currency <Ccy> | [0..1] | CodeSet | C2 | 310 |
| | Name <Nm> | [0..1] | Text | | 311 |
| | Proxy <Prxy> | [0..1] | ± | | 311 |

### Constraints

- **IdentificationAndProxyGuideline**

If the account identification is not defined through a conventional identification such as an email address or a mobile number, then the proxy element should be used for the identification of the account.

- **IdentificationOrProxyPresenceRule**

Identification must be present or Proxy must be present. Both may be present.

```
Following Must be True
/Identification Must be present
Or
/Proxy Must be present
```

## 5.4.2.11 CreditorAgent <CddrAgt>

*Presence:* [1..1]

*Definition:* Financial institution servicing an account for the creditor.

---

<!-- Page 260 -->

CreditorAgent <CdrAgnt> contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on page 320 for details)



<table>
  <tr>
    <th>Or</th>
    <th>MessageElement&lt;XML Tag&gt;</th>
    <th>Mult.</th>
    <th>Type</th>
    <th>Constr. No.</th>
    <th>Page</th>
  </tr>
  <tr>
    <td></td>
    <td>FinancialInstitutionIdentification &lt;FinInstlId&gt;</td>
    <td>[1..1]</td>
    <td></td>
    <td></td>
    <td>321</td>
  </tr>
  <tr>
    <td></td>
    <td>BICFI &lt;BICFI&gt;</td>
    <td>[0..1]</td>
    <td>IdentifierSet</td>
    <td>C6</td>
    <td>321</td>
  </tr>
  <tr>
    <td></td>
    <td>ClearingSystemMemberIdentification &lt;ClrSysMmbId&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>322</td>
  </tr>
  <tr>
    <td></td>
    <td>LEI &lt;LEI&gt;</td>
    <td>[0..1]</td>
    <td>IdentifierSet</td>
    <td></td>
    <td>322</td>
  </tr>
  <tr>
    <td></td>
    <td>Name &lt;Nm&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>322</td>
  </tr>
  <tr>
    <td></td>
    <td>PostalAddress &lt;PstlAdr&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>322</td>
  </tr>
  <tr>
    <td></td>
    <td>Other &lt;Othr&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>323</td>
  </tr>
  <tr>
    <td></td>
    <td>BranchIdentification &lt;BrnchId&gt;</td>
    <td>[0..1]</td>
    <td></td>
    <td></td>
    <td>324</td>
  </tr>
  <tr>
    <td></td>
    <td>Identification &lt;Id&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>324</td>
  </tr>
  <tr>
    <td></td>
    <td>LEI &lt;LEI&gt;</td>
    <td>[0..1]</td>
    <td>IdentifierSet</td>
    <td></td>
    <td>324</td>
  </tr>
  <tr>
    <td></td>
    <td>Name &lt;Nm&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>324</td>
  </tr>
  <tr>
    <td></td>
    <td>PostalAddress &lt;PstlAdr&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>324</td>
  </tr>
</table>

## 5.4.2.12 CreditorAgentAccount <CdrAgntAcct>

*Presence:* [0..1]

*Definition:* Unambiguous identification of the account of the creditor agent at its servicing agent in the payment chain.

*Impacted by:* C14 "IdentificationOrProxyPresenceRule", C13 "IdentificationAndProxyGuideline"

CreditorAgentAccount <CdrAgntAcct> contains the following elements (see "CashAccount40" on page 309 for details)



<table>
  <tr>
    <th>Or</th>
    <th>MessageElement&lt;XML Tag&gt;</th>
    <th>Mult.</th>
    <th>Type</th>
    <th>Constr. No.</th>
    <th>Page</th>
  </tr>
  <tr>
    <td></td>
    <td>Identification &lt;Id&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>310</td>
  </tr>
  <tr>
    <td></td>
    <td>Type &lt;Tp&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>310</td>
  </tr>
  <tr>
    <td></td>
    <td>Currency &lt;Ccy&gt;</td>
    <td>[0..1]</td>
    <td>CodeSet</td>
    <td>C2</td>
    <td>310</td>
  </tr>
  <tr>
    <td></td>
    <td>Name &lt;Nm&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>311</td>
  </tr>
  <tr>
    <td></td>
    <td>Proxy &lt;Prxy&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>311</td>
  </tr>
</table>

---

<!-- Page 261 -->

## Constraints

- **IdentificationAndProxyGuideline**

  If the account identification is not defined through a conventional identification such as an email address or a mobile number, then the proxy element should be used for the identification of the account.

- **IdentificationOrProxyPresenceRule**

  Identification must be present or Proxy must be present. Both may be present.

  ```
  Following Must be True
    /Identification Must be present
    Or    /Proxy Must be present
  ```

### 5.4.2.13 UltimateCreditor <UltmtCdtor>

*Presence:* [0..1]

*Definition:* Ultimate party to which an amount of money is due.

---

<!-- Page 262 -->

UltimateCreditor <UltimateCdtor> contains the following elements (see "PartyIdentification272" on page 336 for details)

| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Name <Nm> | [0..1] | Text | | 337 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 338 |
| | Identification <Id> | [0..1] | | | 338 |
| (Or | OrganisationIdentification <OrgId> | [1..1] | | | 339 |
| | AnyBIC <AnyBIC> | [0..1] | IdentifierSet | C5 | 340 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 340 |
| | Other <Othr> | [0..*] | | | 340 |
| | Identification <Id> | [1..1] | Text | | 341 |
| | SchemeName <SchmeNm> | [0..1] | | | 341 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 341 |
| Or) | Proprietary <Prtry> | [1..1] | Text | | 341 |
| | Issuer <Issr> | [0..1] | Text | | 341 |
| (Or) | PrivateIdentification <PrvtId> | [1..1] | | | 341 |
| | DateAndPlaceOfBirth <DtAndPlcOfBirth> | [0..1] | | | 342 |
| | BirthDate <BirthDt> | [1..1] | Date | | 342 |
| | ProvinceOfBirth <PrvcOfBirth> | [0..1] | Text | | 342 |
| | CityOfBirth <CityOfBirth> | [1..1] | Text | | 343 |
| | CountryOfBirth <CtryOfBirth> | [1..1] | CodeSet | C7 | 343 |
| | Other <Othr> | [0..*] | | | 343 |
| | Identification <Id> | [1..1] | Text | | 343 |
| | SchemeName <SchmeNm> | [0..1] | | | 343 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 344 |
| Or) | Proprietary <Prtry> | [1..1] | Text | | 344 |
| | Issuer <Issr> | [0..1] | Text | | 344 |
| | CountryOfResidence <CtryOfRes> | [0..1] | CodeSet | C7 | 344 |
| | ContactDetails <CtctDtls> | [0..1] | ± | | 344 |

## 5.4.2.14 ChargeBearer <ChrgBr>

*Presence: [0..1]*

*Definition: Specifies which party/parties will bear the charges associated with the processing of the payment transaction.*

---

<!-- Page 263 -->

Datatype: "ChargeBearerType1Code" on page 410



| CodeName | Name | Definition |
|---|---|---|
| DEBT | BorneByDebtor | All transaction charges are to be borne by the debtor. |
| CRED | BorneByCreditor | All transaction charges are to be borne by the creditor. |
| SHAR | Shared | In a credit transfer context, means that transaction charges on the sender side are to be borne by the debtor, transaction charges on the receiver side are to be borne by the creditor. In a direct debit context, means that transaction charges on the sender side are to be borne by the creditor, transaction charges on the receiver side are to be borne by the debtor. |
| SLEV | FollowingServiceLevel | Charges are to be applied following the rules agreed in the service level and/or scheme. |

## 5.4.2.15 ChargesAccount <ChrgsAcct>

*Presence:* [0..1]

*Definition:* Account used to process charges associated with a transaction.

Usage: Charges account should be used when charges have to be booked to an account different from the account identified in debtor's account.

*Impacted by:* C14 "IdentificationOrProxyPresenceRule", C13 "IdentificationAndProxyGuideline"

**ChargesAccount <ChrgsAcct>** contains the following elements (see "CashAccount40" on page 309 for details)



| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Identification <Id> | [0..1] | ± | | 310 |
| | Type <Tp> | [0..1] | ± | | 310 |
| | Currency <Ccy> | [0..1] | CodeSet | C2 | 310 |
| | Name <Nm> | [0..1] | Text | | 311 |
| | Proxy <Prxy> | [0..1] | ± | | 311 |

### Constraints

- **IdentificationAndProxyGuideline**

If the account identification is not defined through a conventional identification such as an email address or a mobile number, then the proxy element should be used for the identification of the account.

- **IdentificationOrProxyPresenceRule**

Identification must be present or Proxy must be present. Both may be present.

---

<!-- Page 264 -->

Following Must be True
/Identification Must be present
Or /Proxy Must be present

## 5.4.2.16 ChargesAccountAgent <ChrgsAcctAgt>

Presence: [0..1]

Definition: Agent that services a charges account.

Usage: Charges account agent should only be used when the charges account agent is different from the creditor agent.

**ChargesAccountAgent <ChrgsAcctAgt>** contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on page 320 for details)



| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | FinancialInstitutionIdentification <FinInstnId> | [1..1] |  |  | 321 |
| | BICFI <BICFI> | [0..1] | IdentifierSet | C6 | 321 |
| | ClearingSystemMemberIdentification <ClrSysMmbId> | [0..1] | ± |  | 322 |
| | LEI <LEI> | [0..1] | IdentifierSet |  | 322 |
| | Name <Nm> | [0..1] | Text |  | 322 |
| | PostalAddress <PstlAdr> | [0..1] | ± |  | 322 |
| | Other <Othr> | [0..1] | ± |  | 323 |
| | BranchIdentification <BrnchId> | [0..1] |  |  | 324 |
| | Identification <Id> | [0..1] | Text |  | 324 |
| | LEI <LEI> | [0..1] | IdentifierSet |  | 324 |
| | Name <Nm> | [0..1] | Text |  | 324 |
| | PostalAddress <PstlAdr> | [0..1] | ± |  | 324 |

## 5.4.2.17 CreditorSchemeIdentification <CdtrSchmeId>

Presence: [0..1]

Definition: Credit party that signs the mandate.

---

<!-- Page 265 -->

CreditorSchemeIdentification <CdtrSchmeId> contains the following elements (see "PartyIdentification27" on page 336 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
| :--- | :--- | :--- | :--- | :--- | :--- |
| | Name *<Nm>* | [0..1] | Text | | 337 |
| | PostalAddress *<PstlAdr>* | [0..1] | ± | | 338 |
| | Identification *<Id>* | [0..1] | | | 338 |
| (Or | OrganisationIdentification *<OrgId>* | [1..1] | | | 339 |
| | AnyBIC *<AnyBIC>* | [0..1] | IdentifierSet | C5 | 340 |
| | LEI *<LEI>* | [0..1] | IdentifierSet | | 340 |
| | Other *<Othr>* | [0..*] | | | 340 |
| | Identification *<Id>* | [1..1] | Text | | 341 |
| | SchemeName *<SchmeNm>* | [0..1] | | | 341 |
| (Or | Code *<Cd>* | [1..1] | CodeSet | | 341 |
| Or) | Proprietary *<Prtry>* | [1..1] | Text | | 341 |
| | Issuer *<Issr>* | [0..1] | Text | | 341 |
| (Or) | PrivateIdentification *<PrvtId>* | [1..1] | | | 341 |
| | DateAndPlaceOfBirth *<DtAndPlcOfBrth>* | [0..1] | | | 342 |
| | BirthDate *<BirthDt>* | [1..1] | Date | | 342 |
| | ProvinceOfBirth *<PrvcOfBrth>* | [0..1] | Text | | 342 |
| | CityOfBirth *<CityOfBrth>* | [1..1] | Text | | 343 |
| | CountryOfBirth *<CtryOfBrth>* | [1..1] | CodeSet | C7 | 343 |
| | Other *<Othr>* | [0..*] | | | 343 |
| | Identification *<Id>* | [1..1] | Text | | 343 |
| | SchemeName *<SchmeNm>* | [0..1] | | | 343 |
| (Or | Code *<Cd>* | [1..1] | CodeSet | | 344 |
| Or) | Proprietary *<Prtry>* | [1..1] | Text | | 344 |
| | Issuer *<Issr>* | [0..1] | Text | | 344 |
| | CountryOfResidence *<CtryOfRes>* | [0..1] | CodeSet | C7 | 344 |
| | ContactDetails *<CtctDtls>* | [0..1] | ± | | 344 |

**5.4.2.18 DirectDebitTransactionInformation <DctDbtTxInf>**

*Presence: [1..*]*

*Definition: Provides information on the individual transaction(s) included in the message.*

*Impacted by: C20 "UltimateCreditorGuideline", C22 "UltimateDebtorGuideline"*

---

<!-- Page 266 -->

DirectDebitTransactionInformation <DctDbtTxInf> contains the following
DirectDebitTransactionInformation32 elements



<table>
  <tr>
    <th>Or</th>
    <th>MessageElement&lt;XML Tag&gt;</th>
    <th>Mult.</th>
    <th>Type</th>
    <th>Constr. No.</th>
    <th>Page</th>
  </tr>
  <tr>
    <td></td>
    <td><b>PaymentIdentification</b> &lt;PmtId&gt;</td>
    <td>[1..1]</td>
    <td>±</td>
    <td></td>
    <td>269</td>
  </tr>
  <tr>
    <td></td>
    <td><b>PaymentTypeInformation</b> &lt;PmtTpInf&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>269</td>
  </tr>
  <tr>
    <td></td>
    <td><b>InstructedAmount</b> &lt;InstdAmt&gt;</td>
    <td>[1..1]</td>
    <td>Amount</td>
    <td>C1, C11</td>
    <td>269</td>
  </tr>
  <tr>
    <td></td>
    <td><b>ChargeBearer</b> &lt;ChrgBr&gt;</td>
    <td>[0..1]</td>
    <td>CodeSet</td>
    <td></td>
    <td>270</td>
  </tr>
  <tr>
    <td></td>
    <td><b>DirectDebitTransaction</b> &lt;DctDbtTx&gt;</td>
    <td>[0..1]</td>
    <td></td>
    <td></td>
    <td>270</td>
  </tr>
  <tr>
    <td></td>
    <td><b>MandateRelatedInformation</b> &lt;MndtRltdIdInf&gt;</td>
    <td>[0..1]</td>
    <td></td>
    <td>C2, C3</td>
    <td>272</td>
  </tr>
  <tr>
    <td></td>
    <td><b>MandateIdentification</b> &lt;MndtId&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>274</td>
  </tr>
  <tr>
    <td></td>
    <td><b>DateOfSignature</b> &lt;DtOfSgntr&gt;</td>
    <td>[0..1]</td>
    <td>Date</td>
    <td></td>
    <td>274</td>
  </tr>
  <tr>
    <td></td>
    <td><b>AmendmentIndicator</b> &lt;AmdmntInd&gt;</td>
    <td>[0..1]</td>
    <td>Indicator</td>
    <td></td>
    <td>274</td>
  </tr>
  <tr>
    <td></td>
    <td><b>AmendmentInformationDetails</b> &lt;AmdmntInfDtls&gt;</td>
    <td>[0..1]</td>
    <td></td>
    <td></td>
    <td>274</td>
  </tr>
  <tr>
    <td></td>
    <td><b>OriginalMandateIdentification</b> &lt;OrgnlMndtId&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>275</td>
  </tr>
  <tr>
    <td></td>
    <td><b>OriginalCreditorSchemeIdentification</b> &lt;OrgnlCdrSchemId&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>275</td>
  </tr>
  <tr>
    <td></td>
    <td><b>OriginalCreditorAgent</b> &lt;OrgnlCdtiAg&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>276</td>
  </tr>
  <tr>
    <td></td>
    <td><b>OriginalCreditorAgentAccount</b> &lt;OrgnlCdtiAgtrAcct&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>277</td>
  </tr>
  <tr>
    <td></td>
    <td><b>OriginalDebtor</b> &lt;OrgnlDbtr&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>278</td>
  </tr>
  <tr>
    <td></td>
    <td><b>OriginalDebtorAccount</b> &lt;OrgnlDbtrAcct&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td>C14, C13</td>
    <td>279</td>
  </tr>
  <tr>
    <td></td>
    <td><b>OriginalDebtorAgent</b> &lt;OrgnlDbtrAg&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>280</td>
  </tr>
  <tr>
    <td></td>
    <td><b>OriginalDebtorAgentAccount</b> &lt;OrgnlDbtrAgtrAcct&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td>C14, C13</td>
    <td>281</td>
  </tr>
  <tr>
    <td></td>
    <td><b>OriginalFinalCollectionDate</b> &lt;OrgnlFnClCollnDt&gt;</td>
    <td>[0..1]</td>
    <td>Date</td>
    <td></td>
    <td>282</td>
  </tr>
  <tr>
    <td></td>
    <td><b>OriginalFrequency</b> &lt;OrgnlFrcy&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>282</td>
  </tr>
  <tr>
    <td></td>
    <td><b>OriginalReason</b> &lt;OrgnlRsn&gt;</td>
    <td>[0..1]</td>
    <td></td>
    <td></td>
    <td>282</td>
  </tr>
  <tr>
    <td>{Or</td>
    <td><b>Code</b> &lt;Cd&gt;</td>
    <td>[1..1]</td>
    <td>CodeSet</td>
    <td></td>
    <td>282</td>
  </tr>
  <tr>
    <td>Or}</td>
    <td><b>Proprietary</b> &lt;Prrty&gt;</td>
    <td>[1..1]</td>
    <td>Text</td>
    <td></td>
    <td>282</td>
  </tr>
  <tr>
    <td></td>
    <td><b>OriginalTrackingDays</b> &lt;OrgnlTrckgDays&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>283</td>
  </tr>
  <tr>
    <td></td>
    <td><b>ElectronicSignature</b> &lt;ElctrncSgntr&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>283</td>
  </tr>
  <tr>
    <td></td>
    <td><b>FirstCollectionDate</b> &lt;FrstCollnDt&gt;</td>
    <td>[0..1]</td>
    <td>Date</td>
    <td></td>
    <td>283</td>
  </tr>
  <tr>
    <td></td>
    <td><b>FinalCollectionDate</b> &lt;FnClCollnDt&gt;</td>
    <td>[0..1]</td>
    <td>Date</td>
    <td></td>
    <td>283</td>
  </tr>
  <tr>
    <td></td>
    <td><b>Frequency</b> &lt;Frcq&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>283</td>
  </tr>
</table>

---

<!-- Page 267 -->

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **Reason** *<Rsn>* | [0..1] |  |  | 283 |
| (Or | **Code** *<Cd>* | [1..1] | CodeSet |  | 284 |
| Or) | **Proprietary** *<Prtry>* | [1..1] | Text |  | 284 |
| | **TrackingDays** *<TrckgDays>* | [0..1] | Text |  | 284 |
| | **CreditorSchemeIdentification** *<CdrSchmId>* | [0..1] | ± |  | 284 |
| | **PreNotificationIdentification** *<PrfNtfctnId>* | [0..1] | Text |  | 285 |
| | **PreNotificationDate** *<PrfNtfctnDt>* | [0..1] | Date |  | 286 |
| | **UltimateCreditor** *<UltmCdr>* | [0..1] | ± |  | 286 |
| | **DebtorAgent** *<DbtrAgt>* | [1..1] | ± |  | 287 |
| | **DebtorAgentAccount** *<DbtrAgtAcc>* | [0..1] | ± | C14, C13 | 288 |
| | **Debtor** *<Dbtr>* | [1..1] | ± |  | 289 |
| | **DebtorAccount** *<DbtrAcc>* | [1..1] | ± | C14, C13 | 290 |
| | **UltimateDebtor** *<UltmDbtr>* | [0..1] | ± |  | 291 |
| | **InstructionForCreditorAgent** *<InstrForCdrAgt>* | [0..1] | Text |  | 292 |
| | **Purpose** *<Purp>* | [0..1] | ± |  | 293 |
| | **RegulatoryReporting** *<RgltryRptg>* | [0..10] | ± |  | 293 |
| | **Tax** *<Tax>* | [0..1] |  |  | 293 |
| | **Creditor** *<Cdr>* | [0..1] | ± |  | 295 |
| | **Debtor** *<Dbtr>* | [0..1] | ± |  | 295 |
| | **UltimateDebtor** *<UltmDbtr>* | [0..1] | ± |  | 295 |
| | **AdministrationZone** *<AdminZone>* | [0..1] | Text |  | 296 |
| | **ReferenceNumber** *<RefNb>* | [0..1] | Text |  | 296 |
| | **Method** *<Mtd>* | [0..1] | Text |  | 296 |
| | **TotalTaxableBaseAmount** *<TtlTaxblBaseAmt>* | [0..1] | Amount | C1, C11 | 296 |
| | **TotalTaxAmount** *<TtlTaxAmt>* | [0..1] | Amount | C1, C11 | 297 |
| | **Date** *<Dt>* | [0..1] | Date |  | 297 |
| | **SequenceNumber** *<SeqNb>* | [0..1] | Quantity |  | 297 |
| | **Record** *<Rcrd>* | [0..*] |  |  | 297 |
| | **Type** *<Tpp>* | [0..1] | Text |  | 298 |
| | **Category** *<Ctgy>* | [0..1] | Text |  | 298 |
| | **CategoryDetails** *<CtgyDtls>* | [0..1] | Text |  | 298 |

---

<!-- Page 268 -->

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **DebtorStatus** `<DbtrSts>` | [0..1] | Text | | 299 |
| | **CertificateIdentification** `<CertId>` | [0..1] | Text | | 299 |
| | **FormsCode** `<FrmsCd>` | [0..1] | Text | | 299 |
| | **Period** `<Prd>` | [0..1] | | | 299 |
| | **Year** `<Yr>` | [0..1] | Year | | 299 |
| | **Type** `<Tp>` | [0..1] | CodeSet | | 299 |
| | **FromToDate** `<FrToDt>` | [0..1] | ± | | 300 |
| | **TaxAmount** `<TaxAmt>` | [0..1] | | | 301 |
| | **Rate** `<Rate>` | [0..1] | Rate | | 301 |
| | **TaxableBaseAmount** `<TaxblBaseAmt>` | [0..1] | Amount | C1, C11 | 301 |
| | **TotalAmount** `<TtlAmt>` | [0..1] | Amount | C1, C11 | 301 |
| | **Details** `<Dtls>` | [0..*] | | | 302 |
| | **Period** `<Prd>` | [0..1] | | | 302 |
| | **Year** `<Yr>` | [0..1] | Year | | 302 |
| | **Type** `<Tp>` | [0..1] | CodeSet | | 303 |
| | **FromToDate** `<FrToDt>` | [0..1] | ± | | 303 |
| | **Amount** `<Amt>` | [1..1] | Amount | C1, C11 | 304 |
| | **AdditionalInformation** `<AddtlInf>` | [0..1] | Text | | 304 |
| | **RelatedRemittanceInformation** `<RltdRmtnf>` | [0..10] | | | 304 |
| | **RemittanceIdentification** `<RmtId>` | [0..1] | Text | | 305 |
| | **RemittanceLocationDetails** `<RmtLctnDtls>` | [0..*] | | | 305 |
| | **Method** `<Mtd>` | [1..1] | CodeSet | | 305 |
| | **ElectronicAddress** `<ElctrncAdr>` | [0..1] | Text | | 306 |
| | **PostalAddress** `<PstlAdr>` | [0..1] | | | 306 |
| | **Name** `<Nm>` | [1..1] | Text | | 306 |
| | **Address** `<Adr>` | [1..1] | ± | | 306 |
| | **RemittanceInformation** `<Rmtnf>` | [0..1] | ± | | 307 |
| | **SupplementaryData** `<SplmtryData>` | [0..*] | ± | C18 | 308 |

---

<!-- Page 269 -->

Constraints
* **UltimateCreditorGuideline**
UltimateCreditor may only be present if different from Creditor.
* **UltimateDebtorGuideline**
UltimateDebtor may only be present if different from Debtor.

### 5.4.2.18.1 PaymentIdentification <PmtId>
*Presence: [1..1]*
*Definition: Set of elements used to reference a payment instruction.*

**PaymentIdentification <PmtId>** contains the following elements (see "PaymentIdentification6" on page 330 for details)



| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | InstructionIdentification <InstdId> | [0..1] | Text | | 330 |
| | EndToEndIdentification <EndToEndId> | [1..1] | Text | | 330 |
| | UETR <UETR> | [0..1] | IdentifierSet | | 330 |

### 5.4.2.18.2 PaymentTypeInformation <PmtTpInf>
*Presence: [0..1]*
*Definition: Set of elements used to further specify the type of transaction.*

**PaymentTypeInformation <PmtTpInf>** contains the following elements (see "PaymentTypeInformation29" on page 348 for details)



| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | InstructionPriority <InstrPrty> | [0..1] | CodeSet | | 348 |
| | ServiceLevel <SvcLv> | [0..*] | | | 349 |
| Or | Code <Cd> | [1..1] | CodeSet | | 349 |
| Or | Proprietary <Prtry> | [1..1] | Text | | 349 |
| | LocalInstrument <LocInstrm> | [0..1] | | | 349 |
| Or | Code <Cd> | [1..1] | CodeSet | | 349 |
| Or | Proprietary <Prtry> | [1..1] | Text | | 350 |
| | SequenceType <SeqTp> | [0..1] | CodeSet | | 350 |
| | CategoryPurpose <CatgPurp> | [0..1] | | | 350 |
| Or | Code <Cd> | [1..1] | CodeSet | | 350 |
| Or | Proprietary <Prtry> | [1..1] | Text | | 350 |

### 5.4.2.18.3 InstructedAmount <InstdAmt>
*Presence: [1..1]*

---

<!-- Page 270 -->

*Definition:* Amount of money to be moved between the debtor and creditor, before deduction of charges, expressed in the currency as ordered by the initiating party.

*Usage:* This amount has to be transported unchanged through the transaction chain.

*Impacted by:* C1 "ActiveOrHistoricCurrency", C11 "CurrencyAmount"

*Datatype:* "ActiveOrHistoricCurrencyAndAmount" on page 407

## Constraints

- **ActiveOrHistoricCurrency**

The Currency Code must be registered, or have already been registered. Valid active or historic currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and may be or not be withdrawn on the day the message containing the Currency is exchanged.

- **CurrencyAmount**

The number of fractional digits (or minor unit of currency) must comply with ISO 4217.

Note: The decimal separator is a dot.

### 5.4.2.18.4 ChargeBearer <ChrgBr>

*Presence:* [0..1]

*Definition:* Specifies which party/parties will bear the charges associated with the processing of the payment transaction.

*Datatype:* "ChargeBearerType1Code" on page 410



| CodeName | Name | Definition |
| :--- | :--- | :--- |
| DEBT | BorneByDebtor | All transaction charges are to be borne by the debtor. |
| CRED | BorneByCreditor | All transaction charges are to be borne by the creditor. |
| SHAR | Shared | In a credit transfer context, means that transaction charges on the sender side are to be borne by the debtor, transaction charges on the receiver side are to be borne by the creditor. In a direct debit context, means that transaction charges on the sender side are to be borne by the creditor, transaction charges on the receiver side are to be borne by the debtor. |
| SLEV | FollowingServiceLevel | Charges are to be applied following the rules agreed in the service level and/or scheme. |

### 5.4.2.18.5 DirectDebitTransaction <DrctDbtTx>

*Presence:* [0..1]

*Definition:* Provides information specific to the direct debit mandate.

---

<!-- Page 271 -->

DirectDebitTransaction `<DctDbtTx>` contains the following **DirectDebitTransaction12** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **MandateRelatedInformation** `<MndtRltdInf>` | [0..1] | | C2, C3 | 272 |
| | **MandateIdentification** `<MndtId>` | [0..1] | Text | | 274 |
| | **DateOfSignature** `<DtOfSgntr>` | [0..1] | Date | | 274 |
| | **AmendmentIndicator** `<AmdmntInd>` | [0..1] | Indicator | | 274 |
| | **AmendmentInformationDetails** `<AmdmntInfDtls>` | [0..1] | | | 274 |
| | **OriginalMandateIdentification** `<OrgnlMndtId>` | [0..1] | Text | | 275 |
| | **OriginalCreditorSchemeIdentification** `<OrgnlCdrtrSchemId>` | [0..1] | ± | | 275 |
| | **OriginalCreditorAgent** `<OrgnlCdrtrAgg>` | [0..1] | ± | | 276 |
| | **OriginalCreditorAgentAccount** `<OrgnlCdrtrAggAcct>` | [0..1] | ± | C14, C13 | 277 |
| | **OriginalDebtor** `<OrgnlDbtr>` | [0..1] | ± | | 278 |
| | **OriginalDebtorAccount** `<OrgnlDbtrAcct>` | [0..1] | ± | C14, C13 | 279 |
| | **OriginalDebtorAgent** `<OrgnlDbtrAgg>` | [0..1] | ± | | 280 |
| | **OriginalDebtorAgentAccount** `<OrgnlDbtrAggAcct>` | [0..1] | ± | C14, C13 | 281 |
| | **OriginalFinalCollectionDate** `<OrgnlFnCltnDt>` | [0..1] | Date | | 282 |
| | **OriginalFrequency** `<OrgnlFrcy>` | [0..1] | ± | | 282 |
| | **OriginalReason** `<OrgnlRsn>` | [0..1] | | | 282 |
| (Or | **Code** `<Cd>` | [1..1] | CodeSet | | 282 |
| Or) | **Proprietary** `<Prtry>` | [1..1] | Text | | 282 |
| | **OriginalTrackingDays** `<OrgnlTrckgDays>` | [0..1] | Text | | 283 |
| | **ElectronicSignature** `<ElctrncSgntr>` | [0..1] | Text | | 283 |
| | **FirstCollectionDate** `<FrstCollnDt>` | [0..1] | Date | | 283 |
| | **FinalCollectionDate** `<FnCltnDt>` | [0..1] | Date | | 283 |
| | **Frequency** `<Frcy>` | [0..1] | ± | | 283 |
| | **Reason** `<Rsn>` | [0..1] | | | 283 |
| (Or | **Code** `<Cd>` | [1..1] | CodeSet | | 284 |
| Or) | **Proprietary** `<Prtry>` | [1..1] | Text | | 284 |
| | **TrackingDays** `<TrckgDays>` | [0..1] | Text | | 284 |
| | **CreditorSchemeIdentification** `<CdrtrSchemId>` | [0..1] | ± | | 284 |
| | **PreNotificationIdentification** `<PrNtfctnId>` | [0..1] | Text | | 285 |

---

<!-- Page 272 -->

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **PreNotificationDate** <PreNtfctnDt> | [0..1] | Date | | 286 |

**5.4.2.18.5.1 MandateRelatedInformation <MndtRltdInf>**

*Presence:* [0..1]

*Definition:* Provides further details of the direct debit mandate signed between the creditor and the debtor.

*Impacted by:* C2 "AmendmentIndicatorFalseRule", C3 "AmendmentIndicatorTrueRule"

---

<!-- Page 273 -->

MandateRelatedInformation <MndtRltdInf> contains the following MandateRelatedInformation16 elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **MandateIdentification** <MndtId> | [0..1] | Text | | 274 |
| | **DateOfSignature** <DtOfSgntr> | [0..1] | Date | | 274 |
| | **AmendmentIndicator** <AmdmntInd> | [0..1] | Indicator | | 274 |
| | **AmendmentInformationDetails** <AmdmntInfDtls> | [0..1] | | | 274 |
| | **OriginalMandateIdentification** <OrgnlMndtId> | [0..1] | Text | | 275 |
| | **OriginalCreditorSchemeIdentification** <OrgnlCdrtrSchemId> | [0..1] | ± | | 275 |
| | **OriginalCreditorAgent** <OrgnlCdrtrAgt> | [0..1] | ± | | 276 |
| | **OriginalCreditorAgentAccount** <OrgnlCdrtrAgtAcct> | [0..1] | ± | C14, C13 | 277 |
| | **OriginalDebtor** <OrgnlDbtr> | [0..1] | ± | | 278 |
| | **OriginalDebtorAccount** <OrgnlDbtrAcct> | [0..1] | ± | C14, C13 | 279 |
| | **OriginalDebtorAgent** <OrgnlDbtrAgt> | [0..1] | ± | | 280 |
| | **OriginalDebtorAgentAccount** <OrgnlDbtrAgtAcct> | [0..1] | ± | C14, C13 | 281 |
| | **OriginalFinalCollectionDate** <OrgnlFinCollnDt> | [0..1] | Date | | 282 |
| | **OriginalFrequency** <OrgnlFrcq> | [0..1] | ± | | 282 |
| | **OriginalReason** <OrgnlRsn> | [0..1] | | | 282 |
| {Or | **Code** <Cd> | [1..1] | CodeSet | | 282 |
| Or} | **Proprietary** <Prtry> | [1..1] | Text | | 282 |
| | **OriginalTrackingDays** <OrgnlTrckgDays> | [0..1] | Text | | 283 |
| | **ElectronicSignature** <ElctrncSgntr> | [0..1] | Text | | 283 |
| | **FirstCollectionDate** <FstCollnDt> | [0..1] | Date | | 283 |
| | **FinalCollectionDate** <FinCollnDt> | [0..1] | Date | | 283 |
| | **Frequency** <Frcq> | [0..1] | ± | | 283 |
| | **Reason** <Rsn> | [0..1] | | | 283 |
| {Or | **Code** <Cd> | [1..1] | CodeSet | | 284 |
| Or} | **Proprietary** <Prtry> | [1..1] | Text | | 284 |
| | **TrackingDays** <TrckgDays> | [0..1] | Text | | 284 |

---

<!-- Page 274 -->

Constraints

* **AmendmentIndicatorFalseRule**

  If AmendmentIndicator is false, then AmendmentInformationDetails is not allowed.

  ```text
  On Condition
  /AmendmentIndicator is equal to value 'false'
  Following Must be True
  /AmendmentInformationDetails Must be absent
  ```

* **AmendmentIndicatorTrueRule**

  If AmendmentIndicator is true, then AmendmentInformationDetails must be present.

  ```text
  On Condition
  /AmendmentIndicator is equal to value 'true'
  Following Must be True
  /AmendmentInformationDetails Must be present
  ```

**5.4.2.18.5.1.1 MandateIdentification <MndId>**

*Presence:* [0..1]

*Definition:* Unique identification, as assigned by the creditor, to unambiguously identify the mandate.

*Datatype:* "Max35Text" on page 431

**5.4.2.18.5.1.2 DateOfSignature <DtOfSgntr>**

*Presence:* [0..1]

*Definition:* Date on which the direct debit mandate has been signed by the debtor.

*Datatype:* "ISODate" on page 425

**5.4.2.18.5.1.3 AmendmentIndicator <AmdmntInd>**

*Presence:* [0..1]

*Definition:* Indicator notifying whether the underlying mandate is amended or not.

*Definition:* One of the following values must be used (see "TrueFalseIndicator" on page 427):

* *Meaning When True:* True

* *Meaning When False:* False

**5.4.2.18.5.1.4 AmendmentInformationDetails <AmdmntInfDtls>**

*Presence:* [0..1]

*Definition:* List of mandate elements that have been modified.

---

<!-- Page 275 -->

AmendmentInformationDetails <AmdmInfDtls> contains the following AmendmentInformationDetails15 elements

| Or | Message Element <XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **OriginalMandateIdentification** <OrgnlMndtd> | [0..1] | Text | | 275 |
| | **OriginalCreditorSchemeIdentification** <OrgnlCdrSchmeId> | [0..1] | ± | | 275 |
| | **OriginalCreditorAgent** <OrgnlCdrAgt> | [0..1] | ± | | 276 |
| | **OriginalCreditorAgentAccount** <OrgnlCdrAgtAcct> | [0..1] | ± | C14, C13 | 277 |
| | **OriginalDebtor** <OrgnlDbtr> | [0..1] | ± | | 278 |
| | **OriginalDebtorAccount** <OrgnlDbtrAcct> | [0..1] | ± | C14, C13 | 279 |
| | **OriginalDebtorAgent** <OrgnlDbtrAgt> | [0..1] | ± | | 280 |
| | **OriginalDebtorAgentAccount** <OrgnlDbtrAgtAcct> | [0..1] | ± | C14, C13 | 281 |
| | **OriginalFinalCollectionDate** <OrgnlFinCollnDt> | [0..1] | Date | | 282 |
| | **OriginalFrequency** <OrgnlFrcq> | [0..1] | ± | | 282 |
| | **OriginalReason** <OrgnlRsn> | [0..1] | | | 282 |
| Or | **Code** <Cd> | [1..1] | CodeSet | | 282 |
| Or | **Proprietary** <Ptry> | [1..1] | Text | | 282 |
| | **OriginalTrackingDays** <OrgnlTrckgDays> | [0..1] | Text | | 283 |

**5.4.2.18.5.1.4.1 OriginalMandateIdentification <OrgnlMndtd>**

*Presence:* [0..1]

*Definition:* Unique identification, as assigned by the creditor, to unambiguously identify the original mandate.

*Datatype:* "Max35Text" on page 431

**5.4.2.18.5.1.4.2 OriginalCreditorSchemeIdentification <OrgnlCdrSchmeId>**

*Presence:* [0..1]

*Definition:* Original creditor scheme identification that has been modified.

---

<!-- Page 276 -->

OriginalCdrSchmeIdentification <OrgnlCdrSchmeId> contains the following elements (see "PartyIdentification22" on page 336 for details)



<table>
  <thead>
    <tr>
      <th>Or</th>
      <th>MessageElement&lt;XML Tag&gt;</th>
      <th>Mult.</th>
      <th>Type</th>
      <th>Constr. No.</th>
      <th>Page</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td>Name &lt;Nm&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>337</td>
    </tr>
    <tr>
      <td></td>
      <td>PostalAddress &lt;PstlAdr&gt;</td>
      <td>[0..1]</td>
      <td>±</td>
      <td></td>
      <td>338</td>
    </tr>
    <tr>
      <td></td>
      <td>Identification &lt;Id&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>338</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>OrganisationIdentification &lt;OrgId&gt;</td>
      <td>[1..1]</td>
      <td></td>
      <td></td>
      <td>339</td>
    </tr>
    <tr>
      <td></td>
      <td>AnyBIC &lt;AnyBIC&gt;</td>
      <td>[0..1]</td>
      <td>IdentifierSet</td>
      <td>C5</td>
      <td>340</td>
    </tr>
    <tr>
      <td></td>
      <td>LEI &lt;LEI&gt;</td>
      <td>[0..1]</td>
      <td>IdentifierSet</td>
      <td></td>
      <td>340</td>
    </tr>
    <tr>
      <td></td>
      <td>Other &lt;Othr&gt;</td>
      <td>[0..*]</td>
      <td></td>
      <td></td>
      <td>340</td>
    </tr>
    <tr>
      <td></td>
      <td>Identification &lt;Id&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td></td>
      <td>SchemaName &lt;SchmeNm&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Code &lt;Cd&gt;</td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Proprietary &lt;Ptry&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td></td>
      <td>Issuer &lt;Issr&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>PrivateIdentification &lt;PrvtId&gt;</td>
      <td>[1..1]</td>
      <td></td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td></td>
      <td>DateAndPlaceOfBirth &lt;DtAndPlcOfBirth&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>342</td>
    </tr>
    <tr>
      <td></td>
      <td>BirthDate &lt;BirthDt&gt;</td>
      <td>[1..1]</td>
      <td>Date</td>
      <td></td>
      <td>342</td>
    </tr>
    <tr>
      <td></td>
      <td>ProvinceOfBirth &lt;PrvcOfBirth&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>342</td>
    </tr>
    <tr>
      <td></td>
      <td>CityOfBirth &lt;CityOfBirth&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>CountryOfBirth &lt;CtryOfBirth&gt;</td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td>C7</td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>Other &lt;Othr&gt;</td>
      <td>[0..*]</td>
      <td></td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>Identification &lt;Id&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>SchemaName &lt;SchmeNm&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Code &lt;Cd&gt;</td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td></td>
      <td>344</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Proprietary &lt;Ptry&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>344</td>
    </tr>
    <tr>
      <td></td>
      <td>Issuer &lt;Issr&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>344</td>
    </tr>
    <tr>
      <td></td>
      <td>CountryOfResidence &lt;CtryOfRes&gt;</td>
      <td>[0..1]</td>
      <td>CodeSet</td>
      <td>C7</td>
      <td>344</td>
    </tr>
    <tr>
      <td></td>
      <td>ContactDetails &lt;CtctDtls&gt;</td>
      <td>[0..1]</td>
      <td>±</td>
      <td></td>
      <td>344</td>
    </tr>
  </tbody>
</table>

**5.4.2.18.5.1.4.3 OriginalCreditorAgent <OrgnlCdrAg>**

*Presence:* [0..1]

*Definition:* Original creditor agent that has been modified.

---

<!-- Page 277 -->

OriginalCreditorAgent `<OrgnlCddtrAgt>` contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on page 320 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | FinancialInstitutionIdentification `<FinInstlId>` | [1..1] | | | 321 |
| | BICFI `<BICFI>` | [0..1] | IdentifierSet | C6 | 321 |
| | ClearingSystemMemberIdentification `<ClrSysMmbId>` | [0..1] | ± | | 322 |
| | LEI `<LEI>` | [0..1] | IdentifierSet | | 322 |
| | Name `<Nm>` | [0..1] | Text | | 322 |
| | PostalAddress `<PstlAdr>` | [0..1] | ± | | 322 |
| | Other `<Othr>` | [0..1] | ± | | 323 |
| | BranchIdentification `<BrnchId>` | [0..1] | | | 324 |
| | Identification `<Id>` | [0..1] | Text | | 324 |
| | LEI `<LEI>` | [0..1] | IdentifierSet | | 324 |
| | Name `<Nm>` | [0..1] | Text | | 324 |
| | PostalAddress `<PstlAdr>` | [0..1] | ± | | 324 |

**5.4.2.18.5.1.4.4 OriginalCreditorAgentAccount `<OrgnlCddtrAgtAcc>`**

Presence: [0..1]

Definition: Original creditor agent account that has been modified.

Impacted by: C14 "IdentificationOrProxyPresenceRule", C13 "IdentificationAndProxyGuideline"

OriginalCreditorAgentAccount `<OrgnlCddtrAgtAcc>` contains the following elements (see "CashAccount40" on page 309 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | Identification `<Id>` | [0..1] | ± | | 310 |
| | Type `<Tp>` | [0..1] | ± | | 310 |
| | Currency `<Ccy>` | [0..1] | CodeSet | C2 | 310 |
| | Name `<Nm>` | [0..1] | Text | | 311 |
| | Proxy `<Prxy>` | [0..1] | ± | | 311 |

## Constraints

*   **IdentificationAndProxyGuideline**
    If the account identification is not defined through a conventional identification such as an email address or a mobile number, then the proxy element should be used for the identification of the account.

*   **IdentificationOrProxyPresenceRule**
    Identification must be present or Proxy must be present. Both may be present.

---

<!-- Page 278 -->

```
Following Must be True
    /Identification Must be present
    Or    /Proxy Must be present
```

**5.4.2.18.5.1.4.5 OriginalDebtor <OrgnlDbtr>**

*Presence:*[0..1]

*Definition:* Original debtor that has been modified.

---

<!-- Page 279 -->

OriginalDebtor <OrgnlDbtr> contains the following elements (see "PartyIdentification27" on page 336 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Name <Nm> | [0..1] | Text | | 337 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 338 |
| | Identification <Id> | [0..1] | | | 338 |
| (Or | OrganisationIdentification <OrgId> | [1..1] | | | 339 |
| | AnyBIC <AnyBIC> | [0..1] | IdentifierSet | C5 | 340 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 340 |
| | Other <Othr> | [0..*] | | | 340 |
| | Identification <Id> | [1..1] | Text | | 341 |
| | SchemeName <SchmeNm> | [0..1] | | | 341 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 341 |
| Or) | Proprietary <Prtry> | [1..1] | Text | | 341 |
| | Issuer <Issr> | [0..1] | Text | | 341 |
| (Or) | PrivateIdentification <PrvtId> | [1..1] | | | 341 |
| | DateAndPlaceOfBirth <DtAndPlcOfBirth> | [0..1] | | | 342 |
| | BirthDate <BirthDt> | [1..1] | Date | | 342 |
| | ProvinceOfBirth <PrvcOfBirth> | [0..1] | Text | | 342 |
| | CityOfBirth <CityOfBirth> | [1..1] | Text | | 343 |
| | CountryOfBirth <CtryOfBirth> | [1..1] | CodeSet | C7 | 343 |
| | Other <Othr> | [0..*] | | | 343 |
| | Identification <Id> | [1..1] | Text | | 343 |
| | SchemeName <SchmeNm> | [0..1] | | | 343 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 344 |
| Or) | Proprietary <Prtry> | [1..1] | Text | | 344 |
| | Issuer <Issr> | [0..1] | Text | | 344 |
| | CountryOfResidence <CtryOfRes> | [0..1] | CodeSet | C7 | 344 |
| | ContactDetails <CtctDtls> | [0..1] | ± | | 344 |

**5.4.2.18.5.1.4.6 OriginalDebtorAccount <OrgnlDbtrAcct>**

*Presence:* [0..1]

*Definition:* Original debtor account that has been modified.

*Impacted by:* C14 "IdentificationOrProxyPresenceRule", C13 "IdentificationAndProxyGuideline"

---

<!-- Page 280 -->

OriginalDebtorAccount <OrgnlDbtrAcct> contains the following elements (see "CashAccount40" on page 309 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Identification <Ids> | [0..1] | ± | | 310 |
| | Type <Tp> | [0..1] | ± | | 310 |
| | Currency <Ccy> | [0..1] | CodeSet | C2 | 310 |
| | Name <Nm> | [0..1] | Text | | 311 |
| | Proxy <Prxy> | [0..1] | ± | | 311 |

## Constraints

- **IdentificationAndProxyGuideline**

  If the account identification is not defined through a conventional identification such as an email address or a mobile number, then the proxy element should be used for the identification of the account.

- **IdentificationOrProxyPresenceRule**

  Identification must be present or Proxy must be present. Both may be present.

  ```
  Following Must be True
  /Identification Must be present
  Or
  /Proxy Must be present
  ```

**5.4.2.18.5.1.4.7 OriginalDebtorAgent <OrgnlDbtrAgt>**

*Presence:* [0..1]

*Definition:* Original debtor agent that has been modified.

---

<!-- Page 281 -->

OriginalDebtorAgent <OrgnlDbtrAgnt> contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on page 320 for details)



| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | FinancialInstitutionIdentification <FinInstlId> | [0..1] | | | 321 |
| | BICFI <BICFI> | | IdentifierSet | C6 | 321 |
| | ClearingSystemMemberIdentification <ClrSysMmbId> | [0..1] | ± | | 322 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 322 |
| | Name <Nm> | [0..1] | Text | | 322 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 322 |
| | Other <Othr> | [0..1] | ± | | 323 |
| | BranchIdentification <BrnchId> | [0..1] | | | 324 |
| | Identification <Id> | [0..1] | Text | | 324 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 324 |
| | Name <Nm> | [0..1] | Text | | 324 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 324 |

### 5.4.2.18.5.1.4.8 OriginalDebtorAgentAccount <OrgnlDbtrAgntAcct>

Presence: [0..1]

Definition: Original debtor agent account that has been modified.

Impacted by: C14 "IdentificationOrProxyPresenceRule", C13 "IdentificationAndProxyGuideline"

OriginalDebtorAgentAccount <OrgnlDbtrAgntAcct> contains the following elements (see "CashAccount40" on page 309 for details)



| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Identification <Id> | [0..1] | ± | | 310 |
| | Type <Tp> | [0..1] | ± | | 310 |
| | Currency <Ccy> | [0..1] | CodeSet | C2 | 310 |
| | Name <Nm> | [0..1] | Text | | 311 |
| | Proxy <Prxy> | [0..1] | ± | | 311 |

## Constraints

- **IdentificationAndProxyGuideline**

If the account identification is not defined through a conventional identification such as an email address or a mobile number, then the proxy element should be used for the identification of the account.

- **IdentificationOrProxyPresenceRule**

Identification must be present or Proxy must be present. Both may be present.

---

<!-- Page 282 -->

Following Must be True
/Identification Must be present
Or /Proxy Must be present

**5.4.2.18.5.1.4.9 OriginalFinalCollectionDate <OrgnlFnlCollnDt>**

*Presence:* [0..1]

*Definition:* Original final collection date that has been modified.

*DataType:* "ISODate" on page 425

**5.4.2.18.5.1.4.10 OriginalFrequency <OrgnlFrcy>**

*Presence:* [0..1]

*Definition:* Original frequency that has been modified.

**OriginalFrequency <OrgnlFrcy>** contains one of the following elements (see "Frequency36Choice" on page 326 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| Or | Type <Tp> | [1..1] | CodeSet | | 327 |
| Or | Period <Prd> | [1..1] | | | 327 |
| | Type <Tp> | [1..1] | CodeSet | | 328 |
| | CountPerPeriod <CntPerPrd> | [1..1] | Quantity | | 328 |
| Or | PointInTime <PtInTm> | [1..1] | | | 328 |
| | Type <Tp> | [1..1] | CodeSet | | 328 |
| | PointInTime <PtInTm> | [1..1] | Text | | 329 |

**5.4.2.18.5.1.4.11 OriginalReason <OrgnlRsn>**

*Presence:* [0..1]

*Definition:* Original reason for the mandate to allow the user to distinguish between different mandates for the same creditor.

**OriginalReason <OrgnlRsn>** contains one of the following **MandateSetupReason1Choice** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| Or | Code <Cd> | [1..1] | CodeSet | | 282 |
| Or) | Proprietary <Prtry> | [1..1] | Text | | 282 |

**5.4.2.18.5.1.4.11.1 Code <Cd>**

*Presence:* [1..1]

*Definition:* Reason for the mandate setup, as published in an external reason code list.

*DataType:* "ExternalMandateSetupReason1Code" on page 417

**5.4.2.18.5.1.4.11.2 Proprietary <Prtry>**

*Presence:* [1..1]

---

<!-- Page 283 -->

Definition: Reason for the mandate setup, in a proprietary form.
Datatype: "Max70Text" on page 431

## 5.4.2.18.5.1.42 OriginalTrackingDays <OrgnlTrckgDays>
Presence: [0..1]
Definition: Original number of tracking days that has been modified.
Datatype: "Exact2NumericText" on page 428

## 5.4.2.18.5.1.5 ElectronicSignature <ElctrncSgntr>
Presence: [0..1]
Definition: Additional security provisions, such as a digital signature, as provided by the debtor.
Datatype: "Max1025Text" on page 429

## 5.4.2.18.5.1.6 FirstCollectionDate <FstColltnDt>
Presence: [0..1]
Definition: Date of the first collection of a direct debit as per the mandate.
Datatype: "ISODate" on page 425

## 5.4.2.18.5.1.7 FinalCollectionDate <FnlColltnDt>
Presence: [0..1]
Definition: Date of the final collection of a direct debit as per the mandate.
Datatype: "ISODate" on page 425

## 5.4.2.18.5.1.8 Frequency <Frcqy>
Presence: [0..1]
Definition: Regularity with which direct debit instructions are to be created and processed.
**Frequency <Frcqy>** contains one of the following elements (see "Frequency36Choice" on page 326 for details)



| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| (Or | Type <Tp> | [1..1] | CodeSet | | 327 |
| Or | Period <Prd> | [1..1] | | | 327 |
| | Type <Tp> | [1..1] | CodeSet | | 328 |
| | CountPerPeriod <CntPerPrd> | [1..1] | Quantity | | 328 |
| Or) | PointInTime <PtInTm> | [1..1] | | | 328 |
| | Type <Tp> | [1..1] | CodeSet | | 328 |
| | PointInTime <PtInTm> | [1..1] | Text | | 329 |

## 5.4.2.18.5.1.9 Reason <Rsn>
Presence: [0..1]

---

<!-- Page 284 -->

*Definition:* Reason for the direct debit mandate to allow the user to distinguish between different mandates for the same creditor.

**Reason** <Rsn> contains one of the following **MandateSetupReason1Choice** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| (Or | **Code** <Cd> | [1..1] | CodeSet | | 284 |
| Or) | **Proprietary** <Ptry> | [1..1] | Text | | 284 |

**5.4.2.18.5.1.9.1 Code <Cd>**

*Presence:* [1..1]

*Definition:* Reason for the mandate setup, as published in an external reason code list.

*Datatype:* "ExternalMandateSetupReason1Code" on page 417

**5.4.2.18.5.1.9.2 Proprietary <Ptry>**

*Presence:* [1..1]

*Definition:* Reason for the mandate setup, in a proprietary form.

*Datatype:* "Max70Text" on page 431

**5.4.2.18.5.1.10 TrackingDays <TrckDays>**

*Presence:* [0..1]

*Definition:* Specifies the number of days the direct debit instruction must be tracked.

*Datatype:* "Exact2NumericText" on page 428

**5.4.2.18.5.2 CreditorSchemeIdentification <CdrSchmeId>**

*Presence:* [0..1]

*Definition:* Credit party that signs the mandate.

---

<!-- Page 285 -->

CreditorSchemeIdentification <CdtrSchmeId> contains the following elements (see "PartyIdentification27" on page 336 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Name <Nm> | [0..1] | Text | | 337 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 338 |
| | Identification <Id> | [0..1] | | | 338 |
| (Or | OrganisationIdentification <OrgId> | [1..1] | | | 339 |
| | AnyBIC <AnyBIC> | [0..1] | IdentifierSet | C5 | 340 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 340 |
| | Other <Othr> | [0..*] | | | 340 |
| | Identification <Id> | [1..1] | Text | | 341 |
| | SchemeName <SchmeNm> | [0..1] | | | 341 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 341 |
| Or) | Proprietary <Prtry> | [1..1] | Text | | 341 |
| | Issuer <Issr> | [0..1] | Text | | 341 |
| (Or) | PrivateIdentification <PrvtId> | [1..1] | | | 341 |
| | DateAndPlaceOfBirth <DtAndPlcOfBirth> | [0..1] | | | 342 |
| | BirthDate <BirthDt> | [1..1] | Date | | 342 |
| | ProvinceOfBirth <PrvcOfBirth> | [0..1] | Text | | 342 |
| | CityOfBirth <CityOfBirth> | [1..1] | Text | | 343 |
| | CountryOfBirth <CtryOfBirth> | [1..1] | CodeSet | C7 | 343 |
| | Other <Othr> | [0..*] | | | 343 |
| | Identification <Id> | [1..1] | Text | | 343 |
| | SchemeName <SchmeNm> | [0..1] | | | 343 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 344 |
| Or) | Proprietary <Prtry> | [1..1] | Text | | 344 |
| | Issuer <Issr> | [0..1] | Text | | 344 |
| | CountryOfResidence <CtryOfRes> | [0..1] | CodeSet | C7 | 344 |
| | ContactDetails <CtctDtls> | [0..1] | ± | | 344 |

**5.4.2.18.5.3 PreNotificationIdentification <PrNtfctnId>**
*Presence:* [0..1]
*Definition:* Unique and unambiguous identification of the pre-notification which is sent separately from the direct debit instruction.

---

<!-- Page 286 -->

Usage: The direct debit pre-notification is used to reconcile separately sent collection information with the direct debit transaction information.

*Datatype:* "Max35Text" on page 431

**5.4.2.18.5.4 PreNotificationDate <PreNtfctnDt>**

*Presence:* [0..1]

*Definition:* Date on which the creditor notifies the debtor about the amount and date on which the direct debit instruction will be presented to the debtor's agent.

*Datatype:* "ISODate" on page 425

**5.4.2.18.6 UltimateCreditor <UltmtCdr>**

*Presence:* [0..1]

*Definition:* Ultimate party to which an amount of money is due.

---

<!-- Page 287 -->

UltimateCreditor <UltmCtdr> contains the following elements (see "PartyIdentification272" on page 336 for details)

| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
| :--- | :--- | :--- | :--- | :--- | :--- |
| | Name <Nm> | [0..1] | Text | | 337 |
| | PostalAddress <PstlAdr> | ± | | | 338 |
| | Identification <Id> | [0..1] | | | 338 |
| (Or | OrganisationIdentification <OrgId> | [1..1] | | | 339 |
| | AnyBIC <AnyBIC> | [0..1] | IdentifierSet | C5 | 340 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 340 |
| | Other <Othr> | [0..*] | | | 340 |
| | Identification <Id> | [1..1] | Text | | 341 |
| | SchemeName <SchrmNm> | [0..1] | | | 341 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 341 |
| Or) | Proprietary <Prtry> | [1..1] | Text | | 341 |
| | Issuer <Issr> | [0..1] | Text | | 341 |
| (Or) | PrivateIdentification <PrvtId> | [1..1] | | | 341 |
| | DateAndPlaceOfBirth <DtAndPlcOfBrth> | [0..1] | | | 342 |
| | BirthDate <BirthDt> | [1..1] | Date | | 342 |
| | ProvinceOfBirth <PrvcOfBrth> | [0..1] | Text | | 342 |
| | CityOfBirth <CityOfBrth> | [1..1] | Text | | 343 |
| | CountryOfBirth <CtryOfBrth> | [1..1] | CodeSet | C7 | 343 |
| | Other <Othr> | [0..*] | | | 343 |
| | Identification <Id> | [1..1] | Text | | 343 |
| | SchemeName <SchrmNm> | [0..1] | | | 343 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 344 |
| Or) | Proprietary <Prtry> | [1..1] | Text | | 344 |
| | Issuer <Issr> | [0..1] | Text | | 344 |
| | CountryOfResidence <CtryOfRes> | [0..1] | CodeSet | C7 | 344 |
| | ContactDetails <CtctDtls> | [0..1] | ± | | 344 |

**5.4.2.18.7 DebtorAgent <DbtrAg>**

*Presence: [1..1]*

*Definition: Financial institution servicing an account for the debtor.*

---

<!-- Page 288 -->

**Debtor Agent** *<DbtrAgt>* contains the following elements (see "BranchAndFinancialInstitutionIdentification8" on page 320 for details)



<table>
  <tr>
    <th>Or</th>
    <th>MessageElement&lt;XML Tag&gt;</th>
    <th>Mult.</th>
    <th>Type</th>
    <th>Constr. No.</th>
    <th>Page</th>
  </tr>
  <tr>
    <td></td>
    <td>FinancialInstitutionIdentification &lt;FinInstId&gt;</td>
    <td>[1..1]</td>
    <td></td>
    <td></td>
    <td>321</td>
  </tr>
  <tr>
    <td></td>
    <td>BICFI &lt;BICFI&gt;</td>
    <td>[0..1]</td>
    <td>IdentifierSet</td>
    <td>C6</td>
    <td></td>
  </tr>
  <tr>
    <td></td>
    <td>ClearingSystemMemberIdentification &lt;ClrSysMmbId&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>322</td>
  </tr>
  <tr>
    <td></td>
    <td>LEI &lt;LEI&gt;</td>
    <td>[0..1]</td>
    <td>IdentifierSet</td>
    <td></td>
    <td>322</td>
  </tr>
  <tr>
    <td></td>
    <td>Name &lt;Nm&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>322</td>
  </tr>
  <tr>
    <td></td>
    <td>PostalAddress &lt;PstlAdr&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>322</td>
  </tr>
  <tr>
    <td></td>
    <td>Other &lt;Othr&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>323</td>
  </tr>
  <tr>
    <td></td>
    <td>BranchIdentification &lt;BrnchId&gt;</td>
    <td>[0..1]</td>
    <td></td>
    <td></td>
    <td>324</td>
  </tr>
  <tr>
    <td></td>
    <td>Identification &lt;Id&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>324</td>
  </tr>
  <tr>
    <td></td>
    <td>LEI &lt;LEI&gt;</td>
    <td>[0..1]</td>
    <td>IdentifierSet</td>
    <td></td>
    <td>324</td>
  </tr>
  <tr>
    <td></td>
    <td>Name &lt;Nm&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>324</td>
  </tr>
  <tr>
    <td></td>
    <td>PostalAddress &lt;PstlAdr&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>324</td>
  </tr>
</table>

### 5.4.2.18.8 **DebtorAgentAccount** *<DbtrAgtAcct>*

**Presence:** [0..1]

*Definition:* Unambiguous identification of the account of the debtor agent at its servicing agent in the payment chain.

*Impacted by:* C14 "IdentificationOrProxyPresenceRule", C13 "IdentificationAndProxyGuideline"

**DebtorAgentAccount** *<DbtrAgtAcct>* contains the following elements (see "CashAccount40" on page 309 for details)



<table>
  <tr>
    <th>Or</th>
    <th>MessageElement&lt;XML Tag&gt;</th>
    <th>Mult.</th>
    <th>Type</th>
    <th>Constr. No.</th>
    <th>Page</th>
  </tr>
  <tr>
    <td></td>
    <td>Identification &lt;Id&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>310</td>
  </tr>
  <tr>
    <td></td>
    <td>Type &lt;Tp&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>310</td>
  </tr>
  <tr>
    <td></td>
    <td>Currency &lt;Ccy&gt;</td>
    <td>[0..1]</td>
    <td>CodeSet</td>
    <td>C2</td>
    <td>310</td>
  </tr>
  <tr>
    <td></td>
    <td>Name &lt;Nm&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>311</td>
  </tr>
  <tr>
    <td></td>
    <td>Proxy &lt;Prxy&gt;</td>
    <td>[0..1]</td>
    <td>±</td>
    <td></td>
    <td>311</td>
  </tr>
</table>

---

<!-- Page 289 -->

Constraints

* **IdentificationAndProxyGuideline**

If the account identification is not defined through a conventional identification such as an email address or a mobile number, then the proxy element should be used for the identification of the account.

* **IdentificationOrProxyPresenceRule**

Identification must be present or Proxy must be present. Both may be present.

```
Following Must be True
    /Identification Must be present
    Or      /Proxy Must be present
```

**5.4.2.18.9 Debtor <Dbtr>**

*Presence:* [1..1]

*Definition:* Party that owes an amount of money to the (ultimate) creditor.

---

<!-- Page 290 -->

Debtor <Dbtr> contains the following elements (see "PartyIdentification272" on page 336 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Name <Nm> | [0..1] | Text | | 337 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 338 |
| | Identification <Id> | [0..1] | | | 338 |
| Or | OrganisationIdentification <OrgId> | [1..1] | | | 339 |
| | AnyBIC <AnyBIC> | [0..1] | IdentifierSet | C5 | 340 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 340 |
| | Other <Othr> | [0.*] | | | 340 |
| | Identification <Id> | [1..1] | Text | | 341 |
| | SchemeName <SchmeNm> | [0..1] | | | 341 |
| Or | Code <Cd> | [1..1] | CodeSet | | 341 |
| Or | Proprietary <Prtry> | [1..1] | Text | | 341 |
| | Issuer <Issr> | [0..1] | Text | | 341 |
| Or | PrivateIdentification <PrvtId> | [1..1] | | | 341 |
| | DateAndPlaceOfBirth <DtAndPlcOfBirth> | [0..1] | | | 342 |
| | BirthDate <BirthDt> | [1..1] | Date | | 342 |
| | ProvinceOfBirth <PrvcOfBirth> | [0..1] | Text | | 342 |
| | CityOfBirth <CityOfBirth> | [1..1] | Text | | 343 |
| | CountryOfBirth <CtryOfBirth> | [1..1] | CodeSet | C7 | 343 |
| | Other <Othr> | [0.*] | | | 343 |
| | Identification <Id> | [1..1] | Text | | 343 |
| | SchemeName <SchmeNm> | [0..1] | | | 343 |
| Or | Code <Cd> | [1..1] | CodeSet | | 344 |
| Or | Proprietary <Prtry> | [1..1] | Text | | 344 |
| | Issuer <Issr> | [0..1] | Text | | 344 |
| | CountryOfResidence <CtryOfRes> | [0..1] | CodeSet | C7 | 344 |
| | ContactDetails <CtctDtls> | [0..1] | ± | | 344 |

### 5.4.2.18.10 DebtorAccount <DbtrAcct>

Presence: [1..1]

Definition: Unambiguous identification of the account of the debtor to which a debit entry will be made as a result of the transaction.

Impacted by: C14 "IdentificationOrProxyPresenceRule", C13 "IdentificationAndProxyGuideline"

---

<!-- Page 291 -->

DebtorAccount <DbtrAcct> contains the following elements (see "CashAccount40" on page 309 for details)



<table>
  <thead>
    <tr>
      <th>Or</th>
      <th>MessageElement&lt;XML Tag&gt;</th>
      <th>Mult.</th>
      <th>Type</th>
      <th>Constr. No.</th>
      <th>Page</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td>Identification &lt;Ids&gt;</td>
      <td>[0..1]</td>
      <td>±</td>
      <td></td>
      <td>310</td>
    </tr>
    <tr>
      <td></td>
      <td>Type &lt;Tp&gt;</td>
      <td>[0..1]</td>
      <td>±</td>
      <td></td>
      <td>310</td>
    </tr>
    <tr>
      <td></td>
      <td>Currency &lt;Ccy&gt;</td>
      <td>[0..1]</td>
      <td>CodeSet</td>
      <td>C2</td>
      <td>310</td>
    </tr>
    <tr>
      <td></td>
      <td>Name &lt;Nm&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>311</td>
    </tr>
    <tr>
      <td></td>
      <td>Proxy &lt;Prxy&gt;</td>
      <td>[0..1]</td>
      <td>±</td>
      <td></td>
      <td>311</td>
    </tr>
  </tbody>
</table>

## Constraints

- **IdentificationAndProxyGuideline**

  If the account identification is not defined through a conventional identification such as an email address or a mobile number, then the proxy element should be used for the identification of the account.

- **IdentificationOrProxyPresenceRule**

  Identification must be present or Proxy must be present. Both may be present.

  ```
  Following Must be True
  /Identification Must be present
  Or      /Proxy Must be present
  ```

## 5.4.2.18.11 UltimateDebtor <UltmtDbtr>

*Presence: [0..1]*

*Definition: Ultimate party that owes an amount of money to the (ultimate) creditor.*

---

<!-- Page 292 -->

UltimateDebtor <UltmDbtr> contains the following elements (see 'PartyIdentification27' on page 336 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Name <Nm> | [0..1] | Text | | 337 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 338 |
| | Identification <Id> | [0..1] | | | 338 |
| (Or | OrganisationIdentification <OrgId> | [1..1] | | | 339 |
| | AnyBIC <AnyBIC> | [0..1] | IdentifierSet | C5 | 340 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 340 |
| | Other <Othr> | [0..*] | | | 340 |
| | Identification <Id> | [1..1] | Text | | 341 |
| | SchemeName <SchrmNm> | [0..1] | | | 341 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 341 |
| Or) | Proprietary <Prtry> | [1..1] | Text | | 341 |
| | Issuer <Issr> | [0..1] | Text | | 341 |
| (Or) | PrivateIdentification <PrvtId> | [1..1] | | | 341 |
| | DateAndPlaceOfBirth <DtAndPlcOfBirth> | [0..1] | | | 342 |
| | BirthDate <BirthDt> | [1..1] | Date | | 342 |
| | ProvinceOfBirth <PrvcOfBirth> | [0..1] | Text | | 342 |
| | CityOfBirth <CityOfBirth> | [1..1] | Text | | 343 |
| | CountryOfBirth <CtryOfBirth> | [1..1] | CodeSet | C7 | 343 |
| | Other <Othr> | [0..*] | | | 343 |
| | Identification <Id> | [1..1] | Text | | 343 |
| | SchemeName <SchrmNm> | [0..1] | | | 343 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 344 |
| Or) | Proprietary <Prtry> | [1..1] | Text | | 344 |
| | Issuer <Issr> | [0..1] | Text | | 344 |
| | CountryOfResidence <CtryOfRes> | [0..1] | CodeSet | C7 | 344 |
| | ContactDetails <CtctDtls> | [0..1] | ± | | 344 |

**5.4.2.18.12 InstructionForCreditorAgent <InstrForCddrAgt>**

*Presence: [0..1]*

*Definition: Further information, related to the processing of the payment instruction, that may need to be acted upon by the creditor agent, depending on agreement between creditor and the creditor agent.*

---

<!-- Page 293 -->

Datatype: "Max140Text" on page 429

## 5.4.2.18.13 Purpose <Purp>

Presence: [0..1]

Definition: Underlying reason for the payment transaction.

Usage: Purpose is used by the end-customers, that is initiating party, (ultimate) debtor, (ultimate) creditor to provide information concerning the nature of the payment. Purpose is a content element, which is not used for processing by any of the agents involved in the payment chain.

**Purpose <Purp>** contains one of the following elements (see "Purpose2Choice" on page 334 for details)



<table>
  <tr>
    <th>Or</th>
    <th>MessageElement&lt;XML Tag&gt;</th>
    <th>Mult.</th>
    <th>Type</th>
    <th>Constr. No.</th>
    <th>Page</th>
  </tr>
  <tr>
    <td>Or</td>
    <td>Code &lt;Cd&gt;</td>
    <td>[1..1]</td>
    <td>CodeSet</td>
    <td></td>
    <td>335</td>
  </tr>
  <tr>
    <td>Or</td>
    <td>Proprietary &lt;Prtry&gt;</td>
    <td>[1..1]</td>
    <td>Text</td>
    <td></td>
    <td>335</td>
  </tr>
</table>

## 5.4.2.18.14 RegulatoryReporting <RgltryRptg>

Presence: [0..10]

Definition: Information needed due to regulatory and statutory requirements.

**RegulatoryReporting <RgltryRptg>** contains the following elements (see "RegulatoryReporting3" on page 361 for details)



<table>
  <tr>
    <th>Or</th>
    <th>MessageElement&lt;XML Tag&gt;</th>
    <th>Mult.</th>
    <th>Type</th>
    <th>Constr. No.</th>
    <th>Page</th>
  </tr>
  <tr>
    <td></td>
    <td>DebitCreditReportingIndicator &lt;DbtCdtRptgInd&gt;</td>
    <td>[0..1]</td>
    <td>CodeSet</td>
    <td></td>
    <td>361</td>
  </tr>
  <tr>
    <td></td>
    <td>Authority &lt;Authry&gt;</td>
    <td>[0..1]</td>
    <td></td>
    <td></td>
    <td>361</td>
  </tr>
  <tr>
    <td></td>
    <td>Name &lt;Nm&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>362</td>
  </tr>
  <tr>
    <td></td>
    <td>Country &lt;Ctry&gt;</td>
    <td>[0..1]</td>
    <td>CodeSet</td>
    <td>C7</td>
    <td>362</td>
  </tr>
  <tr>
    <td></td>
    <td>Details &lt;Dtls&gt;</td>
    <td>[0..*]</td>
    <td></td>
    <td></td>
    <td>362</td>
  </tr>
  <tr>
    <td></td>
    <td>Type &lt;Tp&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>362</td>
  </tr>
  <tr>
    <td></td>
    <td>Date &lt;Dt&gt;</td>
    <td>[0..1]</td>
    <td>Date</td>
    <td></td>
    <td>363</td>
  </tr>
  <tr>
    <td></td>
    <td>Country &lt;Ctry&gt;</td>
    <td>[0..1]</td>
    <td>CodeSet</td>
    <td>C7</td>
    <td>363</td>
  </tr>
  <tr>
    <td></td>
    <td>Code &lt;Cd&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>363</td>
  </tr>
  <tr>
    <td></td>
    <td>Amount &lt;Amt&gt;</td>
    <td>[0..1]</td>
    <td>Amount</td>
    <td>C2, C8</td>
    <td>363</td>
  </tr>
  <tr>
    <td></td>
    <td>Information &lt;Inf&gt;</td>
    <td>[0..*]</td>
    <td>Text</td>
    <td></td>
    <td>363</td>
  </tr>
</table>

## 5.4.2.18.15 Tax <Tax>

Presence: [0..1]

Definition: Provides details on the tax.

---

<!-- Page 294 -->

Tax <Tax> contains the following TaxData1 elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Creditor <CdtItr> | [0..1] | ± | | 295 |
| | Debtor <Dbtr> | [0..1] | ± | | 295 |
| | UltimateDebtor <UltmtDbtr> | [0..1] | ± | | 295 |
| | AdministrationZone <AdminstrZone> | [0..1] | Text | | 296 |
| | ReferenceNumber <RefNb> | [0..1] | Text | | 296 |
| | Method <Mtd> | [0..1] | Text | | 296 |
| | TotalTaxableBaseAmount <TtlTaxblBaseAmt> | [0..1] | Amount | C1, C11 | 296 |
| | TotalTaxAmount <TtlTaxAmt> | [0..1] | Amount | C1, C11 | 297 |
| | Date <Dt> | [0..1] | Date | | 297 |
| | SequenceNumber <SeqNb> | [0..1] | Quantity | | 297 |
| | Record <Rcrd> | [0.*] | | | 297 |
| | Type <Tp> | [0..1] | Text | | 298 |
| | Category <Ctgy> | [0..1] | Text | | 298 |
| | CategoryDetails <CtgyDtls> | [0..1] | Text | | 298 |
| | DebtorStatus <DbtrSts> | [0..1] | Text | | 299 |
| | CertificateIdentification <CertId> | [0..1] | Text | | 299 |
| | FormsCode <FrmsCds> | [0..1] | Text | | 299 |
| | Period <Prd> | [0..1] | | | 299 |
| | Year <Yr> | [0..1] | Year | | 299 |
| | Type <Tp> | [0..1] | CodeSet | | 299 |
| | FromToDate <FrToDt> | [0..1] | ± | | 300 |
| | TaxAmount <TaxAmt> | [0..1] | | | 301 |
| | Rate <Rate> | [0..1] | Rate | | 301 |
| | TaxableBaseAmount <TaxblBaseAmt> | [0..1] | Amount | C1, C11 | 301 |
| | TotalAmount <TtlAmt> | [0..1] | Amount | C1, C11 | 301 |
| | Details <Dtls> | [0.*] | | | 302 |
| | Period <Prd> | [0..1] | | | 302 |
| | Year <Yr> | [0..1] | Year | | 302 |
| | Type <Tp> | [0..1] | CodeSet | | 303 |
| | FromToDate <FrToDt> | [0..1] | ± | | 303 |
| | Amount <Amt> | [1..1] | Amount | C1, C11 | 304 |

---

<!-- Page 295 -->

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | AdditionalInformation <AddtlInf> | [0..1] | Text | | 304 |

## 5.4.2.18.15.1 Creditor <Cdrtr>

*Presence: [0..1]*

*Definition: Party on the credit side of the transaction to which the tax applies.*

**Creditor <Cdrtr>** contains the following elements (see "TaxParty1" on page 405 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | TaxIdentification <TaxId> | [0..1] | Text | | 405 |
| | RegistrationIdentification <RegnId> | [0..1] | Text | | 405 |
| | TaxType <TaxTp> | [0..1] | Text | | 406 |

## 5.4.2.18.15.2 Debtor <Dbtr>

*Presence: [0..1]*

*Definition: Party on the debit side of the transaction to which the tax applies.*

**Debtor <Dbtr>** contains the following elements (see "TaxParty2" on page 406 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | TaxIdentification <TaxId> | [0..1] | Text | | 406 |
| | RegistrationIdentification <RegnId> | [0..1] | Text | | 406 |
| | TaxType <TaxTp> | [0..1] | Text | | 406 |
| | Authorisation <AuthStr> | [0..1] |  | | 406 |
| | Title <Title> | [0..1] | Text | | 407 |
| | Name <Nm> | [0..1] | Text | | 407 |

## 5.4.2.18.15.3 UltimateDebtor <UltmtDbtr>

*Presence: [0..1]*

*Definition: Ultimate party that owes an amount of money to the (ultimate) creditor, in this case, to the taxing authority.*

---

<!-- Page 296 -->

UltimateDebtor <UltimateDbtr> contains the following elements (see "TaxParty2" on page 406 for details)



| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | TaxIdentification <TaxId> | [0..1] | Text | | 406 |
| | RegistrationIdentification <RegnId> | [0..1] | Text | | 406 |
| | TaxType <TaxTp> | [0..1] | Text | | 406 |
| | Authorisation <Authstr> | [0..1] | | | 406 |
| | Title <Title> | [0..1] | Text | | 407 |
| | Name <Nm> | [0..1] | Text | | 407 |

**5.4.2.18.15.4 AdministrationZone <AdminZone>**

*Presence:* [0..1]

*Definition:* Territorial part of a country to which the tax payment is related.

*Datatype:* "Max35Text" on page 431

**5.4.2.18.15.5 ReferenceNumber <RefNb>**

*Presence:* [0..1]

*Definition:* Tax reference information that is specific to a taxing agency.

*Datatype:* "Max140Text" on page 429

**5.4.2.18.15.6 Method <Mtd>**

*Presence:* [0..1]

*Definition:* Method used to indicate the underlying business or how the tax is paid.

*Datatype:* "Max35Text" on page 431

**5.4.2.18.15.7 TotalTaxableBaseAmount <TtlTaxblBaseAmt>**

*Presence:* [0..1]

*Definition:* Total amount of money on which the tax is based.

*Impacted by:* C1 "ActiveOrHistoricCurrency", C11 "CurrencyAmount"

*Datatype:* "ActiveOrHistoricCurrencyAndAmount" on page 407

Constraints

- **ActiveOrHistoricCurrency**

The Currency Code must be registered, or have already been registered. Valid active or historic currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and may be or not be withdrawn on the day the message containing the Currency is exchanged.

- **CurrencyAmount**

The number of fractional digits (or minor unit of currency) must comply with ISO 4217.

---

<!-- Page 297 -->

Note: The decimal separator is a dot.

**5.4.2.18.15.8 TotalTaxAmount <TlTaxAm>**

*Presence:* [0..1]

*Definition:* Total amount of money as result of the calculation of the tax.

*Impacted by:* C1 "ActiveOrHistoricCurrency", C11 "CurrencyAmount"

*Datatype:* "ActiveOrHistoricCurrencyAndAmount" on page 407

**Constraints**

* **ActiveOrHistoricCurrency**

The Currency Code must be registered, or have already been registered. Valid active or historic currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and may be or not be withdrawn on the day the message containing the Currency is exchanged.

* **CurrencyAmount**

The number of fractional digits (or minor unit of currency) must comply with ISO 4217.

Note: The decimal separator is a dot.

**5.4.2.18.15.9 Date <Dt>**

*Presence:* [0..1]

*Definition:* Date by which tax is due.

*Datatype:* "ISODate" on page 425

**5.4.2.18.15.10 SequenceNumber <SeqNb>**

*Presence:* [0..1]

*Definition:* Sequential number of the tax report.

*Datatype:* "Number" on page 427

**5.4.2.18.15.11 Record <Rcrd>**

*Presence:* [0..*]

*Definition:* Record of tax details.

---

<!-- Page 298 -->

Record `<Rcrd>` contains the following **TaxRecord3** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | **Type** `<Tp>` | [0..1] | Text | | 298 |
| | **Category** `<Ctgy>` | [0..1] | Text | | 298 |
| | **CategoryDetails** `<CtgyDtls>` | [0..1] | Text | | 298 |
| | **DebtorStatus** `<DbtrSts>` | [0..1] | Text | | 299 |
| | **CertificateIdentification** `<CertId>` | [0..1] | Text | | 299 |
| | **FormsCode** `<FrmsCd>` | [0..1] | Text | | 299 |
| | **Period** `<Prd>` | [0..1] | | | 299 |
| | **Year** `<Yr>` | [0..1] | Year | | 299 |
| | **Type** `<Tp>` | [0..1] | CodeSet | | 299 |
| | **FromToDate** `<FrToDt>` | [0..1] | ± | | 300 |
| | **TaxAmount** `<TaxAmt>` | [0..1] | | | 301 |
| | **Rate** `<Rate>` | [0..1] | Rate | | 301 |
| | **TaxableBaseAmount** `<TaxblBaseAmt>` | [0..1] | Amount | C1, C11 | 301 |
| | **TotalAmount** `<TtlAmt>` | [0..1] | Amount | C1, C11 | 301 |
| | **Details** `<Dtls>` | [0.*] | | | 302 |
| | **Period** `<Prd>` | [0..1] | | | 302 |
| | **Year** `<Yr>` | [0..1] | Year | | 302 |
| | **Type** `<Tp>` | [0..1] | CodeSet | | 303 |
| | **FromToDate** `<FrToDt>` | [0..1] | ± | | 303 |
| | **Amount** `<Amt>` | [1..1] | Amount | C1, C11 | 304 |
| | **AdditionalInformation** `<AddtlInf>` | [0..1] | Text | | 304 |

**5.4.2.18.15.11.1 Type `<Tp>`**

*Presence:* [0..1]

*Definition:* High level code to identify the type of tax details.

*Datatype:* "Max35Text" on page 431

**5.4.2.18.15.11.2 Category `<Ctgy>`**

*Presence:* [0..1]

*Definition:* Specifies the tax code as published by the tax authority.

*Datatype:* "Max35Text" on page 431

**5.4.2.18.15.11.3 CategoryDetails `<CtgyDtls>`**

*Presence:* [0..1]

---

<!-- Page 299 -->

Definition: Provides further details of the category tax code.
Datatype: "Max35Text" on page 431

**5.4.2.18.15.11.4 DebtorStatus <DbtrSts>**
*Presence:* [0..1]
*Definition:* Code provided by local authority to identify the status of the party that has drawn up the settlement document.
*Datatype:* "Max35Text" on page 431

**5.4.2.18.15.11.5 CertificateIdentification <CertId>**
*Presence:* [0..1]
*Definition:* Identification number of the tax report as assigned by the taxing authority.
*Datatype:* "Max35Text" on page 431

**5.4.2.18.15.11.6 FormsCode <FrmsCd>**
*Presence:* [0..1]
*Definition:* Identifies, in a coded form, on which template the tax report is to be provided.
*Datatype:* "Max35Text" on page 431

**5.4.2.18.15.11.7 Period <Prd>**
*Presence:* [0..1]
*Definition:* Set of elements used to provide details on the period of time related to the tax payment.
**Period <Prd>** contains the following **TaxPeriod3** elements

| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | Year <Yr> | [0..1] | Year | | 299 |
| | Type <Tp> | [0..1] | CodeSet | | 299 |
| | FromToDate <FrToDt> | [0..1] | ± | | 300 |

**5.4.2.18.15.11.7.1 Year <Yr>**
*Presence:* [0..1]
*Definition:* Year related to the tax payment.
*Datatype:* "ISOYear" on page 432

**5.4.2.18.15.11.7.2 Type <Tp>**
*Presence:* [0..1]
*Definition:* Identification of the period related to the tax payment.
*Datatype:* "TaxRecordPeriod1Code" on page 424

| CodeName | Name | Definition |
|:---|:---|:---|
| MM01 | FirstMonth | Tax is related to the second month of the period. |

---

<!-- Page 300 -->

| CodeName | Name | Definition |
|---|---|---|
| MM02 | SecondMonth | Tax is related to the first month of the period. |
| MM03 | ThirdMonth | Tax is related to the third month of the period. |
| MM04 | FourthMonth | Tax is related to the fourth month of the period. |
| MM05 | FifthMonth | Tax is related to the fifth month of the period. |
| MM06 | SixthMonth | Tax is related to the sixth month of the period. |
| MM07 | SeventhMonth | Tax is related to the seventh month of the period. |
| MM08 | EighthMonth | Tax is related to the eighth month of the period. |
| MM09 | NinthMonth | Tax is related to the ninth month of the period. |
| MM10 | TenthMonth | Tax is related to the tenth month of the period. |
| MM11 | EleventhMonth | Tax is related to the eleventh month of the period. |
| MM12 | TwelfthMonth | Tax is related to the twelfth month of the period. |
| QTR1 | FirstQuarter | Tax is related to the first quarter of the period. |
| QTR2 | SecondQuarter | Tax is related to the second quarter of the period. |
| QTR3 | ThirdQuarter | Tax is related to the third quarter of the period. |
| QTR4 | FourthQuarter | Tax is related to the forth quarter of the period. |
| HLF1 | FirstHalf | Tax is related to the first half of the period. |
| HLF2 | SecondHalf | Tax is related to the second half of the period. |

**5.4.2.18.15.11.7.3 FromToDate <FrToDt>**

*Presence:* [0..1]

*Definition:* Range of time between a start date and an end date for which the tax report is provided.

FromToDate <FrToDt> contains the following elements (see "DatePeriod2" on page 316 for details)

| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | FromDate <FrDt> | [1..1] | Date |  | 316 |
| | ToDate <ToDt> | [1..1] | Date |  | 316 |

---

<!-- Page 301 -->

5.4.2.18.15.11.8 TaxAmount <TaxAmt>

*Presence: [0..1]*

*Definition: Set of elements used to provide information on the amount of the tax record.*

**TaxAmount <TaxAmt>** contains the following **TaxAmount3** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | **Rate** <Rate> | [0..1] | Rate | | 301 |
| | **TaxableBaseAmount** <TaxblBaseAmt> | [0..1] | Amount | C1, C11 | 301 |
| | **TotalAmount** <TtlAmt> | [0..1] | Amount | C1, C11 | 301 |
| | **Details** <Dtls> | [0..*] | | | 302 |
| | **Period** <Prd> | [0..1] | | | 302 |
| | **Year** <Yr> | [0..1] | Year | | 302 |
| | **Type** <Tp> | [0..1] | CodeSet | | 303 |
| | **FromToDate** <FrToDt> | [0..1] | ± | | 303 |
| | **Amount** <Amt> | [1..1] | Amount | C1, C11 | 304 |

5.4.2.18.15.11.8.1 Rate <Rate>

*Presence: [0..1]*

*Definition: Rate used to calculate the tax.*

*Datatype: "PercentageRate" on page 428*

5.4.2.18.15.11.8.2 TaxableBaseAmount <TaxblBaseAmt>

*Presence: [0..1]*

*Definition: Amount of money on which the tax is based.*

*Impacted by: C1 "ActiveOrHistoricCurrency", C11 "CurrencyAmount"*

*Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 407*

**Constraints**

*   **ActiveOrHistoricCurrency**

    The Currency Code must be registered, or have already been registered. Valid active or historic currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and may be or not be withdrawn on the day the message containing the Currency is exchanged.

*   **CurrencyAmount**

    The number of fractional digits (or minor unit of currency) must comply with ISO 4217.

    Note: The decimal separator is a dot.

5.4.2.18.15.11.8.3 TotalAmount <TtlAmt>

*Presence: [0..1]*

---

<!-- Page 302 -->

*Definition: Total amount that is the result of the calculation of the tax for the record.*

*Impacted by: C1 "ActiveOrHistoricCurrency", C11 "CurrencyAmount"*

*Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 407*

## Constraints

- **ActiveOrHistoricCurrency**

The Currency Code must be registered, or have already been registered. Valid active or historic currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and may be or not be withdrawn on the day the message containing the Currency is exchanged.

- **CurrencyAmount**

The number of fractional digits (or minor unit of currency) must comply with ISO 4217.

Note: The decimal separator is a dot.

## 5.4.2.18.15.11.8.4 Details <Dtls>

*Presence: [0..*]*

*Definition: Set of elements used to provide details on the tax period and amount.*

**Details <Dtls>** contains the following **TaxRecordDetails3** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Period <Prd> | [0..1] |  |  | 302 |
| | Year <Yr> | [0..1] | Year |  | 302 |
| | Type <Tp> | [0..1] | CodeSet |  | 303 |
| | FromToDate <FrToDt> | [0..1] | ± |  | 303 |
| | Amount <Amt> | [1..1] | Amount | C1, C11 | 304 |

## 5.4.2.18.15.11.8.4.1 Period <Prd>

*Presence: [0..1]*

*Definition: Set of elements used to provide details on the period of time related to the tax payment.*

**Period <Prd>** contains the following **TaxPeriod3** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Year <Yr> | [0..1] | Year |  | 302 |
| | Type <Tp> | [0..1] | CodeSet |  | 303 |
| | FromToDate <FrToDt> | [0..1] | ± |  | 303 |

## 5.4.2.18.15.11.8.4.1.1 Year <Yr>

*Presence: [0..1]*

*Definition: Year related to the tax payment.*

---

<!-- Page 303 -->

*Datatype:* "ISOYear" on page 432

**5.4.2.18.15.11.8.4.1.2 Type <Tp>**

*Presence:* [0..1]

*Definition:* Identification of the period related to the tax payment.

*Datatype:* "TaxRecordPeriod1Code" on page 424



| CodeName | Name | Definition |
| :--- | :--- | :--- |
| MM01 | FirstMonth | Tax is related to the second month of the period. |
| MM02 | SecondMonth | Tax is related to the first month of the period. |
| MM03 | ThirdMonth | Tax is related to the third month of the period. |
| MM04 | FourthMonth | Tax is related to the fourth month of the period. |
| MM05 | FifthMonth | Tax is related to the fifth month of the period. |
| MM06 | SixthMonth | Tax is related to the sixth month of the period. |
| MM07 | SeventhMonth | Tax is related to the seventh month of the period. |
| MM08 | EighthMonth | Tax is related to the eighth month of the period. |
| MM09 | NinthMonth | Tax is related to the ninth month of the period. |
| MM10 | TenthMonth | Tax is related to the tenth month of the period. |
| MM11 | EleventhMonth | Tax is related to the eleventh month of the period. |
| MM12 | TwelfthMonth | Tax is related to the twelfth month of the period. |
| QTR1 | FirstQuarter | Tax is related to the first quarter of the period. |
| QTR2 | SecondQuarter | Tax is related to the second quarter of the period. |
| QTR3 | ThirdQuarter | Tax is related to the third quarter of the period. |
| QTR4 | FourthQuarter | Tax is related to the forth quarter of the period. |
| HLF1 | FirstHalf | Tax is related to the first half of the period. |
| HLF2 | SecondHalf | Tax is related to the second half of the period. |

**5.4.2.18.15.11.8.4.1.3 FromToDate <FrToDt>**

*Presence:* [0..1]

---

<!-- Page 304 -->

*Definition:* Range of time between a start date and an end date for which the tax report is provided.

**FromToDate <FrToDt>** contains the following elements (see "DatePeriod2" on page 316 for details)



<table><tr><td>Or</td><td>MessageElement&lt;XML Tag&gt;</td><td>Mult.</td><td>Type</td><td>Constr. No.</td><td>Page</td></tr><tr><td></td><td>FromDate &lt;FrDt&gt;</td><td>[1..1]</td><td>Date</td><td></td><td>316</td></tr><tr><td></td><td>ToDate &lt;ToDt&gt;</td><td>[1..1]</td><td>Date</td><td></td><td>316</td></tr></table>

## 5.4.2.18.15.11.8.4.2 Amount <Amt>

*Presence:* [1..1]

*Definition:* Underlying tax amount related to the specified period.

*Impacted by:* C1 "ActiveOrHistoricCurrency", C11 "CurrencyAmount"

*Datatype:* "ActiveOrHistoricCurrencyAndAmount" on page 407

**Constraints**

- **ActiveOrHistoricCurrency**

The Currency Code must be registered, or have already been registered. Valid active or historic currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and may be or not be withdrawn on the day the message containing the Currency is exchanged.

- **CurrencyAmount**

The number of fractional digits (or minor unit of currency) must comply with ISO 4217.

Note: The decimal separator is a dot.

## 5.4.2.18.15.11.9 AdditionalInformation <AddtlInf>

*Presence:* [0..1]

*Definition:* Further details of the tax record.

*Datatype:* "Max140Text" on page 429

## 5.4.2.18.16 RelatedRemittanceInformation <RltdRmtInf>

*Presence:* [0..10]

*Definition:* Provides information related to the handling of the remittance information by any of the agents in the transaction processing chain.

---

<!-- Page 305 -->

RelatedRemittanceInformation <RltdRmInf> contains the following RemittanceLocation8 elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | RemittanceIdentification <RmtId> | [0..1] | Text | | 305 |
| | RemittanceLocationDetails <RmtLctnDtls> | [0..*] | | | 305 |
| | Method <Mtd> | [1..1] | CodeSet | | 305 |
| | ElectronicAddress <ElctrncAdr> | [0..1] | Text | | 306 |
| | PostalAddress <PstlAdr> | [0..1] | | | 306 |
| | Name <Nm> | [1..1] | Text | | 306 |
| | Address <Adr> | [1..1] | ± | | 306 |

### 5.4.2.18.16.1 RemittanceIdentification <RmtId>

Presence: [0..1]

Definition: Unique identification, as assigned by the initiating party, to unambiguously identify the remittance information sent separately from the payment instruction, such as a remittance advice.

Datatype: "Max35Text" on page 431

### 5.4.2.18.16.2 RemittanceLocationDetails <RmtLctnDtls>

Presence: [0..*]

Definition: Set of elements used to provide information on the location and/or delivery of the remittance information.

RemittanceLocationDetails <RmtLctnDtls> contains the following RemittanceLocationData2 elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Method <Mtd> | [1..1] | CodeSet | | 305 |
| | ElectronicAddress <ElctrncAdr> | [0..1] | Text | | 306 |
| | PostalAddress <PstlAdr> | [0..1] | | | 306 |
| | Name <Nm> | [1..1] | Text | | 306 |
| | Address <Adr> | [1..1] | ± | | 306 |

### 5.4.2.18.16.2.1 Method <Mtd>

Presence: [1..1]

Definition: Method used to deliver the remittance advice information.

Datatype: "RemittanceLocationMethod2Code" on page 422

| CodeName | Name | Definition |
|---|---|---|
| FAXI | Fax | Remittance advice information must be faxed. |

---

<!-- Page 306 -->

| CodeName | Name | Definition |
|---|---|---|
| EDIC | ElectronicDataInterchange | Remittance advice information must be sent through Electronic Data Interchange (EDI). |
| URID | UniformResourceIdentifier | Remittance advice information needs to be sent to a Uniform Resource Identifier (URI). URI is a compact string of characters that uniquely identify an abstract or physical resource. URI's are the super-set of identifiers, such as URLs, email addresses, ftp sites, etc, and as such, provide the syntax for all of the identification schemes. |
| EMAL | EMail | Remittance advice information must be sent through e-mail. |
| POST | Post | Remittance advice information must be sent through postal services. |
| SMSM | SMS | Remittance advice information must be sent through by phone as a short message service (SMS). |

## 5.4.2.18.16.2.2 ElectronicAddress <ElectrncAdr>

*Presence:* [0..1]

*Definition:* Electronic address to which an agent is to send the remittance information.

*Datatype:* "Max2048Text" on page 430

## 5.4.2.18.16.2.3 PostalAddress <PstlAdr>

*Presence:* [0..1]

*Definition:* Postal address to which an agent is to send the remittance information.

**PostalAddress <PstlAdr>** contains the following **NameAndAddress18** elements

| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
|  | **Name** <Nm> | [1..1] | Text |  | 306 |
|  | **Address** <Adr> | [1..1] | ± |  | 306 |

### 5.4.2.18.16.2.3.1 Name <Nm>

*Presence:* [1..1]

*Definition:* Name by which a party is known and is usually used to identify that party.

*Datatype:* "Max140Text" on page 429

### 5.4.2.18.16.2.3.2 Address <Adr>

*Presence:* [1..1]

*Definition:* Postal address of a party.

---

<!-- Page 307 -->

Address <Adr> contains the following elements (see "PostalAddress27" on page 357 for details)



| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | AddressType <AdrTp> | [0..1] |  |  | 357 |
| (Or | Code <Cd> | [1..1] | CodeSet |  | 358 |
| Or) | Proprietary <Pry> | [1..1] | ± |  | 358 |
| | CareOf <CareOf> | [0..1] | Text |  | 358 |
| | Department <Dept> | [0..1] | Text |  | 358 |
| | SubDepartment <SubDept> | [0..1] | Text |  | 359 |
| | StreetName <StrtNm> | [0..1] | Text |  | 359 |
| | BuildingNumber <BldgNb> | [0..1] | Text |  | 359 |
| | BuildingName <BldgNm> | [0..1] | Text |  | 359 |
| | Floor <Flr> | [0..1] | Text |  | 359 |
| | UnitNumber <UnitNb> | [0..1] | Text |  | 359 |
| | PostBox <PstBx> | [0..1] | Text |  | 359 |
| | Room <Room> | [0..1] | Text |  | 359 |
| | PostCode <PstCd> | [0..1] | Text |  | 360 |
| | TownName <TwnNm> | [0..1] | Text |  | 360 |
| | TownLocationName <TwnLctnNm> | [0..1] | Text |  | 360 |
| | DistrictName <DstrctNm> | [0..1] | Text |  | 360 |
| | CountrySubDivision <CtrySubDvsn> | [0..1] | Text |  | 360 |
| | Country <Ctry> | [0..1] | CodeSet | C7 | 360 |
| | AddressLine <AdrLine> | [0..7] | Text |  | 360 |

## 5.4.2.18.17 RemittanceInformation <RmtInf>

Presence: [0..1]

Definition: Information supplied to enable the matching of an entry with the items that the transfer is intended to settle, such as commercial invoices in an accounts' receivable system.

RemittanceInformation <RmtInf> contains the following elements (see "RemittanceInformation22" on page 364 for details)



| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Unstructured <Ustrd> | [0..*] | Text |  | 364 |
| | Structured <Strd> | [0..*] | ± |  | 364 |

---

<!-- Page 308 -->

**5.4.2.18 SupplementaryData <SplmtryData>**
*Presence:* [0..*]
*Definition:* Additional information that cannot be captured in the structured elements and/or any other specific block.
*Impacted by:* C18 "SupplementaryDataRule"

**SupplementaryData <SplmtryData>** contains the following elements (see "SupplementaryData1" on page 334 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | PlaceAndName <PlcAndNm> | [0..1] | Text | | 334 |
| | Envelope <Envlp> | [1..1] | (External Schema) | | 334 |

**Constraints**
*   **SupplementaryDataRule**
    This component may not be used without the explicit approval of a SEG and submission to the RA of ISO 20022 compliant structure(s) to be used in the Envelope element.

## 5.4.3 SupplementaryData <SplmtryData>
*Presence:* [0..*]
*Definition:* Additional information that cannot be captured in the structured elements and/or any other specific block.
*Impacted by:* C18 "SupplementaryDataRule"

**SupplementaryData <SplmtryData>** contains the following elements (see "SupplementaryData1" on page 334 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | PlaceAndName <PlcAndNm> | [0..1] | Text | | 334 |
| | Envelope <Envlp> | [1..1] | (External Schema) | | 334 |

**Constraints**
*   **SupplementaryDataRule**
    This component may not be used without the explicit approval of a SEG and submission to the RA of ISO 20022 compliant structure(s) to be used in the Envelope element.

---

<!-- Page 309 -->

# 6 Message Items Types

## 6.1 MessageComponents

### 6.1.1 Account

#### 6.1.1.1 CashAccountType2Choice

*Definition: Nature or use of the account.*

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| Or | Code <Cd> | [1..1] | CodeSet | | 309 |
| Or | Proprietary <Prtry> | [1..1] | Text | | 309 |

##### 6.1.1.1.1 Code <Cd>

*Presence: [1..1]*

*Definition: Account type, in a coded form.*

*Datatype: "ExternalCashAccountType1Code" on page 413*

##### 6.1.1.1.2 Proprietary <Prtry>

*Presence: [1..1]*

*Definition: Nature or use of the account in a proprietary form.*

*Datatype: "Max35Text" on page 431*

#### 6.1.1.2 CashAccount40

*Definition: Provides the details to identify an account.*

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Identification <Id> | [0..1] | ± | | 310 |
| | Type <Tp> | [0..1] | ± | | 310 |
| | Currency <Ccy> | [0..1] | CodeSet | C2 | 310 |
| | Name <Nm> | [0..1] | Text | | 311 |
| | Proxy <Prxy> | [0..1] | ± | | 311 |

---

<!-- Page 310 -->

Constraints

- **IdentificationAndProxyGuideline**

  If the account identification is not defined through a conventional identification such as an email address or a mobile number, then the proxy element should be used for the identification of the account.

- **IdentificationOrProxyPresenceRule**

  Identification must be present or Proxy must be present. Both may be present.

  ```
  Following Must be True
  /Identification Must be present
  Or    /Proxy Must be present
  ```

### 6.1.1.2.1 Identification <Id>

*Presence:* [0..1]

*Definition:* Unique and unambiguous identification for the account between the account owner and the account servicer.

**Identification <Id>** contains one of the following elements (see "**AccountIdentification4Choice**" on page 313 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
| :--- | :--- | :--- | :--- | :--- | :--- |
| (Or | IBAN <IBAN> | [1..1] | IdentifierSet | C14 | 313 |
| Or) | Other <Othr> | [1..1] | ± | | 314 |

### 6.1.1.2.2 Type <Tp>

*Presence:* [0..1]

*Definition:* Specifies the nature, or use of the account.

**Type <Tp>** contains one of the following elements (see "**CashAccountType2Choice**" on page 309 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
| :--- | :--- | :--- | :--- | :--- | :--- |
| (Or | Code <Cd> | [1..1] | CodeSet | | 309 |
| Or) | Proprietary <Ptry> | [1..1] | Text | | 309 |

### 6.1.1.2.3 Currency <Ccy>

*Presence:* [0..1]

*Definition:* Identification of the currency in which the account is held.

Usage: Currency should only be used in case one and the same account number covers several currencies

and the initiating party needs to identify which currency needs to be used for settlement on the account.

*Impacted by:* C2 "**ActiveOrHistoricCurrency**"

*Datatype:* "**ActiveOrHistoricCurrencyCode**" on page 409

---

<!-- Page 311 -->

Constraints

- **ActiveOrHistoricCurrency**

The Currency Code must be registered, or have already been registered. Valid active or historic currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and may be or not be withdrawn on the day the message containing the Currency is exchanged.

### 6.1.1.2.4 Name <Nm>

*Presence:* [0..1]

*Definition:* Name of the account, as assigned by the account servicing institution, in agreement with the account owner in order to provide an additional means of identification of the account.

Usage: The account name is different from the account owner name. The account name is used in certain user communities to provide a means of identifying the account, in addition to the account owner's identity and the account number.

*Datatype:* "Max70Text" on page 431

### 6.1.1.2.5 Proxy <Prxy>

*Presence:* [0..1]

*Definition:* Specifies an alternate assumed name for the identification of the account.

**Proxy <Prxy>** contains the following elements (see "ProxyAccountIdentification1" on page 312 for details)



| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Type <Tp> | [0..1] |  |  | 312 |
| {Or | Code <Cd> | [1..1] | CodeSet |  | 313 |
| Or} | Proprietary <Prtry> | [1..1] | Text |  | 313 |
| | Identification <Id> | [1..1] | Text |  | 313 |

### 6.1.1.3 GenericAccountIdentification1

*Definition:* Information related to a generic account identification.



| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Identification <Id> | [1..1] | Text |  | 311 |
| | SchemeName <SchmeNm> | [0..1] |  |  | 312 |
| {Or | Code <Cd> | [1..1] | CodeSet |  | 312 |
| Or} | Proprietary <Prtry> | [1..1] | Text |  | 312 |
| | Issuer <Issr> | [0..1] | Text |  | 312 |

#### 6.1.1.3.1 Identification <Id>

*Presence:* [1..1]

---

<!-- Page 312 -->

Definition: Identification assigned by an institution.
Datatype: "Max34Text" on page 430

### 6.1.1.3.2 SchemeName <SchemeNm>

Presence: [0..1]

Definition: Name of the identification scheme.

SchemeName <SchemeNm> contains one of the following AccountSchemeName1Choice elements

| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| (Or | Code <Cd> | [1..1] | CodeSet |  | 312 |
| (Or) | Proprietary <Prtry> | [1..1] | Text |  | 312 |

#### 6.1.1.3.2.1 Code <Cd>

Presence: [1..1]

Definition: Name of the identification scheme, in a coded form as published in an external list.

Datatype: "ExternalAccountIdentification1Code" on page 413

#### 6.1.1.3.2.2 Proprietary <Prtry>

Presence: [1..1]

Definition: Name of the identification scheme, in a free text form.

Datatype: "Max35Text" on page 431

### 6.1.1.3.3 Issuer <Issr>

Presence: [0..1]

Definition: Entity that assigns the identification.

Datatype: "Max35Text" on page 431

## 6.1.1.4 ProxyAccountIdentification1

Definition: Information related to a proxy identification of the account.

| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
|  | Type <Tp> | [0..1] |  |  | 312 |
| (Or | Code <Cd> | [1..1] | CodeSet |  | 313 |
| (Or) | Proprietary <Prtry> | [1..1] | Text |  | 313 |
|  | Identification <Id> | [1..1] | Text |  | 313 |

### 6.1.1.4.1 Type <Tp>

Presence: [0..1]

Definition: Type of the proxy identification.

---

<!-- Page 313 -->

Type <Tp> contains one of the following ProxyAccountType1Choice elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| (Or | Code <Cd> | [1..1] | CodeSet | | 313 |
| Or) | Proprietary <Prtry> | [1..1] | Text | | 313 |

**6.1.1.4.1.1 Code <Cd>**

*Presence:* [1..1]

*Definition:* Name of the identification scheme, in a coded form as published in an external list.

*Datatype:* "ExternalProxyAccountType1Code" on page 418

**6.1.1.4.1.2 Proprietary <Prtry>**

*Presence:* [1..1]

*Definition:* Name of the identification scheme, in a free text form.

*Datatype:* "Max35Text" on page 431

**6.1.1.4.2 Identification <Id>**

*Presence:* [1..1]

*Definition:* Identification used to indicate the account identification under another specified name.

*Datatype:* "Max2048Text" on page 430

## 6.1.2 Account Identification

**6.1.2.1 AccountIdentification4Choice**

*Definition:* Specifies the unique identification of an account as assigned by the account servicer.

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| (Or | IBAN <IBAN> | [1..1] | IdentifierSet | C14 | 313 |
| Or) | Other <Othr> | [1..1] | ± | | 314 |

**6.1.2.1.1 IBAN <IBAN>**

*Presence:* [1..1]

*Definition:* International Bank Account Number (IBAN) - identifier used internationally by financial institutions to uniquely identify the account of a customer. Further specifications of the format and content of the IBAN can be found in the standard ISO 13616 "Banking and related financial services - International Bank Account Number (IBAN)" version 1997-10-01, or later revisions.

*Impacted by:* C14 "IBAN"

*Datatype:* "IBAN2007Identifier" on page 426

---

<!-- Page 314 -->

Constraints

*   **IBAN**
    A valid IBAN consists of all three of the following components: Country Code, check digits and BBAN.

## 6.1.2.1.2 Other <Othr>

*Presence: [1..1]*

*Definition: Unique identification of an account, as assigned by the account servicer, using an identification scheme.*

**Other <Othr>** contains the following elements (see "GenericAccountIdentification1" on page 311 for details)



| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | Identification <Id> | [1..1] | Text | | 311 |
| | SchemeName <SchemeNm> | [0..1] | | | 312 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 312 |
| Or) | Proprietary <Pty> | [1..1] | Text | | 312 |
| | Issuer <Issr> | [0..1] | Text | | 312 |

## 6.1.3 Amount

### 6.1.3.1 AmountType4Choice

*Definition: Specifies the amount of money to be moved between the debtor and creditor, before deduction of charges, expressed in the currency as ordered by the initiating party.*



| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| (Or | InstructedAmount <InstdAmt> | [1..1] | Amount | C2, C8 | 314 |
| Or) | EquivalentAmount <EqvAmt> | [1..1] | | | 315 |
| | Amount <Amt> | [1..1] | Amount | C2, C8 | 315 |
| | CurrencyOfTransfer <CcyOfTrf> | [1..1] | CodeSet | C2 | 315 |

#### 6.1.3.1.1 InstructedAmount <InstdAmt>

*Presence: [1..1]*

*Definition: Amount of money to be moved between the debtor and creditor, before deduction of charges, expressed in the currency as ordered by the initiating party.*

Usage: This amount has to be transported unchanged through the transaction chain.

*Impacted by:* C2 "ActiveOrHistoricCurrency", C8 "CurrencyAmount"

*Datatype:* "ActiveOrHistoricCurrencyAndAmount" on page 407

---

<!-- Page 315 -->

Constraints

- **ActiveOrHistoricCurrency**

The Currency Code must be registered, or have already been registered. Valid active or historic currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and may be or not be withdrawn on the day the message containing the Currency is exchanged.

- **CurrencyAmount**

The number of fractional digits (or minor unit of currency) must comply with ISO 4217.

Note: The decimal separator is a dot.

## 6.1.3.1.2 EquivalentAmount <EqvtAmt>

*Presence:* [1..1]

*Definition:* Amount of money to be moved between the debtor and creditor, expressed in the currency of the debtor's account, and the currency in which the amount is to be moved.

**EquivalentAmount <EqvtAmt>** contains the following **EquivalentAmount2** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Amount <Amt> | [1..1] | Amount | C2, C8 | 315 |
| | CurrencyOfTransfer <CcyOfTrf> | [1..1] | CodeSet | C2 | 315 |

### 6.1.3.1.2.1 Amount <Amt>

*Presence:* [1..1]

*Definition:* Amount of money to be moved between debtor and creditor, before deduction of charges, expressed in the currency of the debtor's account, and to be moved in a different currency.

Usage: The first agent will convert the equivalent amount into the amount to be moved.

*Impacted by:* C2 "ActiveOrHistoricCurrency", C8 "CurrencyAmount"

*Datatype:* "ActiveOrHistoricCurrencyAndAmount" on page 407

Constraints

- **ActiveOrHistoricCurrency**

The Currency Code must be registered, or have already been registered. Valid active or historic currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and may be or not be withdrawn on the day the message containing the Currency is exchanged.

- **CurrencyAmount**

The number of fractional digits (or minor unit of currency) must comply with ISO 4217.

Note: The decimal separator is a dot.

### 6.1.3.1.2.2 CurrencyOfTransfer <CcyOfTrf>

*Presence:* [1..1]

---

<!-- Page 316 -->

*Definition: Specifies the currency of the to be transferred amount, which is different from the currency of the debtor's account.*

*Impacted by: C2 "ActiveOrHistoricCurrency"*

*Datatype: "ActiveOrHistoricCurrencyCode" on page 409*

**Constraints**

- **ActiveOrHistoricCurrency**

The Currency Code must be registered, or have already been registered. Valid active or historic currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and may be or not be withdrawn on the day the message containing the Currency is exchanged.

## 6.1.4 Date Period

### 6.1.4.1 DatePeriod2

*Definition: Range of time defined by a start date and an end date.*



| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | FromDate <FrDt> | [1..1] | Date | | 316 |
| | ToDate <ToDt> | [1..1] | Date | | 316 |

#### 6.1.4.1.1 FromDate <FrDt>

*Presence: [1..1]*

*Definition: Start date of the range.*

*Datatype: "ISODate" on page 425*

#### 6.1.4.1.2 ToDate <ToDt>

*Presence: [1..1]*

*Definition: End date of the range.*

*Datatype: "ISODate" on page 425*

## 6.1.5 Date Time

### 6.1.5.1 DateAndDateTime2Choice

*Definition: Choice between a date or a date and time format.*



| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| (Or | Date <Dt> | [1..1] | Date | | 317 |
| Or) | DateTime <DtTm> | [1..1] | DateTime | | 317 |

---

<!-- Page 317 -->

#### 6.1.5.1.1 Date <Dt>

*Presence:* [1..1]

*Definition:* Specified date.

*Datatype:* "ISODate" on page 425

#### 6.1.5.1.2 DateTime <DtTm>

*Presence:* [1..1]

*Definition:* Specified date and time.

*Datatype:* "ISODateTime" on page 425

## 6.1.6 Direct Debit

### 6.1.6.1 CreditTransferMandateData1

*Definition:* Provides further details related to a credit transfer mandate signed between the creditor and the debtor.

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | MandateIdentification <MndtId> | [0..1] | Text | | 317 |
| | Type <Tp> | [0..1] | ± | | 317 |
| | DateOfSignature <DtOfSgntr> | [0..1] | Date | | 318 |
| | DateOfVerification <DtOfVrfctn> | [0..1] | DateTime | | 318 |
| | ElectronicSignature <ElectrcSgntr> | [0..1] | Binary | | 318 |
| | FirstPaymentDate <FrstPmtDt> | [0..1] | Date | | 318 |
| | FinalPaymentDate <FnlpmtDt> | [0..1] | Date | | 318 |
| | Frequency <Frqcy> | [0..1] | ± | | 319 |
| | Reason <Rsn> | [0..1] | | | 319 |
| Or | Code <Cd> | [1..1] | CodeSet | | 319 |
| Or | Proprietary <Ptry> | [1..1] | Text | | 319 |

#### 6.1.6.1.1 MandateIdentification <MndtId>

*Presence:* [0..1]

*Definition:* Unique identification, as assigned by the creditor, to unambiguously identify the mandate.

*Datatype:* "Max35Text" on page 431

#### 6.1.6.1.2 Type <Tp>

*Presence:* [0..1]

*Definition:* Specifies the type of mandate, such as paper, electronic or scheme.

---

<!-- Page 318 -->

Type <Tp> contains the following elements (see "MandateTypeInformation2" on page 332 for details)

| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | ServiceLevel <SvcLvl> | [0..1] | | | 332 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 332 |
| Or) | Proprietary <Ptry> | [1..1] | Text | | 332 |
| | LocalInstrument <LclInstrm> | [0..1] | | | 332 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 333 |
| Or) | Proprietary <Ptry> | [1..1] | Text | | 333 |
| | CategoryPurpose <CtgyPurp> | [0..1] | | | 333 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 333 |
| Or) | Proprietary <Ptry> | [1..1] | Text | | 333 |
| | Classification <Classctn> | [0..1] | ± | | 333 |

**6.1.6.1.3 DateOfSignature <DtOfSgntr>**

*Presence:* [0..1]

*Definition:* Date on which the credit transfer mandate has been signed by the debtor.

*Datatype:* "ISODate" on page 425

**6.1.6.1.4 DateOfVerification <DtOfVrfctn>**

*Presence:* [0..1]

*Definition:* Date on which the credit transfer mandate has been verified.

*Datatype:* "ISODateTime" on page 425

**6.1.6.1.5 ElectronicSignature <ElctrncSgntr>**

*Presence:* [0..1]

*Definition:* Additional security provisions, such as a digital signature, as provided by the debtor.

*Datatype:* "Max10KBinary" on page 408

**6.1.6.1.6 FirstPaymentDate <FrstPmtDt>**

*Presence:* [0..1]

*Definition:* Date of the first payment of a recurrent credit transfer as per the mandate.

*Datatype:* "ISODate" on page 425

**6.1.6.1.7 FinalPaymentDate <FnIPmtDt>**

*Presence:* [0..1]

*Definition:* Date of the final payment of a recurrent credit transfer as per the mandate.

*Datatype:* "ISODate" on page 425

---

<!-- Page 319 -->

## 6.1.6.1.8 Frequency <Frcy>

*Presence:* [0..1]

*Definition:* Regularity with which credit transfer instructions are to be created and processed.

**Frequency** <Frcy> contains one of the following elements (see "Frequency36Choice" on page 326 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| Or | Type <Tp> | [1..1] | CodeSet | | 327 |
| Or | Period <Prd> | [1..1] | | | 327 |
| | Type <Tp> | [1..1] | CodeSet | | 328 |
| | CountPerPeriod <CntPerPrd> | [1..1] | Quantity | | 328 |
| Or | PointInTime <Ptlntm> | [1..1] | | | 328 |
| | Type <Tp> | [1..1] | CodeSet | | 328 |
| | PointInTime <Ptlntm> | [1..1] | Text | | 329 |

## 6.1.6.1.9 Reason <Rsn>

*Presence:* [0..1]

*Definition:* Reason for the setup of the credit transfer mandate.

Usage:

The reason will allow the user to distinguish between different mandates for the same creditor.

**Reason** <Rsn> contains one of the following **MandateSetupReason1Choice** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| Or | Code <Cd> | [1..1] | CodeSet | | 319 |
| Or | Proprietary <Prtry> | [1..1] | Text | | 319 |

### 6.1.6.1.9.1 Code <Cd>

*Presence:* [1..1]

*Definition:* Reason for the mandate setup, as published in an external reason code list.

*Datatype:* "ExternalMandateSetupReason1Code" on page 417

### 6.1.6.1.9.2 Proprietary <Prtry>

*Presence:* [1..1]

*Definition:* Reason for the mandate setup, in a proprietary form.

*Datatype:* "Max70Text" on page 431

---

<!-- Page 320 -->

# 6.1.7 Financial Institution Identification

## 6.1.7.1 ClearingSystemMemberIdentification2

*Definition: Unique identification, as assigned by a clearing system, to unambiguously identify a member of the clearing system.*

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | ClearingSystemIdentification <ClrSysId> | [0..1] | ± | | 320 |
| | MemberIdentification <MmbId> | [1..1] | Text | | 320 |

### 6.1.7.1.1 ClearingSystemIdentification <ClrSysId>

*Presence: [0..1]*

*Definition: Specification of a pre-agreed offering between clearing agents or the channel through which the payment instruction is processed.*

**ClearingSystemIdentification <ClrSysId>** contains one of the following elements (see "ClearingSystemIdentification2Choice" on page 405 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| Or | Code <Cd> | [1..1] | CodeSet | | 405 |
| Or | Proprietary <Prtry> | [1..1] | Text | | 405 |

### 6.1.7.1.2 MemberIdentification <MmbId>

*Presence: [1..1]*

*Definition: Identification of a member of a clearing system.*

*Datatype: "Max35Text" on page 431*

## 6.1.7.2 BranchAndFinancialInstitutionIdentification8

*Definition: Unique and unambiguous identification of a financial institution or a branch of a financial institution.*

---

<!-- Page 321 -->

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | FinancialInstitutionIdentification <FinInstId> | [1..1] |  |  | 321 |
| | BICFI <BICFI> | [0..1] | IdentifierSet | C6 | 321 |
| | ClearingSystemMemberIdentification <ClrSysMmbId> | [0..1] | ± |  | 322 |
| | LEI <LEI> | [0..1] | IdentifierSet |  | 322 |
| | Name <Nm> | [0..1] | Text |  | 322 |
| | PostalAddress <PstlAdr> | [0..1] | ± |  | 322 |
| | Other <Othr> | [0..1] | ± |  | 323 |
| | BranchIdentification <BrnchId> | [0..1] |  |  | 324 |
| | Identification <Id> | [0..1] | Text |  | 324 |
| | LEI <LEI> | [0..1] | IdentifierSet |  | 324 |
| | Name <Nm> | [0..1] | Text |  | 324 |
| | PostalAddress <PstlAdr> | [0..1] | ± |  | 324 |

## 6.1.7.2.1 FinancialInstitutionIdentification <FinInstId>

*Presence:* [1..1]

*Definition:* Unique and unambiguous identification of a financial institution, as assigned under an internationally recognised or proprietary identification scheme.

**FinancialInstitutionIdentification <FinInstId>** contains the following **FinancialInstitutionIdentification23** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | BICFI <BICFI> | [0..1] | IdentifierSet | C6 | 321 |
| | ClearingSystemMemberIdentification <ClrSysMmbId> | [0..1] | ± |  | 322 |
| | LEI <LEI> | [0..1] | IdentifierSet |  | 322 |
| | Name <Nm> | [0..1] | Text |  | 322 |
| | PostalAddress <PstlAdr> | [0..1] | ± |  | 322 |
| | Other <Othr> | [0..1] | ± |  | 323 |

## 6.1.7.2.1.1 BICFI <BICFI>

*Presence:* [0..1]

*Definition:* Code allocated to a financial institution by the ISO 9362 Registration Authority as described in ISO 9362 'Banking - Banking telecommunication messages - Business identifier code (BIC)'.

*Impacted by:* C6 "BICFI"

*Datatype:* "BICFIDec2014Identifier" on page 426

---

<!-- Page 322 -->

Constraints

- **BICFI**

Valid BICs for financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous characters.

**6.1.7.2.1.2 ClearingSystemMemberIdentification <ClrSysMmbId>**

*Presence:* [0..1]

*Definition:* Information used to identify a member within a clearing system.

**ClearingSystemMemberIdentification <ClrSysMmbId>** contains the following elements (see "ClearingSystemMemberIdentification2" on page 320 for details)



| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | ClearingSystemIdentification <ClrSysId> | [0..1] | ± | | 320 |
| | MemberIdentification <MmbId> | [1..1] | Text | | 320 |

**6.1.7.2.1.3 LEI <LEI>**

*Presence:* [0..1]

*Definition:* Legal entity identifier of the financial institution.

*Datatype:* "LEIIdentifier" on page 426

**6.1.7.2.1.4 Name <Nm>**

*Presence:* [0..1]

*Definition:* Name by which an agent is known and which is usually used to identify that agent.

*Datatype:* "Max140Text" on page 429

**6.1.7.2.1.5 PostalAddress <PstlAdr>**

*Presence:* [0..1]

*Definition:* Information that locates and identifies a specific address, as defined by postal services.

---

<!-- Page 323 -->

PostalAddress <PstlAdr> contains the following elements (see "PostalAddress27" on page 357 for details)



<table>
  <thead>
    <tr>
      <th>Or</th>
      <th>MessageElement &lt;XML Tag&gt;</th>
      <th>Mult.</th>
      <th>Type</th>
      <th>Constr. No.</th>
      <th>Page</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td>AddressType &lt;AdrTp&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>357</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Code &lt;Cd&gt;</td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td></td>
      <td>358</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Proprietary &lt;Pry&gt;</td>
      <td>[1..1]</td>
      <td>±</td>
      <td></td>
      <td>358</td>
    </tr>
    <tr>
      <td></td>
      <td>CareOf &lt;CareOf&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>358</td>
    </tr>
    <tr>
      <td></td>
      <td>Department &lt;Dept&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>358</td>
    </tr>
    <tr>
      <td></td>
      <td>SubDepartment &lt;SubDept&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>359</td>
    </tr>
    <tr>
      <td></td>
      <td>StreetName &lt;StrtNm&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>359</td>
    </tr>
    <tr>
      <td></td>
      <td>BuildingNumber &lt;BldgNb&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>359</td>
    </tr>
    <tr>
      <td></td>
      <td>BuildingName &lt;BldgNm&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>359</td>
    </tr>
    <tr>
      <td></td>
      <td>Floor &lt;Flr&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>359</td>
    </tr>
    <tr>
      <td></td>
      <td>UnitNumber &lt;UnitNb&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>359</td>
    </tr>
    <tr>
      <td></td>
      <td>PostBox &lt;PstBx&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>359</td>
    </tr>
    <tr>
      <td></td>
      <td>Room &lt;Room&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>359</td>
    </tr>
    <tr>
      <td></td>
      <td>PostCode &lt;PstCd&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>360</td>
    </tr>
    <tr>
      <td></td>
      <td>TownName &lt;TwnNm&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>360</td>
    </tr>
    <tr>
      <td></td>
      <td>TownLocationName &lt;TwnLctnNm&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>360</td>
    </tr>
    <tr>
      <td></td>
      <td>DistrictName &lt;DstrctNm&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>360</td>
    </tr>
    <tr>
      <td></td>
      <td>CountrySubDivision &lt;CtrySubDvsn&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>360</td>
    </tr>
    <tr>
      <td></td>
      <td>Country &lt;Ctry&gt;</td>
      <td>[0..1]</td>
      <td>CodeSet</td>
      <td>C7</td>
      <td>360</td>
    </tr>
    <tr>
      <td></td>
      <td>AddressLine &lt;AdrLine&gt;</td>
      <td>[0..7]</td>
      <td>Text</td>
      <td></td>
      <td>360</td>
    </tr>
  </tbody>
</table>

**6.1.7.2.1.6 Other <Othr>**

*Presence:* [0..1]

*Definition:* Unique identification of an agent, as assigned by an institution, using an identification scheme.

---

<!-- Page 324 -->

Other <Othr> contains the following elements (see "GenericFinancialIdentification1" on page 325 for details)



<table><tr><td>Or</td><td>MessageElement &lt;XML Tag&gt;</td><td>Mult.</td><td>Type</td><td>Constr. No.</td><td>Page</td></tr><tr><td></td><td>Identification &lt;Id&gt;</td><td>[1..1]</td><td>Text</td><td></td><td>326</td></tr><tr><td></td><td>SchemaName &lt;SchmeNm&gt;</td><td>[0..1]</td><td></td><td></td><td>326</td></tr><tr><td>Or</td><td>Code &lt;Cd&gt;</td><td>[1..1]</td><td>CodeSet</td><td></td><td>326</td></tr><tr><td>Or</td><td>Proprietary &lt;Ptry&gt;</td><td>[1..1]</td><td>Text</td><td></td><td>326</td></tr><tr><td></td><td>Issuer &lt;Issr&gt;</td><td>[0..1]</td><td>Text</td><td></td><td>326</td></tr></table>

### 6.1.7.2.2 BranchIdentification <BrnchId>

Presence: [0..1]

Definition: Identifies a specific branch of a financial institution.

Usage: This component should be used in case the identification information in the financial institution component does not provide identification up to branch level.

BranchIdentification <BrnchId> contains the following BranchData5 elements



<table><tr><td>Or</td><td>MessageElement &lt;XML Tag&gt;</td><td>Mult.</td><td>Type</td><td>Constr. No.</td><td>Page</td></tr><tr><td></td><td>Identification &lt;Id&gt;</td><td>[0..1]</td><td>Text</td><td></td><td>324</td></tr><tr><td></td><td>LEI &lt;LEI&gt;</td><td>[0..1]</td><td>IdentifierSet</td><td></td><td>324</td></tr><tr><td></td><td>Name &lt;Nm&gt;</td><td>[0..1]</td><td>Text</td><td></td><td>324</td></tr><tr><td></td><td>PostalAddress &lt;PstlAdr&gt;</td><td>[0..1]</td><td>±</td><td></td><td>324</td></tr></table>

#### 6.1.7.2.2.1 Identification <Id>

Presence: [0..1]

Definition: Unique and unambiguous identification of a branch of a financial institution.

Datatype: "Max35Text" on page 431

#### 6.1.7.2.2.2 LEI <LEI>

Presence: [0..1]

Definition: Legal entity identification for the branch of the financial institution.

Datatype: "LEIIdentifier" on page 426

#### 6.1.7.2.2.3 Name <Nm>

Presence: [0..1]

Definition: Name by which an agent is known and which is usually used to identify that agent.

Datatype: "Max140Text" on page 429

#### 6.1.7.2.2.4 PostalAddress <PstlAdr>

Presence: [0..1]

---

<!-- Page 325 -->

*Definition:* Information that locates and identifies a specific address, as defined by postal services.

**PostalAddress <PstlAdr>** contains the following elements (see "PostalAddress27" on page 357 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | AddressType <AdrTp> | [0..1] | | | 357 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 358 |
| Or) | Proprietary <Ptry> | [1..1] | ± | | 358 |
| | CareOf <CareOf> | [0..1] | Text | | 358 |
| | Department <Dept> | [0..1] | Text | | 358 |
| | SubDepartment <SubDept> | [0..1] | Text | | 359 |
| | StreetName <StrtNm> | [0..1] | Text | | 359 |
| | BuildingNumber <BldgNb> | [0..1] | Text | | 359 |
| | BuildingName <BldgNm> | [0..1] | Text | | 359 |
| | Floor <Flr> | [0..1] | Text | | 359 |
| | UnitNumber <UnitNb> | [0..1] | Text | | 359 |
| | PostBox <PstBx> | [0..1] | Text | | 359 |
| | Room <Room> | [0..1] | Text | | 359 |
| | PostCode <PstCd> | [0..1] | Text | | 360 |
| | TownName <TwnNm> | [0..1] | Text | | 360 |
| | TownLocationName <TwnLctnNm> | [0..1] | Text | | 360 |
| | DistrictName <DstrctNm> | [0..1] | Text | | 360 |
| | CountrySubDivision <CtrySubDvsn> | [0..1] | Text | | 360 |
| | Country <Ctry> | [0..1] | CodeSet | C7 | 360 |
| | AddressLine <AdrLine> | [0..7] | Text | | 360 |

### 6.1.7.3 GenericFinancialIdentification1

*Definition:* Information related to an identification of a financial institution.

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Identification <Id> | [1..1] | Text | | 326 |
| | SchemeName <SchmeNm> | [0..1] | | | 326 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 326 |
| Or) | Proprietary <Ptry> | [1..1] | Text | | 326 |
| | Issuer <Issr> | [0..1] | Text | | 326 |

---

<!-- Page 326 -->

### 6.1.7.3.1 Identification <Id>
*Presence:* [1..1]
*Definition:* Unique and unambiguous identification of a person.
*Datatype:* "Max35Text" on page 431

### 6.1.7.3.2 SchemeName <SchemeNm>
*Presence:* [0..1]
*Definition:* Name of the identification scheme.
**SchemeName <SchemeNm>** contains one of the following **FinancialIdentificationSchemeName1Choice** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| (Or | Code <Cd> | [1..1] | CodeSet | | 326 |
| Or | Proprietary <Ptry> | [1..1] | Text | | 326 |

#### 6.1.7.3.2.1 Code <Cd>
*Presence:* [1..1]
*Definition:* Name of the identification scheme, in a coded form as published in an external list.
*Datatype:* "ExternalFinancialInstitutionIdentification1Code" on page 416

#### 6.1.7.3.2.2 Proprietary <Ptry>
*Presence:* [1..1]
*Definition:* Name of the identification scheme, in a free text form.
*Datatype:* "Max35Text" on page 431

### 6.1.7.3.3 Issuer <Issr>
*Presence:* [0..1]
*Definition:* Entity that assigns the identification.
*Datatype:* "Max35Text" on page 431

## 6.1.8 Frequency

### 6.1.8.1 Frequency36Choice
*Definition:* Choice of format for a frequency, for example, the frequency of payment.

---

<!-- Page 327 -->

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| Or | Type <Tp> | [1..1] | CodeSet | | 327 |
| Or | Period <Prd> | [1..1] | | | 327 |
| | Type <Tp> | [1..1] | CodeSet | | 328 |
| | CountPerPeriod <CntPerPrd> | [1..1] | Quantity | | 328 |
| Or) | PointInTime <PtInTm> | [1..1] | | | 328 |
| | Type <Tp> | [1..1] | CodeSet | | 328 |
| | PointInTime <PtInTm> | [1..1] | Text | | 329 |

## 6.1.8.1.1 Type <Tp>

*Presence:* [1..1]

*Definition:* Specifies a frequency in terms of a specified period type.

*Datatype:* "Frequency6Code" on page 420

| CodeName | Name | Definition |
|---|---|---|
| YEAR | Annual | Event takes place every year or once a year. |
| MNTH | Monthly | Event takes place every month or once a month. |
| QRRT | Quarterly | Event takes place every three months or four times a year. |
| MIAN | SemiAnnual | Event takes place every six months or two times a year. |
| WEEK | Weekly | Event takes place once a week. |
| DAIL | Daily | Event takes place every day. |
| ADHO | Adhoc | Event takes place on request or as necessary. |
| INDA | IntraDay | Event takes place several times a day. |
| FRTN | Fortnightly | Event takes place every two weeks. |

## 6.1.8.1.2 Period <Prd>

*Presence:* [1..1]

*Definition:* Specifies a frequency in terms of a count per period within a specified period type.

**Period <Prd>** contains the following **FrequencyPeriod1** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Type <Tp> | [1..1] | CodeSet | | 328 |
| | CountPerPeriod <CntPerPrd> | [1..1] | Quantity | | 328 |

---

<!-- Page 328 -->

### 6.1.8.1.2.1 Type <Tp>

*Presence:* [1..1]

*Definition:* Period for which the number of instructions are to be created and processed.

*Datatype:* "Frequency6Code" on page 420



| CodeName | Name | Definition |
|---|---|---|
| YEAR | Annual | Event takes place every year or once a year. |
| MNTH | Monthly | Event takes place every month or once a month. |
| QURT | Quarterly | Event takes place every three months or four times a year. |
| MIAN | SemiAnnual | Event takes place every six months or two times a year. |
| WEEK | Weekly | Event takes place once a week. |
| DAIL | Daily | Event takes place every day. |
| ADHO | Adhoc | Event takes place on request or as necessary. |
| INDA | IntraDay | Event takes place several times a day. |
| FRTN | Fortnightly | Event takes place every two weeks. |

### 6.1.8.1.2.2 CountPerPeriod <CntPerPrd>

*Presence:* [1..1]

*Definition:* Number of instructions to be created and processed during the specified period.

*Datatype:* "DecimalNumber" on page 427

### 6.1.8.1.3 PointInTime <PtnITm>

*Presence:* [1..1]

*Definition:* Specifies a frequency in terms of an exact point in time or moment within a specified period type.

**PointInTime <PtnITm>** contains the following **FrequencyAndMoment1** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Const. No. | Page |
|---|---|---|---|---|---|
|  | Type <Tp> | [1..1] | CodeSet |  | 328 |
|  | PointInTime <PtnITm> | [1..1] | Text |  | 329 |

#### 6.1.8.1.3.1 Type <Tp>

*Presence:* [1..1]

*Definition:* Period for which the number of instructions are to be created and processed.

*Datatype:* "Frequency6Code" on page 420

---

<!-- Page 329 -->

| CodeName | Name | Definition |
| :--- | :--- | :--- |
| YEAR | Annual | Event takes place every year or once a year. |
| MNTH | Monthly | Event takes place every month or once a month. |
| QURT | Quarterly | Event takes place every three months or four times a year. |
| MIAN | SemiAnnual | Event takes place every six months or two times a year. |
| WEEK | Weekly | Event takes place once a week. |
| DAIL | Daily | Event takes place every day. |
| ADHO | Adhoc | Event takes place on request or as necessary. |
| INDA | IntraDay | Event takes place several times a day. |
| FRTN | Fortnightly | Event takes place every two weeks. |

**6.1.8.1.3.2 PointInTime <PtlmTm>**

*Presence:* [1..1]

*Definition:* Further information on the exact point in time the event should take place.

*Datatype:* "Exact2NumericText" on page 428

## 6.1.9 Identification Information

### 6.1.9.1 GenericIdentification3

*Definition:* Information related to an identification, for example, party identification or account identification.

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
| :--- | :--- | :--- | :--- | :--- | :--- |
| | Identification <Id> | [1..1] | Text | | 329 |
| | Issuer <Issr> | [0..1] | Text | | 329 |

#### 6.1.9.1.1 Identification <Id>

*Presence:* [1..1]

*Definition:* Name or number assigned by an entity to enable recognition of that entity, for example, account identifier.

*Datatype:* "Max35Text" on page 431

#### 6.1.9.1.2 Issuer <Issr>

*Presence:* [0..1]

*Definition:* Entity that assigns the identification.

*Datatype:* "Max35Text" on page 431

---

<!-- Page 330 -->

## 6.1.9.2 PaymentIdentification6

*Definition: Provides further means of referencing a payment transaction.*

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | InstructionIdentification <InstrId> | [0..1] | Text | | 330 |
| | EndToEndIdentification <EndToEndId> | [1..1] | Text | | 330 |
| | UETR <UETR> | [0..1] | IdentifierSet | | 330 |

### 6.1.9.2.1 InstructionIdentification <InstrId>

*Presence:* [0..1]

*Definition:* Unique identification as assigned by an instructing party for an instructed party to unambiguously identify the instruction.

Usage: The instruction identification is a point to point reference that can be used between the instructing party and the instructed party to refer to the individual instruction. It can be included in several messages related to the instruction.

*Datatype:* "Max35Text" on page 431

### 6.1.9.2.2 EndToEndIdentification <EndToEndId>

*Presence:* [1..1]

*Definition:* Unique identification assigned by the initiating party to unambiguously identify the transaction. This identification is passed on, unchanged, throughout the entire end-to-end chain.

Usage: The end-to-end identification can be used for reconciliation or to link tasks relating to the transaction. It can be included in several messages related to the transaction.

*Datatype:* "Max35Text" on page 431

### 6.1.9.2.3 UETR <UETR>

*Presence:* [0..1]

*Definition:* Universally unique identifier to provide an end-to-end reference of a payment transaction.

*Datatype:* "UUIDv4Identifier" on page 427

## 6.1.9.3 GenericIdentification30

*Definition:* Information related to an identification, for example, party identification or account identification.

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | Identification <Id> | [1..1] | Text | | 331 |
| | Issuer <Issr> | [1..1] | Text | | 331 |
| | SchemeName <SchmeNm> | [0..1] | Text | | 331 |

---

<!-- Page 331 -->

### 6.1.9.3.1 Identification <Id>

*Presence:* [1..1]

*Definition:* Proprietary information, often a code, issued by the data source scheme issuer.

*Datatype:* "Exact4AlphaNumericText" on page 428

### 6.1.9.3.2 Issuer <Issr>

*Presence:* [1..1]

*Definition:* Entity that assigns the identification.

*Datatype:* "Max35Text" on page 431

### 6.1.9.3.3 SchemeName <SchmeNm>

*Presence:* [0..1]

*Definition:* Short textual description of the scheme.

*Datatype:* "Max35Text" on page 431

## 6.1.10 Mandate

### 6.1.10.1 MandateClassification1Choice

*Definition:* Specifies the high level purpose of the instruction based on a set of pre-defined categories.

Usage: This is used by the initiating party to provide information concerning the processing of the payment. It is likely to trigger special processing by any of the agents involved in the payment chain.



<table>
  <tr>
    <th>Or</th>
    <th>MessageElement&lt;XML Tag&gt;</th>
    <th>Mult.</th>
    <th>Type</th>
    <th>Constr. No.</th>
    <th>Page</th>
  </tr>
  <tr>
    <td>{Or</td>
    <td>Code &lt;Cd&gt;</td>
    <td>[1..1]</td>
    <td>CodeSet</td>
    <td></td>
    <td>331</td>
  </tr>
  <tr>
    <td>Or}</td>
    <td>Proprietary &lt;Ptry&gt;</td>
    <td>[1..1]</td>
    <td>Text</td>
    <td></td>
    <td>331</td>
  </tr>
</table>

#### 6.1.10.1.1 Code <Cd>

*Presence:* [1..1]

*Definition:* Category purpose, as published in an external category purpose code list.

*Datatype:* "MandateClassification1Code" on page 420



<table>
  <tr>
    <th>CodeName</th>
    <th>Name</th>
    <th>Definition</th>
  </tr>
  <tr>
    <td>FIXE</td>
    <td>Fixed</td>
    <td>Direct debit amount is fixed.</td>
  </tr>
  <tr>
    <td>USGB</td>
    <td>UsageBased</td>
    <td>Direct debit amount is based on usage.</td>
  </tr>
  <tr>
    <td>VARI</td>
    <td>Variable</td>
    <td>Direct debit amount is variable.</td>
  </tr>
</table>

#### 6.1.10.1.2 Proprietary <Ptry>

*Presence:* [1..1]

*Definition:* Category purpose, in a proprietary form.

*Datatype:* "Max35Text" on page 431

---

<!-- Page 332 -->

## 6.1.10.2 MandateTypeInformation2

*Definition: Set of elements used to further detail the information related to the type of payment.*

| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | ServiceLevel <SvcLv> | [0..1] | | | 332 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 332 |
| Or) | Proprietary <Ptry> | [1..1] | Text | | 332 |
| | LocalInstrument <LclInstrm> | [0..1] | | | 332 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 333 |
| Or) | Proprietary <Ptry> | [1..1] | Text | | 333 |
| | CategoryPurpose <CtgyPurp> | [0..1] | | | 333 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 333 |
| Or) | Proprietary <Ptry> | [1..1] | Text | | 333 |
| | Classification <Classctm> | [0..1] | ± | | 333 |

## 6.1.10.2.1 ServiceLevel <SvcLv>

*Presence: [0..1]*

*Definition: Agreement under which or rules under which the mandate resides.*

**ServiceLevel <SvcLv>** contains one of the following **ServiceLevel8Choice** elements

| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| (Or | Code <Cd> | [1..1] | CodeSet | | 332 |
| Or) | Proprietary <Ptry> | [1..1] | Text | | 332 |

### 6.1.10.2.1.1 Code <Cd>

*Presence: [1..1]*

*Definition: Specifies a pre-agreed service or level of service between the parties, as published in an external service level code list.*

*Datatype: "ExternalServiceLevel1Code" on page 419*

### 6.1.10.2.1.2 Proprietary <Ptry>

*Presence: [1..1]*

*Definition: Specifies a pre-agreed service or level of service between the parties, as a proprietary code.*

*Datatype: "Max35Text" on page 431*

## 6.1.10.2.2 LocalInstrument <LclInstrm>

*Presence: [0..1]*

*Definition: User community specific instrument.*

---

<!-- Page 333 -->

Usage: This element is used to specify a local instrument, local clearing option and/or further qualify the service or service level.

**LocalInstrument** `<LCInstrm>` contains one of the following **LocalInstrument2Choice** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| (Or | Code `<Cd>` | [1..1] | CodeSet | | 333 |
| (Or) | Proprietary `<Prtry>` | [1..1] | Text | | 333 |

### 6.1.10.2.2.1 Code `<Cd>`

*Presence:* [1..1]

*Definition:* Specifies the local instrument, as published in an external local instrument code list.

*Datatype:* "ExternalLocalInstrument1Code" on page 417

### 6.1.10.2.2.2 Proprietary `<Prtry>`

*Presence:* [1..1]

*Definition:* Specifies the local instrument, as a proprietary code.

*Datatype:* "Max35Text" on page 431

### 6.1.10.2.3 CategoryPurpose `<CtgyPurp>`

*Presence:* [0..1]

*Definition:* Specifies the high level purpose of the mandate based on a set of pre-defined categories.

**CategoryPurpose** `<CtgyPurp>` contains one of the following **CategoryPurpose1Choice** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| (Or | Code `<Cd>` | [1..1] | CodeSet | | 333 |
| (Or) | Proprietary `<Prtry>` | [1..1] | Text | | 333 |

### 6.1.10.2.3.1 Code `<Cd>`

*Presence:* [1..1]

*Definition:* Category purpose, as published in an external category purpose code list.

*Datatype:* "ExternalCategoryPurpose1Code" on page 414

### 6.1.10.2.3.2 Proprietary `<Prtry>`

*Presence:* [1..1]

*Definition:* Category purpose, in a proprietary form.

*Datatype:* "Max35Text" on page 431

### 6.1.10.2.4 Classification `<ClsSfcn>`

*Presence:* [0..1]

*Definition:* Type of direct debit instruction.

---

<!-- Page 334 -->

Classification <ClssCtn> contains one of the following elements (see "MandateClassification1Choice" on page 331 for details)



<table>
  <tr>
    <th>Or</th>
    <th>MessageElement&lt;XML Tag&gt;</th>
    <th>Mult.</th>
    <th>Type</th>
    <th>Constr. No.</th>
    <th>Page</th>
  </tr>
  <tr>
    <td>Or</td>
    <td>Code &lt;Cd&gt;</td>
    <td>[1..1]</td>
    <td>CodeSet</td>
    <td></td>
    <td>331</td>
  </tr>
  <tr>
    <td>Or</td>
    <td>Proprietary &lt;Prtry&gt;</td>
    <td>[1..1]</td>
    <td>Text</td>
    <td></td>
    <td>331</td>
  </tr>
</table>

## 6.1.11 Miscellaneous

### 6.11.1.1 SupplementaryData1

Definition: Additional information that can not be captured in the structured fields and/or any other specific block.



<table>
  <tr>
    <th>Or</th>
    <th>MessageElement&lt;XML Tag&gt;</th>
    <th>Mult.</th>
    <th>Type</th>
    <th>Constr. No.</th>
    <th>Page</th>
  </tr>
  <tr>
    <td></td>
    <td>PlaceAndNm &lt;PlcAndNm&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>334</td>
  </tr>
  <tr>
    <td></td>
    <td>Envelope &lt;Envlp&gt;</td>
    <td>[1..1]</td>
    <td>(External Schema)</td>
    <td></td>
    <td>334</td>
  </tr>
</table>

Constraints

* SupplementaryDataRule

This component may not be used without the explicit approval of a SEG and submission to the RA of ISO 20022 compliant structure(s) to be used in the Envelope element.

#### 6.11.1.1.1 PlaceAndNm <PlcAndNm>

Presence: [0..1]

Definition: Unambiguous reference to the location where the supplementary data must be inserted in the message instance.

In the case of XML, this is expressed by a valid XPath.

Datatype: "Max350Text" on page 431

#### 6.11.1.1.2 Envelope <Envlp>

Presence: [1..1]

Definition: Technical element wrapping the supplementary data.

Type: (External Schema)

Technical component that contains the validated supplementary data information. This technical envelope allows to segregate the supplementary data information from any other information.

### 6.11.1.2 Purpose2Choice

Definition: Specifies the underlying reason for the payment transaction.

Usage: Purpose is used by the end-customers, that is initiating party, (ultimate) debtor, (ultimate) creditor to provide information concerning the nature of the payment. Purpose is a content element, which is not used for processing by any of the agents involved in the payment chain.

---

<!-- Page 335 -->

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| Or | Code <Cd> | [1..1] | CodeSet | | 335 |
| Or | Proprietary <Ptry> | [1..1] | Text | | 335 |

## 6.1.11.2.1 Code <Cd>

*Presence:* [1..1]

*Definition:* Underlying reason for the payment transaction, as published in an external purpose code list.

*Datatype:* "ExternalPurpose1Code" on page 419

## 6.1.11.2.2 Proprietary <Ptry>

*Presence:* [1..1]

*Definition:* Purpose, in a proprietary form.

*Datatype:* "Max35Text" on page 431

## 6.1.11.3 NumberOfTransactionsPerStatus5

*Definition:* Set of elements used to provide detailed information on the number of transactions that are reported with a specific transaction status.

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | DetailedNumberOfTransactions <DtldNbOfTxs> | [1..1] | Text | | 335 |
| | DetailedStatus <DtldSts> | [1..1] | CodeSet | | 335 |
| | DetailedControlSum <DtldCtrlSum> | [0..1] | Quantity | | 335 |

### 6.1.11.3.1 DetailedNumberOfTransactions <DtldNbOfTxs>

*Presence:* [1..1]

*Definition:* Number of individual transactions contained in the message, detailed per status.

*Datatype:* "Max15NumericText" on page 430

### 6.1.11.3.2 DetailedStatus <DtldSts>

*Presence:* [1..1]

*Definition:* Common transaction status for all individual transactions reported.

*Datatype:* "ExternalPaymentTransactionStatus1Code" on page 418

### 6.1.11.3.3 DetailedControlSum <DtldCtrlSum>

*Presence:* [0..1]

*Definition:* Total of all individual amounts included in the message, irrespective of currencies, detailed per status.

*Datatype:* "DecimalNumber" on page 427

---

<!-- Page 336 -->

## 6.1.11.4 Authorisation1Choice

*Definition:* Provides the details on the user identification or any user key that allows to check if the initiating party is allowed to issue the transaction.

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| Or | Code <Cd> | [1..1] | CodeSet | | 336 |
| Or | Proprietary <Prtry> | [1..1] | Text | | 336 |

### 6.1.11.4.1 Code <Cd>

*Presence:* [1..1]

*Definition:* Specifies the authorisation, in a coded form.

*Datatype:* "Authorisation1Code" on page 410

| CodeName | Name | Definition |
|---|---|---|
| AUTH | PreAuthorisedFile | Indicates a file has been pre authorised or approved within the originating customer environment and no further approval is required. |
| FDET | FileLevelAuthorisationDetails | Indicates that a file requires additional file level approval, with the ability to view both the payment information block and supporting customer credit transaction detail. |
| FSUM | FileLevelAuthorisationSummary | Indicates that a file requires additional file level approval, with the ability to view only the payment information block level information. |
| ILEV | InstructionLevelAuthorisation | Indicates that a file requires all customer transactions to be authorised or approved. |

### 6.1.11.4.2 Proprietary <Prtry>

*Presence:* [1..1]

*Definition:* Specifies the authorisation, in a free text form.

*Datatype:* "Max128Text" on page 429

## 6.1.12 Party Identification

### 6.1.12.1 PartyIdentification272

*Definition:* Specifies the identification of a person or an organisation.

---

<!-- Page 337 -->

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Name `<Nm>` | [0..1] | Text | | 337 |
| | PostalAddress `<PstlAdr>` | [0..1] | ± | | 338 |
| | Identification `<Id>` | [0..1] | | | 338 |
| (Or | OrganisationIdentification `<OrgId>` | [1..1] | | | 339 |
| | AnyBIC `<AnyBIC>` | [0..1] | IdentifierSet | C5 | 340 |
| | LEI `<LEI>` | [0..1] | IdentifierSet | | 340 |
| | Other `<Othr>` | [0..*] | | | 340 |
| | Identification `<Id>` | [1..1] | Text | | 341 |
| | SchemeName `<SchmeNm>` | [0..1] | | | 341 |
| (Or | Code `<Cd>` | [1..1] | CodeSet | | 341 |
| Or) | Proprietary `<Ptry>` | [1..1] | Text | | 341 |
| | Issuer `<Issr>` | [0..1] | Text | | 341 |
| Or) | PrivateIdentification `<PrvtId>` | [1..1] | | | 341 |
| | DateAndPlaceOfBirth `<DtAndPlcOfBirth>` | [0..1] | | | 342 |
| | BirthDate `<BirthDt>` | [1..1] | Date | | 342 |
| | ProvinceOfBirth `<PrvcOfBirth>` | [0..1] | Text | | 342 |
| | CityOfBirth `<CityOfBirth>` | [1..1] | Text | | 343 |
| | CountryOfBirth `<CtryOfBirth>` | [1..1] | CodeSet | C7 | 343 |
| | Other `<Othr>` | [0..*] | | | 343 |
| | Identification `<Id>` | [1..1] | Text | | 343 |
| | SchemeName `<SchmeNm>` | [0..1] | | | 343 |
| (Or | Code `<Cd>` | [1..1] | CodeSet | | 344 |
| Or) | Proprietary `<Ptry>` | [1..1] | Text | | 344 |
| | Issuer `<Issr>` | [0..1] | Text | | 344 |
| | CountryOfResidence `<CtryOfRes>` | [0..1] | CodeSet | C7 | 344 |
| | ContactDetails `<CtctDtls>` | [0..1] | ± | | 344 |

**6.1.12.1.1 Name `<Nm>`**

*Presence:* [0..1]

*Definition:* Name by which a party is known and which is usually used to identify that party.

*Datatype:* "Max140Text" on page 429

---

<!-- Page 338 -->

## 6.1.12.1.2 PostalAddress <PstlAdr>

*Presence:* [0..1]

*Definition:* Information that locates and identifies a specific address, as defined by postal services.

**PostalAddress <PstlAdr>** contains the following elements (see "PostalAddress27" on page 357 for details)



| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | AddressType <AdrTp> | [0..1] |  |  | 357 |
| (Or | Code <Cd> | [1..1] | CodeSet |  | 358 |
| Or) | Proprietary <Ptry> | [1..1] | ± |  | 358 |
| | CareOf <CareOf> | [0..1] | Text |  | 358 |
| | Department <Dept> | [0..1] | Text |  | 358 |
| | SubDepartment <SubDept> | [0..1] | Text |  | 359 |
| | StreetName <StrtNm> | [0..1] | Text |  | 359 |
| | BuildingNumber <BldgNb> | [0..1] | Text |  | 359 |
| | BuildingName <BldgNm> | [0..1] | Text |  | 359 |
| | Floor <Flr> | [0..1] | Text |  | 359 |
| | UnitNumber <UnitNb> | [0..1] | Text |  | 359 |
| | PostBox <PstBx> | [0..1] | Text |  | 359 |
| | Room <Room> | [0..1] | Text |  | 359 |
| | PostCode <PstCd> | [0..1] | Text |  | 360 |
| | TownName <TwnNm> | [0..1] | Text |  | 360 |
| | TownLocationName <TwnLctnNm> | [0..1] | Text |  | 360 |
| | DistrictName <DstrctNm> | [0..1] | Text |  | 360 |
| | CountrySubDivision <CtrySubDvsn> | [0..1] | Text |  | 360 |
| | Country <Ctry> | [0..1] | CodeSet | C7 | 360 |
| | AddressLine <AdrLine> | [0..7] | Text |  | 360 |

## 6.1.12.1.3 Identification <Id>

*Presence:* [0..1]

*Definition:* Unique and unambiguous identification of a party.

---

<!-- Page 339 -->

Identification <Id> contains one of the following Party52Choice elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| (Or | OrganisationIdentification <OrgId> | [1..1] | | | 339 |
| | AnyBIC <AnyBIC> | [0..1] | IdentifierSet | C5 | 340 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 340 |
| | Other <Othr> | [0..*] | | | 340 |
| | Identification <Id> | [1..1] | Text | | 341 |
| | SchemeName <SchmeNm> | [0..1] | | | 341 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 341 |
| Or | Proprietary <Prtry> | [1..1] | Text | | 341 |
| | Issuer <Issr> | [0..1] | Text | | 341 |
| (Or | PrivateIdentification <PrvtId> | [1..1] | | | 341 |
| | DateAndPlaceOfBirth <DtAndPlcOfBirth> | [0..1] | | | 342 |
| | BirthDate <BirthDt> | [1..1] | Date | | 342 |
| | ProvinceOfBirth <PrvcOfBirth> | [0..1] | Text | | 342 |
| | CityOfBirth <CityOfBirth> | [1..1] | Text | | 343 |
| | CountryOfBirth <CtryOfBirth> | [1..1] | CodeSet | C7 | 343 |
| | Other <Othr> | [0..*] | | | 343 |
| | Identification <Id> | [1..1] | Text | | 343 |
| | SchemeName <SchmeNm> | [0..1] | | | 343 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 344 |
| Or | Proprietary <Prtry> | [1..1] | Text | | 344 |
| | Issuer <Issr> | [0..1] | Text | | 344 |

**6.1.12.1.3.1 OrganisationIdentification <OrgId>**

*Presence: [1..1]*

*Definition: Unique and unambiguous way to identify an organisation.*

---

<!-- Page 340 -->

OrganisationIdentification <OrgId> contains the following OrganisationIdentification39 elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | AnyBIC <AnyBIC> | [0..1] | IdentifierSet | C5 | 340 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 340 |
| | Other <Othr> | [0..*] | | | 340 |
| | Identification <Id> | [1..1] | Text | | 341 |
| | SchemeName <SchmeNm> | [0..1] | | | 341 |
| {Or | Code <Cd> | [1..1] | CodeSet | | 341 |
| Or} | Proprietary <Pprty> | [1..1] | Text | | 341 |
| | Issuer <Issr> | [0..1] | Text | | 341 |

**6.1.12.1.3.1.1 AnyBIC <AnyBIC>**

*Presence:* [0..1]

*Definition:* Business identification code of the organisation.

*Impacted by:* C5 "AnyBIC"

*Datatype:* "AnyBICDec2014Identifier" on page 425

**Constraints**

- **AnyBIC**

Only a valid Business identifier code is allowed. Business identifier codes for financial or non-financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.

**6.1.12.1.3.1.2 LEI <LEI>**

*Presence:* [0..1]

*Definition:* Legal entity identification as an alternate identification for a party.

*Datatype:* "LEIIdentifier" on page 426

**6.1.12.1.3.1.3 Other <Othr>**

*Presence:* [0..*]

*Definition:* Unique identification of an organisation, as assigned by an institution, using an identification scheme.

---

<!-- Page 341 -->

Other <Other> contains the following GenericOrganisationIdentification3 elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Identification <Id> | [1..1] | Text | | 341 |
| | SchemeName <SchmeNm> | [0..1] | | | 341 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 341 |
| Or) | Proprietary <Ptry> | [1..1] | Text | | 341 |
| | Issuer <Issr> | [0..1] | Text | | 341 |

**6.1.12.1.3.3.1 Identification <Id>**

*Presence:* [1..1]

*Definition:* Identification assigned by an institution.

*Datatype:* "Max256Text" on page 430

**6.1.12.1.3.3.2 SchemeName <SchmeNm>**

*Presence:* [0..1]

*Definition:* Name of the identification scheme.

**SchemeName <SchmeNm>** contains one of the following OrganisationIdentificationSchemeName1Choice elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| (Or | Code <Cd> | [1..1] | CodeSet | | 341 |
| Or) | Proprietary <Ptry> | [1..1] | Text | | 341 |

**6.1.12.1.3.3.2.1 Code <Cd>**

*Presence:* [1..1]

*Definition:* Name of the identification scheme, in a coded form as published in an external list.

*Datatype:* "ExternalOrganisationIdentification1Code" on page 417

**6.1.12.1.3.3.2.2 Proprietary <Ptry>**

*Presence:* [1..1]

*Definition:* Name of the identification scheme, in a free text form.

*Datatype:* "Max35Text" on page 431

**6.1.12.1.3.3.3 Issuer <Issr>**

*Presence:* [0..1]

*Definition:* Entity that assigns the identification.

*Datatype:* "Max35Text" on page 431

**6.1.12.1.3.2 PrivateIdentification <PrvtId>**

*Presence:* [1..1]

---

<!-- Page 342 -->

*Definition: Unique and unambiguous identification of a person, for example a passport.*

**PrivateIdentification <PrvIdt>** contains the following **PersonIdentification18** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | DateAndPlaceOfBirth <DtAndPlcOfBirth> | [0..1] | | | 342 |
| | BirthDate <BirthDt> | [1..1] | Date | | 342 |
| | ProvinceOfBirth <PrvcOfBirth> | [1..1] | Text | | 342 |
| | CityOfBirth <CityOfBirth> | [1..1] | Text | | 343 |
| | CountryOfBirth <CtryOfBirth> | [1..1] | CodeSet | C7 | 343 |
| | Other <Othr> | [0..*] | | | 343 |
| | Identification <Id> | [1..1] | Text | | 343 |
| | SchemeName <SchmeNm> | [0..1] | | | 343 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 344 |
| Or) | Proprietary <Ptry> | [1..1] | Text | | 344 |
| | Issuer <Issr> | [0..1] | Text | | 344 |

**6.1.12.1.3.2.1 DateAndPlaceOfBirth <DtAndPlcOfBirth>**

*Presence: [0..1]*

*Definition: Date and place of birth of a person.*

**DateAndPlaceOfBirth <DtAndPlcOfBirth>** contains the following **DateAndPlaceOfBirth1** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | BirthDate <BirthDt> | [1..1] | Date | | 342 |
| | ProvinceOfBirth <PrvcOfBirth> | [0..1] | Text | | 342 |
| | CityOfBirth <CityOfBirth> | [1..1] | Text | | 343 |
| | CountryOfBirth <CtryOfBirth> | [1..1] | CodeSet | C7 | 343 |

**6.1.12.1.3.2.1.1 BirthDate <BirthDt>**

*Presence: [1..1]*

*Definition: Date on which a person is born.*

*Datatype: "ISODate" on page 425*

**6.1.12.1.3.2.1.2 ProvinceOfBirth <PrvcOfBirth>**

*Presence: [0..1]*

*Definition: Province where a person was born.*

*Datatype: "Max35Text" on page 431*

---

<!-- Page 343 -->

6.1.12.1.3.2.1.3 **CityOfBirth** *&lt;CityOfBirth&gt;*

*Presence:* [1..1]

*Definition:* City where a person was born.

*Datatype:* "Max35Text" on page 431

6.1.12.1.3.2.1.4 **CountryOfBirth** *&lt;CtryOfBirth&gt;*

*Presence:* [1..1]

*Definition:* Country where a person was born.

*Impacted by:* C7 "Country"

*Datatype:* "CountryCode" on page 412

**Constraints**

- **Country**

The code is checked against the list of country names obtained from the United Nations (ISO 3166, Alpha-2 code).

6.1.12.1.3.2.2 **Other** *&lt;Othr&gt;*

*Presence:* [0..*]

*Definition:* Unique identification of a person, as assigned by an institution, using an identification scheme.

**Other** *&lt;Othr&gt;* contains the following **GenericPersonIdentification2** elements

| Or | MessageElement&lt;XML Tag&gt; | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Identification *&lt;Id&gt;* | [1..1] | Text | | 343 |
| | SchemeName *&lt;SchmeNm&gt;* | [0..1] | | | 343 |
| Or | Code *&lt;Cd&gt;* | [1..1] | CodeSet | | 344 |
| Or | Proprietary *&lt;Ptry&gt;* | [1..1] | Text | | 344 |
| | Issuer *&lt;Issr&gt;* | [0..1] | Text | | 344 |

6.1.12.1.3.2.2.1 **Identification** *&lt;Id&gt;*

*Presence:* [1..1]

*Definition:* Unique and unambiguous identification of a person.

*Datatype:* "Max256Text" on page 430

6.1.12.1.3.2.2.2 **SchemeName** *&lt;SchmeNm&gt;*

*Presence:* [0..1]

*Definition:* Name of the identification scheme.

---

<!-- Page 344 -->

SchemeName <SchemeNm> contains one of the following
PersonIdentificationSchemeName1Choice elements



| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| (Or | Code <Cd> | [1..1] | CodeSet | | 344 |
| Or) | Proprietary <Prt> | [1..1] | Text | | 344 |

**6.1.12.1.3.2.2.1 Code <Cd>**

*Presence:* [1..1]

*Definition:* Name of the identification scheme, in a coded form as published in an external list.

*Datatype:* "ExternalPersonIdentification1Code" on page 418

**6.1.12.1.3.2.2.2 Proprietary <Prt>**

*Presence:* [1..1]

*Definition:* Name of the identification scheme, in a free text form.

*Datatype:* "Max35Text" on page 431

**6.1.12.1.3.2.2.3 Issuer <Issr>**

*Presence:* [0..1]

*Definition:* Entity that assigns the identification.

*Datatype:* "Max35Text" on page 431

**6.1.12.1.4 CountryOfResidence <CtryOfRes>**

*Presence:* [0..1]

*Definition:* Country in which a person resides (the place of a person's home). In the case of a company, it is the country from which the affairs of that company are directed.

*Impacted by:* C7 "Country"

*Datatype:* "CountryCode" on page 412

**Constraints**

- **Country**

  The code is checked against the list of country names obtained from the United Nations (ISO 3166, Alpha-2 code).

**6.1.12.1.5 ContactDetails <CtctDtls>**

*Presence:* [0..1]

*Definition:* Set of elements used to indicate how to contact the party.

---

<!-- Page 345 -->

ContactDetails <CctDtls> contains the following elements (see "Contact13" on page 354 for details)



<table>
  <tr>
    <th>Or</th>
    <th>MessageElement&lt;XML Tag&gt;</th>
    <th>Mult.</th>
    <th>Type</th>
    <th>Constr. No.</th>
    <th>Page</th>
  </tr>
  <tr>
    <td></td>
    <td>NamePrefix &lt;NmPrfx&gt;</td>
    <td>[0..1]</td>
    <td>CodeSet</td>
    <td></td>
    <td>354</td>
  </tr>
  <tr>
    <td></td>
    <td>Name &lt;Nm&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>355</td>
  </tr>
  <tr>
    <td></td>
    <td>PhoneNumber &lt;PhneNb&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>355</td>
  </tr>
  <tr>
    <td></td>
    <td>MobileNumber &lt;MobNb&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>355</td>
  </tr>
  <tr>
    <td></td>
    <td>FaxNumber &lt;FaxNb&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>355</td>
  </tr>
  <tr>
    <td></td>
    <td>URLAddress &lt;URLAdr&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>355</td>
  </tr>
  <tr>
    <td></td>
    <td>EmailAddress &lt;EmailAdr&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>355</td>
  </tr>
  <tr>
    <td></td>
    <td>EmailPurpose &lt;EmailPurp&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>355</td>
  </tr>
  <tr>
    <td></td>
    <td>JobTitle &lt;JobTtl&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>355</td>
  </tr>
  <tr>
    <td></td>
    <td>Responsibility &lt;Rspnsblty&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>356</td>
  </tr>
  <tr>
    <td></td>
    <td>Department &lt;Dept&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>356</td>
  </tr>
  <tr>
    <td></td>
    <td>Other &lt;Othr&gt;</td>
    <td>[0..*]</td>
    <td></td>
    <td></td>
    <td>356</td>
  </tr>
  <tr>
    <td></td>
    <td>ChannelType &lt;ChanlTp&gt;</td>
    <td>[1..1]</td>
    <td>Text</td>
    <td></td>
    <td>356</td>
  </tr>
  <tr>
    <td></td>
    <td>Identification &lt;Id&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>356</td>
  </tr>
  <tr>
    <td></td>
    <td>PreferredMethod &lt;PrefrlMtd&gt;</td>
    <td>[0..1]</td>
    <td>CodeSet</td>
    <td></td>
    <td>356</td>
  </tr>
</table>

## 6.1.13 Payment

### 6.1.13.1 InstructionForCreditorAgent3

*Definition:* Further information related to the processing of the payment instruction that may need to be acted upon by the creditor's agent. The instruction may relate to a level of service, or may be an instruction that has to be executed by the creditor's agent, or may be information required by the creditor's agent.



<table>
  <tr>
    <th>Or</th>
    <th>MessageElement&lt;XML Tag&gt;</th>
    <th>Mult.</th>
    <th>Type</th>
    <th>Constr. No.</th>
    <th>Page</th>
  </tr>
  <tr>
    <td></td>
    <td>Code &lt;Cd&gt;</td>
    <td>[0..1]</td>
    <td>CodeSet</td>
    <td></td>
    <td>345</td>
  </tr>
  <tr>
    <td></td>
    <td>InstructionInformation &lt;InstrInf&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>346</td>
  </tr>
</table>

#### 6.1.13.1.1 Code <Cd>

*Presence:* [0..1]

*Definition:* Coded information related to the processing of the payment instruction, provided by the initiating party, and intended for the creditor's agent.

*Datatype:* "ExternalCreditorAgentInstruction1Code" on page 415

---

<!-- Page 346 -->

6.1.13.1.2 InstructionInformation <InstrInf>

*Presence:* [0..1]

*Definition:* Further information complementing the coded instruction or instruction to the creditor's agent that is bilaterally agreed or specific to a user community.

*Datatype:* "Max140Text" on page 429

## 6.1.14 Payment Type

### 6.1.14.1 PaymentTypeInformation26

*Definition:* Provides further details of the type of payment.

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | InstructionPriority <InstrPrty> | [0..1] | CodeSet | | 346 |
| | ServiceLevel <SvcLvl> | [0..*] | | | 346 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 347 |
| Or) | Proprietary <Prtry> | [1..1] | Text | | 347 |
| | LocalInstrument <LclInstrm> | [0..1] | | | 347 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 347 |
| Or) | Proprietary <Prtry> | [1..1] | Text | | 347 |
| | CategoryPurpose <CtgyPurp> | [0..1] | | | 347 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 348 |
| Or) | Proprietary <Prtry> | [1..1] | Text | | 348 |

#### 6.1.14.1.1 InstructionPriority <InstrPrty>

*Presence:* [0..1]

*Definition:* Indicator of the urgency or order of importance that the instructing party would like the instructed party to apply to the processing of the instruction.

*Datatype:* "Priority2Code" on page 422

| CodeName | Name | Definition |
|---|---|---|
| HIGH | High | Priority level is high. |
| NORM | Normal | Priority level is normal. |

#### 6.1.14.1.2 ServiceLevel <SvcLvl>

*Presence:* [0..*]

*Definition:* Agreement under which or rules under which the transaction should be processed.

---

<!-- Page 347 -->

`ServiceLevel <SvcLvl>` contains one of the following `ServiceLevel8Choice` elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| Or | Code <Cd> | [1..1] | CodeSet | | 347 |
| Or | Proprietary <Ptry> | [1..1] | Text | | 347 |

### 6.1.14.1.2.1 Code <Cd>

*Presence:* [1..1]

*Definition:* Specifies a pre-agreed service or level of service between the parties, as published in an external service level code list.

*Datatype:* "ExternalServiceLevel1Code" on page 419

### 6.1.14.1.2.2 Proprietary <Ptry>

*Presence:* [1..1]

*Definition:* Specifies a pre-agreed service or level of service between the parties, as a proprietary code.

*Datatype:* "Max35Text" on page 431

## 6.1.14.1.3 LocalInstrument <LclInstrm>

*Presence:* [0..1]

*Definition:* User community specific instrument.

Usage: This element is used to specify a local instrument, local clearing option and/or further qualify the service or service level.

`LocalInstrument <LclInstrm>` contains one of the following `LocalInstrument2Choice` elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| Or | Code <Cd> | [1..1] | CodeSet | | 347 |
| Or | Proprietary <Ptry> | [1..1] | Text | | 347 |

### 6.1.14.1.3.1 Code <Cd>

*Presence:* [1..1]

*Definition:* Specifies the local instrument, as published in an external local instrument code list.

*Datatype:* "ExternalLocalInstrument1Code" on page 417

### 6.1.14.1.3.2 Proprietary <Ptry>

*Presence:* [1..1]

*Definition:* Specifies the local instrument, as a proprietary code.

*Datatype:* "Max35Text" on page 431

## 6.1.14.1.4 CategoryPurpose <CtgyPurp>

*Presence:* [0..1]

*Definition:* Specifies the high level purpose of the instruction based on a set of pre-defined categories.

---

<!-- Page 348 -->

Usage: This is used by the initiating party to provide information concerning the processing of the payment. It is likely to trigger special processing by any of the agents involved in the payment chain.
**CategoryPurpose <CtgyPurp>** contains one of the following **CategoryPurpose1Choice** elements

| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| (Or | Code <Cd> | [1..1] | CodeSet | | 348 |
| Or) | Proprietary <Ptry> | [1..1] | Text | | 348 |

**6.1.14.1.1 Code <Cd>**
*Presence: [1..1]*
*Definition:* Category purpose, as published in an external category purpose code list.
*Datatype:* "ExternalCategoryPurpose1Code" on page 414

**6.1.14.1.2 Proprietary <Ptry>**
*Presence: [1..1]*
*Definition:* Category purpose, in a proprietary form.
*Datatype:* "Max35Text" on page 431

**6.1.14.2 PaymentTypeInformation29**
*Definition:* Provides further details of the type of payment.

| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | InstructionPriority <InstrPty> | [0..1] | CodeSet | | 348 |
| | ServiceLevel <SvcLv> | [0..*] | | | 349 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 349 |
| Or) | Proprietary <Ptry> | [1..1] | Text | | 349 |
| | LocalInstrument <LfInstrm> | [0..1] | | | 349 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 349 |
| Or) | Proprietary <Ptry> | [1..1] | Text | | 350 |
| | SequenceType <SeqTp> | [0..1] | CodeSet | | 350 |
| | CategoryPurpose <CtgyPurp> | [0..1] | | | 350 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 350 |
| Or) | Proprietary <Ptry> | [1..1] | Text | | 350 |

**6.1.14.2.1 InstructionPriority <InstrPty>**
*Presence: [0..1]*
*Definition:* Indicator of the urgency or order of importance that the instructing party would like the instructed party to apply to the processing of the instruction.

---

<!-- Page 349 -->

Datatype: "Priority2Code" on page 422

| CodeName | Name | Definition |
| :--- | :--- | :--- |
| HIGH | High | Priority level is high. |
| NORM | Normal | Priority level is normal. |

## 6.1.14.2.2 ServiceLevel <SvcLvl>

*Presence: [0..]*

*Definition: Agreement under which or rules under which the transaction should be processed.*

**ServiceLevel <SvcLvl>** contains one of the following **ServiceLevel1Choice** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
| :--- | :--- | :--- | :--- | :--- | :--- |
| (Or | Code <Cd> | [1..1] | CodeSet | | 349 |
| Or) | Proprietary <Ptry> | [1..1] | Text | | 349 |

### 6.1.14.2.2.1 Code <Cd>

*Presence: [1..1]*

*Definition: Specifies a pre-agreed service or level of service between the parties, as published in an external service level code list.*

*Datatype: "ExternalServiceLevel1Code" on page 419*

### 6.1.14.2.2.2 Proprietary <Ptry>

*Presence: [1..1]*

*Definition: Specifies a pre-agreed service or level of service between the parties, as a proprietary code.*

*Datatype: "Max35Text" on page 431*

## 6.1.14.2.3 LocalInstrument <LclInstrm>

*Presence: [0..1]*

*Definition: User community specific instrument.*

Usage: This element is used to specify a local instrument, local clearing option and/or further qualify the service or service level.

**LocalInstrument <LclInstrm>** contains one of the following **LocalInstrument1Choice** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
| :--- | :--- | :--- | :--- | :--- | :--- |
| (Or | Code <Cd> | [1..1] | CodeSet | | 349 |
| Or) | Proprietary <Ptry> | [1..1] | Text | | 350 |

### 6.1.14.2.3.1 Code <Cd>

*Presence: [1..1]*

*Definition: Specifies the local instrument, as published in an external local instrument code list.*

*Datatype: "ExternalLocalInstrument1Code" on page 417*

---

<!-- Page 350 -->

**6.1.4.2.3.2 Proprietary <Ptrty>**
*Presence:* [1..1]
*Definition:* Specifies the local instrument, as a proprietary code.
*Datatype:* "Max35Text" on page 431

**6.1.4.2.4 SequenceType <SeqTp>**
*Presence:* [0..1]
*Definition:* Identifies the direct debit sequence, such as first, recurrent, final or one-off.
*Datatype:* "SequenceType3Code" on page 423

| CodeName | Name | Definition |
| :--- | :--- | :--- |
| FRST | First | First collection of a series of direct debit instructions. |
| RCUR | Recurring | Direct debit instruction where the debtor's authorisation is used for regular direct debit transactions initiated by the creditor. |
| FINAL | Final | Final collection of a series of direct debit instructions. |
| OOFF | OneOff | Direct debit instruction where the debtor's authorisation is used to initiate one single direct debit transaction. |
| RPRE | Represented | Collection used to re-present previously reversed or returned direct debit transactions. |

**6.1.4.2.5 CategoryPurpose <CtgyPurp>**
*Presence:* [0..1]
*Definition:* Specifies the high level purpose of the instruction based on a set of pre-defined categories.

Usage: This is used by the initiating party to provide information concerning the processing of the payment. It is likely to trigger special processing by any of the agents involved in the payment chain.
**CategoryPurpose <CtgyPurp>** contains one of the following **CategoryPurpose1Choice** elements

| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
| :--- | :--- | :--- | :--- | :--- | :--- |
| [Or | Code <Cd> | [1..1] | CodeSet | | 350 |
| Or | Proprietary <Ptrty> | [1..1] | Text | | 350 |

**6.1.4.2.5.1 Code <Cd>**
*Presence:* [1..1]
*Definition:* Category purpose, as published in an external category purpose code list.
*Datatype:* "ExternalCategoryPurpose1Code" on page 414

**6.1.4.2.5.2 Proprietary <Ptrty>**
*Presence:* [1..1]

---

<!-- Page 351 -->

Definition: Category purpose, in a proprietary form.
Datatype: "Max35Text" on page 431

## 6.1.14.3 PaymentTypeInfo27

Definition: Provides further details of the type of payment.

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | InstructionPriority <InstrPrty> | [0..1] | CodeSet | | 351 |
| | ClearingChannel <ClrChanl> | [0..1] | CodeSet | | 351 |
| | ServiceLevel <SvcLv> | [0..*] | | | 352 |
| Or | Code <Cd> | [1..1] | CodeSet | | 352 |
| Or | Proprietary <Prtry> | [1..1] | Text | | 352 |
| | LocalInstrument <LocInstrm> | [0..1] | | | 352 |
| Or | Code <Cd> | [1..1] | CodeSet | | 352 |
| Or | Proprietary <Prtry> | [1..1] | Text | | 353 |
| | SequenceType <SeqTp> | [0..1] | CodeSet | | 353 |
| | CategoryPurpose <CtgyPurp> | [0..1] | | | 353 |
| Or | Code <Cd> | [1..1] | CodeSet | | 353 |
| Or | Proprietary <Prtry> | [1..1] | Text | | 353 |

### 6.1.14.3.1 InstructionPriority <InstrPrty>

Presence: [0..1]

Definition: Indicator of the urgency or order of importance that the instructing party would like the instructed party to apply to the processing of the instruction.

Datatype: "Priority2Code" on page 422

| CodeName | Name | Definition |
|---|---|---|
| HIGH | High | Priority level is high. |
| NORM | Normal | Priority level is normal. |

### 6.1.14.3.2 ClearingChannel <ClrChanl>

Presence: [0..1]

Definition: Specifies the clearing channel to be used to process the payment instruction.

Datatype: "ClearingChannel2Code" on page 412

| CodeName | Name | Definition |
|---|---|---|
| RTGS | RealTimeGrossSettlementSystem | Clearing channel is a real-time gross settlement system. |
| RTNS | RealTimeNetSettlementSystem | Clearing channel is a real-time net settlement system. |

---

<!-- Page 352 -->

| CodeName | Name | Definition |
|---|---|---|
| MPNS | MassPaymentNetSystem | Clearing channel is a mass payment net settlement system. |
| BOOK | BookTransfer | Payment through internal book transfer. |

### 6.1.14.3.3 ServiceLevel <SvcLvl>

*Presence:* [0..*]

*Definition:* Agreement under which or rules under which the transaction should be processed.

**ServiceLevel <SvcLvl>** contains one of the following **ServiceLevel8Choice** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| (Or | Code <Cd> | [1..1] | CodeSet | | 352 |
| Or) | Proprietary <Ptry> | [1..1] | Text | | 352 |

#### 6.1.14.3.3.1 Code <Cd>

*Presence:* [1..1]

*Definition:* Specifies a pre-agreed service or level of service between the parties, as published in an external service level code list.

*Datatype:* "ExternalServiceLevel1Code" on page 419

#### 6.1.14.3.3.2 Proprietary <Ptry>

*Presence:* [1..1]

*Definition:* Specifies a pre-agreed service or level of service between the parties, as a proprietary code.

*Datatype:* "Max35Text" on page 431

### 6.1.14.3.4 LocalInstrument <LclInstrm>

*Presence:* [0..1]

*Definition:* User community specific instrument.

Usage: This element is used to specify a local instrument, local clearing option and/or further qualify the service or service level.

**LocalInstrument <LclInstrm>** contains one of the following **LocalInstrument2Choice** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| (Or | Code <Cd> | [1..1] | CodeSet | | 352 |
| Or) | Proprietary <Ptry> | [1..1] | Text | | 353 |

#### 6.1.14.3.4.1 Code <Cd>

*Presence:* [1..1]

*Definition:* Specifies the local instrument, as published in an external local instrument code list.

*Datatype:* "ExternalLocalInstrument1Code" on page 417

---

<!-- Page 353 -->

## 6.1.14.3.4.2 Proprietary <Ptrty>

*Presence:* [1..1]

*Definition:* Specifies the local instrument, as a proprietary code.

*Datatype:* "Max35Text" on page 431

## 6.1.14.3.5 SequenceType <SeqTp>

*Presence:* [0..1]

*Definition:* Identifies the direct debit sequence, such as first, recurrent, final or one-off.

*Datatype:* "SequenceType3Code" on page 423

| CodeName | Name | Definition |
| :--- | :--- | :--- |
| FRST | First | First collection of a series of direct debit instructions. |
| RCUR | Recurring | Direct debit instruction where the debtor's authorisation is used for regular direct debit transactions initiated by the creditor. |
| FINAL | Final | Final collection of a series of direct debit instructions. |
| OOFF | OneOff | Direct debit instruction where the debtor's authorisation is used to initiate one single direct debit transaction. |
| RPPE | Represented | Collection used to re-present previously reversed or returned direct debit transactions. |

## 6.1.14.3.6 CategoryPurpose <CtgyPurp>

*Presence:* [0..1]

*Definition:* Specifies the high level purpose of the instruction based on a set of pre-defined categories.

Usage: This is used by the initiating party to provide information concerning the processing of the payment. It is likely to trigger special processing by any of the agents involved in the payment chain.

**CategoryPurpose <CtgyPurp>** contains one of the following **CategoryPurpose1Choice** elements

| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Or | Code <Cd> | [1..1] | CodeSet | | 353 |
| Or | Proprietary <Ptrty> | [1..1] | Text | | 353 |

### 6.1.14.3.6.1 Code <Cd>

*Presence:* [1..1]

*Definition:* Category purpose, as published in an external category purpose code list.

*Datatype:* "ExternalCategoryPurpose1Code" on page 414

### 6.1.14.3.6.2 Proprietary <Ptrty>

*Presence:* [1..1]

---

<!-- Page 354 -->

Definition: Category purpose, in a proprietary form.
Datatype: "Max35Text" on page 431

# 6.1.15 Person Identification

## 6.1.15.1 Contact13
Definition: Specifies the details of the contact person.

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | NamePrefix <NmPrfx> | [0..1] | CodeSet | | 354 |
| | Name <Nm> | [0..1] | Text | | 355 |
| | PhoneNumber <PhneNb> | [0..1] | Text | | 355 |
| | MobileNumber <MobNb> | [0..1] | Text | | 355 |
| | FaxNumber <FaxNb> | [0..1] | Text | | 355 |
| | URLAddress <URLAdr> | [0..1] | Text | | 355 |
| | EmailAddress <EmailAdr> | [0..1] | Text | | 355 |
| | EmailPurpose <EmailPurp> | [0..1] | Text | | 355 |
| | JobTitle <JobTitl> | [0..1] | Text | | 355 |
| | Responsibility <Rspnsblty> | [0..1] | Text | | 356 |
| | Department <Dept> | [0..1] | Text | | 356 |
| | Other <Othr> | [0..*] | | | 356 |
| | ChannelType <ChaniTyp> | [1..1] | Text | | 356 |
| | Identification <Id> | [0..1] | Text | | 356 |
| | PreferredMethod <PrefrdMtd> | [0..1] | CodeSet | | 356 |

### 6.1.15.1.1 NamePrefix <NmPrfx>
Presence: [0..1]

Definition: Specifies the terms used to formally address a person.
Datatype: "NamePrefix2Code" on page 420

| CodeName | Name | Definition |
|---|---|---|
| DOCT | Doctor | Title of the person is Doctor or Dr. |
| MADM | Madam | Title of the person is Madam. |
| MISS | Miss | Title of the person is Miss. |
| MIST | Mister | Title of the person is Mister or Mr. |
| MIKS | GenderNeutral | Title of the person is gender neutral (Mx). |

---

<!-- Page 355 -->

**6.1.15.1.2 Name <Nm>**

*Presence:* [0..1]

*Definition:* Name by which a party is known and which is usually used to identify that party.

*Datatype:* "Max140Text" on <u>page 429</u>

**6.1.15.1.3 PhoneNumber <PhoneNb>**

*Presence:* [0..1]

*Definition:* Collection of information that identifies a phone number, as defined by telecom services.

*Datatype:* "PhoneNumber" on <u>page 431</u>

**6.1.15.1.4 MobileNumber <MobNb>**

*Presence:* [0..1]

*Definition:* Collection of information that identifies a mobile phone number, as defined by telecom services.

*Datatype:* "PhoneNumber" on <u>page 431</u>

**6.1.15.1.5 FaxNumber <FaxNb>**

*Presence:* [0..1]

*Definition:* Collection of information that identifies a FAX number, as defined by telecom services.

*Datatype:* "PhoneNumber" on <u>page 431</u>

**6.1.15.1.6 URLAddress <URLAdr>**

*Presence:* [0..1]

*Definition:* Address for the Universal Resource Locator (URL), for example an address used over the www (HTTP) service.

*Datatype:* "Max2048Text" on <u>page 430</u>

**6.1.15.1.7 EmailAddress <EmailAdr>**

*Presence:* [0..1]

*Definition:* Address for electronic mail (e-mail).

*Datatype:* "Max256Text" on <u>page 430</u>

**6.1.15.1.8 EmailPurpose <EmailPurp>**

*Presence:* [0..1]

*Definition:* Purpose for which an email address may be used.

*Datatype:* "Max35Text" on <u>page 431</u>

**6.1.15.1.9 JobTitle <JobTitl>**

*Presence:* [0..1]

*Definition:* Title of the function.

*Datatype:* "Max35Text" on <u>page 431</u>

---

<!-- Page 356 -->

**6.1.15.1.10 Responsibility <Rspnsblty>**
*Presence:* [0..1]
*Definition:* Role of a person in an organisation.
*Datatype:* "Max35Text" on page 431

**6.1.15.1.11 Department <Dept>**
*Presence:* [0..1]
*Definition:* Identification of a division of a large organisation or building.
*Datatype:* "Max70Text" on page 431

**6.1.15.1.12 Other <Othr>**
*Presence:* [0..*]
*Definition:* Contact details in another form.
**Other <Othr>** contains the following **OtherContact1** elements

| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | ChannelType <ChnlTp> | [1..1] | Text | | 356 |
| | Identification <Id> | [0..1] | Text | | 356 |

**6.1.15.1.12.1 ChannelType <ChnlTp>**
*Presence:* [1..1]
*Definition:* Method used to contact the financial institution's contact for the specific tax region.
*Datatype:* "Max4Text" on page 431

**6.1.15.1.12.2 Identification <Id>**
*Presence:* [0..1]
*Definition:* Communication value such as phone number or email address.
*Datatype:* "Max128Text" on page 429

**6.1.15.1.13 PreferredMethod <PrfrdMtd>**
*Presence:* [0..1]
*Definition:* Preferred method used to reach the contact.
*Datatype:* "PreferredContactMethod2Code" on page 421

| CodeName | Name | Definition |
|---|---|---|
| MAIL | Email | Preferred method used to reach the contact is per email. |
| FAXX | Fax | Preferred method used to reach the contact is per fax. |
| LETT | Letter | Preferred method used to reach the contact is per letter. |

---

<!-- Page 357 -->

| CodeName | Name | Definition |
| :--- | :--- | :--- |
| CELL | MobileOrCellPhone | Preferred method used to reach the contact is per mobile or cell phone. |
| ONLI | Online | Preferred method used to reach the contact is online. |
| PHON | Phone | Preferred method used to reach the contact is per phone. |

## 6.1.16 Postal Address

### 6.1.16.1 PostalAddress27

*Definition:* Information that locates and identifies a specific address, as defined by postal services.

| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
| :--- | :--- | :--- | :--- | :--- | :--- |
| | AddressType <AdrTp> | [0..1] | | | 357 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 358 |
| Or) | Proprietary <Prtry> | [1..1] | ± | | 358 |
| | CareOf <CareOf> | [0..1] | Text | | 358 |
| | Department <Dept> | [0..1] | Text | | 358 |
| | SubDepartment <SubDept> | [0..1] | Text | | 359 |
| | StreetName <StrtNm> | [0..1] | Text | | 359 |
| | BuildingNumber <BldgNb> | [0..1] | Text | | 359 |
| | BuildingName <BldgNm> | [0..1] | Text | | 359 |
| | Floor <Flr> | [0..1] | Text | | 359 |
| | UnitNumber <UnitNb> | [0..1] | Text | | 359 |
| | PostBox <PstBx> | [0..1] | Text | | 359 |
| | Room <Room> | [0..1] | Text | | 359 |
| | PostCode <PstCd> | [0..1] | Text | | 360 |
| | TownName <TwnNm> | [0..1] | Text | | 360 |
| | TownLocationName <TwnLctnNm> | [0..1] | Text | | 360 |
| | DistrictName <DstrctNm> | [0..1] | Text | | 360 |
| | CountrySubDivision <CtrySubDvsn> | [0..1] | Text | | 360 |
| | Country <Ctry> | [0..1] | CodeSet | C7 | 360 |
| | AddressLine <AdrLine> | [0..7] | Text | | 360 |

#### 6.1.16.1.1 AddressType <AdrTp>

*Presence:* [0..1]

---

<!-- Page 358 -->

*Definition: Identifies the nature of the postal address.*

**AddressType <AdrTp>** contains one of the following AddressType3Choice elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| (Or | Code <Cd> | [1..1] | CodeSet | | 358 |
| Or) | Proprietary <Ptry> | [1..1] | ± | | 358 |

**6.1.16.1.1.1 Code <Cd>**

*Presence: [1..1]*

*Definition: Type of address expressed as a code.*

*Datatype: "AddressType2Code" on page 409*

| CodeName | Name | Definition |
|---|---|---|
| ADDR | Postal | Address is the complete postal address. |
| PBOX | POBox | Address is a postal office (PO) box. |
| HOME | Residential | Address is the home address. |
| BIZZ | Business | Address is the business address. |
| MLTO | MailTo | Address is the address to which mail is sent. |
| DLVY | DeliveryTo | Address is the address to which delivery is to take place. |

**6.1.16.1.1.2 Proprietary <Ptry>**

*Presence: [1..1]*

*Definition: Type of address expressed as a proprietary code.*

**Proprietary <Ptry>** contains the following elements (see "GenericIdentification30" on page 330 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Identification <Id> | [1..1] | Text | | 331 |
| | Issuer <Issr> | [1..1] | Text | | 331 |
| | SchemeName <SchmeNm> | [0..1] | Text | | 331 |

**6.1.16.1.2 CareOf <CareOf>**

*Presence: [0..1]*

*Definition: Identifies an addressee that is accepting the correspondence for the intended recipient. Using care of ensures the correspondence reaches the right recipient rather than getting returned to the sender.*

*Datatype: "Max140Text" on page 429*

**6.1.16.1.3 Department <Dept>**

*Presence: [0..1]*

---

<!-- Page 359 -->

Definition: Identification of a division of a large organisation or building.
DataType: "Max70Text" on page 431

**6.1.16.1.4 SubDepartment <SubDept>**
*Presence:* [0..1]
*Definition:* Identification of a sub-division of a large organisation or building.
*DataType:* "Max70Text" on page 431

**6.1.16.1.5 StreetName <StrtNm>**
*Presence:* [0..1]
*Definition:* Name of a street or thoroughfare.
*DataType:* "Max140Text" on page 429

**6.1.16.1.6 BuildingNumber <BldgNb>**
*Presence:* [0..1]
*Definition:* Number that identifies the position of a building on a street.
*DataType:* "Max16Text" on page 430

**6.1.16.1.7 BuildingName <BldgNm>**
*Presence:* [0..1]
*Definition:* Name of the building or house.
*DataType:* "Max140Text" on page 429

**6.1.16.1.8 Floor <Flr>**
*Presence:* [0..1]
*Definition:* Floor or storey within a building.
*DataType:* "Max70Text" on page 431

**6.1.16.1.9 UnitNumber <UnitNb>**
*Presence:* [0..1]
*Definition:* Identifies a flat or dwelling within the building.
*DataType:* "Max16Text" on page 430

**6.1.16.1.10 PostBox <PstBx>**
*Presence:* [0..1]
*Definition:* Numbered box in a post office, assigned to a person or organisation, where letters are kept until called for.
*DataType:* "Max16Text" on page 430

**6.1.16.1.11 Room <Room>**
*Presence:* [0..1]
*Definition:* Building room number.

---

<!-- Page 360 -->

*Datatype:* "Max70Text" on page 431

**6.1.16.1.12 PostCode <PstCd>**
*Presence:* [0..1]
*Definition:* Identifier consisting of a group of letters and/or numbers that is added to a postal address to assist the sorting of mail.
*Datatype:* "Max16Text" on page 430

**6.1.16.1.13 TownName <TwnNm>**
*Presence:* [0..1]
*Definition:* Name of a built-up area, with defined boundaries, and a local government.
*Datatype:* "Max140Text" on page 429

**6.1.16.1.14 TownLocationName <TwnLctnNm>**
*Presence:* [0..1]
*Definition:* Specific location name within the town.
*Datatype:* "Max140Text" on page 429

**6.1.16.1.15 DistrictName <DstrctNm>**
*Presence:* [0..1]
*Definition:* Identifies a subdivision within a country sub-division.
*Datatype:* "Max140Text" on page 429

**6.1.16.1.16 CountrySubDivision <CtrySubDvsn>**
*Presence:* [0..1]
*Definition:* Identifies a subdivision of a country such as state, region, county.
*Datatype:* "Max35Text" on page 431

**6.1.16.1.17 Country <Ctry>**
*Presence:* [0..1]
*Definition:* Nation with its own government.
*Impacted by:* G7 "Country"
*Datatype:* "CountryCode" on page 412

**Constraints**
*   **Country**
    The code is checked against the list of country names obtained from the United Nations (ISO 3166, Alpha-2 code).

**6.1.16.1.18 AddressLine <AdrLine>**
*Presence:* [0..7]

---

<!-- Page 361 -->

*Definition: Information that locates and identifies a specific address, as defined by postal services, presented in free format text.*
*Datatype: "Max70Text" on page 431*

## 6.1.17 Regulatory Reporting

### 6.1.17.1 RegulatoryReporting3

*Definition: Information needed due to regulatory and/or statutory requirements.*

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | DebitCreditReportingIndicator <DbtCdtRptgInd> | [0..1] | CodeSet | | 361 |
| | Authority <Authrty> | [0..1] | | | 361 |
| | Name <Nm> | [0..1] | Text | | 362 |
| | Country <Ctry> | [0..1] | CodeSet | C7 | 362 |
| | Details <Dtls> | [0..*] | | | 362 |
| | Type <Tp> | [0..1] | Text | | 362 |
| | Date <Dt> | [0..1] | Date | | 363 |
| | Country <Ctry> | [0..1] | CodeSet | C7 | 363 |
| | Code <Cd> | [0..1] | Text | | 363 |
| | Amount <Amt> | [0..1] | Amount | C2, C8 | 363 |
| | Information <Inf> | [0..*] | Text | | 363 |

#### 6.1.17.1.1 DebitCreditReportingIndicator <DbtCdtRptgInd>

*Presence: [0..1]*

*Definition: Identifies whether the regulatory reporting information applies to the debit side, to the credit side or to both debit and credit sides of the transaction.*

*Datatype: "RegulatoryReportingType1Code" on page 422*

| CodeName | Name | Definition |
|:---|:---|:---|
| CRED | Credit | Regulatory information applies to the credit side. |
| DEBT | Debit | Regulatory information applies to the debit side. |
| BOTH | Both | Regulatory information applies to both credit and debit sides. |

#### 6.1.17.1.2 Authority <Authrty>

*Presence: [0..1]*

*Definition: Entity requiring the regulatory reporting information.*

---

<!-- Page 362 -->

Authority <Authority> contains the following **RegulatoryAuthority2** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Name <Nm> | [0..1] | Text | | 362 |
| | Country <Ctry> | [0..1] | CodeSet | C7 | 362 |

**6.1.17.1.2.1 Name <Nm>**

*Presence:* [0..1]

*Definition:* Name of the entity requiring the regulatory reporting information.

*Datatype:* "Max140Text" on page 429

**6.1.17.1.2.2 Country <Ctry>**

*Presence:* [0..1]

*Definition:* Country of the entity that requires the regulatory reporting information.

*Impacted by:* C7 "Country"

*Datatype:* "CountryCode" on page 412

**Constraints**

- **Country**

The code is checked against the list of country names obtained from the United Nations (ISO 3166, Alpha-2 code).

**6.1.17.1.3 Details <Dtls>**

*Presence:* [0..*]

*Definition:* Set of elements used to provide details on the regulatory reporting information.

**Details <Dtls>** contains the following **StructuredRegulatoryReporting3** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Type <Tp> | [0..1] | Text | | 362 |
| | Date <Dt> | [0..1] | Date | | 363 |
| | Country <Ctry> | [0..1] | CodeSet | C7 | 363 |
| | Code <Cd> | [0..1] | Text | | 363 |
| | Amount <Amt> | [0..1] | Amount | C2, C8 | 363 |
| | Information <Inf> | [0..*] | Text | | 363 |

**6.1.17.1.3.1 Type <Tp>**

*Presence:* [0..1]

*Definition:* Specifies the type of the information supplied in the regulatory reporting details.

*Datatype:* "Max35Text" on page 431

---

<!-- Page 363 -->

**6.1.17.1.3.2 Date <Dt>**
*Presence:* [0..1]
*Definition:* Date related to the specified type of regulatory reporting details.
*Datatype:* "ISODate" on page 425

**6.1.17.1.3.3 Country <Ctry>**
*Presence:* [0..1]
*Definition:* Country related to the specified type of regulatory reporting details.
*Impacted by:* C7 "Country"
*Datatype:* "CountryCode" on page 412

**Constraints**
* **Country**
The code is checked against the list of country names obtained from the United Nations (ISO 3166, Alpha-2 code).

**6.1.17.1.3.4 Code <Cd>**
*Presence:* [0..1]
*Definition:* Specifies the nature, purpose, and reason for the transaction to be reported for regulatory and statutory requirements in a coded form.
*Datatype:* "Max10Text" on page 429

**6.1.17.1.3.5 Amount <Amt>**
*Presence:* [0..1]
*Definition:* Amount of money to be reported for regulatory and statutory requirements.
*Impacted by:* C2 "ActiveOrHistoricCurrency", C8 "CurrencyAmount"
*Datatype:* "ActiveOrHistoricCurrencyAndAmount" on page 407

**Constraints**
* **ActiveOrHistoricCurrency**
The Currency Code must be registered, or have already been registered. Valid active or historic currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and may be or not be withdrawn on the day the message containing the Currency is exchanged.
* **CurrencyAmount**
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.

Note: The decimal separator is a dot.

**6.1.17.1.3.6 Information <Inf>**
*Presence:* [0..*]
*Definition:* Additional details that cater for specific domestic regulatory requirements.
*Datatype:* "Max35Text" on page 431

---

<!-- Page 364 -->

# 6.1.18 Remittance

## 6.1.18.1 RemittanceInformation22

*Definition:* Information supplied to enable the matching/reconciliation of an entry with the items that the payment is intended to settle, such as commercial invoices in an accounts' receivable system.

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Unstructured <Ustrd> | [0..] | Text | | 364 |
| | Structured <Strd> | [0..] | ± | | 364 |

### 6.1.18.1.1 Unstructured <Ustrd>

*Presence:* [0..]

*Definition:* Information supplied to enable the matching/reconciliation of an entry with the items that the payment is intended to settle, such as commercial invoices in an accounts' receivable system, in an unstructured form.

*Datatype:* "Max140Text" on page 429

### 6.1.18.1.2 Structured <Strd>

*Presence:* [0..]

*Definition:* Information supplied to enable the matching/reconciliation of an entry with the items that the payment is intended to settle, such as commercial invoices in an accounts' receivable system, in a structured form.

---

<!-- Page 365 -->

Structured <Strd> contains the following elements (see "StructuredRemittanceInformation18" on page 368 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | ReferredDocumentInformation <RltdDocInf> | [0..*] | | | 372 |
| | Type <Tp> | [0..1] | | | 374 |
| | CodeOrProprietary <CdOrPrtry> | [1..1] | | | 374 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 374 |
| Or) | Proprietary <Prtry> | [1..1] | Text | | 374 |
| | Issuer <Issr> | [0..1] | Text | | 374 |
| | Number <Nb> | [0..1] | Text | | 375 |
| | RelatedDate <RltdDt> | [0..1] | | | 375 |
| | Type <Tp> | [1..1] | | | 375 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 375 |
| Or) | Proprietary <Prtry> | [1..1] | Text | | 375 |
| | Date <Dt> | [1..1] | Date | | 375 |
| | LineDetails <LineDtls> | [0..*] | | | 376 |
| | Identification <Id> | [1..1] | | | 376 |
| | Type <Tp> | [0..1] | | | 377 |
| | CodeOrProprietary <CdOrPrtry> | [1..1] | | | 377 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 377 |
| Or) | Proprietary <Prtry> | [1..1] | Text | | 377 |
| | Issuer <Issr> | [0..1] | Text | | 378 |
| | Number <Nb> | [0..1] | Text | | 378 |
| | RelatedDate <RltdDt> | [0..1] | Date | | 378 |
| | Description <Desc> | [0..1] | Text | | 378 |
| | Amount <Amt> | [0..1] | | C24 | 378 |
| | RemittanceAmountAndType <RmtAmtAndTp> | [0..*] | | | 379 |
| | Type <Tp> | [1..1] | | | 379 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 380 |
| Or) | Proprietary <Prtry> | [1..1] | Text | | 380 |
| | Amount <Amt> | [1..1] | Amount | C2, C8 | 380 |
| | AdjustmentAmountAndReason <AdjmtnAmtAndRsn> | [0..*] | | | 380 |
| | Amount <Amt> | [1..1] | Amount | C2, C8 | 380 |

---

<!-- Page 366 -->

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | CreditDebitIndicator <CdtDbtInd> | [0..1] | CodeSet | | 381 |
| | Reason <Rsn> | [0..1] | Text | | 381 |
| | AdditionalInformation <AddtlInf> | [0..1] | Text | | 381 |
| | ReferredDocumentAmount <RtrdDocAmt> | [0..1] | | C24 | 381 |
| | RemittanceAmountAndType <RmtAmtAndTp> | [0..*] | | | 382 |
| | Type <Tp> | [1..1] | | | 382 |
| Or | Code <Cd> | [1..1] | CodeSet | | 383 |
| Or | Proprietary <Prt> | [1..1] | Text | | 383 |
| | Amount <Amt> | [1..1] | Amount | C2, C8 | 383 |
| | AdjustmentAmountAndReason <AdjstmntAmtAndRsn> | [0..*] | | | 383 |
| | Amount <Amt> | [1..1] | Amount | C2, C8 | 383 |
| | CreditDebitIndicator <CdtDbtInd> | [0..1] | CodeSet | | 384 |
| | Reason <Rsn> | [0..1] | Text | | 384 |
| | AdditionalInformation <AddtlInf> | [0..1] | Text | | 384 |
| | CreditorReferenceInformation <CdtrRefInf> | [0..1] | | | 384 |
| | Type <Tp> | [0..1] | | | 385 |
| | CodeOrProprietary <CdOrPrt> | [1..1] | | | 385 |
| Or | Code <Cd> | [1..1] | CodeSet | | 385 |
| Or | Proprietary <Prt> | [1..1] | Text | | 385 |
| | Issuer <Issr> | [0..1] | Text | | 386 |
| | Reference <Ref> | [0..1] | Text | | 386 |
| | Invoker <Invcr> | [0..1] | ± | | 386 |
| | Invoicee <Invcee> | [0..1] | ± | | 387 |
| | TaxRemittance <TaxRmt> | [0..1] | | | 388 |
| | Creditor <Cdtr> | [0..1] | ± | | 390 |
| | Debtor <Dbtr> | [0..1] | ± | | 390 |
| | UltimateDebtor <UltmtDbtr> | [0..1] | ± | | 390 |
| | AdministrationZone <AdminstrZone> | [0..1] | Text | | 391 |
| | ReferenceNumber <RefNb> | [0..1] | Text | | 391 |
| | Method <Mtd> | [0..1] | Text | | 391 |
| | TotalTaxableBaseAmount <TtlTaxblBaseAmt> | [0..1] | Amount | C2, C8 | 391 |

---

<!-- Page 367 -->

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | TotalTaxAmount <TiTaxAmt> | [0..1] | Amount | C2, C8 | 392 |
| | Date <Dt> | [0..1] | Date | | 392 |
| | SequenceNumber <SeqNb> | [0..1] | Quantity | | 392 |
| | Record <Rcrd> | [0..*] | | | 392 |
| | Type <Tp> | [0..1] | Text | | 393 |
| | Category <Ctgy> | [0..1] | Text | | 393 |
| | CategoryDetails <CtgyDtls> | [0..1] | Text | | 393 |
| | DebtorStatus <DbtrSts> | [0..1] | Text | | 394 |
| | CertifiedIdentification <CertId> | [0..1] | Text | | 394 |
| | FormsCode <FrmsCd> | [0..1] | Text | | 394 |
| | Period <Prd> | [0..1] | | | 394 |
| | Year <Yr> | [0..1] | Year | | 394 |
| | Type <Tp> | [0..1] | CodeSet | | 394 |
| | FromToDate <FrToDt> | [0..1] | ± | | 395 |
| | TaxAmount <TaxAmt> | [0..1] | | | 396 |
| | Rate <Rate> | [0..1] | Rate | | 396 |
| | TaxableBaseAmount <TaxblBaseAmt> | [0..1] | Amount | C2, C8 | 396 |
| | TotalAmount <TtlAmt> | [0..1] | Amount | C2, C8 | 396 |
| | Details <Dtls> | [0..*] | | | 397 |
| | Period <Prd> | [0..1] | | | 397 |
| | Year <Yr> | [0..1] | Year | | 397 |
| | Type <Tp> | [0..1] | CodeSet | | 398 |
| | FromToDate <FrToDt> | [0..1] | ± | | 398 |
| | Amount <Amt> | [1..1] | Amount | C2, C8 | 399 |
| | AdditionalInformation <AddtlInf> | [0..1] | Text | | 399 |
| | GarnishmentRemittance <GrnshmtRmt> | [0..1] | | | 399 |
| | Type <Tp> | [1..1] | | | 400 |
| | CodeOrProprietary <CdOrPrtry> | [1..1] | | | 400 |
| Or | Code <Cd> | [1..1] | CodeSet | | 401 |
| Or | Proprietary <Prtry> | [1..1] | Text | | 401 |
| | Issuer <Issr> | [0..1] | Text | | 401 |

---

<!-- Page 368 -->

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Garnishee <Gmrshee> | [0..1] | ± | | 401 |
| | GarnishmentAdministrator <GmrshtAdminstr> | [0..1] | ± | | 402 |
| | ReferenceNumber <RefNbr> | [0..1] | Text | | 403 |
| | Date <Dt> | [0..1] | Date | | 404 |
| | RemittedAmount <RmtdAmt> | [0..1] | Amount | C2, C8 | 404 |
| | FamilyMedicalInsuranceIndicator <FmlyMdclInsmcInd> | [0..1] | Indicator | | 404 |
| | EmployeeTerminationIndicator <MplyeeTermtnInd> | [0..1] | Indicator | | 404 |
| | AdditionalRemittanceInformation <AddtlRmtnInf> | [0..3] | Text | | 404 |

## 6.1.18.2 StructuredRemittanceInformation18

*Definition:* Information supplied to enable the matching/reconciliation of an entry with the items that the payment is intended to settle, such as commercial invoices in an accounts' receivable system, in a structured form.

---

<!-- Page 369 -->

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | ReferredDocumentInformation <RfrdDocInf> | [0..*] |  |  | 372 |
| | Type <Tp> | [0..1] |  |  | 374 |
| | CodeOrProprietary <CdOrPrtry> | [1..1] |  |  | 374 |
| (Or | Code <Cd> | [1..1] | CodeSet |  | 374 |
| Or) | Proprietary <Prtry> | [1..1] | Text |  | 374 |
| | Issuer <Issr> | [0..1] | Text |  | 374 |
| | Number <Nb> | [0..1] | Text |  | 375 |
| | RelatedDate <RltdDt> | [0..1] |  |  | 375 |
| | Type <Tp> | [0..1] |  |  | 375 |
| (Or | Code <Cd> | [1..1] | CodeSet |  | 375 |
| Or) | Proprietary <Prtry> | [1..1] | Text |  | 375 |
| | Date <Dt> | [1..1] | Date |  | 375 |
| | LineDetails <LineDtls> | [0..*] |  |  | 376 |
| | Identification <Id> | [1..*] |  |  | 376 |
| | Type <Tp> | [0..1] |  |  | 377 |
| | CodeOrProprietary <CdOrPrtry> | [1..1] |  |  | 377 |
| (Or | Code <Cd> | [1..1] | CodeSet |  | 377 |
| Or) | Proprietary <Prtry> | [1..1] | Text |  | 377 |
| | Issuer <Issr> | [0..1] | Text |  | 378 |
| | Number <Nb> | [0..1] | Text |  | 378 |
| | RelatedDate <RltdDt> | [0..1] | Date |  | 378 |
| | Description <Desc> | [0..1] | Text |  | 378 |
| | Amount <Amt> | [0..1] |  | C24 | 378 |
| | RemittanceAmountAndType <RmtAmtAndTp> | [0..*] |  |  | 379 |
| | Type <Tp> | [1..1] |  |  | 379 |
| (Or | Code <Cd> | [1..1] | CodeSet |  | 380 |
| Or) | Proprietary <Prtry> | [1..1] | Text |  | 380 |
| | Amount <Amt> | [1..1] | Amount | C2, C8 | 380 |
| | AdjustmentAmountAndReason <AdjstmntAmtAndRsn> | [0..*] |  |  | 380 |
| | Amount <Amt> | [1..1] | Amount | C2, C8 | 380 |
| | CreditDebitIndicator <CdtDbtInd> | [0..1] | CodeSet |  | 381 |

---

<!-- Page 370 -->

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Reason <Rsn> | [0..1] | Text | | 381 |
| | AdditionalInformation <AddtlInf> | [0..1] | Text | | 381 |
| | ReferredDocumentAmount <RfrdDocAmt> | [0..1] | | C24 | 381 |
| | RemittanceAmountAndType <RmtAmtAndTp> | [0..*] | | | 382 |
| | Type <Tp> | [1..1] | | | 382 |
| Or | Code <Cd> | [1..1] | CodeSet | | 383 |
| Or | Proprietary <Prtry> | [1..1] | Text | | 383 |
| | Amount <Amt> | [1..1] | Amount | C2, C8 | 383 |
| | AdjustmentAmountAndReason <AdjstmntAmtAndRsn> | [0..*] | | | 383 |
| | Amount <Amt> | [1..1] | Amount | C2, C8 | 383 |
| | CreditDebitIndicator <CdtDbtInd> | [0..1] | CodeSet | | 384 |
| | Reason <Rsn> | [0..1] | Text | | 384 |
| | AdditionalInformation <AddtlInf> | [0..1] | Text | | 384 |
| | CreditorReferenceInformation <CdrRefInf> | [0..1] | | | 384 |
| | Type <Tp> | [0..1] | | | 385 |
| | CodeOrProprietary <CdOrPrtry> | [1..1] | | | 385 |
| Or | Code <Cd> | [1..1] | CodeSet | | 385 |
| Or | Proprietary <Prtry> | [1..1] | Text | | 385 |
| | Issuer <Issr> | [0..1] | Text | | 386 |
| | Reference <Ref> | [0..1] | Text | | 386 |
| | Invoicer <Invcr> | [0..1] | ± | | 386 |
| | Invoice <Invce> | [0..1] | ± | | 387 |
| | TaxRemittance <TaxRmt> | [0..1] | | | 388 |
| | Creditor <Cdr> | [0..1] | ± | | 390 |
| | Debtor <Dbtr> | [0..1] | ± | | 390 |
| | UltimateDebtor <UltmtDbtr> | [0..1] | ± | | 390 |
| | AdministrationZone <AdminZone> | [0..1] | Text | | 391 |
| | ReferenceNumber <RefNb> | [0..1] | Text | | 391 |
| | Method <Mtd> | [0..1] | Text | | 391 |
| | TotalTaxableBaseAmount <TtlTaxblBaseAmt> | [0..1] | Amount | C2, C8 | 391 |
| | TotalTaxAmount <TtlTaxAmt> | [0..1] | Amount | C2, C8 | 392 |

---

<!-- Page 371 -->

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Date <Dt> | [0..1] | Date | | 392 |
| | SequenceNumber <SeqNb> | [0..1] | Quantity | | 392 |
| | Record <Rcrd> | [0..*] | | | 392 |
| | Type <Tp> | [0..1] | Text | | 393 |
| | Category <Ctgy> | [0..1] | Text | | 393 |
| | CategoryDetails <CtgyDtls> | [0..1] | Text | | 393 |
| | DebtorStatus <DbtrSts> | [0..1] | Text | | 394 |
| | CertificateIdentification <CertId> | [0..1] | Text | | 394 |
| | FormsCode <FrmsCd> | [0..1] | Text | | 394 |
| | Period <Prd> | [0..1] | | | 394 |
| | Year <Yr> | [0..1] | Year | | 394 |
| | Type <Tp> | [0..1] | CodeSet | | 394 |
| | FromToDate <FrToDt> | [0..1] | ± | | 395 |
| | TaxAmount <TaxAmt> | [0..1] | | | 396 |
| | Rate <Rate> | [0..1] | Rate | | 396 |
| | TaxableBaseAmount <TaxblBaseAmt> | [0..1] | Amount | C2, C8 | 396 |
| | TotalAmount <TtlAmt> | [0..1] | Amount | C2, C8 | 396 |
| | Details <Dtls> | [0..*] | | | 397 |
| | Period <Prd> | [0..1] | | | 397 |
| | Year <Yr> | [0..1] | Year | | 397 |
| | Type <Tp> | [0..1] | CodeSet | | 398 |
| | FromToDate <FrToDt> | [0..1] | ± | | 398 |
| | Amount <Amt> | [1..1] | Amount | C2, C8 | 399 |
| | AdditionalInformation <AddtlInf> | [0..1] | Text | | 399 |
| | GarnishmentRemittance <GrnshmtRmtd> | [0..1] | | | 399 |
| | Type <Tp> | [1..1] | | | 400 |
| | CodeOrProprietary <CdOrPrtry> | [1..1] | | | 400 |
| Or | Code <Cd> | [1..1] | CodeSet | | 401 |
| Or | Proprietary <Prtry> | [1..1] | Text | | 401 |
| | Issuer <Issr> | [0..1] | Text | | 401 |
| | Garnishee <Grnshee> | [0..1] | ± | | 401 |

---

<!-- Page 372 -->

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | GarnishmentAdministrator <i><GrnshmtAdmstr></i> | [0..1] | ± | | 402 |
| | ReferenceNumber <i><RefNb></i> | [0..1] | Text | | 403 |
| | Date <i><Dt></i> | [0..1] | Date | | 404 |
| | RemittedAmount <i><RmtdAmt></i> | [0..1] | Amount | C2, C8 | 404 |
| | FamilyMedicalInsuranceIndicator <i><FmlyMdclInsmcInd></i> | [0..1] | Indicator | | 404 |
| | EmployeeTerminationIndicator <i><MplyeTermtnInd></i> | [0..1] | Indicator | | 404 |
| | AdditionalRemittanceInformation <i><AddtlRmtInf></i> | [0..3] | Text | | 404 |

## 6.1.18.2.1 ReferredDocumentInformation <RfrdDocInf>

*Presence: [0..*]*

*Definition: Provides the identification and the content of the referred document.*

---

<!-- Page 373 -->

ReferredDocumentInformation `<RfrdDocIn>` contains the following
ReferredDocumentInformation8 elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Type `<Tp>` | [0..1] | | | 374 |
| | CodeOrProprietary `<CdOrPtry>` | [1..1] | | | 374 |
| (Or | Code `<Cd>` | [1..1] | CodeSet | | 374 |
| Or) | Proprietary `<Ptry>` | [1..1] | Text | | 374 |
| | Issuer `<Issr>` | [0..1] | Text | | 374 |
| | Number `<Nb>` | [0..1] | Text | | 375 |
| | RelatedDate `<RltdDt>` | [0..1] | | | 375 |
| | Type `<Tp>` | [1..1] | | | 375 |
| (Or | Code `<Cd>` | [1..1] | CodeSet | | 375 |
| Or) | Proprietary `<Ptry>` | [1..1] | Text | | 375 |
| | Date `<Dt>` | [1..1] | Date | | 375 |
| | LineDetails `<LineDtls>` | [0..*] | | | 376 |
| | Identification `<Id>` | [1..1] | | | 376 |
| | Type `<Tp>` | [1..1] | | | 377 |
| | CodeOrProprietary `<CdOrPtry>` | [1..1] | | | 377 |
| (Or | Code `<Cd>` | [1..1] | CodeSet | | 377 |
| Or) | Proprietary `<Ptry>` | [1..1] | Text | | 377 |
| | Issuer `<Issr>` | [0..1] | Text | | 378 |
| | Number `<Nb>` | [0..1] | Text | | 378 |
| | RelatedDate `<RltdDt>` | [0..1] | Date | | 378 |
| | Description `<Desc>` | [0..1] | Text | | 378 |
| | Amount `<Amt>` | [0..1] | | C24 | 378 |
| | RemittanceAmountAndType `<RmtAmtAndTp>` | [0..*] | | | 379 |
| | Type `<Tp>` | [1..1] | | | 379 |
| (Or | Code `<Cd>` | [1..1] | CodeSet | | 380 |
| Or) | Proprietary `<Ptry>` | [1..1] | Text | | 380 |
| | Amount `<Amt>` | [1..1] | Amount | C2, C8 | 380 |
| | AdjustmentAmountAndReason `<AdjstmntAmtAndRsn>` | [0..*] | | | 380 |
| | Amount `<Amt>` | [1..1] | Amount | C2, C8 | 380 |
| | CreditDebitIndicator `<CdtDbtInd>` | [0..1] | CodeSet | | 381 |

---

<!-- Page 374 -->

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Reason <Rsn> | [0..1] | Text | | 381 |
| | AdditionalInformation <AddtlInf> | [0..1] | Text | | 381 |

**6.1.18.2.1.1 Type <Tp>**

*Presence:* [0..1]

*Definition:* Specifies the type of referred document.

**Type <Tp>** contains the following **DocumentType1** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | CodeOrProprietary <CdOrPrtry> | [1..1] |  | | 374 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 374 |
| Or) | Proprietary <Prtry> | [1..1] | Text | | 374 |
| | Issuer <Issr> | [0..1] | Text | | 374 |

**6.1.18.2.1.1.1 CodeOrProprietary <CdOrPrtry>**

*Presence:* [1..1]

*Definition:* Coded or proprietary format referred document type.

**CodeOrProprietary <CdOrPrtry>** contains one of the following **DocumentType2Choice** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| (Or | Code <Cd> | [1..1] | CodeSet | | 374 |
| Or) | Proprietary <Prtry> | [1..1] | Text | | 374 |

**6.1.18.2.1.1.1.1 Code <Cd>**

*Presence:* [1..1]

*Definition:* Type of remittance document, as published in an external document type code set.

*Datatype:* "ExternalDocumentType1Code" on page 416

**6.1.18.2.1.1.1.2 Proprietary <Prtry>**

*Presence:* [1..1]

*Definition:* Type of remittance document, in a proprietary form.

*Datatype:* "Max35Text" on page 431

**6.1.18.2.1.1.2 Issuer <Issr>**

*Presence:* [0..1]

*Definition:* Identification of the issuer of the reference document type.

*Datatype:* "Max35Text" on page 431

---

<!-- Page 375 -->

**6.1.18.2.1.2 Number <Nb>**
*Presence:* [0..1]
*Definition:* Unique and unambiguous identification of the referred document.
*Datatype:* "Max35Text" on page 431

**6.1.18.2.1.3 RelatedDate <RltdDt>**
*Presence:* [0..1]
*Definition:* Date and date type associated with the referred document.
**RelatedDate <RltdDt>** contains the following DateAndType1 elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Type <Tp> | [1..1] | | | 375 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 375 |
| Or) | Proprietary <Ptry> | [1..1] | Text | | 375 |
| | Date <Dt> | [1..1] | Date | | 375 |

**6.1.18.2.1.3.1 Type <Tp>**
*Presence:* [1..1]
*Definition:* Type of date associated with the referred document.
**Type <Tp>** contains one of the following DateType2Choice elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| (Or | Code <Cd> | [1..1] | CodeSet | | 375 |
| Or) | Proprietary <Ptry> | [1..1] | Text | | 375 |

**6.1.18.2.1.3.1.1 Code <Cd>**
*Presence:* [1..1]
*Definition:* Specifies the date type, as published in an external date type code set.
*Datatype:* "ExternalDateType1Code" on page 415

**6.1.18.2.1.3.1.2 Proprietary <Ptry>**
*Presence:* [1..1]
*Definition:* Specifies the date type, in a free-text form.
*Datatype:* "Max35Text" on page 431

**6.1.18.2.1.3.2 Date <Dt>**
*Presence:* [1..1]
*Definition:* Date associated with the referred document.
*Datatype:* "ISODate" on page 425

---

<!-- Page 376 -->

6.1.18.2.1.4 LineDetails <LineDtls>

*Presence: [0..*]*

*Definition: Set of elements used to provide the content of the referred document line.*

LineDetails <LineDtls> contains the following DocumentLineInformation2 elements



| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | Identification <Id> | [1..*] | | | 376 |
| | Type <Tp> | [0..1] | | | 377 |
| | CodeOrProprietary <CdOrPtry> | [1..1] | | | 377 |
| Or | Code <Cd> | [1..1] | CodeSet | | 377 |
| Or | Proprietary <Ptry> | [1..1] | Text | | 377 |
| | Issuer <Issr> | [0..1] | Text | | 378 |
| | Number <Nb> | [0..1] | Text | | 378 |
| | RelatedDate <RltdDt> | [0..1] | Date | | 378 |
| | Description <Desc> | [0..1] | Text | | 378 |
| | Amount <Amt> | [0..1] | | C24 | 378 |
| | RemittanceAmountAndType <RmtAmtAndTp> | [0..*] | | | 379 |
| | Type <Tp> | [1..1] | | | 379 |
| Or | Code <Cd> | [1..1] | CodeSet | | 380 |
| Or | Proprietary <Ptry> | [1..1] | Text | | 380 |
| | Amount <Amt> | [1..1] | Amount | C2, C8 | 380 |
| | AdjustmentAmountAndReason <AdjstmtAmtAndRsn> | [0..*] | | | 380 |
| | Amount <Amt> | [1..1] | Amount | C2, C8 | 380 |
| | CreditDebitIndicator <CdtDbtInd> | [0..1] | CodeSet | | 381 |
| | Reason <Rsn> | [0..1] | Text | | 381 |
| | AdditionalInformation <AddtlInf> | [0..1] | Text | | 381 |

6.1.18.2.1.4.1 Identification <Id>

*Presence: [1..*]*

*Definition: Provides identification of the document line.*

---

<!-- Page 377 -->

Identification <Id> contains the following DocumentLineIdentification1 elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Type <Tp> | [0..1] |  |  | 377 |
| | CodeOrProprietary <CdOrPtry> | [1..1] |  |  | 377 |
| (Or | Code <Cd> | [1..1] | CodeSet |  | 377 |
| Or) | Proprietary <Ptry> | [1..1] | Text |  | 377 |
| | Issuer <Issr> | [0..1] | Text |  | 378 |
| | Number <Nb> | [0..1] | Text |  | 378 |
| | RelatedDate <RltdDt> | [0..1] | Date |  | 378 |

**6.1.18.2.1.4.1.1 Type <Tp>**

*Presence:* [0..1]

*Definition:* Specifies the type of referred document line identification.

**Type <Tp>** contains the following **DocumentLineType1** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | CodeOrProprietary <CdOrPtry> | [1..1] |  |  | 377 |
| (Or | Code <Cd> | [1..1] | CodeSet |  | 377 |
| Or) | Proprietary <Ptry> | [1..1] | Text |  | 377 |
| | Issuer <Issr> | [0..1] | Text |  | 378 |

**6.1.18.2.1.4.1.1.1 CodeOrProprietary <CdOrPtry>**

*Presence:* [1..1]

*Definition:* Provides the type details of the referred document line identification.

**CodeOrProprietary <CdOrPtry>** contains one of the following **DocumentLineType1Choice** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| (Or | Code <Cd> | [1..1] | CodeSet |  | 377 |
| Or) | Proprietary <Ptry> | [1..1] | Text |  | 377 |

**6.1.18.2.1.4.1.1.1.1 Code <Cd>**

*Presence:* [1..1]

*Definition:* Line identification type in a coded form.

*DataType:* "ExternalDocumentLineType1Code" on page 416

**6.1.18.2.1.4.1.1.1.2 Proprietary <Ptry>**

*Presence:* [1..1]

---

<!-- Page 378 -->

Definition: Proprietary identification of the type of the remittance document.
Datatype: "Max35Text" on page 431

**6.1.18.2.1.4.1.2 Issuer <Issr>**
*Presence:* [0..1]
*Definition:* Identification of the issuer of the reference document line identificationtype.
*Datatype:* "Max35Text" on page 431

**6.1.18.2.1.4.1.2 Number <Nb>**
*Presence:* [0..1]
*Definition:* Identification of the type specified for the referred document line.
*Datatype:* "Max35Text" on page 431

**6.1.18.2.1.4.1.3 RelatedDate <RltdDt>**
*Presence:* [0..1]
*Definition:* Date associated with the referred document line.
*Datatype:* "ISODate" on page 425

**6.1.18.2.1.4.2 Description <Desc>**
*Presence:* [0..1]
*Definition:* Description associated with the document line.
*Datatype:* "Max2048Text" on page 430

**6.1.18.2.1.4.3 Amount <Amt>**
*Presence:* [0..1]
*Definition:* Provides details on the amounts of the document line.
*Impacted by:* C24 "RemittanceAmountAndTypeGuideline"

---

<!-- Page 379 -->

Amount `<Amt>` contains the following RemittanceAmount4 elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | RemittanceAmountAndType `<RmtAmtAndTp>` | [0..*] |  |  | 379 |
| | Type `<Tp>` | [1..1] |  |  | 379 |
| (Or | Code `<Cd>` | [1..1] | CodeSet |  | 380 |
| Or) | Proprietary `<Prtry>` | [1..1] | Text |  | 380 |
| | Amount `<Amt>` | [1..1] | Amount | C2, C8 | 380 |
| | AdjustmentAmountAndReason `<AdjstmntAmtAndRsn>` | [0..*] |  |  | 380 |
| | Amount `<Amt>` | [1..1] | Amount | C2, C8 | 380 |
| | CreditDebitIndicator `<CdtDbtInd>` | [0..1] | CodeSet |  | 381 |
| | Reason `<Rsn>` | [0..1] | Text |  | 381 |
| | AdditionalInformation `<AddtlInf>` | [0..1] | Text |  | 381 |

## Constraints

- **RemittanceAmountAndTypeGuideline**

  If Type/Code is equal to CREN, DUPA or REMI for RemittanceAmountAndType, RemittanceAmountAndType must not be repeated.

### 6.1.18.2.1.4.3.1 RemittanceAmountAndType `<RmtAmtAndTp>`

*Presence: [0..*]*

*Definition: Type and amount of money for the referred document.*

RemittanceAmountAndType `<RmtAmtAndTp>` contains the following DocumentAmount1 elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Type `<Tp>` | [1..1] |  |  | 379 |
| (Or | Code `<Cd>` | [1..1] | CodeSet |  | 380 |
| Or) | Proprietary `<Prtry>` | [1..1] | Text |  | 380 |
| | Amount `<Amt>` | [1..1] | Amount | C2, C8 | 380 |

### 6.1.18.2.1.4.3.1.1 Type `<Tp>`

*Presence: [1..1]*

*Definition: Defines the type of amount.*

Type `<Tp>` contains one of the following DocumentAmountType1Choice elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| (Or | Code `<Cd>` | [1..1] | CodeSet |  | 380 |
| Or) | Proprietary `<Prtry>` | [1..1] | Text |  | 380 |

---

<!-- Page 380 -->

6.1.18.2.1.4.3.1.1.1 Code <Cd>
Presence: [1..1]
Definition: Specifies the amount type, as published in an external referred amount code set.
Datatype: "ExternalDocumentAmountTypeCode" on page 415

6.1.18.2.1.4.3.1.1.2 Proprietary <Ppry>
Presence: [1..1]
Definition: Specifies the amount type, in a free-text form.
Datatype: "Max35Text" on page 431

6.1.18.2.1.4.3.1.2 Amount <Amt>
Presence: [1..1]
Definition: Amount of money for the referred document.
Impacted by: C2 "ActiveOrHistoricCurrency", C8 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 407

Constraints
* ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and may be or not be withdrawn on the day the message containing the Currency is exchanged.
* CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.

6.1.18.2.1.4.3.2 AdjustmentAmountAndReason <AdjstmntAmtAndRsn>
Presence: [0..*]
Definition: Specifies detailed information on the amount and reason of the adjustment.
AdjustmentAmountAndReason <AdjstmntAmtAndRsn> contains the following DocumentAdjustment1 elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | Amount <Amt> | [1..1] | Amount | C2, C8 | 380 |
| | CreditDebitIndicator <CdtDbtInd> | [0..1] | CodeSet | | 381 |
| | Reason <Rsn> | [0..1] | Text | | 381 |
| | AdditionalInformation <AddtlInf> | [0..1] | Text | | 381 |

6.1.18.2.1.4.3.2.1 Amount <Amt>
Presence: [1..1]
Definition: Amount of money of the document adjustment.

---

<!-- Page 381 -->

*Impacted by: C2 "ActiveOrHistoricCurrency", C8 "CurrencyAmount"*
*DataType: "ActiveOrHistoricCurrencyAndAmount" on page 407*

**Constraints**

- **ActiveOrHistoricCurrency**

The Currency Code must be registered, or have already been registered. Valid active or historic currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and may be or not be withdrawn on the day the message containing the Currency is exchanged.

- **CurrencyAmount**

The number of fractional digits (or minor unit of currency) must comply with ISO 4217.

Note: The decimal separator is a dot.

**6.1.18.2.1.4.3.2.2 CreditDebitIndicator <CdtDbtInd>**

*Presence: [0..1]*

*Definition: Specifies whether the adjustment must be subtracted or added to the total amount.*

*DataType: "CreditDebitCode" on page 412*



| CodeName | Name | Definition |
| :--- | :--- | :--- |
| CRDT | Credit | Operation is an increase. |
| DBIT | Debit | Operation is a decrease. |

**6.1.18.2.1.4.3.2.3 Reason <Rsn>**

*Presence: [0..1]*

*Definition: Specifies the reason for the adjustment.*

*DataType: "Max4Text" on page 431*

**6.1.18.2.1.4.3.2.4 AdditionalInformation <AddtlInf>**

*Presence: [0..1]*

*Definition: Provides further details on the document adjustment.*

*DataType: "Max140Text" on page 429*

**6.1.18.2.2 ReferredDocumentAmount <RfrdDocAmt>**

*Presence: [0..1]*

*Definition: Provides details on the amounts of the referred document.*

*Impacted by: C24 "RemittanceAmountAndTypeGuideline"*

---

<!-- Page 382 -->

ReferredDocumentAmount <RfrdDocAmt> contains the following RemittanceAmount4 elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | RemittanceAmountAndType <RmtAmtAndTp> | [0..*] | | | 382 |
| | Type <Tp> | [1..1] | | | 382 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 383 |
| Or) | Proprietary <Ptry> | [1..1] | Text | | 383 |
| | Amount <Amt> | [1..1] | Amount | C2, C8 | 383 |
| | AdjustmentAmountAndReason <AdjstmntAmtAndRsn> | [0..*] | | | 383 |
| | Amount <Amt> | [1..1] | Amount | C2, C8 | 383 |
| | CreditDebitIndicator <CdtDbtInd> | [0..1] | CodeSet | | 384 |
| | Reason <Rsn> | [0..1] | Text | | 384 |
| | AdditionalInformation <AddtlInf> | [0..1] | Text | | 384 |

**Constraints**

- **RemittanceAmountAndTypeGuideline**

  If Type/Code is equal to CREN, DUPA or REMI for RemittanceAmountAndType, RemittanceAmountAndType must not be repeated.

**6.1.18.2.2.1 RemittanceAmountAndType <RmtAmtAndTp>**

*Presence: [0..*]*

*Definition: Type and amount of money for the referred document.*

**RemittanceAmountAndType <RmtAmtAndTp>** contains the following **DocumentAmount1** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Type <Tp> | [1..1] | | | 382 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 383 |
| Or) | Proprietary <Ptry> | [1..1] | Text | | 383 |
| | Amount <Amt> | [1..1] | Amount | C2, C8 | 383 |

**6.1.18.2.2.1.1 Type <Tp>**

*Presence: [1..1]*

*Definition: Defines the type of amount.*

**Type <Tp>** contains one of the following **DocumentAmountType1Choice** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| (Or | Code <Cd> | [1..1] | CodeSet | | 383 |
| Or) | Proprietary <Ptry> | [1..1] | Text | | 383 |

---

<!-- Page 383 -->

**6.1.18.2.2.1.1.1 Code <Cd>**
*Presence:* [1..1]
*Definition:* Specifies the amount type, as published in an external referred amount code set.
*Datatype:* "ExternalDocumentAmountType1Code" on page 415

**6.1.18.2.2.1.1.2 Proprietary <Ptry>**
*Presence:* [1..1]
*Definition:* Specifies the amount type, in a free-text form.
*Datatype:* "Max35Text" on page 431

**6.1.18.2.2.1.2 Amount <Amt>**
*Presence:* [1..1]
*Definition:* Amount of money for the referred document.
*Impacted by:* C2 "ActiveOrHistoricCurrency", C8 "CurrencyAmount"
*Datatype:* "ActiveOrHistoricCurrencyAndAmount" on page 407

**Constraints**

*   **ActiveOrHistoricCurrency**

    The Currency Code must be registered, or have already been registered. Valid active or historic currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and may be or not be withdrawn on the day the message containing the Currency is exchanged.

*   **CurrencyAmount**

    The number of fractional digits (or minor unit of currency) must comply with ISO 4217.

    Note: The decimal separator is a dot.

**6.1.18.2.2.2 AdjustmentAmountAndReason <AdjstmntAmtAndRsn>**
*Presence:* [0..*]
*Definition:* Specifies detailed information on the amount and reason of the adjustment.

**AdjustmentAmountAndReason <AdjstmntAmtAndRsn>** contains the following **DocumentAdjustment1** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
| :--- | :--- | :--- | :--- | :--- | :--- |
| | Amount <Amt> | [1..1] | Amount | C2, C8 | 383 |
| | CreditDebitIndicator <CdtDbtInd> | [0..1] | CodeSet | | 384 |
| | Reason <Rsn> | [0..1] | Text | | 384 |
| | AdditionalInformation <AddtlInf> | [0..1] | Text | | 384 |

**6.1.18.2.2.2.1 Amount <Amt>**
*Presence:* [1..1]
*Definition:* Amount of money of the document adjustment.

---

<!-- Page 384 -->

*Impacted by: C2 "ActiveOrHistoricCurrency", C8 "CurrencyAmount"*
*Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 407*

## Constraints

- **ActiveOrHistoricCurrency**

The Currency Code must be registered, or have already been registered. Valid active or historic currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and may be or not be withdrawn on the day the message containing the Currency is exchanged.

- **CurrencyAmount**

The number of fractional digits (or minor unit of currency) must comply with ISO 4217.

Note: The decimal separator is a dot.

### 6.1.18.2.2.2.2 CreditDebitIndicator <CdtDbtInd>

*Presence:* [0..1]

*Definition:* Specifies whether the adjustment must be subtracted or added to the total amount.

*Datatype:* "CreditDebitCode" on page 412



| CodeName | Name | Definition |
|---|---|---|
| CRDT | Credit | Operation is an increase. |
| DBIT | Debit | Operation is a decrease. |

### 6.1.18.2.2.2.3 Reason <Rsn>

*Presence:* [0..1]

*Definition:* Specifies the reason for the adjustment.

*Datatype:* "Max4Text" on page 431

### 6.1.18.2.2.2.4 AdditionalInformation <AddtlInf>

*Presence:* [0..1]

*Definition:* Provides further details on the document adjustment.

*Datatype:* "Max140Text" on page 429

### 6.1.18.2.3 CreditorReferenceInformation <CdtrRefInf>

*Presence:* [0..1]

*Definition:* Reference information provided by the creditor to allow the identification of the underlying documents.

---

<!-- Page 385 -->

CreditorReferenceInformation <CdRefInf> contains the following CreditorReferenceInformation3 elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Type <Tp> | [0..1] |  |  | 385 |
| | CodeOrProprietary <CdOrPrtry> | [1..1] |  |  | 385 |
| (Or | Code <Cd> | [1..1] | CodeSet |  | 385 |
| Or) | Proprietary <Prtry> | [1..1] | Text |  | 385 |
| | Issuer <Issr> | [0..1] | Text |  | 386 |
| | Reference <Ref> | [0..1] | Text |  | 386 |

**6.1.18.2.3.1 Type <Tp>**

*Presence:* [0..1]

*Definition:* Specifies the type of creditor reference.

**Type <Tp>** contains the following **CreditorReferenceType3** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | CodeOrProprietary <CdOrPrtry> | [1..1] |  |  | 385 |
| (Or | Code <Cd> | [1..1] | CodeSet |  | 385 |
| Or) | Proprietary <Prtry> | [1..1] | Text |  | 385 |
| | Issuer <Issr> | [0..1] | Text |  | 386 |

**6.1.18.2.3.1.1 CodeOrProprietary <CdOrPrtry>**

*Presence:* [1..1]

*Definition:* Coded or proprietary format creditor reference type.

**CodeOrProprietary <CdOrPrtry>** contains one of the following **CreditorReferenceType2Choice** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| (Or | Code <Cd> | [1..1] | CodeSet |  | 385 |
| Or) | Proprietary <Prtry> | [1..1] | Text |  | 385 |

**6.1.18.2.3.1.1.1 Code <Cd>**

*Presence:* [1..1]

*Definition:* Type of creditor reference, as published in an external creditor reference type code set.

*Datatype:* "ExternalCreditorReferenceType1Code" on page 415

**6.1.18.2.3.1.1.2 Proprietary <Prtry>**

*Presence:* [1..1]

---

<!-- Page 386 -->

*Definition:* Type of creditor reference, in a proprietary form.

*Datatype:* "Max35Text" on page 431

**6.1.18.2.3.1.2 Issuer <Issr>**

*Presence:* [0..1]

*Definition:* Entity that assigns the credit reference type.

*Datatype:* "Max35Text" on page 431

**6.1.18.2.3.2 Reference <Ref>**

*Presence:* [0..1]

*Definition:* Unique reference, as assigned by the creditor, to unambiguously refer to the payment transaction.

Usage: If available, the initiating party should provide this reference in the structured remittance information, to enable reconciliation by the creditor upon receipt of the amount of money.

If the business context requires the use of a creditor reference or a payment remit identification, and only one identifier can be passed through the end-to-end chain, the creditor's reference or payment remittance identification should be quoted in the end-to-end transaction identification.

*Datatype:* "Max35Text" on page 431

**6.1.18.2.4 Invoicer <Invcr>**

*Presence:* [0..1]

*Definition:* Identification of the organisation issuing the invoice, when it is different from the creditor or ultimate creditor.

---

<!-- Page 387 -->

Invoice `<Inv>` contains the following elements (see "PartyIdentification27" on page 336 for details)



<table>
  <thead>
    <tr>
      <th>Or</th>
      <th>MessageElement&lt;XML Tag&gt;</th>
      <th>Mult.</th>
      <th>Type</th>
      <th>Constr. No.</th>
      <th>Page</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td></td>
      <td>Name &lt;Nm&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>337</td>
    </tr>
    <tr>
      <td></td>
      <td>PostalAddress &lt;PstlAdr&gt;</td>
      <td>[0..1]</td>
      <td>±</td>
      <td></td>
      <td>338</td>
    </tr>
    <tr>
      <td></td>
      <td>Identification &lt;Id&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>338</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>OrganisationIdentification &lt;OrgId&gt;</td>
      <td>[1..1]</td>
      <td></td>
      <td></td>
      <td>339</td>
    </tr>
    <tr>
      <td></td>
      <td>AnyBIC &lt;AnyBIC&gt;</td>
      <td>[0..1]</td>
      <td>IdentifierSet</td>
      <td>C5</td>
      <td>340</td>
    </tr>
    <tr>
      <td></td>
      <td>LEI &lt;LEI&gt;</td>
      <td>[0..1]</td>
      <td>IdentifierSet</td>
      <td></td>
      <td>340</td>
    </tr>
    <tr>
      <td></td>
      <td>Other &lt;Othr&gt;</td>
      <td>[0..*]</td>
      <td></td>
      <td></td>
      <td>340</td>
    </tr>
    <tr>
      <td></td>
      <td>Identification &lt;Id&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td></td>
      <td>SchemaName &lt;SchmeNm&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Code &lt;Cd&gt;</td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Proprietary &lt;Ptry&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td></td>
      <td>Issuer &lt;Issr&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>PrivateIdentification &lt;PrvtId&gt;</td>
      <td>[1..1]</td>
      <td></td>
      <td></td>
      <td>341</td>
    </tr>
    <tr>
      <td></td>
      <td>DateAndPlaceOfBirth &lt;DtAndPlcOfBirth&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>342</td>
    </tr>
    <tr>
      <td></td>
      <td>BirthDate &lt;BirthDt&gt;</td>
      <td>[1..1]</td>
      <td>Date</td>
      <td></td>
      <td>342</td>
    </tr>
    <tr>
      <td></td>
      <td>ProvinceOfBirth &lt;PvcOfBirth&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>342</td>
    </tr>
    <tr>
      <td></td>
      <td>CityOfBirth &lt;CityOfBirth&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>CountryOfBirth &lt;CtryOfBirth&gt;</td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td>C7</td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>Other &lt;Othr&gt;</td>
      <td>[0..*]</td>
      <td></td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>Identification &lt;Id&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td></td>
      <td>SchemaName &lt;SchmeNm&gt;</td>
      <td>[0..1]</td>
      <td></td>
      <td></td>
      <td>343</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Code &lt;Cd&gt;</td>
      <td>[1..1]</td>
      <td>CodeSet</td>
      <td></td>
      <td>344</td>
    </tr>
    <tr>
      <td>Or</td>
      <td>Proprietary &lt;Ptry&gt;</td>
      <td>[1..1]</td>
      <td>Text</td>
      <td></td>
      <td>344</td>
    </tr>
    <tr>
      <td></td>
      <td>Issuer &lt;Issr&gt;</td>
      <td>[0..1]</td>
      <td>Text</td>
      <td></td>
      <td>344</td>
    </tr>
    <tr>
      <td></td>
      <td>CountryOfResidence &lt;CtryOfRes&gt;</td>
      <td>[0..1]</td>
      <td>CodeSet</td>
      <td>C7</td>
      <td>344</td>
    </tr>
    <tr>
      <td></td>
      <td>ContactDetails &lt;CtctDtls&gt;</td>
      <td>[0..1]</td>
      <td>±</td>
      <td></td>
      <td>344</td>
    </tr>
  </tbody>
</table>

## 6.1.18.2.5 Invoicee `<Invcee>`

*Presence: [0..1]*

*Definition: Identification of the party to whom an invoice is issued, when it is different from the debtor or ultimate debtor.*

---

<!-- Page 388 -->

Invoice `<Invoice>` contains the following elements (see "PartyIdentification272" on page 336 for details)



| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Name `<Nm>` | [0..1] | Text | | 337 |
| | PostalAddress `<PstlAdr>` | [0..1] | ± | | 338 |
| | Identification `<Id>` | [0..1] | | | 338 |
| (Or | OrganisationIdentification `<OrgId>` | [1..1] | | | 339 |
| | AnyBIC `<AnyBIC>` | [0..1] | IdentifierSet | C5 | 340 |
| | LEI `<LEI>` | [0..1] | IdentifierSet | | 340 |
| | Other `<Othr>` | [0..*] | | | 340 |
| | Identification `<Id>` | [1..1] | Text | | 341 |
| | SchemeName `<SchmeNm>` | [0..1] | | | 341 |
| (Or | Code `<Cd>` | [1..1] | CodeSet | | 341 |
| Or) | Proprietary `<Prtry>` | [1..1] | Text | | 341 |
| | Issuer `<Issr>` | [0..1] | Text | | 341 |
| (Or) | PrivateIdentification `<PrvtId>` | [1..1] | | | 341 |
| | DateAndPlaceOfBirth `<DtAndPlcOfBirth>` | [0..1] | | | 342 |
| | BirthDate `<BirthDt>` | [1..1] | Date | | 342 |
| | ProvinceOfBirth `<PrvcOfBirth>` | [0..1] | Text | | 342 |
| | CityOfBirth `<CityOfBirth>` | [1..1] | Text | | 343 |
| | CountryOfBirth `<CtryOfBirth>` | [1..1] | CodeSet | C7 | 343 |
| | Other `<Othr>` | [0..*] | | | 343 |
| | Identification `<Id>` | [1..1] | Text | | 343 |
| | SchemeName `<SchmeNm>` | [0..1] | | | 343 |
| (Or | Code `<Cd>` | [1..1] | CodeSet | | 344 |
| Or) | Proprietary `<Prtry>` | [1..1] | Text | | 344 |
| | Issuer `<Issr>` | [0..1] | Text | | 344 |
| | CountryOfResidence `<CtryOfRes>` | [0..1] | CodeSet | C7 | 344 |
| | ContactDetails `<CtctDtls>` | [0..1] | ± | | 344 |

## 6.1.18.2.6 TaxRemittance `<TaxRmt>`

*Presence:* [0..1]

*Definition:* Provides remittance information about a payment made for tax-related purposes.

---

<!-- Page 389 -->

TaxRemittance <TaxRmt> contains the following TaxData1 elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Creditor <Cdtor> | [0..1] | ± | | 390 |
| | Debtor <Dbtr> | [0..1] | ± | | 390 |
| | UltimateDebtor <UltmtDbtr> | [0..1] | ± | | 390 |
| | AdministrationZone <AdminZone> | [0..1] | Text | | 391 |
| | ReferenceNumber <RefNb> | [0..1] | Text | | 391 |
| | Method <Mtd> | [0..1] | Text | | 391 |
| | TotalTaxableBaseAmount <TtlTaxblBaseAmt> | [0..1] | Amount | C2, C8 | 391 |
| | TotalTaxAmount <TtlTaxAmt> | [0..1] | Amount | C2, C8 | 392 |
| | Date <Dt> | [0..1] | Date | | 392 |
| | SequenceNumber <SeqNb> | [0..1] | Quantity | | 392 |
| | Record <Rcrd> | [0.*] | | | 392 |
| | Type <Tp> | [0..1] | Text | | 393 |
| | Category <Ctgy> | [0..1] | Text | | 393 |
| | CategoryDetails <CtgyDtls> | [0..1] | Text | | 393 |
| | DebtorStatus <DbtrSts> | [0..1] | Text | | 394 |
| | CertificateIdentification <CertId> | [0..1] | Text | | 394 |
| | FormsCode <FrmsCd> | [0..1] | Text | | 394 |
| | Period <Prd> | [0..1] | | | 394 |
| | Year <Yr> | [0..1] | Year | | 394 |
| | Type <Tp> | [0..1] | CodeSet | | 394 |
| | FromToDate <FrToDt> | [0..1] | ± | | 395 |
| | TaxAmount <TaxAmt> | [0..1] | | | 396 |
| | Rate <Rate> | [0..1] | Rate | | 396 |
| | TaxableBaseAmount <TaxblBaseAmt> | [0..1] | Amount | C2, C8 | 396 |
| | TotalAmount <TtlAmt> | [0..1] | Amount | C2, C8 | 396 |
| | Details <Dtls> | [0.*] | | | 397 |
| | Period <Prd> | [0..1] | | | 397 |
| | Year <Yr> | [0..1] | Year | | 397 |
| | Type <Tp> | [0..1] | CodeSet | | 398 |
| | FromToDate <FrToDt> | [0..1] | ± | | 398 |
| | Amount <Amt> | [1..1] | Amount | C2, C8 | 399 |

---

<!-- Page 390 -->

| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | AdditionalInformation <AddtlInf> | [0..1] | Text | | 399 |

## 6.1.18.2.6.1 Creditor <Cdrtr>

*Presence:* [0..1]

*Definition:* Party on the credit side of the transaction to which the tax applies.

**Creditor <Cdrtr>** contains the following elements (see “**TaxParty1**” on page 405 for details)

| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | TaxIdentification <TaxId> | [0..1] | Text | | 405 |
| | RegistrationIdentification <RegnId> | [0..1] | Text | | 405 |
| | TaxType <TaxTp> | [0..1] | Text | | 406 |

## 6.1.18.2.6.2 Debtor <Dbtr>

*Presence:* [0..1]

*Definition:* Party on the debit side of the transaction to which the tax applies.

**Debtor <Dbtr>** contains the following elements (see “**TaxParty2**” on page 406 for details)

| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | TaxIdentification <TaxId> | [0..1] | Text | | 406 |
| | RegistrationIdentification <RegnId> | [0..1] | Text | | 406 |
| | TaxType <TaxTp> | [0..1] | Text | | 406 |
| | Authorisation <AuthStr> | [0..1] | | | 406 |
| | Title <Title> | [0..1] | Text | | 407 |
| | Name <Nm> | [0..1] | Text | | 407 |

## 6.1.18.2.6.3 UltimateDebtor <UltmtDbtr>

*Presence:* [0..1]

*Definition:* Ultimate party that owes an amount of money to the (ultimate) creditor, in this case, to the taxing authority.

---

<!-- Page 391 -->

UltimateDebtor <Ultmtdbtr> contains the following elements (see "TaxParty2" on page 406 for details)



| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | TaxIdentification <TaxId> | [0..1] | Text | | 406 |
| | RegistrationIdentification <RegnId> | [0..1] | Text | | 406 |
| | TaxType <TaxTp> | [0..1] | Text | | 406 |
| | Authorisation <Authstr> | [0..1] | | | 406 |
| | Title <Title> | [0..1] | Text | | 407 |
| | Name <Nm> | [0..1] | Text | | 407 |

## 6.1.18.2.6.4 AdministrationZone <AdmstnZone>

*Presence:* [0..1]

*Definition:* Territorial part of a country to which the tax payment is related.

*Datatype:* "Max35Text" on page 431

## 6.1.18.2.6.5 ReferenceNumber <RefNb>

*Presence:* [0..1]

*Definition:* Tax reference information that is specific to a taxing agency.

*Datatype:* "Max140Text" on page 429

## 6.1.18.2.6.6 Method <Mtd>

*Presence:* [0..1]

*Definition:* Method used to indicate the underlying business or how the tax is paid.

*Datatype:* "Max35Text" on page 431

## 6.1.18.2.6.7 TotalTaxableBaseAmount <TtlTaxblBaseAmt>

*Presence:* [0..1]

*Definition:* Total amount of money on which the tax is based.

*Impacted by:* C2 "ActiveOrHistoricCurrency", C8 "CurrencyAmount"

*Datatype:* "ActiveOrHistoricCurrencyAndAmount" on page 407

### Constraints

- **ActiveOrHistoricCurrency**

The Currency Code must be registered, or have already been registered. Valid active or historic currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and may be or not be withdrawn on the day the message containing the Currency is exchanged.

- **CurrencyAmount**

The number of fractional digits (or minor unit of currency) must comply with ISO 4217.

---

<!-- Page 392 -->

Note: The decimal separator is a dot.

**6.1.18.2.6.8 TotalTaxAmount <TtlTaxAmt>**

*Presence:* [0..1]

*Definition:* Total amount of money as result of the calculation of the tax.

*Impacted by:* C2 "ActiveOrHistoricCurrency", C8 "CurrencyAmount"

*Datatype:* "ActiveOrHistoricCurrencyAndAmount" on page 407

**Constraints**

- **ActiveOrHistoricCurrency**

  The Currency Code must be registered, or have already been registered. Valid active or historic currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and may be or not be withdrawn on the day the message containing the Currency is exchanged.

- **CurrencyAmount**

  The number of fractional digits (or minor unit of currency) must comply with ISO 4217.

  Note: The decimal separator is a dot.

**6.1.18.2.6.9 Date <Dt>**

*Presence:* [0..1]

*Definition:* Date by which tax is due.

*Datatype:* "ISODate" on page 425

**6.1.18.2.6.10 SequenceNumber <SeqNb>**

*Presence:* [0..1]

*Definition:* Sequential number of the tax report.

*Datatype:* "Number" on page 427

**6.1.18.2.6.11 Record <Rcrd>**

*Presence:* [0..*]

*Definition:* Record of tax details.

---

<!-- Page 393 -->

Record `<Rcrd>` contains the following **TaxRecord3** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Type `<Tp>` | [0..1] | Text | | 393 |
| | Category `<Ctgy>` | [0..1] | Text | | 393 |
| | CategoryDetails `<CtgyDtls>` | [0..1] | Text | | 393 |
| | DebtorStatus `<DbtrSts>` | [0..1] | Text | | 394 |
| | CertificateIdentification `<CertId>` | [0..1] | Text | | 394 |
| | FormsCode `<FrmsCd>` | [0..1] | Text | | 394 |
| | Period `<Prd>` | [0..1] | | | 394 |
| | Year `<Yr>` | [0..1] | Year | | 394 |
| | Type `<Tp>` | [0..1] | CodeSet | | 394 |
| | FromToDate `<FrToDt>` | [0..1] | ± | | 395 |
| | TaxAmount `<TaxAmt>` | [0..1] | | | 396 |
| | Rate `<Rate>` | [0..1] | Rate | | 396 |
| | TaxableBaseAmount `<TaxblBaseAmt>` | [0..1] | Amount | C2, C8 | 396 |
| | TotalAmount `<TtlAmt>` | [0..1] | Amount | C2, C8 | 396 |
| | Details `<Dtls>` | [0.*] | | | 397 |
| | Period `<Prd>` | [0..1] | | | 397 |
| | Year `<Yr>` | [0..1] | Year | | 397 |
| | Type `<Tp>` | [0..1] | CodeSet | | 398 |
| | FromToDate `<FrToDt>` | [0..1] | ± | | 398 |
| | Amount `<Amt>` | [1..1] | Amount | C2, C8 | 399 |
| | AdditionalInformation `<AddtlInf>` | [0..1] | Text | | 399 |

**6.1.18.2.6.11.1 Type `<Tp>`**

*Presence:* [0..1]

*Definition:* High level code to identify the type of tax details.

*Datatype:* "Max35Text" on page 431

**6.1.18.2.6.11.2 Category `<Ctgy>`**

*Presence:* [0..1]

*Definition:* Specifies the tax code as published by the tax authority.

*Datatype:* "Max35Text" on page 431

**6.1.18.2.6.11.3 CategoryDetails `<CtgyDtls>`**

*Presence:* [0..1]

---

<!-- Page 394 -->

Definition: Provides further details of the category tax code.
Datatype: "Max35Text" on page 431

## 6.1.18.2.6.11.4 DebtorStatus <DbtrSts>

Presence: [0..1]

Definition: Code provided by local authority to identify the status of the party that has drawn up the settlement document.

Datatype: "Max35Text" on page 431

## 6.1.18.2.6.11.5 CertificateIdentification <CrtId>

Presence: [0..1]

Definition: Identification number of the tax report as assigned by the taxing authority.

Datatype: "Max35Text" on page 431

## 6.1.18.2.6.11.6 FormsCode <FrmsCd>

Presence: [0..1]

Definition: Identifies, in a coded form, on which template the tax report is to be provided.

Datatype: "Max35Text" on page 431

## 6.1.18.2.6.11.7 Period <Prd>

Presence: [0..1]

Definition: Set of elements used to provide details on the period of time related to the tax payment.

**Period <Prd>** contains the following **TaxPeriod3** elements

| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | Year <Yr> | [0..1] | Year | | 394 |
| | Type <Tp> | [0..1] | CodeSet | | 394 |
| | FromToDate <FrToDt> | [0..1] | ± | | 395 |

### 6.1.18.2.6.11.7.1 Year <Yr>

Presence: [0..1]

Definition: Year related to the tax payment.

Datatype: "ISOYear" on page 432

### 6.1.18.2.6.11.7.2 Type <Tp>

Presence: [0..1]

Definition: Identification of the period related to the tax payment.

Datatype: "TaxRecordPeriod1Code" on page 424

| CodeName | Name | Definition |
|:---|:---|:---|
| MM01 | FirstMonth | Tax is related to the second month of the period. |

---

<!-- Page 395 -->

| CodeName | Name | Definition |
|---|---|---|
| MM02 | SecondMonth | Tax is related to the first month of the period. |
| MM03 | ThirdMonth | Tax is related to the third month of the period. |
| MM04 | FourthMonth | Tax is related to the fourth month of the period. |
| MM05 | FifthMonth | Tax is related to the fifth month of the period. |
| MM06 | SixthMonth | Tax is related to the sixth month of the period. |
| MM07 | SeventhMonth | Tax is related to the seventh month of the period. |
| MM08 | EighthMonth | Tax is related to the eighth month of the period. |
| MM09 | NinthMonth | Tax is related to the ninth month of the period. |
| MM10 | TenthMonth | Tax is related to the tenth month of the period. |
| MM11 | EleventhMonth | Tax is related to the eleventh month of the period. |
| MM12 | TwelfthMonth | Tax is related to the twelfth month of the period. |
| QTR1 | FirstQuarter | Tax is related to the first quarter of the period. |
| QTR2 | SecondQuarter | Tax is related to the second quarter of the period. |
| QTR3 | ThirdQuarter | Tax is related to the third quarter of the period. |
| QTR4 | FourthQuarter | Tax is related to the forth quarter of the period. |
| HLF1 | FirstHalf | Tax is related to the first half of the period. |
| HLF2 | SecondHalf | Tax is related to the second half of the period. |

**6.1.18.2.6.11.7.3 FromToDate <FrToDt>**

*Presence:* [0..1]

*Definition:* Range of time between a start date and an end date for which the tax report is provided.

FromToDate <FrToDt> contains the following elements (see "DatePeriod2" on page 316 for details)

| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | FromDate <FrDt> | [1..1] | Date |  | 316 |
| | ToDate <ToDt> | [1..1] | Date |  | 316 |

---

<!-- Page 396 -->

### 6.1.18.2.6.11.8 TaxAmount <TaxAmt>

*Presence: [0..1]*

*Definition: Set of elements used to provide information on the amount of the tax record.*

**TaxAmount <TaxAmt>** contains the following **TaxAmount3** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
| :--- | :--- | :--- | :--- | :--- | :--- |
| | Rate *<Rate>* | [0..1] | Rate | | 396 |
| | TaxableBaseAmount *<TaxblBaseAmt>* | [0..1] | Amount | C2, C8 | 396 |
| | TotalAmount *<TtlAmt>* | [0..1] | Amount | C2, C8 | 396 |
| | Details *<Dtls>* | [0..*] | | | 397 |
| | Period *<Prd>* | [0..1] | | | 397 |
| | Year *<Yr>* | [0..1] | Year | | 397 |
| | Type *<Tp>* | [0..1] | CodeSet | | 398 |
| | FromToDate *<FrToDt>* | [0..1] | ± | | 398 |
| | Amount *<Amt>* | [1..1] | Amount | C2, C8 | 399 |

### 6.1.18.2.6.11.8.1 Rate <Rate>

*Presence: [0..1]*

*Definition: Rate used to calculate the tax.*

*Datatype: "PercentageRate" on page 428*

### 6.1.18.2.6.11.8.2 TaxableBaseAmount <TaxblBaseAmt>

*Presence: [0..1]*

*Definition: Amount of money on which the tax is based.*

*Impacted by: C2 "ActiveOrHistoricCurrency", C8 "CurrencyAmount"*

*Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 407*

**Constraints**

*   **ActiveOrHistoricCurrency**

    The Currency Code must be registered, or have already been registered. Valid active or historic currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and may be or not be withdrawn on the day the message containing the Currency is exchanged.

*   **CurrencyAmount**

    The number of fractional digits (or minor unit of currency) must comply with ISO 4217.

    Note: The decimal separator is a dot.

### 6.1.18.2.6.11.8.3 TotalAmount <TtlAmt>

*Presence: [0..1]*

---

<!-- Page 397 -->

*Definition:* Total amount that is the result of the calculation of the tax for the record.

*Impacted by:* C2 "ActiveOrHistoricCurrency", C8 "CurrencyAmount"

*Datatype:* "ActiveOrHistoricCurrencyAndAmount" on page 407

## Constraints

- **ActiveOrHistoricCurrency**

The Currency Code must be registered, or have already been registered. Valid active or historic currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and may be or not be withdrawn on the day the message containing the Currency is exchanged.

- **CurrencyAmount**

The number of fractional digits (or minor unit of currency) must comply with ISO 4217.

Note: The decimal separator is a dot.

## 6.1.18.2.6.11.8.4 Details <Dtls>

*Presence:* [0..*]

*Definition:* Set of elements used to provide details on the tax period and amount.

**Details <Dtls>** contains the following **TaxRecordDetails3** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Period <Prd> | [0..1] | | | 397 |
| | Year <Yr> | [0..1] | Year | | 397 |
| | Type <Tp> | [0..1] | CodeSet | | 398 |
| | FromToDate <FrToDt> | [0..1] | ± | | 398 |
| | Amount <Amt> | [1..1] | Amount | C2, C8 | 399 |

## 6.1.18.2.6.11.8.4.1 Period <Prd>

*Presence:* [0..1]

*Definition:* Set of elements used to provide details on the period of time related to the tax payment.

**Period <Prd>** contains the following **TaxRecordDetails3** elements

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | Year <Yr> | [0..1] | Year | | 397 |
| | Type <Tp> | [0..1] | CodeSet | | 398 |
| | FromToDate <FrToDt> | [0..1] | ± | | 398 |

## 6.1.18.2.6.11.8.4.1.1 Year <Yr>

*Presence:* [0..1]

*Definition:* Year related to the tax payment.

---

<!-- Page 398 -->

Datatype: "ISOYear" on page 432

### 6.1.18.2.6.11.8.4.1.2 Type <Tp>

Presence: [0..1]

Definition: Identification of the period related to the tax payment.

Datatype: "TaxRecordPeriod1Code" on page 424



| CodeName | Name | Definition |
|---|---|---|
| MM01 | FirstMonth | Tax is related to the second month of the period. |
| MM02 | SecondMonth | Tax is related to the first month of the period. |
| MM03 | ThirdMonth | Tax is related to the third month of the period. |
| MM04 | FourthMonth | Tax is related to the fourth month of the period. |
| MM05 | FifthMonth | Tax is related to the fifth month of the period. |
| MM06 | SixthMonth | Tax is related to the sixth month of the period. |
| MM07 | SeventhMonth | Tax is related to the seventh month of the period. |
| MM08 | EighthMonth | Tax is related to the eighth month of the period. |
| MM09 | NinthMonth | Tax is related to the ninth month of the period. |
| MM10 | TenthMonth | Tax is related to the tenth month of the period. |
| MM11 | EleventhMonth | Tax is related to the eleventh month of the period. |
| MM12 | TwelfthMonth | Tax is related to the twelfth month of the period. |
| QTR1 | FirstQuarter | Tax is related to the first quarter of the period. |
| QTR2 | SecondQuarter | Tax is related to the second quarter of the period. |
| QTR3 | ThirdQuarter | Tax is related to the third quarter of the period. |
| QTR4 | FourthQuarter | Tax is related to the forth quarter of the period. |
| HLF1 | FirstHalf | Tax is related to the first half of the period. |
| HLF2 | SecondHalf | Tax is related to the second half of the period. |

### 6.1.18.2.6.11.8.4.1.3 FromToDate <FrToDt>

Presence: [0..1]

---

<!-- Page 399 -->

*Definition:* Range of time between a start date and an end date for which the tax report is provided.

**FromToDate <FrToD>** contains the following elements (see "DatePeriod2" on page 316 for details)



| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | FromDate <FrD/> | [1..1] | Date |  | 316 |
| | ToDate <ToD/> | [1..1] | Date |  | 316 |

## 6.1.18.2.6.11.8.4.2 Amount <Amt>

*Presence:* [1..1]

*Definition:* Underlying tax amount related to the specified period.

*Impacted by:* C2 "ActiveOrHistoricCurrency", C8 "CurrencyAmount"

*Datatype:* "ActiveOrHistoricCurrencyAndAmount" on page 407

**Constraints**

- **ActiveOrHistoricCurrency**

The Currency Code must be registered, or have already been registered. Valid active or historic currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and may be or not be withdrawn on the day the message containing the Currency is exchanged.

- **CurrencyAmount**

The number of fractional digits (or minor unit of currency) must comply with ISO 4217.

Note: The decimal separator is a dot.

## 6.1.18.2.6.11.9 AdditionalInformation <AddtlInf>

*Presence:* [0..1]

*Definition:* Further details of the tax record.

*Datatype:* "Max140Text" on page 429

## 6.1.18.2.7 GarnishmentRemittance <GrnshmtRmt>

*Presence:* [0..1]

*Definition:* Provides remittance information about a payment for garnishment-related purposes.

---

<!-- Page 400 -->

GarnishmentRemittance <GrnshmtRmt> contains the following Garnishment4 elements

| Or | **MessageElement<XML Tag>** | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | Type <Tp> | [1..1] | | | 400 |
| | CodeOrProprietary <CdOrPtry> | [1..1] | | | 400 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 401 |
| Or) | Proprietary <Ptry> | [1..1] | Text | | 401 |
| | Issuer <Issr> | [0..1] | Text | | 401 |
| | Garnishee <Gmshee> | [0..1] | ± | | 401 |
| | GarnishmentAdministrator <GrnshmtAdmstr> | [0..1] | ± | | 402 |
| | ReferenceNumber <RefNb> | [0..1] | Text | | 403 |
| | Date <Dt> | [0..1] | Date | | 404 |
| | RemittedAmount <RmttdAmt> | [0..1] | Amount | C2, C8 | 404 |
| | FamilyMedicalInsuranceIndicator <FmyMdclInsrncInd> | [0..1] | Indicator | | 404 |
| | EmployeeTerminationIndicator <MplyeeTermInd> | [0..1] | Indicator | | 404 |

**6.1.18.2.7.1 Type <Tp>**

*Presence:* [1..1]

*Definition:* Specifies the type of garnishment.

Type <Tp> contains the following GarnishmentType1 elements

| Or | **MessageElement<XML Tag>** | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | CodeOrProprietary <CdOrPtry> | [1..1] | | | 400 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 401 |
| Or) | Proprietary <Ptry> | [1..1] | Text | | 401 |
| | Issuer <Issr> | [0..1] | Text | | 401 |

**6.1.18.2.7.1.1 CodeOrProprietary <CdOrPtry>**

*Presence:* [1..1]

*Definition:* Provides the type details of the garnishment.

CodeOrProprietary <CdOrPtry> contains one of the following GarnishmentType1Choice elements

| Or | **MessageElement<XML Tag>** | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| (Or | Code <Cd> | [1..1] | CodeSet | | 401 |
| Or) | Proprietary <Ptry> | [1..1] | Text | | 401 |

---

<!-- Page 401 -->

**6.1.18.2.7.1.1.1 Code <Cd>**

*Presence:* [1..1]

*Definition:* Garnishment type in a coded form.

Would suggest this to be an External Code List to contain:

GNCS Garnishment from a third party payer for Child Support

GNDP Garnishment from a Direct Payer for Child Support

GTPP Garnishment from a third party payer to taxing agency.

*Datatype:* "ExternalGarnishmentType1Code" on page 416

**6.1.18.2.7.1.1.2 Proprietary <Ptry>**

*Presence:* [1..1]

*Definition:* Proprietary identification of the type of garnishment.

*Datatype:* "Max35Text" on page 431

**6.1.18.2.7.1.2 Issuer <Issr>**

*Presence:* [0..1]

*Definition:* Identification of the issuer of the garnishment type.

*Datatype:* "Max35Text" on page 431

**6.1.18.2.7.2 Garnishee <Grnshee>**

*Presence:* [0..1]

*Definition:* Ultimate party that owes an amount of money to the (ultimate) creditor, in this case, to the garnisher.

---

<!-- Page 402 -->

Garnishee <Gnrshsee> contains the following elements (see 'PartyIdentification27' on page 336 for details)

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
| :--- | :--- | :--- | :--- | :--- | :--- |
| | Name <Nm> | [0..1] | Text | | 337 |
| | PostalAddress <PstlAdr> | [0..1] | ± | | 338 |
| | Identification <Id> | [0..1] | | | 338 |
| (Or | OrganisationIdentification <OrgId> | [1..1] | | | 339 |
| | AnyBIC <AnyBIC> | [0..1] | IdentifierSet | C5 | 340 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 340 |
| | Other <Othr> | [0..*] | | | 340 |
| | Identification <Id> | [1..1] | Text | | 341 |
| | SchemeName <SchrmNm> | [0..1] | | | 341 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 341 |
| Or | Proprietary <Prtry> | [1..1] | Text | | 341 |
| | Issuer <Issr> | [0..1] | Text | | 341 |
| Or | PrivateIdentification <PrvtId> | [1..1] | | | 341 |
| | DateAndPlaceOfBirth <DtAndPlcOfBirth> | [0..1] | | | 342 |
| | BirthDate <BirthDt> | [1..1] | Date | | 342 |
| | ProvinceOfBirth <PrvcOfBirth> | [0..1] | Text | | 342 |
| | CityOfBirth <CityOfBirth> | [1..1] | Text | | 343 |
| | CountryOfBirth <CtryOfBirth> | [1..1] | CodeSet | C7 | 343 |
| | Other <Othr> | [0..*] | | | 343 |
| | Identification <Id> | [1..1] | Text | | 343 |
| | SchemeName <SchrmNm> | [0..1] | | | 343 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 344 |
| Or | Proprietary <Prtry> | [1..1] | Text | | 344 |
| | Issuer <Issr> | [0..1] | Text | | 344 |
| | CountryOfResidence <CtryOfRes> | [0..1] | CodeSet | C7 | 344 |
| | ContactDetails <CtctDtls> | [0..1] | ± | | 344 |

**6.1.18.2.7.3 GarnishmentAdministrator <GnshmtAdmstr>**
*Presence: [0..1]*
*Definition: Party on the credit side of the transaction who administers the garnishment on behalf of the ultimate beneficiary.*

---

<!-- Page 403 -->

GarnishmentAdministrator <GrrnsHmtAdmstr> contains the following elements (see "PartyIdentification27" on page 336 for details)

| Or | MessageElement <XML Tag> | Mult. | Type | Constr. No. | Page |
|:---|:---|:---|:---|:---|:---|
| | Name <Nm> | [0..1] | Text | | 337 |
| | PostalAddress <PstlAdr> | | ± | | 338 |
| | Identification <Id> | [0..1] | | | 338 |
| (Or | OrganisationIdentification <OrgId> | [1..1] | | | 339 |
| | AnyBIC <AnyBIC> | [0..1] | IdentifierSet | C5 | 340 |
| | LEI <LEI> | [0..1] | IdentifierSet | | 340 |
| | Other <Othr> | [0..*] | | | 340 |
| | Identification <Id> | [1..1] | Text | | 341 |
| | SchemeName <SchmeNm> | [0..1] | | | 341 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 341 |
| Or) | Proprietary <Prtry> | [1..1] | Text | | 341 |
| | Issuer <Issr> | [0..1] | Text | | 341 |
| (Or) | PrivateIdentification <PrvtId> | [1..1] | | | 341 |
| | DateAndPlaceOfBirth <DtAndPlcOfBirth> | [0..1] | | | 342 |
| | BirthDate <BirthDt> | [1..1] | Date | | 342 |
| | ProvinceOfBirth <PrvcOfBirth> | [0..1] | Text | | 342 |
| | CityOfBirth <CityOfBirth> | [1..1] | Text | | 343 |
| | CountryOfBirth <CtryOfBirth> | [1..1] | CodeSet | C7 | 343 |
| | Other <Othr> | [0..*] | | | 343 |
| | Identification <Id> | [1..1] | Text | | 343 |
| | SchemeName <SchmeNm> | [0..1] | | | 343 |
| (Or | Code <Cd> | [1..1] | CodeSet | | 344 |
| Or) | Proprietary <Prtry> | [1..1] | Text | | 344 |
| | Issuer <Issr> | [0..1] | Text | | 344 |
| | CountryOfResidence <CtryOfRes> | [0..1] | CodeSet | C7 | 344 |
| | ContactDetails <CtctDtls> | [0..1] | ± | | 344 |

**6.1.18.2.7.4 ReferenceNumber <RefNb>**

*Presence:* [0..1]

*Definition:* Reference information that is specific to the agency receiving the garnishment.

*Datatype:* "Max140Text" on page 429

---

<!-- Page 404 -->

**6.1.18.2.7.5 Date <Dt>**
*Presence:* [0..1]
*Definition:* Date of payment which garnishment was taken from.
*Datatype:* "ISODate" on page 425

**6.1.18.2.7.6 RemittedAmount <RmtdAmt>**
*Presence:* [0..1]
*Definition:* Amount of money remitted for the referred document.
*Impacted by:* C2 "ActiveOrHistoricCurrency", C8 "CurrencyAmount"
*Datatype:* "ActiveOrHistoricCurrencyAndAmount" on page 407

**Constraints**
* **ActiveOrHistoricCurrency**
    The Currency Code must be registered, or have already been registered. Valid active or historic currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and may be or not be withdrawn on the day the message containing the Currency is exchanged.
* **CurrencyAmount**
    The number of fractional digits (or minor unit of currency) must comply with ISO 4217.

    Note: The decimal separator is a dot.

**6.1.18.2.7.7 FamilyMedicalInsuranceIndicator <FmlyMdclInsrncInd>**
*Presence:* [0..1]
*Definition:* Indicates if the person to whom the garnishment applies (that is, the ultimate debtor) has family medical insurance coverage available.
*Datatype:* One of the following values must be used (see "TrueFalseIndicator" on page 427):
* *Meaning When True:* True
* *Meaning When False:* False

**6.1.18.2.7.8 EmployeeTerminationIndicator <MplyeeTermnInd>**
*Presence:* [0..1]
*Definition:* Indicates if the employment of the person to whom the garnishment applies (that is, the ultimate debtor) has been terminated.
*Datatype:* One of the following values must be used (see "TrueFalseIndicator" on page 427):
* *Meaning When True:* True
* *Meaning When False:* False

**6.1.18.2.8 AdditionalRemittanceInformation <AddtlRmtInf>**
*Presence:* [0..3]
*Definition:* Additional information, in free text form, to complement the structured remittance information.
*Datatype:* "Max140Text" on page 429

---

<!-- Page 405 -->

## 6.1.19 System Identification

### 6.1.19.1 ClearingSystemIdentification2Choice

*Definition: Choice of a clearing system identifier.*

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| (Or | Code <Cd> | [1..1] | CodeSet | | 405 |
| (Or) | Proprietary <Prtry> | [1..1] | Text | | 405 |

#### 6.1.19.1.1 Code <Cd>

*Presence: [1..1]*

*Definition: Identification of a clearing system, in a coded form as published in an external list.*

*Datatype: "ExternalClearingSystemIdentification1Code" on page 414*

#### 6.1.19.1.2 Proprietary <Prtry>

*Presence: [1..1]*

*Definition: Identification code for a clearing system, that has not yet been identified in the list of clearing systems.*

*Datatype: "Max35Text" on page 431*

## 6.1.20 Tax

### 6.1.20.1 TaxParty1

*Definition: Details about the entity involved in the tax paid or to be paid.*

| Or | MessageElement<XML Tag> | Mult. | Type | Constr. No. | Page |
|---|---|---|---|---|---|
| | TaxIdentification <TaxId> | [0..1] | Text | | 405 |
| | RegistrationIdentification <RegnId> | [0..1] | Text | | 405 |
| | TaxType <TaxTp> | [0..1] | Text | | 406 |

#### 6.1.20.1.1 TaxIdentification <TaxId>

*Presence: [0..1]*

*Definition: Tax identification number of the creditor.*

*Datatype: "Max35Text" on page 431*

#### 6.1.20.1.2 RegistrationIdentification <RegnId>

*Presence: [0..1]*

*Definition: Unique identification, as assigned by an organisation, to unambiguously identify a party.*

*Datatype: "Max35Text" on page 431*

---

<!-- Page 406 -->

6.1.20.1.3 **TaxType** *&lt;TaxTp&gt;*

*Presence:* [0..1]

*Definition:* Type of tax payer.

*Datatype:* "Max35Text" on page 431

## 6.1.20.2 TaxParty2

*Definition:* Details about the entity involved in the tax paid or to be paid.



<table>
  <tr>
    <th>Or</th>
    <th>MessageElement&lt;XML Tag&gt;</th>
    <th>Mult.</th>
    <th>Type</th>
    <th>Constr. No.</th>
    <th>Page</th>
  </tr>
  <tr>
    <td></td>
    <td>TaxIdentification &lt;TaxId&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>406</td>
  </tr>
  <tr>
    <td></td>
    <td>RegistrationIdentification &lt;RegnId&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>406</td>
  </tr>
  <tr>
    <td></td>
    <td>TaxType &lt;TaxTp&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>406</td>
  </tr>
  <tr>
    <td></td>
    <td>Authorisation &lt;AuthStrn&gt;</td>
    <td>[0..1]</td>
    <td></td>
    <td></td>
    <td>406</td>
  </tr>
  <tr>
    <td></td>
    <td>Title &lt;Titl&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>407</td>
  </tr>
  <tr>
    <td></td>
    <td>Name &lt;Nm&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>407</td>
  </tr>
</table>

### 6.1.20.2.1 TaxIdentification *&lt;TaxId&gt;*

*Presence:* [0..1]

*Definition:* Tax identification number of the debtor.

*Datatype:* "Max35Text" on page 431

### 6.1.20.2.2 RegistrationIdentification *&lt;RegnId&gt;*

*Presence:* [0..1]

*Definition:* Unique identification, as assigned by an organisation, to unambiguously identify a party.

*Datatype:* "Max35Text" on page 431

### 6.1.20.2.3 TaxType *&lt;TaxTp&gt;*

*Presence:* [0..1]

*Definition:* Type of tax payer.

*Datatype:* "Max35Text" on page 431

### 6.1.20.2.4 Authorisation *&lt;AuthStrn&gt;*

*Presence:* [0..1]

*Definition:* Details of the authorised tax paying party.

**Authorisation** *&lt;AuthStrn&gt;* contains the following **TaxAuthorisation1** elements



<table>
  <tr>
    <th>Or</th>
    <th>MessageElement&lt;XML Tag&gt;</th>
    <th>Mult.</th>
    <th>Type</th>
    <th>Constr. No.</th>
    <th>Page</th>
  </tr>
  <tr>
    <td></td>
    <td>Title &lt;Titl&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>407</td>
  </tr>
  <tr>
    <td></td>
    <td>Name &lt;Nm&gt;</td>
    <td>[0..1]</td>
    <td>Text</td>
    <td></td>
    <td>407</td>
  </tr>
</table>

---

<!-- Page 407 -->

6.1.20.2.4.1 Title <Ttl>
*Presence:* [0..1]
*Definition:* Title or position of debtor or the debtor's authorised representative.
*Datatype:* "Max35Text" on page 431

6.1.20.2.4.2 Name <Nm>
*Presence:* [0..1]
*Definition:* Name of the debtor or the debtor's authorised representative.
*Datatype:* "Max140Text" on page 429

## 6.2 Message Datatypes

### 6.2.1 Amount

#### 6.2.1.1 ActiveCurrencyAndAmount
*Definition:* A number of monetary units specified in an active currency where the unit of currency is explicit and compliant with ISO 4217.
*Type:* Amount

This data type contains the following XML attribute:

| Name | Attribute XML Name | Datatype |
| :--- | :--- | :--- |
| Currency | Ccy | "ActiveCurrencyCode" on page 408 |

**Format**
minInclusive 0
totalDigits 18
fractionDigits 5

**Constraints**
*   **ActiveCurrency**
    The currency code must be a valid active currency code, not yet withdrawn on the day the message containing the currency is exchanged. Valid active currency codes are registered on the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day the message containing the Currency is exchanged.
*   **CurrencyAmount**
    The number of fractional digits (or minor unit of currency) must comply with ISO 4217.

Note: The decimal separator is a dot.

#### 6.2.1.2 ActiveOrHistoricCurrencyAndAmount
*Definition:* A number of monetary units specified in an active or a historic currency where the unit of currency is explicit and compliant with ISO 4217.

---

<!-- Page 408 -->

*Type: Amount*

This data type contains the following XML attribute:



<table>
  <tr>
    <th>Name</th>
    <th>Attribute XML Name</th>
    <th>Datatype</th>
  </tr>
  <tr>
    <td>Currency</td>
    <td>Ccy</td>
    <td>"ActiveOrHistoricCurrencyCode" on page 409</td>
  </tr>
</table>

**Format**

minInclusive 0

totalDigits 18

fractionDigits 5

**Constraints**

- **ActiveOrHistoricCurrency**

The Currency Code must be registered, or have already been registered. Valid active or historic currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and may be or not be withdrawn on the day the message containing the Currency is exchanged.

- **CurrencyAmount**

The number of fractional digits (or minor unit of currency) must comply with ISO 4217.

Note: The decimal separator is a dot.

## 6.2.2 Binary

### 6.2.2.1 Max10KBinary

*Definition:* Binary data of 10K maximum.

*Type:* Binary

**Format**

minLength 1

maxLength 10240

## 6.2.3 CodeSet

### 6.2.3.1 ActiveCurrencyCode

*Definition:* A code allocated to a currency by a Maintenance Agency under an international identification scheme as described in the latest edition of the international standard ISO 4217 "Codes for the representation of currencies and funds".

*Type:* CodeSet

**Format**

pattern [A-Z]{3,3}

---

<!-- Page 409 -->

Constraints
* **ActiveCurrency**
    The currency code must be a valid active currency code, not yet withdrawn on the day the message containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day the message containing the Currency is exchanged.

## 6.2.3.2 ActiveOrHistoricCurrencyCode

*Definition*: A code allocated to a currency by a Maintenance Agency under an international identification scheme, as described in the latest edition of the international standard ISO 4217 “Codes for the representation of currencies and funds”.

*Type*: CodeSet

**Format**

pattern [A-Z]{3,3}

**Constraints**
* **ActiveOrHistoricCurrency**
    The Currency Code must be registered, or have already been registered. Valid active or historic currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and may be or not be withdrawn on the day the message containing the Currency is exchanged.

## 6.2.3.3 AddressType2Code

*Definition*: Specifies the type of address.

*Type*: CodeSet

| CodeName | Name | Definition |
| :--- | :--- | :--- |
| ADDR | Postal | Address is the complete postal address. |
| PBOX | POBox | Address is a postal office (PO) box. |
| HOME | Residential | Address is the home address. |
| BIZZ | Business | Address is the business address. |
| MLTO | MailTo | Address is the address to which mail is sent. |
| DLVY | DeliveryTo | Address is the address to which delivery is to take place. |

## 6.2.3.4 AdviceType1Code

*Definition*: Specifies the type of advice to provide back in the report.

*Type*: CodeSet

| CodeName | Name | Definition |
| :--- | :--- | :--- |
| ADWD | AdviceWithDetails | Advice with transaction details is requested. |

---

<!-- Page 410 -->

| CodeName | Name | Definition |
|---|---|---|
| ADND | AdviceWithoutDetails | Advice without transaction details is requested. |

## 6.2.3.5 Authorisation1Code

*Definition:* Specifies the level of approval depending on a number of factors, including payment type, threshold amount or local country or operations practice.

*Type:* CodeSet

| CodeName | Name | Definition |
|---|---|---|
| AUTH | PreAuthorisedFile | Indicates a file has been pre authorised or approved within the originating customer environment and no further approval is required. |
| FDET | FileLevelAuthorisationDetails | Indicates that a file requires additional file level approval, with the ability to view both the payment information block and supporting customer credit transaction detail. |
| FSUM | FileLevelAuthorisationSummary | Indicates that a file requires additional file level approval, with the ability to view only the payment information block level information. |
| ILEV | InstructionLevelAuthorisation | Indicates that a file requires all customer transactions to be authorised or approved. |

## 6.2.3.6 ChargeBearerType1Code

*Definition:* Specifies which party(ies) will pay charges due for processing of the instruction.

*Type:* CodeSet

| CodeName | Name | Definition |
|---|---|---|
| DEBT | BorneByDebtor | All transaction charges are to be borne by the debtor. |
| CRED | BorneByCreditor | All transaction charges are to be borne by the creditor. |
| SHAR | Shared | In a credit transfer context, means that transaction charges on the sender side are to be borne by the debtor, transaction charges on the receiver side are to be borne by the creditor. In a direct debit context, means that transaction charges on the sender side are to be borne by the creditor, transaction charges on the receiver side are to be borne by the debtor. |
| SLEV | FollowingServiceLevel | Charges are to be applied following the rules agreed in the service level and/or scheme. |

---

<!-- Page 411 -->

## 6.2.3.7 ChequeDelivery1Code

*Definition: Specifies the method to be used in delivering a cheque to a party.*

Type: CodeSet



<table>
  <tr>
    <th>CodeName</th>
    <th>Name</th>
    <th>Definition</th>
  </tr>
  <tr>
    <td>MLDB</td>
    <td>MailToDebtor</td>
    <td>Cheque is to be sent through mail services to debtor.</td>
  </tr>
  <tr>
    <td>MLCD</td>
    <td>MailToCreditor</td>
    <td>Cheque is to be sent through mail services to creditor.</td>
  </tr>
  <tr>
    <td>MLFA</td>
    <td>MailToFinalAgent</td>
    <td>Cheque is to be sent through mail services to creditor agent.</td>
  </tr>
  <tr>
    <td>CRDB</td>
    <td>CourierToDebtor</td>
    <td>Cheque is to be sent through courier services to debtor.</td>
  </tr>
  <tr>
    <td>CRCD</td>
    <td>CourierToCreditor</td>
    <td>Cheque is to be sent through courier services to creditor.</td>
  </tr>
  <tr>
    <td>CRFA</td>
    <td>CourierToFinalAgent</td>
    <td>Cheque is to be sent through courier services to creditor agent.</td>
  </tr>
  <tr>
    <td>PUDb</td>
    <td>PickUpByDebtor</td>
    <td>Cheque will be picked up by the debtor.</td>
  </tr>
  <tr>
    <td>PUCD</td>
    <td>PickUpByCreditor</td>
    <td>Cheque will be picked up by the creditor.</td>
  </tr>
  <tr>
    <td>PUFA</td>
    <td>PickUpByFinalAgent</td>
    <td>Cheque will be picked up by the creditor agent.</td>
  </tr>
  <tr>
    <td>RGDB</td>
    <td>RegisteredMailToDebtor</td>
    <td>Cheque is to be sent through registered mail services to debtor.</td>
  </tr>
  <tr>
    <td>RGCD</td>
    <td>RegisteredMailToCreditor</td>
    <td>Cheque is to be sent through registered mail services to creditor.</td>
  </tr>
  <tr>
    <td>RGFA</td>
    <td>RegisteredMailToFinalAgent</td>
    <td>Cheque is to be sent through registered mail services to creditor agent.</td>
  </tr>
</table>

## 6.2.3.8 ChequeType2Code

*Definition: Specifies the type of cheque.*

Type: CodeSet



<table>
  <tr>
    <th>CodeName</th>
    <th>Name</th>
    <th>Definition</th>
  </tr>
  <tr>
    <td>CCHQ</td>
    <td>CustomerCheque</td>
    <td>Cheque drawn on the account of the debtor, and debited on the debtor's account when the cheque is cashed. Synonym is 'corporate cheque'.</td>
  </tr>
  <tr>
    <td>CCCH</td>
    <td>CertifiedCustomerCheque</td>
    <td>Cheque drawn on the account of the debtor, and debited on the debtor's account when the cheque is cashed. The financial institution prints and certifies the cheque, guaranteeing the payment.</td>
  </tr>
  <tr>
    <td>BCHQ</td>
    <td>BankCheque</td>
    <td>Cheque drawn on the account of the debtor's financial institution, which is debited on the debtor's account when the cheque is issued. These cheques are printed by the debtor's financial institution and payment is guaranteed by</td>
  </tr>
</table>

---

<!-- Page 412 -->

| CodeName | Name | Definition |
| :--- | :--- | :--- |
| | | the financial institution. Synonym is 'cashier's cheque'. |
| DRFT | Draft | A guaranteed bank cheque with a future value date (do not pay before), which in commercial terms is a 'negotiable instrument': the beneficiary can receive early payment from any bank under subtraction of a discount. The ordering customer's account is debited on value date. |
| ELDR | ElectronicDraft | An instrument with a future value date (do not pay before), which in commercial terms is a 'negotiable instrument': the beneficiary can receive early payment from any bank under subtraction of a discount. The ordering customer's account is debited on value date. |

## 6.2.3.9 ClearingChannel2Code

*Definition:* Specifies the clearing channel for the routing of the transaction, as part of the payment type identification.

*Type:* CodeSet

| CodeName | Name | Definition |
| :--- | :--- | :--- |
| RTGS | RealTimeGrossSettlementSystem | Clearing channel is a real-time gross settlement system. |
| RTNS | RealTimeNetSettlementSystem | Clearing channel is a real-time net settlement system. |
| MPNS | MassPaymentNetSystem | Clearing channel is a mass payment net settlement system. |
| BOOK | BookTransfer | Payment through internal book transfer. |

## 6.2.3.10 CountryCode

*Definition:* Code to identify a country, a dependency, or another area of particular geopolitical interest, on the basis of country names obtained from the United Nations (ISO 3166, Alpha-2 code).

*Type:* CodeSet

**Format**

pattern [A-Z]{2,2}

**Constraints**

- **Country**

The code is checked against the list of country names obtained from the United Nations (ISO 3166, Alpha-2 code).

## 6.2.3.11 CreditDebitCode

*Definition:* Specifies if an operation is an increase or a decrease.

---

<!-- Page 413 -->

Type: CodeSet

| CodeName | Name | Definition |
|---|---|---|
| CRDT | Credit | Operation is an increase. |
| DBIT | Debit | Operation is a decrease. |

## 6.2.3.12 ExchangeRateType1Code

*Definition: Specifies a type of financial or commercial document.*

Type: CodeSet

| CodeName | Name | Definition |
|---|---|---|
| SPOT | Spot | Exchange rate applied is the spot rate. |
| SALE | Sale | Exchange rate applied is the market rate at the time of the sale. |
| AGRD | Agreed | Exchange rate applied is the rate agreed between the parties. |

## 6.2.3.13 ExternalAccountIdentification1Code

*Definition: Specifies the external account identification scheme name code in the format of character string with a maximum length of 4 characters.*

The list of valid codes is an external code list published separately.

External code sets can be downloaded from www.iso20022.org.

Type: CodeSet

**Format**

minLength 1

maxLength 4

## 6.2.3.14 ExternalCashAccountType1Code

*Definition: Specifies the nature, or use, of the cash account in the format of character string with a maximum length of 4 characters.*

The list of valid codes is an external code list published separately.

External code sets can be downloaded from www.iso20022.org.

Type: CodeSet

**Format**

minLength 1

maxLength 4

---

<!-- Page 414 -->

**6.2.3.15 ExternalCashClearingSystem1Code**

*Definition:* Specifies the cash clearing system, as published in an external cash clearing system code list.

External code sets can be downloaded from www.iso20022.org.

*Type:* CodeSet

**Format**

minLength 1

maxLength 3

**6.2.3.16 ExternalCategoryPurpose1Code**

*Definition:* Specifies the category purpose, as published in an external category purpose code list.

External code sets can be downloaded from www.iso20022.org.

*Type:* CodeSet

**Format**

minLength 1

maxLength 4

**6.2.3.17 ExternalChargeType1Code**

*Definition:* Specifies the nature, or use, of the charges in the format of character string with a maximum length of 4 characters.

The list of valid codes is an external code list published separately.

External code sets can be downloaded from www.iso20022.org.

*Type:* CodeSet

**Format**

minLength 1

maxLength 4

**6.2.3.18 ExternalClearingSystemIdentification1Code**

*Definition:* Specifies the clearing system identification code, as published in an external clearing system identification code list.

External code sets can be downloaded from www.iso20022.org.

*Type:* CodeSet

**Format**

minLength 1

maxLength 5

---

<!-- Page 415 -->

**6.2.3.19 ExternalCreditorAgentInstruction1Code**

*Definition:* Specifies further instructions concerning the processing of a payment instruction, as provided to the creditor agent.

*Type:* CodeSet

**Format**

| minLength | 1 |
|---|---|
| maxLength | 4 |

**6.2.3.20 ExternalCreditorReferenceType1Code**

*Definition:* Specifies the type of creditor reference as published in an external creditor reference type code set.

External code sets can be downloaded from www.iso20022.org.

*Type:* CodeSet

**Format**

| minLength | 1 |
|---|---|
| maxLength | 4 |

**6.2.3.21 ExternalDateType1Code**

*Definition:* Defines the type of date, as published in an external date type code list.

External code sets can be downloaded from www.iso20022.org.

*Type:* CodeSet

**Format**

| minLength | 1 |
|---|---|
| maxLength | 4 |

**6.2.3.22 ExternalDebtorAgentInstruction1Code**

*Definition:* Specifies further instructions concerning the processing of a payment instruction, as provided to the creditor agent.

*Type:* CodeSet

**Format**

| minLength | 1 |
|---|---|
| maxLength | 4 |

**6.2.3.23 ExternalDocumentAmountType1Code**

*Definition:* Specifies the nature, or use, of the amount, as published in an external document amount type code set.

---

<!-- Page 416 -->

External code sets can be downloaded from www.iso20022.org.
*Type: CodeSet*

**Format**

| minLength | 1 |
|---|---|
| maxLength | 4 |

## 6.2.3.24 ExternalDocumentLineType1Code

*Definition:* Specifies the document line type as published in an external document type code list.
*Type: CodeSet*

**Format**

| minLength | 1 |
|---|---|
| maxLength | 4 |

## 6.2.3.25 ExternalDocumentType1Code

*Definition:* Specifies the document type as published in an external document type code list.

External code sets can be downloaded from www.iso20022.org.
*Type: CodeSet*

**Format**

| minLength | 1 |
|---|---|
| maxLength | 4 |

## 6.2.3.26 ExternalFinancialInstitutionIdentification1Code

*Definition:* Specifies the external financial institution identification scheme name code in the format of character string with a maximum length of 4 characters.

The list of valid codes is an external code list published separately.

External code sets can be downloaded from www.iso20022.org.
*Type: CodeSet*

**Format**

| minLength | 1 |
|---|---|
| maxLength | 4 |

## 6.2.3.27 ExternalGarnishmentType1Code

*Definition:* Specifies the garnishment type as published in an external document type code list.
*Type: CodeSet*

---

<!-- Page 417 -->

Format
minLength 1
maxLength 4

## 6.2.3.28 ExternalLocalInstrument1Code

*Definition:* Specifies the external local instrument code in the format of character string with a maximum length of 35 characters.

The list of valid codes is an external code list published separately.

External code sets can be downloaded from www.iso20022.org.

*Type:* CodeSet

**Format**
minLength 1
maxLength 35

## 6.2.3.29 ExternalMandateSetupReason1Code

*Definition:* Specifies the external mandate setup reason code in the format of character string with a maximum length of 4 characters.

External code sets can be downloaded from www.iso20022.org.

*Type:* CodeSet

**Format**
minLength 1
maxLength 4

## 6.2.3.30 ExternalOrganisationIdentification1Code

*Definition:* Specifies the external organisation identification scheme name code in the format of character string with a maximum length of 4 characters.

The list of valid codes is an external code list published separately.

External code sets can be downloaded from www.iso20022.org.

*Type:* CodeSet

**Format**
minLength 1
maxLength 4

## 6.2.3.31 ExternalPaymentGroupStatus1Code

*Definition:* Specifies the status of a group of payment instructions, as published in an external payment group status code set.

---

<!-- Page 418 -->

External code sets can be downloaded from www.iso20022.org.
*Type:* CodeSet

**Format**

minLength 1
maxLength 4

## 6.2.3.32 ExternalPaymentTransactionStatus1Code

*Definition:* Specifies the status of an individual payment instructions, as published in an external payment transaction status code set.

External code sets can be downloaded from www.iso20022.org.
*Type:* CodeSet

**Format**

minLength 1
maxLength 4

## 6.2.3.33 ExternalPersonIdentification1Code

*Definition:* Specifies the external person identification scheme name code in the format of character string with a maximum length of 4 characters.

The list of valid codes is an external code list published separately.

External code sets can be downloaded from www.iso20022.org.
*Type:* CodeSet

**Format**

minLength 1
maxLength 4

## 6.2.3.34 ExternalProxyAccountType1Code

*Definition:* Specifies the external proxy account type code, as published in the proxy account type external code set.

External code sets can be downloaded from www.iso20022.org.
*Type:* CodeSet

**Format**

minLength 1
maxLength 4

---

<!-- Page 419 -->

### 6.2.3.35 ExternalPurpose1Code

*Definition:* Specifies the external purpose code in the format of character string with a maximum length of 4 characters.

The list of valid codes is an external code list published separately.

External code sets can be downloaded from www.iso20022.org.

*Type:* CodeSet

**Format**

minLength 1

maxLength 4

### 6.2.3.36 ExternalReversalReason1Code

*Definition:* Specifies the reversal reason, as published in an external reversal reason code list.

External code sets can be downloaded from www.iso20022.org.

*Type:* CodeSet

**Format**

minLength 1

maxLength 4

### 6.2.3.37 ExternalServiceLevel1Code

*Definition:* Specifies the external service level code in the format of character string with a maximum length of 4 characters.

The list of valid codes is an external code list published separately.

External code sets can be downloaded from www.iso20022.org.

*Type:* CodeSet

**Format**

minLength 1

maxLength 4

### 6.2.3.38 ExternalStatusReason1Code

*Definition:* Specifies the status reason, as published in an external status reason code list.

External code sets can be downloaded from www.iso20022.org.

*Type:* CodeSet

**Format**

minLength 1

---

<!-- Page 420 -->

maxLength 4

## 6.2.3.39 Frequency6Code

*Definition: Specifies the regularity of an event.*

*Type: CodeSet*



<table>
  <tr>
    <th>CodeName</th>
    <th>Name</th>
    <th>Definition</th>
  </tr>
  <tr>
    <td>YEAR</td>
    <td>Annual</td>
    <td>Event takes place every year or once a year.</td>
  </tr>
  <tr>
    <td>MNTH</td>
    <td>Monthly</td>
    <td>Event takes place every month or once a month.</td>
  </tr>
  <tr>
    <td>QURT</td>
    <td>Quarterly</td>
    <td>Event takes place every three months or four times a year.</td>
  </tr>
  <tr>
    <td>MIAN</td>
    <td>SemiAnnual</td>
    <td>Event takes place every six months or two times a year.</td>
  </tr>
  <tr>
    <td>WEEK</td>
    <td>Weekly</td>
    <td>Event takes place once a week.</td>
  </tr>
  <tr>
    <td>DAIL</td>
    <td>Daily</td>
    <td>Event takes place every day.</td>
  </tr>
  <tr>
    <td>ADHO</td>
    <td>Adhoc</td>
    <td>Event takes place on request or as necessary.</td>
  </tr>
  <tr>
    <td>INDA</td>
    <td>IntraDay</td>
    <td>Event takes place several times a day.</td>
  </tr>
  <tr>
    <td>FRTN</td>
    <td>Fortnightly</td>
    <td>Event takes place every two weeks.</td>
  </tr>
</table>

## 6.2.3.40 MandateClassification1Code

*Definition: Specifies the type of direct debit amount, such as fixed or variable.*

*Type: CodeSet*



<table>
  <tr>
    <th>CodeName</th>
    <th>Name</th>
    <th>Definition</th>
  </tr>
  <tr>
    <td>FIXE</td>
    <td>Fixed</td>
    <td>Direct debit amount is fixed.</td>
  </tr>
  <tr>
    <td>USGB</td>
    <td>UsageBased</td>
    <td>Direct debit amount is based on usage.</td>
  </tr>
  <tr>
    <td>VARI</td>
    <td>Variable</td>
    <td>Direct debit amount is variable.</td>
  </tr>
</table>

## 6.2.3.41 NamePrefix2Code

*Definition: Specifies the terms used to formally address a person.*

*Type: CodeSet*



<table>
  <tr>
    <th>CodeName</th>
    <th>Name</th>
    <th>Definition</th>
  </tr>
  <tr>
    <td>DOCT</td>
    <td>Doctor</td>
    <td>Title of the person is Doctor or Dr.</td>
  </tr>
  <tr>
    <td>MADM</td>
    <td>Madam</td>
    <td>Title of the person is Madam.</td>
  </tr>
  <tr>
    <td>MISS</td>
    <td>Miss</td>
    <td>Title of the person is Miss.</td>
  </tr>
  <tr>
    <td>MIST</td>
    <td>Mister</td>
    <td>Title of the person is Mister or Mr.</td>
  </tr>
  <tr>
    <td>MIKS</td>
    <td>GenderNeutral</td>
    <td>Title of the person is gender neutral (Mx).</td>
  </tr>
</table>

---

<!-- Page 421 -->

## 6.2.3.42 PaymentMethod2Code

*Definition: Specifies the transfer method that will be used to transfer the cash.*

*Type: CodeSet*

| CodeName | Name | Definition |
|---|---|---|
| DD | DirectDebit | Collection of an amount of money from the debtor's bank account by the creditor. The amount of money and dates of collections may vary. |

## 6.2.3.43 PaymentMethod3Code

*Definition: Specifies the transfer method that will be used to transfer an amount of money.*

*Type: CodeSet*

| CodeName | Name | Definition |
|---|---|---|
| CHK | Cheque | Written order to a bank to pay a certain amount of money from one person to another person. |
| TRF | CreditTransfer | Transfer of an amount of money in the books of the account servicer. |
| TRA | TransferAdvice | Transfer of an amount of money in the books of the account servicer. An advice should be sent back to the account owner. |

## 6.2.3.44 PaymentMethod4Code

*Definition: Specifies the transfer method that will be used to transfer an amount of money.*

*Type: CodeSet*

| CodeName | Name | Definition |
|---|---|---|
| CHK | Cheque | Written order to a bank to pay a certain amount of money from one person to another person. |
| TRF | CreditTransfer | Transfer of an amount of money in the books of the account servicer. |
| DD | DirectDebit | Collection of an amount of money from the debtor's bank account by the creditor. The amount of money and dates of collections may vary. |
| TRA | TransferAdvice | Transfer of an amount of money in the books of the account servicer. An advice should be sent back to the account owner. |

## 6.2.3.45 PreferredContactMethod2Code

*Definition: Preferred method used to reach the individual contact within an organisation.*

*Type: CodeSet*

---

<!-- Page 422 -->

| CodeName | Name | Definition |
|---|---|---|
| MAIL | Email | Preferred method used to reach the contact is per email. |
| FAXX | Fax | Preferred method used to reach the contact is per fax. |
| LETT | Letter | Preferred method used to reach the contact is per letter. |
| CELL | MobileOrCellPhone | Preferred method used to reach the contact is per mobile or cell phone. |
| ONLI | Online | Preferred method used to reach the contact is online. |
| PHON | Phone | Preferred method used to reach the contact is per phone. |

## 6.2.3.46 Priority2Code

*Definition:* Specifies the priority level of an event.

*Type:* CodeSet

| CodeName | Name | Definition |
|---|---|---|
| HIGH | High | Priority level is high. |
| NORM | Normal | Priority level is normal. |

## 6.2.3.47 RegulatoryReportingType1Code

*Definition:* Identifies whether the regulatory reporting information applies to the debit side, to the credit side or to both debit and credit sides of the transaction.

*Type:* CodeSet

| CodeName | Name | Definition |
|---|---|---|
| CRED | Credit | Regulatory information applies to the credit side. |
| DEBT | Debit | Regulatory information applies to the debit side. |
| BOTH | Both | Regulatory information applies to both credit and debit sides. |

## 6.2.3.48 RemittanceLocationMethod2Code

*Definition:* Specifies the method used to deliver the remittance advice information.

*Type:* CodeSet

| CodeName | Name | Definition |
|---|---|---|
| FAXI | Fax | Remittance advice information must be faxed. |
| EDIC | ElectronicDataInterchange | Remittance advice information must be sent through Electronic Data Interchange (EDI). |

---

<!-- Page 423 -->

| CodeName | Name | Definition |
| :--- | :--- | :--- |
| URID | UniformResourceIdentifier | Remittance advice information needs to be sent to a Uniform Resource Identifier (URI). URI is a compact string of characters that uniquely identify an abstract or physical resource. URI's are the super-set of identifiers, such as URLs, email addresses, ftp sites, etc, and as such, provide the syntax for all of the identification schemes. |
| EMAL | EMail | Remittance advice information must be sent through e-mail. |
| POST | Post | Remittance advice information must be sent through postal services. |
| SMSM | SMS | Remittance advice information must be sent through by phone as a short message service (SMS). |

## 6.2.3.49 SequenceType3Code

*Definition: Specifies the type of the current transaction that belongs to a sequence of transactions.*

*Type: CodeSet*

| CodeName | Name | Definition |
| :--- | :--- | :--- |
| FRST | First | First collection of a series of direct debit instructions. |
| RCUR | Recurring | Direct debit instruction where the debtor's authorisation is used for regular direct debit transactions initiated by the creditor. |
| FINAL | Final | Final collection of a series of direct debit instructions. |
| OFF | OneOff | Direct debit instruction where the debtor's authorisation is used to initiate one single direct debit transaction. |
| RPRE | Represented | Collection used to re-present previously reversed or returned direct debit transactions. |

## 6.2.3.50 SettlementMethod1Code

*Definition: Specifies the method used to settle the credit transfer instruction.*

*Type: CodeSet*

| CodeName | Name | Definition |
| :--- | :--- | :--- |
| INDA | InstructedAgent | Settlement is done by the agent instructed to execute a payment instruction. |
| INGA | InstructingAgent | Settlement is done by the agent instructing and forwarding the payment to the next party in the payment chain. |

---

<!-- Page 424 -->

| CodeName | Name | Definition |
|---|---|---|
| COVE | CoverMethod | Settlement is done through a cover payment. |
| CLRG | ClearingSystem | Settlement is done through a payment clearing system. |

## 6.2.3.51 TaxRecordPeriod1Code

*Definition:* Specifies the period related to the tax payment.

*Type:* CodeSet

| CodeName | Name | Definition |
|---|---|---|
| MM01 | FirstMonth | Tax is related to the second month of the period. |
| MM02 | SecondMonth | Tax is related to the first month of the period. |
| MM03 | ThirdMonth | Tax is related to the third month of the period. |
| MM04 | FourthMonth | Tax is related to the fourth month of the period. |
| MM05 | FifthMonth | Tax is related to the fifth month of the period. |
| MM06 | SixthMonth | Tax is related to the sixth month of the period. |
| MM07 | SeventhMonth | Tax is related to the seventh month of the period. |
| MM08 | EighthMonth | Tax is related to the eighth month of the period. |
| MM09 | NinthMonth | Tax is related to the ninth month of the period. |
| MM10 | TenthMonth | Tax is related to the tenth month of the period. |
| MM11 | EleventhMonth | Tax is related to the eleventh month of the period. |
| MM12 | TwelfthMonth | Tax is related to the twelfth month of the period. |
| QTR1 | FirstQuarter | Tax is related to the first quarter of the period. |
| QTR2 | SecondQuarter | Tax is related to the second quarter of the period. |
| QTR3 | ThirdQuarter | Tax is related to the third quarter of the period. |
| QTR4 | FourthQuarter | Tax is related to the forth quarter of the period. |
| HLF1 | FirstHalf | Tax is related to the first half of the period. |
| HLF2 | SecondHalf | Tax is related to the second half of the period. |

---

<!-- Page 425 -->

## 6.2.4 Date

### 6.2.4.1 ISODate

*Definition:* A particular point in the progression of time in a calendar year expressed in the YYYY-MM-DD format. This representation is defined in "XML Schema Part 2: Datatypes Second Edition - W3C Recommendation 28 October 2004" which is aligned with ISO 8601.

*Type:* Date

## 6.2.5 DateTime

### 6.2.5.1 ISODateTime

*Definition:* A particular point in the progression of time defined by a mandatory date and a mandatory time component, expressed in either UTC time format (YYYY-MM-DDThh:mm:ss.sssZ), local time with UTC offset format (YYYY-MM-DDThh:mm:ss.sss+/-hh:mm), or local time format (YYYY-MM-DDThh:mm:ss.sss). These representations are defined in "XML Schema Part 2: Datatypes Second Edition - W3C Recommendation 28 October 2004" which is aligned with ISO 8601.

Note on the time format:

1) beginning / end of calendar day

00:00:00 = the beginning of a calendar day

24:00:00 = the end of a calendar day

2) fractions of second in time format

Decimal fractions of seconds may be included. In this case, the involved parties shall agree on the maximum number of digits that are allowed.

*Type:* Date Time

## 6.2.6 IdentifierSet

### 6.2.6.1 AnyBICDec2014Identifier

*Definition:* Code allocated to a financial or non-financial institution by the ISO 9362 Registration Authority, as described in ISO 9362: 2014 - "Banking - Banking telecommunication messages - Business identifier code (BIC)".

*Type:* IdentifierSet

*Identification scheme:* SWIFT; AnyBICIdentifier

**Format**

| pattern | [A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}[A-Z0-9]{3,3}{0,1} |
|---|---|

---

<!-- Page 426 -->

Constraints
* **AnyBIC**
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.

## 6.2.6.2 BICFIDec2014Identifier

*Definition:* Code allocated to a financial institution by the ISO 9362 Registration Authority as described in ISO 9362: 2014 - "Banking - Banking telecommunication messages - Business identifier code (BIC)".

*Type:* IdentifierSet

*Identification scheme:* SWIFT; BICIdentifier

**Format**

pattern
[A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}

**Constraints**
* **BICFI**
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous characters.

## 6.2.6.3 IBAN2007Identifier

*Definition:* The International Bank Account Number is a code used internationally by financial institutions to uniquely identify the account of a customer at a financial institution as described in the 2007 edition of the ISO 13616 standard "Banking and related financial services - International Bank Account Number (IBAN)" and replaced by the more recent edition of the standard.

*Type:* IdentifierSet

*Identification scheme:* National Banking Association; International Bank Account Number (ISO 13616)

**Format**

pattern
[A-Z]{2,2}[0-9]{2,2}[a-zA-Z0-9]{1,30}

**Constraints**
* **IBAN**
A valid IBAN consists of all three of the following components: Country Code, check digits and BBAN.

## 6.2.6.4 LEIIdentifier

*Definition:* Legal Entity Identifier is a code allocated to a party as described in ISO 17442 "Financial Services - Legal Entity Identifier (LEI)".

*Type:* IdentifierSet

*Identification scheme:* Global LEI System; LEIIdentifier

---

<!-- Page 427 -->

Format
pattern [A-Z0-9]{18,18}[0-9]{2,2}

## 6.2.6.5 UUIDv4Identifier

*Definition:* Universally Unique Identifier (UUID) version 4, as described in IETF RFC 4122 "Universally Unique Identifier (UUID) URN Namespace".

*Type:* IdentifierSet

*Identification scheme:* RFC4122; UUIDv4

**Format**
pattern [a-f0-9]{8}[a-f0-9]{4}[a-f0-9]{3}[89ab][a-f0-9]{3}-[a-f0-9]{12}

# 6.2.7 Indicator

## 6.2.7.1 BatchBookingIndicator

*Definition:* Identifies whether the sending party requests a single debit or credit entry per individual transaction or a batch entry for the sum of the amounts of all transactions.

*Type:* Indicator

*Meaning When True:* Identifies that a batch entry for the sum of the amounts of all transactions in the batch or message is requested.

*Meaning When False:* Identifies that a single entry for each of the transactions in the batch or message is requested.

## 6.2.7.2 TrueFalseIndicator

*Definition:* A flag indicating a True or False value.

*Type:* Indicator

*Meaning When True:* True

*Meaning When False:* False

# 6.2.8 Quantity

## 6.2.8.1 DecimalNumber

*Definition:* Number of objects represented as a decimal number, for example 0.75 or 45.6.

*Type:* Quantity

**Format**
totalDigits 18
fractionDigits 17

## 6.2.8.2 Number

*Definition:* Number of objects represented as an integer.

---

<!-- Page 428 -->

Type: Quantity

**Format**

| totalDigits | 18 |
| :--- | :--- |
| fractionDigits | 0 |

## 6.2.9 Rate

### 6.2.9.1 BaseOneRate

*Definition:* Rate expressed as a decimal, for example, 0.7 is 7/10 and 70%.

Type: Rate

**Format**

| totalDigits | 11 |
| :--- | :--- |
| fractionDigits | 10 |
| baseValue | 1.0 |

### 6.2.9.2 PercentageRate

*Definition:* Rate expressed as a percentage, that is, in hundredths, for example, 0.7 is 7/10 of a percent, and 7.0 is 7%.

Type: Rate

**Format**

| totalDigits | 11 |
| :--- | :--- |
| fractionDigits | 10 |
| baseValue | 100.0 |

## 6.2.10 Text

### 6.2.10.1 Exact2NumericText

*Definition:* Specifies a numeric string with an exact length of 2 digits.

Type: Text

**Format**

| pattern | [0-9]{2} |
| :--- | :--- |

### 6.2.10.2 Exact4AlphaNumericText

*Definition:* Specifies an alphanumeric string with a length of 4 characters.

Type: Text

---

<!-- Page 429 -->

Format

| pattern | [a-zA-Z0-9]{4} |
|---|---|

## 6.2.10.3 Max1025Text

*Definition:* Specifies a character string with a maximum length of 1025 characters.

*Type:* Text

**Format**

| minLength | 1 |
|---|---|
| maxLength | 1025 |

## 6.2.10.4 Max105Text

*Definition:* Specifies a character string with a maximum length of 105 characters.

*Type:* Text

**Format**

| minLength | 1 |
|---|---|
| maxLength | 105 |

## 6.2.10.5 Max10Text

*Definition:* Specifies a character string with a maximum length of 10 characters.

*Type:* Text

**Format**

| minLength | 1 |
|---|---|
| maxLength | 10 |

## 6.2.10.6 Max128Text

*Definition:* Specifies a character string with a maximum length of 128 characters.

*Type:* Text

**Format**

| minLength | 1 |
|---|---|
| maxLength | 128 |

## 6.2.10.7 Max140Text

*Definition:* Specifies a character string with a maximum length of 140 characters.

*Type:* Text

---

<!-- Page 430 -->

| Format | |
|---|---|
| minLength | 1 |
| maxLength | 140 |

## 6.2.10.8 Max15NumericText

*Definition:* Specifies a numeric string with a maximum length of 15 digits.

*Type:* Text

| Format | |
|---|---|
| pattern | [0-9]{1,15} |

## 6.2.10.9 Max16Text

*Definition:* Specifies a character string with a maximum length of 16 characters.

*Type:* Text

| Format | |
|---|---|
| minLength | 1 |
| maxLength | 16 |

## 6.2.10.10 Max2048Text

*Definition:* Specifies a character string with a maximum length of 2048 characters.

*Type:* Text

| Format | |
|---|---|
| minLength | 1 |
| maxLength | 2048 |

## 6.2.10.11 Max256Text

*Definition:* Specifies a character string with a maximum length of 256 characters.

*Type:* Text

| Format | |
|---|---|
| minLength | 1 |
| maxLength | 256 |

## 6.2.10.12 Max34Text

*Definition:* Specifies a character string with a maximum length of 34 characters.

*Type:* Text

---

<!-- Page 431 -->

| Format |
| :--- |
| minLength | 1 |
| maxLength | 34 |

## 6.2.10.13 Max350Text

*Definition:* Specifies a character string with a maximum length of 350 characters.
*Type:* Text

| Format |
| :--- |
| minLength | 1 |
| maxLength | 350 |

## 6.2.10.14 Max35Text

*Definition:* Specifies a character string with a maximum length of 35 characters.
*Type:* Text

| Format |
| :--- |
| minLength | 1 |
| maxLength | 35 |

## 6.2.10.15 Max4Text

*Definition:* Specifies a character string with a maximum length of 4 characters.
*Type:* Text

| Format |
| :--- |
| minLength | 1 |
| maxLength | 4 |

## 6.2.10.16 Max70Text

*Definition:* Specifies a character string with a maximum length of 70characters.
*Type:* Text

| Format |
| :--- |
| minLength | 1 |
| maxLength | 70 |

## 6.2.10.17 PhoneNumber

*Definition:* The collection of information which identifies a specific phone or FAX number as defined by telecom services.

---

<!-- Page 432 -->

It consists of a "+" followed by the country code (from 1 to 3 characters) then a "-" and finally, any combination of numbers, "(", ")", "+" and "-" (up to 30 characters).

*Type:* Text

**Format**

pattern

\+[0-9]{1,3}-[0-9\-\+\(\)]{1,30}

## 6.2.11 Year

### 6.2.11.1 ISOYear

*Definition:* Year represented by YYYY (ISO 8601).

*Type:* Year