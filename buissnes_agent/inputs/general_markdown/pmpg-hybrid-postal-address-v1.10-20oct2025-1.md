<!-- Page 1 -->

# Hybrid Postal Address

Payments Market Practice Group

October 2025
Version 1.10 (20.10.2025)

---

<!-- Page 2 -->

Payments Market Practice Group

# Disclaimer

The Payments Market Practice Group (PMPG) has used its best endeavours to make sure that all the English information, data, documentation and other material (copy and images) in this document are accurate and complete, it does not accept liability for any errors or omissions.

The PMPG, or any of its members, will not be liable for any claims or losses of any nature arising directly or indirectly from use of the information, data, documentation or other material in this document.

Links from this document to other sites are for information only. PMPG accepts no responsibility or liability arising from access to, or for the material on, any site to which it is linked, nor does the presence of links to other sites imply any endorsement by PMPG of these sites or their contents.

Reproduction, redistribution and transmission of any information, data or other material contained in this document is permitted, as long as its source is acknowledged.

Proceeding to read this document is confirmation that you have understood and accepted these terms.

---

<!-- Page 3 -->

# Document Change History

Payments Market Practice Group

| Version | Date | Description |
| :--- | :--- | :--- |
| Version 1.0 | 8th May 2024 | Initial version published. |
| Version 1.02 | 17th March 2025 | Included two new CBPR+ messages camt.105 and camt.106 into the scope of hybrid address. |
| Version 1.06 | 16th July 2025 | Added:<br>Page 40: Special use cases for the Town Name element<br>Page 41: Country mapping inventory for Structured Postal Address |
| Version 1.10 | 20th October 2025 | Slide 15: Updated for published FATF Recommendation 16<br>Slide 34-38, 40: Clarified handling of hybrid postal addresses where it is not supported post-Nov 2025<br>Generic references from "before Nov 2025" to "where hybrid is not supported" |

---

<!-- Page 4 -->

# Payments Market Practice Group

The Payments Market Practice Group (PMPG) is an independent body of payments subject matter experts from Asia Pacific, EMEA and the Americas.

The mission of the PMPG is to:

- Take stock of payments market practices across regions.
- Discuss, explain, and document market practice issues, including possible commercial impact.
- Recommend market practices, covering end-to-end transactions.
- Propose best practice, business responsibilities and rules, message flows, consistent implementation of ISO messaging standards and exception definitions.
- Ensure publication of recommended best practices.
- Recommend payments market practices in response to changing compliance requirements.

The PMPG provides a truly global forum to drive better market practices, which, together with correct use of standards, will help in achieving full straight-through-processing and improved customer service.

Follow us on
LinkedIn

---

<!-- Page 5 -->

# Management Summary

Payments Market Practice Group

Structured customer addresses help to streamline the **processing, monitoring and screening** of payments along the entire value chain thanks to the standardized format that enhances **automated recognition**, thus reducing errors and enabling efficient data extraction due to **unambiguous data qualifiers**.

A new **hybrid postal address** option will be introduced as of **November 2025 (SR 2025)** in Swift and leading Payment Market Infrastructures (PMIs). The hybrid address allows **simultaneous usage** of structured and unstructured elements, with a minimum of structured Town Name and Country.

**Timelines:**

- **Fully structured:** already allowed today and preferred & recommended option in the future
- **Fully unstructured:** Only allowed until November 2026
- **Hybrid address:** Allowed as of November 2025* (no end-date)

## Hybrid address example

```xml
<Cdtr>
  <Nm>JOHN SMITH</Nm>
  <PstlAdr>
    <PstCd>1000</PstCd>
    <TwnNm>BRUSSELS</TwnNm>
    <Ctry>BE</Ctry>
    <AdrLine>HOOGSTRAAT 6, 18TH FLOOR...</AdrLine>
  </PstlAdr>
</Cdtr>
```

| Phase | 2025 | 2026 | 2027 onwards |
|---|---|---|---|
| MT / MX coexistence for payments messages | ◆ November 2025 | | |
| Grace period for fully unstructured addresses | | ◆ November 2026 | |
| Only fully structured or hybrid addresses allowed | | | |

- **Fully structured**
- **Fully unstructured**
- **Hybrid**

---

<!-- Page 6 -->

# Contents

1 Background → 2 Regulatory Drivers → 3 Impact → 4 Roadmap → 5 Guidelines

---

<!-- Page 7 -->

# 1

# Background

More structured & granular debtor & creditor data in ISO 20022 messages offers more precise filtering, improved monitoring and higher automation in the processing of payments

1. **Background**
2. Regulatory Drivers
3. Impact
4. Roadmap
5. Guidelines

---

<!-- Page 8 -->

# 1. Background - Why structured addresses.

Payments Market Practice Group

As the Payments industry is in the process of adopting ISO 20022, the full power of richer and more structured data is still to be unlocked. Structured payments in ISO 20022 messages offer several advantages in terms of providing more precise and more detailed information in payment transactions. However, due to the nuanced challenges inherent in cleansing address data within systems and databases, the proportion of structured customer data in payment messages is still at a relatively low level.

The Payments Market Practice Group (PMPG) has been, and continues, supporting the payments industry in the migration towards structured party addresses. Complete, structured and rich data in payments messages is an integrated part of our ISO 20022 adoption and helps to reduce friction in cross-border payments.

Structured customer addresses help to streamline the processing of payments along the entire value chain thanks to the standardized format that enhances automated recognition, thus reducing errors and enabling efficient data extraction.

- **Financial Crime Compliance:** Reduction in false hits in sanctions screening & more efficient AML monitoring
- **Payment processing:** More precise Creditor name matching
- **FATF rec. 16 monitoring:** Improved monitoring of completeness of required debtor and creditor information
- **Client reporting:** Provide better data quality of reporting towards their creditor
- **Improved interoperability:** Reduce friction for cross-border (instant) payments with aligned party addresses as defined by IP+, CBPR+ and HVPS+ guidelines

In the complex landscape of payments screening, inefficiencies act as silent barriers to payment integrity - addressing

---

<!-- Page 9 -->

# 1. Background - What are structured addresses?

Structured address data refers to a standardized and organized format for representing location information, typically comprising distinct components, such as street name, post code, town and country details. The structured postal address definition in ISO 20222 offers 14 specific attributes, where it is clearly visible what element includes which data. Besides the structured elements, ISO 20222 also provides an unstructured field "Address Line". The structured elements and "Address Line" must not be used together in payments messages in the inter-bank space before November 22ⁿᵈ, 2025 as they are mutually exclusive.

**Fully Unstructured** postal address

```xml
<Cdtr>
    <Nm>JOHN SMITH</Nm>
    <PstlAdr>
        <AdrLine> HOOGSTRAAT 6, PREMIUM</AdrLine>
        <AdrLine> TOWER, 18TH FLOOR</AdrLine>
        <AdrLine>1000 BRUSSELS, BELGIUM</AdrLine>
    </PstlAdr>
</Cdtr>
```

