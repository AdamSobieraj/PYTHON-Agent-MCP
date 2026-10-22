<!-- Page 1 -->

# Migration to ISO 20022

Useful information, hints and tips

## Contents

1. Introduction to the new language of payments: Parties, agents and message types

2. Message and parties: High level view of parties and message types related to payment flow (showing MT and MX data elements)

3. Payments: Data elements guide

4. Reporting and advising: Data elements guide

5. Examples of MT to MX translation:

   a. MT103 to pacs.008

   b. MT202 to pacs.009

   c. MT202cov to pacs.009.cov

   d. MT210 – camt.057

   e. MT192 – camt.056

---

<!-- Page 2 -->

# Parties, agents and message types

| **Parties / Agents** | |
|---|---|
| **MT Name** | **MX - ISO Name** |
| Field | Element |
| Bank | Agent |
| Ordering Customer | Debtor |
| Ordering Institution | Debtor Agent |
| Beneficiary Customer | Creditor |
| Account with Institution | Creditor Agent |
| Intermediary Institution | Intermediary Agent |
| Message Sender | Instructing Agent |
| Message Receiver | Instructed Agent |
| | Ultimate Debtor (new) |
| | Ultimate Creditor (new) |
| | Initiating Party (new) |

| **Message Types** | | |
|---|---|---|
| **Existing** | **MX - ISO Message** | **Message Sets** |
| Pain.001 (v3) / MT101 (relay) | pain.001 (v9) | payment initiation (pain) |
| MT103 | pacs.008 | |
| MT202 | pacs.009 (core, adv) | |
| MT202 cov | pacs.009 (cov) | payment & clearing settlement (pacs) |
| | pacs.004 - (new return message) | |
| MT190 / MT290 (rejections only) | pacs.002 | |
| MT196 | camt.029 | |
| MT 941 / MT942 | camt.052 | |
| MT940 / MT950 | camt.053 | |
| MT900 / MT910 | camt.054 | cash management (camt) |
| MT192 / MT 292 | camt.056 | |
| MT210 | camt.057 | |
| MT920 | camt.060 | |
| MT199 / MT299 | tbc | |

---

<!-- Page 3 -->

related to payment flow (showing MT and MX data elements)

## What is changing? Party Identifiers

**Payment Initiation (pain)**

- Remitter (Initiator)
- Instructing Agent
- Initiator
- Instructing Party

**Previous Instructing Agents**

- `:72:/INS/`
- `:53a` `:54a` `:56a`
- `:56a` `:72:/INT/`

- Order Agent
- Instructing Agent
- Instructed Agent
- Creditor Agent

**Cash Management (camt)**

- Customer (Creditor)
- Creditor

`:50a`
`:52a`
`:50a` Sender
`:59a` Receiver
`:57a`
`:59a`

**Legend: ISO 20022**

- (Circle icon) New parties introduced in ISO 20022
- (Green box `:xx`) FIN MT format equivalent

---

<!-- Page 4 -->

| Data Element | MT101 | MT103 | MT202 | MT202COV | pacs.008 | pacs.009 | pain.001 |
|---|---|---|---|---|---|---|---|
| ULTIMATE_CREDITOR | | | | | UltmtCddr | N/A | N/A |
| CREDITOR | 59 | 59 | 58 | 59 | Cddr | Cddr | Cddr |
| CREDITOR_AGENT | 57 | 57 (or Receiver) | 57 (or Receiver) | 58 | CddrAgt | CddrAgt | CddrAgt |
| INTERMEDIARY_AGENT_3 | | | | | IntrmyAg3 | IntrmyAg3 | IntrmyAg3 |
| INTERMEDIARY_AGENT_2 | | | | 57 (or only if 56 is present) | IntrmyAg2 | IntrmyAg2 | IntrmyAg2 |
| INTERMEDIARY_AGENT_1 | 56 | 56 | 56 | 56 (or 57) | IntrmyAg1 | IntrmyAg1 | IntrmyAg1 |
| INSTRUCTED_AGENT | Receiver | Receiver | Receiver | Receiver | InstdAg | InstdAg | InstdAg |
| THIRD_REIMBURSEMENT_AGENT | | 55 | | | ThirdRmbrsmtAg | N/A | N/A |
| INSTRUCTED_REIMBURSEMENT_AGENT | | 54 | | | InstdRmbrsmtAg | N/A | N/A |
| INSTRUCTING_REIMBURSEMENT_AGENT | | 53 | | | SttlmAcc | N/A | N/A |
| INSTRUCTING_AGENT | Sender | Sender | Sender | Sender | InstgAg | InstgAg | N/A |
| PREVIOUS_INSTRUCTING_AGENT_3 | | | | | PrvInstgAg3 | PrvInstgAg3 | N/A |
| PREVIOUS_INSTRUCTING_AGENT_2 | | | | | PrvInstgAg2 | PrvInstgAg2 | N/A |
| PREVIOUS_INSTRUCTING_AGENT_1 | | | | | PrvInstgAg1 | PrvInstgAg1 | N/A |
| DEBTOR_AGENT | 52 | 52 (or Sender) | | 52 (or Sender) | DbtrAg | DbtrAg | DbtrAg |
| DEBTOR | 50F/50G/50H | 50 | 52 (or Sender) | 50 | Dbtr | Dbtr | Dbtr |
| ULTIMATE_DEBTOR | | | | | UltmtDbtr | N/A | UltmtDbtr |
| FORWARDING_AGENT | | | | | FwdgAg | N/A | N/A |
| INITIATING_PARTY | 50C/50L | | | | N/A | N/A | InitPty |
| REMITTANCE_INFORMATION | 70 | 70 | | | RmtInf Ustrd Strd | RmtInf Ustrd Strd | RmtInf Ustrd Strd |
| INSTRUCTIONS_FOR_CREDITOR_AGENT | | 72 | 72 | 72 | InstrForCddrAg | InstrForCddrAg | InstrForCddrAg |
| INSTRUCTIONS_FOR_NEXT_AGENT | | 23E & 72 | 72 | 72 | InstrForXAg | InstrForXAg | InstrForNxtAg |
| INSTRUCTION_IDENTIFICATION | 20 | 20 | 20 | 20 | InstrId | InstrId | InstrId |
| END_TO_END_IDENTIFICATION | 21 | | 21 | 21 | EndToEndId | EndToEndId | EndToEndId |
| UETR | | 121 | | 121 | UETR | UETR | UETR |
| CHARGE_BEARER | | 71 | | | ChrgBr | N/A | ChrgBr |

