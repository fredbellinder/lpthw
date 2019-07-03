row1 = True
row2 = False
row3 = False
row4 = True
row5 = True
row6 = True
row7 = False
row8 = True
row9 = False
row10 = False
row11 = True
row12 = False
row13 = True
row14 = False
row15 = False
row16 = False
row17 = True
row18 = True
row19 = False
row20 = False

print(True and True, "row1: ", row1)
print(False and True, "row2: ", row2)
print(1 == 1 and 2 == 1, "row3: ", row3)
print("test" == "test", "row4: ", row4)
print(1 == 1 or 2 == 1, "row5: ", row5)
print(True and 1 == 1, "row6: ", row6)
print(False and 0 != 0, "row7: ", row7)
print(True or 1 == 1, "row8: ", row8)
print("test" == "testing", "row9: ", row9)
print(1 != 0 and 2 == 1, "row10: ", row10)
print("test" != "testing", "row11: ", row11)
print("test" == 1, "row12: ", row12)
print(not (True and False), "row13: ", row13)
print(not (1 == 1 and 0 != 1), "row14: ", row14)
print(not (10 == 1 or 1000 == 1000), "row15: ", row15)
print(not (1 != 10 or 3 == 4), "row16: ", row16)
print(not ("testing" == "testing" and "Zed" == "Cool Guy"), "row17: ", row17)
print(1 == 1 and (not ("testing" == 1 or 1 == 0)), "row18: ", row18)
print("chunky" == "bacon" and (not(3 == 4 or 3 == 3)), "row19: ", row19)
print(3 == 3 and (not("testing" == "testing" or "Python" == "Fun")), "row20: ", row20)
