# Notes Đại số tuyến tính

## 1) Hệ tuyến tính, khử Gauss, nghiệm \(Ax=b\)
**(1.1) Điều kiện khả nghiệm**
- \(Ax=b\) có nghiệm ⇔ \(b\in C(A)\) ⇔ \(\mathrm{rank}(A)=\mathrm{rank}([A\ b])\).
- Nếu \(Ax=b\) khả nghiệm, tập nghiệm: \(x=x_p+x_n\) với \(x_n\in N(A)\). (Nghiệm tổng quát = 1 nghiệm riêng + không gian nghiệm thuần nhất)

**(1.2) Duy nhất / vô số**
- Duy nhất ⇔ khả nghiệm và \(N(A)=\{0\}\) ⇔ \(\mathrm{rank}(A)=n\) (cột độc lập tuyến tính).
- Vô số ⇔ khả nghiệm và \(\dim N(A)=n-r>0\).

**(1.3) Pivot & “free variables”**
- Số pivot = \(r\). Số biến tự do = \(n-r\).
- RREF cho trực tiếp: pivot columns ↔ cột độc lập trong \(A\) (và cũng là cột tạo cơ sở cho \(C(A)\)).

**(1.4) Định lý hạng–không gian (Rank–Nullity)**
- \(\dim N(A)+\mathrm{rank}(A)=n\).

---

## 2) Đại số ma trận, nghịch đảo, transpose, permutation
**(2.1) Quy tắc đảo & transpose (rất hay dùng)**
- \((AB)^T=B^TA^T\), \((A^T)^T=A\).
- Nếu \(A,B\) khả nghịch: \((AB)^{-1}=B^{-1}A^{-1}\), \((A^T)^{-1}=(A^{-1})^T\).
- \((A^{-1})^{-1}=A\). Nếu \(A\) khả nghịch ⇒ nghiệm \(Ax=b\) là \(x=A^{-1}b\).

**(2.2) Ma trận trực giao**
- \(Q^TQ=I\) ⇔ các cột của \(Q\) trực chuẩn.
- Khi đó \(Q^{-1}=Q^T\), và \(\|Qx\|_2=\|x\|_2\).

**(2.3) Permutation & hoán vị hàng**
- Ma trận hoán vị \(P\) là trực giao: \(P^TP=I\), \(P^{-1}=P^T\).
- Hoán vị hàng trong Gauss: \(PA\) (thay vì thao tác thủ công).

---

## 3) Phân tích LU / LDU / PA=LU (giải nhanh nhiều vế phải)
**(3.1) LU cơ bản**
- Nếu \(A=LU\) với \(L\) tam giác dưới (đường chéo 1), \(U\) tam giác trên:
  - Giải \(Ax=b\): giải \(Ly=b\) (thế tiến) rồi \(Ux=y\) (thế lùi).
- Điều kiện “đẹp” để LU không pivot: các định thức con đầu (leading principal minors) khác 0 (thực hành: không gặp pivot 0).

**(3.2) Pivoting**
- Thường dùng: \(PA=LU\) (P hoán vị hàng), ổn định số tốt hơn.

**(3.3) LDU**
- \(A=LDU\) với \(D\) chéo, \(U\) tam giác trên có đường chéo 1.
- Hay dùng để tách hệ số pivot vào \(D\).

---

## 4) Không gian vector, cơ sở, chiều, 4 không gian con cơ bản
**(4.1) Subspace test**
- \(W\subseteq\mathbb R^n\) là không gian con ⇔ đóng với cộng & nhân vô hướng & chứa \(0\).

**(4.2) Span, độc lập, cơ sở**
- Tập \(\{v_i\}\) độc lập ⇔ nghiệm duy nhất của \(\sum c_iv_i=0\) là mọi \(c_i=0\).
- Cơ sở = vừa sinh (span) vừa độc lập. Mọi cơ sở của cùng không gian có cùng số phần tử = dimension.

