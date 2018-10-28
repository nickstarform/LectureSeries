# this handles generating the website

LOGFILE := $(shell date +'%Y.%m.%d-%H.%M.%S')

all: refresh

refresh: clean regen

regen:
	python generate_website.py

clean: 
	${RM} -f ./*.log 
	${RM} -f ./build/*
	${RM} -rf __pycache__

update:
	git pull origin master
	make refresh

backup:
	mkdir -p backups &>/dev/null
	mkdir -p "./tmp.$(LOGFILE)" &>/dev/null
	cp -L -r build/* "./tmp.$(LOGFILE)" &>/dev/null
	tar -czvf "website_$(LOGFILE).tar.gz" "./tmp.$(LOGFILE)" &>/dev/null
	mv "website_$(LOGFILE).tar.gz" backups &>/dev/null
	${RM} -rf "./tmp.$(LOGFILE)" &>/dev/null