**Fully Structured** postal address

```xml
<Cdtr>
    <Nm>John Smith</Nm>
    <PstlAdr>
        <StrtNm>Hoogstraat</StrtNm>
        <BldgNb>6</BldgNb>
        <BldgNm>Premium Tower</BldgNm>
        <Flr>18</Flr>
        <PstCd>1000</PstCd>
        <TwnNm>Brussels</TwnNm>
        <Ctry>BE</Ctry>
    </PstlAdr>
</Cdtr>
```

| Name | Department | Sub Department | Street Name | Building Number |
|---|---|---|---|---|
| Building Name | Floor | Post Box | Room | Post Code |

---

<!-- Page 10 -->

# 1. Background - The challenge

Payments Market Practice Group

Based on the recent market engagement and consultation with leading industry groups such as CGI (Common Global Implementation), the PMPG identified a fundamental impediment that may put the migration towards structured customer addresses until November 2025 at risk.

The fully structured postal address format does not allow to co-mingle different data elements into one structured element. The reality shows that many corporates and financial institutions maintain the address data elements of their customers in an unstructured database. In a typical customer data record, the "last mile of the address" consists of various address attributes in a single data field, which fits the industry's current needs, such as the use as a delivery address or as a free format field in FIN MT

Elements like name, town name and country are segregated in most systems and can be easily mapped to the respective ISO 20022 structured format. However, the current CBPR+ and HVPS+ Usage Guidelines do not allow the use of a mix between structured and unstructured postal address elements for the identification of a party. Therefore, a migration to structured addresses has so far been an "all-or-nothing" approach.

**Typical customer address inventory**

| Field | Value | Mapped to |
|---|---|---|
| Name | Mr. JOHN SMITH | `<Nm><John Smith></Nm>` |
| Address | HOOGSTRAAT 6, PREMIUM TOWER, 18TH FLOOR | `<StrtNm><Hoogstraat></StrtNm>` |
| | | `<BldgNb><6</BldgNb>` |
| | | `<BldgNm><Premium Tower</BldgNm>` |
| Postal Code | 1000 | `<PstCd><1000</PstCd>` |
| Town Name | BRUSSELS | `<TwnNm><Brussels</TwnNm>` |
| Country | BE Belgium | `<Ctry><BE</Ctry>` |

**Mapping to fully structured ISO 2022 address**

```
<Cdtr>
  <Nm><John Smith></Nm>
  <PstlAdr>
    <StrtNm><Hoogstraat></StrtNm>
    <BldgNb><6</BldgNb>
    <BldgNm><Premium Tower</BldgNm>
    <PstCd><1000</PstCd>
    <TwnNm><Brussels</TwnNm>
    <Ctry><BE</Ctry>
  </PstlAdr>
```

---

*Risks of enforced migration to fully structured addresses:*

✂ **Data loss**

Stakeholders could **eliminate** secondary address attributes that are not available fully structured

🏺 **Data pollution**

Stakeholders could **co-mingle** various address attributes in incorrect address elements

Misusing and undermining the value of ISO 20022

Decreased level of information triggering friction & human intervention

---

<!-- Page 11 -->

# 1. Background - Hybrid postal address

Considering the industry challenges, involved costs and in order to facilitate the migration towards structured addresses in ISO 20022 payment messages, the PMPG has come forward with a Change Request ("CR") to introduce a new **hybrid** (semi-structured) postal address option across CBPR+ usage guidelines for all parties and agents. The CR has been approved and will become effective as of **November 2025** (SR2025).

## Definition & Rules

The hybrid address will allow **simultaneous usage** of structured elements within PostalAddress and the unstructured "AddressLine" element.

**TownName** and **Country** are mandatory elements within the PostalAddress when a hybrid address is used, just as they are when a fully structured address is used.

The unstructured AddressLine element within the hybrid address can be **up to 2 lines of 70 characters (2*70)**.

The structured address information provided in the respective structured elements must **not be repeated** in the AddressLine elements.

## Example

```xml
<Cdtr>
  <Nm>JOHN SMITH</Nm>
  <PstlAdr>
    <PstCd>1000</PstCd>
    <TwnNm>BRUSSELS</TwnNm>
    <Ctry>BE</Ctry>
    <AdrLine>HOOGSTRAAT 6, 18th floor</AdrLine>
  </PstlAdr>
</Cdtr>
```

| Name | Department | Sub Department | Street Name |
|---|---|---|---|
| Building Number | Building Name | Floor | Post Box |
| Room | Post Code | Town name | Town Location Name |
| District Name | Country Subdivision | Country | AddressLine |

The hybrid address is a good industry compromise that limits the effort for implementation, whilst ensuring the original goal of increased data quality in the more structured and data-rich

---

<!-- Page 12 -->

# 1. Background – Scope of Hybrid address

## Impacted pacs message types:

| Message type | Description |
|---|---|
| pacs.008 | FI-to-FI Customer Credit Transfer |
| pacs.008 (stp) | FI-to-FI Customer Credit Transfer 'STP' |
| pacs.009 (core) | Financial Institution Credit Transfer |
| pacs.009 (cov) | Cover Financial Institution Credit Transfer 'Cover' |
| pacs.009 (adv) | Advice Financial Institution Credit Transfer 'Advice' |
| pacs.002 | FI-to-FI Payment Status Report |
| pacs.003 | FI-to-FI Customer Direct Debit |
| pacs.004 | Payment Return |
| pacs.010 | Interbank Direct Debit |

## Impacted pain & camt message types:

| Message type | Description |
|---|---|
| pain.001 (relay) | Customer-to-Bank 'Relay' Credit Transfer |
| pain.002 | Customer Payment Status Report |
| pain.008 | Customer Direct Debit Initiation |
| camt.029 | Resolution of Investigation |
| camt.055 | Customer Payment Cancellation Request |
| camt.056 | FI-to-FI Payment Cancellation Request |
| camt.057 | Notification to Receive |
| camt.058 | Notification to Receive Cancellation Advice |
| camt.060 | Account Reporting Request |
| camt.105 | Charges Payment Notification |
| camt.106 | Charges Payment Request |
| camt.107 | Cheque Presentation Notification |
| camt.108 | Cheque Presentation Cancellation Request |
| camt.109 | Cheque Presentation Cancellation Status Report |

## Impacted ISO 20022 elements