**(4.3) Bốn không gian con của \(A\)**
- Trong \(\mathbb R^n\): \(C(A^T)\) (row space) và \(N(A)\).
- Trong \(\mathbb R^m\): \(C(A)\) và \(N(A^T)\).
- Trực giao “không hiển nhiên” nhưng cực hay:
  - \(N(A)\perp C(A^T)\).
  - \(N(A^T)\perp C(A)\).
- Hệ quả kích thước:
  - \(\dim C(A)=\dim C(A^T)=r\).
  - \(\dim N(A)=n-r\), \(\dim N(A^T)=m-r\).

**(4.4) Công thức dimension cho tổng/giao**
- \(\dim(U+V)=\dim U+\dim V-\dim(U\cap V)\).

---

## 5) Trực giao, chiếu, least squares, Gram–Schmidt, QR
**(5.1) Chiếu trực giao lên 1 vector**
- Với \(a\neq 0\): \(\mathrm{proj}_a(b)=\dfrac{a^Tb}{a^Ta}a\).
- Thành phần vuông góc: \(b-\mathrm{proj}_a(b)\) vuông góc với \(a\).

**(5.2) Chiếu lên không gian cột \(C(A)\) (least squares)**
- Bài toán: \(\min_x\|Ax-b\|_2\).
- Điều kiện tối ưu (phương trình chuẩn):
  - \(A^T(Ax-b)=0 \iff A^TAx=A^Tb\).
- Vector xấp xỉ tốt nhất: \(p=Ax^\*\in C(A)\) là hình chiếu của \(b\) lên \(C(A)\).
- Khi \(A\) full column rank: nghiệm least squares duy nhất:
  - \(x^\*=(A^TA)^{-1}A^Tb\).
- Ma trận chiếu (projection matrix) lên \(C(A)\):
  - \(P=A(A^TA)^{-1}A^T\) (khi full column rank),
  - tính chất: \(P^2=P\), \(P^T=P\), \(Pb=p\).

**(5.3) Gram–Schmidt**
- Từ độc lập \(\{a_1,\dots,a_n\}\), tạo trực chuẩn \(\{q_i\}\):
  - \(u_k=a_k-\sum_{j<k}(q_j^Ta_k)q_j\), \(q_k=u_k/\|u_k\|\).
- Nhận diện: hệ số chiếu chính là phần tử của \(R\) trong QR.

**(5.4) QR**
- Nếu cột của \(A\) độc lập: \(A=QR\), với \(Q\) có cột trực chuẩn, \(R\) tam giác trên, diag \(R>0\) (chuẩn hoá).
- Least squares nhanh:
  - \(\min\|Ax-b\|=\min\|QRx-b\|=\min\|Rx-Q^Tb\|\).
  - Giải \(Rx=Q^Tb\) (tam giác trên).

**(5.5) Nhận diện trực giao & chuẩn**
- \(\|x\|_2^2=x^Tx\).
- Bất đẳng thức Cauchy–Schwarz: \(|u^Tv|\le \|u\|\|v\|\).
- Pythagoras: nếu \(u\perp v\) thì \(\|u+v\|^2=\|u\|^2+\|v\|^2\).

---

## 6) Định thức (determinant) — tính chất & ứng dụng
**(6.1) Tính chất thao tác hàng (nhớ kỹ để tính nhanh)**
- Đổi chỗ 2 hàng: \(\det\) đổi dấu.
- Nhân 1 hàng với \(c\): \(\det\) nhân \(c\).
- Cộng bội hàng khác vào 1 hàng: \(\det\) không đổi.

**(6.2) Tam giác & tích**
- Nếu \(A\) tam giác (trên/dưới): \(\det(A)=\prod_i a_{ii}\).
- \(\det(AB)=\det(A)\det(B)\).
- Nếu \(A\) khả nghịch: \(\det(A)\neq 0\) và \(\det(A^{-1})=1/\det(A)\).

**(6.3) Cofactor / Laplace (dùng khi thưa)**
- Khai triển theo hàng i:
  - \(\det(A)=\sum_j a_{ij}C_{ij}\), \(C_{ij}=(-1)^{i+j}\det(M_{ij})\).

