"""以 v13（run v5.7_v11_5）的實際輸出重繪論文圖 1、圖 2。
資料來源（OneLeaf-dx/detection @ fcd7573）：
  Train Code/v11.5/Train_output/extracted/runs/detect/v5.7_v11_5/results.csv  （70 輪訓練紀錄）
  Train Code/v11.5/Train_output/extracted/eval/v5.7_v11_5/confusion_matrix.csv （last.pt，test 401 張，conf=0.25）
繪圖樣式比照 ultralytics 8.4 的 plot_results() 與 ConfusionMatrix.plot(normalize=True)。
輸出到本檔同目錄的 Image/論文修訂說明/。用法：python make_figs.py <detection 庫根目錄>
"""
import csv, sys
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter1d

ROOT = sys.argv[1]  # detection repo root
RUN = f"{ROOT}/Train Code/v11.5/Train_output/extracted"
OUT = Path(__file__).resolve().parent / "Image" / "論文修訂說明"
OUT.mkdir(parents=True, exist_ok=True)

# ---- 圖 1：訓練總覽曲線 ----
with open(f"{RUN}/runs/detect/v5.7_v11_5/results.csv", newline="") as f:
    rows = list(csv.reader(f))
cols = [c.strip() for c in rows[0]]
data = np.array([[float(v) for v in r] for r in rows[1:]])
x = data[:, 0]
index = [2, 3, 4, 5, 6, 9, 10, 11, 7, 8]
fig, ax = plt.subplots(2, 5, figsize=(12, 6), tight_layout=True)
ax = ax.ravel()
for i, j in enumerate(index):
    y = data[:, j].astype(float)
    ax[i].plot(x, y, marker=".", label="results", linewidth=2, markersize=8)
    ax[i].plot(x, gaussian_filter1d(y, sigma=3), ":", label="smooth", linewidth=2)
    ax[i].set_title(cols[j], fontsize=12)
ax[1].legend()
fig.savefig(OUT / "yolo26n_p2_v13_results.png", dpi=200)
plt.close(fig)
print("epochs:", int(x[0]), "-", int(x[-1]), "| last val mAP50:", data[-1, 7], "mAP50-95:", data[-1, 8])

# ---- 圖 2：test 正規化混淆矩陣 ----
with open(f"{RUN}/eval/v5.7_v11_5/confusion_matrix.csv", newline="") as f:
    rows = list(csv.reader(f))
labels = [c.replace("true_", "") for c in rows[0][1:]]
assert [r[0].replace("pred_", "") for r in rows[1:]] == labels
m = np.array([[float(v) for v in r[1:]] for r in rows[1:]])
tp = np.trace(m[:-1, :-1]); fp = m[:-1, :].sum() - tp; fn = m[:, :-1].sum() - tp
print("TP/FP/FN:", tp, fp, fn, "Jaccard:", round(tp / (tp + fp + fn), 5))
array = m / (m.sum(0).reshape(1, -1) + 1e-9)
array[array < 0.005] = np.nan
nc = len(labels) - 1
fig, axc = plt.subplots(1, 1, figsize=(12, 9))
tick_fontsize = max(6, 15 - 0.1 * nc)
label_fontsize = max(6, 12 - 0.1 * nc)
title_fontsize = max(6, 12 - 0.1 * nc)
btm = max(0.1, 0.25 - 0.001 * nc)
im = axc.imshow(array, cmap="Blues", vmin=0.0, interpolation="none")
for i in range(array.shape[0]):
    for j in range(array.shape[1]):
        v = array[i, j]
        if not np.isnan(v):
            axc.text(j, i, f"{v:.2f}", ha="center", va="center", fontsize=10,
                     color="white" if v > 0.45 else "black")
cbar = fig.colorbar(im, ax=axc, fraction=0.046, pad=0.05)
axc.set_xlabel("True", fontsize=label_fontsize, labelpad=10)
axc.set_ylabel("Predicted", fontsize=label_fontsize, labelpad=10)
axc.set_title("Confusion Matrix Normalized", fontsize=title_fontsize, pad=20)
ticks = np.arange(len(labels))
axc.set_xticks(ticks); axc.set_yticks(ticks)
axc.set_xticklabels(labels, fontsize=tick_fontsize, rotation=90, ha="center")
axc.set_yticklabels(labels, fontsize=tick_fontsize)
for s in ("left", "right", "bottom", "top"):
    axc.spines[s].set_visible(False); cbar.ax.spines[s].set_visible(False)
cbar.outline.set_visible(False)
fig.subplots_adjust(left=0, right=0.84, top=0.94, bottom=btm)
fig.savefig(OUT / "yolo26n_p2_v13_confusion_matrix_norm.png", dpi=250)
plt.close(fig)
diag = {labels[k]: round(m[k, k] / m[:, k].sum(), 3) for k in range(nc)}
bgmiss = {labels[k]: round(m[nc, k] / m[:, k].sum(), 3) for k in range(nc)}
print("recall@0.25 (diag):", diag)
print("missed as background:", bgmiss)
