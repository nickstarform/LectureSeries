all: clean

clean: 
	find . -name __pycache__ -print0 | xargs -0 rm -rf 
	find . -name "*.html" -maxdepth 1 -print0 | xargs -0 rm -rf 

slides:
	jupyter nbconvert LectureSeries-python1.ipynb --to html
	jupyter nbconvert LectureSeries-python2.ipynb --to html
	jupyter nbconvert LectureSeries-python1.ipynb --to pdf
	jupyter nbconvert LectureSeries-python2.ipynb --to pdf
