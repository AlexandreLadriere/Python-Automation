# Useful Python Scripts

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/f3aaee8fe0904ee899c97808dc1e6f53)](https://www.codacy.com/manual/alexandre.ladriere77/Useful-Python-Scripts?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=AlexandreLadriere/Useful-Python-Scripts&amp;utm_campaign=Badge_Grade)
[![GitHub license](https://img.shields.io/github/license/AlexandreLadriere/Useful-Python-Scripts.svg)](https://github.com/AlexandreLadriere/Useful-Python-Scripts/blob/master/LICENSE)

Set of python scripts useful in everyday life (e.g. sorting files in a folder)

## Scripts
### Desktop Cleaner
This script will clean the given folder by moving all files to a new folder corresponding to its type. For example, if you have the following folder:
```
├── FolderTest
│    ├── image.png
│    ├── text.txt
│    ├── AES.cpp
│    ├── RSA.kt
│    ├── file_without_ext
│    └── sub_folder
```

Then, after running this script on this folder, you will get the following structure:

```
├── FolderTest
│    ├── IMAGE
│    │    └── image.png
│    ├── PROG
│    │    ├── AES.cpp
│    │    └── RSA.kt
│    └── OTHER
│         ├── file_without_ext
│         └── sub_folder
```

The list of all the extensions supported are in the [file_ext.py] file. 

To use the script:
```sh
$ python3 <path_to_script> #It will run the script, then follow instructions
```

## License
This project is licensed under the MIT License - see the [LICENSE] file for details.

## Contributing
Contributions are welcome :smile:

### Pull requests
Just a few guidelines:
-   Write clean code with appropriate comments and add suitable error handling.
-   Test the application and make sure no bugs/ issues come up.
-   Open a pull request and I will be happy to acknowledge your contribution after some checking from my side.

### Issues
If you find any bugs/issues, raise an issue.

  [LICENSE]: <LICENSE>
  [file_ext.py]: <./Desktop_cleaner/file_ext.py>