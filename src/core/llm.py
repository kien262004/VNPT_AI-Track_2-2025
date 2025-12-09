import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

from typing import Optional, List, Mapping, Any
import requests
import json

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_core.messages import (
    BaseMessage,
    HumanMessage,
    AIMessage,
    SystemMessage,
    ChatMessage,
)

from langchain_core.outputs import (
    ChatGeneration,
    ChatResult,
)

load_dotenv()

def get_llm(type: str = "google", temperature: float = 0.3):
    if type == "large_vnpt":
        return LargeLLM()
    if type == "small_vnpt":
        return SmallLLM()
    if type == "google":
        return ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=temperature,
            google_api_key=os.getenv("GOOGLE_API_KEY"),
        )
    


# class LargeLLM(LLM):
        

#     def _call(self, prompt: str, stop: Optional[List[str]] = None) -> str:
#         headers = {
#             'Authorization': os.getenv("AUTHORIZATION_VNPT_LARGE"),
#             'Token-id': os.getenv("TOKEN_ID_VNPT_LARGE"),
#             'Token-key': os.getenv("TOKEN_KEY_VNPT_LARGE"),
#             'Content-Type': 'application/json',
#         }

#         json_data = {
#             "model": "vnptai_hackathon_large",
#             "messages": [{"role": "user", "content": prompt}],
#             "temperature": 1.0,
#             "top_p": 1.0,
#             "top_k": 20,
#             "n": 1,
#             "max_completion_tokens": 100,
#         }

#         response = requests.post(
#             "https://api.idg.vnpt.vn/data-service/vnptai-hackathon-large",
#             headers=headers,
#             json=json_data
#         )

#         try:
#             return response.json()["choices"][0]["message"]["content"]
#         except Exception:
#             return str(response.json())

#     @property
#     def _identifying_params(self) -> Mapping[str, Any]:
#         return {}

#     @property
#     def _llm_type(self) -> str:
#         return "vnpt_ai"

class SmallLLM(BaseChatModel):
    
    temperature: float = 0.3
    top_p: float = 1.0
    top_k: int = 20
    max_tokens: int = 256
    
    def __init__(self, temperature: float = 0.3, top_p: float = 1.0, top_k: int = 20, max_tokens: int = 256) -> None:
        super().__init__()
        self.temperature = temperature
        self.top_p = top_p
        self.top_k = top_k
        self.max_tokens = max_tokens


    # ---- LangChain required properties ----
    @property
    def _llm_type(self) -> str:
        return "vnpt_ai"

    # ---- Core generate function ----
    def _generate(
        self,
        messages: List[BaseMessage],
        stop: Optional[List[str]] = None,
    ):
        headers = {
            "Authorization": f"Bearer {os.getenv('AUTHORIZATION_VNPT_SMALL')}",
            "Token-id": os.getenv("TOKEN_ID_VNPT_SMALL"),
            "Token-key": os.getenv("TOKEN_KEY_VNPT_SMALL"),
            "Content-Type": "application/json",
        }
        
        # Convert LangChain messages -> VNPT format
        payload_messages = []
        for m in messages:
            if isinstance(m, HumanMessage):
                payload_messages.append({"role": "user", "content": m.content})
            elif isinstance(m, AIMessage):
                payload_messages.append({"role": "assistant", "content": m.content})
            elif isinstance(m, SystemMessage):
                payload_messages.append({"role": "system", "content": m.content})
            elif isinstance(m, ChatMessage):
                payload_messages.append({"role": m.role, "content": m.content})

        json_data = {
            "model": "vnptai_hackathon_small",
            "messages": payload_messages,
            "temperature": self.temperature,
            "top_p": self.top_p,
            "top_k": self.top_k,
            "max_completion_tokens": self.max_tokens,
        }

        try:
            res = requests.post(
                "https://api.idg.vnpt.vn/data-service/v1/chat/completions/vnptai-hackathon-small",
                headers=headers,
                json=json_data,
                timeout=15
            ).json()
        except Exception as e:
            raise ValueError(f"VNPT API error: {e}")

        text = res["choices"][0]["message"]["content"]

        return ChatResult(
            generations=[ChatGeneration(message=AIMessage(content=text))]
        )

class LargeLLM(BaseChatModel):
    
    temperature: float = 0.3
    top_p: float = 1.0
    top_k: int = 20
    max_tokens: int = 256
    
    def __init__(self, temperature: float = 0.3, top_p: float = 1.0, top_k: int = 20, max_tokens: int = 256) -> None:
        super().__init__()
        self.temperature = temperature
        self.top_p = top_p
        self.top_k = top_k
        self.max_tokens = max_tokens


    # ---- LangChain required properties ----
    @property
    def _llm_type(self) -> str:
        return "vnpt_ai"

    # ---- Core generate function ----
    def _generate(
        self,
        messages: List[BaseMessage],
        stop: Optional[List[str]] = None,
    ):
        headers = {
            "Authorization": f"Bearer {os.getenv('AUTHORIZATION_VNPT_LARGE')}",
            "Token-id": os.getenv("TOKEN_ID_VNPT_LARGE"),
            "Token-key": os.getenv("TOKEN_KEY_VNPT_LARGE"),
            "Content-Type": "application/json",
        }
        
        # Convert LangChain messages -> VNPT format
        payload_messages = []
        for m in messages:
            if isinstance(m, HumanMessage):
                payload_messages.append({"role": "user", "content": m.content})
            elif isinstance(m, AIMessage):
                payload_messages.append({"role": "assistant", "content": m.content})
            elif isinstance(m, SystemMessage):
                payload_messages.append({"role": "system", "content": m.content})
            elif isinstance(m, ChatMessage):
                payload_messages.append({"role": m.role, "content": m.content})

        json_data = {
            "model": "vnptai_hackathon_large",
            "messages": payload_messages,
            "temperature": self.temperature,
            "top_p": self.top_p,
            "top_k": self.top_k,
            "max_completion_tokens": self.max_tokens,
        }

        try:
            res = requests.post(
                "https://api.idg.vnpt.vn/data-service/v1/chat/completions/vnptai-hackathon-large",
                headers=headers,
                json=json_data,
                timeout=15
            ).json()
        except Exception as e:
            raise ValueError(f"VNPT API error: {e}")

        text = res["choices"][0]["message"]["content"]

        return ChatResult(
            generations=[ChatGeneration(message=AIMessage(content=text))]
        )
    

if __name__ == "__main__":
    llm = get_llm("small_vnpt")
    print(llm.invoke("Hello, VNPT AI"))