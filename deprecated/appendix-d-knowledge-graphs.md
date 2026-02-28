# Appendix D: Knowledge Graphs

> **Editorial Note (Claude Opus 4.6, Tech/Artifact Builder):** These graphs implement section 5.1.B's proposal for visual knowledge mapping. Two layers are provided: (1) a historical timeline of fractures and convergences, and (2) a conceptual influence map of theological ideas across traditions. Both are rendered in Mermaid.js syntax for portability. The graphs are deliberately simplified — they are pedagogical tools for lay readers, not exhaustive scholarly maps.

---

## D.1 Historical Timeline: Fractures and Convergences

```mermaid
timeline
    title Christianity's Major Fractures and Convergences
    section The Shared Foundation
        1st–3rd c. : Early Church
                   : Local bishops, shared letters, creeds
                   : Liturgy precedes polemics
                   : Desert monasticism emerges
        313 : Edict of Milan
            : Christianity legalized
        325 : Council of Nicaea
            : Trinitarian creed established
            : Emperor convenes — theology meets empire
        381 : Council of Constantinople
            : Nicene Creed finalized
        451 : Council of Chalcedon
            : Two-natures Christology defined
    section The First Fractures
        451 : Oriental Orthodox separation
            : Coptic, Armenian, Syriac, Ethiopian churches diverge
            : Linguistic and political factors harden the split
        589 : Council of Toledo
            : Filioque appears in Western usage
        787 : Nicaea II (last ecumenical council recognized by East)
        800 : Charlemagne crowned
            : Rival Western empire — political axis shifts
    section The East-West Fracture
        1054 : Mutual excommunications
             : More symbol than immediate lived separation
        1204 : Sack of Constantinople (Fourth Crusade)
             : The wound that made the schism permanent
        1274 : Council of Lyon II
             : Reunion attempted — failed (political duress)
        1438 : Council of Florence
             : Reunion attempted — failed (no reception)
    section The Reformation Fracture
        1517 : Luther's 95 Theses
             : Indulgence crisis as immediate trigger
        1525 : Zwingli's Zurich reforms
        1529 : Marburg Colloquy
             : Luther vs. Zwingli on the Eucharist — fracture within the fracture
        1534 : Act of Supremacy (England)
             : Anglican settlement begins
        1545–1563 : Council of Trent
                  : Catholic reform and boundary-setting
        1555 : Peace of Augsburg
             : Religion becomes a political category
        1648 : Peace of Westphalia
             : Confessional identity entrenched
    section Modern Convergences
        1870 : Vatican I
             : Papal infallibility defined
        1901–1906 : Pentecostal revivals
                  : Topeka and Azusa Street
        1962–1965 : Vatican II
                  : Collegiality, ecumenism, liturgical renewal
        1965 : Mutual lifting of 1054 excommunications
        1993 : Balamand Statement
             : Rejects uniatism as reunion method
        1999 : Joint Declaration on Justification
             : Catholic-Lutheran convergence on Reformation's core dispute
        2016 : Holy and Great Council (Crete)
             : First pan-Orthodox council in 1,000+ years — several churches absent
```

---

## D.2 The Three Authority Grammars: Structure Map

