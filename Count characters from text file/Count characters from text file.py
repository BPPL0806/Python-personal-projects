def count(text, character):
    characters_counted = 0
    for x in text :
        if x == character:
            characters_counted += 1
    print(characters_counted, "characters", character, "have been counted.")

file = open("text_to_count_from.txt", "w+")
text = file.read()
file.close()

while True:
    selected_letter = input("What character should program count?" + "\n")
    if len(selected_letter) > 1:
        print("Please select single character." + "\n")
    else:
        break

count(text, selected_letter)
