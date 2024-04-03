This folder contains the following scripts, used to populate the dataset:
- scrape: Reads a source.pdf file, scans for text coordinates, uses them to create a data_raw.json file.
- clean: Reads a data_raw.json file, converts the coordinates from the AutoCAD format to a more manageable web standard (either px or rem, currently rem). Saves the result in a data.json file.
- build: Reads a data.json file and uses it to create a result.html file with the text element placed absolutely.

## Run order
The files should be ran in the same order they are listed. They were used to create the existing datasets in the repo, it should not be necessary to run them again.