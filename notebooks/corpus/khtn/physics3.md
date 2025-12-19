# Vật lý đại cương III

## 0. Hằng số & ký hiệu nhanh
0.1. Hằng số
- c: vận tốc ánh sáng
- h = 6.625×10^-34 J·s ; ħ = h/(2π)
- e: điện tích electron ; m_e: khối lượng electron ; ε0: hằng số điện môi chân không
- σ = 5.67×10^-8 W/(m^2·K^4) (Stefan–Boltzmann)
- b = 2.896×10^-3 m·K (Wien)
- λ_C = h/(m_e c) ≈ 2.4×10^-12 m (Compton)
0.2. Ký hiệu quang học
- Quang lộ: L = n·(độ dài hình học) ; hiệu quang lộ: ΔL = L1 − L2
- Bước sóng: λ ; tần số: f ; ω = 2πf ; số sóng: k = 2π/λ
- Cường độ: I ; biên độ: a
- Góc: i (góc tới), θ/φ/α (góc theo ngữ cảnh)

## 1. Giao thoa ánh sáng
1.1. Hai nguồn kết hợp (coherent)
- Cực đại (vân sáng): ΔL = kλ, k = 0, ±1, ±2, ...
- Cực tiểu (vân tối): ΔL = (k + 1/2)λ, k = 0, ±1, ±2, ...
- Nếu môi trường là không khí/chân không: ΔL = r1 − r2

1.2. Giao thoa Young (hai khe)
- Vân sáng bậc k: x_s(k) = k·λD/a
- Vân tối thứ k: x_t(k) = (k + 1/2)·λD/a
- Khoảng vân: i = λD/a
(Ghi chú: a = khoảng cách 2 khe (nguồn kết hợp), D = khoảng cách đến màn, x đo trên màn)

1.3. Young + đặt bản mỏng (dày e, chiết suất n) chắn 1 khe
- Vận tốc trong môi trường: v = c/n
- Tia bị “kéo dài quang lộ” thêm: (n − 1)e  → ΔL thay đổi
- Độ dời vân trung tâm: x_0 = (n − 1)e·D/a (hệ vân dịch về phía khe có đặt bản mỏng)

1.4. Young + dịch chuyển nguồn S (song song S1S2)
- Hệ vân dịch ngược chiều, khoảng vân i không đổi
- Độ dời hệ vân (theo notes): x_0 = (D/d)·x   (ký hiệu D, d, x theo hình bài)

1.5. Giao thoa trên bản mỏng có bề dày thay đổi (vân cùng độ dày)
1.5.1. Hiệu quang lộ (hai tia phản xạ trên 2 mặt bản mỏng)
- Theo notes: ΔL = 2dn·sin(i) − λ/2
  (d: bề dày tại điểm xét; n: chiết suất; i: góc tới)
- Điều kiện:
  + Vân sáng: ΔL = kλ
  + Vân tối:  ΔL = (k + 1/2)λ

1.5.2. Nêm không khí (air wedge)
- Vân tối: 2d_t = kλ  (k = 0,1,2,...)
- Vân sáng: 4d_s = (2k − 1)λ  (k = 1,2,3,...)

1.5.3. Vân tròn Newton
- Vân tối: 2d_t = kλ
- Vân sáng: 4d_s = (2k − 1)λ
- Bán kính vân tối thứ k: r_k^2 = kλR  (R: bán kính cong thấu kính)

## 2. Nhiễu xạ ánh sáng
2.1. Phương pháp đới cầu Fresnel
2.1.1. Cách chia đới
- Chọn mặt sóng cầu Σ phát từ O (bán kính R), điểm quan sát M cách đới 1 khoảng b
- Dùng các mặt cầu tâm M có bán kính: b, b+λ/2, b+2·λ/2, ... để chia Σ thành các đới Fresnel

2.1.2. Công thức Fresnel
- Diện tích mỗi đới: ΔΣ = π·(Rb/(R+b))·λ
- Bán kính đới thứ k: r_k^2 = k·(Rb/(R+b))·λ   (k = 1,2,3,...)
- Biên độ tổng tại M (xấp xỉ):
  a = a1 − a2 + a3 − a4 + ...
  Nếu a_k biến thiên chậm → a_n ≈ ±a_n/2 ; n→∞ → a_∞ ≈ a1/2

