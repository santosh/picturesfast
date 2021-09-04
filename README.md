# santosh.pictures

<santosh.pictures> is a photo management application originally written in Go, but ported to FastAPI in early stage. It uses Postgres for storing metadata of the images and the application's own data.

## Stack

- FastAPI backend.
- Application is planned to run as a microservice with help of docker and aws. 
- The database server also runs on the same host.
- Traefik - TODO: Let's Encrypt

## Development

* Don't be confused with pydantic models and sqlalchemy models. pydantic models are used for parsing and validation of upstream data/request.

## Metadata

This project is a part of application I developed during AWS Certified Developer Assciate Exam. 

Strategies for application growth:

- Deploy manually on EC2
- Try deploying it on Elastic Beanstalk and have it scale
- Try createing a CICD pipeline for it
- Try decoupling components sub/pub architecture.
- If possible, try running it on AWS Lambda & friends
- Write automation scripts using the CLI / SDK
    - Idea 1: Shut down EC2 instances at night / start in the morning
    - Idea 2: Automate snapshots of EBS volumes at night
    - Idea 3: List all under-utilized EC2 instances (CPU Utilization < 10%)
