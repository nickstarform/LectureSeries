all: clean slides

clean: 
	find . -name __pycache__ -print0 | xargs -0 rm -rf 
	find . -maxdepth 1 -name "*.html"  -print0 | xargs -0 rm -rf 

slides:
	jupyter nbconvert LectureSeries-python1.ipynb --to html &
	jupyter nbconvert LectureSeries-python2.ipynb --to html &
