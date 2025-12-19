# Notes Sinh học

## 1. Di truyền quần thể & Định luật Hardy–Weinberg

### 1.1. Các khái niệm nền tảng
- **Alen (allele)**: Các trạng thái khác nhau của cùng một gen tại **một locus**.
- **Kiểu gen (genotype)**: Tổ hợp các alen trong cơ thể (Ví dụ: AA, Aa, aa).
- **Kiểu hình (phenotype)**: Sự biểu hiện ra bên ngoài có thể quan sát hoặc đo lường được.
- **Trạng thái kiểu gen**:
  - **Đồng hợp**: AA hoặc aa.
  - **Dị hợp**: Aa (xét ở cơ thể lưỡng bội, gen nằm trên nhiễm sắc thể thường).

### 1.2. Nguyên lý Hardy–Weinberg

#### 1.2.1. Công thức tần số alen và kiểu gen
- **Ký hiệu**:
  - Gọi **p = f(A)** là tần số alen trội.
  - Gọi **q = f(a)** là tần số alen lặn.
  - Với locus có 2 alen, ta luôn có: **p + q = 1**.
- **Trạng thái cân bằng Hardy–Weinberg (H–W)**:
  - Cấu trúc di truyền: **p² AA + 2pq Aa + q² aa = 1**.
  - Tần số kiểu gen: **f(AA) = p²**; **f(Aa) = 2pq**; **f(aa) = q²**.
- **Cách tính tần số alen từ tần số kiểu gen**:
  - **p = f(AA) + 1/2 f(Aa)**.
  - **q = f(aa) + 1/2 f(Aa)**.

#### 1.2.2. Điều kiện nghiệm đúng
Để quần thể đạt trạng thái cân bằng di truyền, cần thỏa mãn các điều kiện sau:
- Quần thể có **kích thước lớn** (để tránh tác động đáng kể của biến động di truyền/trôi dạt gen).
- Diễn ra **giao phối ngẫu nhiên** (random mating) đối với locus đang xét.
- **Không có đột biến** làm thay đổi hoặc tạo mới alen theo hướng đáng kể.
- **Không có di - nhập gen** (gene flow) làm thay đổi tần số alen của quần thể.
- **Không có chọn lọc tự nhiên** (tất cả các kiểu gen đều có sức sống và khả năng sinh sản tương đương nhau).

### 1.3. Các nhân tố tiến hóa phá vỡ cân bằng
Các yếu tố sau đây thường làm thay đổi tần số alen hoặc thành phần kiểu gen (thường gặp trong câu hỏi trắc nghiệm):
- **Chọn lọc tự nhiên**: Nhân tố định hướng tiến hóa, làm thay đổi tần số alen và kiểu gen dựa trên ưu thế thích nghi.
- **Giao phối không ngẫu nhiên**:
  - Bao gồm tự phối và giao phối cận huyết.
  - Hệ quả: Làm **giảm tỉ lệ dị hợp**, tăng tỉ lệ đồng hợp; tần số alen có thể không đổi ngay lập tức nhưng cấu trúc di truyền thay đổi.
- **Đột biến**: Tạo ra alen mới hoặc chuyển hóa qua lại giữa các alen. Tác động thường nhỏ ở từng thế hệ nhưng có ý nghĩa tích lũy lâu dài.
- **Di - nhập gen**: Sự trao đổi cá thể giữa các quần thể, làm “pha loãng” hoặc thay đổi nhanh chóng tần số alen.
- **Trôi dạt di truyền (Biến động di truyền)**: Tác động mạnh ở các quần thể có kích thước nhỏ (bao gồm hiệu ứng cổ chai và hiệu ứng kẻ sáng lập).

### 1.4. Kỹ năng giải bài tập và phân tích

#### 1.4.1. Phương pháp tính toán và suy luận từ kiểu hình
**Quy tắc chung:**
- Cần xác định rõ quan hệ **trội – lặn** (hoàn toàn, không hoàn toàn, hay đồng trội).
- Trong trường hợp **trội hoàn toàn**: Kiểu hình trội bao gồm **AA + Aa**; Kiểu hình lặn là **aa**.

**Bài toán bệnh/đột biến lặn trên NST thường (a gây bệnh):**
- Người mắc bệnh có kiểu gen **aa**, tần số = **q²**.
- Suy ra tần số alen: **q = √(q²)**; **p = 1 − q**.
- Tần số người mang gen bệnh nhưng không biểu hiện (carrier/dị hợp): **f(Aa) = 2pq**.
- Tần số kiểu hình bình thường (gồm AA và Aa): **1 − q²**.

