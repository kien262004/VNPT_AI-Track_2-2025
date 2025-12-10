import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


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
                timeout=15
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
        
from typing import Literal
from pydantic import BaseModel, Field
import json

class RouteQuery(BaseModel):
    """Route a user query to the appropriate data source."""

    datasource: Literal["medical_knowledge", "store_database"] = Field(
        ...,
        description="Route to store_database for sales-related queries or medical_knowledge for medical queries",
    )
    reasoning: str = Field(..., description="Brief for the decision")

ROUTER_SYSTEM_PROMPT = """
Bạn là bộ định tuyến câu hỏi (router). Hãy phân loại câu hỏi người dùng thành đúng 1 trong 5 loại sau, và trả về JSON hợp lệ theo format bên dưới.

Các loại (datasource):

1. "Restricted_Questions": câu hỏi không được phép trả lời (nhạy cảm, chính trị, kích động, xuyên tạc, ảnh hưởng tiêu cực).

2. "Mandatory_Accuracy_Questions": yêu cầu độ chính xác tuyệt đối (Lịch sử, Chính trị, Pháp luật, Khoa học). Không suy đoán, không sáng tạo, trả lời theo nguồn tin đáng tin cậy.

3. "Long_Text_Questions": có đoạn văn dài > 50 từ.

4. "Math_Logical_Reasoning": toán học, tính toán, phương trình, logic, giải đố, suy luận.

5. "Various_Domain": câu hỏi đa lĩnh vực, bao gồm nhiều lĩnh vực.

Quy tắc phân loại:
- Ưu tiên Restricted_Questions nếu có yếu tố nhạy cảm.
- Nếu có yếu tố chính xác cao (lịch sử/chính trị) → Mandatory_Accuracy_Questions.
- Nếu có văn bản dài > 50 từ → Long_Text_Questions.
- Nếu liên quan tính toán/logic → Math_Logical_Reasoning.

Output JSON:

{
  "datasource": "Tên loại",
  "reasoning": "Giải thích ngắn gọn"
}

"""
ROUTER_HUMAN_PROMPT = "User query: {question}"