---

<!-- Page 5 -->

# 4. Reporting and advising: Data elements guide

| Data Element | MT900 | MT910 | Iso20022 (camt.54) |
| :--- | :--- | :--- | :--- |
| ULTIMATE_CREDITOR | | | UltmtCdtor |
| CREDITOR | 59 | 59 | Cdtor |
| CREDITOR_AGENT | 57 (or Receiver) | 57 (or Receiver) | CdtorAgt |
| INTERMEDIARY_AGENT_3 | | | IntrmyAgt3 |
| INTERMEDIARY_AGENT_2 | | | IntrmyAgt2 |
| INTERMEDIARY_AGENT_1 | 56 | 56 | IntrmyAgt1 |
| INSTRUCTED_AGENT | Receiver | Receiver | InstdAgt |
| INSTRUCTING_AGENT | Sender | Sender | InstdgAgt |
| DEBTOR_AGENT | 52 (or Sender) | 52 (or Sender) | DbtrAgt |
| DEBTOR | 50 | 50 | Dbtr |
| ULTIMATE_DEBTOR | | | UltmtDbtr |
| INITIATING_PARTY | | | InitgPty |
| REMITTANCE_INFORMATION | | | RmtInf Ustrd Strd |
| INSTRUCTIONS_FOR_CREDITOR_AGENT | 72 | 72 | No direct mapping in camt.054 schema; J.P. Morgan will map it to /Intrpy/AddtlIntrlyInf |
| INSTRUCTIONS_FOR_NEXT_AGENT | 72 | 72 | |
| INSTRUCTION_IDENTIFICATION | 20 | 20 | InstdId |
| END_TO_END_IDENTIFICATION | 21 | 21 | EndToEndId |
| UETR | 121 | 121 | UETR |
| CHARGE_BEARER | 71 | 71 | ChrgBr |

---

<!-- Page 6 -->

