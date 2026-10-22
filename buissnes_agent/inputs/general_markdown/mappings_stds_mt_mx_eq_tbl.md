<!-- Page 1 -->

# Standards

## MT and MX Equivalence Tables

This document provides a list of all MT messages together with the equivalent MX messages, where these exist. This document is for readers that wish to know the equivalences between MT and MX messages.

**08 May 2024**

---

<!-- Page 2 -->

# Table of Contents

| | |
|---|---|
| Table of Contents | 2 |
| Preface | 3 |
| 1 Category 1 – Customer Payments and Cheques | 4 |
| 2 Category 2 – Financial Institution Transfers | 5 |
| 3 Category 3 – FX, Money Markets, and Derivatives | 6 |
| 4 Category 4 – Collection and Cash Letters | 7 |
| 5 Category 5 – Securities Markets | 8 |
| 6 Category 6 – Commodities and Reference Data | 13 |
| 7 Category 7 – Documentary Credits and Guarantees/Standby Letters of Credit | 14 |
| 8 Category 8 – Travellers Cheques | 16 |
| 9 Category 9 – Cash Management and Customer Status | 17 |
| Legal Notices | 18 |

---

<!-- Page 3 -->

# Preface

**About this document**

This document provides a list of payments, securities, treasury, and trade MT messages together with the equivalent MX messages, where these exist.

**Note** The intention of this document is to identify the primary MX equivalent to an MT message. In many cases, there are secondary purpose MX messages, for example to amend, reject, or return an instruction or confirmation. These are fully described in the relevant message definition reports.

All the MX messages are not necessarily provisioned on Swift managed InterAct service such as FINplus or Swift funds service.

**Intended audience**

This document is for readers who wish to know the equivalences between MT and MX messages.

**Related documentation**

- **Standards MT Message Reference Guides**
- **Standards MX Message Definition Report and Schemas**

---

<!-- Page 4 -->

# 1 Category 1 – Customer Payments and Cheques

See the CBPR+ dedicated document for category 1, 2 & 9: https://www2.swift.com/mystandards/res/cbpr/CBPR_plus_MT_MX_equivalence.pdf

---

<!-- Page 5 -->

# 2 Category 2 – Financial Institution Transfers

See the CBPR+ dedicated document for category 1, 2 & 9: https://www2.swift.com/mystandards/res/cbpr/CBPR_plus_MT_MX_equivalence.pdf

---

<!-- Page 6 -->

# 3 Category 3 – FX, Money Markets, and Derivatives

| **MT Number** | **MT Name** | **MX ID** |
|---|---|---|
| MT 300 | Foreign Exchange Confirmation | fxtr.014 |
| MT 304 | Advice/Instruction of a Third Party Deal | None available |
| MT 305 | Foreign Currency Option Confirmation | None available |
| MT 306 | Foreign Currency Option Confirmation | None available |
| MT 320 | Fixed Loan/Deposit Confirmation | None available |
| MT 321 | Instruction to Settle a Third Party Loan/Deposit | None available |
| MT 330 | Call/Notice Loan/Deposit Confirmation | None available |
| MT 340 | Forward Rate Agreement Confirmation | None available |
| MT 341 | Forward Rate Agreement Settlement Confirmation | None available |
| MT 350 | Advice of Loan/Deposit Interest Payment | None available |
| MT 360 | Single Currency Interest Rate Derivative Confirmation | None available |
| MT 361 | Cross Currency Interest Rate Swap Confirmation | None available |
| MT 362 | Interest Rate Reset/Advice of Payment | None available |
| MT 364 | Single Currency Interest Rate Derivative Termination/Recouponing Confirmation | None available |
| MT 365 | Cross Currency Interest Rate Swap Termination/Recouponing Confirmation | None available |
| MT 370 | Netting Position Advice | None available |
| MT 380 | Foreign Exchange Order | None available |
| MT 381 | Foreign Exchange Order Confirmation | None available |
| **Common Group** | | |
| MT 390 | Advice of Charges, Interest and Other Adjustments | None available |
| MT 391 | Request for Payment of Charges, Interest and Other Expenses | None available |
| MT 392 | Request for Cancellation | None available |
| MT 395 | Queries | None available |
| MT 396 | Answers | None available |
| MT 398 | Proprietary Message | None available |
| MT 399 | Free Format Message | None available |

---

<!-- Page 7 -->

# 4 Category 4 – Collection and Cash Letters



