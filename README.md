# CTF challenges


Once your challenge is ready for testing, organize it into the following format
```
/category/challenge-name/
  - readme.md 
  - challenge-description.md
  - players/ (files given to players)
  - hosted/  (files required for hosting)
      - readme.md (instructions for hosting, hopefully just docker run)
      - start.sh (or something similar, again hopefully just docker run)
  - solve/   (solve scripts)
```
