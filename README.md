"#Random Hyper Car"

The docker build command is quite simple - it takes an optional tag name with -t and a location of the directory containing the Dockerfile.

```
docker build -t gauravshindolkar/hypercar


```

To run the image

```
docker run -p 8888:5000 gauravshindolkar/hypercar


```