# Notes Toán rời rạc

## A. TỔ HỢP — BÀI TOÁN ĐẾM

### A1) Nguyên lý cơ bản (không hiển nhiên, hay cài bẫy)
- **Nguyên lý nhân/cộng (phiên bản điều kiện)**: nếu phép chọn theo bước với số cách bước i phụ thuộc lịch sử → dùng *nhân có điều kiện*; nếu các trường hợp giao nhau → không dùng cộng trực tiếp.
- **Nguyên lý đối xứng**: đếm cấu hình “không phân biệt” thường quy về đếm có nhãn rồi chia cho số hoán vị *khi và chỉ khi* mọi lớp tương đương có cùng kích thước (tác động nhóm tự do).
- **Đếm bù**: tốt khi điều kiện “ít nhất một”/“tồn tại” → đếm tổng − đếm “không có”; nhớ kiểm tra chồng lấp.

### A2) Nguyên lý bù trừ (PIE)
- **PIE cho hữu hạn**: \|⋃A_i\| = Σ\|A_i\| − Σ\|A_i∩A_j\| + … + (−1)^{k+1}Σ\|A_{i1}∩…∩A_{ik}\| + …  
- **PIE xác suất**: P(⋃A_i) = ΣP(A_i) − ΣP(A_i∩A_j)+… (không cần độc lập).
- **Số phần tử có đúng t tính chất**: nếu N(S) = số đối tượng có ít nhất các tính chất trong S, thì  
  N_exact(t)= Σ_{|S|=t} N(S) − (t+1)Σ_{|S|=t+1}N(S)+… (dạng hệ số nhị thức).
- **Derangements** (không điểm bất động): !n = n! Σ_{k=0..n} (−1)^k / k! ; gần đúng !n ≈ n!/e.

### A3) Quy về bài toán đơn giản (Stirling, phân hoạch, vòng)
- **Hoán vị vòng (chu trình)**: số vòng của n phần tử: (n−1)! ; nếu tính cả quay và lật (vòng không hướng) với n>2: (n−1)!/2.
- **Stirling loại 2** (phân hoạch n phần tử vào k nhóm không rỗng, nhóm không nhãn):  
  S(n,k)=S(n−1,k−1)+k·S(n−1,k), với S(0,0)=1.
- **Số onto (surjection)** từ [n]→[k]: k!·S(n,k) = Σ_{i=0..k} (−1)^i C(k,i)(k−i)^n.
- **Stirling loại 1 (không dấu)** (số hoán vị n phần tử có k chu trình):  
  c(n,k)=c(n−1,k−1)+(n−1)c(n−1,k), c(0,0)=1.
- **Phân hoạch số nguyên** p(n): hàm sinh Π_{i≥1} 1/(1−x^i); truy hồi Euler:  
  p(n)=Σ_{k≠0} (−1)^{k+1} p(n−k(3k−1)/2).

### A4) Công thức truy hồi (khuôn giải nhanh)
- **Truy hồi tuyến tính hệ số hằng**: a_n = Σ_{i=1..d} c_i a_{n−i} → nghiệm dạng Σ P_j(n) r_j^n (r_j là nghiệm đặc trưng, bội m → nhân n^{0..m−1}).
- **Fibonacci chuẩn**: F_{n}=F_{n−1}+F_{n−2}, F_0=0,F_1=1; hệ quả: Σ_{i=0..n}F_i = F_{n+2}−1.
- **Nguyên lý “đếm theo phần tử cuối/đầu”**: cố định vị trí đặc biệt để cắt bài (đặt vật/đánh dấu) → suy ra truy hồi + điều kiện biên.

### A5) Hàm sinh (Generating Functions) — công thức dùng trực tiếp
- **OGF**: A(x)=Σ_{n≥0} a_n x^n; tích tương ứng *chập* (convolution):  
  [x^n]A(x)B(x)=Σ_{k=0..n} a_k b_{n−k}.
- **Chuỗi hình học**: 1/(1−x)=Σ x^n; 1/(1−x)^k = Σ C(n+k−1,k−1) x^n.
- **Dịch chỉ số**: Σ_{n≥m} a_{n−m} x^n = x^m A(x).
- **Nhân bởi n**: nếu A(x)=Σ a_n x^n thì xA'(x)=Σ n a_n x^n.
- **Đếm nghiệm nguyên không âm**: x_1+…+x_k=n ⇒ # = C(n+k−1,k−1); ràng buộc x_i≥L_i ⇒ đổi biến.
- **Đếm nghiệm nguyên bị chặn**: 0≤x_i≤u_i, Σx_i=n ⇒ hệ số của x^n trong Π (1−x^{u_i+1})/(1−x).
- **EGF cho gán nhãn**: A(x)=Σ a_n x^n/n!; tích EGF tương ứng *phân hoạch nhãn* (đặc biệt cho cấu trúc tổ hợp gán nhãn).

