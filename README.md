# Rubik3D

<img src="/gitimages/miniature.png" alt="Project Overview" width="100%">

## Overview

This project is focused on creating a program that solves Rubik's Cubes using the fewest possible spins.

**Available here :** [Rubik](https://rubik3d.netlify.app)

## Try the Project - WebApp

### 1. Install Docker

To run this project, the first step is to install [Docker](https://docs.docker.com/engine/install/) on your machine. Docker simplifies deployment by providing an isolated environment for your application.

### 2. Install Make (Optional)

This project includes a Makefile, which allows you to execute Docker commands more easily, without having to type them manually. While using `make` is optional, it is highly recommended to simplify operations. You can install `make` by following [this link](https://www.gnu.org/software/make/#download) or by searching for installation instructions specific to your system.

### 3. Run the WebApp

#### With Make

Run this command in your terminal:

```bash
make
```
This will display:

<img src="/gitimages/make_output.png" width="75%">
Next, run this to start the web application:

```bash
make run
```
#### Without Make

If you prefer not to use `make`, you can start the web application by running the following command:

```bash
docker-compose -f docker-compose.yml build
docker-compose -f docker-compose.yml up -d

```
## Try the Project - Script Only

**Navigate to the Project Folder**

You can access the project folder by using [this link](https://github.com/DevJ2K/app_rubik/tree/main/backend/rubik).

<!-- ## Todo-list
- [ ] Update current and project README.md.
- [x] Change colors Host link in display_project
- [x] Download project link?
- [x] Computorv1 -> Project_name in frontend/app/.../HomeView.vue
- [x] Use Args in Dockerfile
- [x] Add colors to Makefile -->
