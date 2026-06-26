# REGULAR EXPRESSIONS (REGEX) IN PYTHON

# Regular Expressions (Regex) are special patterns used to search, match, extract, and replace text.
# Python provides the built-in 're' module for working with regular expressions.

# Common Uses:
# -> Searching for words
# -> Validating emails and phone numbers
# -> Extracting numbers from text
# -> Replacing words
# -> Data Cleaning

#------------------------------------------------#------------------------------------------------#------------------------------------------------#------------------------------------------------#
import re
text = "The quick brown fox jumps over the lazy dog."


# Returns:
# -> Match object if found
# -> None if not found
# Syntax: re.search(pattern, string)



# re.search : Search for a pattern
match = re.search("brown", text)
print(match)

if match:
    print("Match found!")
    print("Start index:", match.start())    # start() returns the index where the matched word starts.
    print("End index:", match.end())        # end() returns ONE POSITION AFTER the last character.



# re.findall: Finds ALL occurrences of a pattern.
# Returns a LIST: Unlike re.search(), it does NOT stop after the first match.

# Syntax: re.findall(pattern, string)

matches = re.findall("the", text, re.IGNORECASE) # Case-insensitive search
print("Matches:", matches)
# Output: ['The', 'the']




# re.sub : Replace all occurrences of a pattern
# Syntax: re.sub(old_pattern, new_pattern, string)

new_text = re.sub("fox", "cat", text)
print("New text:", new_text)




# Compile a regex for efficiency (if used multiple times)

# Why use it?
# If the SAME regex pattern will be used many times, compiling improves efficiency because Python does not need to parse the pattern repeatedly.

# Syntax: pattern = re.compile(regex)

pattern = re.compile(r"\b\w+\b")   # Matches whole words
words = pattern.findall(text)
print("Words:", words)