**(6.4) Ứng dụng**
- \(A\) khả nghịch ⇔ \(\det(A)\neq 0\).
- Diễn giải hình học: \(|\det(A)|\) là hệ số co giãn thể tích; dấu cho biết đổi hướng.

---

## 7) Trị riêng, vector riêng, chéo hoá, Markov
**(7.1) Đa thức đặc trưng**
- \(\lambda\) là trị riêng ⇔ \(\det(A-\lambda I)=0\).
- Vector riêng \(x\neq 0\): \((A-\lambda I)x=0\) ⇒ \(x\in N(A-\lambda I)\).

**(7.2) Chéo hoá**
- \(A\) chéo hoá được ⇔ có \(n\) vector riêng độc lập ⇔ tồn tại \(A=S\Lambda S^{-1}\).
- Khi đó: \(A^k=S\Lambda^kS^{-1}\) (rất hay cho Markov, truy hồi).
- Nếu \(A\) có \(n\) trị riêng phân biệt ⇒ chắc chắn chéo hoá được.

**(7.3) Trace & determinant qua trị riêng**
- \(\mathrm{tr}(A)=\sum_i \lambda_i\) (tính theo bội đại số),
- \(\det(A)=\prod_i \lambda_i\).

**(7.4) Markov matrices (chuỗi Markov)**
- Ma trận Markov (chuẩn theo cột): các phần tử \(\ge 0\), tổng mỗi cột = 1.
- Luôn có trị riêng \(\lambda=1\).
- Trạng thái ổn định \(x_\*\): \(Ax_\*=x_\*\), với \(x_\*\ge 0\), tổng thành phần = 1.
- Nếu các trị riêng còn lại có \(|\lambda|<1\) ⇒ \(A^k x_0\to x_\*\) (hội tụ về ổn định).

---

## 8) Ma trận đối xứng, xác định dương, chéo hoá trực giao
**(8.1) Đối xứng**
- \(A=A^T\) ⇒ mọi trị riêng là thực.
- Các eigenvectors ứng với trị riêng khác nhau là trực giao.

**(8.2) Spectral theorem (cực quan trọng)**
- Nếu \(A\) đối xứng: tồn tại \(Q\) trực giao sao cho
  - \(A=Q\Lambda Q^T\) (chéo hoá trực giao).

**(8.3) Positive definite (PD)**
- \(A\) đối xứng là PD ⇔ \(x^TAx>0\ \forall x\neq 0\).
- Tương đương:
  - mọi trị riêng \(>0\),
  - mọi định thức con đầu (leading principal minors) \(>0\),
  - tồn tại Cholesky: \(A=R^TR\) (R tam giác trên) hoặc \(A=LL^T\) (L tam giác dưới).

---

## 9) Similarity, biến đổi cơ sở, biến đổi tuyến tính
**(9.1) Similar matrices**
- \(B=S^{-1}AS\) ⇒ \(A\) và \(B\) similar.
- Bất biến theo similarity:
  - trị riêng, đa thức đặc trưng, \(\det\), \(\mathrm{tr}\), rank.
- Ý nghĩa: cùng phép biến đổi tuyến tính nhưng trong cơ sở khác.

**(9.2) Ma trận của ánh xạ tuyến tính**
- Với \(T:\mathbb R^n\to\mathbb R^m\), ma trận \(A\) thoả \(T(x)=Ax\) (trong cơ sở chuẩn).
- Đổi cơ sở: nếu cột của \(S\) là cơ sở mới, thì ma trận trong cơ sở mới: \(A_{\text{new}}=S^{-1}AS\).

---

## 10) SVD (Singular Value Decomposition) & hệ quả (cực hay cho MCQ)
**(10.1) SVD**
- Với mọi \(A\in\mathbb R^{m\times n}\):
  - \(A=U\Sigma V^T\),
  - \(U\in\mathbb R^{m\times m}\), \(V\in\mathbb R^{n\times n}\) trực giao,
  - \(\Sigma\) chéo (không âm) với singular values \(\sigma_1\ge\dots\ge\sigma_r>0\).

