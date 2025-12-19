# Hệ Tuyến Tính & Biến Đổi Laplace

## 2. Modeling by First Order Linear ODEs
### 2.1. Mô hình tài khoản tiết kiệm
- A'(t) = rA(t) + u(t) (r: lãi suất liên tục; u(t): dòng nộp/rút).
- Nếu u(t)=u0 hằng: A(t) = (A0 + u0/r)e^{rt} - u0/r (r≠0).

### 2.2. Cách nhiệt tuyến tính / định luật Newton làm mát
- T'(t) = -k(T - T_env(t)) + q(t) (k>0).
- Trường hợp T_env hằng, q=0: T(t) = T_env + (T0 - T_env)e^{-kt}.

### 2.3. System–Signal–Response
- Tín hiệu vào x(t), ra y(t), hệ T: y=T[x].
- Hệ tuyến tính bậc 1 chuẩn: y' + p(t)y = g(t) (g phụ thuộc x).

---

## 3. Solutions of First Order Linear ODEs
### 3.1. Thuần nhất, không thuần nhất; chồng chập
- Thuần nhất: y' + p(t)y = 0 ⇒ y_h = C e^{-∫p dt}.
- Không thuần nhất: y' + p(t)y = g(t).
- Chồng chập (linear): y = y_h + y_p.

### 3.2. Hệ số tích phân / biến thiên hằng số
- μ(t)=exp(∫p(t)dt).
- Nghiệm tổng quát: y(t)= μ(t)^{-1}\[∫ μ(t)g(t)dt + C\].

### 3.3. Tiếp tục nghiệm; tồn tại–duy nhất (ý chính)
- Với y' = f(t,y), nếu f và ∂f/∂y liên tục gần (t0,y0) ⇒ tồn tại & duy nhất nghiệm địa phương.
- Nghiệm cực đại có thể “nổ” (blow-up) khi |y|→∞ hoặc ra khỏi miền xác định.

### 3.4. Ghi chú mô hình ngân hàng
- Ổn định dài hạn phụ thuộc dấu của r (r<0 ⇒ suy giảm; r>0 ⇒ tăng mũ).

---

## 4. Sinusoidal Solutions
### 4.1. Hàm tuần hoàn & sin/cos
- Tuần hoàn chu kỳ T: f(t+T)=f(t).
- sin(ωt+φ), cos(ωt+φ); ω=2π/T.

### 4.2. Nghiệm tuần hoàn & quá độ
- Với hệ ổn định: y(t)=y_ss(t)+y_tr(t), trong đó y_tr(t)→0 khi t→∞.

### 4.3. Đáp ứng biên độ & pha
- Với vào x(t)=A cos(ωt), ra y_ss(t)=A|H(iω)| cos(ωt+∠H(iω)).
- |H(iω)|: amplitude response; ∠H(iω): phase response.

---

## 5. Đại số số phức
### 5.1. Đại số cơ bản
- z=a+ib; cộng/trừ theo từng phần; nhân: (a+ib)(c+id)=(ac-bd)+i(ad+bc).
- Chia: z1/z2 = z1 * \bar z2 / |z2|^2 (z2≠0).

### 5.2. Liên hợp & môđun
- \bar z = a - ib; |z| = √(a^2+b^2).
- z\bar z = |z|^2; Re(z)=(z+\bar z)/2; Im(z)=(z-\bar z)/(2i).

### 5.3. Định lý cơ bản đại số
- Mọi đa thức bậc n≥1 trên ℂ có đúng n nghiệm (tính cả bội).

---

## 6. Số mũ phức
### 6.1. Nghiệm mũ
- Nếu y' = ky ⇒ y = Ce^{kt}. (k có thể phức)

### 6.2. Euler
- e^{iθ}=cosθ + i sinθ.
- e^{σ+iω} = e^σ (cosω + i sinω).

### 6.3. Dạng cực
- z = r e^{iθ}, r=|z|, θ=arg(z).

### 6.4. Nhân trong dạng cực
- (r1e^{iθ1})(r2e^{iθ2}) = (r1r2)e^{i(θ1+θ2)}.

### 6.5. Căn bậc n & nghiệm đơn vị
- Nghiệm n của z=re^{iθ}: z_k = r^{1/n} e^{i(θ+2πk)/n}, k=0..n-1.
- Roots of unity: e^{i2πk/n}.

---

## 7. Beats (nhịp phách)
### 7.1. Beats là gì
- cos(ω1 t)+cos(ω2 t)=2cos((ω1-ω2)t/2)cos((ω1+ω2)t/2).
- Bao (envelope) tần số: Δω/2, với Δω=|ω1-ω2|.

