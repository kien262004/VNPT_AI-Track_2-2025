# Notes Vật lý đại cương II

## 1. Điện trường tĩnh

### 1.1 Điện tích
- Điện tích: đại lượng bảo toàn; hai loại (+), (−).
- Lượng tử hóa: \(q = n e\), \(e = 1.602\times 10^{-19}\,\mathrm{C}\).
- Mật độ điện tích:
  - Tuyến tính: \(\lambda = \mathrm{d}q/\mathrm{d}l\)
  - Mặt: \(\sigma = \mathrm{d}q/\mathrm{d}S\)
  - Thể tích: \(\rho = \mathrm{d}q/\mathrm{d}V\)

### 1.2 Định luật Coulomb
- Lực giữa hai điện tích điểm:
  \[
  \vec F_{12} = k\,\frac{q_1 q_2}{r^2}\,\hat r,\quad k=\frac{1}{4\pi\varepsilon_0}
  \]
- Dạng môi trường: \(k=\frac{1}{4\pi\varepsilon}\), \(\varepsilon=\varepsilon_r\varepsilon_0\).

### 1.3 Điện trường \(\vec E\)
- Định nghĩa:
  \[
  \vec E = \frac{\vec F}{q_0}
  \]
- Điện trường do điện tích điểm:
  \[
  \vec E = \frac{1}{4\pi\varepsilon}\frac{q}{r^2}\hat r
  \]
