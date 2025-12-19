# Notes Vật lý đại cương I
*(Dùng làm corpus RAG/MCQ — ngắn gọn, ưu tiên ký hiệu chuẩn)*

## Quy ước – ký hiệu chung
- Vectơ: **\(\vec r, \vec v, \vec a, \vec F\)**. Độ lớn: \(r, v, a, F\).  
- Đạo hàm theo thời gian: \(\dot{x}=\dfrac{dx}{dt}\), \(\ddot{x}=\dfrac{d^2x}{dt^2}\).  
- Tích vô hướng: \(\vec A\cdot \vec B = AB\cos\theta\). Tích có hướng: \(\vec A\times \vec B\) (độ lớn \(AB\sin\theta\)).  
- Góc: \(\omega=\dot{\theta}\), \(\alpha=\dot{\omega}\).  
- Trọng trường gần mặt đất: \(g \approx 9{,}8\,\text{m/s}^2\).  
- Mômen quán tính: \(I=\sum m_ir_i^2\) (hoặc \(I=\int r^2\,dm\)).  
- Hằng số hấp dẫn: \(G\). Hằng số khí: \(R\). Hằng số Boltzmann: \(k_B\).

---

# 1. Động học chất điểm

## 1.1. Khái niệm mở đầu
### 1.1.1. Chất điểm – hệ quy chiếu
- **Chất điểm**: vật có kích thước bỏ qua so với quãng đường/độ chính xác khảo sát.  
- **Hệ quy chiếu**: gốc \(O\), trục tọa độ, đồng hồ.  
- **Vị trí**: \(\vec r(t)\). **Độ dời**: \(\Delta \vec r=\vec r_2-\vec r_1\).  
- **Quãng đường**: \(s\) (không phải vectơ).

## 1.2. Vận tốc
### 1.2.1. Vận tốc trung bình – tức thời
- \(\vec v_{tb}=\dfrac{\Delta \vec r}{\Delta t}\).  
- \(\vec v=\dfrac{d\vec r}{dt}\).  
- Tốc độ: \(v=\dfrac{ds}{dt}\).

### 1.2.2. Thành phần theo tọa độ
- Cartesian: \(\vec v=(\dot x,\dot y,\dot z)\).  
- Chuyển động thẳng: \(v=\dot x\).

## 1.3. Gia tốc
### 1.3.1. Gia tốc trung bình – tức thời
- \(\vec a_{tb}=\dfrac{\Delta \vec v}{\Delta t}\).  
- \(\vec a=\dfrac{d\vec v}{dt}=\dfrac{d^2\vec r}{dt^2}\).  

### 1.3.2. Thành phần theo tọa độ
- \(\vec a=(\ddot x,\ddot y,\ddot z)\).

## 1.4. Gia tốc tiếp tuyến và pháp tuyến
- Tách theo tiếp tuyến (t) và pháp tuyến (n) của quỹ đạo:  
  - \(a_t=\dfrac{dv}{dt}\).  
  - \(a_n=\dfrac{v^2}{R}\) (với \(R\) bán kính cong quỹ đạo).  
- \(\vec a=a_t\hat t+a_n\hat n\).

## 1.5. Ứng dụng: một số chuyển động cơ đặc biệt
### 1.5.1. Chuyển động thẳng biến đổi đều (gia tốc không đổi)
- \(v=v_0+at\)  
- \(x=x_0+v_0t+\dfrac12at^2\)  
- \(v^2=v_0^2+2a(x-x_0)\)

### 1.5.2. Rơi tự do (bỏ qua cản không khí)
- Lấy trục \(+y\) hướng lên: \(a_y=-g\).  
- \(v_y=v_{0y}-gt\), \(y=y_0+v_{0y}t-\dfrac12gt^2\).

