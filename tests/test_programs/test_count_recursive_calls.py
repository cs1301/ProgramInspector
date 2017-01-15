def basic_program(num):
    if num > 0:
        basic_program(num - 1)


def renamed_recursive_call(num):
    b = renamed_recursive_call
    if num > 0:
        b(num - 1)


def nested_recursive_call(num):
    def b(num_2):
        if num_2 > 0:
            nested_recursive_call(num_2 - 1)

    b(num)


def looping_recursion(num):
    if num > 0:
        for x in range(3):
            looping_recursion(num - 1)


def kwarg_function(num=5):
    if num > 0:
        kwarg_function(num - 1)


def var_arg_test(*args):
    if len(args):
        var_arg_test(*args[1:])


def large_arg_test(large_num):
    if large_num > 10 ** 100:
        large_arg_test(large_num - 1)


def many_constants(num):
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
         30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57,
         58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85,
         86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110,
         111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132,
         133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154,
         155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176,
         177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198,
         199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220,
         221, 222, 223, 224, 225, 226, 227, 228, 229, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 240, 241, 242,
         243, 244, 245, 246, 247, 248, 249, 250, 251, 252, 253, 254, 255, 256, 257, 258, 259, 260, 261, 262, 263, 264,
         265, 266, 267, 268, 269, 270, 271, 272, 273, 274, 275, 276, 277, 278, 279, 280, 281, 282, 283, 284, 285, 286,
         287, 288, 289, 290, 291, 292, 293, 294, 295, 296, 297, 298, 299, 300, 301, 302, 303, 304, 305, 306, 307, 308,
         309, 310, 311, 312, 313, 314, 315, 316, 317, 318, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330,
         331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347, 348, 349, 350, 351, 352,
         353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366, 367, 368, 369, 370, 371, 372, 373, 374,
         375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390, 391, 392, 393, 394, 395, 396,
         397, 398, 399, 400, 401, 402, 403, 404, 405, 406, 407, 408, 409, 410, 411, 412, 413, 414, 415, 416, 417, 418,
         419, 420, 421, 422, 423, 424, 425, 426, 427, 428, 429, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 440,
         441, 442, 443, 444, 445, 446, 447, 448, 449, 450, 451, 452, 453, 454, 455, 456, 457, 458, 459, 460, 461, 462,
         463, 464, 465, 466, 467, 468, 469, 470, 471, 472, 473, 474, 475, 476, 477, 478, 479, 480, 481, 482, 483, 484,
         485, 486, 487, 488, 489, 490, 491, 492, 493, 494, 495, 496, 497, 498, 499, 500, 501, 502, 503, 504, 505, 506,
         507, 508, 509, 510, 511, 512, 513, 514, 515, 516, 517, 518, 519, 520, 521, 522, 523, 524, 525, 526, 527, 528,
         529, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 540, 541, 542, 543, 544, 545, 546, 547, 548, 549, 550,
         551, 552, 553, 554, 555, 556, 557, 558, 559, 560, 561, 562, 563, 564, 565, 566, 567, 568, 569, 570, 571, 572,
         573, 574, 575, 576, 577, 578, 579, 580, 581, 582, 583, 584, 585, 586, 587, 588, 589, 590, 591, 592, 593, 594,
         595, 596, 597, 598, 599, 600, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 611, 612, 613, 614, 615, 616,
         617, 618, 619, 620, 621, 622, 623, 624, 625, 626, 627, 628, 629, 630, 631, 632, 633, 634, 635, 636, 637, 638,
         639, 640, 641, 642, 643, 644, 645, 646, 647, 648, 649, 650, 651, 652, 653, 654, 655, 656, 657, 658, 659, 660,
         661, 662, 663, 664, 665, 666, 667, 668, 669, 670, 671, 672, 673, 674, 675, 676, 677, 678, 679, 680, 681, 682,
         683, 684, 685, 686, 687, 688, 689, 690, 691, 692, 693, 694, 695, 696, 697, 698, 699, 700, 701, 702, 703, 704,
         705, 706, 707, 708, 709, 710, 711, 712, 713, 714, 715, 716, 717, 718, 719, 720, 721, 722, 723, 724, 725, 726,
         727, 728, 729, 730, 731, 732, 733, 734, 735, 736, 737, 738, 739, 740, 741, 742, 743, 744, 745, 746, 747, 748,
         749, 750, 751, 752, 753, 754, 755, 756, 757, 758, 759, 760, 761, 762, 763, 764, 765, 766, 767, 768, 769, 770,
         771, 772, 773, 774, 775, 776, 777, 778, 779, 780, 781, 782, 783, 784, 785, 786, 787, 788, 789, 790, 791, 792,
         793, 794, 795, 796, 797, 798, 799, 800, 801, 802, 803, 804, 805, 806, 807, 808, 809, 810, 811, 812, 813, 814,
         815, 816, 817, 818, 819, 820, 821, 822, 823, 824, 825, 826, 827, 828, 829, 830, 831, 832, 833, 834, 835, 836,
         837, 838, 839, 840, 841, 842, 843, 844, 845, 846, 847, 848, 849, 850, 851, 852, 853, 854, 855, 856, 857, 858,
         859, 860, 861, 862, 863, 864, 865, 866, 867, 868, 869, 870, 871, 872, 873, 874, 875, 876, 877, 878, 879, 880,
         881, 882, 883, 884, 885, 886, 887, 888, 889, 890, 891, 892, 893, 894, 895, 896, 897, 898, 899, 900, 901, 902,
         903, 904, 905, 906, 907, 908, 909, 910, 911, 912, 913, 914, 915, 916, 917, 918, 919, 920, 921, 922, 923, 924,
         925, 926, 927, 928, 929, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 940, 941, 942, 943, 944, 945, 946,
         947, 948, 949, 950, 951, 952, 953, 954, 955, 956, 957, 958, 959, 960, 961, 962, 963, 964, 965, 966, 967, 968,
         969, 970, 971, 972, 973, 974, 975, 976, 977, 978, 979, 980, 981, 982, 983, 984, 985, 986, 987, 988, 989, 990,
         991, 992, 993, 994, 995, 996, 997, 998, 999]
    if num > 0:
        many_constants(num - 1)


