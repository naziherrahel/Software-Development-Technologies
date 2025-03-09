# Lab 03: CI/CD for an AI Model Project with GitHub Actions & GitHub Pages

## Overview

In this lab, you will set up a Continuous Integration (CI) and Continuous Deployment (CD) pipeline for an AI project. You will:

- **Train a Random Forest classifier** on the Iris dataset.
- **Generate dynamic reports** (including a confusion matrix and accuracy metric).
- **Run tests** to verify the model’s performance.
- **Automatically update an HTML report** with the latest metrics.
- **Deploy the updated report** using GitHub Pages.

**Important:**  
- **Do not clone this repository.** Use it only as a reference.
- Manually create the project files on your local machine by copying the code from the links below.
- Once your local project is ready, push it to your own GitHub repository, then configure GitHub Actions and GitHub Pages.

---

## Learning Outcomes

After completing this lab, you will be able to:

- Organize a project using industry-standard structures.
- Set up GitHub Actions for automated training, testing, and report updating.
- Deploy a dynamic report using GitHub Pages.
- Integrate AI model workflows with CI/CD pipelines.
- Push your local project to your own GitHub repository and configure it for CI/CD.

---

## Repository Structure (Reference)

Your final project should have a structure similar to this:

ai-lab-gh-actions/
├── .github/
│   └── workflows/
│       ├── ci.yml         # CI pipeline: training, testing, and updating the report
│       └── deploy.yml     # Deployment pipeline: publishing the report to GitHub Pages
├── docs/
│   └── index.html       # HTML report template (includes a placeholder for dynamic metrics)
├── src/
│   ├── model.py         # Script for training the model and generating outputs
│   └── test_model.py    # Tests to verify model performance
├── requirements.txt     # Project dependencies
└── assets/              # (Optional) Folder for intermediate output files


*Note:* The `docs` folder is used by GitHub Pages to serve your live report.

---

## File References

Please use the following links as your source code reference. Click each link to view the code, then copy its contents into the corresponding file in your local project.

- **[requirements.txt](./requirements.txt)**  
  Contains the project dependencies.

- **[CI Workflow File: .github/workflows/ci.yml](./ci.yml)**  
  Handles model training, testing, and report updating.

- **[Deploy Workflow File: .github/workflows/deploy.yml](./deploy.yml)**  
  Deploys the content of the `docs` folder to GitHub Pages.

- **[Model Training Script: src/model.py](./model.py)**  
  Trains the model on the Iris dataset, generates outputs (confusion matrix and metrics), and saves them.

- **[Test Script: src/test_model.py](./test_model.py)**  
  Contains tests to ensure that the model meets the performance threshold.

- **[HTML Report Template: docs/index.html](./index.html)**  
  The report template that includes a placeholder ({{accuracy}}) for dynamic metric updates.

---

## Instructions

### 1. Set Up Your Local Project

1. **Create a New Local Repository:**
   - Create a folder on your machine (e.g., `ai-lab-gh-actions`).
   - Inside that folder, manually create the following directories:
     - `.github/workflows`
     - `docs`
     - `src`
     - `assets` (optional; your script may create it automatically)

2. **Create the Files:**
   - Open each link above, copy the code, and paste it into a new file with the corresponding name and location in your local repository.
   - For example, copy the contents from [requirements.txt](./requirements.txt) into a file named `requirements.txt` at the root of your project.

### 2. Push Your Local Project to Your GitHub Repository

1. **Initialize Git in Your Local Project (if not already done):**
   ```bash
   git init
   git add .
   git commit -m "Initial commit for Lab 03"

```
Create a New Repository on GitHub:

Create a new repository under your GitHub account.
Add the Remote and Push Your Changes:

    ```bash
    git remote add origin https://github.com/<your-username>/<your-repo-name>.git
    git push -u origin main 

Important: You must push your local project to your own GitHub repository. The repository in this lab is only for reference.

### 3. Configure GitHub Actions and GitHub Pages

GitHub Actions:

Once you push your repository, GitHub Actions will trigger the CI pipeline defined in .github/workflows/ci.yml.
Check the Actions tab in your repository to ensure the pipeline runs successfully. This pipeline trains the model, runs tests, updates the HTML report, and commits the changes.

**GitHub Pages:**

In your GitHub repository, go to Settings > Pages.
Under Source, select the main branch and set the folder to /docs.
Save your settings.
Your live report will be available at:

    ```bash 
    https://<your-username>.github.io/<your-repo-name>/

**Lab Submission** 

Submit a document that includes:

Your GitHub Repository URL:
The URL of your repository where your Lab 03 project is hosted.
Screenshots:
A screenshot of a successful GitHub Actions run (from the Actions tab).
A screenshot of your live GitHub Pages site.
Documentation:
A brief explanation of your project structure.
A description of how you set up GitHub Actions and GitHub Pages.
Any challenges you encountered and how you resolved them.
Final Notes
Manual Setup:
Use the file links above as your code source. Copy the contents from each file link into the corresponding file in your local project.

Industry Standards:
This lab simulates real-world CI/CD pipelines and automated deployment practices for AI projects.

Assistance:
If you encounter any issues, refer to this README or contact your instructor for help.

Happy coding and good luck with Lab 03!



---

This `README.md` file provides all the lab instructions and links to the code files. Students can cl

```