Schumacher e Hall (1933)

$$
\ln{C} = \beta_0 + \beta_1 \ln{DAP} + \beta_2 \ln{H_t}
$$

```
beta0 = -0.906586 
beta1 = 1.60421 
beta2 = 0.37162
```

# Habitas

## To initialize the project on Windows:

1. Download [python](https://www.python.org/downloads/).
2. Open cmd and run command ```pip3 install virtualenv```.

#### Inside project's root directory:

3. Run command ```python -m venv env``` to create a virtual environment for the project. Please do not forget adding *env* folder inside .gitignore!
4. Activate virtual environment running command ```env\Scripts\activate```.
5. Install project dependencies running commmand ```pip3 install -r requirements.txt```.
6. Run command ```python .\habitas\manage.py runserver``` to run app.
7. You're good to go!
