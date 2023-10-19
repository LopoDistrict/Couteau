# import required module
import os

# assign directory
directory = r'C:\Users\LordN\OneDrive\Bureau\code'

# iterate over files in
# that directory
for root, dirs, files in os.walk(directory):
	for filename in files:
		print(os.path.join(root, filename))
print("All good bro! :)")