### 1.5.3. Ném xiên (không cản)
- \(\vec a=(0,-g)\).  
- \(x=x_0+v_0\cos\theta\;t\)  
- \(y=y_0+v_0\sin\theta\;t-\dfrac12gt^2\)  
- Tầm xa (cùng độ cao): \(L=\dfrac{v_0^2\sin 2\theta}{g}\).  
- Thời gian bay (cùng độ cao): \(T=\dfrac{2v_0\sin\theta}{g}\).  
- Độ cao cực đại: \(H=\dfrac{v_0^2\sin^2\theta}{2g}\).

### 1.5.4. Chuyển động tròn đều
- \(v=\omega R\)  
- \(a_n=\omega^2R=\dfrac{v^2}{R}\)  
- Chu kỳ \(T=\dfrac{2\pi}{\omega}\), tần số \(f=\dfrac1T\).

---

# 2. Động lực học chất điểm

## 2.1. Các định luật Newton
### 2.1.1. Định luật I
- Trong hệ quy chiếu quán tính: \(\sum \vec F=0 \Rightarrow \vec v\) không đổi.

### 2.1.2. Định luật II
- \(\sum \vec F = m\vec a\).

### 2.1.3. Định luật III
- \(\vec F_{12}=-\vec F_{21}\) (cùng đường thẳng, cùng độ lớn, ngược chiều).

### 2.1.4. Lực thường gặp
- Trọng lực: \(\vec P=m\vec g\).  
- Phản lực: \(\vec N\) (vuông góc mặt tiếp xúc).  
- Ma sát trượt: \(F_{ms}=\mu_k N\), hướng ngược vận tốc tương đối.  
- Ma sát nghỉ: \(F_{ms}\le \mu_s N\).  
- Lò xo (Hooke): \(\vec F=-k\vec x\).

## 2.2. Các định lý về động lượng
### 2.2.1. Động lượng – xung lượng
- Động lượng: \(\vec p=m\vec v\).  
- Xung lượng: \(\vec J=\int_{t_1}^{t_2}\vec F\,dt\).  
- Định lý xung lượng–động lượng: \(\Delta \vec p=\vec J\).  
- Lực không đổi: \(\vec J=\vec F\Delta t\).

## 2.3. Ứng dụng phương trình cơ bản \(\sum\vec F=m\vec a\)
- Quy trình: vẽ FBD → chọn trục → chiếu lực → lập phương trình → giải.  
- Mặt phẳng nghiêng (không ma sát): \(a=g\sin\alpha\).  
- Mặt phẳng nghiêng (có ma sát trượt): \(a=g(\sin\alpha-\mu_k\cos\alpha)\).

## 2.4. Mômen động lượng
- Mômen lực (momen lực): \(\vec\tau=\vec r\times\vec F\).  
- Mômen động lượng: \(\vec L=\vec r\times \vec p\).  
- Định lý: \(\dfrac{d\vec L}{dt}=\vec\tau_{ngoại}\).

## 2.5. Chuyển động tương đối – nguyên lý Galile
### 2.5.1. Cộng vận tốc (Galile)
- \(\vec v_{A/C}=\vec v_{A/B}+\vec v_{B/C}\) (hệ quy chiếu quán tính).

### 2.5.2. Gia tốc
- Trong biến đổi Galile (vận tốc tương đối không đổi): \(\vec a\) là bất biến.

---

# 3. Động lực học hệ chất điểm – Động lực học vật rắn

## 3.1. Khối tâm
- \(\vec r_{CM}=\dfrac{1}{M}\sum m_i\vec r_i\) (rời rạc), \(M=\sum m_i\).  
- Liên tục: \(\vec r_{CM}=\dfrac{1}{M}\int \vec r\,dm\).  
- Vận tốc khối tâm: \(\vec v_{CM}=\dfrac{d\vec r_{CM}}{dt}\).

## 3.2. Định luật bảo toàn động lượng (hệ)
- Tổng động lượng: \(\vec P=\sum \vec p_i\).  
- \(\dfrac{d\vec P}{dt}=\sum \vec F_{ngoại}\).  
- Nếu \(\sum \vec F_{ngoại}=0 \Rightarrow \vec P\) bảo toàn.

