# Notes Giải tích nhiều biến

## A. Hình học vectơ–ma trận trong R^2/R^3
- **Bất đẳng thức Cauchy–Schwarz**: |a·b| ≤ ||a|| ||b||; đẳng thức ⇔ a,b phụ thuộc tuyến tính.
- **Tích có hướng & hình học**: ||a×b|| = diện tích hình bình hành; a×b = 0 ⇔ a // b.
- **Đồng nhất thức Lagrange**: ||a×b||^2 = ||a||^2||b||^2 − (a·b)^2.
- **Tích hỗn tạp (thể tích)**: a·(b×c) = det[a b c]; |a·(b×c)| = thể tích hộp; =0 ⇔ a,b,c đồng phẳng.
- **Định thức & khả nghịch**: det(A)≠0 ⇔ A khả nghịch; det(AB)=detA·detB; det(A^{-1})=1/detA.
- **Công thức nghịch đảo nhanh**: (AB)^{-1}=B^{-1}A^{-1; } (A^T)^{-1}=(A^{-1})^T (khi khả nghịch).
- **Cramer (hệ vuông Ax=b)**: detA≠0 ⇒ nghiệm duy nhất; x_i = det(A_i)/det(A) (A_i thay cột i bằng b).
- **Mặt phẳng qua 3 điểm**: n=(b−a)×(c−a), phương trình n·(r−a)=0 (cần n≠0).
- **Khoảng cách điểm–mặt phẳng**: dist(p,Π)=|n·(p−a)|/||n|| (n là pháp tuyến Π).
- **Giao tuyến 2 mặt phẳng**: hướng d = n1×n2 (cần n1×n2≠0); tìm 1 điểm bằng giải hệ tuyến tính.

## B. Đường thẳng/đường cong tham số; động học; Kepler 2
- **Tiếp tuyến**: r(t) khả vi ⇒ vectơ tiếp tuyến tại t0 là r'(t0); pháp tuyến mặt phẳng quỹ đạo ⟂ r'×r'' (nếu khác 0).
- **Độ cong**: κ(t)=||r'×r''||/||r'||^3 (điều kiện: r'≠0).
- **Độ dài cung**: L=∫_a^b ||r'(t)|| dt (cần r' liên tục/khả tích).
- **Vận tốc, gia tốc**: v=r'(t), a=r''(t); phân rã a = v' T + v^2 κ N (khi v≠0, κ xác định).
- **Kepler II (định luật diện tích)**: lực trung tâm ⇒ mômen lực τ=r×F=0 ⇒ mômen động lượng h=r×v không đổi ⇒ tốc độ quét diện tích (1/2)||r×v|| không đổi.

## C. Vi phân riêng, xấp xỉ, tối ưu (không tuyến tính)
- **Tiếp xúc & xấp xỉ tuyến tính**: f C^1 gần a ⇒ f(a+h)=f(a)+∇f(a)·h+o(||h||); sai số nhỏ bậc 1.
- **Mặt phẳng tiếp tuyến (z=f(x,y))**: z≈f(a,b)+f_x(a,b)(x−a)+f_y(a,b)(y−b) (cần f C^1).
- **Đạo hàm theo hướng**: D_u f(a)=∇f(a)·u (u đơn vị, f C^1); max_{||u||=1} D_u f = ||∇f|| đạt tại u // ∇f.
- **Level curve/surface**: f=C ⇒ tại điểm regular (∇f≠0), ∇f vuông góc tiếp tuyến/tiếp diện.
- **Chain rule (Jacobian)**: y=g(u), z=f(y) ⇒ J_{z,u}=J_{z,y}·J_{y,u} (cần khả vi).
- **Vi phân toàn phần**: df = Σ f_{x_i} dx_i; xấp xỉ sai số |Δf−df|=o(||Δx||) khi f C^1.
- **Cực trị không ràng buộc (Hessian)**: ∇f(a)=0; H(a) dương xác định ⇒ cực tiểu; âm xác định ⇒ cực đại; không xác định ⇒ yên ngựa.
- **Kiểm tra dương xác định (2 biến)**: H = [[A,B],[B,C]]; A>0 & detH>0 ⇒ cực tiểu; A<0 & detH>0 ⇒ cực đại; detH<0 ⇒ yên ngựa.
- **Biên & vô cực**: tối ưu trên miền đóng–hữu hạn ⇒ xét điểm tới hạn + biên; miền không bị chặn ⇒ phải xét giới hạn “ra vô cực”.
- **Least squares (bình phương tối thiểu)**: min_x ||Ax−b||^2 ⇒ phương trình chuẩn A^T A x = A^T b (cần A có hạng cột đầy đủ để nghiệm duy nhất).
- **Lagrange multipliers (1 ràng buộc)**: min/max f s.t. g=0 ⇒ ∇f=λ∇g tại điểm regular (∇g≠0); luôn phải xét thêm biên/điểm không regular nếu có.
- **Nhiều ràng buộc**: ∇f=Σ λ_i ∇g_i với ma trận gradient ràng buộc hạng đầy đủ (điều kiện độc lập tuyến tính).
- **Hàm ẩn (Implicit Function)**: F(x,y,z)=0, F_z(a)≠0 ⇒ tồn tại z=z(x,y) C^1 gần a; z_x=−F_x/F_z, z_y=−F_y/F_z.
- **Jacobian & biến phụ thuộc**: nếu (u,v)↔(x,y) khả nghịch C^1, J=∂(x,y)/∂(u,v)≠0 ⇒ ∂(u,v)/∂(x,y)=1/J.