| MT Number | MT Name | MX ID |
| :--- | :--- | :--- |
| **Collections** | | |
| MT 400 | Advice of Payment | None available |
| MT 410 | Acknowledgement | None available |
| MT 412 | Advice of Acceptance | None available |
| MT 416 | Advice of Non-Payment/Non-Acceptance | None available |
| MT 420 | Tracer | None available |
| MT 422 | Advice of Fate Request for Instructions | None available |
| MT 430 | Amendment of Instructions | None available |
| **Cash letters** | | |
| MT 450 | Cash Letter Credit Advice | None available |
| MT 455 | Cash Letter Credit Adjustment Advice | None available |
| MT 456 | Advice of Dishonour | None available |
| **Common Group** | | |
| MT 490 | Advice of Charges, Interest and Other Adjustments | None available |
| MT 491 | Request for Payment of Charges, Interest and Other Expenses | None available |
| MT 492 | Request for Cancellation | None available |
| MT 495 | Queries | None available |
| MT 496 | Answers | None available |
| MT 498 | Proprietary Message | None available |
| MT 499 | Free Format Message | None available |

---

<!-- Page 8 -->

# 5 Category 5 – Securities Markets

| MT Number | MT Name | MX ID | MX Name |
|---|---|---|---|
| MT 500 | Instruction to Register | None available | |
| MT 501 | Confirmation of Registration or Modification | None available | |
| MT 502 | Order to Buy or Sell (Funds Template) | setr.004 | RedemptionOrder |
| | | setr.005 | RedemptionOrderCancellationRequest |
| | | setr.010 | SubscriptionOrder |
| | | setr.011 | SubscriptionOrderCancellationRequest |
| | | setr.013 | SwitchOrder |
| | | setr.014 | SwitchOrderCancellationRequest |
| MT 502 | Order to Buy or Sell | None available | |
| MT 503 | Collateral Claim | colr.003 | MarginCallRequest |
| | | colr.005 | CollateralManagementCancellationRequest |
| MT 504 | Collateral Proposal | colr.005 | CollateralManagementCancellationRequest |
| | | colr.007 | CollateralProposal |
| MT 505 | Collateral Substitution | colr.005 | CollateralManagementCancellationRequest |
| | | colr.010 | CollateralSubstitutionRequest |
| MT 506 | Collateral and Exposure Statement | colr.016 | CollateralValuationReport |
| MT 507 | Collateral Status and Processing Advice | None available | |
| MT 508 | Intra-Position Advice | semt.015 | IntraPositionMovementConfirmation |
| | | semt.020 | SecuritiesMessageCancellationAdvice |
| MT 509 | Trade Status Message (Funds Template) | semt.016 | OrderInstructionStatusReport |
| | | setr.017 | OrderCancellationStatusReport |
| MT 509 | Trade Status Message | None available | |
| MT 510 | Registration Status and Processing Advice | None available | |
| MT 513 | Client Advice of Execution | None available | |
| MT 514 | Trade Allocation Instruction | None available | |
| MT 515 | Client Confirmation of Purchase or Sale (Funds Template) | setr.027 | SecuritiesTradeConfirmation |
| | | setr.006 | RedemptionOrderConfirmation |
| | | setr.012 | SubscriptionOrderConfirmation |

---

<!-- Page 9 -->