| MT103 | pacs.008 |
|---|---|
| [1:F01CHASGB2LXXXX:0000000000000]:[2:01030000099123 CHASDEFXXXX 00000000000991231000000]:[3:111:001]:[21: 000000000-0000-4000-8000-0000000000000]:[4: 20:P5607186 298 :23B:CREO :32A:200721EUR39,36 :33B:EUR39,36 :50F:/123991234 1/SAMPLE DEBTOR LTD 2/SAMPLE DEBTOR STREET,1 3/GB/SAMPLE DEBTOR CITY :52D: SAMPLE DB AGENT NAME SAMPLE DB AGENT STREET SAMPLE DB AGENT CITY ZIP COD3 :57A:MVBWDE55 :59:/DE123456789000000000000 SAMPLE CR NAME LTD SAMPLE CR STREET 56 CITY ZIP COD3 :70:/PURD/FUNDING//UBI/this is unstructured remittance :71A:SHA :71F:EURO. :72:/ACC/instruct for creditor agent /PRIORITY/ /FND/ :J5:{CHK:E82015BFF39CE}} | <AppHdr xmlns="urn:iso:std:iso:20022:tech:xsd:head.001.001.02"> <Fr> <Flld> <FinInstlId> <BICF>CHASDEFXXXX</BICF> </FinInstlId> </Flld> </Fr> <To> <Flld> <FinInstlId> <BICF>CHASGB2LXXXX</BICF> </FinInstlId> </Flld> </To> <BizMsgIdr>P5607186 298</BizMsgIdr> <MsgDefIdr>pacs.008.001.08</MsgDefIdr> <BizSvc>swift.chpplus.02</BizSvc> <Credt>9999-12-31T00:00:00+00:00</Credt> <Pty>NORM</Pty> </AppHdr> <Document xmlns="urn:iso:std:iso:20022:tech:xsd:pacs.008.001.08"> <FitotCstmrCdtTr> <GrpHdr> <MsgId>P5607186 298</MsgId> <CdBrTm>9999-12-31T00:00:00+00:00</CredTm> <NbOfTxs>1</NbOfTxs> <SttlInf> <SttlMtd>INDA</SttlMtd> </SttlInf> </GrpHdr> <CdtTrTxInf> <PmtId> <InstdId>P5607186 298</InstdId> </PmtId> </EndToEndId>NOTPROVIDED</EndToEndId> <UETR>00000000-0000-4000-8000-0000000000000</UETR> </PmtId> <PmtTpInf> <SvcTl> <Cd>G001</Cd> </SvcTl> </PmtTpInf> <InstdAmt Ccy="EUR">39.36</InstdAmt> <InstdAmt Ccy="EUR">39.36</InstdAmt> <InstdAmt Ccy="EUR">39.36</InstdAmt> <ChrgBr>SHAR</ChrgBr> <ChrgInf> <Amt Ccy="EUR">0</Amt> </ChrgInf> <Ag> <FinInstlId> <Nm>NOTPROVIDED</Nm> </FinInstlId> <PstlAdr> <AdrLine>NOTPROVIDED</AdrLine> </PstlAdr> </FinInstlId> |

---

<!-- Page 7 -->

# a. MT103 - pacs.008

| MT103 | pacs.008 (continued) |
|---|---|
| [1:F01CHASGB2LXXXX0000000000]{2:0103000099123 | </Ag> |
| CHASEDEFXXXX 0000000000099123100000N}{3:{111:001}}{21: | </ChrgInf> |
| 00000000-0000-4000-8000-000000000000}}{4: | </InstgAg> |
| **20:P560718A 29E** | <FinInstnId> |
| :23B:CRED | <BICFI>CHASEDEFXXXX</BICFI> |
| **:32A:200722EUR39,36** | </FinInstnId> |
| **:33B:EUR39,36** | </InstgAg> |
| :50F:/123991234 | <InstdAg> |
| 1/SAMPLE DEBTOR LTD | <FinInstnId> |
| 2/SAMPLE DEBTOR STREET,1 | <BICFI>CHASGB2LXXXX</BICFI> |
| 3/GB/SAMPLE DEBTOR CITY | </FinInstnId> |
| :52D: SAMPLE_DB_AGENT_NAME | </InstdAg> |
| SAMPLE_DB_AGENT_STREET | <Dbtr> |
| SAMPLE_DB_AGENT_CITY ZIP_CODE3 | <Nm>SAMPLE_DB_NAME LTD</Nm> |
| :57A:MVBMD€55 | <PstlAdr> |
| :59:/DE12345678900000000000 | <StrtNm>SAMPLE_DB_STREET</StrtNm> |
| SAMPLE_CR_NAME LTD | <BldgNb>123</BldgNb> |
| SAMPLE_CR_STREET 56 CITY ZIP_CODE3 | <PstCd>SAMPLE_ZIP_CODE3</PstCd> |
| **:70:/PURD/FUNDING//UBI/this is unstructured remittance** | <TwnNm>SAMPLE_DB_CITY</TwnNm> |
| **:71A:SHA** | <Ctry>GB</Ctry> |
| **:71F:EURO** | </PstlAdr> |
| :72:/ACC/instruct for creditor agent | </Dbtr> |
| /PRIORITY/ | <DbtrAcct> |
| /FWD/ | <Id> |
| -}{5:[CHK:E82015BF3FCE]} | <Othr> |
|  | <Id>123991234</Id> |
|  | </Othr> |
|  | </Id> |
|  | </DbtrAcct> |
|  | <DbtrAg> |
|  | <FinInstnId> |
|  | <Nm>SAMPLE_DB_AGENT_NAME</Nm> |
|  | <PstlAdr> |
|  | <AdrLine>SAMPLE_DB_AGENT_STREET</AdrLine> |
|  | <AdrLine>SAMPLE_DB_AGENT_CITY ZIP_CODE3</AdrLine> |
|  | </PstlAdr> |
|  | </FinInstnId> |
|  | </DbtrAg> |
|  | <CdtTr> |
|  | <FinInstnId> |
|  | <BICFI>MVBMD€55</BICFI> |
|  | </FinInstnId> |
|  | </CdtTr> |

---

