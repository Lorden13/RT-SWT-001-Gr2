# PRISMA Flow — LLM-based Automated Unit Test Generation

## 1. PRISMA Flowchart

```text
┌──────────────────────────────────────────────┐
│ Records identified from database searching   │
│ (N = 231)                                    │
└──────────────────────────────────────────────┘
                      │
                      ▼
┌──────────────────────────────────────────────┐
│ Records after duplicate removal              │
│ (N = 228)                                    │
└──────────────────────────────────────────────┘
                      │
                      ▼
                Screening V1
┌──────────────────────────────────────────────┐      ┌──────────────────────────────┐
│ Title and abstract screened                  │      │ Records excluded             │
│ (N = 228)                                    │─────▶│ (N = 175)                    │
└──────────────────────────────────────────────┘      └──────────────────────────────┘
                      │
                      ▼
                Eligibility V2
┌──────────────────────────────────────────────┐      ┌──────────────────────────────┐
│ Full-text assessed                           │      │ Full-text excluded           │
│ (N = 53)                                     │─────▶│ (N = 35)                     │
└──────────────────────────────────────────────┘      │ Reasons:                     │
                      │                               │ EC4 = 7                      │
                      ▼                               │ EC5 = 14                     │
┌──────────────────────────────────────────────┐      │ EC6 = 14                     │
│ Included in evidence synthesis               │      └──────────────────────────────┘
│ (N = 18)                                     │
└──────────────────────────────────────────────┘
```

---

## 2. PRISMA Summary Table

| Stage | Number |
|---|---:|
| Records identified from database searching | 231 |
| Duplicate records removed | 3 |
| Records after deduplication | 228 |
| Records screened by title and abstract | 228 |
| Records excluded at V1 | 175 |
| Full-text records assessed | 53 |
| Full-text records excluded at V2 | 35 |
| Final included studies | 18 |

---

## 3. Explanation

The search process identified 231 records from two search strings. After removing 3 duplicate records, 228 records remained for title-and-abstract screening. At V1, 175 records were excluded because they were unrelated to LLM-based unit test generation or lacked empirical relevance. The remaining 53 records were assessed at full-text level. After applying full-text exclusion criteria, 18 studies were included in the final evidence synthesis.