| MT Number | MT Name | MX ID | MX Name |
|---|---|---|---|
| MT 515 | Client Confirmation of Purchase or Sale | None available |  |
| MT 516 | Securities Loan Confirmation | None available |  |
| MT 517 | Trade Confirmation Affirmation | None available |  |
| MT 518 | Market-Side Securities Trade Confirmation | None available |  |
| MT 519 | Modification of Client Details | None available |  |
| MT 524 | Intra-Position Instruction | sent.013 | IntraPositionMovementInstruction |
|  |  | sese.020 | SecuritiesTransactionCancellationRequest |
| MT 526 | General Securities Lending/Borrowing Message | None available |  |
| MT 527 | Triparty Collateral Instruction | colr.019 | TripartyCollateralTransactionInstruction |
| MT 530 | Transaction Processing Command | sese.030 | SecuritiesSettlementConditionsModificationRequest |
| MT 535 | Statement of Holdings | sent.002 | SecuritiesBalanceCustodyReport.003 |
|  |  | sent.003 | SecuritiesBalanceAccountingReport.003 |
|  |  | sent.020 | SecuritiesMessageCancellationAdvice |
| MT 536 | Statement of Transactions | sent.017 | SecuritiesTransactionPostingReport |
|  |  | sent.020 | SecuritiesMessageCancellationAdvice |
| MT 537 | Statement of Pending Transactions | sent.018 | SecuritiesTransactionPendingReport |
|  |  | sent.020 | SecuritiesMessageCancellationAdvice |
| MT 538 | Statement of Intra-Position Advices | sent.016 | IntraPositionMovementPostingReport |
|  |  | sent.020 | SecuritiesMessageCancellationAdvice |
| MT 540 | Receive Free | sese.020 | SecuritiesTransactionCancellationRequest |
|  |  | sese.023 | SecuritiesSettlementTransactionInstruction |
|  |  | sese.032 | SecuritiesSettlementTransactionGenerationNotification |
|  |  | sese.033 | SecuritiesFinancingInstruction |
|  |  | sese.036 | SecuritiesFinancingModificationInstruction |
| MT 541 | Receive Against Payment | sese.020 | SecuritiesTransactionCancellationRequest |
|  |  | sese.023 | SecuritiesSettlementTransactionInstruction |
|  |  | sese.032 | SecuritiesSettlementTransactionGenerationNotification |
|  |  | sese.033 | SecuritiesFinancingInstruction |
|  |  | sese.036 | SecuritiesFinancingModificationInstruction |

---

<!-- Page 10 -->

| MT Number | MT Name | MX ID | MX Name |
|---|---|---|---|
| | | sese.023 | SecuritiesSettlementTransactionInstruction |
| | | sese.032 | SecuritiesSettlementTransactionGenerationNotification |
| | | sese.033 | SecuritiesFinancingInstruction |
| | | sese.036 | SecuritiesFinancingModificationInstruction |
| MT 543 | Deliver Against Payment | sese.020 | SecuritiesTransactionCancellationRequest |
| | | sese.023 | SecuritiesSettlementTransactionInstruction |
| | | sese.032 | SecuritiesSettlementTransactionGenerationNotification |
| | | sese.033 | SecuritiesFinancingInstruction |
| | | sese.036 | SecuritiesFinancingModificationInstruction |
| MT 544 | Receive Free Confirmation | semt.020 | SecuritiesMessageCancellationAdvice |
| | | sese.025 | SecuritiesSettlementTransactionConfirmation |
| | | sese.026 | SecuritiesSettlementTransactionReversalAdvice |
| | | sese.035 | SecuritiesFinancingConfirmation |
| MT 545 | Receive Against Payment Confirmation | semt.020 | SecuritiesMessageCancellationAdvice |
| | | sese.025 | SecuritiesSettlementTransactionConfirmation |
| | | sese.026 | SecuritiesSettlementTransactionReversalAdvice |
| | | sese.035 | SecuritiesFinancingConfirmation |
| MT 546 | Deliver Free Confirmation | semt.020 | SecuritiesMessageCancellationAdvice |
| | | sese.025 | SecuritiesSettlementTransactionConfirmation |
| | | sese.026 | SecuritiesSettlementTransactionReversalAdvice |
| | | sese.035 | SecuritiesFinancingConfirmation |
| MT 547 | Deliver Against Payment Confirmation | semt.020 | SecuritiesMessageCancellationAdvice |
| | | sese.025 | SecuritiesSettlementTransactionConfirmation |
| | | sese.026 | SecuritiesSettlementTransactionReversalAdvice |
| | | sese.035 | SecuritiesFinancingConfirmation |
| MT 548 | Settlement Status and Processing Advice | sese.022 | SecuritiesStatusOrStatementQueryStatusAdvice |
| | | sese.024 | SecuritiesSettlementTransactionStatusAdvice |
| | | sese.027 | SecuritiesTransactionCancellationRequestStatusAdvice |
| | | sese.031 | SecuritiesSettlementConditionModificationStatusAdvice |

---

<!-- Page 11 -->