```mermaid
graph TD
    subgraph SHARED["SHARED FOUNDATION"]
        NC["Nicene Creed (325/381)"]
        CH["Chalcedon (451)"]
        SC["Shared Scriptures"]
        BP["Baptism, Eucharist, Prayer"]
        AH["Apophatic Humility"]
    end

    subgraph ORTHODOX["CONCILIAR CONTINUITY (Orthodox)"]
        OA["Authority: Ecumenical Councils + Synods"]
        OS1["S: Historical rootedness"]
        OS2["S: Sacramental density"]
        OS3["S: Apophatic restraint"]
        OS4["S: Theosis"]
        OR1["R: Stagnation"]
        OR2["R: Ethnic captivity"]
        OR3["R: Suspicion of novelty"]
    end

    subgraph CATHOLIC["MAGISTERIAL DEVELOPMENT (Catholic)"]
        CA["Authority: Pope + Magisterium"]
        CS1["S: Institutional coherence"]
        CS2["S: Doctrinal development"]
        CS3["S: Social teaching tradition"]
        CS4["S: Religious orders"]
        CR1["R: Over-centralization"]
        CR2["R: Development circularity"]
        CR3["R: Juridical dominance"]
    end

    subgraph PROTESTANT["SCRIPTURAL PRIMACY (Protestant)"]
        PA["Authority: Scripture + Conscience"]
        PS1["S: Accessibility"]
        PS2["S: Missionary zeal"]
        PS3["S: Prophetic capacity"]
        PS4["S: Reformability"]
        PR1["R: Fragmentation"]
        PR2["R: Interpretive instability"]
        PR3["R: Loss of historical memory"]

        subgraph PROT_SUB["Three Dialects"]
            LP["Liturgical/Confessional"]
            RB["Reformed/Baptist"]
            CP["Charismatic/Pentecostal"]
        end
    end

    NC --> ORTHODOX
    NC --> CATHOLIC
    NC --> PROTESTANT
    CH --> ORTHODOX
    CH --> CATHOLIC
    CH --> PROTESTANT
    SC --> ORTHODOX
    SC --> CATHOLIC
    SC --> PROTESTANT

    OA -.->|"tension"| CA
    CA -.->|"tension"| PA
    OA -.->|"tension"| PA

    style SHARED fill:#e8f5e9,stroke:#2e7d32
    style ORTHODOX fill:#e3f2fd,stroke:#1565c0
    style CATHOLIC fill:#fff3e0,stroke:#e65100
    style PROTESTANT fill:#f3e5f5,stroke:#6a1b9a
```

---

## D.3 Conceptual Influence Map: Ideas Across Traditions

```mermaid
graph LR
    subgraph EARLY["Early Church (1st–5th c.)"]
        DESERT["Desert Fathers<br/>Monasticism"]
        CAPP["Cappadocians<br/>(Basil, Gregory of Nyssa, Gregory Naz.)"]
        AUG["Augustine<br/>(354–430)"]
        CHRYS["Chrysostom<br/>(347–407)"]
        PDIO["Pseudo-Dionysius<br/>(c. 500)"]
    end

    subgraph EAST["Eastern Development"]
        MAX["Maximus the Confessor<br/>(c. 580–662)"]
        DAM["John of Damascus<br/>(c. 675–749)"]
        PAL["Gregory Palamas<br/>(1296–1359)"]
        HESY["Hesychasm"]
        PHILO["Philokalia<br/>(compiled 1782)"]
    end

    subgraph WEST_MED["Western Medieval"]
        BEN["Benedict of Nursia<br/>(c. 480–547)"]
        ANS["Anselm<br/>(1033–1109)"]
        AQ["Thomas Aquinas<br/>(1225–1274)"]
        CLOUD["Cloud of Unknowing<br/>(14th c.)"]
        ECKH["Meister Eckhart<br/>(c. 1260–1328)"]
        JC["John of the Cross<br/>(1542–1591)"]
    end

    subgraph REFORM["Reformation"]
        LUTH["Luther<br/>(1483–1546)"]
        CALV["Calvin<br/>(1509–1564)"]
        CRAN["Cranmer / BCP<br/>(1489–1556)"]
        TRENT["Council of Trent<br/>(1545–1563)"]
    end

    subgraph MODERN["Modern Developments"]
        NEWM["Newman<br/>(1801–1890)"]
        AZUSA["Azusa Street<br/>(1906)"]
        RESS["Ressourcement<br/>(de Lubac, Balthasar)"]
        VAT2["Vatican II<br/>(1962–1965)"]
        JDDJ["JDDJ<br/>(1999)"]
        PENT_THEO["Pentecostal Theology<br/>(Yong, Macchia)"]
    end

    CAPP -->|"apophatic theology"| PDIO
    PDIO -->|"mystical theology"| MAX
    PDIO -->|"via negativa"| CLOUD
    PDIO -->|"via negativa"| ECKH
    MAX -->|"theosis"| PAL
    PAL -->|"essence/energies"| HESY
    HESY -->|"compiled"| PHILO

    DESERT -->|"monastic rule"| BEN
    AUG -->|"grace, sin, will"| ANS
    ANS -->|"scholastic method"| AQ
    AUG -->|"grace theology"| LUTH
    AUG -->|"predestination"| CALV
    AQ -->|"responded to"| TRENT
    LUTH -->|"responded to"| TRENT

    NEWM -->|"development theory"| VAT2
    RESS -->|"patristic recovery"| VAT2
    LUTH -.->|"justification convergence"| JDDJ
    TRENT -.->|"justification convergence"| JDDJ

    AZUSA -->|"pneumatology"| PENT_THEO
    HESY -.->|"apophatic connection"| PENT_THEO

    CAPP -->|"central for East"| EAST
    AUG -->|"central for West"| WEST_MED
    CHRYS -->|"liturgical theology"| EAST

    style EARLY fill:#f9f9f9,stroke:#999
    style EAST fill:#e3f2fd,stroke:#1565c0
    style WEST_MED fill:#fff3e0,stroke:#e65100
    style REFORM fill:#f3e5f5,stroke:#6a1b9a
    style MODERN fill:#e8f5e9,stroke:#2e7d32
```

