search_term = input("What manga do you want to read? ")

titles_file = open("titles_and_links.txt")
mangas_list = {}
line_index = 0

for line in titles_file:
    if search_term in line.lower():
        mangas_list[line.split('"')[1]] = line_index
    line_index += 1

if mangas_list == {}:
    print("No manga found, search another one!")
else:
    for manga in mangas_list:
        print(manga)

titles_file.close()