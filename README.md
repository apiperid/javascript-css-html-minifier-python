# javascript-css-html-minifier-python
This repository has python codes for just <strong>minifying javascript ,html and css code</strong>.
There are many tools that do the same thing and many more (e.g Koala) but this is for someone who wants to do it from script without extra software.<br>

# Essential setups
In order to run the <strong>javascript-minifier.py</strong> first you have to install the jsmin package.You can do that by excecuting :<br>
<code> pip install jsmin</code>

In order to run the <strong>css-minifier.py</strong> first you have to install the csscompressor package.You can do that by excecuting :<br>
<code> pip install csscompressor</code>

In order to run the <strong>html-minifier.py</strong> first you have to install the htmlmin package.You can do that by excecuting :<br>
<code> pip install htmlmin</code>
 
# Run
Both .py scripts have the same arguments :<br>
<code>python script filename</code><br><br>
where <strong>script</strong> is either <strong>javascript-minifier.py</strong> or <strong>css-minifier.py</strong> or <strong>html-minifier.py</strong><br>
<strong>filename</strong> is the path of the file (.js or .css) you want to minify.

# Output
The output for all scripts is a new file with the stamp min (e.g input=myFile.js , output=myFile.min.js)

# Python Version
The Python Version is 3.7.4
