import sys

script, encoding, error = sys.argv


def main(language_file, encoding, errors):
	line = language_file.readline() #不需要seek（0）定位？
	# print(f'line\'s type: {type(line)}')  line是字符串

	if line:
		print_line(line, encoding, errors)
		return main(language_file, encoding, errors)


def print_line(line, encoding, errors):
	next_lang = line.strip()
	raw_bytes = next_lang.encode(encoding, errors=errors)
	cooked_string = raw_bytes.decode(encoding, errors=errors)

	print(raw_bytes, '<===>', cooked_string)


languages = open('ex23_languages.txt', encoding='utf-8')

main(languages, encoding, error)