def many_globals(num):
    global a
    a = 97
    global b
    b = 98
    global c
    c = 99
    global d
    d = 100
    global e
    e = 101
    global f
    f = 102
    global g
    g = 103
    global h
    h = 104
    global i
    i = 105
    global j
    j = 106
    global k
    k = 107
    global l
    l = 108
    global m
    m = 109
    global n
    n = 110
    global o
    o = 111
    global p
    p = 112
    global q
    q = 113
    global r
    r = 114
    global s
    s = 115
    global t
    t = 116
    global u
    u = 117
    global v
    v = 118
    global w
    w = 119
    global x
    x = 120
    global y
    y = 121
    global z
    z = 122
    global A
    A = 65
    global B
    B = 66
    global C
    C = 67
    global D
    D = 68
    global E
    E = 69
    global F
    F = 70
    global G
    G = 71
    global H
    H = 72
    global I
    I = 73
    global J
    J = 74
    global K
    K = 75
    global L
    L = 76
    global M
    M = 77
    global N
    N = 78
    global O
    O = 79
    global P
    P = 80
    global Q
    Q = 81
    global R
    R = 82
    global S
    S = 83
    global T
    T = 84
    global U
    U = 85
    global V
    V = 86
    global W
    W = 87
    global X
    X = 88
    global Y
    Y = 89
    global Z
    Z = 90
    global aa
    aa = 194
    global bb
    bb = 196
    global cc
    cc = 198
    global dd
    dd = 200
    global ee
    ee = 202
    global ff
    ff = 204
    global gg
    gg = 206
    global hh
    hh = 208
    global ii
    ii = 210
    global jj
    jj = 212
    global kk
    kk = 214
    global ll
    ll = 216
    global mm
    mm = 218
    global nn
    nn = 220
    global oo
    oo = 222
    global pp
    pp = 224
    global qq
    qq = 226
    global rr
    rr = 228
    global ss
    ss = 230
    global tt
    tt = 232
    global uu
    uu = 234
    global vv
    vv = 236
    global ww
    ww = 238
    global xx
    xx = 240
    global yy
    yy = 242
    global zz
    zz = 244
    global AA
    AA = 130
    global BB
    BB = 132
    global CC
    CC = 134
    global DD
    DD = 136
    global EE
    EE = 138
    global FF
    FF = 140
    global GG
    GG = 142
    global HH
    HH = 144
    global II
    II = 146
    global JJ
    JJ = 148
    global KK
    KK = 150
    global LL
    LL = 152
    global MM
    MM = 154
    global NN
    NN = 156
    global OO
    OO = 158
    global PP
    PP = 160
    global QQ
    QQ = 162
    global RR
    RR = 164
    global SS
    SS = 166
    global TT
    TT = 168
    global UU
    UU = 170
    global VV
    VV = 172
    global WW
    WW = 174
    global XX
    XX = 176
    global YY
    YY = 178
    global ZZ
    ZZ = 180
    global aaa
    aaa = 291
    global bbb
    bbb = 294
    global ccc
    ccc = 297
    global ddd
    ddd = 300
    global eee
    eee = 303
    global fff
    fff = 306
    global ggg
    ggg = 309
    global hhh
    hhh = 312
    global iii
    iii = 315
    global jjj
    jjj = 318
    global kkk
    kkk = 321
    global lll
    lll = 324
    global mmm
    mmm = 327
    global nnn
    nnn = 330
    global ooo
    ooo = 333
    global ppp
    ppp = 336
    global qqq
    qqq = 339
    global rrr
    rrr = 342
    global sss
    sss = 345
    global ttt
    ttt = 348
    global uuu
    uuu = 351
    global vvv
    vvv = 354
    global www
    www = 357
    global xxx
    xxx = 360
    global yyy
    yyy = 363
    global zzz
    zzz = 366
    global AAA
    AAA = 195
    global BBB
    BBB = 198
    global CCC
    CCC = 201
    global DDD
    DDD = 204
    global EEE
    EEE = 207
    global FFF
    FFF = 210
    global GGG
    GGG = 213
    global HHH
    HHH = 216
    global III
    III = 219
    global JJJ
    JJJ = 222
    global KKK
    KKK = 225
    global LLL
    LLL = 228
    global MMM
    MMM = 231
    global NNN
    NNN = 234
    global OOO
    OOO = 237
    global PPP
    PPP = 240
    global QQQ
    QQQ = 243
    global RRR
    RRR = 246
    global SSS
    SSS = 249
    global TTT
    TTT = 252
    global UUU
    UUU = 255
    global VVV
    VVV = 258
    global WWW
    WWW = 261
    global XXX
    XXX = 264
    global YYY
    YYY = 267
    global ZZZ
    ZZZ = 270
    if num > 0:
        many_globals(num - 1)


def unending_recursion():
    unending_recursion()


def timeout_test():
    while True:
        pass