| ISO 20022 element | Type (party or agent) | Structured only structured elements | Fully unstructured only AdrLine elements | Hybrid Mix of structured elements with minimum structured TownName & Country and up to 2 x 70 char AdrLine |
|---|---|---|---|---|
| Previous Instructing Agent 1 | Agent | Preferred | To be decommissioned by NOV/26 | Allowed from NOV25 onwards |
| Previous Instructing Agent 2 | Agent | Preferred | To be decommissioned by NOV/26 | Allowed from NOV25 onwards |
| Previous Instructing Agent 3 | Agent | Preferred | To be decommissioned by NOV/26 | Allowed from NOV25 onwards |
| Intermediary Agent 1 | Agent | Preferred | To be decommissioned by NOV/26 | Allowed from NOV25 onwards |
| Intermediary Agent 2 | Agent | Preferred | To be decommissioned by NOV/26 | Allowed from NOV25 onwards |
| Intermediary Agent 3 | Agent | Preferred | To be decommissioned by NOV/26 | Allowed from NOV25 onwards |
| Ultimate Debtor | Party | Preferred | Not allowed (new element) | Allowed from NOV25 onwards |
| Initiating Party | Party | Preferred | Not allowed (new element) | Allowed from NOV25 onwards |
| Debtor | Party | Preferred | To be decommissioned by NOV/26 | Allowed from NOV25 onwards |
| Debtor Agent | Agent | Preferred | To be decommissioned by NOV/26 | Allowed from NOV25 onwards |
| Creditor Agent | Agent | Preferred | To be decommissioned by NOV/26 | Allowed from NOV25 onwards |
| Creditor | Party | Preferred | To be decommissioned by NOV/26 | Allowed from NOV25 onwards |

---

<!-- Page 13 -->

# 2 Regulatory Drivers

1 Background → **2 Regulatory Drivers** → 3 Impact → 4 Roadmap → 5 Guidelines

---

<!-- Page 14 -->

# 2. Regulatory Drivers - Overview

Payments Market Practice Group

## Regulatory Bodies

| Regulatory Body | Description |
|---|---|
| **FATF** — FINANCIAL ACTION TASK FORCE | Revision of **FATF Rec.16** |
| **BIS** | CPMI harmonised ISO 20022 data requirements for enhancing cross-border payments (G20) |
| **the Wolfsberg Group** | Updated Payments Transparency Principles |

## Local legislation & central banks policies

- Bank of England
- $ EU Reg. 847
- EUROPEAN CENTRAL BANK
- US Travel Rules
- Hong Kong Monetary Authority
- MAS — Monetary Authority of Singapore
- Etc...

## Impacted stakeholders

- Financial Institutions
- Payment Market Infrastructures
- Software providers
- Corporate Clients
- Non-traditional PSP's

| Organisation | Description |
|---|---|
| **Swift** | |
| **HVPS+** — HIGH-VALUE PAYMENTS SYSTEMS | High-Value Payments Systems guidelines |
| **PMPG** — Payments Market Practice Group | |
| **CBPR+** | Cross-Border Payments & Reporting guidelines |

---

<!-- Page 15 -->

# 2. Regulatory Drivers > FATF Recommendation 16

Payments Market Practice Group

**FATF**
FINANCIAL ACTION TASK FORCE

**Revised recommendation 16**
*Full implementation expected by 2030*

> **Note: Implementation guidance is still under development**

**Requirement for cross-border payments above threshold (>EUR/USD 1,000):**

*   Name + address (originator)
*   Name + town name & country (beneficiary)
*   Account number or unique reference
*   Legal person: LEI, BIC, or official ID (if available)
*   Natural person: Date of birth (DOB)

**Principles & Flexibility:**

*   Use structured data where possible (ISO 20022 compatible)
*   For beneficiary address, FATF requires only town name and country
*   Allow fallback IDs or year if full DOB unavailable

**FATF Rec. 16 enhances transparency and trust in cross-border payments through structured, reliable originator and beneficiary data**

---

<!-- Page 16 -->

# 2. Regulatory Drivers - G20 / BIS / CPMI

Payments Market Practice Group

## BIS

CPMI – Committee for Payments & Market Infrastructures
Harmonised ISO 20222 data requirements for enhancing cross-border payments

**Published in October 2023**
https://www.bis.org/cpmi/publ/d218.htm

> The G20 has made faster, cheaper, more transparent and more inclusive cross-border payments a priority and has set targets to achieve this by

- Requirement #9 – To identify all **entities** involved in a cross-border payment in a standardized and structured way
- Requirement #10 – To identify all **persons** involved in a cross-border payment in a standardized and structured way
- Requirement #11 – To provide a **common minimum level** of postal address information **structured** to the extent possible

### Solution

Provide the name and a minimum of key postal address attributes such as Country and Town Name, using the **appropriate and explicit structured message elements** (see Annex 2 and 3 for minimum data requirement for postal address information). For entities, e.g. corporations, the Name and Postal Address

### Link to G20 targets

The use of structured addresses will **speed up** overall processing of cross-border payments, especially where it will facilitate **screening** processes and **prevent the need for manual interventions** (e.g. for sanctions checks), in turn **reducing costs** through enhanced straight through processing (STP). Furthermore, it will provide increased **transparency** about the parties involved in the cross-border payment.

---

<!-- Page 17 -->

# 2. Regulatory Drivers - The Wolfsberg Group

Payments Market Practice Group

## the Wolfsberg Group

Updated Wolfsberg Payment Transparency Standards

Published in October 2023
https://wolfsberg-group.org/news/50

Ensuring minimum levels of transparency and providing clarity about where these responsibilities lie to all payment service providers.

[...]

Address information **should be sufficient** to identify clearly the location of the party/parties for sanctions screening and AML/CTF monitoring. It should **include country and other aspects of address** in accordance with the resident country conventions such as city, state/province/municipality, street name, building number and building name, and postal code.

Having only a post office (P.O.) box as an address should be avoided except where no alternative exists due to market practices/limitations and is supported by local regulations.

Address should be **fully structured**, when possible, and at a minimum employ a **hybrid structure** (structured town and country name, but potentially unstructured for street name, building number, etc. due to local naming conventions).

[...]

---

<!-- Page 18 -->

# 3 Impact

Various stakeholder groups will need to contribute their part to ensure provision and adequate handling & interpretation of hybrid addresses

1 Background — 2 Regulatory Drivers — **3 Impact** — 4 Roadmap — 5 Guidelines

---

<!-- Page 19 -->

# 5. Impact - Overview

Financial Institutions
Payment Market Infrastructures
Impacted stakeholders
Non-traditional PSP's
ERP / TMS Software providers
Corporate clients

The **key success factor** for a global migration to structured customer data in payments is that **all actors are aware of their responsibilities and take the required steps to comply with these requirements.**

As high quality data can only be guaranteed at the "source of the information", it must be **sourced at the origin** of a payment transaction to avoid labor and cost-intensive repair to structure data for subsequent processing.

This underlines the crucial role of the originating parties, i.e., the Debtor and Debtor Agent of a payment:

* The **Debtor** is responsible for the provision of high-quality (structured) information of the Creditor and Ultimate Parties (Ultimate Debtor & Ultimate Creditor). It also has a responsibility for ensuring all required information on Creditor is included.
* The **Debtor Agent** is responsible for delivering the required, accurate and structured customer data of the debtor.

But the journey doesn't end here...

