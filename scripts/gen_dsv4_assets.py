# -*- coding: utf-8 -*-
"""
补充素材：关键信息卡 + 微信封面裁剪
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from PIL import Image

for f in ["Microsoft YaHei", "SimHei"]:
    try:
        fm.findfont(f, fallback_to_default=False)
        plt.rcParams["font.sans-serif"] = [f, "Microsoft YaHei", "SimHei", "DejaVu Sans"]
        break
    except Exception:
        continue
plt.rcParams["axes.unicode_minus"] = False

OUT = "D:/project-group/boyzcf.blog/src/assets/images/2026/deepseek-v4-pro"
DS_BLUE = "#4D6BFE"
DS_DARK = "#1F2937"
BG = "#F8FAFC"
GRAY = "#6B7280"

# ---------------- 关键信息卡 ----------------
fig, ax = plt.subplots(figsize=(9, 6.5), dpi=160)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis("off")
ax.set_facecolor(BG)
fig.patch.set_facecolor(BG)

# 标题
ax.text(0.5, 0.92, "DeepSeek V4 Pro 0813 关键信息卡", fontsize=17, fontweight="bold",
        color=DS_DARK, ha="center", va="top")
ax.text(0.5, 0.86, "北京时间 2026-08-13 凌晨，DeepSeek 官网 API 文档悄然更新",
        fontsize=10, color=GRAY, ha="center", va="top")

items = [
    ("版本号", "DeepSeek-V4-Pro-0813"),
    ("模型 ID", "deepseek-v4-pro（无需改代码）"),
    ("架构 / 参数", "MoE，总参数 1.6T，每 Token 激活 49B"),
    ("上下文 / 输出", "1M Token 上下文，384K Token 最大输出"),
    ("API 定价（人民币）", "输入 3 元/百万 · 输出 6 元/百万 · 缓存命中 0.025 元/百万"),
    ("推理模式", "thinking 模式默认开启，支持 high / xhigh"),
    ("协议兼容", "OpenAI / Anthropic / Responses API"),
    ("开源许可", "MIT"),
]

y = 0.76
for label, value in items:
    ax.add_patch(plt.Rectangle((0.08, y - 0.07), 0.84, 0.078, facecolor="white",
                                edgecolor="#E5E7EB", linewidth=0.8, zorder=1, joinstyle="round"))
    ax.text(0.12, y - 0.015, label, fontsize=10, fontweight="bold", color=DS_BLUE, va="top", zorder=2)
    ax.text(0.12, y - 0.050, value, fontsize=10, color=DS_DARK, va="top", zorder=2)
    y -= 0.092

ax.text(0.5, 0.02, "数据来源：DeepSeek 官方 API 定价页、官方博客及多家科技媒体报道（2026-08-13）",
        fontsize=8, color=GRAY, ha="center", va="bottom")
plt.tight_layout()
plt.savefig(f"{OUT}/p05_info_card.png", bbox_inches="tight", facecolor=BG)
plt.close()

# ---------------- 微信封面裁剪（2.35:1） ----------------
cover = Image.open(f"{OUT}/A_clean__modern_tech_blog_cove_2026-08-13T02-16-51.png")
w, h = cover.size
# 裁剪掉底部水印后取 2.35:1
crop_h = int(w / 2.35)
if crop_h > h:
    crop_w = int(h * 2.35)
    left = (w - crop_w) // 2
    wechat = cover.crop((left, 0, left + crop_w, h - 100))
else:
    top = (h - crop_h) // 2
    wechat = cover.crop((0, top, w, top + crop_h))
wechat.save(f"{OUT}/cover_wechat.png", quality=95)

print("补充素材生成完成：")
import os
for f in os.listdir(OUT):
    if "cover" in f or "info_card" in f:
        print(" -", f)