**(10.2) Liên hệ với \(A^TA\) và \(AA^T\)**
- Trị riêng của \(A^TA\) là \(\sigma_i^2\); vector riêng tương ứng là cột của \(V\).
- Trị riêng của \(AA^T\) là \(\sigma_i^2\); vector riêng tương ứng là cột của \(U\).

**(10.3) Pseudoinverse & least squares tổng quát**
- \(A^+=V\Sigma^+U^T\).
- Nghiệm least squares chuẩn 2 “nhỏ nhất chuẩn”:
  - \(x^\*=A^+b\) (đúng cả khi không full rank).
- Hạng \(r\) = số singular values dương.

**(10.4) Best rank-k approximation (Eckart–Young)**
- Ma trận hạng-k tốt nhất theo chuẩn 2/Frobenius:
  - \(A_k=\sum_{i=1}^k \sigma_i u_iv_i^T\).
- Sai số chuẩn 2: \(\|A-A_k\|_2=\sigma_{k+1}\).

---

## 11) Fourier/FFT & ma trận phức (mức công thức)
- Cơ sở Fourier: các vector mũ phức trực giao (theo chuẩn hoá).
- Ma trận DFT \(F\) (chuẩn hoá) là “gần như” trực giao trong phức: \(F^*F=I\) (với \(*\) là liên hợp–chuyển vị).
- FFT là thuật toán tính DFT nhanh: giảm từ \(O(n^2)\) xuống \(O(n\log n)\).

---

## 12) Mạng/đồ thị & ma trận (graphs and networks)
- Ma trận incidence/adjacency dùng mô hình hoá mạng.
- Luồng trong mạng thường dẫn về hệ tuyến tính + ràng buộc (conservation laws) ⇒ rank/khả nghiệm quan trọng.
- (Điểm hay hỏi) Mạng liên thông ⇒ một số ma trận liên quan (ví dụ Laplacian) có trị riêng 0 bội 1 (tuỳ định nghĩa).

---

## 13) Linear programming (LP) — xương sống ý tưởng
- Dạng chuẩn: tối ưu tuyến tính với ràng buộc tuyến tính.
- Nghiệm tối ưu (nếu tồn tại hữu hạn) đạt tại một đỉnh (extreme point) của đa diện khả thi.
- Simplex di chuyển giữa các đỉnh; duality: có bài toán đối ngẫu, và (thường) tối ưu mạnh: primal=dual khi thoả điều kiện.

---

## 14) Numerical linear algebra (tóm tắt công thức hay hỏi)
- Độ điều kiện (condition number) theo chuẩn 2:
  - \(\kappa_2(A)=\|A\|_2\|A^{-1}\|_2=\sigma_1/\sigma_n\) (khi \(A\) vuông khả nghịch).
- Nhạy cảm nghiệm: \(\frac{\|\delta x\|}{\|x\|}\) thường bị chặn bởi \(\kappa(A)\frac{\|\delta b\|}{\|b\|}\) (cùng bậc).
- Pivoting trong LU cải thiện ổn định.
- Normal equations có thể làm xấu điều kiện: \(\kappa(A^TA)\approx \kappa(A)^2\).

---
# Checklist “hay ra MCQ”
- Rank–Nullity; số pivot & biến tự do.
- 4 không gian con & các trực giao: \(N(A)\perp C(A^T)\), \(N(A^T)\perp C(A)\).
- Least squares: \(A^TAx=A^Tb\), \(P=A(A^TA)^{-1}A^T\) (full col rank).
- QR giải least squares: \(Rx=Q^Tb\).
- Spectral theorem cho đối xứng: \(A=Q\Lambda Q^T\); PD ⇔ eigenvalues > 0 ⇔ Cholesky.
- Chéo hoá: \(A=S\Lambda S^{-1}\Rightarrow A^k=S\Lambda^kS^{-1}\).
- SVD: \(A=U\Sigma V^T\), \(A^+=V\Sigma^+U^T\), best rank-k và \(\|A-A_k\|_2=\sigma_{k+1}\).