High-quality data will only be as good as the surrounding processes that are consuming the rich data. Systems involved in the validation, processing, screening and monitoring of payments need to be enhanced to embrace the additional data structure. There will be a paradigm shift from interpreting free-text information towards a future to where it is possible to make sense of unambiguous data.

---

<!-- Page 20 -->

# 6. Impact > Financial Institutions

## Financial Institutions

Financial Institutions (FIs) play a pivotal role - not only as payment processing agents, but they also carry the responsibility to proactively educate and guide their clients on adhering to the prescribed target address format.

The degree of impact and obligation differs based on one's position within the payment chain, with the Debtor Agent bearing the most significant responsibility.

**Key responsibilities :**

**Clear Communication and Planning:**
- Engage in transparent communication with clients regarding the migration plan.

**Client Data Collection and Validation:**
- Request Debtors to provide essential details of the counterparty (be it Creditor, Ultimate Debtor, or Ultimate Creditor), including at least the country and town name in a structured format, irrespective of the initiation channel.
- Equip clients with updated payment specifications and interfaces that mandate the inclusion of minimum address data in the prescribed format.
- Scrutinize and validate customer-entered data for accuracy, ensuring alignment, if required, with the ISO 20022 data structure.
- Maintain client static data in an organized format, emphasizing the inclusion of at least the country and town name.

**Process Adaptation and Optimization:**
- Modify mapping procedures to consistently present Debtor information in outgoing payments in either a fully structured or hybrid format.
- Ensure seamless transmission of Beneficiary/Creditor details to subsequent Parties in the payment chain without alterations.
- Refine processing, screening, and monitoring mechanisms to harness the full potential of structured customer

**Key deliverables:**

- **Customer Education:** Inform both customers and vendors about upcoming requirements, associated timelines, and repercussions of non-compliance with payment standards.
- **Customer Testing Support:** Coordinate and oversee customer testing across all payment initiation channels to ensure seamless integration.
- **Data Quality Assurance:** Uphold stringent standards for data accuracy and completeness at payment initiation , encompassing front-end interfaces and client channels.
- **Data Format Alignment:** Verify and align customer data to conform with the specified target format (fully structured or hybrid).
- **Implementation Readiness:** Allocate adequate time and resources for the seamless integration of necessary system modifications, including channel enhancements, validation tools, formatting guidelines and updates to general terms and conditions.

By prioritizing the dialogue with clients and emphasizing the importance of structured address data, financial institutions can pave the way for a

---

<!-- Page 21 -->

# 6. Impact - Payment Service Providers

## Payment Service Providers (PSPs)

Technological advances and efforts by Regulators to increase competition has seen the emergence of non-bank Payment Service Providers (PSPs) particularly in the retail (P2P) payments space. As such, they play a significant role in the end-to-end payment chain.

Some PSPs operate in a closed-loop system using proprietary formats. These are outside of the scope of this discussion. Other PSPs are direct participants of PMIs with a number recently connecting to Swift. These PSPs have a role similar to Financial Institutions, thus the requirements of FIs would also apply to these entities.

Many PSPs have indirect participation to the PMI through the services of an Agent Bank and play a critical role as they are accountable for the data quality from the debtor client.

**Key responsibilities:**

**Engagement with their Agent Bank:**
- To understand the Agent Bank's requirements in order to meet PMI usage guidelines, payment screening and regulatory reporting obligations

**Client Data Collection and Validation:**
- Educate and require Debtor clients to provide complete details of all parties/agents in the chain, including a minimum of town name and country name in a structured format.
- Where feasible, provide Debtors with an address look-up functionality to minimise manual data input.
- Where there are client inputs, validate these for accuracy, ensuring alignment with the ISO 20022 data structure.
- Maintain client static data in ISO structure as much as possible, recording town name and country.

**Update of processes:**

**Key deliverables:**

* **Agent Bank Engagement:** work collaboratively with Agent Banks to ensure message instructions meet their requirements for them to comply with PMI usage guidelines, regulatory requirements and those of any downstream Correspondents.
* **Client Engagement:** Educate clients on requirements, associated timelines, and consequences of non-compliance with payment data standards.
* **Data Quality:** Ensure high standards for data accuracy and completeness at client payment initiation. Validate and structure customer inputs of data to conform with either fully structured or hybrid models. Where possible, minimise client manual data input by providing address look-up software or reference files.
* **Implementation:** Ensure sufficient time to updated all impacted systems, business process, and data records as well as for the training of staff.

Active dialogue with Agent Banks and Debtor clients is key to ensuring required data in structured format is provided to ensure seamless end-to-end processing.

---

<!-- Page 22 -->

# 6. Impact > Payment Market Infrastructures

Payments Market Practice Group

## Payment Market Infrastructures

To foster seamless operations, Payment Market Infrastructures (PMIs) should facilitate the exchange of payments in the ISO 20022 target format (or its equivalent). Recognizing their pivotal role as catalysts for change and compliance in the global economy, PMIs must also promote market preparedness beyond local payment processing.

**Key Responsibilities:**

**Format Enablement:**

- Ensure the adoption of the ISO 20022 target format (or its equivalent), aligning with CBPR+ and HVPS+ standards.
- Revise current standards and publish the updated Usage Guidelines.
- Deploy the new standard/Usage Guideline in a timely manner to avoid friction in cross-border payments.

**Data Accuracy & Testing Support:**

- Deploy network validation mechanisms to verify data accuracy, ensuring alignment with the target format.
- Encourage and facilitate testing for both target formats — fully structured and hybrid — by offering dedicated testing and validation portals.

**Advocacy and Progress Monitoring:**

- Advocate completion of the adoption of structured party data that complies with the target format by November 2026.
- Provide regular updates and dedicated reports on industry's progress of the compliance.

Payment Market Infrastructures are encouraged to consider adherence to the High-Value Payments Plus (HVPS+) Harmonization Charter. The HVPS+ Group maintains a set of HVPS+ message Usage Guidelines which acts as template for MIs to base their own message collection on to achieve interoperability and harmonization.

**Key deliverables:**

- **Collaboration and Alignment:** Engage with market to develop a roadmap aligned with CBPR+ and HVPS+ standards.
- **Communication:** Clearly and proactively communicate requirements and timelines to all affected stakeholders, including 3rd party vendors.
- **Updated Usage Guidelines/Standards:** Amend, publish and implement Usage Guidelines/equivalent standards.
- **Testing Support:** Enable, coordinate and oversee industry testing to ensure seamless migration.
- **Community Progress:** Monitor and report on the usage of the different address options

By outlining these responsibilities and addressing potential challenges, the adoption of structured data can be effectively promoted, ensuring a smooth transition and enhanced data management within the financial ecosystem.

---

<!-- Page 23 -->

# 6. Impact > Corporate Clients

## Corporate clients