## 3.3. Chuyển động của vật rắn
### 3.3.1. Tịnh tiến
- Mọi điểm có cùng \(\vec v,\vec a\). \(\sum \vec F_{ngoại}=M\vec a_{CM}\).

### 3.3.2. Quay quanh trục cố định
- \(v=\omega r\), \(a_t=\alpha r\), \(a_n=\omega^2 r\).  
- Động học góc (α không đổi):  
  - \(\omega=\omega_0+\alpha t\)  
  - \(\theta=\theta_0+\omega_0t+\dfrac12\alpha t^2\)  
  - \(\omega^2=\omega_0^2+2\alpha(\theta-\theta_0)\)

## 3.4. Định lý mômen động lượng của hệ chất điểm
- \(\dfrac{d\vec L}{dt}=\vec\tau_{ngoại}\), với \(\vec L=\sum \vec r_i\times \vec p_i\).

## 3.5. Phương trình cơ bản quay quanh trục cố định
- \(\sum \tau = I\alpha\).  
- \(\vec L=I\vec\omega\) (quay quanh trục cố định, \(I\) theo trục đó).

## 3.6. Bảo toàn mômen động lượng
- Nếu \(\vec\tau_{ngoại}=0\Rightarrow \vec L\) bảo toàn.  
- Hệ quả (quay quanh trục): \(I\omega=\text{hằng số}\).

## 3.7. Con quay (tóm tắt công thức hay dùng)
- Tiền tiến (precession) do mômen trọng lực:  
  - \(\vec\tau=\vec r\times m\vec g\).  
  - Xấp xỉ tốc độ tiền tiến đều: \(\Omega \approx \dfrac{\tau}{L}=\dfrac{mgr}{I\omega}\) (mô hình con quay đối xứng, góc nhỏ/ổn định).

---

# 4. Năng lượng

## 4.1. Công và công suất
- Công phần tử: \(dA=\vec F\cdot d\vec r\).  
- Công: \(A=\int \vec F\cdot d\vec r\).  
- Lực không đổi: \(A=Fs\cos\theta\).  
- Công suất: \(P=\dfrac{dA}{dt}=\vec F\cdot\vec v\).

## 4.2. Năng lượng (khái niệm)
- Năng lượng là đại lượng vô hướng đặc trưng khả năng sinh công.  
- Cơ năng: \(E=K+U\) (khi có thế năng).

## 4.3. Động năng
- Động năng tịnh tiến: \(K=\dfrac12mv^2\).  
- Định lý động năng: \(A_{tổng}=\Delta K\).  
- Động năng quay: \(K_{quay}=\dfrac12 I\omega^2\).  
- Lăn không trượt: \(K=\dfrac12Mv_{CM}^2+\dfrac12I_{CM}\omega^2\), với \(v_{CM}=\omega R\).

## 4.4. Va chạm
### 4.4.1. Bảo toàn động lượng
- Trong thời gian va chạm ngắn, nếu xung ngoại lực bỏ qua: \(\vec P\) bảo toàn.

### 4.4.2. Hệ số đàn hồi (1D)
- \(e=\dfrac{v_2'-v_1'}{v_1-v_2}\), \(0\le e\le 1\).  
- Va chạm đàn hồi: \(e=1\) và \(K\) bảo toàn.  
- Va chạm mềm hoàn toàn: \(e=0\) (dính vào nhau).

## 4.5. Trường lực thế
- Lực thế: công không phụ thuộc đường đi, chỉ phụ thuộc hai điểm.  
- Điều kiện tương đương (miền đơn liên): \(\oint \vec F\cdot d\vec r=0\).  
- Có thế năng \(U\): \(\vec F=-\nabla U\).

## 4.6. Thế năng
- Quan hệ: \(\Delta U=-A_{lực\;thế}\).  
- Trọng trường đều: \(U=mgh\) (mốc tùy chọn).  
- Lò xo: \(U=\dfrac12kx^2\).