2.2. Sóng cầu qua lỗ tròn nhỏ (lỗ chứa n đới Fresnel)
- Biên độ tại M: a_M = a1 − a2 + ... ± a_n ≈ ±a_n/2
- Nếu n lẻ (dấu “+”): I_M ∝ ( (2n+1)/(2n) )^2·I0  (dạng theo notes)
- Nếu n chẵn (dấu “−”): I_M ∝ ( (2n−1)/(2n) )^2·I0  (dạng theo notes)
- n→∞: I_M = I0/4
- Trường hợp đặc biệt (theo notes): n=2 → I≈0 ; n=1 → I=I0

2.3. Sóng cầu qua đĩa tròn nhỏ (che khuất m đới)
- a_M = a_{m+1} − a_{m+2} + ... ≈ a_{m+1} (vì n lớn → a_n→0)
- Che nhiều đới → M tối dần (I_M→0)
- Che ít đới → I_M xấp xỉ I0/4

2.4. Nhiễu xạ Fraunhofer qua khe hẹp chữ nhật (bề rộng khe b, tới vuông góc)
- Gọi φ là góc lệch:
  + Cực đại giữa: φ0 = 0
  + Cực tiểu bậc k (k≠0): sinφ_k = kλ/b, k = ±1, ±2, ...
  + Cực đại bậc k: sinφ_k ≈ (k + 1/2)λ/b, k = ±1, ±2, ...

2.5. Nhiễu xạ qua cách tử phẳng (chu kỳ d)
- Tới vuông góc: sinθ_k = kλ/d, k = ±1, ±2, ...
- Tới xiên (góc tới α): ΔL = d(sinθ − sinα)
  Cực đại: sinθ − sinα = kλ/d

2.6. Nhiễu xạ tia X trên tinh thể (định luật Bragg)
- Hiệu quang lộ giữa hai lớp: ΔL = 2d·sinθ
- Cực đại: 2d·sinθ = kλ, k = 1,2,3,...

## 3. Phân cực ánh sáng
3.1. Định luật Malus
- I = I0·cos^2θ (θ: góc giữa quang trục kính phân cực & kính phân tích)
- Ánh sáng chưa phân cực qua 1 kính phân cực (bỏ hấp thụ/phản xạ): I = I0/2

3.2. Quay mặt phẳng phân cực
3.2.1. Tinh thể đơn trục
- Góc quay: φ = [α]·ρ·d
  ([α]: góc quay riêng; ρ: khối lượng riêng; d: bề dày bản)

3.2.2. Chất vô định hình (quang hoạt)
- Góc quay: φ = [α]·C·d
  (C: nồng độ dung dịch; d: chiều dài lớp dung dịch)
- Ứng dụng: phân cực kế đo C

## 4. Quang học lượng tử
4.1. Vật đen tuyệt đối (VĐTĐ)
- ĐN: hấp thụ hoàn toàn mọi bức xạ đơn sắc chiếu tới
- Stefan–Boltzmann: R_T = σT^4
- Wien: λ_max·T = b
- Planck (năng suất phát xạ đơn sắc):
  + Theo tần số f:
    ε_{f,T} = (2πh f^3 / c^2) / (e^{hf/(kT)} − 1)
  + Theo bước sóng λ:
    ε_{λ,T} = (2πh c^2 / λ^5) / (e^{hc/(λkT)} − 1)
  + Liên hệ: ε_{λ,T} dλ = ε_{f,T} df

4.2. Vật xám (không tuyệt đối)
- R'_T = α·σT^4  (α: hệ số hấp thụ)

4.3. Phát xạ cân bằng (vật ở nhiệt độ T)
- Hệ số phát xạ đơn sắc: r_{T,λ} = dR_T/dλ
- Liên hệ toàn phần–đơn sắc: R_T = ∫_0^∞ r_{T,λ} dλ

4.4. Photon & quang điện
4.4.1. Photon
- Năng lượng: E = hf = hc/λ
- Khối lượng tương đương: m = E/c^2 = hf/c^2
- Động lượng: p = E/c = h/λ

