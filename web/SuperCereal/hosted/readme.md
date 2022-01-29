# Super Cereal

## Instructions for hosting

1. There's a `start.sh` script you can run that will simply call the correct docker build and run commands.
2. Alternatively you can do this manually:

```bash
docker build . -t web-supercereal
docker run -p 8990:8990 -t web-supercereal
```
The port `8990` is used for this. If this changes, let me know. 
