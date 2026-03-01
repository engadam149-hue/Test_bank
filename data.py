# ==========================================
# ملف: data.py
# ==========================================

# 1. استدعاء الملفات
import ml_lec1
import ml_lec2
import arc_lec1
import arc_lec2
import arc_lec3  # 👈 ضفنا المحاضرة التالتة هنا

# 2. إعدادات المواد
SUBJECTS = [
    {
        "icon": "🤖", 
        "name": "Machine Learning", 
        "code": "AIE121",
        "desc": "Intro, KNN, Decision Trees...", 
        "key": "ml",
        "lectures": [
            {"num": "01", "title": "Intro to ML", "count": "50 سؤال", "key": "ml_lec1", "available": True},
            {"num": "02", "title": "KNN Algorithm", "count": "50 سؤال", "key": "ml_lec2", "available": True},
        ]
    },
    {
        "icon": "💻", 
        "name": "Computer Architecture", 
        "code": "CSE132",
        "desc": "CPU, Memory, Buses, Cycle...", 
        "key": "arc",
        "lectures": [
            {"num": "01", "title": "Lec 1: Intro & Structure", "count": "43 سؤال", "key": "arc_lec1", "available": True},
            {"num": "02", "title": "Lec 2: CPU & Buses", "count": "50 سؤال", "key": "arc_lec2", "available": True},
            {"num": "03", "title": "Lec 3: Instruction Cycle", "count": "42 سؤال", "key": "arc_lec3", "available": True}, # 👈 فتحنا الزرار بتاعها أهو
        ]
    }
]

# 3. ربط المفاتيح بملفات الأسئلة
QUESTIONS_DB = {
    # 🤖 الماشين ليرننج
    "ml_lec1": ml_lec1.QUESTIONS,
    "ml_lec2": ml_lec2.QUESTIONS,
    
    # 💻 الأركتكتشر
    "arc_lec1": arc_lec1.QUESTIONS, 
    "arc_lec2": arc_lec2.QUESTIONS,
    "arc_lec3": arc_lec3.QUESTIONS, # 👈 ربطناها بالأسئلة بتاعتها هنا
}