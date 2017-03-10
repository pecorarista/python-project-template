author  = "Miyazawa Akira"
project = "nyan"
version = "0.1"

docroot = "docs"
docconf = "$(docroot)/source/conf.py"

python  = $(shell python -V 2>&1 | sed -e 's@python\s\+\([23]\).*@\1@i')

.PHONY: test
test:
	@python -m unittest -v

.PHONY: install
install:
	@pip install -e . --ignore-installed

.PHONY: uninstall
uninstall:
	@pip uninstall $(project) -y || true

.PHONY: doc
doc: docs/Makefile docs/build/html/index.html

docs/Makefile:
	@sphinx-quickstart \
	--quiet \
	--sep \
	-v $(version) \
	--project $(project) \
	--author=$(author) \
	--ext-autodoc \
	--makefile \
	--no-batchfile \
	docs
	@sed -i -e 's@^\s*#\s*import os\s*@import os@' $(docconf)
	@sed -i -e 's@^\s*#\s*import sys\s*@import sys@' $(docconf)
	@sed -i -e \
		"s@^\s*#\s*sys\.path\.insert(0,\s*os\.path\.abspath('\.'))@sys.path.insert(0, os.path.abspath('../..'))@" \
		$(docconf)
	@sed -i -e "s@^[\s#]*extensions\s*=.*\]@extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon']@" \
		$(docconf)

docs/build/html/index.html:
	$(MAKE) -C $(docroot) html

.PHONY: clean
clean:
	@if [ -d docs ]; \
	then \
		$(MAKE) -C $(docroot) clean; \
	fi

.PHONY: preview
preview: docs/build/html/index.html
	@cd $(docroot)/build/html; \
		if [ $(python) = "3" ]; \
		then \
			python -m http.server; \
		else \
			python -m SimpleHTTPServer; \
		fi
