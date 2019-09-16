import random

# Boolean values of each variables
varA = bool
varB = bool
varC = bool
varD = bool
varE = bool

# Counters
c = int
c_up = int  # Counter for the numerator part (if there is conditional dependency)
c_down = int  # Counter for the denominator part (if there is conditional dependency)

# Constants
TURNS = 100000


# Functions of variables
def var_a():
    global varA
    x = random.randint(1, 10)
    if x <= 2:
        varA = True
    else:
        varA = False


def var_b():
    global varA
    global varB
    x = random.randint(1, 10)
    if varA:
        if x <= 8:
            varB = True
        else:
            varB = False
    else:
        if x <= 2:
            varB = True
        else:
            varB = False


def var_c():
    global varA
    global varC
    x = random.randint(1, 100)
    if varA:
        if x <= 20:
            varC = True
        else:
            varC = False
    else:
        if x <= 5:
            varC = True
        else:
            varC = False


def var_d():
    global varB
    global varC
    global varD
    x = random.randint(1, 100)
    if varB:
        if varC:
            if x <= 80:
                varD = True
            else:
                varD = False
        else:
            if x <= 80:
                varD = True
            else:
                varD = False
    else:
        if varC:
            if x <= 80:
                varD = True
            else:
                varD = False
        else:
            if x <= 5:
                varD = True
            else:
                varD = False


def var_e():
    global varC
    global varE
    x = random.randint(1, 10)
    if varC:
        if x <= 8:
            varE = True
        else:
            varE = False
    else:
        if x <= 6:
            varE = True
        else:
            varE = False


# Function of each questions
def question_1():
    global varD
    global c
    c = 0   # Counter
    for i in range(TURNS):
        var_a()
        var_b()
        var_c()
        var_d()
        var_e()
        if varD:
            c = c + 1
    print("P(+d) = " + str(c/TURNS))


def question_2():
    global varA
    global varD
    global c
    c = 0  # Counter
    for i in range(TURNS):
        var_a()
        var_b()
        var_c()
        var_d()
        var_e()
        if not varA:
            if varD:
                c = c + 1
    print("P(+d,-a) = " + str(c/TURNS))


def question_3():
    global varB
    global varE
    global c_up
    global c_down
    c_up = c_down = 0  # Counters
    for i in range(TURNS):
        var_a()
        var_b()
        var_c()
        var_d()
        var_e()
        if not varB:
            c_down = c_down + 1
            if varE:
                c_up = c_up + 1
    print("P(+e|-b) = " + str((c_up/TURNS)/(c_down/TURNS)))


def question_4():
    global varA
    global varD
    global varE
    global c_up
    global c_down
    c_up = c_down = 0  # Counters
    for i in range(TURNS):
        var_a()
        var_b()
        var_c()
        var_d()
        var_e()
        if varD:
            if not varE:
                c_down = c_down + 1
                if varA:
                    c_up = c_up + 1
    print("P(+a|+d,-e) = " + str((c_up/TURNS)/(c_down/TURNS)))


def question_5():
    global varA
    global varB
    global varE
    global c_up
    global c_down
    c_up = c_down = 0  # Counters
    for i in range(TURNS):
        var_a()
        var_b()
        var_c()
        var_d()
        var_e()
        if varA:
            c_down = c_down + 1
            if varB:
                if not varE:
                    c_up = c_up + 1
    print("P(+b,-e|+a) = " + str((c_up/TURNS)/(c_down/TURNS)))


question_1()
question_2()
question_3()
question_4()
question_5()
