# santosh.pictures

<santosh.pictures> is a photo management application originally written in Go, but ported to FastAPI in early stage. It uses Postgres for storing metadata of the images and the application's own data.

## Stack

- FastAPI backend.
- Microservices architecture with Bealstalk as platform.
- Database runs on different container in same beanstalk environment.
- Traefik - TODO: Let's Encrypt

## Development

* We use `tiangolo/sqlmodel` for both validation and data modeling. `sqlmodel` brings pydantic and SQLAlchemy together.

## Metadata

This project is a part of application I developed during AWS Certified Developer Assciate Exam. 

Strategies for application growth:

- Deploy it on Elastic Beanstalk and have it scale
- Try decoupling components sub/pub architecture.
