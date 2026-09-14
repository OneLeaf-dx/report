---
name: add-report
description: 新增一篇報告到報告庫時使用。涵蓋放哪一章的判斷、檔名決定、骨架模板、索引頁掛載與驗證。
---

# 新增一篇報告

## 1. 先決定放哪一章

依 [`SPECIFICATION.md`](../../SPECIFICATION.md) §2 的職責界線判斷。口訣：

> 「怎麼算」進〈效能指標評估〉，「算出來多少」進〈系統測試與評估〉，「怎麼做出來的」進各建置章。

判斷不出來就問使用者，**不要新開一章**。章的數量是刻意固定的。

## 2. 決定檔名

依 [`SPECIFICATION.md`](../../SPECIFICATION.md) §5.2 樣式表，模型代號取自 §5.4 名詞統一表。

| 這篇是 | 檔名長這樣 |
| --- | --- |
| 訓練報告 | `20260729_yolo26n_p2_training_report.md` |
| 基準測試 | `yolo26n_p2_fp16_benchmark.md` |
| 版本比較 | `yolo26n_p2_v2_vs_v3_comparison.md` |
| 資料集統計 | `yolo26_v2_dataset_stats.md` |
| 週期報告 | `20260729_weekly_report.md` |
| 設計／說明 | `架構設計.md`（中文 2–8 字） |

檢查：無空格、無括號、無流水號結尾、日期為 8 位含年份。

## 3. 建檔位置

```
植物病蟲害辨識 (115資工四A)/<章名>/<篇名>.md          ← 報告本體
植物病蟲害辨識 (115資工四A)/<章名>/Image/<篇名>/      ← 圖表資料夾（有圖才建）
```

不得建到第四層。編碼一律 **UTF-8 不含 BOM**。章導覽 `README.md` 與資產資料夾同層，不要另建 `<章名>.md`。

## 4. 骨架

**從模板開始，不要自己排版。** 依類型複製 [`.agent/templates/`](../../templates) 裡的對應檔案：

| 這篇是 | 模板 |
| --- | --- |
| 訓練報告 | `training_report_template.md` |
| 基準測試 | `benchmark_template.md` |
| 版本比較 | `comparison_template.md` |
| 資料集統計 | `dataset_stats_template.md` |
| 週期報告 | `weekly_report_template.md` |
| 設計／說明 | `design_doc_template.md` |

步驟：

1. 把模板複製到第 3 步決定的位置，檔名依第 2 步：

   ```powershell
   Copy-Item .agent/templates/training_report_template.md "植物病蟲害辨識 (115資工四A)/病蟲害辨識模型/20260729_yolo26n_p2_training_report.md"
   ```

2. 填入所有 `<...>` 佔位欄位。模型名稱依 [`SPECIFICATION.md`](../../SPECIFICATION.md) §5.4：檔名用代號、正文用正式名稱
3. 模板裡的連結與圖片範例寫在行內程式碼裡（否則 verify-links 會把佔位路徑當成斷鏈），填寫時去掉反引號、換成實際相對路徑
4. 刪除所有 `<!-- -->` 指引註解。用不到的選用節整節刪除，並把後面的 H2 編號往前遞補
5. 超過 400 行時，在報告資訊區塊之後加 `## 目錄`

哪些段落固定、中段怎麼分，見 [`SPECIFICATION.md`](../../SPECIFICATION.md) §3。**模板是骨架的唯一來源**，不要在這裡另抄一份——兩份一定會漂移。

## 5. 標題規則

寫的時候就守住，事後改很麻煩（見 [`SPECIFICATION.md`](../../SPECIFICATION.md) §4）：

- 全檔**只有一個 H1**
- 不跳級、最深 H4
- 標題不加粗 `## **標題**`、不放 emoji
- 編號用 `1.` / `1.1`，**不用**「一、二、三」
- 同層編號不得重複
- 表圖用獨立流水號 `表 3-1` / `圖 3-1`，緊接表說／圖說；解讀句只在違反預期或需額外說明時才寫

寫內容時另守 [`SPECIFICATION.md`](../../SPECIFICATION.md) §3.1 的資訊密度規則：摘要每條 ≤ 30 字、只寫結論；完整數據表與過程性描述用 `<details>` 折疊；解讀句是條件性的。

## 6. 圖片

放進該章 `Image/` 底下與報告同名的資料夾，檔名依 [`SPECIFICATION.md`](../../SPECIFICATION.md) §5.3：

```
<對象>_<圖表類型>[_<條件>].png
```

圖表類型只能用 §5.3 字典裡的詞。**不要在這裡另抄一份清單**——字典會增修，兩份清單一定會漂移，以 §5.3 為唯一來源。

**不得**用流水號區分不同對象。

引用時用相對路徑，中文與空格 percent-encode：

```markdown
![圖 3-1 PR 曲線](Image/%E6%A8%A1%E5%9E%8B%E8%A8%93%E7%B7%B4%E6%95%B8%E6%93%9A%E5%A0%B1%E5%91%8A/yolo26n_p2_pr_curve.png)
```

## 7. 掛上索引

章導覽只有一份：`植物病蟲害辨識 (115資工四A)/README.md`。在該章對應的 H2 區塊底下加一行連結，
維持與同區塊其他子篇一致的寫法（一行一條、相對路徑、中文 percent-encode）。

**章導覽只放導覽，不要順手把正文寫進去。** 那 191 行的〈行動端應用程式開發〉正是這樣長出來的。某章的章旨超過 3 行，會被 `audit-structure.ps1` 的 `chapter_intro_too_long` 擋下。

## 8. 驗證

```powershell
powershell -ExecutionPolicy Bypass -File .agent/scripts/verify-links.ps1
powershell -ExecutionPolicy Bypass -File .agent/scripts/audit-structure.ps1
```

新增報告會讓 `files_without_summary` 等指標上升 → audit 直接 fail。這是**設計如此**：新報告本來就該一次寫對。fail 的話回去補，不要改基準線。

最後依 [`SPECIFICATION.md`](../../SPECIFICATION.md) §7 檢查清單逐項確認，再依 [`commit-and-push`](../commit-and-push/SKILL.md) 提交。
