# end-to-end-ml-projects

## Workflows

1. Update config.yaml -- Done
2. Update schema.yaml
3. Update params.yaml
4. Update the entity -- Done
5. Update the configuration manager in src config -- Done
6. Update the components -- Done
7. Update the pipeline -- 
8. Update the main.py
9. Update the app.py



# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/shihabict/end-to-end-ml-projects.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
python3 -m venv mlproj
```

```bash
source mlproj/bin/activate
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```



## MLflow

[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/shihabict/end-to-end-ml-projects.mlflow \
MLFLOW_TRACKING_USERNAME=shihabict \
MLFLOW_TRACKING_PASSWORD=f907faf39a83b9389a2a1c7bb5492420e048949a \
python script.py
Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/shihabict/end-to-end-ml-projects.mlflow

export MLFLOW_TRACKING_USERNAME=shihabict 

export MLFLOW_TRACKING_PASSWORD=f907faf39a83b9389a2a1c7bb5492420e048949a

```