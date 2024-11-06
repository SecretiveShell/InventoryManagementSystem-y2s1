# Important system considerations

## Reliability

### pros

- the system can be used more
- downtime is costly
- if our service is unreliable we loose customers

### cons

- complexity (postgres raft consensus)

## scalability

### pros

- statelessness allows for scalability
- reliability through replicas

### cons

- complexity (required statelessness, redis)

## performance

### pros

- the website loads faster
- lower cart abandonment

### cons

- no time to make coffee

## security

### pros

- no fines
- regulation compliance
- safety of the system
- better reliability

## maintainability

### pros

- cheap to run
- faster development times
- more agile
- less downtime

## how we addressed these in our application:

We chose to address reliability by separating the database into an external server. This allows us to have faults in the API server without impacting data reliability. This also has the advantage of making the API server stateless and thus also allows us to scale better. To manage the API tokens we are using a shared redis instance to persist data across user sessions. This also boosts performance by ensuring that API keys are stored in ram and not on disk.

To address security, we will make sure to use pydantic secret string types where passwords are stored in ram, and then hash them in the database. We will use cryptographically secure PRNG to make sure that we do not create insecure tokens, and tokens will expire after 30 minutes.

To improve maintainability we have a dev container config to enable us to create ephemeral environments on the fly for both development and testing. We will also add comments to the code and maintain internal documentation along side the program.