<!-- Page 8 -->

a. MT103 - pacs.008

**MT103**

{1:F01:CHASDEFXXX{2:O000000009}{3:{O:01030000099123
CHASDEFXXX 0000000000099123100000M}{4:{103:121:
00000000-0000-4000-8000-000000000000}}}{4:
:20:P5607186 298
:23B:CRED
:32A:200212EUR39,36
:33B:EUR39,36
:50F:1/23991234
1/SAMPLE DEBTOR LTD
2/SAMPLE DEBTOR STREET,1
3/GB/SAMPLE DEBTOR CITY
:52A:SAMPLE DB AGENT NAME
SAMPLE DB AGENT STREET
SAMPLE DB AGENT CITY ZIP_CODE3
:57A:MVBMODE5
:59:/DE12345678900000000000
SAMPLE CR NAME LTD
SAMPLE CR STREET 56 CITY ZIP_CODE3
:70:/PURP/FUNDING//URI/this is unstructured remittance
:71A:SHA
:77F:EURO,
:72:/ACC/instruct for creditor agent
/PRIORITY/
/FND/
-}{5:{CHK:E820158F3FCE}}}

**pacs.008 (continued)**

<Cdtr>
<Nm>SAMPLE CR_NAME LTD</Nm>
<PstlAdr>
<AdrLine>SAMPLE CR_STREET 56 CITY ZIP_CODE3</AdrLine>
</PstlAdr>
</Cdtr>
<CdtrAcct>
<Id>
<Othr>
<dD>DE12345678900000000000</dD>
</Othr>
</Id>
</CdtrAcct>
<InstrForCdtrAg>
<InstrIn>Instruct for creditor agent</InstrIn>
</InstrForCdtrAg>
<InstrForNxtAg>
<InstrIn>/PRIORITY/ /FND/</InstrIn>
</InstrForNxtAg>
<RmtnInf>
<Ustd>/PURP/FUNDING//URI/this is unstructured remittance</Ustd>
</RmtnInf>
</CdtTrf>
</Document>

---

<!-- Page 9 -->

## b. MT202 - pacs.009

---

**MT202**

```
{1:F01CHASGB2LXXXX0000000000}{2:O2020000000000
CHASDEFXXXX000000000001010100000N}{3:{11:001}{12:
00000000-0000-4000-8000-000000000000}}{4:
P20-P5607I86 298
21:ABCD/1234567
:32A:000124:UK:9,36
:52A:/123991234
CHASFRPP
:57A:DEUTDEFF
:58A:/DE99551900000907039999
DEUTGB2L
//2:/BNF/Testing of Translation of MT20
//2 into a pacs.009 Core
-}
```

**pacs.009**

```xml
<AppHdr xmlns="urn:iso:std:iso:20022:tech:xsd:head.001.001.02">
    <Fr>
        <Field>
            <FinInstnId>
                <BICFI>CHASDEFXXXX</BICFI>
            </FinInstnId>
        </Field>
    </Fr>
    <To>
        <Field>
            <FinInstnId>
                <BICFI>CHASGB2LXXXX</BICFI>
            </FinInstnId>
        </Field>
    </To>
    <BizMsgIdr>P5607I86 298</BizMsgIdr>
    <MsgDefIdr>pacs.009.001.08</MsgDefIdr>
    <BizSvc>swift.cbprplus.02</BizSvc>
    <Credt>9999-12-31T00:00:00+00:00</Credt>
    <Prtty>NORM</Prtty>
</AppHdr>
<Document xmlns="urn:iso:std:iso:20022:tech:xsd:pacs.009.001.08">
    <FICdtTrf>
        <GrpHdr>
            <MsgId>P5607I86 298</MsgId>
            <CredtTm>9999-12-31T00:00:00+00:00</CredtTm>
            <NbOfTxs>1</NbOfTxs>
            <SttlmInf>
                <SttlmMtd>INDA</SttlmMtd>
            </SttlmInf>
        </GrpHdr>
        <CdtTrfTxInf>
            <PmtId>
                <InstrId>P5607I86 298</InstrId>
                <EndToEndId>ABCD/1234567</EndToEndId>
                <UETR>00000000-0000-4000-8000-000000000000</UETR>
            </PmtId>
            <PmtTpInf>
                <Svcl>
                    <Cd>G001</Cd>
                </Svcl>
            </PmtTpInf>
            <IntrBkStlmAmt Ccy="EUR">9,36</IntrBkStlmAmt>
            <IntrBkStlmDt>2020-01-24</IntrBkStlmDt>
            <InstgAgt>
                <FinInstnId>
                    <BICFI>CHASDEFXXXX</BICFI>
                </FinInstnId>
            </InstgAgt>
            <InstdAgt>
                <FinInstnId>
                    <BICFI>CHASGB2LXXXX</BICFI>
                </FinInstnId>
            </InstdAgt>
```

---

<!-- Page 10 -->

