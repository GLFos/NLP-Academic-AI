from readability import Readability

text = "C:\\Users\\GLFos\\Documents\\HighSchool.txt"

with open(text, "r", encoding="utf-8") as file:
    content = file.read()

r = Readability(content)

fk = r.flesch_kincaid()
print("Flesch-Kincaid Score: ", fk.score)
print("Felsch-Kincaid Grade Level: ", fk.grade_level)

gf = r.gunning_fog()
print("Gunning Fog Score: ", gf.score)
print("Gunning Fog Grade Level: ", gf.grade_level)