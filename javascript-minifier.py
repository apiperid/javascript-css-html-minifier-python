# install the jsmin library by excecuting :
# pip install jsmin
from jsmin import jsmin
import sys
import os

if __name__=="__main__":
	if(len(sys.argv))!=2:
		print("Two Arguments Required")
		print("1st Argument : .py file excecuted")
		print("2nd Argument : .js file to be minified")
		sys.exit(0)
	javascript_filename = sys.argv[1]
	#print(javascript_filename)
	if(javascript_filename.endswith(".js")==False):
		print("The file (2nd Argument) must be JavaScript (.js)")
		sys.exit(0)

	folder_to_be_saved = os.path.dirname(sys.argv[1]);
	#print(folder_to_be_saved)
	minified_javascript_filename = os.path.splitext(os.path.basename(javascript_filename))[0]+".min.js"
	#print(minified_javascript_filename)
	if(folder_to_be_saved==""):
		complete_file_name = minified_javascript_filename
	else:
		complete_file_name = folder_to_be_saved+'\\'+minified_javascript_filename
	#print(complete_file_name)
	f = open(complete_file_name, "w")
	with open(javascript_filename) as js_file:
		initial_size = os.path.getsize(javascript_filename)
		print(f"Initial Size : {initial_size} Bytes")
		f.write(jsmin(js_file.read()))
		f.close()
		minified_size = os.path.getsize(complete_file_name)
		print(f"Minified Size : {minified_size} Bytes")
		print(f"Compression Rate : {round(((minified_size/initial_size)*100),2)} %")