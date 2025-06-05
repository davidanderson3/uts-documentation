# UMLS API Documentation

This site is built using [JBake](https://jbake.org/), a static site generator for developers.

## Build and Preview Locally 


### Download JBake

Obtain the JBake `.zip` release from:

👉 https://jbake.org/download.html

Extract it to a directory of your choosing (note the directory for JBAKE_PATH below)

---

### Build the Site

Open Git Bash and go to your project folder:

```bash
cd YOUR_PATH/uts-documentation/src/gov/nih/nlm/lo/umls/uts/documentation
/c/JBAKE_PATH/jbake/bin/jbake -b
```

---

### Preview the Site

```bash
cd output
python -m http.server 8000
```

Then open your browser and visit:

```
http://localhost:8000/rest/home.html
```