## 4.7. Bảo toàn cơ năng trong trường lực thế
- Nếu chỉ có lực thế: \(K+U=\text{hằng số}\).  
- Nếu có lực không thế (ma sát…): \(\Delta(K+U)=A_{không\;thế}\).

---

# 5. Trường hấp dẫn

## 5.1. Định luật Newton về hấp dẫn
- \(F=G\dfrac{m_1m_2}{r^2}\), hướng hút dọc đường nối hai vật.

## 5.2. Trường hấp dẫn Newton
- Cường độ trường: \(\vec g(\vec r)=\dfrac{\vec F}{m}=-G\dfrac{M}{r^2}\hat r\).  
- Thế hấp dẫn (thế năng trên 1 đơn vị khối lượng): \(\phi=-\dfrac{GM}{r}\).  
- Thế năng hấp dẫn: \(U=m\phi=-G\dfrac{Mm}{r}\).

## 5.3. Chuyển động trong trường hấp dẫn Trái Đất
- Gần mặt đất: \(g\approx\) hằng → các công thức rơi tự do/ném xiên (Ch.1).  
- Vệ tinh quỹ đạo tròn bán kính \(r\):  
  - \(v=\sqrt{\dfrac{GM}{r}}\)  
  - \(T=2\pi\sqrt{\dfrac{r^3}{GM}}\)

## 5.4. Chuyển động hành tinh (điểm chính)
- Định luật Kepler (tóm tắt):  
  - Quỹ đạo elip, Mặt Trời tại 1 tiêu điểm.  
  - Diện tích quét đều theo thời gian (mômen động lượng bảo toàn).  
  - \(T^2\propto a^3\) (bán trục lớn \(a\)): \(T^2=\dfrac{4\pi^2}{GM}a^3\) (xấp xỉ \(m\ll M\)).

---

# 6. Dao động – Sóng (cơ)

## 6.1. Dao động điều hòa (SHM)
- Phương trình: \(x=A\cos(\omega t+\varphi)\).  
- Vận tốc: \(v=\dot x=-A\omega\sin(\omega t+\varphi)\).  
- Gia tốc: \(a=\ddot x=-\omega^2x\).  
- Chu kỳ: \(T=\dfrac{2\pi}{\omega}\), \(f=\dfrac{1}{T}\).  
- Năng lượng:  
  - \(K=\dfrac12mv^2\)  
  - \(U=\dfrac12kx^2\) (lò xo)  
  - \(E=K+U=\dfrac12kA^2=\dfrac12m\omega^2A^2\) (không tắt dần).  
- Lò xo: \(\omega=\sqrt{\dfrac{k}{m}}\).  
- Con lắc đơn (góc nhỏ): \(\omega=\sqrt{\dfrac{g}{\ell}}\), \(T=2\pi\sqrt{\dfrac{\ell}{g}}\).

## 6.2. Con lắc vật lý (góc nhỏ)
- \(\omega=\sqrt{\dfrac{mgd}{I_O}}\), \(T=2\pi\sqrt{\dfrac{I_O}{mgd}}\).  
- \(d\): khoảng cách từ trục quay đến khối tâm; \(I_O\): mômen quán tính quanh trục quay.

## 6.3. Dao động tắt dần (mô hình tuyến tính)
- Phương trình: \(m\ddot x+b\dot x+kx=0\).  
- Tần số riêng: \(\omega_0=\sqrt{\dfrac{k}{m}}\).  
- Hệ số tắt dần: \(\gamma=\dfrac{b}{2m}\).  
- Dao động dưới tắt (underdamped): \(x=Ae^{-\gamma t}\cos(\omega t+\varphi)\), \(\omega=\sqrt{\omega_0^2-\gamma^2}\).  
- Tới hạn: \(\gamma=\omega_0\). Quá tắt: \(\gamma>\omega_0\).

---

# 7. Vật lí thống kê cổ điển

