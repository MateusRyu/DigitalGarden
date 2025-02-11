---
created_at: 2025-01-30T22:12:02-03:00
updated_at: 2025-01-27T20:46:41-03:00
---
Quartz comes shipped with a Docker image that will allow you to preview your Quartz locally without installing Node.

You can run the below one-liner to run Quartz in Docker.

```sh
docker run --rm -itp 8080:8080 $(docker build -q .)
```
