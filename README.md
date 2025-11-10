## Assignment 7: Kubernetes Autoscaling and Performance Testing

### Objective

This assignment builds upon the existing Continuous Deployment (CD) pipeline from Week 6. The goal is to prove the scalability and stability of the IRIS Classification API on Google Kubernetes Engine (GKE) under heavy load, using the `wrk` stress testing utility and the Horizontal Pod Autoscaler (HPA).

We demonstrate two core scenarios:
1.  **Scaling:** HPA successfully scales the application up (e.g., to 3 Pods) to handle high concurrency.
2.  **Bottleneck:** Restricting the HPA to 1 Pod to observe resource exhaustion, high latency, and request failures.

### Repository File Structure

The project structure is organized for clear separation of application code, Docker configuration, Kubernetes manifests, and the GitHub workflow.  
/  
├── .github/  
│   └── workflows/  
│       └── cd-pipeline.yml   <-- The automation script  
├── k8s/  
│   ├── deployment.yaml       <-- Kubernetes Deployment with Resource Limits  
│   ├── service.yaml          <-- Kubernetes Service (LoadBalancer)  
│   └── hpa.yaml              <-- Horizontal Pod Autoscaler definition  
├── iris_fastapi.py           <-- FastAPI application code  
├── requirements.txt          <-- Python dependencies  
├── model.joblib              <-- Trained IRIS ML model  
└── Dockerfile                <-- Container image blueprint  

### File Utility Explanation

| File Name | Utility/Objective |
| :--- | :--- |
| **`iris_fastapi.py`** | The core application code. It defines the `/` (root) endpoint and the primary `/predict/` POST endpoint, which loads `model.joblib` and performs inference. |
| **`model.joblib`** | The serialized (trained) K-Nearest Neighbors machine learning model for Iris classification. It is copied into the Docker image for runtime predictions. |
| **`requirements.txt`** | Lists all Python package dependencies required to run the IRIS API (`fastapi`, `uvicorn`, `scikit-learn`, `joblib`, `pandas`). |
| **`Dockerfile`** | Defines the container image build process: sets the base image, copies all necessary files, installs dependencies, exposes port `8200`, and runs the application using `uvicorn`. |
| **`.github/workflows/cd-pipeline.yml`** | **The CI/CD Brain.** This file automates the entire process: Authenticates to GCP, builds the Docker image, pushes it to Google Artifact Registry, applies all Kubernetes manifests (including **HPA**), retrieves the LoadBalancer IP, installs **`wrk`**, and runs the high-concurrency stress test against the `/predict/` endpoint. |
| **`k8s/deployment.yaml`** | Defines the desired state for the application Pods. **Crucially for A7, it includes `resources.requests` and `resources.limits`** which HPA uses to measure CPU load and scale the application accordingly. |
| **`k8s/service.yaml`** | Creates a **LoadBalancer** Service in GKE, assigning a public IP address to route external traffic to the application Pods. |
| **`k8s/hpa.yaml`** | **The Autoscaling Rule.** Defines the Horizontal Pod Autoscaler object. It targets the Deployment and instructs Kubernetes to scale the Pods between a set minimum and maximum based on CPU usage. |
