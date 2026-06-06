# 💼 AI Business

AI商业工具，支持商业计划、市场分析、竞品分析。

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/OpenAI-API-green?logo=openai" />
  <img src="https://img.shields.io/badge/License-MIT-yellow" />
</p>

## ✨ 特性

- 📋 商业计划生成
- 📊 市场分析
- 🔍 竞品分析
- 📑 融资PPT生成
- 💰 单位经济计算
- 📈 增长策略

## 🚀 快速开始

```bash
pip install openai

python tools.py
```

## 📖 使用

```python
from ai_business import create_tools

tools = create_tools()

# 商业计划
plan = tools.generate_business_plan("AI教育平台", "在线教育")

# 市场分析
market = tools.analyze_market("AI软件", "中国")

# 竞品分析
competitor = tools.analyze_competitor("竞品A", "我的产品")

# 融资PPT
pitch = tools.generate_pitch_deck(startup_info)

# 单位经济
economics = tools.calculate_unit_economics(business_data)

# 增长策略
strategy = tools.generate_growth_strategy("SaaS", "早期")
```

## 📁 项目结构

```
ai-business/
├── tools.py       # 商业工具核心
└── README.md
```

## 📄 许可证

MIT License
