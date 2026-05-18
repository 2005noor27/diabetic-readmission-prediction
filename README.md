# 🏥 Diabetic Readmission Prediction — Streamlit App

تطبيق ويب تفاعلي يعرض مشروع Pattern Recognition لتوقع إعادة دخول المستشفى لمرضى السكري.

---

## 📁 هيكل المشروع

```
streamlit_app/
│
├── Home.py                          ← الصفحة الرئيسية
├── requirements.txt                 ← المكتبات المطلوبة
├── diabetic_data.csv                ← الداتاست (ضعيه هنا!)
│
├── .streamlit/
│   └── config.toml                  ← إعدادات الثيم والألوان
│
└── pages/
    ├── 1_📊_Data_Exploration.py
    ├── 2_🔧_Preprocessing.py
    ├── 3_🎯_Feature_Selection.py
    ├── 4_🤖_Models_Results.py
    ├── 5_🔮_Live_Prediction.py
    └── 6_📝_Conclusion.py
```

---

## 🚀 خطوات التشغيل (Windows + VS Code)

### 1. افتحي مجلد المشروع في VS Code

افتحي مجلد `streamlit_app` كاملاً في VS Code.

### 2. ضعي ملف الداتاست داخل المجلد

انسخي `diabetic_data.csv` إلى نفس مجلد المشروع.

### 3. افتحي terminal جديد في VS Code

من القائمة: `Terminal → New Terminal`

### 4. أنشئي بيئة افتراضية (اختياري لكن مُستحسن)

```bash
python -m venv venv
venv\Scripts\activate
```

### 5. ثبّتي المكتبات

```bash
pip install -r requirements.txt
```

### 6. شغّلي التطبيق

```bash
streamlit run Home.py
```

سيفتح التطبيق تلقائياً في المتصفح على `http://localhost:8501`

---

## 🎨 الألوان المستخدمة

| اللون | الكود |
|------|-------|
| Teal Dark | `#2A6F6F` |
| Teal Medium | `#4A9B9B` |
| Teal Light | `#8AC4C4` |
| Coral | `#D97757` |
| Gray | `#A8A8A8` |
| Background | `#F5F5F0` |

---

## 📊 الصفحات

1. **Home** — نظرة عامة، metrics، workflow
2. **Data Exploration** — استكشاف الداتا، توزيعات، missing values
3. **Preprocessing** — خطوات معالجة الداتا
4. **Feature Selection** — Random Forest importance، heatmap، PCA
5. **Models & Results** — مقارنة الأربع موديلات + confusion matrices
6. **Live Prediction** — تنبؤ تفاعلي لمريض جديد
7. **Conclusion** — النتائج النهائية، limitations، future work

---

## ⚙️ تخصيصات لازم تعمليها قبل التسليم

### في صفحة `4_🤖_Models_Results.py`:
- حدّثي قيم `results` بالأرقام الحقيقية اللي طلعت معك من Colab
- حدّثي مصفوفات `cms` بالـ confusion matrices الحقيقية

### في صفحة `Home.py`:
- استبدلي أسماء `Team Members` بأسماء الفريق الحقيقية

### في صفحة `5_🔮_Live_Prediction.py`:
- اختياري: استبدلي الـ rule-based logic بموديل حقيقي محفوظ بـ pickle

---

## 🌐 نشر التطبيق (اختياري)

ارفعي المشروع على GitHub، بعدين سجّلي في [streamlit.io/cloud](https://streamlit.io/cloud) وانشري التطبيق بنقرة واحدة.

---

**Pattern Recognition Project · DA360 · Yarmouk University**
