# ==========================================
# ملف: data.py
# ==========================================

# 1. استدعاء الملفات
import ml_lec1
import ml_lec2
import arc_lec1  # 👈 استدعاء أسئلة الأركتكتشر

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
            {"num": "02", "title": "Lecture 2", "count": "قريباً", "key": "arc_lec2", "available": False}, # مقفولة
            {"num": "03", "title": "Lecture 3", "count": "قريباً", "key": "arc_lec3", "available": False}, # مقفولة
        ]
    }
]

# 3. ربط المفاتيح بملفات الأسئلة
QUESTIONS_DB = {
    # 🤖 أسئلة الماشين ليرننج
    "ml_lec1": ml_lec1.QUESTIONS,
    "ml_lec2": ml_lec2.QUESTIONS,
    
    # 💻 أسئلة الأركتكتشر
    "arc_lec1": arc_lec1.QUESTIONS, 
}