### A6) Liệt kê (Enumeration) — Burnside/Pólya (nâng cao, hay thi)
- **Burnside**: số quỹ đạo = (1/|G|) Σ_{g∈G} |Fix(g)| (đếm cấu hình modulo đối xứng).
- **Pólya**: số tô màu (m màu) của cấu trúc có cycle index Z_G: thay mỗi biến a_i bằng m và tính theo chu kỳ; cần đúng Z_G theo nhóm tác động.

---

## B. TỔ HỢP — BÀI TOÁN TỒN TẠI

### B1) Phản chứng (khung hay dùng)
- **Phản chứng bằng cực trị**: giả sử phản ví dụ tối tiểu/tối đại theo tham số (n, số cạnh, …) → suy ra mâu thuẫn bằng thao tác “giảm” cấu hình.
- **Double counting để phản chứng**: cùng một đại lượng đếm theo hai cách, ép bất đẳng thức không thể.

### B2) Nguyên lý Dirichlet (Pigeonhole) — bản mạnh
- **Bản mạnh**: phân N vật vào k hộp ⇒ có hộp chứa ≥ ⌈N/k⌉ vật.
- **Dạng sai phân**: nếu có k+1 số nguyên thì tồn tại hai số có cùng phần dư mod k ⇒ chênh lệch chia hết cho k.
- **Dạng liên tục**: chia đoạn/miền thành k phần bằng nhau → có hai điểm rơi cùng phần (tạo khoảng cách nhỏ).

### B3) Hệ đại diện phân biệt (SDR) — Hall
- **Định lý Hall**: họ tập {A_i} có SDR ⇔ ∀S⊆I, |⋃_{i∈S} A_i| ≥ |S|.
- **Corollary ghép cặp trong song đồ thị**: song đồ thị có matching phủ U ⇔ ∀S⊆U, |N(S)|≥|S|.
- **Dạng đều (regular bipartite)**: song đồ thị d-đều ⇒ tồn tại perfect matching (áp dụng Hall).

### B4) Ramsey (mốc kết quả để suy luận nhanh)
- **Ramsey 2-màu**: tồn tại R(s,t) sao cho mọi tô cạnh K_n (n≥R) có K_s đỏ hoặc K_t xanh.
- **Cận truy hồi**: R(s,t) ≤ R(s−1,t)+R(s,t−1), với R(1,t)=1.
- **Mốc nhỏ**: R(3,3)=6; hệ quả: mọi K_6 tô 2 màu có tam giác đơn sắc.

---

## C. TỔ HỢP — BÀI TOÁN LIỆT KÊ & TỐI ƯU (thuật toán)

### C1) Độ phức tạp & khuôn đánh giá
- **Big-O/Θ/Ω**: f=O(g) nếu ∃c,n0: f(n)≤c g(n) ∀n≥n0; f=Θ(g) nếu O và Ω đồng thời.
- **Cận trên quay lui**: T(n)=b·T(n−1)+… ⇒ thường O(b^n); dùng “branching factor” theo trường hợp để chặt hơn.
- **Nguyên tắc cắt tỉa**: nếu bound hiện tại ≥ best ⇒ bỏ nhánh; cần bound *admissible* (không đánh giá thấp tối ưu).

### C2) Sinh cấu hình (generation)
- **Gray code cho nhị phân**: i ↦ i ⊕ (i>>1) (hai cấu hình kề khác 1 bit).
- **Sinh tổ hợp k phần tử**: next-combination theo tăng từ phải sang trái (lexicographic), đảm bảo không lặp.

### C3) Quay lui (backtracking)
- **Điều kiện hợp lệ từng phần**: thiết kế predicate P(partial) sao cho nếu P sai thì mọi mở rộng đều sai (pruning đúng).
- **Ràng buộc thứ tự**: áp đặt x_1≤x_2≤… để loại hoán vị tương đương (giảm bội số lời giải).

