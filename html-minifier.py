# install the htmlmin library by excecuting :
# pip install htmlmin
import htmlmin
import sys
import os

if __name__=="__main__":
	if(len(sys.argv))!=2:
		print("Two Arguments Required")
		print("1st Argument : .py file excecuted")
		print("2nd Argument : .html file to be minified")
		sys.exit(0)
	html_filename = sys.argv[1]
	#print(html_filename)
	if(html_filename.endswith(".html")==False):
		print("The file (2nd Argument) must be HTML (.html)")
		sys.exit(0)

	folder_to_be_saved = os.path.dirname(sys.argv[1]);
	#print(folder_to_be_saved)
	minified_html_filename = os.path.splitext(os.path.basename(html_filename))[0]+".min.html"
	#print(minified_html_filename)
	if(folder_to_be_saved==""):
		complete_file_name = minified_html_filename
	else:
		complete_file_name = folder_to_be_saved+'\\'+minified_html_filename
	#print(complete_file_name)
	f = open(complete_file_name, "w")
	with open(html_filename) as html_file:
		initial_size = os.path.getsize(html_filename)
		print(f"Initial Size : {initial_size} Bytes")
		f.write(htmlmin.minify(html_file.read(), remove_comments=True, remove_all_empty_space=True))
		f.close()
		minified_size = os.path.getsize(complete_file_name)
		print(f"Minified Size : {minified_size} Bytes")
		print(f"Compression Rate : {round(((minified_size/initial_size)*100),2)} %")