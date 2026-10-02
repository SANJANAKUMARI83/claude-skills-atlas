# Claude Skills Atlas — How It Works

The Atlas is a community-maintained library of reusable Claude building blocks. GitHub renders Mermaid diagrams directly in Markdown, so these diagrams stay editable and version-controlled.

## 🧠 How the Atlas works

```mermaid
flowchart LR
    U[User / Contributor] --> D[Discover a task]
    D --> R{Choose resource type}

    R --> S[🧩 Skill]
    R --> P[📝 Prompt]
    R --> W[🔄 Workflow]
    R --> A[🤖 Agent]
    R --> T[📐 Template]

    S --> C[Use / Adapt]
    P --> C
    W --> C
    A --> C
    T --> C

    C --> F[Feedback / Improvement]
    F --> PR[Pull Request]
    PR --> REV[Community Review]
    REV -->|Approved| M[Merge]
    REV -->|Changes needed| F
    M --> LIB[(Atlas Library)]
    LIB --> D
```

## 🤝 How a contribution becomes part of the Atlas

```mermaid
flowchart TD
    I[💡 Idea or repeated task]
    I --> Q[Write a reusable resource]
    Q --> V[Validate clarity, safety, licensing]
    V --> B{Meets contribution standards?}
    B -->|No| FIX[Improve resource]
    FIX --> V
    B -->|Yes| BR[Create branch]
    BR --> C[Commit changes]
    C --> PR[Open Pull Request]
    PR --> CI[Automated checks]
    CI --> REVIEW[Maintainer / community review]
    REVIEW -->|Requested changes| FIXPR[Update PR]
    FIXPR --> CI
    REVIEW -->|Approved| MERGE[Merge]
    MERGE --> LIB[(Claude Skills Atlas)]
    LIB --> U[🌍 Community reuse]
```

## 🧱 Resource architecture

```mermaid
flowchart TB
    ATLAS[🧠 Claude Skills Atlas]

    ATLAS --> SK[skills/]
    ATLAS --> PRM[prompts/]
    ATLAS --> WF[workflows/]
    ATLAS --> AG[agents/]
    ATLAS --> TMP[templates/]
    ATLAS --> DOC[docs/]

    SK --> CODE[💻 Coding]
    SK --> RES[🔬 Research]
    SK --> MATH[📐 Mathematics]
    SK --> DATA[📊 Data]
    SK --> EDU[🎓 Education]
    SK --> BIO[🧬 Biology]
    SK --> WRITE[✍️ Writing]

    PRM --> REUSE[Copy → Adapt → Use]
    WF --> REPEAT[Repeatable process]
    AG --> SPECIAL[Specialized behavior]
    TMP --> START[Contribution starting point]
    DOC --> GUIDE[Guides + source curation]
```

## 🔁 The contribution loop

```mermaid
flowchart LR
    CREATE[Create] --> TEST[Test]
    TEST --> SHARE[Open PR]
    SHARE --> REVIEW[Review]
    REVIEW --> MERGE[Merge]
    MERGE --> USE[Community uses it]
    USE --> FEEDBACK[Feedback]
    FEEDBACK --> CREATE
```

## Design principle

A good Atlas resource should be **specific, reusable, testable, and honest about its limitations**.

The visual diagrams complement the written contribution rules; the repository remains understandable without the diagrams.
