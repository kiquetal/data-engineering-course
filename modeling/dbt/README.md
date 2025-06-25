# dbt Project Bootstrap Guide

## Index

1. [Create and Activate Python Virtual Environment (Optional)](#1-create-and-activate-python-virtual-environment-optional)
2. [Install dbt-postgres (Optional)](#2-install-dbt-postgres-optional)
3. [Initialize dbt Project](#3-initialize-dbt-project)
4. [Configure dbt Profile for PostgreSQL](#4-configure-dbt-profile-for-postgresql)
5. [Run dbt](#5-run-dbt)
6. [Run with Docker Compose (Recommended)](#6-run-with-docker-compose-recommended)

This guide will help you set up a dbt project using Docker Compose for both dbt and PostgreSQL, or optionally with a local Python environment.

## 1. Create and Activate Python Virtual Environment (Optional)

```bash
python3 -m venv venv
source venv/bin/activate
```

## 2. Install dbt-postgres (Optional)

```bash
pip install dbt-postgres
```

## 3. Initialize dbt Project

```bash
dbt init my_dbt_project
```

## 4. Configure dbt Profile for PostgreSQL

Create a `profiles` directory in your project root and add a `profiles.yml` file with your PostgreSQL credentials:

```yaml
my_dbt_project:
  target: dev
  outputs:
    dev:
      type: postgres
      host: postgres
      user: dbt_user
      password: dbt_pass
      port: 5432
      dbname: dbt_db
      schema: public
      threads: 1
      keepalives_idle: 0
      connect_timeout: 10
```

## 5. Run dbt

If using your local environment:
```bash
dbt run
```

## 6. Run with Docker Compose (Recommended)

1. Start the services:
   ```bash
   docker-compose up -d
   ```
2. Enter the dbt container:
   ```bash
   docker-compose exec dbt bash
   ```
3. Run dbt commands inside the container:
   ```bash
   dbt run
   dbt test
   dbt compile
   ```

> **Note:**
> - The dbt container uses the `profiles` directory for configuration. Make sure your `profiles.yml` is present in `./profiles`.
> - Project files are mounted into the container for live development.

---

For more, see the [dbt documentation](https://docs.getdbt.com/docs/introduction).
