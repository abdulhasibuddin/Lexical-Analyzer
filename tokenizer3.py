def main():
	string = []
	operator_list = ['+','-','*','/','&','|','<','=','>','%','+=','-=','*=','/=','++','--','||','==','<=','>=','&&']
	digit_list = ['0','1','2','3','4','5','6','7','8','9']
	char_list = ['_','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
	keyword_list = ['int','float','double','if', 'else', 'for', 'printf','while']
	found_tokens = []
	found_keywords = []
	found_identifier = []
	found_operators = []
	found_numbers = []
	found_errors = []
	string = input("Enter input:")
	string_length = len(string)
	string_pointer = 0
	double_string_operator_check = False
	current_char = ''
	is_digit = False
	is_space = False
	is_error = False

	##################### TOKENIZATION:: ##########################
	for s in string:
		string_pointer += 1;
		
		if s in digit_list:
			is_digit = True
		if is_digit==True and s in char_list:
			is_error = True
			is_digit = False
		if (s==' ' or s==';') and is_error==True:
			found_errors.append(current_char)
			current_char = ''
			is_error = False
			if s==';':
					found_tokens.append(s)
					break
			continue
		if s==' ' and is_error==False: #When a word ends...
			found_tokens.append(current_char)
			current_char = ''
			is_digit = False
			continue
		if s==';' and is_error==False: #When sentence is complete...
			found_tokens.append(current_char)
			found_tokens.append(s)
			break
		if s in operator_list and double_string_operator_check==False:
			if not current_char=='':
				found_tokens.append(current_char)
			current_char = s
			double_string_operator_check = True
			continue
		if s in operator_list and double_string_operator_check==True:
			current_char += s
			continue
		if s not in operator_list and double_string_operator_check==True:
			if not current_char=='':
				found_tokens.append(current_char)
			double_string_operator_check = False
			if not s==' ':
				current_char = s
			continue
		current_char += s
	##################### End of TOKENIZATION ############################

	##################### LEXICAL ANALYSIS:: #############################
	for token in found_tokens:
		if token in keyword_list:
			found_keywords.append(token)
			continue
		if token in operator_list:
			found_operators.append(token)
			continue

	##################### End of LEXICAL ANALYSIS ########################

	print("Tokens: ")
	print(found_tokens)
	print("\nKeywords: ")
	print(found_keywords)
	#print("\nIdentifiers: ")
	#print(found_identifier)
	#print("\nNumbers: ")
	#print(found_numbers)
	print("\nOperators: ")
	print(found_operators)
	print("\nErrors: ")
	print(found_errors)

if __name__=='__main__':
	main()
