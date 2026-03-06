# ==========================================
# 📖 arc_ass.py
# Computer Architecture - Assignments & Quizzes
# ==========================================

QUESTIONS = [

    # ══════════════════════════════════════════════
    # 📝 Assignment 1 Questions
    # ══════════════════════════════════════════════

    {
        "q": "______ is those attributes visible to the programmer.",
        "type": "mcq",
        "options": ["Organization", "Structure", "Architecture", "Function"],
        "ans": "Architecture"
    },
    {
        "q": "______ is how features are implemented.",
        "type": "mcq",
        "options": ["Organization", "Structure", "Architecture", "Function"],
        "ans": "Organization"
    },
    {
        "q": "Control signals, interfaces, memory technology refers to:",
        "type": "mcq",
        "options": ["Organization", "Structure", "Architecture", "Function"],
        "ans": "Organization"
    },
    {
        "q": "Instruction set, number of bits used for data representation refers to:",
        "type": "mcq",
        "options": ["Organization", "Structure", "Architecture", "Function"],
        "ans": "Architecture"
    },
    {
        "q": "The IBM System/370 family share the same basic architecture.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True"
    },
    {
        "q": "Computer Organization differs between different versions of the same family.",
        "type": "tf",
        "options": ["True", "False"],
        "ans": "True"
    },
    {
        "q": "______ is the way in which components relate to each other.",
        "type": "mcq",
        "options": ["Organization", "Structure", "Architecture", "Function"],
        "ans": "Structure"
    },
    {
        "q": "______ is the operation of individual components as part of the structure.",
        "type": "mcq",
        "options": ["Organization", "Structure", "Architecture", "Function"],
        "ans": "Function"
    },
    {
        "q": "Computer functions may be data:",
        "type": "mcq",
        "options": ["Processing", "Movement", "Storage", "All are correct"],
        "ans": "All are correct"
    },
    {
        "q": "Addition is considered as data:",
        "type": "mcq",
        "options": ["Processing", "Movement", "Storage", "Control"],
        "ans": "Processing"
    },
    {
        "q": "The Loading of data is considered as data:",
        "type": "mcq",
        "options": ["Processing", "Movement", "Storage", "Control"],
        "ans": "Movement"
    },
    {
        "q": "Storing data in memory is considered as data:",
        "type": "mcq",
        "options": ["Processing", "Movement", "Storage", "Control"],
        "ans": "Storage"
    },
    {
        "q": "______ controls the operation of the computer and performs its data processing function.",
        "type": "mcq",
        "options": ["Main memory", "System interconnection", "I/O", "CPU"],
        "ans": "CPU"
    },
    {
        "q": "______ stores data.",
        "type": "mcq",
        "options": ["Main memory", "System interconnection", "I/O", "CPU"],
        "ans": "Main memory"
    },
    {
        "q": "______ is some mechanism that provides for communication among CPU, main memory, and I/O.",
        "type": "mcq",
        "options": ["Main memory", "System interconnection", "I/O", "CPU"],
        "ans": "System interconnection"
    },
    {
        "q": "______ moves data between the computer and its external environment.",
        "type": "mcq",
        "options": ["Main memory", "System interconnection", "I/O", "CPU"],
        "ans": "I/O"
    },
    {
        "q": "______ Controls the operation of the CPU and hence the computer.",
        "type": "mcq",
        "options": ["CPU interconnection", "ALU", "Registers", "Control Unit"],
        "ans": "Control Unit"
    },
    {
        "q": "______ Performs the computer's data processing functions.",
        "type": "mcq",
        "options": ["CPU interconnection", "ALU", "Registers", "Control Unit"],
        "ans": "ALU"
    },
    {
        "q": "______ Provides storage internal to the CPU.",
        "type": "mcq",
        "options": ["CPU interconnection", "ALU", "Registers", "Control Unit"],
        "ans": "Registers"
    },
    {
        "q": "Sequencing logic, Control Unit Registers, Decoders, and Control Memory are the internal components of:",
        "type": "mcq",
        "options": ["ALU", "Control Unit", "Memory", "BUS"],
        "ans": "Control Unit"
    },
    {
        "q": "______ is used to transmit data and instruction everywhere.",
        "type": "mcq",
        "options": ["ALU", "Control Unit", "Memory", "BUS"],
        "ans": "BUS"
    },
    {
        "q": "Semiconductor memory capacity approximately doubles each:",
        "type": "mcq",
        "options": ["week", "month", "year", "2 years"],
        "ans": "2 years"
    },

    # ══════════════════════════════════════════════
    # 📝 Assignment 2 Questions
    # ══════════════════════════════════════════════

    {
        "q": "Transfer of instruction will be found on ______ bus.",
        "type": "mcq",
        "options": ["Data", "Address", "Control", "All are correct"],
        "ans": "Data"
    },
    {
        "q": "Memory read/write signal is found on ______ bus.",
        "type": "mcq",
        "options": ["Data", "Address", "Control", "All are correct"],
        "ans": "Control"
    },
    {
        "q": "CPU generates ______.",
        "type": "mcq",
        "options": ["Data", "Addresses", "Control Signals", "All are correct"],
        "ans": "All are correct"
    },
    {
        "q": "Bus width of ______ bus determines maximum memory capacity of system.",
        "type": "mcq",
        "options": ["Data", "Address", "Control", "All are correct"],
        "ans": "Address"
    },
    {
        "q": "The ______ bus width is a key determinant of CPU performance.",
        "type": "mcq",
        "options": ["Data", "Address", "Control", "All are correct"],
        "ans": "Data"
    },
    {
        "q": "Separate data & address lines are found in ______ buses.",
        "type": "mcq",
        "options": ["Dedicated", "Multiplexed", "Distributed", "Centralized"],
        "ans": "Dedicated"
    },
    {
        "q": "Address valid or data valid control lines are found in ______ buses.",
        "type": "mcq",
        "options": ["Dedicated", "Multiplexed", "Distributed", "Centralized"],
        "ans": "Multiplexed"
    },
    {
        "q": "If the address bus were 16 bit, so it can access ______ RAM.",
        "type": "mcq",
        "options": ["16 Bit", "64 KB", "32 GB", "64 GB"],
        "ans": "64 KB"
    },
    {
        "q": "If the data bus were 16 bit, so it can deal with ______ in parallel.",
        "type": "mcq",
        "options": ["16 Bit", "64 KB", "32 GB", "64 GB"],
        "ans": "16 Bit"
    },
    {
        "q": "A ______ is a sequence of steps.",
        "type": "mcq",
        "options": ["inflexible", "Program", "Main Memory", "Bus"],
        "ans": "Program"
    },
    {
        "q": "______ is a temporary storage of code and results.",
        "type": "mcq",
        "options": ["Program", "Main Memory", "Bus", "Registers"],
        "ans": "Main Memory"
    },
    {
        "q": "Executing instruction from memory location to processor is done during ______ cycle.",
        "type": "mcq",
        "options": ["PC", "decode", "fetch", "execute"],
        "ans": "execute"
    },
    {
        "q": "Reading instruction from memory location to processor is done during ______ cycle.",
        "type": "mcq",
        "options": ["PC", "decode", "fetch", "execute"],
        "ans": "fetch"
    },
    {
        "q": "______ contains the address of the next instruction.",
        "type": "mcq",
        "options": ["PC", "decode", "fetch", "execute"],
        "ans": "PC"
    },
    {
        "q": "______ analyzes instruction to determine type of the operation to be performed.",
        "type": "mcq",
        "options": ["PC", "decode cycle", "fetch cycle", "execute cycle"],
        "ans": "decode cycle"
    },
    {
        "q": "______ is a mechanism by which other modules may interrupt normal sequence of processing.",
        "type": "mcq",
        "options": ["Program", "Interrupt", "Main memory", "Bus"],
        "ans": "Interrupt"
    },
    {
        "q": "Overflow and division by zero are types of ______ interrupt.",
        "type": "mcq",
        "options": ["Timer", "I/O", "Hardware failure", "Program"],
        "ans": "Program"
    },
    {
        "q": "Used in pre-emptive multi-tasking is a type of ______ interrupt.",
        "type": "mcq",
        "options": ["Timer", "I/O", "Hardware failure", "Program"],
        "ans": "Timer"
    },
    {
        "q": "Memory parity error is a type of ______ interrupt.",
        "type": "mcq",
        "options": ["Timer", "I/O", "Hardware failure", "Program"],
        "ans": "Hardware failure"
    },
    {
        "q": "______ interrupt comes from the I/O controller.",
        "type": "mcq",
        "options": ["Timer", "I/O", "Hardware failure", "Program"],
        "ans": "I/O"
    },
    {
        "q": "Instruction loaded into Instruction Register (IR) is done during ______ cycle.",
        "type": "mcq",
        "options": ["execute", "fetch", "decode", "interrupt"],
        "ans": "fetch"
    },
    {
        "q": "Data transfer between CPU and I/O module is typically done during ______ cycle.",
        "type": "mcq",
        "options": ["execute", "fetch", "decode", "first"],
        "ans": "execute"
    },
    {
        "q": "In ______ interrupt, processor will ignore further interrupts whilst processing one.",
        "type": "mcq",
        "options": ["Disable", "Priority", "multi", "single"],
        "ans": "Disable"
    },
    {
        "q": "In ______ interrupt, Low priority interrupts can be interrupted by higher priority ones.",
        "type": "mcq",
        "options": ["Disable", "Priority", "multi", "single"],
        "ans": "Priority"
    },
    {
        "q": "Hardwired systems are generally ______.",
        "type": "mcq",
        "options": ["inflexible", "Program", "Main Memory", "Bus"],
        "ans": "inflexible"
    },
    {
        "q": "______ contains a word to be stored in memory or sent to the I/O unit, or is used to receive a word.",
        "type": "mcq",
        "options": ["PC", "MBR", "MAR", "IR"],
        "ans": "MBR"
    },
    {
        "q": "______ Specifies the address in memory of the word to be written from or read into the MBR.",
        "type": "mcq",
        "options": ["PC", "MBR", "MAR", "IR"],
        "ans": "MAR"
    },
    {
        "q": "______ Contain the instruction fetched from the memory.",
        "type": "mcq",
        "options": ["PC", "MBR", "MAR", "IR"],
        "ans": "IR"
    },

    # ══════════════════════════════════════════════
    # 📝 Assignment 2 - Problem Solving Questions (Memory Decode)
    # ══════════════════════════════════════════════

    {
        "q": "Based on the memory content: Address 2C00 holds '01010010110001010000'. What does this instruction do?",
        "type": "mcq",
        "options": [
            "Store AC to memory location 2C50",
            "Load AC from memory location 2C50",
            "Multiply AC with memory location 2C00",
            "Add AC to memory location 2C50"
        ],
        "ans": "Load AC from memory location 2C50"
    },
    {
        "q": "Based on the memory content: Address 2C02 holds '10110010110001010010'. What does this instruction do?",
        "type": "mcq",
        "options": [
            "Load AC from memory location 2C52",
            "Store AC to memory location 2C52",
            "Multiply AC with memory location 2C50",
            "Store AC to memory location 2C02"
        ],
        "ans": "Store AC to memory location 2C52"
    },
    {
        "q": "Given an instruction like '01010010110001010000', what is the total size of the instruction in bits?",
        "type": "mcq",
        "options": ["8 bits", "16 bits", "20 bits", "24 bits"],
        "ans": "20 bits"
    },
    {
        "q": "Given the instruction structure (4-bit opcode + 16-bit address), what is the size of the Address?",
        "type": "mcq",
        "options": ["4 bits", "16 bits", "20 bits", "32 bits"],
        "ans": "16 bits"
    },
    {
        "q": "Based on a 16-bit address field, how many words can the memory contain?",
        "type": "mcq",
        "options": ["16 words", "4096 words", "65,536 (64K) words", "1,048,576 (1M) words"],
        "ans": "65,536 (64K) words"
    },
    {
        "q": "If the opcode consists of 4 bits, how many different operations can the system support?",
        "type": "mcq",
        "options": ["4 operations", "8 operations", "16 operations", "32 operations"],
        "ans": "16 operations"
    },
    {
        "q": "What is the number of instructions per word if the word size equals the instruction size?",
        "type": "mcq",
        "options": ["1", "2", "4", "It depends on the opcode"],
        "ans": "1"
    }
]