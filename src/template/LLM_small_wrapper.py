from langchain.llms.base import LLM
from typing import Optional, List, Mapping, Any
import requests
import json

class SmallLLM(LLM):

    def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
        headers = {
            'Authorization': 'Bearer YOUR_AUTH',
            'Token-id': 'YOUR_TOKEN_ID',
            'Token-key': 'YOUR_TOKEN_KEY',
            'Content-Type': 'application/json',
        }

        json_data = {
            "model": "vnptai_hackathon_small",
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 1.0,
            "top_p": 1.0,
            "top_k": 20,
            "n": 1,
            "max_completion_tokens": 100,
        }

        response = requests.post(
            "https://api.idg.vnpt.vn/data-service/vnptai-hackathon-small",
            headers=headers,
            json=json_data
        )

        try:
            return response.json()["choices"][0]["message"]["content"]
        except Exception:
            return str(response.json())

    @property
    def _identifying_params(self) -> Mapping[str, Any]:
        return {}

    @property
    def _llm_type(self) -> str:
        return "vnpt_ai_small"