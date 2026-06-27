# PRISMA 2020 Flow Diagram

```markdown
[Records từ database searching (N = 218)]
│   ├── String A (IEEE/Scholar): 158 papers
│   └── String B (Scopus/Scholar): 60 papers
↓
[Sau khi xóa duplicate (N = 217)]  ← Số dòng trong 01_all_records.csv (217 papers)
│   └── Loại trùng lặp (N = 1): ID 69 (trùng với ID 61)
↓
┌────────────────────────────────────────────────────────┐
│  Screened title + abstract (N = 217)              │
│  └── Excluded (N = 172):                               │
│       - IC1 (Non-English): 14 papers                   │
│       - IC2 (Pre-2018): 18 papers                      │
│       - EC4 (Out of scope / noise): 134 papers         │
│       - EC2 (Citation only/No PDF): 6 papers           │
└────────────────────────────────────────────────────────┘
↓ 45 papers pass                               ← INCLUDE trong 02_after_screening_v1.csv
┌────────────────────────────────────────────────────────┐
│  Full-text assessed (N = 45)                           │
│  └── Excluded (N = 29):                                │
│       - EC2 (No full-text PDF available): 2 papers     │
│       - EC3 (Short paper < 4 pages): 3 papers          │
│       - EC4 (Focuses only on execution/maintenance): 15│
│       - IC5 (No quantitative empirical metrics): 9     │
└────────────────────────────────────────────────────────┘
↓
[Final included (N = 16)]                      ← Include trong 03_final_included.csv
```

**Kiểm tra nhất quán (Consistency Check):**
- Rows trong `01_all_records.csv` = N sau dedup = **217** ✓
- Count(v1_decision = EXCLUDE) = Excluded vòng 1 = **172** ✓
- Count(v1_decision = INCLUDE) = Full-text assessed = **45** ✓
- Count(v2_decision = Exclude) = Excluded vòng 2 = **29** ✓
- Count(v2_decision = Include) = Final included = **16** ✓
- Tổng N = Excluded vòng 2 (29) + Final included (16) = **45** ✓