## 7.1. Thuyết động học phân tử khí lý tưởng
- Phương trình trạng thái: \(pV=nRT=Nk_BT\).  
- Liên hệ vi mô: \(pV=\dfrac13Nm\overline{v^2}\).  
- Động năng tịnh tiến trung bình: \(\overline{\varepsilon}=\dfrac32k_BT\).  
- Vận tốc căn phương trung bình: \(v_{rms}=\sqrt{\overline{v^2}}=\sqrt{\dfrac{3k_BT}{m}}=\sqrt{\dfrac{3RT}{M}}\).  
- Quãng đường tự do trung bình: \(\lambda=\dfrac{1}{\sqrt2\pi d^2 n}\) (với \(d\) đường kính phân tử, \(n\) mật độ hạt).

## 7.2. Phương pháp thống kê – phân bố vận tốc Maxwell
- Phân bố tốc độ (khí lý tưởng):  
  - \(f(v)=4\pi\left(\dfrac{m}{2\pi k_BT}\right)^{3/2}v^2e^{-mv^2/(2k_BT)}\).  
- Các vận tốc đặc trưng:  
  - \(v_{mp}=\sqrt{\dfrac{2k_BT}{m}}\) (xác suất cực đại)  
  - \(\overline{v}=\sqrt{\dfrac{8k_BT}{\pi m}}\)  
  - \(v_{rms}=\sqrt{\dfrac{3k_BT}{m}}\)

## 7.3. Phân bố Boltzmann
- Xác suất mức năng lượng \(\varepsilon_i\):  
  - \(P_i=\dfrac{1}{Z}e^{-\varepsilon_i/(k_BT)}\).  
- Tỷ số quần thể: \(\dfrac{N_2}{N_1}=\dfrac{g_2}{g_1}e^{-(\varepsilon_2-\varepsilon_1)/(k_BT)}\).  
- Hàm vách ngăn (partition function): \(Z=\sum_i g_i e^{-\varepsilon_i/(k_BT)}\).

---

# 8. Cơ sở Nhiệt động lực học

## 8.1. Hệ nhiệt động
- **Hệ**: phần vật chất khảo sát; **môi trường**: phần còn lại.  
- Hệ cô lập / kín / hở.  
- Trạng thái: \((p,V,T)\) (khí lý tưởng).  
- Quá trình: đẳng nhiệt \(T=\) const, đẳng tích \(V=\) const, đẳng áp \(p=\) const, đoạn nhiệt \(Q=0\).

## 8.2. Nội năng, công, nhiệt
- Nội năng \(U\): hàm trạng thái.  
- Nhiệt \(Q\): năng lượng truyền do chênh lệch nhiệt độ (không là hàm trạng thái).  
- Công \(A\) (hệ thực hiện): \(A=\int p\,dV\) (quasi-static).  
  - Nở: \(dV>0\Rightarrow A>0\). Nén: \(A<0\).

## 8.3. Nguyên lý I nhiệt động lực học
- \(\Delta U = Q - A\) (quy ước: \(A\) là công do hệ sinh).  
- Khí lý tưởng: \(U=U(T)\).  
  - Monoatomic: \(U=\dfrac32nRT\).  
  - \(\Delta U = nC_V\Delta T\).  
- Nhiệt dung: \(C_V, C_p\). Với khí lý tưởng: \(C_p-C_V=R\).  
- Tỉ số \(\gamma=\dfrac{C_p}{C_V}\).

## 8.4. Áp dụng NL I cho các quá trình của khí lý tưởng
### 8.4.1. Đẳng tích
- \(A=0\). \(Q=\Delta U=nC_V\Delta T\).

### 8.4.2. Đẳng áp
- \(A=p\Delta V=nR\Delta T\).  
- \(Q=nC_p\Delta T\).

### 8.4.3. Đẳng nhiệt (khí lý tưởng)
- \(\Delta U=0\). \(Q=A\).  
- \(A=\int_{V_1}^{V_2}\dfrac{nRT}{V}\,dV=nRT\ln\!\left(\dfrac{V_2}{V_1}\right)\).