**Bài toán bệnh trội trên NST thường (A gây bệnh):**
- Người bình thường có kiểu gen **aa**, tần số = **q²**.
- Suy ra tần số alen: **q = √(q²)**; **p = 1 − q**.
- Tần số kiểu hình bệnh (gồm AA và Aa): **1 − q² = p² + 2pq**.
- *Lưu ý*: Với bệnh trội hiếm gặp (p rất nhỏ), phần lớn người bệnh trong quần thể thường ở trạng thái **dị hợp (Aa)**.

**Khi đề bài cho tỉ lệ kiểu hình Trội (T) và Lặn (L):**
- Nếu trội hoàn toàn: **L = q²** → tính được q, p → suy ra cấu trúc **p², 2pq, q²**.
- Nếu trội không hoàn toàn hoặc đồng trội (thường có 3 kiểu hình riêng biệt): Tần số mỗi kiểu hình tương ứng trực tiếp với **p², 2pq, q²** theo định nghĩa của đề.

#### 1.4.2. Mẹo nhận dạng tình huống nhanh
- Nếu đề bài cho “Quần thể cân bằng H–W”: Áp dụng ngay tỉ lệ **p² : 2pq : q²**.
- Nếu đề cập “Giao phối không ngẫu nhiên / Cận huyết / Tự phối”: Chắc chắn **tỉ lệ dị hợp giảm**. Khi hỏi tần số alen, cần tìm thêm thông tin (không được tự ý suy ra p, q từ kiểu hình lặn như trong H–W).
- Nếu đề cập “Chọn lọc chống lại kiểu gen aa”: Sau quá trình chọn lọc, **q sẽ giảm**. Cần tính lại tần số kiểu gen dựa trên tổng số cá thể sống sót đã được chuẩn hóa.
- Nếu đề cập “Di nhập gen”: Tần số alen mới được tính bằng trung bình cộng có trọng số, dựa trên quy mô và mức độ đóng góp của nhóm nhập cư.
- Nếu đề cập “Đột biến A→a hoặc a→A”: Tần số p, q sẽ thay đổi theo chiều hướng đột biến (dựa trên tỉ lệ đột biến đề bài cung cấp).

---

## 2. Sinh học phân tử & Hóa sinh cơ bản

### 2.1. Cấu trúc và cơ chế di truyền

#### 2.1.1. Axit Nucleic (DNA & RNA)
- **DNA (Deoxyribonucleic acid)**:
  - Là polymer của các nucleotide.
  - Cấu tạo từ đường **deoxyribose** và 4 loại base: **A, T, G, C**.
  - Thường tồn tại dạng **mạch kép**, tuân theo nguyên tắc bổ sung: **A–T**, **G–C**.
- **RNA (Ribonucleic acid)**:
  - Cấu tạo từ đường **ribose** và 4 loại base: **A, U, G, C**.
  - Thường tồn tại dạng **mạch đơn**.
  - Các loại chính: **mRNA** (thông tin), **tRNA** (vận chuyển), **rRNA** (ribosome).
- **Gen**: Là một đoạn DNA mang thông tin mã hóa cho một sản phẩm chức năng xác định (có thể là protein hoặc RNA chức năng).

