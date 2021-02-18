import re

with open ('wbenjamin.art-fr.xml', 'r' ) as f:
    orig = f.read()

    # Create <head> </head> tags for Roman Numerals
    orig = re.sub(r"(^(?=[MDCLXVI])M*(C[MD]|D?C*)(X[CL]|L?X*)(I[XV]|V?I*)$)", r"<head>\1</head>", orig, flags = re.M)
    
    # Create </s> endtags (excludes last sentence)
    orig = re.sub(r"\.[^<]", ".</s> \n", orig, flags = re.M)

    # Edge case: </s> for last sentence
    orig = re.sub(r"to that of politics.", "to that of politics.</s>", orig, flags = re.M)

    # Replace ' with ’ (it was causing the text to be encoded as strings)
    orig = re.sub(r"'", "’", orig, flags = re.M)

    # Create <s> starttags (excludes first sentence)
    orig = re.sub(r"</s> \n", "</s> \n\n<s>", orig, flags = re.M)

    # Remove <s> starttags in front of <head> tags
    orig = re.sub(r"<s><head>", "<head>", orig, flags = re.M)

    # Add <s> starttags
    orig = re.sub(r"<s><head>", "<head>", orig, flags = re.M)

    # Edge case: <s> for first sentence
    orig = re.sub(r"Il est du principe", "<s>Il est du principe", orig, flags = re.M)

    # Remove beginning extra newline inside <s> tags
    orig = re.sub(r"<s>\n", "<s>", orig, flags = re.M)

    print(orig)