## D. Tích phân kép & tích phân đường trong mặt phẳng
- **Fubini/Tonelli (đổi thứ tự)**: ∬_D f dA = ∫(∫ f dy)dx = ∫(∫ f dx)dy nếu f liên tục/khả tích tuyệt đối trên D.
- **Đổi sang cực**: x=r cosθ, y=r sinθ; dA = r dr dθ; dùng khi D “tròn/đối xứng” và r≥0.
- **Đổi biến tổng quát (Jacobian)**: ∬_D f(x,y)dA = ∬_{D'} f(x(u,v),y(u,v)) |∂(x,y)/∂(u,v)| dudv; cần ánh xạ 1-1, C^1, J≠0.
- **Khối lượng & trọng tâm (mật độ δ)**: m= ∬ δ dA; x̄= (1/m) ∬ xδ dA, ȳ= (1/m) ∬ yδ dA (δ≥0, khả tích).
- **Moment quán tính**: I_x= ∬ y^2 δ dA, I_y= ∬ x^2 δ dA, I_O=I_x+I_y.
- **Tích phân đường công**: ∫_C F·dr = ∫_a^b F(r(t))·r'(t) dt (C trơn từng khúc).
- **Tích phân đường theo độ dài cung**: ∫_C g ds = ∫_a^b g(r(t)) ||r'(t)|| dt.
- **Trường thế & độc lập đường**: nếu F=∇φ trên miền ⇒ ∫_C F·dr = φ(B)−φ(A); ∮ F·dr=0.
- **Tiêu chuẩn bảo toàn (2D)**: F=(P,Q) C^1, miền đơn liên ⇒ (∂P/∂y = ∂Q/∂x) ⇔ F bảo toàn.
- **Green (dạng tuần hoàn)**: ∮_{∂D} P dx + Q dy = ∬_D (∂Q/∂x − ∂P/∂y) dA; D đơn, biên trơn từng khúc, hướng CCW.
- **Green (dạng thông lượng)**: ∮_{∂D} P dy − Q dx = ∬_D (∂P/∂x + ∂Q/∂y) dA (cùng điều kiện).
- **Thông lượng qua đường phẳng**: với F=(P,Q), thông lượng ra ngoài qua ∂D: ∮ (P dy − Q dx) (quy ước hướng dương CCW).

## E. Tích phân ba; tích phân mặt; định lý Gauss–Stokes
- **Đổi sang trụ**: (x,y,z)=(r cosθ, r sinθ, z); dV = r dr dθ dz.
- **Đổi sang cầu**: (x,y,z)=(ρ sinφ cosθ, ρ sinφ sinθ, ρ cosφ); dV = ρ^2 sinφ dρ dφ dθ.
- **Diện tích mặt (đồ thị z=g(x,y))**: dS = √(1+g_x^2+g_y^2) dA (g C^1).
- **Mặt tham số**: r(u,v) ⇒ dS = ||r_u×r_v|| dudv; pháp tuyến theo hướng chọn của r_u×r_v.
- **Thông lượng qua mặt (vector field)**: ∬_S F·n dS = ∬_{D} F(r(u,v))·(r_u×r_v) dudv (cần định hướng nhất quán).
- **Pháp tuyến đồ thị**: z=g(x,y) ⇒ n dS = (−g_x,−g_y,1) dA (hướng “lên”); đổi dấu nếu hướng “xuống”.
- **Divergence theorem (Gauss)**: ∬_{∂E} F·n dS = ∭_E (∇·F) dV; F C^1, E bị chặn, ∂E trơn từng khúc, n hướng ra ngoài.
- **Stokes**: ∮_{∂S} F·dr = ∬_S (∇×F)·n dS; F C^1; hướng biên theo quy tắc bàn tay phải với n.
- **Chuỗi “gradient–curl–div”**: ∇×(∇φ)=0; ∇·(∇×F)=0 (hữu ích để loại đáp án).
- **Thế trong R^3**: trên miền đơn liên, ∇×F=0 ⇒ tồn tại φ sao cho F=∇φ; dùng đường tích phân để dựng φ.
- **Vi phân chính xác (3D)**: ω=M dx+N dy+P dz là vi phân toàn phần ⇔ ∂M/∂y=∂N/∂x, ∂M/∂z=∂P/∂x, ∂N/∂z=∂P/∂y trên miền đơn liên.

## F. Tôpô; “điều kiện miền” & Maxwell
- **Đơn liên quan trọng**: điều kiện ∇×F=0 (hoặc ∂P/∂y=∂Q/∂x) chưa đủ nếu miền không đơn liên ⇒ có thể tồn tại vòng kín cho ∮ F·dr ≠0.
- **Ví dụ chuẩn (lỗ thủng)**: F=(−y/(x^2+y^2), x/(x^2+y^2)) có curl=0 trên R^2\{0} nhưng ∮_C F·dr = 2π quanh gốc.
- **Maxwell (dạng vi phân)**: ∇·E=ρ/ε0, ∇·B=0, ∇×E=−∂B/∂t, ∇×B=μ0 J+μ0ε0 ∂E/∂t.
- **Maxwell (dạng tích phân)**: Gauss(E): ∬ E·n dS=Q_enc/ε0; Gauss(B): ∬ B·n dS=0; Faraday: ∮ E·dr=−d/dt ∬ B·n dS; Ampère–Maxwell: ∮ B·dr=μ0 I_enc+μ0ε0 d/dt ∬ E·n dS (liên hệ Gauss/Stokes).