| MT Number | MT Name | MX ID | MX Name |
|---|---|---|---|
| | | sese.034 | SecuritiesFinancingStatusAdvice |
| MT 549 | Request for Statement/Status Advice | semt.021 | SecuritiesStatementQuery |
| | | sese.021 | SecuritiesTransactionStatusQuery |
| | | coir.020 | TripartyCollateralTransactionInstructionProcessingAdvice |
| MT 558 | Triparty Collateral Status and Processing Advice | coir.021 | TripartyCollateralAlignmentNotification |
| | | coir.023 | TripartyCollateralStatusAdvice |
| | | coir.024 | TripartyCollateralAlignmentNotificationCancellationRequest |
| | | seev.031 | CorporateActionNotification |
| MT 564 | Corporate Action Notification | seev.035 | CorporateActionMovementPreliminaryAdvice |
| | | seev.039 | CorporateActionCancellationAdvice |
| | | seev.044 | CorporateActionMovementPreliminaryAdviceCancellationAdvice |
| MT 565 | Corporate Action Instruction | seev.033 | CorporateActionInstruction |
| | | seev.040 | CorporateActionInstructionCancellationRequest |
| MT 566 | Corporate Action Confirmation | seev.036 | CorporateActionMovementConfirmation |
| | | seev.037 | CorporateActionMovementReversalAdvice |
| MT 567 | Corporate Action Status and Processing Advice | seev.032 | CorporateActionEventProcessingStatusAdvice |
| | | sese.034 | CorporateActionInstructionStatusAdvice |
| | | seev.041 | CorporateActionInstructionCancellationRequestStatusAdvice |
| MT 568 with linked MT 564 | Corporate Action Narrative | seev.031 | CorporateActionNotification |
| MT 568 standalone | Corporate Action Narrative (for restricted business processes) | seev.038 | CorporateActionNarrative |
| MT 569 | Triparty Collateral and Exposure Statement | coir.022 | TripartyCollateralandExposureReport |
| MT 575 | Report of Combined Activity | None available | |
| MT 576 | Statement of Open Orders | None available | |
| MT 578 | Settlement Allegement | semt.020 | SecuritiesMessageCancellationAdvice |
| | | sese.028 | SecuritiesSettlementTransactionAllegementNotification |
| | | sese.029 | SecuritiesSettlementAllegementRemovalAdvice |
| MT 581 | Collateral Adjustment Message | None available | |
| MT 586 | Statement of Settlement Allegements | sese.037 | PortfolioTransferNotification |

---

<!-- Page 12 -->

| **MT Number** | **MT Name** | **MX ID** | **MX Name** |
|---|---|---|---|
| | | semt.020 | SecuritiesMessageCancellationAdvice |
| | | | |
| **Common Group** | | | |
| MT 590 | | None available | |
| MT 591 | Request for Payment of Charges, Interest & Other Expenses | None available | |
| MT 592 | Request for Cancellation | None available | |
| MT 595 | Queries | None available | |
| MT 596 | Answers | None available | |
| MT 598 | Proprietary Message | None available | |
| MT 599 | Free Format Message | None available | |

---

<!-- Page 13 -->

# 6 Category 6 – Commodities and Reference Data

| MT Number | MT Name | MX ID |
|---|---|---|
| **Commodities** | | |
| MT 600 | Commodity Trade Confirmation | None available |
| MT 601 | Commodity Option Confirmation | None available |
| MT 604 | Commodity Transfer/Delivery Order | None available |
| MT 605 | Commodity Notice to Receive | None available |
| MT 606 | Commodity Debit Advice | None available |
| MT 607 | Commodity Credit Advice | None available |
| MT 608 | Statement of a Commodity Account | None available |
| MT 620 | Commodity Fixed Loan/Deposit Confirmation | None available |
| **Reference Data** | | |
| MT 670 | Standing Settlement Instruction Update Notification Request | None available |
| MT 671 | Standing Settlement Instruction Update Notification | None available |
| **Common Group** | | |
| MT 690 | Advice of Charges, Interest and Other Adjustments | None available |
| MT 691 | Request for Payment of Charges, Interest and Other Expenses | None available |
| MT 692 | Request for Cancellation | None available |
| MT 695 | Queries | None available |
| MT 696 | Answers | None available |
| MT 698 | Proprietary Message | None available |
| MT 699 | Free Format Message | None available |

---

<!-- Page 14 -->

# 7 Category 7 – Documentary Credits and Guarantees/Standby Letters of Credit