### 8.4.4. Đoạn nhiệt thuận nghịch
- \(Q=0\). \(\Delta U=-A\).  
- Quan hệ: \(pV^\gamma=\text{hằng số}\), \(TV^{\gamma-1}=\text{hằng số}\).  
- Công đoạn nhiệt: \(A=\dfrac{p_1V_1-p_2V_2}{\gamma-1}\).

## 8.5. Sự xuất hiện tất yếu của nguyên lý II (ý chính)
- Không thể biến toàn bộ nhiệt thành công trong chu trình mà không có biến đổi khác.  
- Chiều tự diễn biến: nhiệt tự truyền từ nóng → lạnh.

## 8.6. Nguyên lý II nhiệt động lực học
- Entropy \(S\):  
  - \(dS=\dfrac{\delta Q_{thuận\;nghịch}}{T}\).  
- Bất đẳng thức Clausius: \(\Delta S \ge \int \dfrac{\delta Q}{T}\).  
- Hệ cô lập: \(\Delta S \ge 0\) (tăng trong quá trình không thuận nghịch).

## 8.7. Máy nhiệt – hiệu suất – Carnot
- Máy nhiệt: nhận \(Q_h\) từ nguồn nóng \(T_h\), thải \(Q_c\) về nguồn lạnh \(T_c\), sinh công \(A=Q_h-Q_c\).  
- Hiệu suất: \(\eta=\dfrac{A}{Q_h}=1-\dfrac{Q_c}{Q_h}\).  
- Carnot (thuận nghịch, tối đa):  
  - \(\eta_{C}=1-\dfrac{T_c}{T_h}\) (T tính theo Kelvin).  
- Bơm nhiệt / tủ lạnh:  
  - Hệ số làm lạnh: \(\text{COP}_R=\dfrac{Q_c}{A}\).  
  - Bơm nhiệt: \(\text{COP}_{HP}=\dfrac{Q_h}{A}\).  
  - Carnot: \(\text{COP}_R=\dfrac{T_c}{T_h-T_c}\), \(\text{COP}_{HP}=\dfrac{T_h}{T_h-T_c}\).

---
## Checklist công thức “hay ra MCQ”
- Động học: \(v=\dot x\), \(a=\ddot x\), \(v^2=v_0^2+2a\Delta x\), \(a_n=v^2/R\).  
- Newton: \(\sum \vec F=m\vec a\), \(F_{ms}=\mu N\), \(\vec p=m\vec v\), \(\Delta \vec p=\int \vec Fdt\).  
- Quay: \(\sum \tau=I\alpha\), \(K_{quay}=\tfrac12I\omega^2\), \(I\omega=\) const nếu \(\tau_{ngoại}=0\).  
- Năng lượng: \(A=\int \vec F\cdot d\vec r\), \(P=\vec F\cdot\vec v\), \(\Delta(K+U)=A_{không\;thế}\).  
- Hấp dẫn: \(F=Gm_1m_2/r^2\), \(U=-GMm/r\), vệ tinh \(v=\sqrt{GM/r}\), \(T\propto r^{3/2}\).  
- SHM: \(x=A\cos(\omega t+\varphi)\), \(a=-\omega^2x\), \(\omega=\sqrt{k/m}\), con lắc đơn \(T=2\pi\sqrt{\ell/g}\).  
- Khí lý tưởng: \(pV=nRT\), \(\overline{\varepsilon}=\tfrac32k_BT\), \(v_{rms}=\sqrt{3k_BT/m}\).  
- Nhiệt động: \(\Delta U=Q-A\), \(A=\int pdV\), đẳng nhiệt \(A=nRT\ln(V_2/V_1)\), đoạn nhiệt \(pV^\gamma=\) const, \(dS=\delta Q_{rev}/T\), \(\eta_C=1-T_c/T_h\).
