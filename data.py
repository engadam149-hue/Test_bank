# ==========================================
# ملف: data.py
# ==========================================

# 1. استدعاء الملفات
# 👈 ملفات مادة Machine Learning
import ml_lec1
import ml_lec2
import ml_lec3
import ml_lec4
import ml_lec5

# 👈 ملفات مادة Computer Architecture
import arc_lec1
import arc_lec2
import arc_lec3
import arc_lec4
import arc_ass   

# 👈 ملفات مادة Discrete Mathematics
import dm_lec1  
import dm_lec2  
import dm_lec3  
import dm_lec4  # 👈 المحاضرة الرابعة (Sets)
import dm_lec5  # 👈 المحاضرة الخامسة (Functions)

# 👈 ملفات مادة Digital Signal Processing
import dsp_lec1 
import dsp_lec2
import dsp_lec3
import dsp_lec4
import dsp_lec5_6

# 2. إعدادات المواد (بترتيبها الأصلي المظبوط)
SUBJECTS = [
    {
        "icon": "🤖", 
        "name": "Machine Learning", 
        "code": "AIE121",
        "desc": "Intro, KNN, Decision Trees, Regression, Clustering...", 
        "key": "ml",
        "lectures": [
            {"num": "01", "title": "Intro to ML", "count": "50 سؤال", "key": "ml_lec1", "available": True},
            {"num": "02", "title": "KNN Algorithm", "count": "50 سؤال", "key": "ml_lec2", "available": True},
            {"num": "03", "title": "Linear Regression & GD", "count": "25 سؤال", "key": "ml_lec3", "available": True},
            {"num": "04", "title": "Logistic Regression", "count": "22 سؤال", "key": "ml_lec4", "available": True},
            {"num": "05", "title": "K-Means Clustering", "count": "21 سؤال", "key": "ml_lec5", "available": True},
        ]
    },
    {
        "icon": "💻", 
        "name": "Computer Architecture", 
        "code": "CSE132",
        "desc": "CPU, Memory, Buses, Cycle...", 
        "key": "arc",
        "lectures": [
            {"num": "🏆", "title": "Assignments & Quizzes", "count": "65 سؤال", "key": "arc_ass", "available": True, "special": True}, 
            {"num": "01", "title": "Lec 1: Intro & Structure", "count": "31 سؤال", "key": "arc_lec1", "available": True},
            {"num": "02", "title": "Lec 2: CPU & Buses", "count": "50 سؤال", "key": "arc_lec2", "available": True},
            {"num": "03", "title": "Lec 3: Instruction Cycle", "count": "42 سؤال", "key": "arc_lec3", "available": True}, 
            {"num": "04", "title": "Lec 4: Bus Construction", "count": "50 سؤال", "key": "arc_lec4", "available": True},
        ]
    },
    {
        "icon": "🧮", 
        "name": "Discrete Mathematics", 
        "code": "CSE315",
        "desc": "Logic, Proofs, Sets, Functions...", 
        "key": "dm",
        "lectures": [
            {"num": "01", "title": "Lec 1: Logic & Proofs", "count": "36 سؤال", "key": "dm_lec1", "available": True},
            {"num": "02", "title": "Lec 2: Bit Strings & Eq", "count": "51 سؤال", "key": "dm_lec2", "available": True},
            {"num": "03", "title": "Lec 3: Quantifiers & Proofs", "count": "50 سؤال", "key": "dm_lec3", "available": True}, 
            {"num": "04", "title": "Lec 4: Sets & Operations", "count": "21 سؤال", "key": "dm_lec4", "available": True},
            {"num": "05", "title": "Lec 5: Functions", "count": "21 سؤال", "key": "dm_lec5", "available": True},
        ]
    },
    {
        "icon": "📡", 
        "name": "Digital Signal Processing", 
        "code": "DSP201",  
        "desc": "Signals, Sampling, Z-Transform, Filters...", 
        "key": "dsp",
        "lectures": [
            {"num": "01", "title": "Lec 1: Intro & Sampling", "count": "40 سؤال", "key": "dsp_lec1", "available": True},
            {"num": "02", "title": "Lec 2: Periodicity & Operations", "count": "51 سؤال", "key": "dsp_lec2", "available": True},
            {"num": "03", "title": "Lec 3: Signals & Energy", "count": "46 سؤال", "key": "dsp_lec3", "available": True},
            {"num": "04", "title": "Lec 4: LTI Systems", "count": "36 سؤال", "key": "dsp_lec4", "available": True},
            {"num": "5-6", "title": "Lec 5-6: Convolution & LTI", "count": "35 سؤال", "key": "dsp_lec5_6", "available": True},
        ]
    }
]

# 3. ربط المفاتيح بملفات الأسئلة
QUESTIONS_DB = {
    # Machine Learning
    "ml_lec1": ml_lec1.QUESTIONS,
    "ml_lec2": ml_lec2.QUESTIONS,
    "ml_lec3": ml_lec3.QUESTIONS,
    "ml_lec4": ml_lec4.QUESTIONS,
    "ml_lec5": ml_lec5.QUESTIONS,
    
    # Computer Architecture
    "arc_ass": arc_ass.QUESTIONS, 
    "arc_lec1": arc_lec1.QUESTIONS, 
    "arc_lec2": arc_lec2.QUESTIONS,
    "arc_lec3": arc_lec3.QUESTIONS, 
    "arc_lec4": arc_lec4.QUESTIONS, 
    
    # Discrete Mathematics
    "dm_lec1": dm_lec1.QUESTIONS,
    "dm_lec2": dm_lec2.QUESTIONS, 
    "dm_lec3": dm_lec3.QUESTIONS,
    "dm_lec4": dm_lec4.QUESTIONS,
    "dm_lec5": dm_lec5.QUESTIONS,
    
    # Digital Signal Processing
    "dsp_lec1": dsp_lec1.QUESTIONS,
    "dsp_lec2": dsp_lec2.QUESTIONS,
    "dsp_lec3": dsp_lec3.QUESTIONS,
    "dsp_lec4": dsp_lec4.QUESTIONS,
    "dsp_lec5_6": dsp_lec5_6.QUESTIONS,
}