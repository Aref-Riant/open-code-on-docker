# open-code-on-docker
docker project for open coder on CPU

## Build:
To build the docker image:  
`docker build -t opencoder:cpu .`


## Run:
```
docker run --cpus 8 --rm opencoder:cpu python3 "write a java script code that adds a circle to users mouse cursor"
```