| | |
|---|---|
| Whilst the Debtor Agent data is the responsibility of the FI, corporates and individual payment originators are responsible for sourcing the Creditor data in the required format. FIs need to ensure that channels can support the MX address formats for all parties in the payment.<br><br>Whilst address data is a hot topic for banks, end users need to be educated about the new address formats. FIs should have a dialogue with payment originators on how to uplift the name and address data in any preformats that the FI supports via its channels. Special attention should be given to legacy file and message formats.<br><br>While the pain.001 V9 supports the structured and hybrid address data, older versions or non-ISO based file format might be a challenge. FIs should analyze the data structure and quality of the address data provided by corporate customers (file and MT 101) and discuss if these need to be upgraded. If payment initiation continues via MT101, a mutually-agreed mapping rule will need to be deployed.<br><br>Third-party tools should be considered to enrich Creditor data if the source format in the customer's ERP system cannot be fixed. Use of the LEI and populating the name and address fields for Creditor and Ultimate Parties via the GLEIF database could be another option, depending on the industry.<br><br>FIs offering multibank payment initiation services will need to review not only the impact of any data mapping or enrichment to their own systems, but also how it impact other banks receiving the pain.001 in a relay mode. Testing might not just be required with internal payment processes, but also with downstream banks.<br><br>Lastly, API channels will need to be reviewed and upgraded and tested with corporate customers. Pre-validation APIs that also perform address data validation should be considered. | **Key points to cover:**<br>• Liaise with house bank(s) on roadmap and formatting requirements<br>• Analyze data quality of Creditor and Ultimates in database & payments. For records that do not include Town Name and Country, prioritize collecting this information.<br>• Ensure that minimum structured data elements are mapped into pain.001<br>• If not using pain.001, review legacy payment format and discuss with house bank(s) if a format upgrade is required.<br>• Provide a tool and strategy to migrate pre-formats stored on the bank's EB platform to the new format<br>• Review multi-banking, third-party tools<br>• Consider moving from MT 101 to pain.001 SCORE<br>• Avoid over-population of ISO 20022 fields<br>• If the exact sub-element is not known, use the hybrid format and put it in the unstructured address line (AdrLine)<br>• Do not duplicate structured data elements in the unstructured data elements |

Early customer engagement in the address format discussion and planning in sufficient time for

---

<!-- Page 24 -->

# 6. Impact - ERP / TSM Software Providers

## ERP / TSM¹ Software Providers

ERP and TSM vendors have created tools to support different address formats, but, as these are optional and require set-up, corporate customers might have opted to implement a simplified address format that captures country (ISO 2-letter code) and town in a structured manner and stores any other address component in two or more free format lines of text.

As with corporate customers, it will be important for FIs to engage with the ERP and TSM vendor community to provide education and discuss a pathway on how legacy address formats can be uplifted to a more structured version.

This also presents an opportunity to build out the Swift pre-validation service to check address data quality or even provide a centralized enrichment service.

→ https://www.placekey.io/blog/address-matching

→ https://www.placekey.io/blog/address-matching-python

→ https://www.codeproject.com/Articles/1096978/Smart-TextDiff-Utility-for-Intel-i-Platform

### Key points to cover:

- Engage with FI's and end clients on roadmap
- Offer validation portals for fully structured and hybrid address
- Roadmap, timing
- Review with ERP/TSM provider what their plan is to support the new data requirements for cross-border payments
- Which versions of the software can support the new format?

Address data validation and structuring is as a critical part of a corporate data management strategy.

---

<!-- Page 25 -->

# 4 Roadmap

Whilst the hybrid address will go live as of NOV25, the fully unstructured addresses will be sun-set as of NOV26

| 1 | 2 | 3 | 4 | 5 |
|---|---|---|---|---|
| Background | Regulatory Drivers | Impact | **Roadmap** | Guidelines |

---

<!-- Page 26 -->

# 4. Roadmap

Payments Market Practice Group

| | 2023 | 2024 | 2025 | 2026 | 2027+ |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Preferred** | | | | | |
| **Fully structured** | **Fully structured** Postal Address can be used already today (preferred format) | | | | |
| **Fully unstructured** | Migration to fully structured or hybrid Postal Address | | | End of «Fully unstructured» | Fully unstructured addresses to be **rejected** by Swift and local RTGS systems |
| **New** | | | | | |
| **Hybrid** | Approval of CR0942 (hybrid) | Preparation for hybrid Postal Address | Go-live «Hybrid» **Hybrid Postal Address can be used** | | |

**MT / MX coexistence for payments messages**

End of MT/MX coexistence

**Grace period for fully unstructured addresses**

**Only fully structured or hybrid addresses allowed**

November 2025

November 2026

*   **No end-date** for hybrid address option
*   **Go-live** of hybrid option *must happen at the same time* in Swift MX (CBPR+) and local RTGS systems (HVPS+)
*   **The decommissioning** of fully unstructured addresses *must happen at the same time* in Swift MX (CBPR+) and local RTGS systems (HVPS+)
*   Proposed changes apply for all **payments MX message types** containing a Postal Address (pac.008/009/004, pain.001 relay)
*   Proposed changes apply for **all elements** in these message types with Postal Address (debtor, creditor, ultimates* and agents*)
    * *Exception: for the elements ‘ultimate debtor’, ‘ultimate creditor’ & ‘initiating party’, the fully unstructured option will not be allowed*

---

<!-- Page 27 -->

# 5 Guidelines

1. Background
2. Regulatory Drivers
3. Impact
4. Roadmap
5. **Guidelines**

---

<!-- Page 28 -->

# 6. Mapping principles

Payments Market Practice Group

**Mapping scheme 1** **Hybrid address from MX to MT** > **Summary**

Despite the global adoption of ISO 20022 in payments, there are still market infrastructures that will operate on legacy systems based on Swift FIN messages for a given period beyond the sunseting of MT 103 & MT 202 as of November 2025 for cross-border payments.

When these institutions need to interface with modern systems using ISO 20022, a mapping process becomes essential to convert ISO 20022 payments messages into the native Swift FIN format. This applies both for the in-flow translation, where intermediaries must downgrade to local format, and on-premise translation (screening/monitoring, processing). The following mapping principles shall ensure seamless communication and integration between the old and new systems.

## Mapping rules

- The Debtor & Creditor hybrid address should be mapped into MT fields using **option F**
- Hybrid addresses of Bank parties should be mapped into MT fields using **option D**
- "**Name**" shall be mapped to the sub-field 1 (suffix: 1/)
- "**AdrLine**" shall be mapped into the sub-field 2 (suffix: 2/)
- "**Country**", "**Post Code**" and "**TownName**" shall be mapped into the sub-field 3 (suffix: 3/)

Please refer to the next page for the mapping priorities of additional structured address attributes for the case where they are available.

**ISO 20022**

```
<Cdtr>
  <Nm>JOHN SMITH</Nm>
  <PstAdr>
    <PstCd>1000</PstCd>
    <TwnNm>BRUSSELS</TwnNm>
    <Ctry>BE</Ctry>
    <AdrLine>HOOGSTRAAT 6, 18th FLOOR</AdrLine>
  </PstAdr>
</Cdtr>
```

