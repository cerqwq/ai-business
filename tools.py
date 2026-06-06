"""
AI Business - AI商业工具
支持商业计划、市场分析、竞品分析
"""

import json
import os
from typing import Dict, List, Any
from datetime import datetime

try:
    from openai import OpenAI
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


class AIBusinessTools:
    """
    AI商业工具
    支持：计划、市场、竞品
    """

    def __init__(self, model: str = "mimo-v2.5-pro", api_key: str = None, base_url: str = None):
        self.model = model
        if OPENAI_AVAILABLE:
            self.client = OpenAI(
                api_key=api_key or os.environ.get('OPENAI_API_KEY', ''),
                base_url=base_url or os.environ.get('OPENAI_BASE_URL', 'https://api.xiaomimimo.com/v1')
            )
        else:
            self.client = None

    def generate_business_plan(self, idea: str, market: str) -> str:
        """生成商业计划"""
        if not self.client:
            return "LLM客户端未配置"

        prompt = f"""请为以下商业想法生成商业计划：

想法：{idea}
市场：{market}

要求：
1. 执行摘要
2. 市场分析
3. 产品/服务
4. 营销策略
5. 财务预测"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=4000
        )

        return response.choices[0].message.content

    def analyze_market(self, industry: str, region: str) -> Dict:
        """分析市场"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请分析{region}的{industry}市场：

请返回JSON格式：
{{
    "market_size": "市场规模",
    "growth_rate": "增长率",
    "trends": ["趋势1", "趋势2"],
    "opportunities": ["机会"],
    "threats": ["威胁"],
    "key_players": ["主要玩家"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"market": content}

    def analyze_competitor(self, competitor: str, your_product: str) -> Dict:
        """分析竞品"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请分析竞品{competitor}，对比{your_product}：

请返回JSON格式：
{{
    "competitor_strengths": ["优势"],
    "competitor_weaknesses": ["劣势"],
    "your_advantages": ["你的优势"],
    "differentiation": ["差异化点"],
    "threat_level": "威胁程度",
    "recommendations": ["建议"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"competitor": content}

    def generate_pitch_deck(self, startup_info: Dict) -> Dict:
        """生成融资PPT"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        info_text = json.dumps(startup_info, ensure_ascii=False)

        prompt = f"""请根据以下信息生成融资PPT内容：

{info_text}

请返回JSON格式：
{{
    "slides": [
        {{"title": "标题", "content": "内容", "key_points": ["要点"]}}
    ],
    "talking_points": ["演讲要点"]
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=2000
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"pitch": content}

    def calculate_unit_economics(self, data: Dict) -> Dict:
        """计算单位经济"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        data_text = json.dumps(data, ensure_ascii=False)

        prompt = f"""请计算以下业务的单位经济：

{data_text}

请返回JSON格式：
{{
    "cac": "获客成本",
    "ltv": "客户终身价值",
    "ltv_cac_ratio": "LTV/CAC比率",
    "payback_period": "回收期",
    "gross_margin": "毛利率",
    "assessment": "评估"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=300
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"economics": content}

    def generate_growth_strategy(self, business_type: str, current_stage: str) -> Dict:
        """生成增长策略"""
        if not self.client:
            return {"error": "LLM客户端未配置"}

        prompt = f"""请为{current_stage}阶段的{business_type}生成增长策略：

请返回JSON格式：
{{
    "short_term": ["短期策略"],
    "long_term": ["长期策略"],
    "channels": ["增长渠道"],
    "metrics": ["关键指标"],
    "budget_allocation": "预算分配建议"
}}"""

        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )

        try:
            content = response.choices[0].message.content
            import re
            json_match = re.search(r'\{.*\}', content, re.DOTALL)
            if json_match:
                return json.loads(json_match.group())
        except:
            pass

        return {"strategy": content}


def create_tools(**kwargs) -> AIBusinessTools:
    """创建商业工具"""
    return AIBusinessTools(**kwargs)


if __name__ == "__main__":
    tools = create_tools()

    print("AI Business Tools")
    print()

    # 测试
    market = tools.analyze_market("AI软件", "中国")
    print(json.dumps(market, ensure_ascii=False, indent=2))