---

## D.4 The Three-Layer Model (East-West Fracture)

```mermaid
graph TB
    subgraph LAYER1["Layer 1: THEOLOGY"]
        T1["Filioque dispute"]
        T2["Papal authority scope"]
        T3["Doctrinal development<br/>vs. conciliar finality"]
        T4["Essence/energies<br/>distinction"]
    end

    subgraph LAYER2["Layer 2: GOVERNANCE"]
        G1["Conciliar authority<br/>vs. papal jurisdiction"]
        G2["How is change<br/>authorized?"]
        G3["Who settles<br/>disputes?"]
        G4["Autocephaly vs.<br/>centralization"]
    end

    subgraph LAYER3["Layer 3: MEMORY"]
        M1["1054<br/>Mutual excommunications"]
        M2["1204<br/>Sack of Constantinople"]
        M3["Lyon II / Florence<br/>Imposed reunions"]
        M4["Centuries of<br/>mutual non-communication"]
    end

    LAYER1 ---|"intertwined with"| LAYER2
    LAYER2 ---|"hardened by"| LAYER3
    LAYER3 ---|"colors perception of"| LAYER1

    CONVERGENCE["Modern Convergence<br/>(JDDJ 1999, Balamand 1993,<br/>Lifting of 1054 excommunications 1965)"]

    CONVERGENCE -->|"addresses"| LAYER1
    CONVERGENCE -.->|"barely touches"| LAYER2
    CONVERGENCE -.->|"barely touches"| LAYER3

    style LAYER1 fill:#e3f2fd,stroke:#1565c0
    style LAYER2 fill:#fff3e0,stroke:#e65100
    style LAYER3 fill:#ffebee,stroke:#c62828
    style CONVERGENCE fill:#e8f5e9,stroke:#2e7d32
```

---

## Notes on These Graphs

1. **These are pedagogical tools, not scholarly claims.** They simplify dramatically. A full influence map of Christian theology would require a book of its own.

2. **The color coding is consistent across graphs:** Blue = Orthodox/Eastern, Orange = Catholic/Western, Purple = Protestant, Green = Shared/Convergent.

3. **Dotted lines indicate contested or emerging connections.** Solid lines indicate well-established historical influence.

4. **The Three-Layer Model graph (D.4)** visually demonstrates GPT-5.2's key analytical insight: modern convergence efforts work primarily on Layer 1 (theology) while Layers 2 (governance) and 3 (memory) remain largely untouched. This is why "convergence without communion" is the persistent pattern.

5. **Rendering:** These graphs are written in Mermaid.js syntax. They can be rendered in any Mermaid-compatible tool (GitHub, GitLab, Obsidian, or via the Mermaid Live Editor at mermaid.live). For print publication, they should be rendered to SVG or PDF.
