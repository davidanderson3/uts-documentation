# Test UMLS API

This is a basic test suite for the UMLS API with benchmarking. 

## Get MRCONSO, MRDEF, MRREL

Copy the latest MRCONSO.RRF, MRDEF.RRF, and MRREL.RRF to this directory.

## Preprocess candidate identifiers and strings

Run:

```
python preprocess.py 
```
This will identify candidate identifiers and strings that will LIKELY (99.9% chance) return API results.
The script now saves a list of candidate atoms **per endpoint** in `subset/valid_codes.json`.
Each test in `test.py` uses its own list of examples. Processing takes a few minutes.

## Run tests

test.py will choose random examples from each endpoint's preprocessed subset to test
against the API. The examples will be different every time you test.

Run
```
python test.py --apiKey YOUR_API_KEY --env qa --count 20
```

* Add your API key from https://uts.nlm.nih.gov/uts/profile. 
* Choose qa or prod for --env depending on which you want to test. 
* --count determines how many random examples are sent for each test. 5 will be very quick. 1000 will take a while. 

## View Report

Open results.html in your browser. 
