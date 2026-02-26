import streamlit as st

# --- إعدادات الصفحة ---
st.set_page_config(page_title="بنك أسئلة الدفعة", page_icon="📚")

# --- القائمة الجانبية (Sidebar) لتنظيم المواد ---
st.sidebar.title("📚 اختر المادة")
subject = st.sidebar.selectbox(
    "المواد المتاحة:",
    ["اختر مادة...", "Machine Learning (AIE121)", "Solid State Physics"]
)

# --- عرض المحتوى بناءً على المادة ---
if subject == "Machine Learning (AIE121)":
    st.title("🤖 أسئلة Machine Learning")
    
    # اختيار المحاضرة
    lecture = st.sidebar.selectbox(
        "اختر المحاضرة:",
        ["اختر...", "Lecture 1: Intro", "Lecture 2: KNN Algorithm"]
    )
    
    if lecture == "Lecture 2: KNN Algorithm":
        st.subheader("📝 أسئلة المحاضرة الثانية (KNN)")
        
        # السؤال الأول
        q1 = st.radio(
            "1. What happens when K is very small in KNN?",
            ["Algorithm becomes robust to noise", "Algorithm is very sensitive to noise", "Bias increases significantly"],
            index=None # عشان ميكونش في إجابة متختارة جاهزة
        )
        
        # السؤال الثاني
        q2 = st.radio(
            "2. Which distance metric is commonly used in KNN?",
            ["Euclidean Distance", "Jaccard Index", "Cosine Similarity"],
            index=None
        )
        
        # زرار إرسال الإجابات والتصحيح
        if st.button("تأكيد الإجابات"):
            score = 0
            
            # تصحيح السؤال الأول
            if q1 == "Algorithm is very sensitive to noise":
                st.success("السؤال الأول: صح! ✅")
                score += 1
            else:
                st.error("السؤال الأول: غلط ❌ (الإجابة الصحيحة: Algorithm is very sensitive to noise)")
                
            # تصحيح السؤال الثاني
            if q2 == "Euclidean Distance":
                st.success("السؤال الثاني: صح! ✅")
                score += 1
            else:
                st.error("السؤال الثاني: غلط ❌ (الإجابة الصحيحة: Euclidean Distance)")
                
            st.info(f"النتيجة النهائية: {score} من 2")

elif subject == "Solid State Physics":
    st.title("⚛️ أسئلة Solid State Physics")
    st.info("جاري إضافة أسئلة هذه المادة قريباً...")
    
else:
    st.write("👈 أهلاً بك! يرجى اختيار المادة من القائمة الجانبية للبدء.")