| MT Number | MT Name | MX ID | MX Name |
|---|---|---|---|
| **Documentary Credits** | | | |
| MT 700 | Issue of a Documentary Credit | None available | |
| MT 701 | Issue of a Documentary Credit | None available | |
| MT 705 | Pre-Advice of a Documentary Credit | None available | |
| MT 707 | Amendment to a Documentary Credit | None available | |
| MT 708 | Amendment to a Documentary Credit | None available | |
| MT 710 | Advice of a Third Bank's or a Non-Bank's Documentary Credit | None available | |
| MT 711 | Advice of a Third Bank's or a Non-Bank's Documentary Credit | None available | |
| MT 720 | Transfer of a Documentary Credit | None available | |
| MT 721 | Transfer of a Documentary Credit | None available | |
| MT 730 | Acknowledgement | None available | |
| MT 734 | Advice of Refusal | None available | |
| **Common to Several Instruments** | | | |
| MT 732 | Advice of Discharge | None available | |
| MT 740 | Authorisation to Reimburse | None available | |
| MT 742 | Reimbursement Claim | None available | |
| MT 744 | Notice of Non-Conforming Reimbursement Claim | None available | |
| MT 747 | Amendment to an Authorisation to Reimburse | None available | |
| MT 750 | Advice of Discrepancy | None available | |
| MT 752 | Authorisation to Pay, Accept or Negotiate | None available | |
| MT 754 | Advice of Payment/Acceptance/Negotiation | None available | |
| MT 756 | Advice of Reimbursement or Payment | None available | |
| MT 759 | Ancillary Trade Structured Message | None available | |
| **Guarantees/Standby Letters of Credit** | | | |
| MT 760 | Issue of a Demand Guarantee/Standby Letter of Credit | Isvn.001 | UndertakingIssuance |

---

<!-- Page 15 -->

| MT Number | MT Name | MX ID | MX Name |
|---|---|---|---|
| MT 765 | Guarantee/Standby Letter of Credit Demand | None available |  |
| MT 767 | Amendment to a Demand Guarantee/Standby Letter of Credit | tsv.005 | UndertakingAmendment |
| MT 768 | Acknowledgement of a Guarantee/Standby Message | tsv.019 | UndertakingStatusReport |
| MT 769 | Advice of Reduction or Release | tsv.015 | ExtendOrPayResponse |
| MT 775 | Amendment to a Demand Guarantee/Standby Letter of Credit | None available |  |
| MT 785 | Guarantee/Standby Letter of Credit Non Extension Notification | None available |  |
| MT 786 | Guarantee/Standby Letter of Credit Demand Refusal | None available |  |
| MT 787 | Guarantee/Standby Letter of Credit Amendment Response | None available |  |
| **Common Group** |  |  |  |
| MT 790 | Advice of Charges, Interest and Other Adjustments | None available |  |
| MT 791 | Request for Payment of Charges, Interest and Other Expenses | None available |  |
| MT 792 | Request for Cancellation | None available |  |
| MT 795 | Queries | None available |  |
| MT 796 | Answers | None available |  |
| MT 798 | Proprietary Message | None available |  |
| MT 799 | Free Format Message | None available |  |

---

<!-- Page 16 -->

# 8 Category 8 – Travellers Cheques

| **MT Number** | **MT Name** | **MX ID** |
|---|---|---|
| MT 801 | T/C Multiple Sales Advice | None available |
| MT 802 | T/C Settlement Advice | None available |
| **Common Group** | | |
| MT 890 | Advice of Charges, Interest and Other Adjustments | None available |
| MT 891 | Request for Payment of Charges, Interest and Other Expenses | None available |
| MT 892 | Request for Cancellation | None available |
| MT 895 | Queries | None available |
| MT 896 | Answers | None available |
| MT 898 | Proprietary Message | None available |
| MT 899 | Free Format Message | None available |

---

<!-- Page 17 -->

# 9 Category 9 – Cash Management and Customer Status

See the CBPR+ dedicated document for category 1, 2 & 9: https://www2.swift.com/mystandards/res/cbpr/CBPR_plus_MT_MX_equivalence.pdf

---

<!-- Page 18 -->

# Legal Notices

**Copyright**

Swift ©2024. All rights reserved.

**Disclaimer**

The information in this publication may change from time to time. You must always refer to the latest available version.

**Swift Standards Intellectual Property Rights (IPR) Policy - End-User License Agreement**

Swift Standards are licensed subject to the terms and conditions of the Swift Standards IPR Policy - End-User License Agreement, available at www.swift.com > About Us > Legal > IPR Policies > Swift Standards IPR Policy.

**Translations**

The English version of Swift documentation is the only official and binding version.

**Trademarks**

Swift is the trade name of S.W.I.F.T. SC. The following are registered trademarks of Swift: 3SKey, Innovitbe, MyStandards, Sibos, Swift, SwiftNet, Swift Institute, the Standards Forum logo, the Swift logo, Swift GPI with logo, the Swift GPI logo, and UETR. Other product, service, or company names in this publication are trade names, trademarks, or registered trademarks of their respective owners.