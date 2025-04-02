# 8. Explain why the code below prints different values on lines 3 and 4

text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29

# line 6: str.rfind method uses start & end arguments to start the search the substring; when start & end arguments are explicitly noted during the invocation, the method knows where the starting index is.

# line 5: use of a slice method means that a copy of the string is created and str.rfind() method performs its search on the copy and not the original line - thus the starting index for the copy will have changed

# ls:
# Line 3 first extracts a slice from text ranging from index 21 through index 35. That returns the string 'for the fjords'. rfind then returns 8, the index of the rightmost instance of an 'f'.

# On the other hand, line 4 does a search for the rightmost f between indexes 21 and 35. Since the f occurs at index 29, that's what the method returns.