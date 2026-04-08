import numpy as np
from scipy.special import lambertw # دالة ال
# قيمة تقريبية لتيار الإ
e = 1.6e-19
k = 1.38e-23
h = 6.63e-34
y0 = 0.2
Eg = 0.62 * 1.6e-19
n = 1.2
T = 300
VT = (k * T) / e
Rs = 100# المقاومة التسلسلية
Is = (8 * e * k * T * y0 / h) * np.exp(-Eg / (k * T)) * 10**9
# الآن يمكنك تحديد مجال الجهد V كما تريد
V_input = np.linspace(0.1, 2, 1000) 

# تحويل المعادلة لتعطي I بدلالة V باستخدام Lambert W
# المعادلة: I = (n*VT/Rs) * W( (Is*Rs / n*VT) * exp((V + Is*Rs)/(n*VT)) ) - Is
exponent_term = (Is * Rs / (n * VT)) * np.exp((V_input + Is * Rs) / (n * VT))
I_output = (n * VT / Rs) * lambertw(exponent_term).real - Is

# الآن احسب المشتقات كالمعتاد
dIdV = np.gradient(I_output, V_input)
d2IdV2 = np.gradient(dIdV, V_input)

Vth = V_input[np.argmax(d2IdV2)]
print(f"Vth المستنتج: {Vth:.4f} فولت")