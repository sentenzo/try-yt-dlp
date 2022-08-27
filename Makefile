
# https://stackoverflow.com/a/4511164/2493536
ifdef OS # Windows
   RM = del /Q /S #Remove-Item -Recurse -Force -LiteralPath
   FixPath = $(subst /,\,$1)
   PYTHON = python
   EXT = .exe
else
   ifeq ($(shell uname), Linux) # Linux
      RM = rm -rf
	  FixPath = $1
	  PYTHON = python3.10
   endif
endif

# APP_FILE = app
APP_FILE = app_gui

APP_NAME = yt-dpl-qt6

ENTRY_POINT = ./src/$(APP_FILE).py

all:

pyui:
	pyuic6 -o ./src/qt/py_ui/main_window.py \
	       -x ./src/qt/ui/main_window.ui

build:
	pyinstaller --workpath ./.pyinstaller/build \
	            --distpath ./bin --specpath ./.pyinstaller \
				--noconsole --onefile \
				--name $(APP_NAME) \
				$(ENTRY_POINT)

run:
	./bin/$(APP_NAME)

runpy: pyui
	$(PYTHON) $(ENTRY_POINT)

clean:
	$(RM) $(call FixPath,./bin/*)
	$(RM) $(call FixPath,./.pyinstaller/*)