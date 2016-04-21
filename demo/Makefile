

TPP = pandoc-tpp

all: out/default.html5 out/demo.html

out/default.html5: templates/default.html5 \
                   templates/head.html5 \
                   templates/meta.html5
	@if [ ! -d $(dir $@) ]; then mkdir -p $(dir $@); fi
	$(TPP) $< > $@

out/demo.html: demo.md out/default.html5
	pandoc $< --template $(shell $(TPP) -t templates/default.html5) -o $@

.PHONY: clean

clean:
	rm -rf out