**FIN MT**

```
:59F:/BE30001216371411
1/JOHN SMITH
2/HOOGSTRAAT 6, 18th FLOOR
3/BE/BRUSSELS,1000
```

Mapping:
- `Nm` (JOHN SMITH) → Name → `1/JOHN SMITH`
- `AdrLine` (HOOGSTRAAT 6, 18th FLOOR) → Address Line(s) → `2/HOOGSTRAAT 6, 18th FLOOR`
- `Ctry` (BE) → Country → `3/BE`
- `TwnNm` (BRUSSELS) → Town name → `BRUSSELS`
- `PstCd` (1000) → Post Code → `1000`

---

<!-- Page 29 -->

# 6. Mapping principles

Mapping scheme 1 **Hybrid address from MX to MT** > Priorities

| Element description | ISO20022 tag | Occurrences | Data type | Target field/sub-field in SWIFT FIN | Priority fully structured within sub-field | Priority for Hybrid within sub-field |
|---|---|---|---|---|---|---|
| Debtor | `<DBtr>` | [1..1] | | | | |
| Name | `<Nm>` | [0..1] | text[1,140] | F Option Subfield 1 (two occurrences if no LEI is present, 1 occurrence if LEI is present) | **1** | **1** |
| Postal Address | `<PstlAdr>` | [0..1] | | | | |
| Department | `<Dept>` | [0..1] | text[1,70] | F Option Subfield 2 | **7** | **8** |
| Sub Department | `<SubDept>` | [0..1] | text[1,70] | F Option Subfield 2 | **8** | **9** |
| Street Name | `<StrtNm>` | [0..1] | text[1,70] | F Option Subfield 2 | **1** | **1** |
| Building Number | `<BldgNb>` | [0..1] | text[1,16] | F Option Subfield 2 | **2** | **2** |
| Building Name | `<BldgNm>` | [0..1] | text[1,35] | F Option Subfield 2 | **3** | **4** |
| Floor | `<Flr>` | [0..1] | text[1,70] | F Option Subfield 2 | **4** | **5** |
| Post Box | `<PstBx>` | [0..1] | text[1,16] | F Option Subfield 2 | **5** | **6** |
| Room | `<Room>` | [0..1] | text[1,70] | F Option Subfield 2 | **6** | **7** |
| Post Code | `<PstCd>` | [0..1] | text[1,16] | F Option Subfield 3 | **3** | **3** |
| Town Name | `<TwnNm>` | [0..1] | text[1,35] | F Option Subfield 3 | **2** | **2** |
| Town Location Name | `<TwnLctnNm>` | [0..1] | text[1,35] | F Option Subfield 3 | **5** | **5** |
| District Name | `<DstrctNm>` | [0..1] | text[1,35] | F Option Subfield 3 | **6** | **6** |
| Country Sub Division | `<CtrySubDvsn>` | [0..1] | text[1,35] | F Option Subfield 3 | **4** | **4** |
| Country | `<Ctry>` | [0..1] | text[A-Z]{2,2} | F Option Subfield 3 | **1** | **1** |
| Address Line | `<AdrLine>` | [0..1] | text[1,70] | F Option Subfield 2 | n/a | 3 |

| | SWIFT FIN sub-field (option F) |
|---|---|
| 1/ | **<Nm>** (mandatory) (use “+” in case of space limitations) |
| 2/ | Prio 1: <StrtNm> Prio 2: <BldgNm> Prio 3: <AdrLine> (first occurrence) Prio 4: <AdrLine> (second occurrence) Prio 5: <Flr> Prio 6: <PstBx> Prio 7: <Room> Prio 8: <Dept> Prio 9: <SubDept> (use “+” in case of space limitations) |
| 3/ | Prio 1: <Ctry> (mandatory) Prio 2: **<TwnNm>** (mandatory) Prio 3: <PstCd> Prio 4: <TwnLctnNm> Prio 5: <CtrySubDvsn> Prio 6: <DstrctNm> (use “+” in case of space limitations) |

---

<!-- Page 30 -->

Payments Market Practice Group

# 6. Mapping principles

**Mapping scheme 1** **Hybrid address from MX to MT**

**Example 1A:** Long hybrid address mapping from MX to MT

| ISO 20022 | FIN MT |
|---|---|
| `<Cdtr>` | `:59F:/BE30001216371411` |
| `<Nm>Acme NV</Nm>` | `1/Acme NV` |
| `<PstAdr>` | `2/LONG BUILDING NAME WEST VERDIEPIN` |
| `<PstCd>9990</PstCd>` | `2/G 4 BLOEMENDALELAAN 62/3 BUS 47` |
| `<TwnNm>Maldegem</TwnNm>` | `3/BE/MALDEGEM, 9990` |
| `<Ctry>BE</Ctry>` | |
| `<AdrLine>Long Building Name West Verdiep 4</AdrLine>` | |
| `<AdrLine>Bloemendalelaan 62/3 bus 47</AdrLine>` | |
| `</PstAdr>` | |
| `</Cdt>` | |

Mapping labels: Name, Address Line(s), Country, Town name, Post Code

---

<!-- Page 31 -->

# 6. Mapping principles

Payments Market Practice Group

**Mapping scheme 1** **Hybrid address from MX to MT**

**Example 1B: Long name mapping from MX to MT**

## ISO 20022

```xml
<Cdtr>
  <Nm>BROKEN ARROW CORPORATION VERY LONG NAME EXCEEDING 35 CHARACTERS</Nm>
  <PstlAdr>
    <PstCd>1000</PstCd>
    <TwnNm>BRUSSELS</TwnNm>
    <Ctry>BE</Ctry>
    <AdrLine>Long Building Name West Verdiep 4</AdrLine>
  </PstlAdr>
</Cdtr>
```

## FIN MT

```
:59F:/BE30001216371411
1/BROKEN ARROW CORPORATION VERY LON
1/G NAME EXCEEDING 35 CHARACTERS
2/Long Building Name Westverdiepin+
3/BE/BRUSSELS, 1000
```

| ISO 20022 Field | FIN MT Field | Label |
|---|---|---|
| `<Nm>` | `1/` `1/G` | Name |
| `<AdrLine>` | `2/` | Address Line(s) |
| `<Ctry>` | `3/` (pos 1) | Country |
| `<TwnNm>` | `3/` (pos 2) | Town name |
| `<PstCd>` | `3/` (pos 3) | Post Code |

---

<!-- Page 32 -->

# 6. Mapping principles

**Mapping scheme 1** **Hybrid address from MX to MT**

**Example 1C:** Prioritization of structured and hybrid address information from MX to MT

**ISO 20022**

```xml
<Cdtr>
  <Nm>Carol Teo May Lin</Nm>
  <PstlAdr>
    <StrtNm>Keppel Bay</StrtNm>
    <BldgNb>34</BldgNb>
    <PstCd>123456</PstCd>
    <TwnNm>Singapore</TwnNm>
    <Ctry>SG</Ctry>
    <AdrLine>Caribbean At Keppel Bay</AdrLine>
    <AdrLine>#05-66</AdrLine>
  </PstlAdr>
</Cdtr>
```

