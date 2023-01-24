
## Generate gitignore

https://www.toptal.com/developers/gitignore


## Install miniconda

https://docs.conda.io/en/latest/miniconda.html



## Manage conda environment

### Create

```{bash}
conda env create --file environment.yml
```

### Remove

```{bash}
conda env remove -n ds_dev_env
```

## Code formatting

```{bash}
# black -t py38 -l 79 .
black -t py38 -l 79 --check .
```


## Use mypy for type checking

```{bash}
mypy src/demo_package/demo_module/module.py
```


## Use pylint for code quality checking

```{bash}
pylint src
```

## Unittest

```{bash}
pytest .
```