### 7.2. Beats không phải là gì
- Không phải “tần số mới” cố định; là điều biên theo thời gian do giao thoa.

---

## 8. RLC Circuits (mạch RLC nối tiếp)
### 8.1. Phương trình vi phân
- Với điện tích q(t): L q'' + R q' + (1/C)q = E(t).
- Dòng i(t)=q'(t). Dạng chuẩn (cho q): q'' + (R/L)q' + (1/LC)q = E(t)/L.

### 8.2. Đơn vị (nhắc nhanh)
- R(Ω), L(H), C(F), V(Volt), A(Ampere).

### 8.3. Hệ quả động lực
- ω0 = 1/√(LC) (tần số riêng), α = R/(2L) (hệ số tắt dần).
- Underdamped khi α<ω0; critically damped α=ω0; overdamped α>ω0.

---

## 9. Normalization of Solutions
### 9.1. Điều kiện đầu
- Ví dụ bậc 2: y(0)=y0, y'(0)=v0.

### 9.2. Chuẩn hoá nghiệm
- Viết nghiệm theo “hình dạng chuẩn”: y(t)=y0·φ1(t)+v0·φ2(t)+y_forced(t) (tuỳ hệ).

### 9.3. ZSR / ZIR (hệ LTI)
- Total response: y = y_ZIR + y_ZSR.
- ZIR: đáp ứng do điều kiện đầu, vào x=0.
- ZSR: đáp ứng do vào x, điều kiện đầu bằng 0.

---

## 10. Operators & Exponential Response Formula
### 10.1. Toán tử
- P(D) := a_n D^n + ... + a_1 D + a_0.
- ODE hệ số hằng: P(D)y = x(t).

### 10.2. Tín hiệu mũ là “hàm riêng” của LTI
- Nếu x(t)=e^{st} và P(s)≠0 ⇒ y(t)= (1/P(s)) e^{st}.
- Transfer (dạng toán tử): H(s)=1/P(s) (cho bài toán P(D)y=x).

### 10.3. Sinusoidal (phasor)
- cos(ωt)=Re(e^{iωt}); đáp ứng: y_ss(t)=Re(H(iω)e^{iωt}).

### 10.4. Damped sinusoidal
- e^{σt}cos(ωt)=Re(e^{(σ+iω)t}); dùng H(σ+iω).

### 10.5. Time invariance (nhắc lại)
- T[x(t-t0)] = y(t-t0).

---

## 11. Undetermined Coefficients (hệ số bất định)
- Áp dụng cho ODE tuyến tính hệ số hằng.
- Nếu x(t) là tổ hợp: e^{at}·P_m(t), sin(ωt), cos(ωt), hoặc tích của chúng ⇒ đoán y_p cùng “họ”.
- Quy tắc cộng hưởng: nếu dạng đoán trùng với nghiệm của thuần nhất bội k ⇒ nhân thêm t^k.

---

## 12. Resonance & Exponential Shift Law
### 12.1. Exponential shift (đổi biến toán tử)
- P(D)\[e^{at}u(t)\] = e^{at} P(D+a)\[u(t)\].
- Tương đương trong Laplace: L{e^{at}f(t)} = F(s-a).

### 12.2. Tín hiệu tích (product signals)
- Dùng shift để xử lý e^{at}·(sin/cos/polynomial).

### 12.3–12.4. Cộng hưởng
- Khi P(a)=0 (hoặc P(iω)=0 cho sin/cos) ⇒ nghiệm riêng cần nhân thêm t^k (k theo bội nghiệm).

### 12.5. Tóm tắt
- “Shift + resonance” là lõi để dựng nghiệm riêng nhanh.

---

## 13. Natural Frequency & Damping Ratio
- Chuẩn bậc 2: y'' + 2ζω_n y' + ω_n^2 y = x(t).
- ω_n: natural frequency; ζ: damping ratio.
- Quan hệ với RLC: ω_n=ω0=1/√(LC), ζ = R/(2)·√(C/L).
- Phân loại:
  - 0<ζ<1: underdamped (dao động tắt dần).
  - ζ=1: critical.
  - ζ>1: overdamped.

---

## 14. Frequency Response
### 14.1–14.2. Kích qua lò xo / giảm chấn (mô hình cơ)
- Mô hình khối–lò xo–giảm chấn: m y'' + b y' + k y = F(t).
- H(s)=Y(s)/F(s)=1/(m s^2 + b s + k).

