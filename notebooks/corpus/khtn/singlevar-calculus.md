# Notes Giải tích một biến

## CHAPTER 2 — Limits and Derivatives

### 1) Các giới hạn chuẩn + dạng tương đương hay dùng
- \(\displaystyle \lim_{x\to 0}\frac{\sin x}{x}=1,\quad \lim_{x\to 0}\frac{\tan x}{x}=1,\quad \lim_{x\to 0}\frac{1-\cos x}{x^2}=\frac12\)
- Tương đương khi \(x\to 0\):
  - \(\sin x \sim x\), \(\tan x \sim x\), \(\arcsin x \sim x\), \(\arctan x \sim x\)
  - \(1-\cos x \sim \dfrac{x^2}{2}\)
  - \(e^x-1 \sim x\), \(\ln(1+x)\sim x\)
  - \((1+x)^\alpha - 1 \sim \alpha x\) (hằng \(\alpha\))
- Các giới hạn mũ–log chuẩn:
  - \(\displaystyle \lim_{x\to 0}(1+x)^{1/x}=e\)
  - \(\displaystyle \lim_{n\to\infty}\left(1+\frac{a}{n}\right)^n=e^a\)
- Dạng “tương đương log”:
  - Nếu \(u(x)\to 0\) thì \(\ln(1+u)\sim u\) ⇒ \(\displaystyle (1+u)^{v}=\exp(v\ln(1+u))\) rất hữu dụng cho \(0^0,1^\infty,\infty^0\).

### 2) Kẹp (Squeeze) và bất đẳng thức chuẩn cho giới hạn
- \(|\sin x|\le |x|\) (mọi \(x\)), và với \(x>0\): \(\sin x < x < \tan x\).
- \(1-\cos x \le \dfrac{x^2}{2}\) (mọi \(x\)).
- \(\ln(1+x)\le x\) (với \(x>-1\)); \(e^x\ge 1+x\) (mọi \(x\)).
- **Bernoulli**: \((1+x)^\alpha \ge 1+\alpha x\) khi \(x>-1,\ \alpha\ge 1\) (và đảo chiều phù hợp khi \(0\le\alpha\le 1\)).

