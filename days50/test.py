def findContentChildren(g, s):
    # count = 0
    # if not g or not s:
    #     return count
    #
    # g = sorted(g)  # 孩子胃口
    # s = sorted(s)  # 饼干大小
    #
    #
    # for i in range(len(s)):
    #     if g[0] <= s[i]:
    #         count = 1
    #         g.pop(0)
    #         s.remove(s[i])
    #         break
    #     else:
    #         s.remove(s[i])
    #
    # if count == 0:
    #     return count
    #
    # count += findContentChildren(g, s)
    # return count
    g.sort()
    s.sort()
    i = 0
    for e in s:
        if i == len(g):
            break
        if e >= g[i]:
            i += 1
    return i

# g=[1,2,3]
# s=[1,1]
# g=[1,2]
# s=[1,2,3]

g=[10,9,8,7]
s=[5,6,7,8]
# g=[250,490,328,149,495,325,314,360,333,418,430,458]
# s=[376,71,228,110,215,410,363,135,508,268,494,288,24,362,20,5,247,118,152,393,458,354,201,188,425,167,220,114,148,43,403,385,512,459,71,425,142,102,361,102,232,203,25,461,298,437,252,364,171,240,233,257,305,346,307,408,163,216,243,261,137,319,33,91,116,390,139,283,174,409,191,338,123,231,101,458,497,306,400,513,175,454,273,88,169,250,196,109,505,413,371,448,12,193,396,321,466,526,276,276,198,260,131,322,65,381,204,32,83,431,81,108,366,188,443,331,102,72,496,521,502,165,439,161,257,324,348,176,272,341,230,323,124,13,51,241,186,329,70,387,93,126,159,370,292,16,211,327,431,26,70,239,379,368,215,501,382,299,481,163,100,488,259,524,481,87,118,112,110,425,295,352,62,162,19,404,301,163,389,13,383,43,397,165,385,274,59,499,136,309,301,345,381,124,394,492,96,243,4,297,153,9,210,291,33,450,202,313,138,214,308,239,129,154,354,289,484,388,351,339,337,161,97,185,190,498,348,242,38,217,343,170,269,465,514,89,366,447,166,52,33,436,268,3,74,505,403,302,513,69,439,68,72,403,33,130,466,417,186,339,328,237,138,427,392,496,430,442,260,229,372,217,399,203,170,246,153,137,358,138,22,19,110,304,399,458,165,372,254,358,364,345,52,150,121,226,156,231,83,377,237,342,184,27,73,392,238,366,258,434,498,184,309,394,110,246,430,437,33,488,520,69,24,18,221,146,19,147,283,407,437,185,399,238,471,117,110,266,507,263,293,94,314,31,217,224,36,515,147,432,270,327,521,113,153,14,160,435,396,501,13,461,103,441,461,68,55,510,380,291,305,365,511,218,515,148,324,136,291,519,201,192,97,183,448,294,242,379,52,154,224,183,344,452,240,380,338,337,437,92,206,490,405,396,274,41,305,170,423,437,92,480,477,260,224,176,239,466,525,458,226,189,251,516,479,305,463,116,126,88,490,93,389,246,480,139,193,303,205,270,83,89,461,492,209,311,368,457,478,188,484,4,501,513,18,2,90,39,205,500,391,191,229,32,147,438,123,493,71,363,143,163,110,199,305,476,430,86,378,416,444,325,207,519,380,81,116,503,13,211,290,327,510,141,37,242,370,117,208,58,336,432,19,474,488,74,472,63,287,11,470,221,349,211,191,497,50,442,315,376,355,302,206,291,376,499,405,498,202,40,115,178,66,438,446,498,443,292,123,493,505,205,490,368,349,341,107,290,428,141,271,117,54,410,172,92,450,524,427,371,69,77,35,234,25,152,365,509,154,61,143,111,188,101,327,21,378,186,57,241,351,136,213,143,86,325,83,358,79,427,406,491,192,248,360,428,478,385,252,270,106,524,343,92,483,9,15,54,511,296,238,392,106,198,64,394,122,187,14,481,50,221,226,63,50,449,504,357,499,120,448,275,363,465,451,68,25,233,124,520,415,90,302,246,19,63,335,308,235,297,410,349,78,324,210,327,199,202,455,387,159,148,344,375,127,368,305,347,307,451,412,323,188,16,139,143,362,228,493,334,341,406,113,368,234,439,193,211,500,231,311,204,99,82,52,66,286,142,27,445,12,410,370,118,104,358,330,96,351,93,469,63,450,14,455,309,84,101,58,166,224,34,158,322,388,345,328,329,509,168,292,367,5,309,477,75,306,524,416,35,417,229,448,513,99,179,526,147,390,260,459,394,503,414,221,429,469,160,415,417,435,139,277,195,340,526,7,369,177,324,132,505,36,239,354,414,144,221,378,441,13,93,70,104,449,387,288,492,329,257,489,501,308,376,289,421,320,226,407,294,463,209,322,34,72,310,2,293,11,196,411,136,455,106,432,193,475,518,243,306,410,14,273,145,492,290,33,345,108,75,271,115,517,456,326,108,319,470,40,429,408,380,271,423,475,100,402,408,379,428,512,340,8,172,43,383,72,422,35,57,281,185,304,442,224,376,163,478,210,146,266,139,309,263,210,400,131,400,56,371,458,365,215,173,148,349,369,300,144,225,162,335,221,311,276,248,261,90,270,12,450,80,420,227,126,16,263,326,139,104,454,137,295,68,400,277,463,88,355,32,242,116,205,396,397,448,217,505,224,376,280,252,455,46,49,455,60,228,30,70,157,346,190,455,222,426,377,447,299,305,484,282,135,147,262,339,139,446,272,215,89,304,194,495,466,509,2,329,57,264,230,121,273,237,498,179,216,54,317,473,198,331,117,479,503,438,514,58,72,259,224,424,381,35,53,40,393,274,180,174,435,131,426,401,195,472,59,157,178,73,217,262,253,387,487,430,342,487,122,352,496,116,214,159,403,513,434,348,72,321,72,174,113,335,31,84,353,8,111,11,284,378,406,2,156,409,69,8,332,15,467,206,57,408,272,446,10,345,457,194,146,459,222,371,22,159,73,90,440,144,87,244,506,129,526,237,27,83,249,281,259,171,243,524,385,490,383,151,337,488,312,117,313,357,231,251,263,396,277,355,350,82,75,382,73,124,126,49,33,160,118,180,166,357,143,254,417,410,280,526,217,358,2,469,328,148,350,99,465,423,179,72,496,150,46,154,57,65,332,489,59,101,138,276,290,411,35,85,166,350,338,320,167,11,395,159,49,75,379,33,123,90,118,133,485,484,370,224,421,16,39,340,70,311,448,93,53,100,230,345,287,57,318,420,194,291,146,384,262,388,313,453,53,461,266,208,152,15,276,459,523,17,309,187,171,16,482,149,184,54,372,177,43,240,213,67,168,194,296,475,344,152,478,244,122,48,360,426,492,223,189,291,259,475,237,263,518,460,279,261,487,81,337,470,301,175,343,113,111,524,104,127,428,403,449,481,404,297,332,215,517,92,101,353,199,456,475,44,399,67,270,394,90,421,93,66,162,396,352,397,26,461,140,211,458,375,82,177,108,71,30,175,443,471,34,6,423,385,78,422,254,480,469,236,96,394,48,175,300,170,366,49,168,28,154,315,84,52,255,110,309,320,295,123,337,202,186,38,54,309,501,119,99,448,163,110,138,119,244,306,384,141,441,419,410,168,370,440,483,398,328,419,522,322,398,365,149,523,453,351,347,408,209,422,341,44,270,3,135,342,51,270,115,181,474,487,195,266,56,149,22,11,194,293,238,206,220,398,9,169,431,248,514,22,186,135,348,319,206,513,289,455,21,421,8,258,176,408,327,470,379,27,204,339,344,192,127,466,347,414,429,399,212,244,350,103,434,332,414,235,70,517,45,370,212,300,400,241,128,111,93,217,287,140,72,188,208,33,227,124,401,306,517,416,324,485,191,79,194,342,183,344,206,355,195,40,117,112,313,520,126,38,211,151,124,447,28,68,284,214,187,411,340,513,87,465,263,511,465,87,205,179,320,485,169,153,34,403,417,226,246,447,219,420,268,495,351,269,214,311,188,28,60,167,93,62,173,469,423,58,358,161,83,297,461,53,357,227,20,191,96,182,212,52,113,242,442,420,243,314,426,524,115,56,172,173,477,189,188,414,122,451,453,465,262,17,398,425,519,243,437,251,105,94,503,213,405,362,470,148,96,343,470,30,344,114,285,37,49,323,424,513,119,194,280,179,332,198,389,412,273,34,209,72,314,203,389,471,339,173,280,82,219,90,523,36,187,453,439,418,381,324,146,430,456,394,461,345,449,129,150,241,512,411,78,26,273,275,424,217,188,172,391,223,489,35,420,300,322,518,2,117,122,290,318,518,147,470,75,308,368,12,510,206,157,138,355,487,446,217,121,443,505,294,218,339,523,21,125,249,185,520,453,189,454,146,9,259,198,399,121,436,511,397,525,313,489,144,52,372,156,59,316,231,89,241,207,325,117,415,4,208,116,321,166,223,463,29,260,360,408,124,464,188,194,245,401,491,389,145,414,120,375,422,423,153,489,220,42,374,179,402,367,434,471,203,303,83,428,123,49,487,127,251,213,64,116,470,192,436,489,428,61,302,273,219,495,172,354,17,163,30,105,487,303,224,260,59,121,199,251,166,437,232,494,422,88,435,185,411,162,296,327,186,140,450,323,289,38,187,499,490,78,259,156,275,234,369,328,511,280,17,303,431,48,229,513,72,42,98,515,110,363,446,202,79,328,485,118,434,487,310,401,112,472,258,462,84,72,378,337,413,395,32,230,145,289,504,167,158,128,356,435,26,294,130,277,276,78,133,519,467,208,89,89,418,107,429,31,86,387,172,193,343,390,303,61,452,10,161,254,48,492,292,114,240,158,241,291,383,345,429,358,227,224,340,63,279,203,205,382,461,203,496,498,6,453,89,24,507,143,63,408,165,402,336,333,205,153,180,288,399,83,122,504,178,24,60,471,283,378,2,210,33,315,253,124,134,141,363,410,267,40,310,159,391,33,345,496,298,380,190,202,294,149,67,4,427,381,163,332,300,389,176,254,222,378,345,486,259,111,285,249,482,295,26,313,282,121,115,406,32,242,134,476,80,131,459,334,186,112,419,488,460,81,120,452,191,490,29,31,289,104,442,172,457,256,154,1,365,124,472,388,374,365,300,474,229,147,447,314,399,230,187,397,105,399,65,516,296,4,14,351,407,331,238,278,376,325,149,336,85,458,281,467,253,411,494,49,177,26,119,471,342,114,5,340,36,481,417,516,123,168,177,111,506,242,313,162,478,126,255,426,246,420,236,222,517,479,71,146,148,509,299,60,341,345,228,97,222,71,127,421,395,476,295,521,523,44,68,156,424,251,362,356,111,282,400,401,465,341,512,217,275,232,375,70,480,136,263,235,513,110,335,257,167,117,342,488,176,396,18,15,110,225,313,214,173,418,214,160,358,43,278,225,342,415,464,521,341,395,163,420,136,461,35,469,157,268,284,30,101,156,67,149,91,139,84,298,419,123,345,186,140,418,453,46,423,494,4,338,521,227,131,109,48,341,419,164,81,250,391,10,356,130,264,311,513,146,495,395,211,227,182,169,242,459,207,307,519,349,4,194,99,220,292,18,335,178,283,412,224,304,214,258,402,236,235,470,289,269,341,18,210,151,361,157,317,181,129,219,320,140,180,267,311,346,243,156,510,433,125,148,307,338,191,398,173,87,94,56,296,75,100,513,504,99,267,105,428,258,515,437,44,464,319,128,184,464,102,328,505,291,20,396,252,437,77,94,493,462,327,315,178,13,318,447,510,91,411,44,270,398,79,519,438,367,141,382,501,521,341,194,516,397,441,439,21,501,345,268,390,234,378,428,247,133,454,273,88,289,330,45,101,264,478,28,338,185,171,235,514,442,353,243,352,202,268,4,322,300,71,126,277,473,70,453,256,487,500,304,128,206,63,58,289,452,359,12,286,513,264,467,96,444,509,500,205,402,404,89,86,136,189,180,478,165,508,320,437,341,60,431,113,365,359,150,269,217,313,247,315,250,223,385,381,167,499,503,13,243,100,102,446,126,485,205,400,89,313,211,64,50,262,121,472,236,14,465,158,502,493,162,121,199,242,410,31,258,34,107,42,175,324,101,224,293,224,397,112,314,251,2,482,331,210,484,324,297,291,255,101,146,355,443,310,416,8,292,505,87,496,370,5,7,264,348,77,102,478,245,156,114,452,427,518,506,342,181,52,397,203,17,152,101,181,416,221,43,176,461,374,13,469,49,226,212,406,205,388,29,20,447,107,462,258,358,428,192,182,323,277,463,159,430,140,406,432,305,91,41,504,103,402,141,176,15,31,89,364,109,92,355,155,2,468,307,418,250,49,384,399,134,219,416,59,473,409,505,122,166,410,289,278,328,493,180,94,341,491,5,160,465,214,141,79,40,327,362,442,521,365,385,96,480,337,269,315,341,399,381,87,174,128,313,429,259,434,244,495,5,238,416,192,225,275,14,416,446,418,123,469,468,112,253,504,221,502,244,175,92,520,453,234,362,219,220,138,303,430,247,125,447,392,2,27,40,92,127,450,511,438,397,398,46,246,222,212,195,283,329,487,423,378,58,428,168,428,405,358,302,324,153,243,87,336,438,342,327,389,282,165,129,82,454,145,236,456,378,297,127,23,522,133,279,386,85,343,514,301,169,279,251,123,243,74,309,46,29,198,341,373,386,130,282,144,211,69,223,124,194,173,59,141,414,431,406,81,134,298,46,115,188,329,66,337,61,9,330,153,355,524,465,68,41,134,33,460,33,14,187,469,217,256,239,458,523,410,263,45,391,65,337,426,232,86,65,201,249,243,262,352,238,177,54,57,359,230,314,327,410,268,4,90,431,158,253,89,18,176,393,244,362,156,134,28,444,115,325,331,181,338,49,262,361,213,412,66,36,283,216,297,371,53,380,142,2,66,370,34,233,436,255,214,157,423,220,339,516,278,196,259,361,143,63,346,241,465,116,193,55,368,24,246,353,205,28,210,87,236,85,463,349,460,463,379,335,341,405,10,309,168,429,205,177,35,284,310,95,401,362,428,33,320,513,20,293,481,19,396,425,418,272,22,487,502,331,511,361,471,488,282,411,85,213,401,373,444,241,337,375,470,506,140,67,335,56,149,312,433,54,29,417,235,285,15,351,112,366,91,168,86,458,151,304,64,92,87,11,421,393,24,31,189,357,451,377,50,338,233,153,292,423,182,165,72,275,329,191,6,361,477,359,172,69,445,275,82,458,482,353,222,505,326,27,127,237,347,5,60,496,324,106,226,195,414,354,368,76,47,353,506,399,120,202,237,309,472,446,487,471,315,16,87,267,369,28,172,283,372,323,355,149,182,70,501,58,344,324,132,70,525,457,283,183,415,368,63,57,360,334,183,289,285,179,184,464,150,307,431,405,178,221,346,355,80,169,404,46,218,16,161,369,41,71,500,105,373,462,274,151,457,28,55,517,319,252,159,425,514,441,466,349,484,351,313,508,508,345,63,197,342,21,359,360,391,317,117,108,504,18,237,379,267,313,356,322,90,518,456,125,48,300,199,465,320,3,497,303,113,405,228,130,135,401,421,174,451,326,30,27,320,346,400,317,86,114,488,426,507,141,458,181,116,109,60,289,389,435,41,228,358,84,489,100,325,45,426,158,225,293,409,447,267,413,478,210,32,344,237,186,236,295,511,87,105,408,117,321,391,407,333,203,241,498,194,96,23,427,518,487,271,333,454,357,166,149,322,351,463,455,508,466,322,445,267,492,45,75,463,162,181,152,164,122,382,288,25,152,178,52,301,115,461,155,33,54,34,318,175,1,123,405,454,478,259,149,35,461,14,29,469,389,261,285,245,514,283,468,397,381,434,140,138,393,367,64,481,514,518,43,34,464,345,363,153,504,100,479,308,303,356,392,474,506,214,119,332,499,313,244,473,275,247,487,9,472,89,397,75,246,472,297,341,166,223,93,503,289,164,423,39,211,270,4,3,97,141,406,279,411,386,519,524,107,494,46,381,85,186,141,447,279,444,179,153,350,14,127,219,102,457,476,499,303,358,142,56,62,377,9,143,266,59,219,185,98,210,329,161,154,419,311,308,409,286,170,79,511,482,494,124,331,523,274,133,57,381,425,357,501,197,107,415,441,118,515,197,195,170,520,462,228,82,416,365,115,32,339,68,510,78,478,221,128,193,241,163,258,150,182,499,96,109,126,404,236,471,48,517,109,453,276,291,209,525,307,239,159,363,168,237,192,58,71,420,111,301,421,180,70,191,346,125,228,254,210,317,25,236,86,504,226,187,104,461,139,145,412,291,354,79,519,430,197,3,233,65,403,464,162,410,5,81,240,58,156,257,503,124,4,254,123,526,520,266,43,5,55,359,280,497,380,320,69,307,64,437,288,6,486,49,337,177,358,517,393,458,81,282,352,364,233,1,212,401,360,143,289,191,225,467,173,207,475,203,50,109,424,517,243,372,358,322,92,481,165,399,376,202,440,380,70,434,310,414,334,440,376,273,451,379,193,199,424,66,330,433,465,48,137,510,329,491,90,32,242,425,52,24,408,149,524,373,261]
res=findContentChildren(g,s)
print(res)