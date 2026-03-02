---
title: "Appendix: Knowledge Graphs"
nav_title: "Appendix: Knowledge Graphs"
order: 19
slug: appendix-knowledge-graphs
---


These diagrams are **memory aids**. They are not proofs, and they are not intended to flatten complex history into a single narrative. Use them to keep your bearings when the prose gets dense.

## D1) Timeline of fractures, councils, and dialogue milestones (high-level)

```mermaid
flowchart LR
  A[313\nEdict of Milan] --> B[325\nNicaea I]
  B --> C[381\nConstantinople I]
  C --> D[431\nEphesus]
  D --> E[451\nChalcedon]
  E --> F[787\nNicaea II]
  F --> G[800\nCharlemagne crowned]
  G --> H[1054\nMutual excommunications (later “schism” marker)]
  H --> I[1204\nSack of Constantinople]
  I --> J[1274\nLyon II (reunion attempt)]
  J --> K[1438–39\nFlorence (reunion attempt)]
  K --> L[1517\nLuther’s theses]
  L --> M[1545–1563\nCouncil of Trent]
  M --> N[1555\nPeace of Augsburg]
  N --> O[1618–1648\nThirty Years’ War / Westphalia]
  O --> P[1870\nVatican I]
  P --> Q[1965\nLifting 1054 excommunications (gesture)]
  Q --> R[1993\nBalamand (Catholic–Orthodox)]
  R --> S[1999\nJDDJ (Catholic–Lutheran)]
  S --> T[2016\nHoly and Great Council (Crete)]
```

## D2) “Authority grammars” concept map (why people talk past each other)

```mermaid
flowchart TB
  subgraph ORTH[Orthodox authority grammar (typical)]
    O1[Conciliar reception\n(councils + lived reception)]
    O2[Liturgy as carrier\n(prayer shapes belief)]
    O3[Fathers as baseline\n(continuity instinct)]
    O4[Scripture in the Church\n(heard inside worship)]
    O1 --> O3 --> O2
    O4 --> O2
  end

  subgraph CATH[Catholic authority grammar (typical)]
    C1[Scripture + Tradition\n(one deposit)]
    C2[Magisterium\n(binding teaching office)]
    C3[Development\n(continuity through time)]
    C4[Visible unity mechanisms\n(pastoral adjudication)]
    C1 --> C2 --> C4
    C3 --> C2
  end

  subgraph PROT[Protestant authority grammar (family resemblance)]
    P1[Scripture as final norm\n(court of appeal)]
    P2[Confessions / catechesis\n(stabilizers in community)]
    P3[Conscience before God\n(anti-coercion instinct)]
    P4[Local church governance\n(elders/pastors/synods vary)]
    P1 --> P2
    P1 --> P3
    P2 --> P4
  end

  ORTH --- CATH --- PROT
```

