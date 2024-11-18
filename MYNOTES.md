# My Notes

This is a project that aims to create a API that can provide nutritional information about food and finally became a food logger app

## Development

This app is developed using python within a docker container (check the `Dockerfile`).

There're two data sources considered to fill this app with information

### FatSecret Api

An actual macro tracker app with an authentication required API that we can use to search for foods an macronutrient info

#### Pros
- An acceptable large food database including foods from multiple regions
- Contains information for non branded/packaged foods such as plain "Jamon Serrano" or "Yogurt Griego"

#### Cons
- Needs authentication. A Client_id + Client_secret are required to authenticate. However this token can be silently refreshed

### Open Food Facts Api

#### Pros
- No authentication required
- An acceptable large food databse with much more detailed information than fatsecret

#### Cons
- Mainly branded/packaged foods can be found
- Since the database is maintained by the people, data cannot be 100% reliable and can sometimes be missing key information

## Roadmap

- [x] Using FatSecret Api search method, develop a connection with silent refresh between the NutritionApp and the FatSecret Api
- [x] Perform search queries by search_term to get food information from the API
- [x] Search for a solution to host the project database:
    - [x] Solution was to use PostgreSQLSQL within docker-compose
    - [x] Also installed PGAdmin to interact with PostgreSQL database
- Develop a Databse Model to support food logging
- Log the first food with their macronutrients
- Calculate the daily calories consumed