### 14.3. Đáp ứng tần số bậc 2 theo ζ
- H(iω)=1/( -mω^2 + i bω + k).
- Dạng chuẩn: |H(iω)| = 1 / √((1-(ω/ω_n)^2)^2 + (2ζ ω/ω_n)^2) (tới hằng số tỉ lệ tuỳ chuẩn hoá).
- Pha: ∠H(iω) = -atan2(2ζ(ω/ω_n), 1-(ω/ω_n)^2).

---

## 15. Wronskian
- Với nghiệm y1,...,yn: W(t)=det\[y_j^{(k-1)}(t)\]_{k,j=1..n}.
- y1,...,yn độc lập tuyến tính trên I ⇔ W(t)≠0 tại một điểm trong I (cho ODE tuyến tính).
- Abel (bậc 2): nếu y'' + p(t)y' + q(t)y=0 ⇒ W(t)=C e^{-∫p(t)dt}.

---

## 16. Fourier Series (bổ sung)
### 16.1. Chuỗi Fourier thực
- Với f tuần hoàn T, ω0=2π/T:
  - f(t) ~ a0/2 + Σ_{n≥1}[a_n cos(nω0 t) + b_n sin(nω0 t)]
  - a_n = (2/T)∫_{t0}^{t0+T} f(t)cos(nω0 t)dt
  - b_n = (2/T)∫_{t0}^{t0+T} f(t)sin(nω0 t)dt

### 16.2. Đối xứng
- f chẵn ⇒ b_n=0. f lẻ ⇒ a_n=0 (và a0=0).

### 16.3. Gibbs
- Xấp xỉ gần điểm nhảy có overshoot không triệt tiêu khi n→∞.

### 16.4. “Khoảng cách Fourier”
- Sai số năng lượng thường dùng: ∫|f - S_N|^2 (liên quan Parseval).

### 16.5. Fourier phức
- f(t) ~ Σ_{n∈ℤ} c_n e^{inω0 t}, c_n=(1/T)∫ f(t)e^{-inω0 t}dt.

### 16.6. Harmonic response
- Với LTI: mỗi harmonic e^{inω0 t} bị nhân H(inω0); tổng đáp ứng = tổng từng harmonic.

---

## 17. Impulses & Generalized Functions
### 17.1–17.2. Delta Dirac
- Tính chất “sàng”: ∫_{-∞}^{∞} δ(t-t0) f(t) dt = f(t0).
- δ(t) = u'(t) (nghĩa phân phối).

### 17.3. Tích phân phân phối
- ∫ δ(t-a) dt = u(t-a) + C (theo nghĩa phân phối).

### 17.4. Đạo hàm tổng quát
- ∫ δ'(t-a) f(t) dt = -f'(a).

---

## 18. Impulse & Step Responses (LTI)
### 18.1. Impulse response
- h(t) := đáp ứng của hệ khi vào x(t)=δ(t) với điều kiện đầu bằng 0.
- Với LTI: y(t)= (x*h)(t).

### 18.2. Impulse trong ODE bậc 2 (jump conditions)
- Nếu y'' chứa δ(t-t0) ⇒ y' có bước nhảy tại t0.
- Quy tắc: tích phân ODE qua (t0-ε, t0+ε) để suy ra độ nhảy.