### C4) Nhánh cận (Branch & Bound) — TSP
- **Lower bound TSP (gợi ý công thức)**: LB ≥ (1/2) Σ_{v} (min1(v)+min2(v)) cho đồ thị vô hướng (hai cạnh nhỏ nhất kề mỗi đỉnh).
- **Cắt bằng 1-tree/MST**: LB từ MST trên n−1 đỉnh + 2 cạnh nhỏ nhất nối đỉnh còn lại (phiên bản Held–Karp đơn giản).

### C5) Lập lịch 2 máy (Johnson)
- **Johnson (2-machine flow shop)**: với job j có (a_j,b_j).  
  Chia: S1={a_j≤b_j} sắp tăng theo a_j; S2={a_j>b_j} sắp giảm theo b_j; ghép S1 rồi S2 ⇒ tối ưu makespan.

---

## D. LÝ THUYẾT ĐỒ THỊ — NỀN TẢNG & HỆ QUẢ

### D1) Đếm bậc & hệ quả
- **Bắt tay**: Σ_v deg(v)=2m (đồ thị vô hướng); hệ quả: số đỉnh bậc lẻ là chẵn.
- **Đồ thị có hướng**: Σ outdeg(v)=Σ indeg(v)=m.

### D2) Tính liên thông & cây
- **Đặc trưng cây (tương đương)**: liên thông + m=n−1 ⇔ không chu trình + m=n−1 ⇔ liên thông và bỏ bất kỳ cạnh nào sẽ rời.
- **Số cạnh tối đa không có chu trình (forest)**: m ≤ n−c (c là số thành phần liên thông).
- **Cây khung**: mọi đồ thị liên thông có cây khung; cây khung luôn có n−1 cạnh.

---

## E. BIỂU DIỄN ĐỒ THỊ TRÊN MÁY TÍNH (dùng cho MCQ)
- **Ma trận kề**: kiểm tra kề O(1), duyệt láng giềng O(n); phù hợp đồ thị dày.
- **Danh sách kề**: duyệt láng giềng O(deg), tổng O(n+m); phù hợp đồ thị thưa.
- **Ma trận liên thuộc**: tiện cho bài toán dòng/cắt; kích thước n×m.

---

## F. THUẬT TOÁN TÌM KIẾM & ỨNG DỤNG

### F1) DFS/BFS — hệ quả chuẩn
- **BFS (đồ thị vô hướng/không trọng số)**: cho khoảng cách ngắn nhất theo số cạnh; đúng khi mọi cạnh trọng số = 1.
- **DFS thời gian vào/ra**: cạnh ngược (back edge) ⇔ tồn tại chu trình trong đồ thị có hướng (dựa trên trạng thái thăm).
- **Topo sort**: DAG ⇔ có thứ tự topo; thuật toán Kahn/DFS cho thứ tự topo.

---

## G. ĐỒ THỊ EULER & HAMILTON

### G1) Euler
- **Chu trình Euler (vô hướng)**: đồ thị liên thông (bỏ đỉnh cô lập) và mọi đỉnh có bậc chẵn.
- **Đường đi Euler (vô hướng)**: liên thông và có đúng 0 hoặc 2 đỉnh bậc lẻ (2 đỉnh lẻ là hai đầu mút).
- **Có hướng**: chu trình Euler ⇔ mạnh liên thông theo cạnh có bậc dương và ∀v indeg(v)=outdeg(v); đường đi Euler: đúng 2 đỉnh lệch ±1, còn lại cân bằng.

### G2) Hamilton (điều kiện đủ hay dùng)
- **Dirac**: n≥3, δ(G)≥n/2 ⇒ Hamilton cycle.
- **Ore**: n≥3, ∀u≠v không kề nhau: deg(u)+deg(v)≥n ⇒ Hamilton cycle.

---

## H. CÂY, CÂY KHUNG & CHU TRÌNH CƠ BẢN

### H1) Chu trình cơ bản theo cây khung
- **Thêm 1 cạnh ngoài cây** vào cây khung ⇒ tạo đúng 1 chu trình cơ bản.
- **Số cạnh ngoài cây**: m−(n−1) = m−n+1 (đồ thị liên thông) = số chu trình độc lập theo không gian chu trình.

### H2) MST — điều kiện cắt/chu trình
- **Cut property**: với mọi lát cắt, cạnh nhẹ nhất băng cắt (nếu duy nhất) thuộc mọi MST.
- **Cycle property**: trong mọi chu trình, cạnh nặng nhất (nếu duy nhất) không thuộc bất kỳ MST.
- **Kruskal**: đúng với trọng số bất kỳ; sắp cạnh tăng dần + DSU; O(m log m).
- **Prim**: dùng heap; O(m log n) (danh sách kề).

