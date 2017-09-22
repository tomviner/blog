Add submodules and connect up reveal.js folder. This presents the slides at a reasonable URL path.

```bash
REPO = "exploring-unittesting-talk"
git submodule add -b master "git@github.com:tomviner/$REPO.git" "content/talks/$REPO-repo"

ln -s "$(readlink -f content/talks/$REPO-repo/reveal.js/)" "content/talks/$REPO"

echo "[View slides](/talks/$REPO/)"
```

The Makefile contains:

    # http://stackoverflow.com/a/9189815/15890
    update_submodules:
        git submodule init
        git submodule update --remote

So to update talks (and pelican plugins):

    make update_submodules
