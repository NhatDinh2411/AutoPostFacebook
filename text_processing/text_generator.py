from openai import OpenAI
import json
import os
from typing import List

def createAnalysis(detail_papers: List, OPENAI_KEY:str):
    client = OpenAI(api_key=OPENAI_KEY)
    detail_info = '\n\n'.join(detail_papers)
    response_text = client.responses.create(
        model="gpt-4o-mini-2024-07-18",
        instructions="Bạn là một nhà báo chuyên gia phân tích những thông tin dựa trên các bài báo.",
        input=f"Dựa trên thông tin tôi thu thập được hãy viết một bài phân tích ngắn dựa trên thông tin đó và cuối cùng tạo ra một câu prompt ngắn không vi phạm chính sách để sinh ảnh liên quan đến bài viết cho mô hình dall-e. Thông tin: {detail_info}",
        text={
            "format": {
                "type": "json_schema",
                "name": "math_reasoning",
                "schema": {
                    "type": "object",
                    "properties": {
                        "phân tích": {"type": "string"},
                        "prompt": {"type": "string"}
                    },
                    "required": ["phân tích", "prompt"],
                    "additionalProperties": False
                },
                "strict": True
            }
        }
    )
    output = json.loads(response_text.output_text)
    return output
