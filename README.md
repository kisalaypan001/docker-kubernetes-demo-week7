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
