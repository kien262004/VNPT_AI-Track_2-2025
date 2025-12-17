from curses import raw
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from typing import Optional, List, Mapping, Any, Union
import requests
import json

from langchain_core.prompts import HumanMessagePromptTemplate, ChatPromptTemplate


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

from ..prompt_template import ROUTER_HUMAN_PROMPT, ROUTER_SYSTEM_PROMPT
from ..utils import count_word


load_dotenv()

def get_llm(type: str = "google", cfg: dict = None):
    if type == "large_vnpt":
        return LargeLLM(**cfg)
    if type == "small_vnpt":
        return SmallLLM(**cfg)
    if type == "google":
        return ChatGoogleGenerativeAI(
            model="gemini-2.5-flash",
            temperature=cfg.get("temperature", 0.3) if cfg else 0.3,
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
    max_tokens: int = 512
    response_format: Optional[dict] = None
    
    def __init__(self, temperature: float = 0.3, top_p: float = 1.0, top_k: int = 20, max_tokens: int = 512, response_format: Optional[dict] = None) -> None:
        super().__init__()
        self.temperature = temperature
        self.top_p = top_p
        self.top_k = top_k
        self.max_tokens = max_tokens
        self.response_format = response_format


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
                timeout=100
            ).json()
        except Exception as e:
            raise ValueError(f"VNPT API request error: {e}")

        # Debug nếu API trả về lỗi, không có 'choices'
        if "choices" not in res:
            raise ValueError(f"VNPT API logical error response: {res}")

        text = res["choices"][0]["message"]["content"]

        return ChatResult(
            generations=[ChatGeneration(message=AIMessage(content=text))]
        )

class LargeLLM(BaseChatModel):
    
    temperature: float = 0.3
    top_p: float = 1.0
    top_k: int = 20
    max_tokens: int = 256
    response_format: Optional[dict] = None
    
    def __init__(self, temperature: float = 0.3, top_p: float = 1.0, top_k: int = 20, max_tokens: int = 256, response_format=None) -> None:
        super().__init__()
        self.temperature = temperature
        self.top_p = top_p
        self.top_k = top_k
        self.max_tokens = max_tokens
        self.response_format = response_format
        


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
            "response_format": self.response_format
        }

        try:
            res = requests.post(
                "https://api.idg.vnpt.vn/data-service/v1/chat/completions/vnptai-hackathon-large",
                headers=headers,
                json=json_data,
                timeout=100
            ).json()
        except Exception as e:
            raise ValueError(f"VNPT API request error: {e}")

        # Debug nếu API trả về lỗi, không có 'choices'
        if "choices" not in res:
            raise ValueError(f"VNPT API logical error response: {res}")

        text = res["choices"][0]["message"]["content"]

        return ChatResult(
            generations=[ChatGeneration(message=AIMessage(content=text))]
        )
        

class Router:
    def __init__(self, type_llm="large_vnpt"):
        self.llm = get_llm(type=type_llm, cfg={"response_format": {"type": "json_object"}})
        self.prompt = self._get_prompt()
        self.chain = self.prompt | self.llm
        
    def _get_prompt(self):

        prompt = ChatPromptTemplate.from_messages(
            [
                SystemMessage(content=ROUTER_SYSTEM_PROMPT),
                HumanMessagePromptTemplate.from_template(ROUTER_HUMAN_PROMPT),
            ]
        )
        return prompt
        
    
    def route(self, question: str) -> dict:
        len_words = count_word(question)
        if len_words > 500:
            return {
                "datasource": "Long_Text_Questions",
                "reasoning": f"Văn bản có độ dài {len_words} từ, vượt quá 500 từ."
            }
        data = self.chain.invoke({"question": question})
        raw = data.content.encode('utf-8')
        try:
            res = json.loads(raw)
        except:
            res = {
                "datasource": "Math_Logical_Reasoning",
                "reasoning": f"Quá trình json load lỗi do không đúng định dạng json (thường do công thức toán học)"
            }
        return res

class VNPTAIEmbeddingClient:
    def __init__(
        self,
        model: str = "vnptai_hackathon_embedding",
        timeout: int = 100
    ):
        self.api_url = 'https://api.idg.vnpt.vn/data-service/vnptai-hackathon-embedding'
        self.model = model
        self.timeout = timeout

        self.headers = {
            "Authorization": f"Bearer {os.getenv('AUTHORIZATION_VNPT_EMBED')}",
            "Token-id": os.getenv('TOKEN_ID_VNPT_EMBED'),
            "Token-key": os.getenv('TOKEN_KEY_VNPT_EMBED'),
            "Content-Type": "application/json",
        }

    def embed(
        self,
        texts: Union[str, List[str]],
        normalize: bool = False
    ):
        """
        texts: string hoặc list[string]
        return: embedding vector hoặc list[vector]
        """
        if isinstance(texts, str):
            texts = [texts]
            single = True
        else:
            single = False

        payload = {
            "model": self.model,
            "input": texts,
            "encoding_format": "float"
        }

        response = requests.post(
            self.api_url,
            headers=self.headers,
            json=payload,
            timeout=self.timeout
        )

        response.raise_for_status()
        data = response.json()

        embeddings = [item["embedding"] for item in data["data"]]

        if normalize:
            embeddings = [self._normalize(vec) for vec in embeddings]

        return embeddings[0] if single else embeddings

    @staticmethod
    def _normalize(vec):
        norm = sum(v * v for v in vec) ** 0.5
        return [v / norm for v in vec] if norm > 0 else vec


if __name__ == "__main__":
    llm = VNPTAIEmbeddingClient()
    vec = llm.embed("Hello")
    norm = sum(v * v for v in vec) ** 0.5
    print(norm)
    