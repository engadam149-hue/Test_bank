# ==========================================
# ملف: data.py
# ==========================================

# 1. استدعاء الملفات
import ml_lec1
import ml_lec2

import arc_lec1
import arc_lec2
import arc_lec3
import arc_lec4
import arc_ass   

import dm_lec1  
import dm_lec2  
import dm_lec3  

# 👈 استدعاء ملفات مادة الـ DSP
import dsp_lec1 
import dsp_lec2
import dsp_lec3
import dsp_lec4  # 👈 المحاضرة الرابعة الجديدة

# 2. إعدادات المواد (بترتيبها الأصلي المظبوط)
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
            # 👈 المحاضرة الرابعة اتضافت هنا بـ 36 سؤال!
            {"num": "04", "title": "Lec 4: LTI Systems", "count": "36 سؤال", "key": "dsp_lec4", "available": True},
        ]
    }
]

# 3. ربط المفاتيح بملفات الأسئلة
QUESTIONS_DB = {
    "ml_lec1": ml_lec1.QUESTIONS,
    "ml_lec2": ml_lec2.QUESTIONS,
    
    "arc_ass": arc_ass.QUESTIONS, 
    "arc_lec1": arc_lec1.QUESTIONS, 
    "arc_lec2": arc_lec2.QUESTIONS,
    "arc_lec3": arc_lec3.QUESTIONS, 
    "arc_lec4": arc_lec4.QUESTIONS, 
    
    "dm_lec1": dm_lec1.QUESTIONS,
    "dm_lec2": dm_lec2.QUESTIONS, 
    "dm_lec3": dm_lec3.QUESTIONS,
    
    # 👈 ربطنا أسئلة الـ DSP كلها بالملفات بتاعتها
    "dsp_lec1": dsp_lec1.QUESTIONS,
    "dsp_lec2": dsp_lec2.QUESTIONS,
    "dsp_lec3": dsp_lec3.QUESTIONS,
    "dsp_lec4": dsp_lec4.QUESTIONS, # 👈 المحاضرة الرابعة
}