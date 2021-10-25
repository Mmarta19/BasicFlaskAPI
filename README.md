### HOW TO EXECUTE THE PYTHON PART:
1. Build the api:
    ````
    docker-compose build api`
    ````

2. Start the api
    ```
    docker-compose up api
    ```

3. Execute the test (using pytest) 
    ```
    docker-compose run --rm api bash -c "pytest -vv tests/"
    ```
 
 