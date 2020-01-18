def parse_mastery_response(mastery_response, field_name):
	counter = 0
	for champion in mastery_response:
		counter += champion[field_name]

	return counter
