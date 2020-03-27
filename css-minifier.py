# install the csscompressor library by excecuting :
# pip install csscompressor
from csscompressor import compress
import sys
import os

if __name__=="__main__":
	if(len(sys.argv))!=2:
		print("Two Arguments Required")
		print("1st Argument : .py file excecuted")
		print("2nd Argument : .css file to be minified")
		sys.exit(0)
	css_filename = sys.argv[1]
	#print(css_filename)
	if(css_filename.endswith(".css")==False):
		print("The file (2nd Argument) must be Cascading Style Sheets (.css)")
		sys.exit(0)

	folder_to_be_saved = os.path.dirname(sys.argv[1]);
	#print(folder_to_be_saved)
	minified_css_filename = os.path.splitext(os.path.basename(css_filename))[0]+".min.css"
	#print(minified_css_filename)
	if(folder_to_be_saved==""):
		complete_file_name = minified_css_filename
	else:
		complete_file_name = folder_to_be_saved+'\\'+minified_css_filename
	#print(complete_file_name)
	f = open(complete_file_name, "w")
	with open(css_filename) as css_file:
		initial_size = os.path.getsize(css_filename)
		print(f"Initial Size : {initial_size} Bytes")
		f.write(compress(css_file.read()))
		f.close()
		minified_size = os.path.getsize(complete_file_name)
		print(f"Minified Size : {minified_size} Bytes")
		print(f"Compression Rate : {round(((minified_size/initial_size)*100),2)} %")