---

## I. ĐƯỜNG ĐI NGẮN NHẤT

### I1) Dijkstra & điều kiện
- **Dijkstra**: đúng khi mọi trọng số cạnh **không âm**; sau khi “chốt” đỉnh u, dist[u] là tối ưu.
- **DAG shortest path**: nếu đồ thị có hướng không chu trình ⇒ topo order + relax một lượt, đúng cả khi có trọng số âm (miễn không có chu trình).
- **All-pairs**: Floyd–Warshall O(n^3), cập nhật: d_{ij} = min(d_{ij}, d_{ik}+d_{kj}); phát hiện chu trình âm nếu d_{ii}<0.
- **Bellman–Ford (mốc)**: xử lý cạnh âm; phát hiện chu trình âm sau n−1 lần relax còn cải thiện.

---

## J. LUỒNG CỰC ĐẠI TRONG MẠNG

### J1) Định lý & cấu trúc
- **Max-Flow Min-Cut**: giá trị luồng cực đại = dung lượng lát cắt nhỏ nhất.
- **Đồ thị dư (residual)**: cạnh xuôi còn c_f(u,v)=c(u,v)−f(u,v); cạnh ngược có c_f(v,u)=f(u,v); đường tăng luồng phải theo c_f>0.
- **Bảo toàn luồng**: ∀v≠s,t: Σ_in f = Σ_out f; ràng buộc 0≤f≤c.

### J2) Thuật toán & độ phức tạp
- **Ford–Fulkerson**: đúng nếu năng lực nguyên và chọn đường tăng bất kỳ ⇒ kết thúc; có thể không kết thúc với số thực.
- **Edmonds–Karp** (BFS đường tăng ngắn nhất theo số cạnh): O(VE^2).
- **Dinic** (mốc): O(EV^2) tổng quát; tốt hơn trên mạng đơn vị/bipartite.

### J3) Ứng dụng tổ hợp
- **Matching song đồ thị**: ghép cực đại = luồng cực đại trên mạng nguồn→U (cap 1), U→V (cap 1 nếu có cạnh), V→đích (cap 1).
- **Min vertex cover (Kőnig)**: trong song đồ thị: |MVC|=|maximum matching|.
- **Phân rã luồng nguyên**: luồng nguyên có thể tách thành tổng các đường s→t và chu trình (hữu hạn).

---

## K. HÀM ĐẠI SỐ LOGIC (Boolean) — BIỂU DIỄN & TỐI THIỂU

### K1) Dạng chuẩn (DNF/CNF) & chuyển đổi
- **De Morgan**: ¬(A∧B)=¬A∨¬B; ¬(A∨B)=¬A∧¬B (mấu chốt khi đổi CNF↔DNF).
- **Hấp thụ**: A∨(A∧B)=A; A∧(A∨B)=A.
- **Phân phối**: A∧(B∨C)=(A∧B)∨(A∧C); A∨(B∧C)=(A∨B)∧(A∨C) (dùng để đưa về CNF/DNF, nhưng có thể nổ kích thước).
- **Consensus (hệ quả rút gọn)**: (x∨A)∧(¬x∨B) ⇒ (A∨B) là hệ quả (dùng suy diễn/giảm CNF).

### K2) Dạng tuyển chuẩn tắc (DNF chuẩn)
- **Minterm/Maxterm**: DNF chuẩn là tổng các minterm ứng với các hàng giá trị 1; CNF chuẩn là tích các maxterm ứng với các hàng giá trị 0.
- **Rút gọn DNF bằng gộp**: hai minterm khác đúng 1 biến (x và ¬x) ⇒ gộp thành implicant bỏ biến đó (điều kiện: còn lại giống hệt).

### K3) Tối thiểu hoá (Quine–McCluskey / Karnaugh / sơ đồ)
- **Luật gộp 2^k**: nhóm 2^k ô 1 kề nhau (K-map, có cuộn biên) ⇒ khử k biến; nhóm càng lớn càng tốt nhưng phải phủ hết 1.
- **Prime implicant**: implicant không thể gộp lớn hơn; nghiệm tối thiểu phải chọn tập prime implicant phủ mọi minterm 1.
- **Essential prime implicant**: prime implicant phủ một minterm mà không prime nào khác phủ ⇒ bắt buộc chọn.
- **McCluskey**: sắp theo số bit 1, ghép cặp khác 1 bit → tạo “–”; lặp đến khi không ghép được; phần còn lại là prime implicant.