4.4.2. Hiện tượng quang điện
- Giới hạn đỏ: λ0 = hc/A  (A: công thoát)
- Einstein: hf = A + W_max = A + (1/2)m v_max^2
- Hiệu điện thế hãm: eU_h = W_max

4.5. Hiệu ứng Compton
- Bước sóng Compton: λ_C = h/(m_e c)
- Độ dời bước sóng: Δλ = λ' − λ = 2λ_C·sin^2(θ/2)

## 5. Cơ học lượng tử
5.1. Hệ thức De Broglie
- E = hf = ħω
- p = h/λ = ħk
- k = 2π/λ ; ω = 2πf
- Vận tốc pha: v_p = ω/k

5.2. Hạt tích điện gia tốc bởi hiệu điện thế U
- Năng lượng động học: W = eU
- Động lượng (phi tương đối tính): p^2/(2m) = eU  ⇒ p = √(2meU)
- Bước sóng De Broglie:
  + Newton (v<<c): λ = h/p = h/(mv) = h/√(2mW) = h/√(2meU)
  + Tương đối tính (dùng khi eU lớn):
    λ = h / √(2m0 eU (1 + eU/(2m0 c^2)))
    (tương đương: λ = hc / √(eU(2m0 c^2 + eU)))

5.3. Bất định Heisenberg
- Δx·Δp_x ≥ ħ
- ΔE·Δt ≥ ħ

5.4. Phương trình Schrödinger
5.4.1. Dạng tổng quát (phụ thuộc thời gian)
- iħ ∂ψ/∂t = −(ħ^2/2m)Δψ + Uψ

5.4.2. Trạng thái dừng (U chỉ phụ thuộc r)
- ψ(r,t) = ψ(r)·e^{−iEt/ħ}
- Phương trình độc lập thời gian:
  −(ħ^2/2m)Δψ + Uψ = Eψ
  ⇔ Δψ + (2m/ħ^2)(E − U)ψ = 0
- Laplacian: Δ = ∂^2/∂x^2 + ∂^2/∂y^2 + ∂^2/∂z^2
- Điều kiện ψ: đơn trị, liên tục, ψ→0 khi r→∞
- Điều kiện nối tại x0: ψ_I(x0)=ψ_II(x0) và (dψ/dx)_I|(x0)=(dψ/dx)_II|(x0)

5.5. Giếng thế năng vô hạn 1D (0<x<a)
- U(x)=0 (0<x<a), U=∞ (x≤0 hoặc x≥a)
- Hàm sóng riêng:
  ψ_n(x) = √(2/a) · sin(nπx/a), n=1,2,3,...
- Mức năng lượng:
  E_n = (n^2 π^2 ħ^2)/(2 m a^2)

## 6. Nguyên tử – phân tử
6.1. Nguyên tử Hydro (Z=1)
6.1.1. Thế năng Coulomb
- U(r) = − Z e^2 / (4π ε0 r)

6.1.2. Schrödinger & tọa độ cầu
- Bài toán đối xứng cầu → dùng (r, θ, φ)
- Phân ly biến:
  ψ(r,θ,φ) = R_{nl}(r) · Y_{lm}(θ,φ)
- Số lượng tử:
  n = 1,2,3,...
  l = 0,1,2,...,n−1
  m = 0, ±1, ±2, ..., ±l

6.1.3. Năng lượng mức n
- E_n = − Rh / n^2  (dạng theo notes)
- Hằng số Rydberg (theo notes, dạng tần số): R ≈ 3.29×10^15 s^-1

6.2. Nguyên tử kim loại kiềm (electron hoá trị)
- Trạng thái phụ thuộc (n,l,m); năng lượng phụ thuộc (n,l)
- Năng lượng:
  E_{n,l} = − Rh / (n + x_l)^2
  (x_l: số bổ chính Rydberg, phụ thuộc l và nguyên tử)
- Tần số bức xạ khi chuyển mức:
  f = R[ 1/(n1 + x)^2 − 1/(n2 + x)^2 ]
- Quy tắc chọn (chuyển trạng thái): Δl = ±1
- Ký hiệu số hạng quang phổ: nX, với X = S,P,D,F,... ứng với l = 0,1,2,3,...
- Vạch cộng hưởng (ví dụ): Li(2P→2S), Na(3P→3S)