if __name__ == "__main__":
    
    llm = get_llm(type="large_vnpt", cfg={"response_format": {"type": "json_object"}})
    prompt = ChatPromptTemplate.from_messages(
        [
            SystemMessage(content=ROUTER_SYSTEM_PROMPT),
            HumanMessage(content=ROUTER_HUMAN_PROMPT),
        ]
    )
    chain = prompt | llm
    data = chain.invoke({"question": "Câu hỏi sau có 500 từ. Đoạn thông tin:\n[1] Tiêu đề: Khỉ thí nghiệm\nNội dung: Khỉ thí nghiệm là thuật ngữ chỉ về các loài linh trưởng (trừ con người), thông thường là các loài khỉ được sử dụng trong thí nghiệm y khoa (NHPs). Khỉ bao gồm các loài khỉ thực sự và các loài khỉ lớn (Ape) được sử dụng cho các mục đích thí nghiệm khoa học, nhất là trong y học. Xuất phát từ sự tương đồng của về cấu trúc sinh học giữa các loài khỉ và người do đó chúng thường được nuôi để làm vật thí nghiệm liên quan đến y khoa, trên cơ sở đó sẽ nhân rộng ra cho con người.\nCó 22 loài khỉ đuôi dài, trong đó một số được sử dụng thường xuyên trong các thí nghiệm khoa học. Khỉ vàng là nguồn nguyên liệu đầu để sản xuất hàng chục triệu liều văcxin bại liệt mỗi năm, góp phần vào việc thanh toán hoàn toàn bệnh bại liệt tại Việt Nam vào những năm 2000 Được sử dụng trong sản xuất vacxin chống bệnh bại liệt trẻ em, làm vật mẫu, đối tượng nghiên cứu khoa học. Khỉ vàng được lựa chọn là đối tượng nghiên cứu của các đề tài khoa học cũng như kiểm định chất lượng, thử nghiệm tiền lâm sàng nhiều sản phẩm sinh học và văcxin.\n\nI. Tổng quan\n\nCác loài linh trưởng nói chung và khỉ nói riêng được sử dụng rộng rãi trong thực nghiệm y học, đặc biệt chúng gắn liền với khoa học về thần kinh và một số bệnh lý. Do đặc tính sinh lý của chúng liên quan gần với con người, nên chúng có thể chia sẻ một số bệnh truyền nhiễm với con người. Theo thống kê y học, khỉ cũng mắc các bệnh thường có ở người như: virus herpes, thủy đậu (varicella), dại, sốt xuất huyết, bại liệt, cúm, sởi, viêm gan A, viêm gan B. Trong một số trường hợp, ký sinh trùng Plasmodium knowlesi gây bệnh sốt rét trên khỉ cũng có thể gây nhiễm sốt rét trên người, một số trường hợp đã được báo cáo trên người, thậm chí gây sốt rét ác tính và tử vong. Trong giới động vật, khỉ là loài gần gũi với con người nhất. Do cơ thể gần tương đồng với cơ thể người nên các loài khỉ, đặc biệt là khỉ nuôi dài có nguồn gốc gây nuôi sinh sản có tác dụng tốt cho công tác nghiên cứu y học. Nhiều cơ sở y học hàng đầu trên thế giới ở Mỹ, Anh, Pháp đều sử dụng khỉ đuôi dài làm vật thí nghiệm các loại vaccine trước khi sử dụng phổ biến ở người.\nCơ thể khỉ gần giống người, nên trong y học khỉ là đối tượng để nghiên cứu bệnh học, y học thực nghiệm, từ đó để có biện pháp giải quyết chữa bệnh cho người. Người ta đã nghiên cứu nhiều bộ phận cơ thể của khỉ để ghép cho người như thận, tim, gan. Tuy nhiên, bệnh nhân được ghép cũng không sống được lâu. Trong sản xuất vacxin chống các bệnh vi rút, người ta cũng dùng một số bộ phận của khỉ. Ngoài ra, để phục vụ cho công việc nghiên cứu và sản xuất vắc-xin phòng các bệnh cho con người, hàng ngày có những con khỉ đã âm thầm bị hiến thận cho những công việc. Vì bản thân tế bào thận Khỉ không mang bất kỳ tác nhân truyền nhiễm lạ, hoặc nguy cơ gây bệnh hiểm nghèo cho con người. Chẳng hạn, khi tiến hành bào chế vắc-xin Sabin phòng bệnh bại liệt, hoặc vắc–xin phòng dịch cúm H5N1, người ta đã sử dụng tế bào thận khỉ vàng để làm công việc đó\n\nII. Quy trình\n\nVì cơ địa khỉ vàng gần giống với con người, nên trong những năm gần đây khỉ vàng lại là vật thí nghiệm để thử phản ứng các loại vắc-xin H5N1, H1N1 trước khi tiêm vào con người. Khỉ ở được chọn là giống khỉ lông vàng đuôi ngắn, chúng có cơ thể tương đối sạch, ít bị nhiễm các mầm bệnh hơn các loài khỉ khác. Mỗi lần thử nghiệm có từ 30 đến 50 con khỉ khoảng 1 năm tuổi, chúng được tiêm, được uống, được chăm sóc, nuôi nhốt theo dõi hết sức cẩn thận trong quá trình nghiên cứu.\nKhỉ được chọn ra để chiết vắc-xin thường là khỉ con một năm rưỡi đến hai năm tuổi, có trọng lượng khoảng 2,5 kg (khỉ trưởng thành nặng trung bình từ 6–7 kg, có con nặng tới 13 kg). Những chú khỉ đủ tiêu chuẩn được lựa chọn tiến hành nghiên cứu là những chú khỉ trong độ tuổi 1,5-2 năm tuổi, cân nặng từ 1,5–2 kg và thường chọn khỉ đực để nghiên cứu vì khỉ cái còn dùng để sinh sản. Những con khỉ được lựa chọn sẽ được nuôi cách ly và kiểm tra xác nhận không có mầm bệnh, đưa về Trung tâm Nghiên cứu, sản xuất văcxin và sinh phẩm y tế (POLYVAC).\nSau đó, những chuyên gia tại đây sẽ phẫu thuật lấy thận, tách các tế bào thận riêng rẽ để nuôi cấy trên các chai thủy tinh bằng môi trường phát triển, khi tế bào đã phát triển phủ kín một lớp trên bề mặt chai sẽ được gây nhiễm chủng virút polio đã giảm độc lực. Chủng virút này nhân lên trên tế bào, trưởng thành và giải phóng ra khỏi tế bào tạo thành hỗn dịch văcxin bại liệt bán thành phẩm đơn type. Khi sản xuất văcxin thành phẩm sẽ tiến hành phối trộn ba type virút, bổ sung chất bảo quản, lọc vô trùng và đóng lọ để trở thành văcxin thành phẩm. Mỗi con khỉ chiết được gần một triệu liều vắc-xin giúp trẻ em thoát khỏi nhiều căn bệnh hiểm nghèo.\n\nIII. Nhân nuôi\n\nLoài được nuôi sinh sản nhiều nhất ở Việt Nam là khỉ đuôi dài. Tại Việt Nam cũng như một số nước trên thế giới, mặc dù nằm trong nhóm các loài nguy cấp với số lượng ít trong tự nhiên, khỉ đuôi dài lại có khả năng sinh sản rất tốt trong điều kiện gây nuôi. Ở các tỉnh phía nam Việt Nam, khỉ đuôi dài đã được gây nuôi sinh sản thành công tại một số trại gây nuôi động vật hoang dã với số lượng sinh sản hàng nghìn cá thể mỗi năm. Với tốc độ sinh sản tốt (2 lứa/3 năm), khỉ đuôi dài đã góp phần đa dạng hóa các loại hình sản xuất nông nghiệp, đem lại nguồn thu khoảng 3-4 triệu USD/năm cho kinh tế đất nước, tạo ra công ăn việc làm cho người lao động. Một quần thể khỉ mặt đỏ lông nâu sinh sôi nảy nở trong các khu đầm lầy của Florida, đặc biệt là tại Khu vườn quốc gia Silver. Khỉ được đưa đến phong thí nghiệm sinh học đặt ở đây từ năm 1938. Sáu mươi sáu năm sau (1992) trận bão khủng khiếp mang tên Andrew, gây thiệt hại lớn về người và của, đã phá hủy nghiêm trọng các phòng thí nghiệm. Đàn khỉ nâu bị xô đẩy ra tự nhiên Florida. Khỉ nâu là loài rất hung dữ, nên người ta đã khuyên du khách không nên tiếp xúc với chúng.\n\nIV. Ở Việt Nam\n\nKhỉ còn là vật thí nghiệm để sản xuất thuốc ở Việt Nam. Đảo khỉ ở Việt Nam là hòn đảo độc nhất vô nhị ở Việt Nam, nơi đây đã và đang nuôi dưỡng hàng ngàn con khỉ trong điều kiện bán hoang dã để phục vụ cho những thí nghiệm khoa học, sản xuất vaccin và nhiều sinh phẩm y tế phục vụ cho sự nghiệp cứu người chúng đang được nuôi rất nhiều ở đảo Rều thuộc Quảng Ninh với số lượng hơn 1.000 cá thể khỉ vàng được nuôi trên đảo Rều phục vụ sản xuất văcxin và các công trình nghiên cứu y học. Đây là những chú khỉ được nuôi để sản xuất văcxin bại liệt và phục vụ nhiều công trình nghiên cứu y học.\nNăm 1962, đảo Rều được Bộ Y tế đầu tư thành trại nuôi khỉ để nghiên cứu y học phục vụ sản xuất các loại văcxin phòng bại liệt, viêm gan A, thuốc phòng chống virút H5N1. Người ta dùng tế bào thận của loài khỉ vàng để điều chế các loại văcxin giúp khống chế nhiều bệnh tật truyền nhiễm nguy hiểm. Nhiều thế hệ khỉ đã góp công lớn cho sự nghiệp nghiên cứu, phát triển y học Việt Nam. Nhờ sự cống hiến của giống khỉ vàng, dịch bệnh bại liệt tại Việt Nam đã bị đẩy lùi. Khỉ vàng là nguồn nguyên liệu đầu để sản xuất hàng chục triệu liều văcxin bại liệt mỗi năm, góp phần vào việc thanh toán hoàn toàn bệnh bại liệt tại Việt Nam vào những năm 2000.\nCâu hỏi: Loài khỉ nào được sử dụng phổ biến nhất trong sản xuất vắc-xin bại liệt và các loại vắc-xin phòng virus H5N1 ở Việt Nam?"})
    print(data.content)