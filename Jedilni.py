#-*- coding: utf-8 -*-

print ("Pozdravljeni v elektronskem jedilnem listu!")

jedilni_list = {}

while True:
    dodaj_jed = raw_input("Vnesi jed: ")
    dodaj_ceno = raw_input("Vnesi ceno jedi: ")
    jedilni_list[dodaj_jed] = dodaj_ceno

    addNew = raw_input("Želite dodati novo jed? (da/ne): ")
    if addNew.lower() == "ne":
        break

with open("menu.txt", "w+") as menu_file:
    for jed in jedilni_list:
        menu_file.write(jed)
        menu_file.write(jedilni_list[jed])


