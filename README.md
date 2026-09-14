# 一葉知病 OneLeaf — 研究報告

柑橘病蟲害辨識專題「**一葉知病**」（115 資工四A）的完整研究報告，系統採端側離線優先設計。

## 從哪裡開始讀

| 你是 | 從這裡進去 |
| --- | --- |
| 想快速看完整體成果 | [成果總覽](SUMMARY.md) — 核心結論、關鍵數字，每段附原報告連結 |
| 指導教授、評審、農業研究者 | [研究報告總覽](%E6%A4%8D%E7%89%A9%E7%97%85%E8%9F%B2%E5%AE%B3%E8%BE%A8%E8%AD%98%20%28115%E8%B3%87%E5%B7%A5%E5%9B%9BA%29/README.md) — 系統三大模組、七章的章旨與全部子篇 |
| 行動端／邊緣端工程師 | [RAG 架構設計](%E6%A4%8D%E7%89%A9%E7%97%85%E8%9F%B2%E5%AE%B3%E8%BE%A8%E8%AD%98%20%28115%E8%B3%87%E5%B7%A5%E5%9B%9BA%29/RAG%E5%90%91%E9%87%8F%E8%B3%87%E6%96%99%E5%BA%AB/%E6%9E%B6%E6%A7%8B%E8%A8%AD%E8%A8%88.md)、[Flutter 實作與模組整合](%E6%A4%8D%E7%89%A9%E7%97%85%E8%9F%B2%E5%AE%B3%E8%BE%A8%E8%AD%98%20%28115%E8%B3%87%E5%B7%A5%E5%9B%9BA%29/%E8%A1%8C%E5%8B%95%E7%AB%AF%E6%87%89%E7%94%A8%E7%A8%8B%E5%BC%8F%E9%96%8B%E7%99%BC/Flutter%E5%AF%A6%E4%BD%9C%E8%88%87%E6%A8%A1%E7%B5%84%E6%95%B4%E5%90%88.md) |
| 想直接看數據 | [系統測試與評估](%E6%A4%8D%E7%89%A9%E7%97%85%E8%9F%B2%E5%AE%B3%E8%BE%A8%E8%AD%98%20%28115%E8%B3%87%E5%B7%A5%E5%9B%9BA%29/README.md#%E7%B3%BB%E7%B5%B1%E6%B8%AC%E8%A9%A6%E8%88%87%E8%A9%95%E4%BC%B0) — 各模型 TFLite benchmark 與行動端實測 |
| 想看影像辨識模型的程式碼 | [`OneLeaf-dx/detection`](https://github.com/OneLeaf-dx/detection) — YOLO 訓練、評估與手機端延遲量測 ｜ 組織首頁 [`OneLeaf-dx`](https://github.com/OneLeaf-dx) |
| AI agent 或維護者 | [`AGENTS.md`](AGENTS.md) 操作規則 ｜ [`.agent/SPECIFICATION.md`](.agent/SPECIFICATION.md) 報告撰寫規範 ｜ [`CHANGELOG.md`](CHANGELOG.md) 異動紀錄 |

本庫由人類與 AI agent 共同維護：agent 負責結構與命名的機械性維護，也可依人類提供的數據起草報告；研究內容的敘述與結論須經人類核准後才合併。

<details>
<summary>其他說明</summary>

- **遷移公告**：本庫原本掛在個人帳號下，2026-09-10 轉入組織並改名為 `report`。舊網址會自動轉址，但請把本機 remote 換成新的：`git remote set-url origin https://github.com/OneLeaf-dx/report.git`
- **資料說明**：報告內容多數自 Notion 匯出後整理，原始匯出檔名中的 Notion ID 已移除，檔案間相對連結已一併改寫。參考文獻中的**第三方論文 PDF 未納入版本控制**，改以官方 / arXiv 連結呈現。
- **異動紀錄**：任何人或 agent 的每一次 commit，都必須在 [`CHANGELOG.md`](CHANGELOG.md) 最上方新增一筆固定格式的紀錄。累積超過 50 筆或 50KB 時，較舊的條目整段搬到 [`.agent/changelog_archive/`](.agent/changelog_archive/README.md)。

</details>
