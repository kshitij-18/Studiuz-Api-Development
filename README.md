# Studiuz-Api-Development

### Instructions for inputs:
### Both the Apis have to be given input inside the address bar.

## API 1:
```
url/api1?string=()&number=()
```
url -> host domain like localhost

string=() -> we have to write string (nothing else) which will be equal to the string which we want to enter for e.g string=abrakadabra

number=() -> we have to specify the chunk size for eg. number=8

#### Model URL:
```
localhost:5000/api1?string=abrakadabra&number=8
```
### WARNING: Here string and number should be passed as it is and should not be changed to anything else like string->strings or number->numbers

#### output:
```
{
  "output": "abr akadabra "
}
```

## API2:
```
url/api2?string=()
```
url -> host domain like localhost 

string=() -> we have to write string (nothing else) which will be equal to the string which we want to enter.the string should have comma
separated values as specified in the example of the problem.

### Model URL:
```
localhost:5000/api2?string=1,a,c,b,c,1
```

#### output:
```
{
  "1": 2,
  "a": 1,
  "b": 1,
  "c": 2
}
```
### WARNING: Here string should be passed as it is and should not be changed to anything else like string->strings also string should be strictly comma separated.