### 18.3. Singularity matching
- Cân bằng các “kỳ dị” (δ, δ') hai vế để tìm hệ số nhảy.

### 18.4. Step response
- s(t) := đáp ứng khi vào u(t), điều kiện đầu 0.
- Quan hệ (hệ nhân quả): s(t)=∫_0^t h(τ)dτ, và h(t)=s'(t) (ngoại trừ tại điểm nhảy).

---

## 19. Convolution
### 19.1. Tích chập
- (x*h)(t)=∫_{-∞}^{∞} x(τ)h(t-τ)dτ.
- Hệ nhân quả: (x*h)(t)=∫_0^t x(τ)h(t-τ)dτ.

### 19.2. Ví dụ tích luỹ chất ô nhiễm (mẫu hoá)
- y(t)=∫_0^t (inflow)(τ)·(kernel)(t-τ)dτ.

### 19.3. Tính chất
- Giao hoán: x*h = h*x.
- Kết hợp: (x*h1)*h2 = x*(h1*h2).
- Đồng nhất: x*δ = x.

---

## 20. Laplace Transform Technique: Cover-up (Partial Fractions)
### 20.0.1. Định nghĩa & tuyến tính  
- F(s)=𝓛{f(t)}=∫_0^∞ e^{-st} f(t) dt  
- 𝓛{a f(t)+b g(t)} = aF(s)+bG(s)

### 20.0.2. Các cặp cơ bản 
- 𝓛{1} = 1/s  
- 𝓛{t^n} = n!/s^{n+1}, n=0,1,2,...  
- 𝓛{e^{at}} = 1/(s-a)  
- 𝓛{cos(ωt)} = s/(s^2+ω^2)  
- 𝓛{sin(ωt)} = ω/(s^2+ω^2)

### 20.0.3. Completing the square (dạng chuẩn hay dùng)  
- 𝓛^{-1}{(s-a)/((s-a)^2+ω^2)} = e^{at}cos(ωt)u(t)  
- 𝓛^{-1}{ω/((s-a)^2+ω^2)} = e^{at}sin(ωt)u(t)

### 20.1. Định nghĩa & trường hợp đơn giản
- F(s)=L{f(t)}=∫_0^∞ e^{-st}f(t)dt.
- L^{-1}{1/(s-a)} = e^{at}u(t).

### 20.2. Cực lặp
- L^{-1}{1/(s-a)^n} = t^{n-1}e^{at}/(n-1)! · u(t).

### 20.3. Hoàn bình phương
- 1/((s-a)^2+ω^2) ↔ e^{at}·(1/ω)sin(ωt)u(t).
- (s-a)/((s-a)^2+ω^2) ↔ e^{at}cos(ωt)u(t).

### 20.4. Cover-up phức
- Với cực phức liên hợp a±iω: ghép cặp để ra dạng sin/cos thực.

### 20.5. Phân tích thành phần
- Với F(s)=N(s)/D(s), D phân tích được ⇒ tách phân số riêng để lấy L^{-1}.

---

## 21. Laplace & Generalized Functions
### 21.1. Laplace của δ và u
- L{δ(t)}=1.
- L{δ(t-a)}=e^{-as}.
- L{u(t)}=1/s.

### 21.2. “Laplace không nói gì”
- Không tự động mã hoá đầy đủ hành vi tại t=0 nếu có xung/nhảy; cần dùng điều kiện đầu một phía (0+).

### 21.3. Cẩn thận tại t=0
- Dùng f(0+), f'(0+)…; phân biệt với giá trị “trước 0” nếu có.

### 21.4. Quy tắc đạo hàm theo t
- L{f'(t)} = sF(s) - f(0+).
- Tổng quát: L{f^{(n)}} = s^nF - s^{n-1}f(0+) - ... - f^{(n-1)}(0+).

### 21.5. Initial singularity (ý chính)
- Nếu f có bước nhảy tại 0 ⇒ f' chứa δ; khi biến đổi Laplace phải cộng các hạng f(0+) phù hợp.


### 21.6. Dịch mũ (Exponential shift)
- 𝓛{e^{at} f(t)} = F(s-a)

### 21.7. Dịch thời gian (Heaviside shift)
- 𝓛{u(t-a) f(t-a)} = e^{-as} F(s), a>0  
- Hệ quả: 𝓛{u(t-a)} = e^{-as}/s

### 21.8. Co giãn thời gian (Time scaling)
- 𝓛{f(ct)} = (1/c) F(s/c), c>0

### 21.9. Nhân với t (đạo hàm theo s)
- 𝓛{t f(t)} = - dF/ds  
- Tổng quát: 𝓛{t^n f(t)} = (-1)^n d^nF/ds^n

### 21.10. Final Value Formula (khi điều kiện áp dụng thỏa)
- lim_{t→∞} f(t) = lim_{s→0} sF(s)  
  (đúng khi mọi pole của sF(s) nằm ở nửa trái, trừ có thể tại s=0)

### 21.11. Initial value theorem
- lim_{t→0+} f(t) = lim_{s→∞} sF(s) (khi các điều kiện phù hợp).

### 21.12. Gắn điều kiện đầu
- Giải ODE bằng Laplace: biến đổi hai vế + thay điều kiện đầu vào các hạng sF(s)-f(0+).

---

## 22. Pole Diagram & Laplace Transform
### 22.1. Poles (cực) và biểu đồ cực
- Pole: nghiệm của D(s)=0 trong F(s)=N(s)/D(s).

### 22.2. Pole diagram của Laplace
- Vị trí cực quyết định dạng thời gian:
  - Re(p)<0 ⇒ thành phần suy giảm e^{Re(p)t}.
  - Re(p)=0 ⇒ dao động bền (nếu không bội >1).
  - Re(p)>0 ⇒ tăng (mất ổn định).

### 22.3. Tích phân Laplace
- F(s)=∫_0^∞ e^{-st}f(t)dt: hội tụ khi s nằm trong ROC.

### 22.4. Inverse Laplace (ý chính)
- L^{-1} bằng phân tích phân số riêng / bảng biến đổi / residue (ý niệm).

---

## 23. Amplitude Response & Pole Diagram
- Với H(s)=K·∏(s-z_i)/∏(s-p_i):
  - |H(iω)| = |K|·∏|iω - z_i| / ∏|iω - p_i|.
  - ∠H(iω)=∠K + Σ∠(iω-z_i) - Σ∠(iω-p_i).
- “Gần cực” ⇒ biên độ lớn; gần zero ⇒ biên độ nhỏ.

---

## 24. Laplace Transform & General LTI Systems
### 24.1. Zeros: “stillness in motion”
- Zero: nghiệm N(s)=0 (triệt đáp ứng tại một tần/điểm mũ nhất định).
- Nếu H(iω0)=0 ⇒ vào sin ω0 không tạo ra steady-state ở ω0.

### 24.2. Hệ LTI tổng quát
- Transfer function: H(s)=Y(s)/X(s) (điều kiện đầu = 0).
- Convolution theorem: L{x*h}=X(s)H(s).
- Time shift: L{u(t-a)f(t-a)}=e^{-as}F(s).
- Frequency response: H(iω) (nếu ổn định/đủ điều kiện).

---

## 25. First Order Systems & Second Order Equations
### 25.1. Companion system (đưa về hệ bậc 1)
- Với y'' + a1 y' + a0 y = x(t):
  - x1=y, x2=y'
  - x1' = x2
  - x2' = -a0 x1 - a1 x2 + x(t)
- Dạng ma trận: x' = A x + b x(t).

### 25.2. Bài toán giá trị ban đầu (IVP)
- Cho x(t0)=x0 ⇒ nghiệm duy nhất nếu vế phải “đủ trơn” (Lipschitz theo x).

---

## 26. Phase Portraits in Two Dimensions
### 26.1. Phase portrait & eigenvectors
- Hệ tuyến tính: x' = A x.
- Nghiệm: x(t)=e^{At}x(0).
- Nếu A có eigenpair (λ,v): thành phần theo v ~ e^{λt}.

### 26.2. Mặt phẳng (tr, det) & ổn định cấu trúc
- Char poly: λ^2 - (tr A)λ + det A = 0.
- Δ = (tr A)^2 - 4 det A.
- Phân loại nhanh (2D):
  - det<0 ⇒ saddle (không ổn định).
  - det>0, Δ>0 ⇒ node (ổn định nếu tr<0; không ổn định nếu tr>0).
  - det>0, Δ<0 ⇒ spiral/focus (ổn định nếu tr<0; không ổn định nếu tr>0).
  - det>0, tr=0, Δ<0 ⇒ center (biên ổn; thường không “structurally stable”).

### 26.3. Portrait gallery (mẫu nghiệm)
- λ=α±iβ ⇒ x(t)=e^{αt}(C1 Re(e^{iβt}v)+C2 Im(e^{iβt}v)).
- α<0 ⇒ cuộn vào gốc; α>0 ⇒ cuộn ra; α=0 ⇒ quỹ đạo kín (lý tưởng hoá).

## A. Laplace Transform — bảng công thức tối thiểu (1 phía, từ 0→∞)
### A.1. Định nghĩa & tính tuyến tính
- F(s)=L{f(t)}=∫_0^∞ e^{-st} f(t) dt
- L{a f + b g} = aF + bG

### A.2. Cặp biến đổi cơ bản
- L{1} = 1/s
- L{t^n} = n!/s^{n+1}, n=0,1,2,...
- L{e^{at}} = 1/(s-a)
- L{cos(ωt)} = s/(s^2+ω^2)
- L{sin(ωt)} = ω/(s^2+ω^2)

### A.3. Dịch mũ (exponential shift)
- L{e^{at} f(t)} = F(s-a)

### A.4. Dịch thời gian (Heaviside shift)
- L{u(t-a) f(t-a)} = e^{-as} F(s), a>0

### A.5. Nhân t (đạo hàm theo s)
- L{t f(t)} = - dF/ds
- Tổng quát: L{t^n f(t)} = (-1)^n d^nF/ds^n

### A.6. Đạo hàm theo t (kèm điều kiện đầu 0+)
- L{f'(t)} = sF(s) - f(0+)
- L{f''(t)} = s^2F(s) - s f(0+) - f'(0+)

### A.7. Tích chập
- L{(f*g)(t)} = F(s)G(s)
- (f*g)(t)=∫_0^t f(τ)g(t-τ)dτ (hệ nhân quả)

### A.8. Initial/Final Value (khi điều kiện áp dụng thỏa)
- f(0+) = lim_{s→∞} sF(s)
- lim_{t→∞} f(t) = lim_{s→0} sF(s)  (nếu mọi pole của sF(s) ở nửa trái, trừ có thể tại s=0)