| MT202 | pacs.009 (continued) |
| :--- | :--- |
| {1:F01:CHASDEF2XXXXX:0000000000}{2:0202000000000<br>CHASDEFXXXX0000000000010100000}{3:{111:001}{21:<br>000000000-0000-4000-8000-000000000000}}{4:<br>**20:P5607186.298**<br>**21:ABCD/1234567**<br>**32A:20021224EUR39.36**<br>:52A:/123991234<br>CHASFRPP<br>:57A:DEUTDEFF<br>:58A:/DE995519000000907039999<br>DEUTGB2L<br>**//2:BNI//testing of Translation of MT20**<br>**//2 into a pacs.009 Core.**<br>-} | <Dbtr><br>&nbsp;&nbsp;<FinInstId><br>&nbsp;&nbsp;&nbsp;&nbsp;<BICFI>CHASFRPP</BICFI><br>&nbsp;&nbsp;</FinInstId><br></Dbtr><br><DbtrAcct><br>&nbsp;&nbsp;<Id><br>&nbsp;&nbsp;&nbsp;&nbsp;<Othr><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<Id>123991234</Id><br>&nbsp;&nbsp;&nbsp;&nbsp;</Othr><br>&nbsp;&nbsp;</Id><br></DbtrAcct><br><CdtrAgt><br>&nbsp;&nbsp;<FinInstId><br>&nbsp;&nbsp;&nbsp;&nbsp;<BICFI>DEUTDEFF</BICFI><br>&nbsp;&nbsp;</FinInstId><br></CdtrAgt><br><Cdtr><br>&nbsp;&nbsp;<FinInstId><br>&nbsp;&nbsp;&nbsp;&nbsp;<BICFI>DEUTGB2L</BICFI><br>&nbsp;&nbsp;</FinInstId><br></Cdtr><br><CdtrAcct><br>&nbsp;&nbsp;<Id><br>&nbsp;&nbsp;&nbsp;&nbsp;<Othr><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<Id>DE995519000000907039999</Id><br>&nbsp;&nbsp;&nbsp;&nbsp;</Othr><br>&nbsp;&nbsp;</Id><br></CdtrAcct><br>**<RmtInf>**<br>&nbsp;&nbsp;**<Ustrd>BNI//testing of Translation of MT202 into a pacs.009 Core</Ustrd>**<br>**</RmtInf>**<br></FIToFIIv1><br></Document><br></Envelope> |

---

<!-- Page 11 -->

| MT202cov | pacs.009cov |
|---|---|
| `{1:F01CHASG62LXXXX0000000000}{2:0020000000000`<br>`CHASDEFXXXX00000000000101000000N}{3:{11:001121:`<br>`00000000-0000-4000-8000-000000000000}}{4:`<br>`:20:P5607186_298`<br>`:21:ABC0/1234567`<br>`:32A:090711USD9,35`<br>`:50A:DEUTDEFF`<br>`:58A:DEUTSU33`<br>`:72:BN//Testing of Translation of MT20`<br>`//2 into a pacs.009 Core`<br>`:50F/123456`<br>`1/SAMPLE_DB_NAME_LTD`<br>`2/SAMPLE_DB_STREET,123`<br>`3/US/SAMPLE_DB_CITY SAMPLE_ZIP_COD3`<br>`:57A:DEUTSU33`<br>`:59:/99009900`<br>`SAMPLE_CR_NAME`<br>`SAMPLE_CR_STREET 456`<br>`SAMPLE_CR_CITY SAMPLE_ZIP_COD3`<br>`US`<br>`:70:/ROC/1234567//`<br>`Remittance information for SAMPLE_CR_NAME`<br>`-}` | `<AppHdr xmlns="urn:iso:std:iso:20022:tech:xsd:head.001.001.02">`<br>`<Fr>`<br>`<FinInstnId>`<br>`<BICFi>CHASDEFXXXX</BICFi>`<br>`</FinInstnId>`<br>`</Fr>`<br>`<To>`<br>`<FinInstnId>`<br>`<BICFi>CHASGB2LXXX</BICFi>`<br>`</FinInstnId>`<br>`</To>`<br>`<MsgDefId>pacs.009.001.08</MsgDefId>`<br>`<MsgId>pacs.009.001.08</MsgId>`<br>`<BizSvc>swift.cbprplus.co.02</BizSvc>`<br>`<Cred>9999-12-31T00:00:00+00:00</Cred>`<br>`<Prtty>NORM</Prtty>`<br>`</AppHdr>`<br>`<Document xmlns="urn:iso:std:iso:20022:tech:xsd:pacs.009.001.08">`<br>`<FicDtTrf>`<br>`<GrpHdr>`<br>`<MsgId>P5607186_298</MsgId>`<br>`<CredDtTm>9999-12-31T00:00:00+00:00</CredDtTm>`<br>`<NbOfTxs>1</NbOfTxs>`<br>`<SttlmInf>`<br>`<SttlmMtd>INDA</SttlmMtd>`<br>`</SttlmInf>`<br>`</GrpHdr>`<br>`<CdtTrfTxInf>`<br>`<PmtId>`<br>`<InstrId>P5607186_298</InstrId>`<br>`<EndToEndId>ABC0/1234567</EndToEndId>`<br>`<UETR>00000000-0000-4000-8000-000000000000</UETR>`<br>`</PmtId>`<br>`<PmtTpInf>`<br>`<SvcLvl>`<br>`<Cd>G001</Cd>`<br>`</SvcLvl>`<br>`</PmtTpInf>`<br>`<IntrBkSttlmAmt Ccy="EUR">30.36</IntrBkSttlmAmt>`<br>`<IntrBkSttlmDt>2020-02-12</IntrBkSttlmDt>`<br>`<InstgAgt>`<br>`<FinInstnId>`<br>`<BICFi>CHASDEFXXXX</BICFi>`<br>`</FinInstnId>`<br>`</InstgAgt>`<br>`<InstdAgt>`<br>`<FinInstnId>`<br>`<BICFi>CHASGB2LXXX</BICFi>`<br>`</FinInstnId>`<br>`</InstdAgt>`<br>`<Dbtr>`<br>`<FinInstnId>`<br>`<BICFi>CHASDEFXXXX</BICFi>`<br>`</FinInstnId>`<br>`</Dbtr>`<br>`<CdtrAgt>`<br>`<FinInstnId>`<br>`<BICFi>DEUTDEFF</BICFi>`<br>`</FinInstnId>`<br>`</CdtrAgt>` |

---

<!-- Page 12 -->

| **MT202Cov** | **pac.009Cov (continued)** |
|---|---|
| {1:F01CHASEGB2LXXXX0000000000}{2:02020000000000<br>CHASEDEFXXXXX000000000001010100000}{3:{11:001}{21:<br>00000000-0000-4000-8000-000000000000}}{4:<br>**20:PSA607186 291**<br>**21:ABCD/1234567**<br>**32A:000126/UK39,36**<br>:57A:DEUTDEFF<br>:58A:DEUTUS33<br>**72:/BNF/Testing of Translation of MT20**<br>**/72 into a pac.009 Core**<br>**50F:/123456**<br>**1/SAMPLE_DB_NAME LTD**<br>2/SAMPLE_DB_STREET,123<br>**3/US/SAMPLE_DB_CITY SAMPLE_ZIP,CO33**<br>:57A:DEUTUS33<br>:59:/99009900<br>SAMPLE_CR_NAME<br>SAMPLE_CR_STREET 456<br>SAMPLE_CR_CITY SAMPLE_ZIP,CO33<br>US<br>:70:/ROC/1234567//<br>Remittance Information for SAMPLE_CR_NAME<br>-} | <Cdt><br>&nbsp;&nbsp;&nbsp;&nbsp;<FinInstrId><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<BICF>DEUTUS33</BICF><br>&nbsp;&nbsp;&nbsp;&nbsp;</FinInstrId><br></Cdt><br><RmtInf><br>&nbsp;&nbsp;&nbsp;&nbsp;<Ustrd>BNF/Testing of Translation of MT202 into a pac.009 Core</Ustrd><br>&nbsp;&nbsp;&nbsp;&nbsp;</RmtInf><br>&nbsp;&nbsp;&nbsp;&nbsp;<UndrlygCstmrCdtTr><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<Dbtr><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<Nm>SAMPLE_DB_NAME </Nm><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<PstlAdr><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<AdrLine>SAMPLE_DB_STREET,123</AdrLine><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<AdrLine>US_DB_CITY SAMPLE_ZIP,CO33</AdrLine><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</PstlAdr><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</Dbtr><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<DbtrAcct><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<Id><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<Othr><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<Id>123456</Id><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</Othr><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</Id><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</DbtrAcct><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<DbtrAgt><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<FinInstrId><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<BICF>CHASEXXXX</BICF><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</FinInstrId><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</DbtrAgt><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<CdtAgt><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<FinInstrId><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<BICF>DEUTUS33</BICF><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</FinInstrId><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</CdtAgt><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<Cdt><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<Nm> SAMPLE_CR_NAME LTD </Nm><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<PstlAdr><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<AdrLine>SAMPLE_CR_STREET 456 </AdrLine><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<AdrLine>SAMPLE_CR_CITY SAMPLE_ZIP,CO33</AdrLine><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<AdrLine>US</AdrLine><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</PstlAdr><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</Cdt><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<CdtAcct><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<Id><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<Othr><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<Id>99009900</Id><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</Othr><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</Id><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</CdtAcct><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<RmtInf><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<Ustrd>ROC/1234567/ Remittance Information for SAMPLE_CR_NAME</Ustrd><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</RmtInf><br>&nbsp;&nbsp;&nbsp;&nbsp;</UndrlygCstmrCdtTr><br>&nbsp;&nbsp;&nbsp;&nbsp;</CdtTrTxInf><br></FicDtTr><br></Document><br></Envelope> |

---

<!-- Page 13 -->

d. MT210 - camt.057

| **MT210** | **camt.052** |
|---|---|
| [1:F:KREDDEBBXXXXXXXX000000991231<br>RABOBE22XXXX00000000009912310000W][3:12I:<br>761646b-3734-4953-a160-afa9d8101212][4:4:<br>:20:450032UH1H:<br>:23:RABO2564185-365v:<br>:30:201201<br>:32E:EUR2000000,<br>:50: SAMPLE_DB_NAME LTD<br>SAMPLE_DB STREET,123<br>:56A:CBPXE99<br>-][5:[CHK:BCS9D414F788]] | <AppHdr xmlns="urn:iso:std:iso:20022:tech:xsd:head.001.001.02"><br>&nbsp;&nbsp;<Fr><br>&nbsp;&nbsp;&nbsp;&nbsp;<FinInstnId><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<BICFI>RABOBE22</BICFI><br>&nbsp;&nbsp;&nbsp;&nbsp;</FinInstnId><br>&nbsp;&nbsp;</Fr><br>&nbsp;&nbsp;<To><br>&nbsp;&nbsp;&nbsp;&nbsp;<FinInstnId><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<BICFI>KREDDEBB</BICFI><br>&nbsp;&nbsp;&nbsp;&nbsp;</FinInstnId><br>&nbsp;&nbsp;</To><br>&nbsp;&nbsp;<Tp><br>&nbsp;&nbsp;&nbsp;&nbsp;<BizMsgIdr>450032UH1H</BizMsgIdr><br>&nbsp;&nbsp;<MsgDefIdr>camt.057.001.06</MsgDefIdr><br>&nbsp;&nbsp;<BizSvc>swift.cbprplus.02</BizSvc><br>&nbsp;&nbsp;<Credt>2020-11-30T09:00:00+01:00</Credt><br></AppHdr><br><Document xmlns="urn:iso:std:iso:20022:tech:xsd:camt.057.001.06"><br>&nbsp;&nbsp;<NtfcnToBtc><br>&nbsp;&nbsp;&nbsp;&nbsp;<GrpHd><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<MsgId>450032UH1H</MsgId><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<CredtTm>2020-11-30T09:00:00+01:00</CredtTm><br>&nbsp;&nbsp;&nbsp;&nbsp;</GrpHd><br>&nbsp;&nbsp;&nbsp;&nbsp;<Ntfcn><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<Id>NFTCTNID10001</Id><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<Acct><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<Id><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<Othr><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<Id>RABO2564185-365v</Id><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</Othr><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</Id><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</Acct><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<AcctOwnr><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<Agt><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<FinInstnId><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<BICFI>RABOBE22</BICFI><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</FinInstnId><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</Agt><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</AcctOwnr><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<AcctSvcr><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<FinInstnId><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<BICFI>KREDDEBB</BICFI><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</FinInstnId><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</AcctSvcr><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<Dbtr><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<Pty><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<Nm>ABC Ltd</Nm><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<PstlAdr><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<AdrLine>10 Broad Street London GB</AdrLine><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</PstlAdr><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</Pty><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</Dbtr> |

---

<!-- Page 14 -->

| MT210 | camt.057 (continued) |
| :--- | :--- |
| {[L:FIX:RED:BE:XXXX0000000000]{Z:0210000991231<br>RAB08E22:XXX000000000000999123100000}{E:{I21:<br>761d46fb-3734-4953-a160-afa9d8101212}{4:<4:<br>20:450032UHH<br>20:RAB0264185-965<br>30:201201<br>21:INFTCTNITEM01<br>32B:EUR2000000,<br>50: SAMPLE DR NAME LTD<br>SAMPLE DR STREET 123<br>56A:CBPXBE99<br>}{S:{CHK:BC59D414F788}}} | <IntrmyAgt><br>&nbsp;&nbsp;<FinInstnId><br>&nbsp;&nbsp;&nbsp;&nbsp;<BICFI>CBPXBE99</BICFI><br>&nbsp;&nbsp;</FinInstnId><br></IntrmyAgt><br><Itm><br>&nbsp;&nbsp;<Id>NFTCTNITEM01 </Id><br>&nbsp;&nbsp;<UETR>761d46fb-3734-4953-a160-afa9d8101212</UETR><br>&nbsp;&nbsp;<Amt Ccy="EUR">2000000</Amt><br>&nbsp;&nbsp;<pctdValDt>2020-12-01</XpctdValDt><br></Itm><br></NftcTo><br></Document> |

---

<!-- Page 15 -->

e. MT192 - camt.056

| **MT192** | **camt.056** |
|---|---|
| [1:F:INDEAFIHHXXXX0000000000][2:019200000991231<br>RB05GB2LXX00000000000099123100000][3:[21:<br>8a562c67-ca16-48ba-b074-6581be6f001][4:<br>**220-CE-001**<br>**21:pac58bizmsgdr01**<br>:15:103<br>**16:R**<br>:79:/AMO9/<br>/UETR/8a562c67-ca16-48ba-b074-6581be6f001<br>**32A:210217EURL000000,**<br>-]55:[CHK/ABD90896761B] | <AppHdr xmlns="urn:iso:std:iso:20022:tech:xsd:head.001.001.02"><br>&nbsp;&nbsp;<Fr><br>&nbsp;&nbsp;&nbsp;&nbsp;<FinInstnId><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<BICFI>RB05GB2L</BICFI><br>&nbsp;&nbsp;&nbsp;&nbsp;</FinInstnId><br>&nbsp;&nbsp;</Fr><br>&nbsp;&nbsp;<To><br>&nbsp;&nbsp;&nbsp;&nbsp;<FinInstnId><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<BICFI>NDEAFIHH</BICFI><br>&nbsp;&nbsp;&nbsp;&nbsp;</FinInstnId><br>&nbsp;&nbsp;</To><br>&nbsp;&nbsp;<BizMsgIdr>cm056bizmsgdr-001</BizMsgIdr><br>&nbsp;&nbsp;<MsgDefIdr>camt.056.001.08</MsgDefIdr><br>&nbsp;&nbsp;<BizSvc>swift.cbprplus.02</BizSvc><br>&nbsp;&nbsp;<CreDt>2021-02-17T12:10:00+01:00</CreDt><br></AppHdr><br><Document xmlns="urn:iso:std:iso:20022:tech:xsd:camt.056.001.08"><br>&nbsp;&nbsp;<FitOfrPmtCclRqrp><br>&nbsp;&nbsp;&nbsp;&nbsp;<Assignmt><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<Id>ASSNID-001</Id><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<Assignr><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<Agtr><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<FinInstnId><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<BICFI>RB05GB2L</BICFI><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</FinInstnId><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</Agtr><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</Assignr><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<Assigne><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<Agtr><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<FinInstnId><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<BICFI>NDEAFIHH</BICFI><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</FinInstnId><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</Agtr><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</Assigne><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<CreDtTm>2021-02-17T08:30:00+01:00</CreDtTm><br>&nbsp;&nbsp;&nbsp;&nbsp;</Assignmt><br>&nbsp;&nbsp;&nbsp;&nbsp;<Undrlyg><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<TxInf><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<Case><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<Id>**CE-001**</Id><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<Cctr><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<Agtr><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<FinInstnId><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<BICFI>RB05GB2L</BICFI><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</FinInstnId><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</Agtr><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</Cctr><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</Case><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</TxInf><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<OrgnlGrpInf><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<OrgnlMsgIdr>**pac58bizmsgdr01**</OrgnlMsgIdr><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<OrgnlMsgNmIdr>pac.008.001.08</OrgnlMsgNmIdr><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<OrgnlCreDtTm>2021-02-17T08:30:00+01:00</OrgnlCreDtTm> |

---

<!-- Page 16 -->

e. MT192 - camt.056

**MT192**

```text
{I:POINDEAFHXXXXXXXX000000000}{2:1920000991231
805GCEL1:XXXXXXXX00000000099123100000}{3:{21:
8a562c67-ca16-48ba-b074-65581be6f001}}{4:
20:CSE-001
21:pacsBkzmssgdr01
:115:103
201217
:79:/AM09/
/UETR/8a562c67-ca16-48ba-b074-65581be6f001
8a562c67-ca16-48ba-b074-65581be6f001
:15:{CHK:ABD908967618}}
```

**camt.056 (continued)**

```xml
</OrgnlPrinf>
<OrgnlInstrId><pacsBkzmssgdr01/></OrgnlInstrId>
<OrgnlEndToEndId><pacs008EndToEndId-001/></OrgnlEndToEndId>
<OrgnlUETR>8a562c67-ca16-48ba-b074-65581be6f001</OrgnlUETR>
<OrgnlInstrAmt><Amt Ccy="EUR">1000.00</Amt></OrgnlInstrAmt>
<OrgnlInstrStm><pacs008EndToEndId-001/></OrgnlInstrStm>
</CxlRsnInf>
<Orgtr>
<Nm>A Debitor</Nm>
<PstlAdr>
<StrtNm>280 Bishopsgate</StrtNm>
<TwnNm>London</TwnNm>
<Ctry>GB</Ctry>
</PstlAdr>
</Orgtr>
<Rsm>
<Cd>AM09</Cd>
</Rsm>
</CxlRsnInf>
</TxInf>
</Undrlyg>
</FIToFIPmtCxlReq>
</Document>
</Envelope>
```