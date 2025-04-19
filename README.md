# Usage

- use `docker-compose` up to run the app
- frontend is hosted at `localhost:5173`
- backend is hosted at `localhost:8001`
- to load data: 
    - import the attached Postman collection
    - Open the Upload file request
    - Use the "file" field in the request body to attach the CSV file (included in the repo)
    - Press Send

#### Existing endpoints
- POST: `upload/` to upload a file
- GET: `surveys/` to get all survey responses
- GET: `surveys/{survey_name}` to get a single survey response
    -   note that this currently expect the full file name uploaded instead of the survey name
- GET: `questions/{question_id}/`



## Components Used

### Backend:
- FastAPI as the API framework
- Pydantic for parsing requests
- SQLAlchemy for talking to database

### Frontend:
- Svelte for frontend framework
- Vite for dev server and hot module swapping

### Other:
- Docker for containerazing everything



# Responses to bonus questions
## Part 1
- For pagination, creating a base schema like <offset, limit> and using that to filter would be a good starting solution.
- For malformed inputs, could expand the mapping solution so it uses larger vocabulary (F, woman, etc. instead of just Female). Could also look into using a lightweight LLM based cleanup solution, but would need to proceed cautiously to not use AI to fill out data that doesn't exist.
- For caching, initially something lightweight like Redis should work well, it would save responses to recent requests and pull them from memory instead of hitting the database. Later on we could pre-analyze the most commonly polled results and pull them from another database that's better suited like MongoDB or GraphQL.

## Part 2
- First easy step would be adding a multi-select dropdown of states, which could be improved with a zipcode and city addition.
- `How might you compare responses over time?`
    - This question is a bit ambiguous, but every created record has a `created_at` so you could easily track trends in results over time.

## Part 3
- Note that I didn't get to writing any Terraform scripts
- CI/CD pipeline is almost always a good idea for a modern application. I'd add steps to clean up code via something like `black`, add testing with something like `pytest`, and most importantly, actually add some database migrations to be able to manage updates in the long term. Could use something like Alembic for this.
- Running low on time so can't draw a full diagram, but ideally when you upload files they should be tossed into a blob store, an async service should be started to process and add them to the database, do any analytics and indexing, while the main app focuses on servicing customers and users to read and visualize data. 

# To-Dos

- Handle database migrations
- Fix CSV file upload handling, currently the file contents get saved into the database. Should use blob storage initially, then an async service should process the file and pull the data into specific objects. This method will bottleneck quite quickly.
- Add question types to properly format and standardize data types
- Expand and make secure the data mapping tools in utils, depending on use case
- Create a visual data mapper, or better yet, research and find an existing framework that provides visual mapping and cleanup tools.
- To help with above, create individual APIs for all the different models we have, so the frontend can more specifically update individual records
- Create a system for fetching nested data optionally, instead of making multiple requests or having to create separate endpoints for nested vs. not
- Redesign UI to be cleaner / take up less space
- Add filters to surveys / frontend to be able to query specific data.

## Known issues
- survey name is taken from the file name, not the "upload_name" passed in
- error handling, especially in the Upload script, is basically nonexistent. that service needs to be broken up and refactored