**FIN MT**

```
:59F:/BE30001216371411
1/Carol Teo May Lin
2/Keppel Bay,34, Caribbean At Keppel
2/Bay #05-66
3/SG/SINGAPORE, 123456
```

**Mapping fields:**

*   **Name** → `Carol Teo May Lin`
*   **Street Name** → `Keppel Bay`
*   **Building Number** → `34`
*   **Address Line(s)** → `Caribbean At Keppel Bay`, `#05-66`
*   **Country** → `SG`
*   **Town name** → `SINGAPORE`
*   **Post Code** → `123456`

---

<!-- Page 33 -->

# 6. Mapping principles

**Mapping scheme 2** | **MX hybrid to MX unstructured – where hybrid is not yet supported** > **Summary**

There could be cases where financial institutions might be exposed to receiving hybrid addresses in payments from their clients and/or local market infrastructures before the official go-live date for cross-border payments as of November 2025. Those financial institutions would need to implement mapping rules before November 2025.

Examples:

1. Corporate clients might have proactively upgraded their internal systems and are already **incorporating hybrid addresses** in pain.001 (CGI) messages sent to banks **before the official support** in the inter-bank space as of November 2025.

2. **Early adoption** of hybrid in certain market infrastructures before November 2025. There are market infrastructures, such as the Fedwire system (for USD), that plan to launch hybrid addresses before November 2025).

**Mapping rules**

- As long as the target MX market infrastructure does not yet allow using hybrid, the simultaneous usage of structured elements and AdrLine is not allowed.
- Hence, both the **structured** and **unstructured** address elements must be mapped into the **AdrLine elements**
- To ensure cross-border interoperability, use up to 3 occurrences of AdrLine (each max. 35 characters) in the output
- Separate the elements with at "," (comma)

Please refer to the next page for the mapping priorities of additional structured address attributes for the case where they are available.

---

<!-- Page 34 -->

# 6. Mapping principles

Mapping scheme 2 **MX hybrid to MX unstructured – where hybrid is not yet supported** > **Priorities**

| Element description | ISO20022 tag | Occurrences | Data type | Target AdrLine mapping within MX unstructured | Priority for mapping within AdrLine | MX address elements of output |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Debitor | `<Dbtr>` | [1..1] | | | | |
| Name | `<Nm>` | [0..1] | text(1,140) | | | `<Nm>` (mandatory) |
| Postal Address | `<PstAdr>` | [0..1] | | | | |
| Department | `<Dept>` | [0..1] | text(1,70) | **3** (or truncate) | **7** | **AdrLine 3** (if not yet filled) |
| Sub Department | `<SubDept>` | [0..1] | text(1,70) | **3** (or truncate) | **8** | Prio 1: `<StrtNm>`<br>Prio 2: `<BldgNb>`<br>Prio 3: `<BldgNm>`<br>Prio 4: `<Flr>`<br>Prio 5: `<PstBx>`<br>Prio 6: `<Room>`<br>Prio 7: `<Dept>`<br>Prio 8: `<SubDept>`<br>(use '^' in case of space limitations) |
| Street Name | `<StrtNm>` | [0..1] | text(1,70) | **3** (or truncate) | **1** | |
| Building Number | `<BldgNb>` | [0..1] | text(1,16) | **3** (or truncate) | **2** | |
| Building Name | `<BldgNm>` | [0..1] | text(1,35) | **3** (or truncate) | **3** | |
| Floor | `<Flr>` | [0..1] | text(1,70) | **3** (or truncate) | **4** | |
| Post Box | `<PstBx>` | [0..1] | text(1,16) | **3** (or truncate) | **5** | |
| Room | `<Room>` | [0..1] | text(1,70) | **3** (or truncate) | **6** | |
| Post Code | `<PstCd>` | [0..1] | text(1,16) | **3** (or 2) | **3** | **AdrLine 3** (or 2 if not yet filled) |
| Town Name | `<TwnNm>` | [0..1] | text(1,35) | **3** (or 2) | **2** | Prio 1: `<Ctry>` (mandatory)<br>Prio 2: `<TwnNm>` (mandatory)<br>Prio 3: `<PstCd>`<br>Prio 4: `<CtrySubDvsn>`<br>Prio 5: `<TwnLctnNm>`<br>Prio 6: `<DstrctNm>`<br>(use '^' in case of space limitations) |
| Town Location Name | `<TwnLctnNm>` | [0..1] | text(1,35) | **3** (or 2) | **5** | |
| District Name | `<DstrctNm>` | [0..1] | text(1,35) | **3** (or 2) | **6** | |
| Country Sub-Division | `<CtrySubDvsn>` | [0..1] | text(1,35) | **3** (or 2) | **4** | |
| Country | `<Ctry>` | [0..1] | text(A,2),2) | **3** (or 2) | **1** | |
| Address Line | `<AdrLne>` | [0..1] | text(1,70) | **1** | **1** | Prio 1: `<AdrLne>` (first occurrence) |

---

<!-- Page 35 -->

# 6. Mapping principles

**Mapping scheme 2** MX hybrid to MX unstructured – where hybrid is not yet supported

**Example 2A:** Prioritization of hybrid address information from **MX hybrid** to **MX fully unstructured**

**ISO 20022**

```
<Cdtr>
  <Nm>JOHN SMITH</Nm>
  <PstlAdr>
    <PstCd>1000</PstCd>
    <TwnNm>BRUSSELS</TwnNm>
    <Ctry>BE</Ctry>
    <AdrLine>HOOGSTRAAT 6, 18th FLOOR</AdrLine>
  </PstlAdr>
</Cdtr>
```

**ISO 20022**

```
<Cdtr>
  <Nm>JOHN SMITH</Nm>
  <PstlAdr>
    <AdrLine>HOOGSTRAAT 6, 18th FLOOR</AdrLine>
    <AdrLine>BE, BRUSSELS, 1000</AdrLine>
  </PstlAdr>
</Cdtr>
```

| Name | Department | Sub Department | Street Name | Building Number |
| :--- | :--- | :--- | :--- | :--- |
| Building Name | Floor | Post Box | Room | Post Code |
| Town name | Town Location Name | District Name | Country Subdivision | Country |

---

<!-- Page 36 -->

# 6. Mapping principles

**Illustration 1: Mapping from pain.001 to inter-bank** > **General use cases & rules**

## Where hybrid is not supported

Corporate customer → Pain.001 (Hybrid) → Financial institution → MT 103 (F-option) → MT-based CSM
Financial institution → Pacs.008 (Unstructured) → ISO20022 based CSM

**Mapping scheme 1**
**Mapping scheme 2**

Financial institutions allowing such customer-to-bank messages are responsible to ensure appropriate mapping from pain.001 to a valid inter-bank pacs.008 message :
- If forwarded into a MT-based system: semi-structured (option F)
- If forwarded to ISO20022: use unstructured AdrLines if hybrid is not supported by target infrastructure

