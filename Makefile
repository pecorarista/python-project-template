author  = "Miyazawa Akira"
project = "nyan"
version = "0.1.0"

docroot = "docs"
docconf = "$(docroot)/source/conf.py"
docport = "8888"

python  = $(shell python -c 'from __future__ import print_function; import sys; print(sys.version_info.major)')

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
doc: $(docroot)/Makefile $(docroot)/build/html/index.html

$(docroot)/Makefile:
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

$(docroot)/build/html/index.html:
	$(MAKE) -C $(docroot) html

.PHONY: clean
clean:
	@if [ -d docs ]; \
	then \
		$(MAKE) -C $(docroot) clean; \
	fi

.PHONY: preview
preview: $(docroot)/build/html/index.html
	@cd $(docroot)/build/html; \
		if [ $(python) = "3" ]; \
		then \
			python -m http.server $(port); \
		else \
			python -m SimpleHTTPServer $(port); \
		fi
