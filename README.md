# Instructions

## Extraction

If no argument is provided, this will look for the file `submissions.zip` (the zip file downloaded from canvas) and attempt to extract this to a directory with the current date.

### Default

```bash
python3 extract.py
```
### With Argument
```bash
python3 extract.py <NAME_OF_ZIPFILE>
```
If there were errors in extraction, a file `notes.txt` will be created with information. For example, if a student does not submit a tar/zip file, `notes.txt` will contain something like
`<lastNameFirstName><filename>.h` is not a zipfile or tar file


## Compilation

You'll need a filepath to run this:

```bash
python3 compile.py <DIRNAME>
```
This will generate a text file, `results.txt`. Its contents will be the following:
`<lastnamefirstname>,<pass/fail>`

# Todo
+ Currently, the extraction script manually cleans up '__MACOSX' directories that are hidden when a student tars/zips a file. There could be other things uncaught. If there is a trend, please submit a PR that shows this.

+ `compile.py` is relatively slow. Probably could be run in parallel

+ Lots of try/excepts in here. Not the most efficient but it gets the job done. If you want to clean it up and sumbit a PR feel free.



