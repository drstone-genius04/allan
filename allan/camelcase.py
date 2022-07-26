

def convert_camel(string):
	words = string.split(" ")
	result = words[0].lower()
	for word in words[1:]:
		result += word.capitalize()
	return(result)
	