### 3) Liên tục: hệ quả hay dùng
- Nếu \(f\) liên tục trên \([a,b]\) ⇒ đạt \(\min,\max\) (Weierstrass).
- Nếu \(f\) liên tục và \(f(a)f(b)<0\) ⇒ tồn tại \(c\in(a,b)\) sao cho \(f(c)=0\) (Định lý giá trị trung gian).
- Liên tục + đơn điệu ⇒ có nghịch đảo liên tục; nếu \(f'(x_0)\ne 0\) thì \((f^{-1})'(f(x_0))=\dfrac{1}{f'(x_0)}\).

### 4) Quy tắc đạo hàm “hơi nâng cao”
- Đạo hàm hàm hợp (Chain rule): \((f\circ g)'(x)=f'(g(x))g'(x)\).
- Đạo hàm hàm ngược: \((f^{-1})'(y)=\dfrac{1}{f'(x)}\) với \(y=f(x)\), \(f'(x)\ne 0\).
- Đạo hàm ẩn: nếu \(F(x,y)=0\), \(F_y\ne 0\) thì \(\displaystyle \frac{dy}{dx}=-\frac{F_x}{F_y}\).
- Đạo hàm theo tham số: \(y=y(t), x=x(t)\), \(x'(t)\ne 0\):
  \[
  \frac{dy}{dx}=\frac{dy/dt}{dx/dt},\qquad
  \frac{d^2y}{dx^2}=\frac{d}{dt}\left(\frac{dy}{dx}\right)\Big/\frac{dx}{dt}.
  \]

---

## CHAPTER 3 — Applications of Derivatives

### 1) Định lý giá trị trung bình (MVT) và hệ quả
- **Rolle**: \(f\) liên tục \([a,b]\), khả vi \((a,b)\), \(f(a)=f(b)\) ⇒ \(\exists c: f'(c)=0\).
- **MVT**: \(\exists c\in(a,b)\) sao cho \(\displaystyle f'(c)=\frac{f(b)-f(a)}{b-a}\).
- **Cauchy MVT**: \(\exists c\) sao cho \(\displaystyle \frac{f'(c)}{g'(c)}=\frac{f(b)-f(a)}{g(b)-g(a)}\) (dùng để chứng minh L’Hôpital).
- Hệ quả “ước lượng sai số tuyến tính”: nếu \(|f'(x)|\le M\) trên \([a,b]\) ⇒ \(|f(b)-f(a)|\le M|b-a|\) (Lipschitz).

### 2) Đơn điệu, cực trị, độ cong
- Nếu \(f'(x)>0\) trên khoảng ⇒ \(f\) tăng; \(f'(x)<0\) ⇒ \(f\) giảm.
- **Kiểm tra cực trị (đạo hàm 1)**: đổi dấu của \(f'\) qua \(x_0\).
- **Kiểm tra cực trị (đạo hàm 2)**: \(f'(x_0)=0\), \(f''(x_0)>0\) ⇒ cực tiểu; \(f''(x_0)<0\) ⇒ cực đại.
- **Lồi/lõm**: \(f''\ge 0\) ⇒ lồi; \(f''\le 0\) ⇒ lõm. Điểm uốn khi \(f''\) đổi dấu (không chỉ \(f''=0\)).

### 3) Newton’s Method (nghiệm phương trình)
- Lặp Newton: \(\displaystyle x_{n+1}=x_n-\frac{f(x_n)}{f'(x_n)}\).
- Hội tụ nhanh bậc 2 gần nghiệm đơn \(r\) nếu \(f'(r)\ne 0\) và khởi tạo đủ gần.

### 4) Related Rates / xấp xỉ vi phân
- Tuyến tính hóa tại \(a\): \(\displaystyle f(a+\Delta x)\approx f(a)+f'(a)\Delta x\).
- Sai số xấp xỉ (từ Taylor bậc 1): \(\displaystyle f(a+\Delta x)-[f(a)+f'(a)\Delta x]=\frac{f''(\xi)}{2}(\Delta x)^2\).

---

## CHAPTER 4 — Additional Concepts (Differentials / Approximations)
- Vi phân: \(dy=f'(x)\,dx\). Với \(\Delta x\) nhỏ: \(\Delta y\approx dy\).
- Truyền sai số tương đối (hay gặp):
  \[
  \frac{d(\ln y)}{dx}=\frac{y'}{y}
  \quad\Rightarrow\quad
  \frac{\Delta y}{y}\approx \frac{dy}{y}.
  \]
- Nếu \(y=uv\): \(\displaystyle \frac{dy}{y}\approx \frac{du}{u}+\frac{dv}{v}\) (xấp xỉ sai số tương đối).

---

## CHAPTER 5 — Elementary Transcendental Functions

### 1) Log–Exp các “mẹo” hay dùng
- Đổi dạng mũ: \(a^{g(x)}=e^{g(x)\ln a}\) (với \(a>0\)).
- Dạng \(u(x)^{v(x)}\): viết \(y=u^v\Rightarrow \ln y=v\ln u\) rồi lấy đạo hàm.
- Giới hạn tạo \(e\): nếu \(u\to 0\) thì \((1+u)^{1/u}\to e\); tổng quát \((1+u)^{v}\to e^{\lim uv}\) khi \(u\to 0,\ v\to\infty\) và \(uv\to L\).

### 2) Hyperbolic (ít hiển nhiên nhưng hay hỏi)
- \(\sinh x=\dfrac{e^x-e^{-x}}{2},\ \cosh x=\dfrac{e^x+e^{-x}}{2}\).
- \(\cosh^2x-\sinh^2x=1\).
- \((\sinh x)'=\cosh x,\ (\cosh x)'=\sinh x,\ (\tanh x)'=\operatorname{sech}^2 x\).

---

## CHAPTER 6 — Definite Integrals

### 1) FTC và hệ quả nhanh
- **FTC I**: \(F(x)=\int_a^x f(t)\,dt\) (liên tục) ⇒ \(F'(x)=f(x)\).
- **FTC II**: nếu \(F'=f\) thì \(\int_a^b f(x)\,dx=F(b)-F(a)\).
- Công thức Leibniz (cận biến thiên):
  \[
  \frac{d}{dx}\int_{\alpha(x)}^{\beta(x)} f(t)\,dt
  =f(\beta(x))\beta'(x)-f(\alpha(x))\alpha'(x).
  \]

### 2) Đổi biến & từng phần (dạng định tích phân)
- Đổi biến: \(x=g(u)\) đơn điệu, khả vi:
  \[
  \int_{x=a}^{b} f(x)\,dx=\int_{u=g^{-1}(a)}^{g^{-1}(b)} f(g(u))g'(u)\,du.
  \]
- Từng phần: \(\displaystyle \int_a^b u\,dv=[uv]_a^b-\int_a^b v\,du\).

### 3) Tính chất đối xứng (rất hay dùng)
- Nếu \(f\) lẻ: \(\displaystyle \int_{-a}^{a} f(x)\,dx=0\).
- Nếu \(f\) chẵn: \(\displaystyle \int_{-a}^{a} f(x)\,dx=2\int_0^a f(x)\,dx\).
- Trên \([0,a]\): \(\displaystyle \int_0^a f(x)\,dx=\int_0^a f(a-x)\,dx\).
- Suy ra: \(\displaystyle \int_0^a f(x)+f(a-x)\,dx = 2\int_0^a f(x)\,dx\) (dùng “ghép cặp”).

### 4) Bất đẳng thức tích phân hay dùng
- Nếu \(m\le f\le M\) trên \([a,b]\) ⇒ \(m(b-a)\le \int_a^b f \le M(b-a)\).
- (So sánh) \(0\le f\le g\) ⇒ \(\int f\le \int g\).
- (Cauchy–Schwarz) \(\left(\int_a^b fg\right)^2\le \left(\int_a^b f^2\right)\left(\int_a^b g^2\right)\).

### 5) Improper integrals — test nhanh
- **p-test**: \(\displaystyle \int_1^\infty \frac{dx}{x^p}\) hội tụ ⇔ \(p>1\).
- Gần 0: \(\displaystyle \int_0^1 \frac{dx}{x^p}\) hội tụ ⇔ \(p<1\).
- So sánh: nếu \(0\le f\le g\) và \(\int g\) hội tụ ⇒ \(\int f\) hội tụ.
- So sánh giới hạn: nếu \(\lim_{x\to\infty}\frac{f}{g}=c\in(0,\infty)\) ⇒ \(\int f\) và \(\int g\) cùng tính hội tụ.

---

## CHAPTER 7 — Indefinite Integration (kỹ thuật “ăn điểm”)
- **Đổi biến (u-sub)**: chọn \(u=\varphi(x)\) để xuất hiện \(du=\varphi'(x)dx\).
- **Từng phần (IBP)**: \(\int u\,dv=uv-\int v\,du\) (chọn \(u\) giảm độ phức tạp).
- **Hữu tỉ**:
  - \(\int \frac{P(x)}{Q(x)}dx\): chia đa thức nếu \(\deg P\ge \deg Q\), rồi phân tích thành phân thức đơn.
- **Mẫu bậc hai** (hay ra):
  - \(\displaystyle \int \frac{dx}{x^2+a^2}=\frac{1}{a}\arctan\frac{x}{a}+C\)
  - \(\displaystyle \int \frac{dx}{a^2-x^2}=\frac{1}{2a}\ln\left|\frac{a+x}{a-x}\right|+C\)
- **Trig substitutions**:
  - \(a^2-x^2\): \(x=a\sin\theta\)
  - \(a^2+x^2\): \(x=a\tan\theta\)
  - \(x^2-a^2\): \(x=a\sec\theta\)
- **Tích phân dạng mũ–lượng giác** (mẹo tuyến tính):
  - Với \(\int e^{ax}\sin bx\,dx\), \(\int e^{ax}\cos bx\,dx\): đặt \(I\), \(J\) rồi IBP hai lần để giải hệ.

---

## CHAPTER 8 — Vectors / Parametric / Polar (phần 1 biến theo tham số)

### 1) Đường cong tham số
- Tiếp tuyến: \(\displaystyle \frac{dy}{dx}=\frac{y'(t)}{x'(t)}\).
- Độ dài cung: \(\displaystyle L=\int_{t_0}^{t_1}\sqrt{(x')^2+(y')^2}\,dt\).
- Diện tích (Green dạng đơn giản cho tham số):
  \[
  A=\int_{t_0}^{t_1} y\,dx=\int_{t_0}^{t_1} y(t)\,x'(t)\,dt
  \quad (\text{với định hướng phù hợp}).
  \]
- Độ cong (curvature):
  \[
  \kappa=\frac{|x'y''-y'x''|}{\left((x')^2+(y')^2\right)^{3/2}}.
  \]

### 2) Tọa độ cực (polar)
- Liên hệ: \(x=r\cos\theta,\ y=r\sin\theta\).
- Đạo hàm dốc: \(\displaystyle \frac{dy}{dx}=\frac{r'\sin\theta+r\cos\theta}{r'\cos\theta-r\sin\theta}\).
- Diện tích miền cực: \(\displaystyle A=\frac12\int_{\alpha}^{\beta} r(\theta)^2\,d\theta\).
- Độ dài cung cực: \(\displaystyle L=\int_{\alpha}^{\beta}\sqrt{r^2+(r')^2}\,d\theta\).

---

## CHAPTER 12 — Approximations (Taylor, Simpson, L’Hôpital)

### 1) Taylor/Maclaurin + dạng dư (rất hay dùng)
- Taylor tại \(a\):
  \[
  f(x)=\sum_{k=0}^{n}\frac{f^{(k)}(a)}{k!}(x-a)^k + R_n(x).
  \]
- Dư Lagrange:
  \[
  R_n(x)=\frac{f^{(n+1)}(\xi)}{(n+1)!}(x-a)^{n+1},\quad \xi \text{ giữa } a \text{ và } x.
  \]
- Dư dạng \(O\): nếu \(f^{(n+1)}\) bị chặn gần \(a\) ⇒ \(R_n(x)=O((x-a)^{n+1})\).

### 2) Khai triển chuẩn cần thuộc (kèm sai số)
- \(e^x=1+x+\dfrac{x^2}{2!}+\dfrac{x^3}{3!}+O(x^4)\).
- \(\ln(1+x)=x-\dfrac{x^2}{2}+\dfrac{x^3}{3}+O(x^4)\) (|x|<1; dùng làm tiệm cận khi \(x\to 0\)).
- \((1+x)^\alpha=1+\alpha x+\dfrac{\alpha(\alpha-1)}{2}x^2+O(x^3)\).
- \(\sin x=x-\dfrac{x^3}{3!}+O(x^5)\), \(\cos x=1-\dfrac{x^2}{2!}+O(x^4)\).
- \(\arctan x=x-\dfrac{x^3}{3}+O(x^5)\).

### 3) L’Hôpital (điều kiện + biến dạng)
- Áp dụng cho \(0/0\) hoặc \(\infty/\infty\) khi \(f,g\) khả vi và \(g'\ne 0\):
  \[
  \lim \frac{f}{g} = \lim \frac{f'}{g'} \quad (\text{nếu giới hạn RHS tồn tại/hội tụ}).
  \]
- Biến dạng:
  - \(0\cdot\infty\): đổi thành \(\frac{0}{0}\) hoặc \(\frac{\infty}{\infty}\) bằng nhân/chia.
  - \(\infty-\infty\): quy đồng / nhân liên hợp / đưa về log.
  - \(1^\infty, 0^0, \infty^0\): đặt \(y=u^v\Rightarrow \ln y=v\ln u\) rồi dùng L’Hôpital cho \(\ln y\).

### 4) Simpson’s Rule + sai số
- Quy tắc Simpson (n chẵn, \(h=\frac{b-a}{n}\)):
  \[
  \int_a^b f(x)\,dx \approx \frac{h}{3}\Big[f(x_0)+4\sum_{\text{i lẻ}} f(x_i)+2\sum_{\text{i chẵn, }i\ne 0,n} f(x_i)+f(x_n)\Big].
  \]
- Sai số: nếu \(f^{(4)}\) liên tục và \(\max|f^{(4)}|\le M\) trên \([a,b]\) thì
  \[
  |E_S|\le \frac{(b-a)}{180}h^4\,M.
  \]

---

## CHAPTER 13 — Series (chuỗi số & chuỗi hàm)

### 1) Test hội tụ quan trọng
- **So sánh trực tiếp**: \(0\le a_n\le b_n\), \(\sum b_n\) hội tụ ⇒ \(\sum a_n\) hội tụ.
- **So sánh giới hạn**: \(a_n,b_n>0\), \(\lim \frac{a_n}{b_n}=c\in(0,\infty)\) ⇒ cùng tính hội tụ.
- **Tỉ số (D’Alembert)**: \(L=\limsup\left|\frac{a_{n+1}}{a_n}\right|\).
  - \(L<1\) hội tụ tuyệt đối; \(L>1\) phân kỳ.
- **Căn (Cauchy)**: \(L=\limsup \sqrt[n]{|a_n|}\) tương tự.
- **Tích phân**: \(a_n=f(n)\), \(f\) dương, giảm ⇒ \(\sum a_n\) hội tụ ⇔ \(\int_1^\infty f(x)\,dx\) hội tụ.
- **Luân phiên (Leibniz)**: \(\sum (-1)^n b_n\), \(b_n\downarrow 0\) ⇒ hội tụ; sai số cắt cụt \(|R_N|\le b_{N+1}\).
- Chuỗi \(p\): \(\sum \frac{1}{n^p}\) hội tụ ⇔ \(p>1\).

### 2) Chuỗi lũy thừa & bán kính hội tụ
- \(\sum c_n(x-a)^n\) có bán kính \(R\):
  - hội tụ tuyệt đối khi \(|x-a|<R\); phân kỳ khi \(|x-a|>R\); biên cần xét riêng.
- Trong \(|x-a|<R\): được phép đạo hàm/tích phân từng hạng:
  \[
  \left(\sum c_n(x-a)^n\right)'=\sum n c_n(x-a)^{n-1},\quad
  \int \sum c_n(x-a)^n dx=\sum \frac{c_n}{n+1}(x-a)^{n+1}+C.
  \]

### 3) Chuỗi chuẩn để “nhận dạng nhanh”
- \(\displaystyle \frac{1}{1-x}=\sum_{n=0}^\infty x^n\) (|x|<1).
- \(\displaystyle \ln(1+x)=\sum_{n=1}^\infty (-1)^{n-1}\frac{x^n}{n}\) (|x|<1; tại \(x=1\) hội tụ có điều kiện).
- \(\displaystyle e^x=\sum_{n=0}^\infty \frac{x^n}{n!}\) (mọi \(x\)).
- \(\displaystyle \sin x=\sum_{n=0}^\infty (-1)^n\frac{x^{2n+1}}{(2n+1)!}\), \(\cos x=\sum_{n=0}^\infty (-1)^n\frac{x^{2n}}{(2n)!}\).
- \(\displaystyle \arctan x=\sum_{n=0}^\infty (-1)^n\frac{x^{2n+1}}{2n+1}\) (|x|≤1, xét biên).

---

## CHAPTER 14 — Differential Equations

### 1) Tách biến
- \(y'=g(x)h(y)\Rightarrow \displaystyle \int \frac{dy}{h(y)}=\int g(x)\,dx + C\).

### 2) Tuyến tính cấp 1 (Integrating Factor)
- \(y'+p(x)y=q(x)\).
- Nhân tử tích phân: \(\mu(x)=e^{\int p(x)\,dx}\).
- Nghiệm tổng quát:
  \[
  y(x)=\frac{1}{\mu(x)}\left(\int \mu(x)q(x)\,dx + C\right).
  \]

### 3) Bernoulli
- \(y'+p(x)y=q(x)y^n\) (\(n\ne 0,1\)).
- Đặt \(v=y^{1-n}\Rightarrow v'+(1-n)p(x)v=(1-n)q(x)\) ⇒ tuyến tính theo \(v\).

### 4) Cấp 2 tuyến tính hệ số hằng
- \(y''+ay'+by=0\). Đặc trưng \(r^2+ar+b=0\):
  - 2 nghiệm phân biệt \(r_1\ne r_2\): \(y=C_1e^{r_1x}+C_2e^{r_2x}\).
  - nghiệm kép \(r\): \(y=(C_1+C_2x)e^{rx}\).
  - nghiệm phức \(r=\alpha\pm i\beta\): \(y=e^{\alpha x}(C_1\cos\beta x + C_2\sin\beta x)\).

### 5) Không thuần nhất: Undetermined Coefficients (mẫu nghiệm)
- Với \(y''+ay'+by=f(x)\) và \(f(x)\) là đa thức / \(e^{kx}\) / \(\sin\omega x,\cos\omega x\) / tích các dạng đó:
  - đoán \(y_p\) cùng “họ” với \(f(x)\);
  - nếu trùng với nghiệm riêng của thuần nhất, nhân thêm \(x^m\) (m là bội trùng).

### 6) Variation of Parameters (công thức khung)
- Với \(y''+P(x)y'+Q(x)y=G(x)\), biết \(y_1,y_2\) độc lập nghiệm thuần nhất.
- Đặt \(y_p=u_1y_1+u_2y_2\), giải hệ:
  \[
  \begin{cases}
  u_1'y_1+u_2'y_2=0\\
  u_1'y_1'+u_2'y_2'=G(x)
  \end{cases}
  \Rightarrow
  u_1'=-\frac{y_2G}{W},\quad u_2'=\frac{y_1G}{W},
  \]
  với \(W=y_1y_2'-y_1'y_2\) (Wronskian).

### 7) Power Series Method (ý chính để làm MCQ)
- Giả sử \(y=\sum_{n=0}^\infty a_n(x-a)^n\), suy ra
  \[
  y'=\sum_{n=1}^\infty n a_n(x-a)^{n-1},\quad
  y''=\sum_{n=2}^\infty n(n-1)a_n(x-a)^{n-2}.
  \]
- Thế vào ODE ⇒ đồng nhất hệ số theo \((x-a)^n\) ⇒ truy hồi \(a_{n+k}\) theo \(a_n\).
- Điều kiện đầu (IVP) cho \(y(a),y'(a)\) ⇒ chốt \(a_0,a_1\).

---

## (Appendix – chọn lọc hay gặp)
- Liên tục trên \([a,b]\) ⇒ khả tích Riemann trên \([a,b]\).
- Hàm đơn điệu trên \([a,b]\) ⇒ khả tích Riemann.
- Tiêu chuẩn Riemann (ý tưởng): khả tích ⇔ có thể làm \(\overline{S}-\underline{S}\) nhỏ tùy ý (hiệu tổng Darboux).
