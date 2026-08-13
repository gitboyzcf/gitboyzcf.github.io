# -*- coding: utf-8 -*-
"""
生成 DeepSeek V4 Pro 文章配图：
1. p01_agent_bench.png  - 预览版 vs 0813 正式版 Agent 基准提升
2. p02_horizontal.png   - 与头部模型横向对比
3. p03_price.png        - 价格对比（对数轴）
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np

# 中文字体
for f in ["Microsoft YaHei", "SimHei", "SimSun"]:
    try:
        fm.findfont(f, fallback_to_default=False)
        plt.rcParams["font.sans-serif"] = [f, "Microsoft YaHei", "SimHei", "DejaVu Sans"]
        break
    except Exception:
        continue
plt.rcParams["axes.unicode_minus"] = False

OUT = "D:/project-group/boyzcf.blog/src/assets/images/2026/deepseek-v4-pro"

# 主题色：DeepSeek 蓝 #4D6BFE / 深蓝 #1E3A8A
DS_BLUE = "#4D6BFE"
DS_DARK = "#1F2937"
GRAY = "#9CA3AF"
ORANGE = "#F59E0B"
GREEN = "#10B981"

# ---------------- 图1：Agent 基准：预览版 vs 0813 ----------------
benches = ["DeepSWE", "CyberGym", "NL2Repo", "Terminal\nBench 2.1", "Toolathlon", "Auto\nmationBench", "DSBench\nFullStack", "DSBench\nHard"]
preview = [12.8, 52.7, 38.5, 72.1, 55.9, 12.8, 41.8, 31.1]
v0813 = [62.7, 83.3, 61.5, 87.9, 74.1, 31.8, 71.1, 67.2]

x = np.arange(len(benches))
w = 0.36
fig, ax = plt.subplots(figsize=(11, 5.6), dpi=150)
b1 = ax.bar(x - w/2, preview, w, label="V4 Pro 预览版", color=GRAY, edgecolor="white")
b2 = ax.bar(x + w/2, v0813, w, label="V4 Pro 0813 正式版", color=DS_BLUE, edgecolor="white")
for bars in (b1, b2):
    for rect in bars:
        h = rect.get_height()
        ax.annotate(f"{h:.1f}", (rect.get_x() + rect.get_width()/2, h),
                    ha="center", va="bottom", fontsize=9, color=DS_DARK, fontweight="bold")
ax.set_xticks(x)
ax.set_xticklabels(benches, fontsize=10)
ax.set_ylim(0, 100)
ax.set_ylabel("得分", fontsize=11)
ax.set_title("DeepSeek V4 Pro 0813 vs 预览版：Agent 基准大幅跃升", fontsize=13, fontweight="bold", color=DS_DARK, pad=12)
ax.legend(loc="upper left", frameon=False, fontsize=10)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(axis="y", linestyle="--", alpha=0.3)
fig.text(0.99, 0.02, "数据来源：DeepSeek 官方/社区流出的评测对比表（2026-08）", ha="right", fontsize=8, color=GRAY)
plt.tight_layout()
plt.savefig(f"{OUT}/p01_agent_bench.png", bbox_inches="tight")
plt.close()

# ---------------- 图2：与头部模型横向对比（分组柱状） ----------------
metrics = ["Terminal Bench 2.1", "CyberGym", "DeepSWE", "Toolathlon", "HLE(带工具)", "AutoBench"]
ds = [87.9, 83.3, 62.7, 74.1, 60.0, 31.8]
opus = [85.0, 78.3, 58.0, 76.2, 57.9, 27.2]
fable = [88.0, 83.1, 70.0, 77.9, 63.0, 29.1]
kimi = [88.3, 80.0, 67.5, 76.5, 56.0, 30.8]

x = np.arange(len(metrics))
w = 0.2
fig, ax = plt.subplots(figsize=(11, 5.6), dpi=150)
ax.bar(x - 1.5*w, ds, w, label="DeepSeek V4 Pro 0813", color=DS_BLUE, edgecolor="white")
ax.bar(x - 0.5*w, opus, w, label="Opus 4.8", color="#8B5CF6", edgecolor="white")
ax.bar(x + 0.5*w, fable, w, label="Fable 5", color=ORANGE, edgecolor="white")
ax.bar(x + 1.5*w, kimi, w, label="Kimi K3", color=GREEN, edgecolor="white")
ax.set_xticks(x)
ax.set_xticklabels(metrics, fontsize=9.5)
ax.set_ylim(0, 100)
ax.set_ylabel("得分", fontsize=11)
ax.set_title("DeepSeek V4 Pro 0813 与头部模型横向对比（Agent 维度）", fontsize=13, fontweight="bold", color=DS_DARK, pad=12)
ax.legend(loc="upper left", ncol=4, frameon=False, fontsize=9)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(axis="y", linestyle="--", alpha=0.3)
fig.text(0.99, 0.02, "数据来源：官方/社区流出的评测对比表（2026-08）；横评以各家最新公开数据为准", ha="right", fontsize=8, color=GRAY)
plt.tight_layout()
plt.savefig(f"{OUT}/p02_horizontal.png", bbox_inches="tight")
plt.close()

# ---------------- 图3：价格对比（对数坐标） ----------------
models = ["DeepSeek\nV4 Pro", "GLM-5.2", "Kimi K3", "Opus 4.8", "Fable 5"]
price_out = [0.87, 4.4, 15.0, 25.0, 50.0]
price_in = [0.435, 1.5, 5.0, 8.0, 15.0]

x = np.arange(len(models))
w = 0.32
fig, ax = plt.subplots(figsize=(10, 5.4), dpi=150)
b1 = ax.bar(x - w/2, price_in, w, label="输入价格", color="#A5B4FC", edgecolor="white")
b2 = ax.bar(x + w/2, price_out, w, label="输出价格", color=DS_BLUE, edgecolor="white")
for bars in (b1, b2):
    for rect in bars:
        h = rect.get_height()
        ax.annotate(f"${h:.2f}" if h < 10 else f"${h:.0f}",
                    (rect.get_x() + rect.get_width()/2, h),
                    ha="center", va="bottom", fontsize=9, color=DS_DARK, fontweight="bold")
ax.set_yscale("log")
ax.set_xticks(x)
ax.set_xticklabels(models, fontsize=10)
ax.set_ylabel("价格（美元 / 百万 Token，对数轴）", fontsize=11)
ax.set_title("API 价格对比：DeepSeek 输出价约为 Fable 5 的 1/57", fontsize=13, fontweight="bold", color=DS_DARK, pad=12)
ax.legend(loc="upper left", frameon=False, fontsize=10)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(axis="y", linestyle="--", alpha=0.3)
fig.text(0.99, 0.02, "数据来源：各家官方 API 定价（2026-08），取约数", ha="right", fontsize=8, color=GRAY)
plt.tight_layout()
plt.savefig(f"{OUT}/p03_price.png", bbox_inches="tight")
plt.close()

# ---------------- 图4：DeepSWE 跃迁轨迹 ----------------
stages = ["V4 Pro\n预览版初期", "V4 Pro\n预览版", "V4 Pro\n0813 正式版"]
scores = [7.3, 12.8, 62.7]
fig, ax = plt.subplots(figsize=(8.5, 4.8), dpi=150)
ax.plot(stages, scores, marker="o", markersize=9, linewidth=2.5, color=DS_BLUE, markerfacecolor="white", markeredgewidth=2.5)
for i, s in enumerate(scores):
    ax.annotate(f"{s}", (i, s), textcoords="offset points", xytext=(0, 12),
                ha="center", fontsize=13, fontweight="bold", color=DS_BLUE)
ax.set_ylim(0, 75)
ax.set_ylabel("DeepSWE 得分", fontsize=11)
ax.set_title("DeepSWE（软件工程智能体基准）跃迁轨迹：7.3 → 62.7", fontsize=13, fontweight="bold", color=DS_DARK, pad=12)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.grid(axis="y", linestyle="--", alpha=0.3)
fig.text(0.99, 0.02, "数据来源：社区流传的评测对比表（2026-08）；非官方正式发布", ha="right", fontsize=8, color=GRAY)
plt.tight_layout()
plt.savefig(f"{OUT}/p04_deepswe.png", bbox_inches="tight")
plt.close()

print("图表生成完成：")
import os
for f in os.listdir(OUT):
    print(" -", f)