## Where hybrid is supported

Corporate customer → Pain.001 (Hybrid) → Financial institution → Pacs.008 (Hybrid) → ISO20022 based CSM

**Standard ISO20022 mapping (1:1)**

Once hybrid is supported by the receiving infrastructure, the hybrid addresses data in pain.001 should be forwarded as hybrid in the inter-bank message.

---

<!-- Page 37 -->

# 6. Mapping principles

Payments Market Practice Group

## Illustration 2: Intermediary bank mapping

> General use cases & rules

**Where hybrid is not supported**

unstructured
MT 103
MT-based CSM
Financial institution
unstructured
MT 103
Pacs.008
Fully unstructured
MT-based CSM
ISO2002 based CSM

Standard mapping of unstructured address

Unstructured address data from MT 103 should be forwarded as unstructured MT 103 / fully unstructured pacs.008

F-option
MT 103
MT-based CSM
Pacs.008
Financial institution
Pacs.008
ISO2002
Hybrid

Mapping scheme 1

Mapping scheme 2

Financial institutions exposed to market infrastructures allowing early usage of hybrid are responsible for appropriate mapping from pacs.008 to a valid inter-bank pacs.008 message :

➔ If forwarded into a MT-based system: semi-structured (option F)

➔ If forwarded to ISO20022: use unstructured AdrLines if hybrid is not supported by target

---

<!-- Page 38 -->

# 6. Mapping principles

## PMPG Guidance for mapping from hybrid address from/to non-ISO market infrastructures

PMPG suggest guidelines for banks connecting to the MT-based RTGS systems are to implement the following by SR2025:

- **Forwarding bank to RTGS** *(as instructing BIC):*
    - Intermediary banks to convert CBPR+ MX into MT for the RTGS.
    - Intermediary banks to receive and process the newly introduced Hybrid address format
    - Intermediary banks to convert to the MT F Option for the RTGS MT payment (by SR2026)
- **Forwarding bank to cross-border** *(as instructing BIC):*
    - Intermediary banks to convert RTGS MT into CBPR+ MX.
    - Intermediary banks to convert to the Structured or Hybrid address format (by SR2026)
- **Initiating bank – payment with a cross-border leg after the RTGS** *(as instructing BIC):*
    - Send MT payment to RTGS with MT F Option, so that the forwarding bank could convert to MX Structured or Hybrid address format more readily (by SR2026)
    - Update the customer channels to accept only Structured or Hybrid address format for RTGS (by SR2026)
    - *Banks will have to implement this capability for cross-border CBPR+ MX payments as well.*

These guidelines could help to prevent negative impacts to the payment processing in the payment journey

- MX payments without the correct address format cannot be sent to cross-border CBPR+
- Exceptional or manual amendments could be needed with longer delivery time and incur repair fees
- Payments could be rejected or returned
- Delays could cause missing value dates
- Additional customer enquiries and investigations with counterparty banks

---

<!-- Page 39 -->

# 6. Mapping principles

Payments Market Practice Group

## Illustration 3: Intermediary bank mapping

> General use cases & rules

**Where hybrid is supported**

| ISO 2002 based CSM | Pacs.008 | Financial institution | Pacs.008 | ISO2002 based CSM |
| :--- | :--- | :--- | :--- | :--- |
| | Hybrid | | Hybrid | |

Once the receiving infrastructure supports hybrid, the hybrid addresses data in the pacs.008 should be forwarded as the hybrid address of the inter-bank message.

| ISO 2002 based CSM | Pacs.008 | Financial institution | MT 103 | Local CSM (not yet on ISO) |
| :--- | :--- | :--- | :--- | :--- |
| | Hybrid | | F-option | |

| Local CSM (not yet on ISO) | MT 103 | Financial institution | Pacs.008 | SWIFT |
| :--- | :--- | :--- | :--- | :--- |
| | F-option | | MT 103 | |

These guidelines could help to prevent negative impacts to the payment processing in the payment journey

*   MX payments without the correct address format cannot be sent to cross-border CBPR+
*   Exceptional or manual amendments could be needed with longer delivery time and incur repair fees
*   Payments could be rejected or returned
*   Delays could cause missing value dates
*   Additional customer enquiries and investigations with counterparty banks

---

<!-- Page 40 -->

# 6. Town Name - Special cases

Payments Market Practice Group

## 1

### Town Name *is not available*

**How to proceed if no Town Name or City is available?**

There are rare certain cases where a town or city name may not be available, particularly in remote areas. To address this, the PMPG suggests allowing a country subdivision (e.g., province, state, region, or county) to serve as the **next smallest identifying entity** when a town name is not clearly defined.

For clarity and consistency, the town name and the country subdivision (even if they have the same value) should be entered respectively if the same name applies at both levels. This ensures accurate geographic identification while accommodating regional variations in address conventions. The repetition of country subdivision indicates this formatting is intentional.

**Examples**

Sarah Johnson
101 Desert Road
Town/City: **Navajo County**
City/Sub-Division: **Arizona**
City: US

123 Pingan Avenue
Town/City: **Beijing**
City/Sub-Division: **Beijing**
City: CN

Patrick O'Connor
789 Shamrock Lane
Town/City: **County Kerry**

Priya Singh
456 Banyan Road
Town/City: **District Kanara**

## 2

### Town Name *is very long* *(exceeding 35 characters)*

**How to handle very long Town Names?**

For Town Name with >35 characters, the PMPG suggests truncating them to **something identifiable**. For example, while *Welwyn Garden City* is less than 35 characters, it could be abbreviated to "Welwyn Gdn City" for clarity. We believe that the industry is likely to move away from using "NOTPROVIDED" for compliance reasons, and it may eventually become a red-flag issue.

With that in mind, we recommend reintroducing the state/province in the Town Name element. In cases where there's no clear town or city, the province can serve as the next smallest identifying entity, making it appropriate to list both the Town Name and State. This ensures clarity and emphasizes that both are associated with the address, much like the example "NY NY".

**Example**

Full name: Llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch
*(58 characters (!))*

Common abbreviations:
- Llanfairpwllgwyngyll
- Llanfair Pwllgwyngyll
- Llanfairpwll

*(a village on the Isle of Anglesey, Wales)*

---

<!-- Page 41 -->

# 6. Country Mapping

The PMPG country mapping inventory provides a recommended ISO20022 element usage for local addresses

Please download the latest version from the
PMPG Document Centre

Swift Payments Market Practice
Group document centre

- **M** **Mandatory** by schema
- **E** **Expected** by local market practice
- **O** **Optional** element
- **C** **Conditional** (-> see comment)
- **N** **No** (element should not be used)

---

<!-- Page 42 -->

Payments Market Practice Group

To contact the PMPG or provide feedback on the content of this paper, please email info@pmpg.info

follow us on
Linked in