- Chồng chất:
  \[
  \vec E = \sum_i \vec E_i,\quad \vec E(\vec r)=\frac{1}{4\pi\varepsilon}\int \rho(\vec r')\frac{\vec r-\vec r'}{\lVert \vec r-\vec r'\rVert^3}\,\mathrm{d}V'
  \]
- Thông lượng điện trường:
  \[
  \Phi_E=\iint_S \vec E\cdot \mathrm{d}\vec S
  \]
- Đường sức: tiếp tuyến tại mọi điểm trùng hướng \(\vec E\).

### 1.4 Điện thế \(V\) và thế năng
- Hiệu điện thế:
  \[
  V(B)-V(A)=-\int_A^B \vec E\cdot \mathrm{d}\vec l
  \]
- Điện thế do điện tích điểm:
  \[
  V = \frac{1}{4\pi\varepsilon}\frac{q}{r}
  \]
- Thế năng:
  \[
  U=qV,\quad \Delta U = q\,\Delta V
  \]

### 1.5 Liên hệ \(\vec E\) – \(V\)
- Trường tĩnh điện:
  \[
  \vec E = -\nabla V
  \]
- Tuần hoàn bằng 0:
  \[
  \oint \vec E\cdot \mathrm{d}\vec l=0
  \]

### 1.6 Định lý Gauss (Gau-xơ)
- Dạng tích phân:
  \[
  \iint_S \vec E\cdot \mathrm{d}\vec S = \frac{Q_{\text{enc}}}{\varepsilon}
  \]
- Dạng vi phân:
  \[
  \nabla\cdot \vec E = \frac{\rho}{\varepsilon}
  \]

### 1.7 Các kết quả chuẩn hay dùng (Gauss)
- Mặt cầu (điện tích điểm / phân bố cầu đối xứng):
  \[
  E(r)=\frac{1}{4\pi\varepsilon}\frac{Q}{r^2}
  \]
- Dây dài vô hạn (mật độ \(\lambda\)):
  \[
  E(r)=\frac{\lambda}{2\pi\varepsilon r}
  \]
- Mặt phẳng vô hạn (mật độ \(\sigma\)):
  \[
  E=\frac{\sigma}{2\varepsilon}
  \]
- Hai bản song song \(\pm\sigma\) (bỏ qua biên):
  \[
  E=\frac{\sigma}{\varepsilon}
  \]

---

## 2. Vật dẫn – Tụ điện

### 2.1 Vật dẫn cân bằng tĩnh điện
- Trong vật dẫn: \(\vec E=0\) (bên trong khối).
- Điện tích dư nằm trên bề mặt.
- Bề mặt vật dẫn là đẳng thế (\(V=\text{hằng}\)).
- \(\vec E\) ngay ngoài mặt dẫn vuông góc bề mặt:
  \[
  E_n = \frac{\sigma}{\varepsilon}
  \]
- Mật độ \(\sigma\) lớn ở chỗ cong nhọn (bán kính cong nhỏ).

### 2.2 Hiện tượng điện hưởng (cảm ứng tĩnh điện)
- Đưa điện tích gần vật dẫn: điện tích tự do phân bố lại → xuất hiện vùng \(\pm\) trên bề mặt.
- Nối đất: có thể “hút”/“đẩy” điện tích → vật dẫn còn điện tích thuần.

### 2.3 Hệ vật dẫn – Tụ điện
- Điện dung:
  \[
  C=\frac{Q}{U} \quad (\mathrm{F})
  \]
- Tụ phẳng:
  \[
  C=\varepsilon\frac{S}{d}
  \]
- Tụ cầu đồng tâm (bán kính \(a<b\)):
  \[
  C=4\pi\varepsilon\frac{ab}{b-a}
  \]
- Tụ trụ đồng tâm (chiều dài \(L\), bán kính \(a<b\)):
  \[
  C=\frac{2\pi\varepsilon L}{\ln(b/a)}
  \]
- Ghép tụ:
  - Song song: \(C_{\text{eq}}=\sum C_i\)
  - Nối tiếp: \(\frac{1}{C_{\text{eq}}}=\sum \frac{1}{C_i}\)

### 2.4 Phương pháp ảnh điện (ý chính)
- Thay vật dẫn đẳng thế bằng “điện tích ảnh” sao cho thỏa điều kiện biên \(V=\text{hằng}\) trên bề mặt dẫn.
- Ví dụ (điện tích \(q\) trước mặt phẳng dẫn nối đất): lực như tương tác với \(q'=-q\) đối xứng qua mặt phẳng.

### 2.5 Năng lượng điện trường – năng lượng tụ
- Mật độ năng lượng điện trường:
  \[
  w=\frac{1}{2}\varepsilon E^2
  \]
- Năng lượng tụ:
  \[
  W=\frac{1}{2}CU^2=\frac{Q^2}{2C}=\frac{1}{2}QU
  \]

---

## 3. Điện môi

### 3.1 Phân cực điện môi
- Vector phân cực \(\vec P\): mômen lưỡng cực điện trên một đơn vị thể tích.
- Điện tích liên kết:
  \[
  \rho_b=-\nabla\cdot \vec P,\quad \sigma_b=\vec P\cdot \hat n
  \]

### 3.2 Trường trong điện môi – \(\vec D\)
- Vector điện cảm (điện dịch):
  \[
  \vec D=\varepsilon_0\vec E+\vec P
  \]
- Gauss cho \(\vec D\):
  \[
  \nabla\cdot \vec D=\rho_f,\quad \iint \vec D\cdot \mathrm{d}\vec S = Q_f
  \]
- Điện môi tuyến tính đẳng hướng:
  \[
  \vec P=\varepsilon_0\chi_e \vec E,\quad \varepsilon=\varepsilon_0(1+\chi_e)=\varepsilon_0\varepsilon_r,\quad \vec D=\varepsilon \vec E
  \]
- Điều kiện biên cơ bản:
  - Thành phần pháp tuyến:
    \[
    D_{n2}-D_{n1}=\sigma_f
    \]
  - Thành phần tiếp tuyến (tĩnh điện):
    \[
    E_{t2}-E_{t1}=0
    \]

---

## 4. Dòng điện

### 4.1 Bản chất và các đặc trưng
- Dòng điện: chuyển dời có hướng của điện tích.
- Cường độ dòng:
  \[
  I=\frac{\mathrm{d}q}{\mathrm{d}t}
  \]
- Mật độ dòng:
  \[
  \vec J=\frac{\mathrm{d}I}{\mathrm{d}S}\hat n,\quad I=\iint \vec J\cdot \mathrm{d}\vec S
  \]
- Phương trình liên tục:
  \[
  \nabla\cdot \vec J + \frac{\partial \rho}{\partial t}=0
  \]

### 4.2 Dòng điện trong kim loại – định luật Ohm
- Vi mô:
  \[
  \vec J=\sigma \vec E
  \]
- Vĩ mô:
  \[
  U=IR,\quad R=\rho \frac{l}{S},\quad \rho=\frac{1}{\sigma}
  \]
- Công suất tỏa nhiệt (Joule–Lenz):
  \[
  P=UI=I^2R=\frac{U^2}{R}
  \]
- Suất điện động nguồn \(\mathcal{E}\), điện trở trong \(r\):
  \[
  U=\mathcal{E}-Ir
  \]

### 4.3 Điện trường xoáy (liên quan nguồn biến thiên)
- Suất điện động:
  \[
  \mathcal{E}=\oint \vec E\cdot \mathrm{d}\vec l
  \]
- Với cảm ứng điện từ (liên hệ chương 6):
  \[
  \oint \vec E\cdot \mathrm{d}\vec l=-\frac{\mathrm{d}\Phi_B}{\mathrm{d}t}
  \]

### 4.4 Các định luật Kirchhoff (Kiarchốp)
- Nút (KCL):
  \[
  \sum I_k=0
  \]
- Vòng kín (KVL):
  \[
  \sum \Delta V_k=0 \quad (\text{gồm cả }+\mathcal{E},-IR)
  \]

---

## 5. Từ trường (cơ bản)

### 5.1 Khái niệm từ trường
- Từ trường đặc trưng bởi \(\vec B\) (cảm ứng từ).
- Lực Lorentz:
  \[
  \vec F=q(\vec E+\vec v\times \vec B)
  \]
- Lực từ lên dây dẫn mang dòng:
  \[
  \mathrm{d}\vec F=I\,\mathrm{d}\vec l\times \vec B
  \]

### 5.2 Định luật Ampère (trường tĩnh)
- Dạng tích phân (trong chân không/đơn giản):
  \[
  \oint \vec B\cdot \mathrm{d}\vec l=\mu_0 I_{\text{enc}}
  \]
- Dạng vi phân:
  \[
  \nabla\times \vec B=\mu_0 \vec J
  \]

---

## 5'. Từ trường (tiếp)

### 5.3 Vectơ từ cảm \(\vec B\): các kết quả chuẩn
- Dây thẳng dài:
  \[
  B(r)=\frac{\mu_0 I}{2\pi r}
  \]
- Vòng dây tròn (tâm, bán kính \(R\)):
  \[
  B=\frac{\mu_0 I}{2R}
  \]
- Ống dây dài (solenoid, \(n\) vòng/m):
  \[
  B=\mu_0 n I
  \]
- Từ trường đều: \(\Phi_B = BA\cos\theta\)

### 5.4 \(\vec H\) và quan hệ vật liệu
- Trong vật liệu:
  \[
  \vec B=\mu_0(\vec H+\vec M)
  \]
- Môi trường tuyến tính:
  \[
  \vec B=\mu \vec H,\quad \mu=\mu_0\mu_r
  \]

### 5.5 Gauss cho từ trường
- Không có đơn cực từ:
  \[
  \iint \vec B\cdot \mathrm{d}\vec S = 0,\quad \nabla\cdot \vec B=0
  \]

### 5.6 Tác dụng của từ trường lên dòng điện – mômen
- Mômen lên khung dây (N vòng):
  \[
  \vec \tau=\vec m\times \vec B,\quad \vec m=NI\vec A
  \]
- Thế năng từ:
  \[
  U=-\vec m\cdot \vec B
  \]

### 5.7 Công của lực từ
- Lực từ không sinh công lên hạt điểm trong \(\vec B\) đều:
  \[
  W_B=0 \quad (\vec F\perp \vec v)
  \]

### 5.8 Chuyển động hạt trong \(\vec B\)
- Bán kính quỹ đạo (thành phần vuông góc):
  \[
  r=\frac{mv_\perp}{|q|B}
  \]
- Tần số cyclotron:
  \[
  \omega=\frac{|q|B}{m},\quad f=\frac{\omega}{2\pi}
  \]
- Bước xoắn (có \(v_\parallel\)):
  \[
  p=v_\parallel T,\quad T=\frac{2\pi}{\omega}
  \]

### 5.9 Vật liệu từ (tóm tắt)
- Thuận từ/nghịch từ/sắt từ: phân loại theo \(\chi_m\) và \(\mu_r\).
- Vòng trễ (hysteresis) ở sắt từ: \(B(H)\), từ dư, lực kháng từ.

---

## 6. Cảm ứng điện từ – Điện từ trường

### 6.1 Cảm ứng điện từ (Faraday–Lenz)
- Định luật Faraday:
  \[
  \mathcal{E}=-\frac{\mathrm{d}\Phi_B}{\mathrm{d}t}
  \]
- Dạng trường:
  \[
  \oint \vec E\cdot \mathrm{d}\vec l=-\frac{\mathrm{d}}{\mathrm{d}t}\iint \vec B\cdot \mathrm{d}\vec S,\quad
  \nabla\times \vec E=-\frac{\partial \vec B}{\partial t}
  \]
- Lenz: chiều dòng cảm ứng chống lại nguyên nhân gây biến thiên \(\Phi_B\).

### 6.2 Tự cảm
- Từ thông liên kết: \(\lambda = N\Phi_B\).
- Định nghĩa hệ số tự cảm:
  \[
  \lambda = LI
  \]
- Suất điện động tự cảm:
  \[
  \mathcal{E}_L=-L\frac{\mathrm{d}I}{\mathrm{d}t}
  \]
- Năng lượng trong cuộn cảm:
  \[
  W_L=\frac{1}{2}LI^2
  \]

### 6.3 Hỗ cảm
- Từ thông liên kết do mạch 1 gây lên mạch 2:
  \[
  \lambda_2 = M I_1
  \]
- Suất điện động hỗ cảm:
  \[
  \mathcal{E}_2=-M\frac{\mathrm{d}I_1}{\mathrm{d}t}
  \]
- Hệ số liên kết (coupling):
  \[
  M=k\sqrt{L_1L_2},\quad 0\le k\le 1
  \]

### 6.4 Dao động điện (mạch LC, RLC)
- LC lý tưởng:
  \[
  \omega_0=\frac{1}{\sqrt{LC}},\quad f_0=\frac{1}{2\pi\sqrt{LC}}
  \]
- Phương trình dao động điện tích:
  \[
  \frac{\mathrm{d}^2 q}{\mathrm{d}t^2}+\omega_0^2 q=0
  \]
- Năng lượng trao đổi:
  \[
  W=\frac{q^2}{2C}+\frac{Li^2}{2}=\text{hằng}
  \]
- RLC nối tiếp:
  \[
  L\frac{\mathrm{d}^2 q}{\mathrm{d}t^2}+R\frac{\mathrm{d}q}{\mathrm{d}t}+\frac{q}{C}=0
  \]
  (tắt dần; hệ số tắt dần \(\gamma=R/(2L)\), \(\omega_d=\sqrt{\omega_0^2-\gamma^2}\) khi dưới tắt).

---

## 7. Thuyết Maxwell về điện từ trường

### 7.1 Luận điểm về điện trường xoáy
- Điện trường có thể có xoáy khi \(\partial \vec B/\partial t\neq 0\):
  \[
  \nabla\times \vec E=-\frac{\partial \vec B}{\partial t}
  \]

### 7.2 Dòng điện dịch và bổ sung Ampère
- Dòng điện dịch:
  \[
  \vec J_d=\frac{\partial \vec D}{\partial t}
  \]
- Ampère–Maxwell:
  \[
  \nabla\times \vec H=\vec J_f+\frac{\partial \vec D}{\partial t}
  \]
  Trong chân không: \(\nabla\times \vec B=\mu_0\vec J+\mu_0\varepsilon_0\frac{\partial \vec E}{\partial t}\).

### 7.3 Hệ phương trình Maxwell (tổng quát)
- Gauss điện:
  \[
  \nabla\cdot \vec D=\rho_f
  \]
- Gauss từ:
  \[
  \nabla\cdot \vec B=0
  \]
- Faraday:
  \[
  \nabla\times \vec E=-\frac{\partial \vec B}{\partial t}
  \]
- Ampère–Maxwell:
  \[
  \nabla\times \vec H=\vec J_f+\frac{\partial \vec D}{\partial t}
  \]
- Quan hệ vật liệu tuyến tính:
  \[
  \vec D=\varepsilon \vec E,\quad \vec B=\mu \vec H,\quad \vec J=\sigma \vec E
  \]

### 7.4 Hệ quả quan trọng
- Phương trình sóng trong chân không:
  \[
  \nabla^2\vec E-\mu_0\varepsilon_0\frac{\partial^2\vec E}{\partial t^2}=0,\quad
  \nabla^2\vec B-\mu_0\varepsilon_0\frac{\partial^2\vec B}{\partial t^2}=0
  \]
- Vận tốc sóng điện từ:
  \[
  c=\frac{1}{\sqrt{\mu_0\varepsilon_0}}
  \]

---

## 8. Sóng điện từ

### 8.1 Khái niệm
- Sóng điện từ: dao động lan truyền của \(\vec E,\vec B\), mang năng lượng và động lượng.

### 8.2 Hàm sóng – mô tả sóng phẳng
- Sóng phẳng điều hòa:
  \[
  \vec E=\vec E_0\cos(\omega t-\vec k\cdot \vec r+\varphi),\quad
  \vec B=\vec B_0\cos(\omega t-\vec k\cdot \vec r+\varphi)
  \]
- Quan hệ:
  \[
  \vec E\perp \vec B\perp \vec k,\quad B_0=\frac{E_0}{v}
  \]
- Hệ thức sóng:
  \[
  v=\frac{\omega}{k},\quad \lambda=\frac{2\pi}{k},\quad f=\frac{\omega}{2\pi},\quad v=\lambda f
  \]
- Trong môi trường tuyến tính không dẫn:
  \[
  v=\frac{1}{\sqrt{\mu\varepsilon}}
  \]

### 8.3 Vector Poynting – cường độ năng lượng
- Mật độ năng lượng:
  \[
  u=\frac{1}{2}\varepsilon E^2+\frac{1}{2\mu}B^2
  \]
- Poynting:
  \[
  \vec S=\vec E\times \vec H
  \]
- Cường độ trung bình (sóng phẳng điều hòa):
  \[
  \langle S\rangle=\frac{1}{2}E_0H_0
  \]

---

## 9. Sóng ánh sáng

### 9.1 Tổng quát
- Ánh sáng: sóng điện từ (xấp xỉ sóng ngang).
- Chiết suất:
  \[
  n=\frac{c}{v}
  \]

### 9.2 Giao thoa ánh sáng
- Điều kiện cực đại (hai sóng cùng tần số):
  \[
  \Delta = m\lambda \quad (m\in\mathbb{Z})
  \]
- Điều kiện cực tiểu:
  \[
  \Delta = \left(m+\frac{1}{2}\right)\lambda
  \]
- Khe Young (khoảng vân):
  \[
  i=\frac{\lambda D}{a}
  \]
  (D: khoảng cách tới màn, a: khoảng cách hai khe).

### 9.3 Nhiễu xạ ánh sáng
- Khe đơn (cực tiểu):
  \[
  a\sin\theta = m\lambda\quad (m=\pm1,\pm2,\dots)
  \]
- Cách tử nhiễu xạ (cực đại bậc m):
  \[
  d\sin\theta = m\lambda
  \]

---

## 10. Thuyết tương đối và hạt ánh sáng

### 10.1 Maxwell và tính bất biến của vận tốc ánh sáng
- Trong chân không: \(c\) không phụ thuộc nguồn/phát hiện (tiên đề SR).

### 10.2 Thuyết tương đối hẹp (Einstein)
- Hai tiên đề: (i) các định luật vật lý như nhau trong mọi hệ quán tính; (ii) \(c\) bất biến.
- Hệ số Lorentz:
  \[
  \gamma=\frac{1}{\sqrt{1-\frac{v^2}{c^2}}}
  \]
- Giãn thời gian:
  \[
  \Delta t=\gamma \Delta t_0
  \]
- Co độ dài:
  \[
  L=\frac{L_0}{\gamma}
  \]
- Cộng vận tốc (1D):
  \[
  u=\frac{u'+v}{1+\frac{u'v}{c^2}}
  \]
- Động lượng và năng lượng tương đối tính:
  \[
  \vec p=\gamma m\vec v,\quad E=\gamma mc^2,\quad E^2=(pc)^2+(mc^2)^2
  \]

### 10.3 Photon
- Lượng tử ánh sáng:
  \[
  E=hf=\hbar\omega
  \]
- Động lượng photon:
  \[
  p=\frac{E}{c}=\frac{h}{\lambda}
  \]
- Hiệu ứng quang điện (công thức Einstein):
  \[
  h f = A + K_{\max}
  \]
  với \(A\) là công thoát, \(K_{\max}=\frac{1}{2}mv_{\max}^2=eU_h\) (điện thế hãm \(U_h\)).
