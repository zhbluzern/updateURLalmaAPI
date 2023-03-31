# updateURLalmaAPI

This project contains two Jupyter notebooks with python scripts:

### GetNetworkID_byXLS

Creates the input file by getting the NZ id from SRU. This script does not need to be run again. Result of this script is file SoSaGraphics_ARK_MMSIDs_20230310.json

### Update bib records via Alma API: updateARK

update several bib records through the alma api:
- replace the url in field 856$u 
- create field 024 with ark id
- create field 506 and 540 with license information

The script reads an input file and loops through the list of ID-URL pairs. It downloads the bib record in marcxml, finds the 856 field, updates the url, adds field 024, 506 and 540 and uploads the new bib record. This script assumes there is only one field 856 $$u.

*To run this script, do the following:*

Check and adapt the input file path (line 11ff.): 

- test file sosatest01.json contains 1 record
- test file sosatest10.json contains 10 records
- the full list of records is in file named 'SoSaGraphics_ARK_MMSIDs.json' 

Write your Alma API key in a file named config.py in the same folder as your script. The file should look like this:

(This file is under .gitignore, the API keys are not publicly shared)

```
api_key_nz = "NZ_API_KEY"

```
This script assumes that field 856 contains the old links to the Sosa graphics (edoc.zhbluzern.ch) and can be overwritten (which is true for these ca. 2300 titles, but may have to be checked for another purpose).

## Remove a certain field

```python
    # Remove all 024 matching Subfield a with the given ARK
    
    '''
    marc_024 = marcxml.findall(".//datafield[@tag='506']")
    print(bib['ARK'])
    for field in marc_024:
        subfield_a = field.find(".//subfield[@code='a']")
        subfield_u = field.find(".//subfield[@code='u']")
        subfield_2 = field.find(".//subfield[@code='2']")
        print(subfield_a.text)
        print(subfield_2.text)
        #if subfield_a.text == bib["ARK"] and subfield_2.text == "ark":
        #    print("match ARK")
        field.remove(subfield_a)
        field.remove(subfield_u)
        field.remove(subfield_2)
    '''
```