"""
Languages
CP1404/CP5632 Practical
Estimate: 30 minutes
Actual: 45 minutes
A program to print the dynamic languages.
"""

from prac_06.programming_language import ProgrammingLanguage

python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
print(python)
programming_languages = [python, ruby, visual_basic]
for programming_language in programming_languages:
    if ProgrammingLanguage.is_dynamic(programming_language):
        print(programming_language.language)
