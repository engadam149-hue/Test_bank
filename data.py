# ==========================================
# ملف: data.py
# ==========================================

# 1. استدعاء الأسئلة من الملفات اللي جنبك في نفس الفولدر
import ml_lec1
import ml_lec2

# 2. إعدادات المادة (اللي بتظهر كزراير في الموقع)
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
    }
]

# 3. ربط المفاتيح بالأسئلة عشان الموقع يقراها
QUESTIONS_DB = {
    "ml_lec1": ml_lec1.QUESTIONS,
    "ml_lec2": ml_lec2.QUESTIONS,
}
