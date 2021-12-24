
with open("./input/Names/invited_names.txt", "r") as f:
	invite_names = f.readlines()

for line in invite_names:
	name = line.strip()
	with open("./input/Letters/starting_letter.txt", "r") as letter:
		letter_file = letter.readlines()
		first_line = letter_file[0]
		replaced_name = first_line.replace("[name]",name)
		letter_file[0]=replaced_name
	with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w")as file:
		file.writelines(letter_file)


##############################################
# Instructor solution - Option below
##############################################
#
# PLACEHOLDER = "[name]"
#
# with open("./input/Names/invited_names.txt", "r") as names_file:
# 	names = names_file.readlines()
#
# with open("./input/Letters/starting_letter.txt", "r") as letter_file:
# 	letter_contents = letter_file.read()
# 	for name in names:
# 		stripped_name = name.strip()
# 		new_letter = letter_contents.replace(PLACEHOLDER,stripped_name)
# 		with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as completed_letter:
# 			completed_letter.write(new_letter)