#### 2.1.2. Quá trình phiên mã (Transcription)
- **Cơ chế**: Tổng hợp RNA dựa trên mạch khuôn DNA.
- **Thành phần chính**: Enzyme **RNA polymerase**; sử dụng **mạch khuôn (template)** của DNA.
- **Chiều tổng hợp**: Mạch RNA được tổng hợp theo chiều **5' → 3'**; enzyme đọc mạch khuôn theo chiều **3' → 5'**.
- **Sản phẩm**: Tạo ra **mRNA**. Ở sinh vật nhân thực, mRNA sơ khai thường trải qua quá trình trưởng thành (gắn mũ 5', thêm đuôi poly(A), cắt nối exon) trước khi thực hiện chức năng.

#### 2.1.3. Quá trình dịch mã (Translation)
- **Nơi diễn ra**: Trên **ribosome**.
- **Đơn vị thông tin**: **Codon** (bộ ba mã hóa) nằm trên mRNA.
- **Cơ chế vận chuyển**: **tRNA** mang amino acid tương ứng, có bộ ba đối mã (**anticodon**) khớp bổ sung với codon trên mRNA.
- **Tiến trình**: Gồm 3 giai đoạn: **Khởi đầu → Kéo dài → Kết thúc**. Kết quả tạo ra chuỗi polypeptide theo trình tự quy định.
- **Tính chất mã di truyền**:
  - **Đặc hiệu**: Một codon chỉ mã hóa một loại amino acid.
  - **Thoái hóa**: Một amino acid có thể được mã hóa bởi nhiều codon khác nhau.
  - **Gần như phổ biến**: Dùng chung cho hầu hết sinh giới.
  - **Đọc liên tục, không chồng gối**: Đọc theo từng bộ ba kế tiếp nhau (trong mô hình cơ bản).

### 2.2. Enzyme và Xúc tác sinh học
- **Bản chất**: Chủ yếu là **protein** (ngoại lệ có một số RNA xúc tác gọi là ribozyme).
- **Cấu trúc**: Có **trung tâm hoạt động** để gắn cơ chất.
- **Cơ chế tác động**: Làm giảm **năng lượng hoạt hóa**, giúp tăng tốc độ phản ứng. Enzyme **không làm thay đổi ΔG** (năng lượng tự do) và **không làm thay đổi vị trí cân bằng** của phản ứng.
- **Tính đặc hiệu**:
  - Đặc hiệu cơ chất (chỉ tác dụng lên chất cụ thể).
  - Đặc hiệu phản ứng (xúc tác cho loại phản ứng cụ thể).
- **Các yếu tố ảnh hưởng**: Nhiệt độ, pH, nồng độ cơ chất, nồng độ enzyme, chất ức chế/hoạt hóa, ion kim loại/cofactor.
- **Ức chế enzyme**:
  - **Cạnh tranh**: Chất ức chế tranh giành trực tiếp vị trí hoạt động với cơ chất.
  - **Không cạnh tranh/Phi cạnh tranh**: Chất ức chế gắn vào vị trí khác, làm biến đổi cấu trúc enzyme hoặc ngăn cản xúc tác dù cơ chất đã gắn vào.
- **Cofactor/Coenzyme**: Các thành phần phi protein (ion kim loại hoặc phân tử hữu cơ) cần thiết để enzyme hoạt động.

### 2.3. Tín hiệu tế bào: Hormone và Thụ thể
- **Hormone**: Chất truyền tin hóa học của hệ nội tiết, tác động lên tế bào đích có **thụ thể đặc hiệu**.
- **Cơ chế tác động dựa trên tính tan**:
  - **Hormone tan trong nước**: Thường gắn vào **thụ thể trên màng tế bào**, kích hoạt chuỗi truyền tin thứ cấp bên trong tế bào.
  - **Hormone tan trong lipid**: Thường đi qua màng tế bào, gắn vào **thụ thể nội bào hoặc trong nhân**, trực tiếp điều hòa phiên mã gen.
- **Thụ thể (Receptor)**: Protein nhận tín hiệu.
- **Nguyên tắc then chốt**:
  - Sự đặc hiệu giữa phối tử (ligand) và thụ thể.
  - Sự **khuếch đại tín hiệu** thông qua các bước trung gian.
- **Mô hình chung**: Ligand → Receptor → Chất truyền tin nội bào → Đáp ứng tế bào (thay đổi hoạt tính enzyme, kênh ion hoặc biểu hiện gen).

---

## 3. Vi sinh cơ bản

### 3.1. Tổng quan về kháng sinh
- **Khái niệm**: Là chất có khả năng ức chế hoặc tiêu diệt vi khuẩn (hoặc vi sinh vật khác) ở nồng độ thích hợp.
- **Phân loại nguồn gốc**: Có thể là tự nhiên, bán tổng hợp hoặc tổng hợp hoàn toàn.
- **Nguồn gốc tự nhiên**: Thường được chiết xuất từ vi sinh vật, phổ biến nhất là **xạ khuẩn (Actinomycetes/Streptomyces)**, một số loại **vi khuẩn** và **nấm**.
- **Nguyên tắc tác động**: Kháng sinh tấn công vào các **đích đặc hiệu** của vi khuẩn như: thành tế bào, ribosome, quá trình tổng hợp acid nucleic hoặc các con đường chuyển hóa (tùy theo loại kháng sinh).

### 3.2. Vấn đề kháng kháng sinh
- **Nguyên nhân chính**:
  - **Đột biến**: Vi khuẩn phát sinh biến thể kháng thuốc, sau đó được **chọn lọc** và giữ lại do áp lực của việc dùng kháng sinh.
  - **Trao đổi gen ngang**: Vi khuẩn nhận gen kháng thuốc từ vi khuẩn khác thông qua plasmid hoặc transposon.
  - **Hành vi sử dụng**: Lạm dụng thuốc, dùng sai chỉ định, không đủ liều lượng hoặc thời gian điều trị.
- **Hậu quả**: Giảm hiệu quả điều trị bệnh nhiễm trùng, tăng nguy cơ lan truyền các chủng vi khuẩn đa kháng, làm tăng chi phí y tế và biến chứng.
- **Nguyên tắc sử dụng an toàn**:
  - Dùng đúng chỉ định, đúng liều lượng, đủ thời gian liệu trình.
  - Hạn chế tự ý mua và sử dụng kháng sinh.
  - Ưu tiên sử dụng dựa trên kết quả kháng sinh đồ (nếu có).
  - Tuân thủ kiểm soát lây nhiễm và quy chế kê đơn.